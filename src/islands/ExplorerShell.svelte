<script lang="ts">
  /**
   * ExplorerShell.svelte
   *
   * Primary interactive explorer island matching legacy IconStash UI 1:1:
   * - Search bar (`#main-search`, `#search-clear`, `#result-count`)
   * - Collapsible filter sidebar (all 28 libraries with live counts, docs links,
   *   npm install command copy; 7 styles + "All"; 16 categories; Preview Size slider;
   *   Sort selector; live Color/Stroke controls; Clear All Filters)
   * - Active filter pills bar
   * - Main toolbar (live status, density switcher, Select mode, Draw an Icon,
   *   Compare, Collections/Favorites with badge, Shortcuts `?`, Theme toggle)
   * - Embedded `VirtualIconGrid`
   * - Global keyboard shortcuts (`/`, arrows, `Ctrl+C`, `F`, `Ctrl+D`, `Ctrl+A`,
   *   `Escape`, `?`) with guaranteed listener teardown on unmount & `astro:before-swap`
   */

  import { explorerState, type ResolvedIcon } from '../lib/state/explorer.svelte';
  import { previewState, type GridDensity } from '../lib/state/preview.svelte';
  import { inspectorState } from '../lib/state/inspector.svelte';
  import { collectionsState } from '../lib/state/collections.svelte';
  import { formatCode } from '../lib/svg/codegen';
  import { downloadBlob } from '../lib/export/client';
  import VirtualIconGrid from './VirtualIconGrid.svelte';
  import { LIBRARY_BADGE_SVGS } from '../lib/library-icons';

  interface Props {
    initialLibrary?: string;
    initialCategory?: string;
    initialStyle?: string;
    initialQuery?: string;
  }

  let {
    initialLibrary,
    initialCategory,
    initialStyle,
    initialQuery,
  }: Props = $props();

  let colorWheelEl = $state<HTMLInputElement | null>(null);
  let gridRef = $state<ReturnType<typeof VirtualIconGrid> | null>(null);
  let gridRightInset = $state(4);

  let searchDraft = $state('');
  let libFilterQuery = $state('');
  let focusedPos = $state(-1);

  // Sidebar & collapsible card toggles
  let sidebarCollapsed = $state(false);
  let mobileSidebarOpen = $state(
    typeof document !== 'undefined' && document.body.classList.contains('sidebar-open'),
  );
  let libsExpanded = $state(false);
  let stylesExpanded = $state(false);
  let categoriesExpanded = $state(false);
  let customizeExpanded = $state(false);

  // Initialize explorer store on mount or route-prop changes
  $effect(() => {
    const lib = initialLibrary;
    const cat = initialCategory;
    const sty = initialStyle;
    const q = initialQuery;

    searchDraft = q ?? '';
    void explorerState.initExplorer({
      initialLibrary: lib,
      initialCategory: cat,
      initialStyle: sty,
      initialQuery: q,
    });

    return () => {
      explorerState.disposeTimers();
    };
  });

  // Sync desktop collapsed state without clobbering Header.astro's mobile sidebar-open state
  $effect(() => {
    if (typeof document === 'undefined') return;
    document.body.classList.toggle('sidebar-collapsed', sidebarCollapsed);
    return () => {
      document.body.classList.remove('sidebar-collapsed');
      document.body.classList.remove('sidebar-open');
    };
  });

  $effect(() => {
    if (typeof window === 'undefined') return;
    const onSidebarToggle = (e: Event) => {
      const open = (e as CustomEvent<{ open?: boolean }>).detail?.open;
      if (typeof open === 'boolean') {
        mobileSidebarOpen = open;
      } else if (typeof document !== 'undefined') {
        mobileSidebarOpen = document.body.classList.contains('sidebar-open');
      }
    };
    window.addEventListener('iconstash:sidebar-toggle', onSidebarToggle);
    return () => {
      window.removeEventListener('iconstash:sidebar-toggle', onSidebarToggle);
    };
  });

  // Keep searchDraft synced when query is cleared or updated externally (e.g. suggestion chip)
  $effect(() => {
    if (explorerState.query !== searchDraft && explorerState.query === '') {
      searchDraft = '';
    }
  });

  const libraries = $derived(explorerState.meta?.libraries ?? []);
  const categories = $derived(explorerState.meta?.categories ?? []);
  const styles = $derived(explorerState.meta?.styles ?? []);
  const totalCatalogIcons = $derived(explorerState.meta?.totalIcons ?? 134701);

  const filteredLibraries = $derived.by(() => {
    const q = libFilterQuery.trim().toLowerCase();
    if (!q) return libraries;
    return libraries.filter(
      (lib) =>
        lib.name.toLowerCase().includes(q) ||
        lib.slug.toLowerCase().includes(q) ||
        lib.npmPackage.toLowerCase().includes(q),
    );
  });

  const selectedLibraryIndices = $derived.by(() => {
    const mask = explorerState.selectedLibMask;
    const out: number[] = [];
    for (let i = 0; i < libraries.length; i++) {
      if ((mask & (1 << libraries[i].id)) !== 0) out.push(libraries[i].id);
    }
    return out;
  });

  const selectedCategoryIndices = $derived.by(() => {
    const mask = explorerState.selectedCatMask;
    const out: number[] = [];
    for (let i = 0; i < categories.length; i++) {
      if ((mask & (1 << i)) !== 0) out.push(i);
    }
    return out;
  });

  const selectedStyleIndices = $derived.by(() => {
    const mask = explorerState.selectedStyleMask;
    const out: number[] = [];
    for (let i = 0; i < styles.length; i++) {
      if ((mask & (1 << i)) !== 0) out.push(i);
    }
    return out;
  });

  const hasActiveFilters = $derived(
    explorerState.query.length > 0 ||
      explorerState.selectedLibMask !== 0 ||
      explorerState.selectedCatMask !== 0 ||
      explorerState.selectedStyleMask !== 0,
  );

  const selectedLibsLabel = $derived(
    selectedLibraryIndices.length === 0
      ? 'All'
      : `${selectedLibraryIndices.length} selected`,
  );

  const favoritesCount = $derived(collectionsState.favorites.length);

  function closeMobileSidebar(): void {
    mobileSidebarOpen = false;
    if (typeof document !== 'undefined') {
      document.body.classList.remove('sidebar-open');
      const btn = document.getElementById('sidebar-toggle');
      if (btn) {
        btn.setAttribute('aria-expanded', 'false');
        btn.setAttribute('aria-label', 'Open filters');
        btn.title = 'Open filters';
      }
      window.dispatchEvent(new CustomEvent('iconstash:sidebar-toggle', { detail: { open: false } }));
    }
  }

  function syncHeaderSearch(query: string): void {
    if (typeof window !== 'undefined') {
      window.dispatchEvent(new CustomEvent('iconstash:search-sync', { detail: { query } }));
    }
  }

  function formatNumber(n: number): string {
    return n.toLocaleString('en-US');
  }

  function formatStyleLabel(style: string): string {
    return style.charAt(0).toUpperCase() + style.slice(1);
  }

  function clearSearchInput(): void {
    searchDraft = '';
    explorerState.setQuery('');
    syncHeaderSearch('');
    const headerInput = document.getElementById('main-search') as HTMLInputElement | null;
    headerInput?.focus();
  }

  async function copyText(text: string, toastMsg: string): Promise<void> {
    try {
      if (typeof navigator !== 'undefined' && navigator.clipboard?.writeText) {
        await navigator.clipboard.writeText(text);
      } else if (typeof document !== 'undefined') {
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        ta.remove();
      }
      inspectorState.showToast(toastMsg);
    } catch {
      inspectorState.showToast('Copy failed — clipboard unavailable');
    }
  }

  async function resolveFocusedOrActiveIcon(): Promise<ResolvedIcon | null> {
    if (focusedPos >= 0 && focusedPos < explorerState.resultIndices.length) {
      const iconIndex = explorerState.resultIndices[focusedPos];
      const syncIcon = explorerState.getIconPayload(iconIndex);
      if (syncIcon) return syncIcon;
      return explorerState.ensureChunkForIcon(iconIndex);
    }
    return inspectorState.activeIcon;
  }

  async function copyIconSvg(icon: ResolvedIcon): Promise<void> {
    const svg = formatCode(icon, 'svg', {
      color: previewState.color || undefined,
      strokeWidth: previewState.strokeWidth,
      size: previewState.gridSize,
    });
    await copyText(svg, `Copied ${icon.name}.svg`);
  }

  function downloadIconSvg(icon: ResolvedIcon): void {
    const svg = formatCode(icon, 'svg', {
      color: previewState.color || undefined,
      strokeWidth: previewState.strokeWidth,
      size: inspectorState.custom.size || 128,
    });
    const blob = new Blob([svg], { type: 'image/svg+xml;charset=utf-8' });
    downloadBlob(blob, `${icon.librarySlug}-${icon.name}.svg`);
    inspectorState.showToast(`Downloaded ${icon.name}.svg`);
  }

  function selectAllVisibleOrCapped(): void {
    const indices = explorerState.resultIndices;
    const cap = Math.min(indices.length, 200);
    const ids: string[] = [];
    for (let i = 0; i < cap; i++) {
      const icon = explorerState.getIconPayload(indices[i]);
      if (icon) ids.push(icon.id);
    }
    if (ids.length > 0) {
      collectionsState.setSelectMode(true);
      collectionsState.selectAll(ids);
      inspectorState.showToast(`Selected ${ids.length} icons`);
    }
  }

  // Global keyboard shortcuts with strict unmount & Astro View Transition teardown
  $effect(() => {
    if (typeof window === 'undefined' || typeof document === 'undefined') return;

    const isEditableTarget = (target: EventTarget | null): boolean => {
      if (!(target instanceof HTMLElement)) return false;
      const tag = target.tagName;
      return (
        tag === 'INPUT' ||
        tag === 'TEXTAREA' ||
        tag === 'SELECT' ||
        target.isContentEditable
      );
    };

    const onKeyDown = (event: KeyboardEvent) => {
      const editable = isEditableTarget(event.target);
      const hasModifier = event.ctrlKey || event.metaKey;

      // `/` focuses search bar when not typing in an input
      if (event.key === '/' && !editable && !hasModifier && !event.altKey) {
        event.preventDefault();
        const headerInput = document.getElementById('main-search') as HTMLInputElement | null;
        headerInput?.focus();
        headerInput?.select();
        return;
      }

      // `?` opens shortcuts modal when not typing in an input
      if (event.key === '?' && !editable && !hasModifier && !event.altKey) {
        event.preventDefault();
        if (inspectorState.shortcutsOpen) {
          inspectorState.closeShortcuts();
        } else {
          inspectorState.openShortcuts();
        }
        return;
      }

      // `Escape` closes modals -> inspector -> mobile sidebar -> select mode -> search
      if (event.key === 'Escape') {
        if (inspectorState.shortcutsOpen) {
          event.preventDefault();
          inspectorState.closeShortcuts();
          return;
        }
        if (inspectorState.drawOpen) {
          event.preventDefault();
          inspectorState.closeDraw();
          return;
        }
        if (inspectorState.compareOpen) {
          event.preventDefault();
          inspectorState.closeCompare();
          return;
        }
        if (inspectorState.collectionsOpen) {
          event.preventDefault();
          inspectorState.closeCollections();
          return;
        }
        if (inspectorState.activeIcon) {
          event.preventDefault();
          inspectorState.closeInspector();
          return;
        }
        if (mobileSidebarOpen || document.body.classList.contains('sidebar-open')) {
          event.preventDefault();
          closeMobileSidebar();
          return;
        }
        if (collectionsState.selectMode) {
          event.preventDefault();
          collectionsState.setSelectMode(false);
          return;
        }
        if (explorerState.query) {
          event.preventDefault();
          clearSearchInput();
          return;
        }
        return;
      }

      // Skip navigation/action shortcuts while typing or while a modal is open
      if (
        editable ||
        inspectorState.drawOpen ||
        inspectorState.compareOpen ||
        inspectorState.shortcutsOpen ||
        inspectorState.collectionsOpen
      ) {
        return;
      }

      // Arrow keys navigate the virtualized icon grid
      if (
        event.key === 'ArrowRight' ||
        event.key === 'ArrowLeft' ||
        event.key === 'ArrowDown' ||
        event.key === 'ArrowUp'
      ) {
        const total = explorerState.resultIndices.length;
        if (total === 0) return;
        event.preventDefault();
        const cols = gridRef?.getColumns() ?? 1;
        const current = focusedPos < 0 ? 0 : focusedPos;
        let next = current;
        if (event.key === 'ArrowRight') next = Math.min(total - 1, current + 1);
        else if (event.key === 'ArrowLeft') next = Math.max(0, current - 1);
        else if (event.key === 'ArrowDown') next = Math.min(total - 1, current + cols);
        else if (event.key === 'ArrowUp') next = Math.max(0, current - cols);
        gridRef?.focusResultPosition(next);
        return;
      }

      // `Ctrl/Cmd + C` copies focused or active icon SVG (when no text selection exists)
      if (hasModifier && event.key.toLowerCase() === 'c') {
        const selectionText = window.getSelection?.()?.toString() ?? '';
        if (selectionText.length > 0) return;
        event.preventDefault();
        void resolveFocusedOrActiveIcon().then((icon) => {
          if (icon) void copyIconSvg(icon);
        });
        return;
      }

      // `Ctrl/Cmd + D` downloads focused or active icon SVG
      if (hasModifier && event.key.toLowerCase() === 'd') {
        event.preventDefault();
        void resolveFocusedOrActiveIcon().then((icon) => {
          if (icon) downloadIconSvg(icon);
        });
        return;
      }

      // `Ctrl/Cmd + A` selects icons when selectMode is active
      if (hasModifier && event.key.toLowerCase() === 'a' && collectionsState.selectMode) {
        event.preventDefault();
        selectAllVisibleOrCapped();
        return;
      }

      // `F` toggles favorite on focused or active icon
      if (!hasModifier && !event.altKey && event.key.toLowerCase() === 'f') {
        event.preventDefault();
        void resolveFocusedOrActiveIcon().then((icon) => {
          if (!icon) return;
          const added = collectionsState.toggleFavorite(icon.id);
          inspectorState.showToast(
            added ? `Saved "${icon.name}" to Favorites` : `Removed "${icon.name}" from Favorites`,
          );
        });
      }
    };

    const cleanup = () => {
      window.removeEventListener('keydown', onKeyDown);
      document.removeEventListener('astro:before-swap', cleanup);
    };

    window.addEventListener('keydown', onKeyDown);
    document.addEventListener('astro:before-swap', cleanup, { once: true });

    return cleanup;
  });
  $effect(() => {
    if (typeof window === 'undefined') return;
    const onHeaderSearch = (e: Event) => {
      const q = (e as CustomEvent<{ query?: string }>).detail?.query ?? '';
      searchDraft = q;
      explorerState.setQuery(q);
    };
    const onOpenDraw = () => inspectorState.openDraw();
    const onOpenCompare = () => inspectorState.openCompare(inspectorState.activeIcon?.name ?? explorerState.query ?? 'home');
    const onOpenCollections = () => inspectorState.openCollections();
    window.addEventListener('iconstash:search-input', onHeaderSearch);
    window.addEventListener('iconstash:open-draw', onOpenDraw);
    window.addEventListener('iconstash:open-compare', onOpenCompare);
    window.addEventListener('iconstash:open-collections', onOpenCollections);
    return () => {
      window.removeEventListener('iconstash:search-input', onHeaderSearch);
      window.removeEventListener('iconstash:open-draw', onOpenDraw);
      window.removeEventListener('iconstash:open-compare', onOpenCompare);
      window.removeEventListener('iconstash:open-collections', onOpenCollections);
    };
  });
  $effect(() => {
    if (typeof document === 'undefined') return;
    const el = document.getElementById('result-count');
    if (el) {
      el.textContent = formatNumber(explorerState.totalMatches || totalCatalogIcons);
      el.classList.remove('hidden');
    }
  });
