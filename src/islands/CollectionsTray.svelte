<script lang="ts">
  import { inspectorState } from '../lib/state/inspector.svelte';
  import { previewState } from '../lib/state/preview.svelte';
  import { collectionsState } from '../lib/state/collections.svelte';
  import { explorerState, type ResolvedIcon as ExplorerResolvedIcon } from '../lib/state/explorer.svelte';
  import { renderCustomizedSvg } from '../lib/svg/effects';
  import { createSprite, formatCode } from '../lib/svg/codegen';
  import { createDefaultCustomizationState } from '../lib/svg/types';
  import { slugFilePart } from '../lib/svg/normalize';
  import {
    exportBulkZip,
    exportCollectionZip,
    downloadBlob,
    type ExportSvgInput,
  } from '../lib/export/client';

  type ResolvedIcon = ExplorerResolvedIcon & { tags?: string[] };

  interface NormalizedCollection {
    id: string;
    name: string;
    icons: string[];
    isFavorites: boolean;
  }

  const FALLBACK_CUSTOM = createDefaultCustomizationState();

  let newCollectionName = $state('');
  let renamingTarget = $state<string | null>(null);
  let renameDraft = $state('');
  let bulkColor = $state('#00c3ff');
  let bulkCollectOpen = $state(false);
  let busyExport = $state(false);
  let iconCache = $state<Record<string, ResolvedIcon>>({});

  const collectionsOpen = $derived(Boolean(inspectorState.collectionsOpen));
  const shortcutsOpen = $derived(Boolean(inspectorState.shortcutsOpen));
  const toastMessage = $derived(inspectorState.toastMessage || '');
  const custom = $derived(inspectorState.custom ?? FALLBACK_CUSTOM);

  const selectedList = $derived.by(() => {
    const raw = collectionsState.selectedIds as unknown;
    if (raw instanceof Set) return Array.from(raw) as string[];
    if (Array.isArray(raw)) return raw as string[];
    return [] as string[];
  });

  const selectedCount = $derived(selectedList.length);

  const favoriteIds = $derived.by(() => {
    const raw = collectionsState.favorites as unknown;
    if (raw instanceof Set) return Array.from(raw) as string[];
    if (Array.isArray(raw)) return raw as string[];
    return [] as string[];
  });

  const normalizedCollections = $derived.by<NormalizedCollection[]>(() => {
    const list: NormalizedCollection[] = [
      {
        id: 'favorites',
        name: 'Favorites',
        icons: favoriteIds,
        isFavorites: true,
      },
    ];

    const raw = collectionsState.collections as unknown;
    if (Array.isArray(raw)) {
      for (const entry of raw as Array<{ id?: string; name?: string; icons?: string[] }>) {
        const name = entry.name || entry.id || '';
        if (!name || name.toLowerCase() === 'favorites' || entry.id === 'favorites') continue;
        list.push({
          id: entry.id || name,
          name,
          icons: Array.isArray(entry.icons) ? entry.icons : [],
          isFavorites: false,
        });
      }
    } else if (raw instanceof Map) {
      for (const [key, value] of raw.entries()) {
        const name = String(key);
        if (!name || name.toLowerCase() === 'favorites') continue;
        const icons = value instanceof Set ? Array.from(value) : Array.isArray(value) ? value : [];
        list.push({ id: name, name, icons: icons as string[], isFavorites: false });
      }
    } else if (raw && typeof raw === 'object') {
      for (const [name, value] of Object.entries(raw as Record<string, unknown>)) {
        if (!name || name.toLowerCase() === 'favorites') continue;
        const icons = value instanceof Set ? Array.from(value) : Array.isArray(value) ? value : [];
        list.push({ id: name, name, icons: icons as string[], isFavorites: false });
      }
    }

    return list;
  });

  async function resolveIconById(id: string): Promise<ResolvedIcon | null> {
    if (iconCache[id]) return iconCache[id];

    const active = inspectorState.activeIcon as ResolvedIcon | null;
    if (active && active.id === id) {
      return active;
    }

    // Attempt resolution via numeric index if stored as index string
    const asNum = Number(id);
    if (Number.isInteger(asNum) && asNum >= 0 && String(asNum) === id) {
      try {
        await explorerState.ensureChunkForIcon(asNum);
        const payload = explorerState.getIconPayload(asNum) as ResolvedIcon | null | undefined;
        if (payload) return payload;
      } catch {
        // Fallback below
      }
    }

    // Attempt concept match lookup by stripped icon name
    const parts = id.split('-');
    const candidateName = parts.length > 1 ? parts.slice(1).join('-') : id;
    try {
      const matchArr = await explorerState.findConceptMatches(candidateName);
      for (const resolved of matchArr.slice(0, 30)) {
        if (resolved && resolved.id === id) {
          return resolved;
        }
      }
    } catch {
      // Ignore lookup errors
    }

    return null;
  }

  $effect(() => {
    if (!collectionsOpen) return;
    const allIds = new Set<string>();
    for (const col of normalizedCollections) {
      for (const id of col.icons.slice(0, 24)) {
        if (!iconCache[id]) allIds.add(id);
      }
    }
    if (allIds.size === 0) return;

    let cancelled = false;
    (async () => {
      const resolvedMap: Record<string, ResolvedIcon> = {};
      for (const id of allIds) {
        if (cancelled) return;
        const found = await resolveIconById(id);
        if (found) resolvedMap[id] = found;
      }
      if (!cancelled && Object.keys(resolvedMap).length > 0) {
        iconCache = { ...iconCache, ...resolvedMap };
      }
    })();

    return () => {
      cancelled = true;
    };
  });

  async function resolveIconsForExport(ids: string[], colorOverride?: string): Promise<{
    resolved: ResolvedIcon[];
    exportInputs: ExportSvgInput[];
  }> {
    const resolved: ResolvedIcon[] = [];
    for (const id of ids.slice(0, 200)) {
      const icon = await resolveIconById(id);
      if (icon) resolved.push(icon);
    }

    const exportInputs: ExportSvgInput[] = resolved.map((icon) => ({
      id: icon.id,
      name: icon.name,
      librarySlug: icon.librarySlug || 'iconstash',
      library: icon.library || icon.librarySlug || 'IconStash',
      tags: icon.tags,
      license: icon.license,
      svgMarkup: renderCustomizedSvg(icon, {
        color: colorOverride || custom.color,
        strokeWidth: custom.strokeWidth,
        size: custom.size,
        width: custom.width ?? custom.size,
        height: custom.height ?? custom.size,
        gradient: colorOverride ? null : custom.gradient,
        effects: custom.effects,
        motion: custom.motion,
      }),
    }));

    return { resolved, exportInputs };
  }

  function handleCreateCollection() {
    const name = newCollectionName.trim();
    if (!name) return;
    collectionsState.createCollection(name);
    newCollectionName = '';
    inspectorState.showToast(`Created "${name}"`);
  }

  function startRename(col: NormalizedCollection) {
    if (col.isFavorites) return;
    renamingTarget = col.name;
    renameDraft = col.name;
  }

  function commitRename(oldName: string) {
    const trimmed = renameDraft.trim();
    renamingTarget = null;
    if (!trimmed || trimmed === oldName) return;
    collectionsState.renameCollection(oldName, trimmed);
    inspectorState.showToast(`Renamed to "${trimmed}"`);
  }

  function handleDeleteCollection(col: NormalizedCollection) {
    if (col.isFavorites) return;
    collectionsState.deleteCollection(col.name);
    inspectorState.showToast(`Deleted "${col.name}"`);
  }

  function handleRemoveIcon(col: NormalizedCollection, iconId: string) {
    if (col.isFavorites) {
      collectionsState.toggleFavorite(iconId);
    } else {
      collectionsState.removeFromCollection(col.name, iconId);
    }
    inspectorState.showToast(`Removed from ${col.name}`);
  }

  async function handleExportCollectionZip(col: NormalizedCollection, includePngs: boolean) {
    if (!col.icons.length || busyExport) {
      if (!col.icons.length) inspectorState.showToast('Collection is empty');
      return;
    }
    busyExport = true;
    inspectorState.showToast(
      `Packaging ${Math.min(col.icons.length, 200)} icons${includePngs ? ' + PNGs' : ''}...`,
    );
    try {
      const { exportInputs } = await resolveIconsForExport(col.icons);
      if (!exportInputs.length) {
        inspectorState.showToast('No icon payloads available to export');
        return;
      }
      await exportCollectionZip(exportInputs, col.name, includePngs);
      inspectorState.showToast(includePngs ? 'PNG ZIP downloaded' : 'ZIP downloaded');
    } catch {
      inspectorState.showToast('Collection ZIP export failed');
    } finally {
      busyExport = false;
    }
  }

  async function handleDevExport(
    col: NormalizedCollection,
    kind: 'react' | 'vue' | 'sprite' | 'css' | 'json',
  ) {
    if (!col.icons.length) {
      inspectorState.showToast('Collection is empty');
      return;
    }
    const { resolved } = await resolveIconsForExport(col.icons);
    if (!resolved.length) {
      inspectorState.showToast('No icon payloads available to export');
      return;
    }
    const slug = slugFilePart(col.name);
    const opts = {
      color: custom.color,
      strokeWidth: custom.strokeWidth,
      size: custom.size,
      gradient: custom.gradient,
      effects: custom.effects,
      motion: custom.motion,
    };

    let content = '';
    let filename = `${slug}.txt`;
    let mime = 'text/plain;charset=utf-8';

    if (kind === 'react') {
      content = resolved.map((icon) => formatCode(icon, 'jsx', opts)).join('\n');
      filename = `${slug}.jsx`;
    } else if (kind === 'vue') {
      content = resolved.map((icon) => formatCode(icon, 'vue', opts)).join('\n\n');
      filename = `${slug}.vue`;
    } else if (kind === 'sprite') {
      content = createSprite(resolved);
      filename = `${slug}-sprite.svg`;
      mime = 'image/svg+xml;charset=utf-8';
    } else if (kind === 'css') {
      content = resolved.map((icon) => formatCode(icon, 'css', opts)).join('\n\n');
      filename = `${slug}.css`;
      mime = 'text/css;charset=utf-8';
    } else if (kind === 'json') {
      content = JSON.stringify(
        resolved.map((icon) => ({
          id: icon.id,
          name: icon.name,
          library: icon.library || icon.librarySlug,
          style: icon.style,
        })),
        null,
        2,
      );
      filename = `${slug}.json`;
      mime = 'application/json;charset=utf-8';
    }

    downloadBlob(new Blob([content], { type: mime }), filename);
    inspectorState.showToast(`Exported ${filename}`);
  }

  function handleBulkRecolor(nextColor: string) {
    bulkColor = nextColor;
    previewState.setColor(nextColor);
    inspectorState.updateCustom({ color: nextColor });
  }

  async function handleBulkDownloadZip() {
    if (!selectedList.length || busyExport) return;
    busyExport = true;
    inspectorState.showToast(`Packaging ${Math.min(selectedList.length, 200)} selected icons...`);
    try {
      const { exportInputs } = await resolveIconsForExport(selectedList, bulkColor);
      if (!exportInputs.length) {
        inspectorState.showToast('No selected icon payloads available');
        return;
      }
      await exportBulkZip(exportInputs);
      inspectorState.showToast('Bulk ZIP downloaded');
    } catch {
      inspectorState.showToast('Bulk ZIP export failed');
    } finally {
      busyExport = false;
    }
  }

  function handleBulkAddToCollection(col: NormalizedCollection) {
    for (const id of selectedList) {
      if (col.isFavorites) {
        if (!collectionsState.isFavorite(id)) {
          collectionsState.toggleFavorite(id);
        }
      } else {
        collectionsState.addToCollection(col.name, id);
      }
    }
    bulkCollectOpen = false;
    inspectorState.showToast(`Added ${selectedList.length} icons to ${col.name}`);
  }

  function handleKeydown(event: KeyboardEvent) {
    const target = event.target as HTMLElement | null;
    const inField =
      target &&
      (target.tagName === 'INPUT' ||
        target.tagName === 'TEXTAREA' ||
        target.tagName === 'SELECT' ||
        target.isContentEditable);

    if (event.key === '?' && !inField) {
      event.preventDefault();
      if (shortcutsOpen) inspectorState.closeShortcuts();
      else inspectorState.openShortcuts();
      return;
    }

    if (event.key === 'Escape') {
      if (shortcutsOpen) {
        inspectorState.closeShortcuts();
      } else if (collectionsOpen) {
        inspectorState.closeCollections();
      }
    }
  }
