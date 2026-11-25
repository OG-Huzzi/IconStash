<script lang="ts">
  /**
   * VirtualIconGrid.svelte
   *
   * Windowed row virtualizer powered by `@tanstack/svelte-virtual`.
   * Guarantees <= 180 mounted `[data-icon-tile]` DOM nodes at any scroll position,
   * hydrates visible library chunks on demand via `ChunkLRUCache` (with AbortController
   * cancellation on fast scroll), cleans up `ResizeObserver` on unmount, and drives
   * live color/stroke/size/transform updates purely via CSS custom properties.
   */

  import { untrack } from 'svelte';
  import { createVirtualizer } from '@tanstack/svelte-virtual';
  import { explorerState, type ResolvedIcon } from '../lib/state/explorer.svelte';
  import { previewState, type GridDensity } from '../lib/state/preview.svelte';
  import { inspectorState } from '../lib/state/inspector.svelte';
  import { collectionsState } from '../lib/state/collections.svelte';
  import { LIBRARY_BADGE_SVGS } from '../lib/library-icons';
  import type { LibraryManifestEntry } from '../lib/protocol/types';

  interface Props {
    focusedPos?: number;
    onFocusPos?: (pos: number) => void;
    onSuggestionClick?: (term: string) => void;
    onGridInsetChange?: (insetPx: number) => void;
  }

  let {
    focusedPos = $bindable(-1),
    onFocusPos,
    onSuggestionClick,
    onGridInsetChange,
  }: Props = $props();

  const MAX_MOUNTED_TILES = 180;
  const GRID_GAP = 8;
  const HEADER_BANNER_HEIGHT = 58;
  const HEADER_ROW_HEIGHT = HEADER_BANNER_HEIGHT + GRID_GAP;
  const SUGGESTION_CHIPS = ['camera', 'arrow', 'user', 'chart', 'download', 'lock'] as const;

  const DENSITY_METRICS: Record<GridDensity, { cardSize: number; rowHeight: number }> = {
    compact: { cardSize: 60, rowHeight: 68 },
    default: { cardSize: 80, rowHeight: 88 },
    comfortable: { cardSize: 100, rowHeight: 118 },
  };

  interface LibraryGridSection {
    lib: LibraryManifestEntry | null;
    startPos: number;
    count: number;
    showHeader: boolean;
    startRow: number;
    rowCount: number;
  }

  type VirtualGridRow =
    | { type: 'header'; lib: LibraryManifestEntry; count: number; key: string }
    | { type: 'cards'; startPos: number; count: number; key: string };

  let scrollContainerEl = $state<HTMLDivElement | null>(null);
  let containerWidth = $state(960);
  let containerHeight = $state(680);

  const baseMetrics = $derived(DENSITY_METRICS[previewState.density] ?? DENSITY_METRICS.compact);
  const metrics = $derived.by(() => {
    const g = previewState.gridSize;
    const cardSize = Math.max(baseMetrics.cardSize, g + 28);
    const extraH = previewState.density === 'comfortable' ? 30 : 8;
    const rowHeight = Math.max(baseMetrics.rowHeight, cardSize + extraH);
    return { cardSize, rowHeight };
  });
  const columns = $derived(
    Math.max(1, Math.floor((containerWidth + GRID_GAP) / (metrics.cardSize + GRID_GAP))),
  );

  function findLibraryIdForIndex(
    iconIndex: number,
    libraries: LibraryManifestEntry[],
    hintId: number,
  ): number {
    if (hintId >= 0 && hintId < libraries.length) {
      const hintLib = libraries[hintId];
      if (iconIndex >= hintLib.startIndex && iconIndex <= hintLib.endIndex) {
        return hintId;
      }
      if (hintId + 1 < libraries.length) {
        const nextLib = libraries[hintId + 1];
        if (iconIndex >= nextLib.startIndex && iconIndex <= nextLib.endIndex) {
          return hintId + 1;
        }
      }
    }
    let lo = 0;
    let hi = libraries.length - 1;
    while (lo <= hi) {
      const mid = (lo + hi) >> 1;
      const lib = libraries[mid];
      if (iconIndex < lib.startIndex) {
        hi = mid - 1;
      } else if (iconIndex > lib.endIndex) {
        lo = mid + 1;
      } else {
        return mid;
      }
    }
    return 0;
  }

  const groupedOrder = $derived.by(() => {
    const indices = explorerState.resultIndices;
    const manifest = explorerState.manifest;
    const total = indices.length;
    const groupByLibrary =
      Boolean(manifest) &&
      (explorerState.sort === 'relevance' || explorerState.sort === 'library');

    if (!groupByLibrary || !manifest || total === 0) {
      return {
        orderedIndices: indices,
        groups:
          total > 0
            ? [{ lib: null as LibraryManifestEntry | null, startPos: 0, count: total, showHeader: false }]
            : ([] as { lib: LibraryManifestEntry | null; startPos: number; count: number; showHeader: boolean }[]),
      };
    }

    const libs = manifest.libraries;
    const libCount = libs.length;
    const counts = new Int32Array(libCount);
    let hintId = 0;
    let maxLibSeen = -1;
    let monotonic = true;

    for (let i = 0; i < total; i++) {
      const libId = findLibraryIdForIndex(indices[i], libs, hintId);
      hintId = libId;
      if (libId < maxLibSeen) {
        monotonic = false;
      } else {
        maxLibSeen = libId;
      }
      counts[libId]++;
    }

    let orderedIndices: Uint32Array;
    if (monotonic) {
      orderedIndices = indices;
    } else {
      orderedIndices = new Uint32Array(total);
      const cursors = new Int32Array(libCount);
      let offset = 0;
      for (let l = 0; l < libCount; l++) {
        cursors[l] = offset;
        offset += counts[l];
      }
      hintId = 0;
      for (let i = 0; i < total; i++) {
        const idx = indices[i];
        const libId = findLibraryIdForIndex(idx, libs, hintId);
        hintId = libId;
        orderedIndices[cursors[libId]++] = idx;
      }
    }

    const groups: { lib: LibraryManifestEntry; startPos: number; count: number; showHeader: boolean }[] = [];
    let pos = 0;
    for (let l = 0; l < libCount; l++) {
      const count = counts[l];
      if (count > 0) {
        groups.push({ lib: libs[l], startPos: pos, count, showHeader: true });
        pos += count;
      }
    }

    return { orderedIndices, groups };
  });

  const layoutModel = $derived.by(() => {
    const cols = columns;
    const sections: LibraryGridSection[] = [];
    let currentRow = 0;
    let sigParts = '';

    for (const g of groupedOrder.groups) {
      const cardRows = Math.ceil(g.count / cols);
      const rowCount = (g.showHeader ? 1 : 0) + cardRows;
      sections.push({
        lib: g.lib,
        startPos: g.startPos,
        count: g.count,
        showHeader: g.showHeader,
        startRow: currentRow,
        rowCount,
      });
      sigParts += `${g.lib?.id ?? 'flat'}:${currentRow}:${rowCount}|`;
      currentRow += rowCount;
    }

    return {
      sections,
      totalRowCount: currentRow,
      signature: `${sigParts}${metrics.rowHeight}`,
    };
  });

  function getRowAt(rowIndex: number, sections: LibraryGridSection[] = layoutModel.sections, cols: number = columns): VirtualGridRow | null {
    if (rowIndex < 0 || sections.length === 0) return null;

    let lo = 0;
    let hi = sections.length - 1;
    let found = 0;
    while (lo <= hi) {
      const mid = (lo + hi) >> 1;
      if (sections[mid].startRow <= rowIndex) {
        found = mid;
        lo = mid + 1;
      } else {
        hi = mid - 1;
      }
    }

    const sec = sections[found];
    const localRow = rowIndex - sec.startRow;
    if (localRow < 0 || localRow >= sec.rowCount) return null;

    if (sec.showHeader && localRow === 0 && sec.lib) {
      return {
        type: 'header',
        lib: sec.lib,
        count: sec.count,
        key: `hdr-${sec.lib.slug}`,
      };
    }

    const cardRowOffset = sec.showHeader ? localRow - 1 : localRow;
    const startPos = sec.startPos + cardRowOffset * cols;
    const remaining = sec.startPos + sec.count - startPos;
    const count = Math.min(cols, Math.max(0, remaining));
    return {
      type: 'cards',
      startPos,
      count,
      key: `cards-${sec.lib?.slug ?? 'flat'}-${cardRowOffset}`,
    };
  }

  function rowIndexForResultPos(targetPos: number): number {
    const sections = layoutModel.sections;
    if (sections.length === 0) return 0;
    let lo = 0;
    let hi = sections.length - 1;
    let found = 0;
    while (lo <= hi) {
      const mid = (lo + hi) >> 1;
      if (sections[mid].startPos <= targetPos) {
        found = mid;
        lo = mid + 1;
      } else {
        hi = mid - 1;
      }
    }
    const sec = sections[found];
    const cardRow = Math.floor(Math.max(0, targetPos - sec.startPos) / columns);
    return sec.startRow + (sec.showHeader ? 1 : 0) + cardRow;
  }

  const totalMatches = $derived(groupedOrder.orderedIndices.length);
  const rowCount = $derived(layoutModel.totalRowCount);

  // Hard mathematical cap so mounted `[data-icon-tile]` count NEVER exceeds 180
  const maxMountedRows = $derived(Math.max(1, Math.floor(MAX_MOUNTED_TILES / columns)));
  const visibleRowEstimate = $derived(Math.max(1, Math.ceil(containerHeight / metrics.rowHeight)));
  const effectiveOverscan = $derived(
    Math.min(2, Math.max(0, Math.floor((maxMountedRows - visibleRowEstimate) / 2))),
  );

  const rowVirtualizer = createVirtualizer<HTMLDivElement, HTMLDivElement>({
    count: 0,
    getScrollElement: () => scrollContainerEl,
    estimateSize: () => 88,
    overscan: 2,
  });

  // Keep virtualizer synced when result count, grouped layout, density, or viewport changes
  $effect(() => {
    const count = rowCount;
    const rowHeight = metrics.rowHeight;
    const overscan = effectiveOverscan;
    const el = scrollContainerEl;
    const cols = columns;
    const sections = layoutModel.sections;
    const _sig = layoutModel.signature;

    untrack(() => {
      $rowVirtualizer.setOptions({
        count,
        getScrollElement: () => el,
        getItemKey: (index) => getRowAt(index, sections, cols)?.key ?? index,
        estimateSize: (index) => {
          const row = getRowAt(index, sections, cols);
          return row?.type === 'header' ? HEADER_ROW_HEIGHT : rowHeight;
        },
        overscan,
      });
      $rowVirtualizer.measure();
    });
  });

  // Reset scroll to top when a new search result set arrives
  $effect(() => {
    const _indices = explorerState.resultIndices;
    if (scrollContainerEl && _indices.length >= 0) {
      scrollContainerEl.scrollTop = 0;
    }
  });

  // Observe grid viewport width/height and scrollbar inset with strict teardown on unmount
  $effect(() => {
    const el = scrollContainerEl;
    if (!el || typeof ResizeObserver === 'undefined') return;

    const updateRect = () => {
      const innerW = Math.max(0, el.clientWidth - 4);
      const clientH = el.clientHeight;
      if (innerW > 0) containerWidth = innerW;
      if (clientH > 0) containerHeight = clientH;
      onGridInsetChange?.(Math.max(0, el.offsetWidth - el.clientWidth) + 4);
    };
    updateRect();

    const observer = new ResizeObserver(() => {
      updateRect();
    });
    observer.observe(el);

    return () => {
      observer.disconnect();
    };
  });

  // Attach zero-re-render CSS custom properties to the grid root
  $effect(() => {
    const el = scrollContainerEl;
    if (!el) return;
    previewState.applyCssVars(el);
    return () => {
      previewState.cleanup();
    };
  });

  const virtualRows = $derived.by(() => {
    const items = $rowVirtualizer.getVirtualItems();
    const out: { vRow: (typeof items)[number]; row: VirtualGridRow }[] = [];
    let tileCount = 0;
    for (const vRow of items) {
      const row = getRowAt(vRow.index);
      if (!row) continue;
      if (row.type === 'cards') {
        if (tileCount + row.count > MAX_MOUNTED_TILES && out.length > 0) break;
        tileCount += row.count;
      }
      out.push({ vRow, row });
    }
    return out;
  });
  const totalHeight = $derived($rowVirtualizer.getTotalSize());

  // Hydrate shards required for mounted virtual rows plus a 3-row lookahead.
  // Never attach an abort signal for top-of-grid initial rows (scrollTop === 0) so
  // layout/ResizeObserver updates never cancel the first visible icon chunk and leave skeletons.
  let scrollAbortController: AbortController | null = null;
  let retryTimer: ReturnType<typeof setTimeout> | null = null;
  let retryCount = 0;

  $effect(() => {
    const _indices = explorerState.resultIndices;
    retryCount = 0;
    if (retryTimer !== null) {
      clearTimeout(retryTimer);
      retryTimer = null;
    }
    scrollAbortController?.abort();
    scrollAbortController = null;
    return () => {
      if (retryTimer !== null) {
        clearTimeout(retryTimer);
        retryTimer = null;
      }
      scrollAbortController?.abort();
      scrollAbortController = null;
    };
  });

  $effect(() => {
    const rows = virtualRows;
    const indices = groupedOrder.orderedIndices;
    const manifest = explorerState.manifest;
    const cols = columns;
    const _ver = explorerState.chunkVersion;

    if (!manifest || indices.length === 0 || rows.length === 0) return;

    const needed: number[] = [];
    let maxCardPos = 0;
    for (let r = 0; r < rows.length; r++) {
      const row = rows[r].row;
      if (row.type !== 'cards') continue;
      const startPos = row.startPos;
      const endPos = Math.min(startPos + row.count, indices.length);
      if (endPos > maxCardPos) maxCardPos = endPos;
      for (let pos = startPos; pos < endPos; pos++) {
        const idx = indices[pos];
        if (!untrack(() => explorerState.getIconPayload(idx))) {
          needed.push(idx);
        }
      }
    }

    const prefetchStart = maxCardPos;
    const prefetchEnd = Math.min(indices.length, prefetchStart + cols * 3);
    for (let pos = prefetchStart; pos < prefetchEnd; pos++) {
      const idx = indices[pos];
      if (!untrack(() => explorerState.getIconPayload(idx))) {
        needed.push(idx);
      }
    }

    if (needed.length === 0) {
      retryCount = 0;
      return;
    }

    const isScrolledDown = (scrollContainerEl?.scrollTop ?? 0) > 120;
    let signal: AbortSignal | undefined;
    if (isScrolledDown) {
      scrollAbortController?.abort();
      scrollAbortController = new AbortController();
      signal = scrollAbortController.signal;
    }

    void explorerState.ensureChunksForIndices(needed, signal).then(() => {
      if (signal?.aborted) return;
      const stillMissing = rows.some(({ row }) => {
        if (row.type !== 'cards') return false;
        const s = row.startPos;
        const e = Math.min(s + row.count, indices.length);
        for (let p = s; p < e; p++) {
          if (!explorerState.getIconPayload(indices[p])) return true;
        }
        return false;
      });
      if (stillMissing && retryCount < 2 && retryTimer === null) {
        retryCount++;
        retryTimer = setTimeout(() => {
          retryTimer = null;
          void explorerState.ensureChunksForIndices(needed);
        }, 250 * retryCount);
      }
    });
  });

  function resolveTile(iconIndex: number, _version: number): ResolvedIcon | null {
    return explorerState.getIconPayload(iconIndex);
  }

  function handleTileClick(icon: ResolvedIcon | null, resultPos: number): void {
    focusedPos = resultPos;
    onFocusPos?.(resultPos);
    if (!icon) return;
    if (collectionsState.selectMode) {
      collectionsState.toggleSelect(icon.id);
      return;
    }
    inspectorState.openInspector(icon);
  }

  function handleTileKeydown(event: KeyboardEvent, icon: ResolvedIcon | null, resultPos: number): void {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      handleTileClick(icon, resultPos);
    }
  }

  function handleFavoriteClick(event: MouseEvent, icon: ResolvedIcon | null): void {
    event.stopPropagation();
    if (!icon) return;
    const added = collectionsState.toggleFavorite(icon.id);
    inspectorState.showToast(
      added ? `Saved "${icon.name}" to Favorites` : `Removed "${icon.name}" from Favorites`,
    );
  }

  export function getColumns(): number {
    return columns;
  }

  export function focusResultPosition(targetPos: number): void {
    if (totalMatches === 0) return;
    const clamped = Math.max(0, Math.min(totalMatches - 1, targetPos));
    focusedPos = clamped;
    onFocusPos?.(clamped);

    const targetRow = rowIndexForResultPos(clamped);
    $rowVirtualizer.scrollToIndex(targetRow, { align: 'auto' });

    if (typeof window !== 'undefined') {
      window.requestAnimationFrame(() => {
        const el = scrollContainerEl?.querySelector<HTMLElement>(
          `[data-result-pos="${clamped}"]`,
        );
        el?.focus({ preventScroll: true });
      });
    }
  }
