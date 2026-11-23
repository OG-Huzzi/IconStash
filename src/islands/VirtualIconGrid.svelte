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

  interface Props {
    focusedPos?: number;
    onFocusPos?: (pos: number) => void;
    onSuggestionClick?: (term: string) => void;
  }

  let {
    focusedPos = $bindable(-1),
    onFocusPos,
    onSuggestionClick,
  }: Props = $props();

  const MAX_MOUNTED_TILES = 180;
  const GRID_GAP = 8;
  const SUGGESTION_CHIPS = ['camera', 'arrow', 'user', 'chart', 'download', 'lock'] as const;

  const DENSITY_METRICS: Record<GridDensity, { cardSize: number; rowHeight: number }> = {
    compact: { cardSize: 64, rowHeight: 72 },
    default: { cardSize: 80, rowHeight: 88 },
    comfortable: { cardSize: 100, rowHeight: 118 },
  };

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
  const totalMatches = $derived(explorerState.resultIndices.length);
  const rowCount = $derived(Math.ceil(totalMatches / columns));

  // Hard mathematical cap so mounted `[data-icon-tile]` count NEVER exceeds 180
  const maxMountedRows = $derived(Math.max(1, Math.floor(MAX_MOUNTED_TILES / columns)));
  const visibleRowEstimate = $derived(Math.max(1, Math.ceil(containerHeight / metrics.rowHeight)));
  const effectiveOverscan = $derived(
    Math.min(2, Math.max(0, Math.floor((maxMountedRows - visibleRowEstimate) / 2))),
  );

  const rowVirtualizer = createVirtualizer<HTMLDivElement, HTMLDivElement>({
    count: 0,
    getScrollElement: () => scrollContainerEl,
    estimateSize: () => 72,
    overscan: 2,
  });

  // Keep virtualizer synced when result count, column count, density, or viewport changes
  $effect(() => {
    const count = rowCount;
    const size = metrics.rowHeight;
    const overscan = effectiveOverscan;
    const el = scrollContainerEl;
    untrack(() => {
      $rowVirtualizer.setOptions({
        count,
        getScrollElement: () => el,
        estimateSize: () => size,
        overscan,
      });
    });
  });

  // Reset scroll to top when a new search result set arrives
  $effect(() => {
    const _indices = explorerState.resultIndices;
    if (scrollContainerEl && _indices.length >= 0) {
      scrollContainerEl.scrollTop = 0;
    }
  });

  // Observe grid viewport width/height with strict teardown on unmount
  $effect(() => {
    const el = scrollContainerEl;
    if (!el || typeof ResizeObserver === 'undefined') return;

    const updateRect = () => {
      const rect = el.getBoundingClientRect();
      if (rect.width > 0) containerWidth = rect.width;
      if (rect.height > 0) containerHeight = rect.height;
    };
    updateRect();

    const observer = new ResizeObserver((entries) => {
      const entry = entries[0];
      if (!entry) return;
      const { width, height } = entry.contentRect;
      if (width > 0) containerWidth = width;
      if (height > 0) containerHeight = height;
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

  const virtualRows = $derived($rowVirtualizer.getVirtualItems().slice(0, maxMountedRows));
  const totalHeight = $derived($rowVirtualizer.getTotalSize());

  // Hydrate only the shards required for the currently mounted virtual rows
  $effect(() => {
    const rows = virtualRows;
    const indices = explorerState.resultIndices;
    const manifest = explorerState.manifest;
    const cols = columns;

    if (!manifest || indices.length === 0 || rows.length === 0) return;

    const needed: number[] = [];
    for (let r = 0; r < rows.length; r++) {
      const startPos = rows[r].index * cols;
      const endPos = Math.min(startPos + cols, indices.length);
      for (let pos = startPos; pos < endPos; pos++) {
        needed.push(indices[pos]);
      }
    }

    if (needed.length === 0) return;

    const controller = new AbortController();
    void explorerState.ensureChunksForIndices(needed, controller.signal);

    return () => {
      controller.abort();
    };
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

    const targetRow = Math.floor(clamped / columns);
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
      {#each virtualRows as vRow (vRow.key)}
        {@const startPos = vRow.index * columns}
        {@const rowSliceLen = Math.min(columns, Math.max(0, totalMatches - startPos))}
        <div
          class="ic-virtual-row"
          data-row-index={vRow.index}
          style="position: absolute; top: 0; left: 0; width: 100%; height: {metrics.rowHeight}px; transform: translateY({vRow.start}px); display: grid; grid-template-columns: repeat({columns}, minmax(0, 1fr)); gap: {GRID_GAP}px; align-items: stretch;"
        >
          {#each { length: rowSliceLen } as _, colOffset (startPos + colOffset)}
            {@const pos = startPos + colOffset}
            {@const iconIndex = explorerState.resultIndices[pos]}
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
      {/each}
    </div>
  {/if}
</div>

<style>
  #virtual-grid-container {
    flex: 1;
    min-height: 0;
    overflow-y: auto;
    overflow-x: hidden;
    position: relative;
    padding: 8px 16px 24px;
    contain: layout style;
    height: calc(100vh - 120px);
    min-height: 520px;
    --ic-color: currentColor;
    --ic-stroke: 1.75;
    --ic-stroke-width: 1.75;
    --ic-rot: 0deg;
    --ic-flip-x: 1;
    --ic-flip-y: 1;
    --ic-blur: 0px;
  }

  .ic-tile {
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
    color: var(--ic-color, var(--icon-color, #888888));
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
    cursor: pointer;
    transition: opacity 120ms ease, color 120ms ease;
  }

  .ic-tile:hover .card-favorite-btn,
  .ic-tile:focus-within .card-favorite-btn,
  .card-favorite-btn.favorited {
    opacity: 1;
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