</script>

<svelte:window onkeydown={handleKeydown} />

<!-- Bulk Action Bar -->
<div id="bulk-action-bar" class:hidden={selectedCount === 0}>
  <div class="bulk-count">
    <span id="bulk-num">{selectedCount}</span> icons selected
  </div>
  <div class="bulk-actions">
    <label class="glass-btn bulk-color-label" for="bulk-color">
      Set Color
      <input
        id="bulk-color"
        type="color"
        value={bulkColor}
        oninput={(e) => handleBulkRecolor((e.currentTarget as HTMLInputElement).value)}
      />
    </label>
    <button
      type="button"
      class="gradient-btn"
      id="bulk-download"
      disabled={busyExport}
      onclick={handleBulkDownloadZip}
    >
      {busyExport ? 'Packaging…' : 'Download ZIP'}
    </button>
    <div style="position: relative;">
      <button
        type="button"
        class="glass-btn"
        id="bulk-collect"
        onclick={() => (bulkCollectOpen = !bulkCollectOpen)}
      >
        Add to Collection
      </button>
      {#if bulkCollectOpen}
        <div
          class="qa-menu"
          role="menu"
          aria-label="Add selected icons to collection"
          style="bottom: calc(100% + 8px); top: auto; right: 0; min-width: 180px;"
        >
          {#each normalizedCollections as col (col.id)}
            <button
              type="button"
              class="qa-menu-item"
              role="menuitem"
              onclick={() => handleBulkAddToCollection(col)}
            >
              <span>{col.name}</span>
              <em>{col.icons.length}</em>
            </button>
          {/each}
        </div>
      {/if}
    </div>
    <button
      type="button"
      class="glass-btn"
      id="bulk-clear"
      onclick={() => {
        bulkCollectOpen = false;
        collectionsState.clearSelection();
      }}
    >
      Clear
    </button>
  </div>
</div>

<!-- Modal Backdrop for Collections or Shortcuts -->
{#if collectionsOpen || shortcutsOpen}
  <!-- svelte-ignore a11y_click_events_have_key_events -->
  <!-- svelte-ignore a11y_no_static_element_interactions -->
  <div
    class="modal-backdrop"
    id="modal-backdrop"
    onclick={() => {
      if (collectionsOpen) inspectorState.closeCollections();
      if (shortcutsOpen) inspectorState.closeShortcuts();
    }}
  ></div>
{/if}

<!-- Collections & Favorites Modal -->
<div
  class="modal"
  class:hidden={!collectionsOpen}
  id="collections-modal"
  aria-modal="true"
  role="dialog"
  aria-label="Collections"
>
  <div class="modal-header">
    <h2 class="gradient-text">Collections</h2>
    <button
      type="button"
      class="close-btn modal-close"
      aria-label="Close collections"
      onclick={() => inspectorState.closeCollections()}
    >
      <svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12" /></svg>
    </button>
  </div>
  <div class="modal-content">
    <div class="collection-create">
      <input
        id="collection-name-input"
        class="mini-search"
        placeholder="New collection name"
        bind:value={newCollectionName}
        onkeydown={(e) => {
          if (e.key === 'Enter') handleCreateCollection();
        }}
      />
      <button
        type="button"
        class="gradient-btn"
        id="collection-create-btn"
        onclick={handleCreateCollection}
      >
        Create
      </button>
    </div>

    <div id="collections-list" class="collections-list">
      {#each normalizedCollections as col (col.id)}
        <article class="collection-row" data-collection-id={col.id}>
          <div class="collection-row-info">
            {#if renamingTarget === col.name}
              <div style="display: flex; gap: 6px; align-items: center;">
                <input
                  type="text"
                  class="mini-search"
                  bind:value={renameDraft}
                  onkeydown={(e) => {
                    if (e.key === 'Enter') commitRename(col.name);
                    if (e.key === 'Escape') renamingTarget = null;
                  }}
                />
                <button
                  type="button"
                  class="gradient-btn text-btn"
                  onclick={() => commitRename(col.name)}
                >
                  Save
                </button>
              </div>
            {:else}
              <h3 class="collection-name-title">{col.name}</h3>
            {/if}
            <p class="muted">{col.icons.length} {col.icons.length === 1 ? 'icon' : 'icons'}</p>

            <div class="collection-preview">
              {#each col.icons.slice(0, 24) as iconId (iconId)}
                {@const iconObj = iconCache[iconId]}
                <span class="mini-icon" title={iconObj ? `${iconObj.library || iconObj.librarySlug} / ${iconObj.name}` : iconId}>
                  {#if iconObj}
                    <button
                      type="button"
                      class="mini-icon-inspect"
                      aria-label={`Inspect ${iconObj.name}`}
                      onclick={() => {
                        inspectorState.openInspector(iconObj);
                        inspectorState.closeCollections();
                      }}
                    >
                      {@html renderCustomizedSvg(iconObj, {
                        size: 20,
                        width: 20,
                        height: 20,
                        color: 'currentColor',
                      })}
                    </button>
                  {:else}
                    <span class="muted" style="font-size: 10px;">•</span>
                  {/if}
                  <button
                    type="button"
                    class="remove-mini-icon-btn"
                    data-icon-id={iconId}
                    title="Remove from collection"
                    aria-label="Remove from collection"
                    onclick={() => handleRemoveIcon(col, iconId)}
                  >
                    &times;
                  </button>
                </span>
              {/each}
            </div>
          </div>

          <div class="collection-actions-group">
            <div class="actions-primary">
              {#if !col.isFavorites}
                <button
                  type="button"
                  class="glass-btn text-btn"
                  data-collection-action="rename"
                  onclick={() => startRename(col)}
                >
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4 12.5-12.5Z" />
                  </svg>
                  <span>Rename</span>
                </button>
              {/if}
              <button
                type="button"
                class="gradient-btn text-btn"
                data-collection-action="zip"
                disabled={busyExport || col.icons.length === 0}
                onclick={() => handleExportCollectionZip(col, false)}
              >
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3" />
                </svg>
                <span>Download ZIP</span>
              </button>
              <button
                type="button"
                class="gradient-btn text-btn"
                data-collection-action="png-zip"
                disabled={busyExport || col.icons.length === 0}
                onclick={() => handleExportCollectionZip(col, true)}
              >
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3" />
                </svg>
                <span>Download PNG ZIP</span>
              </button>
              {#if !col.isFavorites}
                <button
                  type="button"
                  class="glass-btn delete-btn"
                  data-collection-action="delete"
                  title="Delete Collection"
                  aria-label={`Delete ${col.name}`}
                  onclick={() => handleDeleteCollection(col)}
                >
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 6h18M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M10 11v6M14 11v6" />
                  </svg>
                </button>
              {/if}
            </div>

            <div class="actions-exports">
              <span class="export-label">Developer Exports</span>
              <div class="export-buttons">
                <button
                  type="button"
                  class="glass-btn mini-export-btn"
                  data-collection-action="react"
                  title="Export React JSX components"
                  onclick={() => handleDevExport(col, 'react')}
                >
                  React JSX
                </button>
                <button
                  type="button"
                  class="glass-btn mini-export-btn"
                  data-collection-action="vue"
                  title="Export Vue component snippets"
                  onclick={() => handleDevExport(col, 'vue')}
                >
                  Vue
                </button>
                <button
                  type="button"
                  class="glass-btn mini-export-btn"
                  data-collection-action="sprite"
                  title="Export SVG Symbol Sprite"
                  onclick={() => handleDevExport(col, 'sprite')}
                >
                  SVG Sprite
                </button>
                <button
                  type="button"
                  class="glass-btn mini-export-btn"
                  data-collection-action="css"
                  title="Export CSS mask-image sprite"
                  onclick={() => handleDevExport(col, 'css')}
                >
                  CSS Sprite
                </button>
                <button
                  type="button"
                  class="glass-btn mini-export-btn"
                  data-collection-action="json"
                  title="Export JSON list of icon data"
                  onclick={() => handleDevExport(col, 'json')}
                >
                  JSON list
                </button>
              </div>
            </div>
          </div>
        </article>
      {/each}
    </div>
  </div>
</div>

<!-- Keyboard Shortcuts Help Modal -->
<div
  class="modal"
  class:hidden={!shortcutsOpen}
  id="shortcuts-modal"
  aria-modal="true"
  role="dialog"
  aria-label="Keyboard Shortcuts"
>
  <div class="modal-header">
    <h2 class="gradient-text">Keyboard Shortcuts</h2>
    <button
      type="button"
      class="close-btn modal-close"
      aria-label="Close shortcuts"
      onclick={() => inspectorState.closeShortcuts()}
    >
      <svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12" /></svg>
    </button>
  </div>
  <div class="modal-content shortcuts-list">
    <div class="shortcut-row"><span>Focus search</span><kbd>/</kbd></div>
    <div class="shortcut-row"><span>Close detail, modal, or clear search</span><kbd>Esc</kbd></div>
    <div class="shortcut-row"><span>Navigate grid</span><kbd>Arrow keys</kbd></div>
    <div class="shortcut-row"><span>Copy focused SVG</span><kbd>Ctrl+C</kbd></div>
    <div class="shortcut-row"><span>Favorite focused icon</span><kbd>F</kbd></div>
    <div class="shortcut-row"><span>Select all visible</span><kbd>Ctrl+A</kbd></div>
    <div class="shortcut-row"><span>Download focused SVG</span><kbd>Ctrl+D</kbd></div>
    <div class="shortcut-row"><span>Open shortcuts</span><kbd>?</kbd></div>
  </div>
</div>

<!-- Global Toast Notification Overlay -->
<div id="toast-container" aria-live="polite">
  {#if toastMessage}
    <div class="toast toast-success" role="status">
      {toastMessage}
    </div>
  {/if}
</div>

<style>
  .mini-icon-inspect {
    all: unset;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
</style>