</script>

<div class="explorer-shell">
  <!-- Main Workspace: Collapsible Filter Sidebar + Virtual Grid -->
  <div class="workspace">
    <button
      type="button"
      class="sidebar-collapse"
      id="sidebar-collapse"
      title={sidebarCollapsed ? 'Expand filters' : 'Collapse filters'}
      aria-label={sidebarCollapsed ? 'Expand filters' : 'Collapse filters'}
      aria-expanded={!sidebarCollapsed}
      onclick={() => (sidebarCollapsed = !sidebarCollapsed)}
    >
      <svg
        viewBox="0 0 24 24"
        width="16"
        height="16"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        style={sidebarCollapsed ? 'transform: rotate(180deg);' : ''}
        aria-hidden="true"
      >
        <path d="m15 18-6-6 6-6" />
      </svg>
    </button>

    <aside
      id="left-sidebar"
      class:collapsed={sidebarCollapsed}
      class:open={mobileSidebarOpen}
      aria-label="Filters"
    >
      <div class="mobile-sidebar-header">
        <span>Filters</span>
        <button
          type="button"
          class="close-btn mobile-sidebar-close"
          aria-label="Close filters"
          onclick={closeMobileSidebar}
        >
          <svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12" /></svg>
        </button>
      </div>
      <div class="sidebar-content">
        <!-- Libraries Filter (All 28 Libraries) -->
        <section class="filter-section">
          <div class="filter-header">
            <h2>Libraries</h2>
            <span class="muted" id="selected-libs-count">{selectedLibsLabel}</span>
          </div>
          <input
            type="search"
            id="lib-search"
            class="mini-search"
            placeholder="Filter libraries..."
            autocomplete="off"
            bind:value={libFilterQuery}
            aria-label="Filter libraries"
          />
          <div class="lib-list" id="lib-list-container">
            <button
              type="button"
              class="lib-row all-icons-row"
              class:active={explorerState.selectedLibMask === 0}
              data-all-icons="true"
              onclick={() => explorerState.selectSingleLibrary(null)}
            >
              <span class="lib-badge" aria-hidden="true">
                <svg class="lib-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                  <path d="M4 5h16v14H4z" />
                  <path d="M8 9h8M8 13h8" />
                </svg>
              </span>
              <span class="lib-name">All Icons</span>
              <span class="lib-count">{formatNumber(totalCatalogIcons)}</span>
            </button>

            <div class="sidebar-card" id="lib-card-section" class:open={libsExpanded}>
              <button
                type="button"
                class="filter-header lib-toggle"
                id="lib-toggle"
                aria-expanded={libsExpanded}
                onclick={() => (libsExpanded = !libsExpanded)}
              >
                <h2>Libraries List</h2>
                <svg class="chevron" viewBox="0 0 24 24" aria-hidden="true">
                  <path d="m6 9 6 6 6-6" />
                </svg>
              </button>

              {#if libsExpanded}
                <div class="card-content lib-collapse-list" id="lib-collapse-list">
                  {#each filteredLibraries as lib (lib.slug)}
                    {@const isChecked = (explorerState.selectedLibMask & (1 << lib.id)) !== 0}
                    {@const liveCount = explorerState.libraryCounts[lib.id] ?? lib.count}
                    <label class="lib-row" class:active={isChecked} data-slug={lib.slug}>
                    <span class="lib-badge">
                      {@html LIBRARY_BADGE_SVGS[lib.slug] ?? '<svg class="lib-icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="3"/></svg>'}
                    </span>
                    <span class="lib-name">{lib.name}</span>
                    <span class="lib-count">{formatNumber(liveCount)}</span>
                    <input
                      class="lib-check"
                      type="checkbox"
                      value={lib.slug}
                      checked={isChecked}
                      onchange={() => explorerState.toggleLibrary(lib.id)}
                    />
                  </label>
                {/each}
                </div>
              {/if}
            </div>
          </div>
        </section>

        <!-- Styles Filter (All + 7 Styles) -->
        <section class="sidebar-card expandable" id="style-section" class:open={stylesExpanded}>
          <button
            type="button"
            class="filter-header style-toggle"
            id="style-toggle"
            aria-expanded={stylesExpanded}
            onclick={() => (stylesExpanded = !stylesExpanded)}
          >
            <h2>Styles</h2>
            <svg class="chevron" viewBox="0 0 24 24" aria-hidden="true">
              <path d="m6 9 6 6 6-6" />
            </svg>
          </button>
          {#if stylesExpanded}
            <div class="card-content style-list" id="style-list-container">
              <div class="style-pills" id="style-pills-container">
                <button
                  type="button"
                  class="style-pill"
                  class:active={explorerState.selectedStyleMask === 0}
                  data-style="all"
                  onclick={() => explorerState.clearStyles()}
                >
                  All
                </button>
                {#each styles as style, idx (style)}
                  {@const active = (explorerState.selectedStyleMask & (1 << idx)) !== 0}
                  {@const count = explorerState.styleCounts[idx] ?? 0}
                  <button
                    type="button"
                    class="style-pill"
                    class:active
                    data-style={style}
                    onclick={() => explorerState.toggleStyle(idx)}
                  >
                    <span>{formatStyleLabel(style)}</span>
                    <span class="pill-count">{formatNumber(count)}</span>
                  </button>
                {/each}
              </div>
            </div>
          {/if}
        </section>

        <!-- Categories Filter (All 16 Categories) -->
        <section class="sidebar-card expandable" id="category-section" class:open={categoriesExpanded}>
          <button
            type="button"
            class="filter-header category-toggle"
            id="category-toggle"
            aria-expanded={categoriesExpanded}
            onclick={() => (categoriesExpanded = !categoriesExpanded)}
          >
            <h2>Categories</h2>
            <svg class="chevron" viewBox="0 0 24 24" aria-hidden="true">
              <path d="m6 9 6 6 6-6" />
            </svg>
          </button>
          {#if categoriesExpanded}
            <div class="card-content category-list" id="category-list-container">
              {#each categories as category, idx (category)}
                {@const active = (explorerState.selectedCatMask & (1 << idx)) !== 0}
                {@const count = explorerState.categoryCounts[idx] ?? 0}
                <button
                  type="button"
                  class="category-pill"
                  class:active
                  data-category={category}
                  onclick={() => explorerState.toggleCategory(idx)}
                >
                  <span>{category}</span>
                  <span class="pill-count">{formatNumber(count)}</span>
                </button>
              {/each}
            </div>
          {/if}
        </section>

        <!-- Preview Size Slider -->
        <section class="filter-section">
          <div class="filter-header">
            <h2 id="preview-size-label">Preview Size: {previewState.gridSize}px</h2>
          </div>
          <input
            type="range"
            id="preview-size-slider"
            aria-label="Preview size"
            class="neon-slider"
            min="16"
            max="128"
            value={previewState.gridSize}
            oninput={(e) => previewState.setGridSize(Number((e.currentTarget as HTMLInputElement).value))}
          />
        </section>

        <!-- Sort Selector -->
        <section class="filter-section">
          <div class="filter-header">
            <h2>Sort By</h2>
          </div>
          <label class="custom-select-wrapper">
            <select
              id="sort-select"
              class="glass-select"
              value={explorerState.sort}
              onchange={(e) => explorerState.setSort((e.currentTarget as HTMLSelectElement).value)}
            >
              <option value="relevance">Relevance</option>
              <option value="az">A to Z</option>
              <option value="za">Z to A</option>
              <option value="library">By Library</option>
            </select>
            <svg class="chevron" viewBox="0 0 24 24" aria-hidden="true">
              <path d="m6 9 6 6 6-6" />
            </svg>
          </label>
          <div>
            <div class="unlocked-badge" title="Every search filter is free and unlocked.">
              All filters unlocked
            </div>
          </div>
        </section>

        <!-- Live Color & Stroke Preview Controls -->
        <section class="sidebar-card expandable" id="customize-section" class:open={customizeExpanded}>
          <button
            type="button"
            class="filter-header category-toggle"
            id="customize-toggle"
            aria-expanded={customizeExpanded}
            onclick={() => (customizeExpanded = !customizeExpanded)}
          >
            <h2>Customize Preview</h2>
            <svg class="chevron" viewBox="0 0 24 24" aria-hidden="true">
              <path d="m6 9 6 6 6-6" />
            </svg>
          </button>
          {#if customizeExpanded}
            <div class="card-content customize-preview-controls" id="customize-content">
              <div class="customize-field">
                <label for="cust-color-hex">Fill Color</label>
                <div class="customize-color-row">
                  <input
                    type="text"
                    id="cust-color-hex"
                    class="mini-search"
                    placeholder={previewState.theme === 'dark' ? '#ffffff' : '#000000'}
                    value={previewState.color}
                    aria-label="Fill color hex value"
                    oninput={(e) => previewState.setColor((e.currentTarget as HTMLInputElement).value)}
                  />
                  <button
                    type="button"
                    id="cust-color-btn"
                    class="color-wheel-btn"
                    aria-label="Choose fill color"
                    style="background: {previewState.color || (previewState.theme === 'dark' ? '#ffffff' : '#111111')};"
                    onclick={() => colorWheelEl?.click()}
                  ></button>
                  <input
                    bind:this={colorWheelEl}
                    type="color"
                    id="cust-color-wheel"
                    class="hidden-color-input"
                    value={previewState.color || (previewState.theme === 'dark' ? '#ffffff' : '#111111')}
                    tabindex="-1"
                    oninput={(e) => previewState.setColor((e.currentTarget as HTMLInputElement).value)}
                  />
                </div>
              </div>

              <div class="customize-field">
                <div class="customize-stroke-row">
                  <span>Stroke Width</span>
                  <span id="cust-stroke-label">{previewState.strokeWidth.toFixed(1)}px</span>
                </div>
                <input
                  type="range"
                  id="cust-stroke-slider"
                  aria-label="Stroke width"
                  class="neon-slider"
                  min="0.1"
                  max="3"
                  step="0.1"
                  value={previewState.strokeWidth}
                  oninput={(e) => previewState.setStrokeWidth(Number((e.currentTarget as HTMLInputElement).value))}
                />
              </div>

              <button
                type="button"
                id="cust-reset-btn"
                class="outlined-neon-btn custom-preview-reset"
                onclick={() => previewState.resetPreview()}
              >
                Reset
              </button>
            </div>
          {/if}
        </section>

        <button
          type="button"
          id="clear-filters-btn"
          class="outlined-neon-btn"
          onclick={() => {
            searchDraft = '';
            explorerState.clearFilters();
            syncHeaderSearch('');
          }}
        >
          Clear All Filters
        </button>
      </div>
    </aside>

    <!-- Main Grid Region -->
    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <main id="main-content" onclickcapture={(e) => { if (typeof document !== "undefined" && document.body.classList.contains("sidebar-open")) { e.stopPropagation(); e.preventDefault(); closeMobileSidebar(); } }}>
      <section id="grid-view" class="route-view active" style="--grid-right-inset: {gridRightInset}px;">
        <h2 class="sr-only">
          Browse {formatNumber(totalCatalogIcons)} free SVG and PNG icons across 28 open-source libraries
        </h2>

        <!-- Active Filter Pills -->
        {#if hasActiveFilters}
          <div class="active-filter-pills" aria-label="Active filters">
            {#if explorerState.query}
              <button type="button" class="filter-pill" onclick={clearSearchInput}>
                <span>Search: "{explorerState.query}"</span>
                <span aria-hidden="true">×</span>
              </button>
            {/if}

            {#each selectedLibraryIndices as libId (libId)}
              {@const lib = libraries.find((l) => l.id === libId)}
              {#if lib}
                <button
                  type="button"
                  class="filter-pill"
                  onclick={() => explorerState.toggleLibrary(libId)}
                >
                  <span>Library: {lib.name}</span>
                  <span aria-hidden="true">×</span>
                </button>
              {/if}
            {/each}

            {#each selectedCategoryIndices as catIdx (catIdx)}
              <button
                type="button"
                class="filter-pill"
                onclick={() => explorerState.toggleCategory(catIdx)}
              >
                <span>Category: {categories[catIdx]}</span>
                <span aria-hidden="true">×</span>
              </button>
            {/each}

            {#each selectedStyleIndices as styleIdx (styleIdx)}
              <button
                type="button"
                class="filter-pill"
                onclick={() => explorerState.toggleStyle(styleIdx)}
              >
                <span>Style: {formatStyleLabel(styles[styleIdx] ?? '')}</span>
                <span aria-hidden="true">×</span>
              </button>
            {/each}

            <button
              type="button"
              class="filter-pill filter-pill-clear"
              onclick={() => {
                searchDraft = '';
                explorerState.clearFilters();
                syncHeaderSearch('');
              }}
            >
              Clear all
            </button>
          </div>
        {/if}

        <!-- Toolbar -->
        <div class="main-toolbar">
          <div class="toolbar-left">
            <span id="grid-status" role="status" aria-live="polite" aria-atomic="true">
              {#if !explorerState.ready && explorerState.loading}
                Loading icon index...
              {:else}
                {hasActiveFilters ? `Showing ${formatNumber(explorerState.totalMatches)} icons` : `All icons: ${formatNumber(explorerState.totalMatches)}`}
              {/if}
            </span>
            {#if explorerState.ready && explorerState.elapsedMs > 0}
              <span class="muted" id="load-status"></span>
            {/if}
          </div>

          <div class="toolbar-right">
            <a href="/api/" class="toolbar-api-link" title="Free static API &amp; MCP server for developers">API &amp; MCP</a>
            <div class="density-toggle" role="group" aria-label="Grid density">
              {#each (['compact', 'default', 'comfortable'] as readonly GridDensity[]) as mode (mode)}
                <button
                  type="button"
                  class="density-btn"
                  class:active={previewState.density === mode}
                  data-density={mode}
                  title={mode.charAt(0).toUpperCase() + mode.slice(1)}
                  aria-label="{mode} density"
                  aria-pressed={previewState.density === mode}
                  onclick={() => previewState.setDensity(mode)}
                >
                  {#if mode === 'compact'}
                    <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
                      <path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z" />
                    </svg>
                  {:else if mode === 'default'}
                    <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
                      <path d="M3 3h8v8H3zM13 3h8v8h-8zM3 13h8v8H3zM13 13h8v8h-8z" />
                    </svg>
                  {:else}
                    <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
                      <path d="M4 4h16v16H4z" />
                    </svg>
                  {/if}
                </button>
              {/each}
            </div>

            <button
              type="button"
              id="select-mode-btn"
              class="glass-btn"
              class:active={collectionsState.selectMode}
              aria-pressed={collectionsState.selectMode}
              onclick={() => collectionsState.toggleSelectMode()}
            >
              {collectionsState.selectMode
                ? `Selected (${collectionsState.selectedIds.size})`
                : 'Select'}
            </button>

            </div>
        </div>

        <!-- Virtualized Icon Grid (<= 180 DOM tiles) -->
        <div class="ad-slot top-ad has-api-banner">
          <a class="api-strip api-strip-ad" href="/api/" aria-label="Explore the free IconStash API and MCP server">
            <span class="api-strip-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m8 8-4 4 4 4M16 8l4 4-4 4M13 5l-2 14"/></svg></span>
            <span class="api-strip-text"><strong>Free API &amp; MCP</strong> &mdash; use all 134,701 icons in your app, build, or AI assistant.</span>
            <span class="api-strip-cta">Explore <span aria-hidden="true">&rarr;</span></span>
          </a>
        </div>

        <VirtualIconGrid
          bind:this={gridRef}
          bind:focusedPos
          onGridInsetChange={(inset) => {
            gridRightInset = inset;
          }}
          onSuggestionClick={(term) => {
            searchDraft = term;
            syncHeaderSearch(term);
          }}
        />
      </section>
    </main>
  </div>

  <!-- Live Toast Container -->
  {#if inspectorState.toastMessage}
    <div id="toast-container" aria-live="polite" role="status">
      <div class="toast">{inspectorState.toastMessage}</div>
    </div>
  {/if}
</div>

<style>
  .explorer-shell {
    display: flex;
    flex-direction: column;
    flex: 1 1 0%;
    min-width: 0;
    min-height: 0;
    width: 100%;
    height: 100%;
    position: relative;
  }

  .workspace {
    flex: 1 1 0%;
    display: flex;
    min-width: 0;
    min-height: 0;
    width: 100%;
    overflow: hidden;
    position: relative;
  }

  .mobile-sidebar-header {
    display: none;
  }

  #left-sidebar {
    width: var(--sidebar-width, 260px);
    flex-shrink: 0;
    border-right: 1px solid var(--border, #1f1f1f);
    background: var(--bg-base, #0a0a0a);
    overflow-y: auto;
    transition: width 160ms ease, transform 180ms ease;
  }

  #left-sidebar.collapsed {
    width: 0;
    border-right: none;
    overflow: hidden;
  }

  @media (max-width: 1199px) {
    .mobile-sidebar-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 14px;
      border-bottom: 1px solid var(--border, #1f1f1f);
      font-family: var(--font-mono, monospace);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-secondary, #888888);
    }

    .mobile-sidebar-close {
      width: 30px;
      height: 30px;
    }

    #left-sidebar {
      width: min(280px, 85vw);
    }
  }

  .sidebar-content {
    padding: 12px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .filter-section,
  .sidebar-card {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .sidebar-card {
    background: var(--bg-surface, #111111);
    border: 1px solid var(--border, #1f1f1f);
    border-radius: var(--radius-card, 8px);
    padding: 8px 10px;
  }

  .filter-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    background: transparent;
    border: none;
    padding: 0;
    width: 100%;
    text-align: left;
    color: var(--text-secondary, #888888);
  }

  button.filter-header {
    cursor: pointer;
  }

  .filter-header h2 {
    margin: 0;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--text-secondary, #888888);
  }

  .chevron {
    width: 15px;
    height: 15px;
    fill: none;
    stroke: currentColor;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
    transition: transform 180ms ease;
  }

  .sidebar-card.expanded > .filter-header .chevron {
    transform: rotate(180deg);
  }

  .mini-search {
    width: 100%;
    height: 32px;
    padding: 0 10px;
    border-radius: var(--radius-button, 6px);
    border: 1px solid var(--border, #1f1f1f);
    background: var(--bg-surface, #111111);
    color: var(--text-primary, #f2f2f2);
    font-size: 12px;
  }

  .lib-collapse-list {
    display: flex;
    flex-direction: column;
    gap: 2px;
    max-height: 280px;
    overflow-y: auto;
    margin-top: 4px;
  }

  .lib-row-wrapper {
    display: flex;
    align-items: center;
    gap: 4px;
  }

  .lib-row {
    flex: 1;
    min-width: 0;
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 6px 8px;
    border-radius: var(--radius-button, 6px);
    border: 1px solid transparent;
    background: transparent;
    color: var(--text-primary, #f2f2f2);
    font-size: 12px;
    cursor: pointer;
    text-align: left;
  }

  .lib-row:hover {
    background: var(--bg-hover, #141414);
  }

  .lib-row.active {
    background: var(--bg-elevated, #161616);
    border-color: var(--control-blue, #c1dd2d);
  }

  .lib-check {
    position: absolute;
    width: 1px;
    height: 1px;
    opacity: 0;
    pointer-events: none;
  }

  .lib-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .lib-icon {
    width: 14px;
    height: 14px;
  }

  .lib-name {
    flex: 1;
    min-width: 0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .lib-count {
    font-size: 11px;
    font-family: var(--font-mono, monospace);
    color: var(--text-muted, #8a8a8a);
  }

  .lib-row-meta {
    display: flex;
    align-items: center;
    gap: 2px;
    flex-shrink: 0;
  }

  .lib-meta-btn {
    padding: 2px 5px;
    font-size: 10px;
    font-family: var(--font-mono, monospace);
    border-radius: 4px;
    border: 1px solid var(--border, #1f1f1f);
    background: var(--bg-elevated, #161616);
    color: var(--text-muted, #8a8a8a);
    text-decoration: none;
    cursor: pointer;
  }

  .lib-meta-btn:hover {
    color: var(--text-primary, #f2f2f2);
    border-color: var(--border-hover, #2a2a2a);
  }

  .style-pills,
  .category-list {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 4px;
  }

  .style-pill,
  .category-pill {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 4px 8px;
    border-radius: var(--radius-button, 6px);
    border: 1px solid var(--border, #1f1f1f);
    background: var(--bg-elevated, #161616);
    color: var(--text-secondary, #888888);
    font-size: 11px;
    cursor: pointer;
  }

  .style-pill.active,
  .category-pill.active {
    background: var(--btn-primary-bg, #c1dd2d);
    color: var(--btn-primary-text, #0a0a0a);
    border-color: var(--btn-primary-bg, #c1dd2d);
    font-weight: 600;
  }

  .pill-count {
    font-size: 10px;
    opacity: 0.75;
    font-family: var(--font-mono, monospace);
  }

  .customize-color-row {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .color-wheel-btn {
    width: 28px;
    height: 28px;
    border-radius: 6px;
    border: 1px solid var(--border-hover, #2a2a2a);
    cursor: pointer;
    flex-shrink: 0;
  }

  .hidden-color-input {
    position: absolute;
    width: 1px;
    height: 1px;
    opacity: 0;
    pointer-events: none;
  }

  .customize-stroke-row {
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    color: var(--text-secondary, #888888);
  }

  #main-content {
    flex: 1;
    min-width: 0;
    min-height: 0;
    display: flex;
    flex-direction: column;
  }

  #grid-view {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
  }

  .active-filter-pills {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 6px;
    padding: 8px 16px 0;
  }

  .filter-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 10px;
    border-radius: 999px;
    border: 1px solid var(--border-hover, #2a2a2a);
    background: var(--bg-elevated, #161616);
    color: var(--text-primary, #f2f2f2);
    font-size: 11px;
    cursor: pointer;
  }

  .filter-pill-clear {
    border-color: var(--neon-red, #ff6b6b);
    color: var(--neon-red, #ff6b6b);
    background: transparent;
  }

  .main-toolbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
    padding: 6px 0;
  }

  .toolbar-left,
  .toolbar-right {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }

  @media (max-width: 767px) {
    .main-toolbar {
      flex-direction: column;
      align-items: stretch;
      gap: 8px;
    }

    .toolbar-left {
      justify-content: flex-start;
    }

    .toolbar-right {
      justify-content: space-between;
      width: 100%;
    }
  }

  @media (max-width: 420px) {
    .density-toggle {
      display: none;
    }
  }

  #grid-status {
    font-size: 13px;
    font-weight: 600;
    color: var(--text-primary, #f2f2f2);
  }

  .muted {
    font-size: 12px;
    color: var(--text-muted, #8a8a8a);
  }

  .density-toggle {
    display: inline-flex;
    border: 1px solid var(--border, #1f1f1f);
    border-radius: var(--radius-button, 6px);
    overflow: hidden;
  }

  @media (max-width: 420px) {
    .density-toggle {
      display: none;
    }
  }

  .density-btn {
    padding: 5px 8px;
    background: var(--bg-surface, #111111);
    border: none;
    color: var(--text-muted, #8a8a8a);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
  }

  .density-btn.active {
    background: var(--btn-primary-bg, #c1dd2d);
    color: var(--btn-primary-text, #0a0a0a);
  }

  .glass-btn,
  .outlined-neon-btn {
    padding: 6px 10px;
    border-radius: var(--radius-button, 6px);
    border: 1px solid var(--border, #1f1f1f);
    background: var(--bg-surface, #111111);
    color: var(--text-primary, #f2f2f2);
    font-size: 12px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }

  .glass-btn:hover,
  .outlined-neon-btn:hover {
    border-color: var(--control-blue, #c1dd2d);
  }

  .glass-btn.active {
    background: var(--btn-primary-bg, #c1dd2d);
    color: var(--btn-primary-text, #0a0a0a);
    border-color: var(--btn-primary-bg, #c1dd2d);
    font-weight: 700;
  }

  .badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 18px;
    height: 18px;
    padding: 0 5px;
    border-radius: 999px;
    background: var(--btn-primary-bg, #c1dd2d);
    color: var(--btn-primary-text, #0a0a0a);
    font-size: 10px;
    font-weight: 700;
  }

  #toast-container {
    position: fixed;
    right: 18px;
    bottom: 18px;
    z-index: 130;
    pointer-events: none;
  }

  .toast {
    padding: 10px 14px;
    border-radius: var(--radius-card, 8px);
    background: var(--bg-elevated, #161616);
    border: 1px solid var(--control-blue, #c1dd2d);
    color: var(--text-primary, #f2f2f2);
    font-size: 12px;
    font-weight: 500;
  }
</style>