</script>

<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
<div
  id="virtual-grid-container"
  class="ic-grid-root density-{previewState.density}"
  class:select-mode-active={collectionsState.selectMode}
  bind:this={scrollContainerEl}
  tabindex="0"
  aria-label="Icon results"
  style="--ic-size: {previewState.gridSize}px; --ic-tile-size: {metrics.cardSize}px; --card-size: {metrics.cardSize}px; --card-row-height: {metrics.rowHeight}px;"
>
  {#if explorerState.error}
    <div id="library-error-card" class="error-card">
      <div>
        <h2>Search index failed to load</h2>
        <p id="library-error-text">{explorerState.error}</p>
      </div>
      <button
        type="button"
        class="outlined-neon-btn"
        id="library-retry-btn"
        onclick={() => void explorerState.initExplorer()}
      >
        Retry
      </button>
    </div>
  {:else if explorerState.ready && totalMatches === 0}
    <div id="no-results" class="no-results">
      <svg class="no-results-icon" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
        <circle cx="11" cy="11" r="7" />
        <path d="m20 20-4.4-4.4M8.5 8.5l5 5m0-5-5 5" />
      </svg>
      <p id="no-results-text">
        {#if explorerState.query}
          No icons matched "{explorerState.query}". Try a broader term or clear filters.
        {:else}
          No icons match the current filter combination.
        {/if}
      </p>
      <div id="suggestion-chips" class="suggestion-chips">
        {#each SUGGESTION_CHIPS as chip (chip)}
          <button
            type="button"
            class="suggestion-chip"
            onclick={() => {
              explorerState.setQuery(chip);
              onSuggestionClick?.(chip);
            }}
          >
            {chip}
          </button>
        {/each}
      </div>
    </div>
  {:else}
    <div
      id="virtual-grid-stage"
      style="height: {totalHeight}px; width: 100%; position: relative; opacity: 1;"
    >
      {#each virtualRows as { vRow, row } (vRow.key)}
        {#if row.type === 'header'}
          <div
            class="ic-library-row"
            data-row-index={vRow.index}
            style="position: absolute; top: 0; left: 0; width: 100%; height: {HEADER_ROW_HEIGHT}px; transform: translateY({vRow.start}px);"
          >
            <div class="library-break" data-library-break={row.lib.slug}>
              <span class="lib-badge" aria-hidden="true">
                {@html LIBRARY_BADGE_SVGS[row.lib.slug] ?? ''}
              </span>
              <div class="library-break-meta">
                <h2>{row.lib.name}</h2>
                <p>{row.count.toLocaleString('en-US')} icons</p>
              </div>
            </div>
          </div>
        {:else}
          <div
            class="ic-virtual-row"
            data-row-index={vRow.index}
            style="position: absolute; top: 0; left: 0; width: 100%; height: {metrics.rowHeight}px; transform: translateY({vRow.start}px); display: grid; grid-template-columns: repeat({columns}, minmax(0, 1fr)); gap: {GRID_GAP}px; align-items: stretch;"
          >
            {#each { length: row.count } as _, colOffset (row.startPos + colOffset)}
              {@const pos = row.startPos + colOffset}
              {@const iconIndex = groupedOrder.orderedIndices[pos]}
              {@const icon = resolveTile(iconIndex, explorerState.chunkVersion)}
              {@const isFav = icon ? collectionsState.isFavorite(icon.id) : false}
              {@const isSelected = icon ? collectionsState.selectedIds.has(icon.id) : false}
              {@const isActive = icon ? inspectorState.activeIcon?.id === icon.id : false}
              <!-- svelte-ignore a11y_no_noninteractive_element_to_interactive_role -->
              <article
                class="icon-card ic-tile"
                class:active={isActive}
                class:selected={isSelected}
                class:loading-tile={!icon}
                data-icon-tile=""
                data-result-pos={pos}
                data-icon-index={iconIndex}
                data-id={icon?.id ?? ''}
                data-library={icon?.librarySlug ?? ''}
                data-filled={icon ? (icon.isFilled ? 'true' : 'false') : 'false'}
                tabindex="0"
                role="button"
                aria-label={icon ? `${icon.name} from ${icon.libraryName}` : 'Loading icon'}
                aria-pressed={collectionsState.selectMode ? isSelected : isActive}
                title={icon ? `${icon.name} (${icon.libraryName})` : 'Loading...'}
                onclick={() => handleTileClick(icon, pos)}
                onkeydown={(e) => handleTileKeydown(e, icon, pos)}
                onfocus={() => {
                  focusedPos = pos;
                  onFocusPos?.(pos);
                }}
              >
                {#if icon}
                  {#if collectionsState.selectMode}
                    <span class="select-check" class:checked={isSelected} aria-hidden="true">
                      {#if isSelected}✓{/if}
                    </span>
                  {:else}
                    <button
                      type="button"
                      class="card-favorite-btn"
                      class:favorited={isFav}
                      data-favorite-id={icon.id}
                      aria-label={isFav ? `Remove ${icon.name} from Favorites` : `Add ${icon.name} to Favorites`}
                      title={isFav ? 'Remove from Favorites' : 'Add to Favorites'}
                      onclick={(e) => handleFavoriteClick(e, icon)}
                    >
                      <svg viewBox="0 0 24 24" fill={isFav ? 'currentColor' : 'none'} stroke="currentColor" stroke-width="2" aria-hidden="true">
                        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
                      </svg>
                    </button>
                  {/if}

                  <div class="icon-wrap">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox={icon.viewBox}
                      width="100%"
                      height="100%"
                      fill={icon.isFilled ? 'currentColor' : 'none'}
                      stroke={icon.isFilled ? 'none' : 'currentColor'}
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      role="img"
                      aria-hidden="true"
                    >
                      {@html icon.svgBody}
                    </svg>
                  </div>

                  {#if previewState.density === 'comfortable'}
                    <span class="card-name">{icon.name}</span>
                  {/if}
                {:else}
                  <div class="icon-skeleton" aria-hidden="true"></div>
                {/if}
              </article>
            {/each}
          </div>
        {/if}
      {/each}
    </div>
  {/if}
</div>

<style>
  #virtual-grid-container {
    flex: 1 1 auto;
    min-height: 0;
    overflow-y: auto;
    overflow-x: hidden;
    position: relative;
    padding: 0 4px 0 0;
    contain: layout paint;
    overscroll-behavior: contain;
    --ic-color: currentColor;
    --ic-stroke: 1.5;
    --ic-stroke-width: 1.5;
    --ic-rot: 0deg;
    --ic-flip-x: 1;
    --ic-flip-y: 1;
    --ic-blur: 0px;
  }

  .ic-library-row {
    width: 100%;
    box-sizing: border-box;
    padding-bottom: 8px;
  }

  .ic-library-row .library-break {
    width: 100%;
    height: 58px;
    min-height: 58px;
    margin: 0;
    box-sizing: border-box;
    overflow: hidden;
  }

  .library-break-meta {
    min-width: 0;
    overflow: hidden;
  }

  .library-break-meta h2 {
    margin: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .library-break-meta p {
    margin: 2px 0 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .ic-tile {
    color: var(--icon-color, #a1a1aa);
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-radius: var(--radius-card, 8px);
    background: var(--bg-surface, #111111);
    border: 1px solid var(--border, #1f1f1f);
    cursor: pointer;
    user-select: none;
    transition: background-color 120ms ease, border-color 120ms ease;
    min-width: 0;
    overflow: hidden;
  }

  .ic-tile:hover,
  .ic-tile:focus-visible {
    background: var(--bg-hover, #141414);
    border-color: var(--border-hover, #2a2a2a);
    color: var(--icon-strong, #f2f2f2);
  }

  .ic-tile.active,
  .ic-tile.selected {
    border-color: var(--control-blue, #c1dd2d);
  }

  .ic-tile .icon-wrap {
    width: var(--ic-size, 24px);
    height: var(--ic-size, 24px);
    max-width: calc(100% - 14px);
    max-height: calc(100% - 14px);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--ic-color, var(--icon-color, #a1a1aa));
    transform: rotate(var(--ic-rot, 0deg)) scaleX(var(--ic-flip-x, 1)) scaleY(var(--ic-flip-y, 1));
    filter: blur(var(--ic-blur, 0px));
  }

  .ic-tile .icon-wrap :global(svg) {
    width: 100%;
    height: 100%;
    color: var(--ic-color, currentColor);
  }

  .ic-tile[data-filled='false'] .icon-wrap :global(svg) {
    fill: none;
    stroke: currentColor;
    stroke-width: var(--ic-stroke, var(--ic-stroke-width, 1.75));
  }

  .ic-tile[data-filled='true'] .icon-wrap :global(svg) {
    fill: currentColor;
    stroke: none;
  }

  .card-name {
    position: absolute;
    bottom: 6px;
    left: 6px;
    right: 6px;
    font-size: 10px;
    line-height: 1.2;
    color: var(--text-muted, #8a8a8a);
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .card-favorite-btn {
    position: absolute;
    top: 4px;
    right: 4px;
    width: 22px;
    height: 22px;
    padding: 3px;
    border: none;
    border-radius: 4px;
    background: transparent;
    color: var(--text-muted, #8a8a8a);
    opacity: 0;
    pointer-events: none;
    cursor: pointer;
    transition: opacity 120ms ease, color 120ms ease;
  }

  .card-favorite-btn svg {
    width: 12px;
    height: 12px;
    pointer-events: none;
  }

  .ic-tile:hover .card-favorite-btn,
  .ic-tile:focus-within .card-favorite-btn,
  .card-favorite-btn.favorited {
    opacity: 1;
    pointer-events: auto;
  }

  @media (hover: none), (pointer: coarse) {
    .card-favorite-btn,
    .ic-tile:hover .card-favorite-btn,
    .ic-tile:focus-within .card-favorite-btn,
    .card-favorite-btn.favorited {
      pointer-events: none;
    }
  }

  .card-favorite-btn.favorited {
    color: var(--neon-blue, #c1dd2d);
  }

  .select-check {
    position: absolute;
    top: 5px;
    right: 5px;
    width: 18px;
    height: 18px;
    border-radius: 4px;
    border: 1px solid var(--border-hover, #2a2a2a);
    background: var(--bg-elevated, #161616);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    font-weight: 700;
    color: var(--btn-primary-text, #0a0a0a);
  }

  .select-check.checked {
    background: var(--btn-primary-bg, #c1dd2d);
    border-color: var(--btn-primary-bg, #c1dd2d);
  }

  .icon-skeleton {
    width: 24px;
    height: 24px;
    border-radius: 6px;
    background: var(--bg-elevated, #161616);
  }

  .no-results {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 14px;
    padding: 64px 24px;
    text-align: center;
    color: var(--text-secondary, #888888);
  }

  .suggestion-chips {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;
  }

  .suggestion-chip {
    padding: 6px 12px;
    border-radius: var(--radius-button, 6px);
    border: 1px solid var(--border, #1f1f1f);
    background: var(--bg-elevated, #161616);
    color: var(--text-primary, #f2f2f2);
    font-size: 12px;
    cursor: pointer;
  }

  .suggestion-chip:hover {
    border-color: var(--control-blue, #c1dd2d);
  }
</style>
