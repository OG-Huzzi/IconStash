<script lang="ts">
  import { inspectorState } from '../lib/state/inspector.svelte';
  import { previewState } from '../lib/state/preview.svelte';
  import { collectionsState } from '../lib/state/collections.svelte';
  import { explorerState, type ResolvedIcon } from '../lib/state/explorer.svelte';
  import { renderCustomizedSvg } from '../lib/svg/effects';
  import { formatCode, toPascalCase } from '../lib/svg/codegen';
  import {
    addGradientStop,
    removeGradientStop,
    textureUsesMaterial,
    createDefaultCustomizationState,
    ROUNDNESS_ORDER,
    MAX_GRADIENT_STOPS,
    MIN_GRADIENT_STOPS,
    type CodeFormat,
    type CustomizationState,
    type GradientProjection,
    type IconSvgInput,
    type MotionEasing,
    type MotionType,
    type RoundnessPreset,
    type SurfaceTexture,
  } from '../lib/svg/types';
  import {
    exportPng,
    exportZip,
    downloadBlob,
    PNG_EXPORT_SIZES,
    DETAIL_ZIP_PNG_SIZES,
    buildPngFilename,
    type ExportSvgInput,
  } from '../lib/export/client';
  import { slugFilePart } from '../lib/svg/normalize';

  type RichIcon = ResolvedIcon & {
    libraryVersion?: string;
    tags?: string[];
    jsxImport?: string;
  };

  const COLOR_SWATCHES = [
    '#2563eb',
    '#C1DD2D',
    '#ffffff',
    '#111111',
    '#ff6b6b',
    '#00c3ff',
    '#a855f7',
    '#f59e0b',
    '#10b981',
  ] as const;

  const FORMAT_OPTIONS: ReadonlyArray<{ id: CodeFormat; label: string; desc: string }> = [
    { id: 'svg', label: 'SVG', desc: 'vector code' },
    { id: 'xml', label: 'XML', desc: 'svg file' },
    { id: 'jsx', label: 'JSX', desc: 'react' },
    { id: 'vue', label: 'Vue', desc: 'component' },
    { id: 'svelte', label: 'Svelte', desc: 'component' },
    { id: 'angular', label: 'Angular', desc: 'template' },
    { id: 'html', label: 'HTML img', desc: 'fallback' },
    { id: 'css', label: 'CSS bg', desc: 'mask' },
    { id: 'base64', label: 'Base64', desc: 'data uri' },
  ];

  const TEXTURE_OPTIONS: ReadonlyArray<{ id: SurfaceTexture; label: string }> = [
    { id: 'none', label: 'None' },
    { id: 'paper', label: 'Paper' },
    { id: 'concrete', label: 'Concrete' },
    { id: 'marble', label: 'Marble' },
    { id: 'wood', label: 'Wood' },
    { id: 'metal', label: 'Metal' },
  ];

  const ROUNDNESS_LABELS: Record<RoundnessPreset, string> = {
    soft: 'Soft',
    round: 'Round',
    medium: 'Medium',
    sharp: 'Sharp',
  };

  const EASING_OPTIONS: ReadonlyArray<{ id: MotionEasing; label: string }> = [
    { id: 'inout', label: 'In-Out' },
    { id: 'in', label: 'In' },
    { id: 'out', label: 'Out' },
    { id: 'linear', label: 'Linear' },
  ];

  const FALLBACK_CUSTOM = createDefaultCustomizationState();

  let advanceOpen = $state(false);
  let activeTab = $state<'copy' | 'download' | 'project' | 'meta'>('copy');
  let activeFormat = $state<CodeFormat>('svg');
  let activePngSize = $state<number>(256);
  let previewBg = $state<'dark' | 'light' | 'checkered'>('dark');
  let previewBgManual = $state(false);
  let copyMenuOpen = $state(false);
  let downloadMenuOpen = $state(false);
  let collectionDropdownOpen = $state(false);
  let newCollectionName = $state('');
  let copyFlash = $state(false);
  let exporting = $state(false);
  let matches = $state<RichIcon[]>([]);
  let matchesLoading = $state(false);

  const activeIcon = $derived(inspectorState.activeIcon as RichIcon | null);
  const custom = $derived<CustomizationState>(inspectorState.custom ?? FALLBACK_CUSTOM);
  const colorLocked = $derived(textureUsesMaterial(custom.effects.texture));
  const roundnessIndex = $derived(
    Math.max(0, ROUNDNESS_ORDER.indexOf(custom.effects.roundness ?? 'round')),
  );
  const effectivePreviewBg = $derived(
    previewBgManual ? previewBg : previewState.theme === 'light' ? 'light' : 'dark',
  );

  const exportWidth = $derived(custom.width ?? custom.size ?? 128);
  const exportHeight = $derived(custom.height ?? custom.size ?? 128);

  const renderOptions = $derived({
    color: custom.color,
    strokeWidth: custom.strokeWidth,
    size: custom.size,
    width: custom.width ?? custom.size,
    height: custom.height ?? custom.size,
    gradient: custom.gradient,
    effects: custom.effects,
    motion: custom.motion,
  });

  const previewSvg = $derived.by(() => {
    if (!activeIcon) return '';
    const previewDim = Math.min(160, Math.max(96, custom.size));
    return renderCustomizedSvg(activeIcon, {
      ...renderOptions,
      size: previewDim,
      width: previewDim,
      height: previewDim,
    });
  });

  const codePreview = $derived.by(() => {
    if (!activeIcon) return '';
    return formatCode(activeIcon, activeFormat, renderOptions);
  });

  const libraryMeta = $derived.by(() => {
    if (!activeIcon || !explorerState.meta?.libraries) return null;
    return (
      explorerState.meta.libraries.find(
        (lib: { slug: string }) => lib.slug === activeIcon.librarySlug,
      ) ?? null
    );
  });

  const npmPackageName = $derived(
    activeIcon?.npmPackage || libraryMeta?.npmPackage || activeIcon?.librarySlug || 'lucide',
  );
  const docsUrl = $derived(activeIcon?.docsUrl || libraryMeta?.docsUrl || '#');
  const libraryDisplay = $derived(activeIcon?.library || libraryMeta?.name || activeIcon?.librarySlug || 'IconStash');
  const libraryVersion = $derived(activeIcon?.libraryVersion || libraryMeta?.version || '');
  const installCommand = $derived(`npm install ${npmPackageName}`);
  const importStatement = $derived(
    activeIcon?.jsxImport ||
      `import { ${toPascalCase(activeIcon?.name)} } from '${npmPackageName}';`,
  );

  const isFav = $derived(activeIcon ? collectionsState.isFavorite(activeIcon.id) : false);

  const collectionNames = $derived.by(() => {
    const raw = collectionsState.collections as unknown;
    if (!raw) return [] as string[];
    if (Array.isArray(raw)) {
      return raw
        .map((c: { id?: string; name?: string }) => c.name || c.id || '')
        .filter((n: string) => Boolean(n) && n.toLowerCase() !== 'favorites');
    }
    if (raw instanceof Map) {
      return Array.from(raw.keys()).filter((n) => String(n).toLowerCase() !== 'favorites');
    }
    if (typeof raw === 'object') {
      return Object.keys(raw as Record<string, unknown>).filter(
        (n) => n.toLowerCase() !== 'favorites',
      );
    }
    return [] as string[];
  });

  function isInCollection(name: string, iconId: string): boolean {
    const raw = collectionsState.collections as unknown;
    if (!raw) return false;
    if (Array.isArray(raw)) {
      const col = raw.find((c: { name?: string; id?: string }) => c.name === name || c.id === name);
      return Boolean(col && Array.isArray(col.icons) && col.icons.includes(iconId));
    }
    if (raw instanceof Map) {
      const ids = raw.get(name);
      return Array.isArray(ids) ? ids.includes(iconId) : ids instanceof Set ? ids.has(iconId) : false;
    }
    if (typeof raw === 'object') {
      const ids = (raw as Record<string, unknown>)[name];
      return Array.isArray(ids) ? ids.includes(iconId) : ids instanceof Set ? ids.has(iconId) : false;
    }
    return false;
  }

  const gradBarCss = $derived.by(() => {
    const stops = custom.gradient.stops
      .slice()
      .sort((a, b) => a.p - b.p)
      .map((s) => `${s.c} ${s.p}%`)
      .join(', ');
    if (custom.gradient.projection === 'radial') {
      return `radial-gradient(circle at ${custom.gradient.cx}% ${custom.gradient.cy}%, ${stops})`;
    }
    return `linear-gradient(${custom.gradient.angle}deg, ${stops})`;
  });


  $effect(() => {
    const icon = activeIcon;
    if (!icon) {
      matches = [];
      advanceOpen = false;
      copyMenuOpen = false;
      downloadMenuOpen = false;
      collectionDropdownOpen = false;
      return;
    }

    let cancelled = false;
    matchesLoading = true;

    (async () => {
      try {
        const list = await explorerState.findConceptMatches(icon.name);
        const resolved: RichIcon[] = list
          .filter((candidate) => candidate && candidate.id !== icon.id)
          .slice(0, 8);
        if (!cancelled) {
          matches = resolved;
        }
      } catch {
        if (!cancelled) matches = [];
      } finally {
        if (!cancelled) matchesLoading = false;
      }
    })();

    return () => {
      cancelled = true;
    };
  });

  function patchCustom(patch: Partial<CustomizationState>) {
    inspectorState.updateCustom(patch);
  }

  function patchGradient(patch: Partial<CustomizationState['gradient']>) {
    inspectorState.updateCustom({
      gradient: { ...custom.gradient, ...patch },
    });
  }

  function patchEffects(patch: Partial<CustomizationState['effects']>) {
    inspectorState.updateCustom({
      effects: { ...custom.effects, ...patch },
    });
  }

  function patchMotion(patch: Partial<CustomizationState['motion']>) {
    inspectorState.updateCustom({
      motion: { ...custom.motion, ...patch },
    });
  }

  function handleColorChange(nextColor: string) {
    patchCustom({ color: nextColor });
    previewState.setColor(nextColor);
  }

  function handleStrokeChange(nextStroke: number) {
    patchCustom({ strokeWidth: nextStroke });
  }

  function handleSizeSlider(nextSize: number) {
    const clamped = Math.min(256, Math.max(16, Math.round(nextSize)));
    patchCustom({ size: clamped, width: clamped, height: clamped });
  }

  function handleWidthInput(nextWidth: number) {
    const clamped = Math.min(512, Math.max(16, Math.round(nextWidth || 128)));
    patchCustom({ width: clamped, size: Math.min(256, clamped) });
  }

  function handleHeightInput(nextHeight: number) {
    const clamped = Math.min(512, Math.max(16, Math.round(nextHeight || 128)));
    patchCustom({ height: clamped });
  }

  function setPreviewBg(bg: 'dark' | 'light' | 'checkered') {
    previewBg = bg;
    previewBgManual = true;
  }

  function toggleShadow() {
    const nextOn = !custom.effects.shadowOn;
    patchEffects({ shadowOn: nextOn });
    if (nextOn && effectivePreviewBg === 'dark') {
      setPreviewBg('light');
    }
  }

  function handleAddStop() {
    const nextStops = addGradientStop(custom.gradient.stops);
    patchGradient({ stops: nextStops });
  }

  function handleRemoveStop(index: number) {
    const nextStops = removeGradientStop(custom.gradient.stops, index);
    patchGradient({ stops: nextStops });
  }

  function handleStopColor(index: number, color: string) {
    const nextStops = custom.gradient.stops.map((s, i) => (i === index ? { ...s, c: color } : s));
    patchGradient({ stops: nextStops });
  }

  function handleStopPos(index: number, pos: number) {
    const clamped = Math.min(100, Math.max(0, Math.round(Number(pos) || 0)));
    const nextStops = custom.gradient.stops.map((s, i) => (i === index ? { ...s, p: clamped } : s));
    patchGradient({ stops: nextStops });
  }

  function handleRoundnessSlider(idx: number) {
    const preset = ROUNDNESS_ORDER[Math.min(3, Math.max(0, Math.round(idx)))] ?? 'round';
    patchEffects({ roundness: preset });
  }

  function selectMotionType(type: 'off' | MotionType) {
    if (type === 'off') {
      patchMotion({ on: false });
    } else {
      patchMotion({ on: true, type });
    }
  }

  async function copyTextToClipboard(text: string, label: string) {
    try {
      await navigator.clipboard.writeText(text);
      inspectorState.showToast(label);
    } catch {
      const textarea = document.createElement('textarea');
      textarea.value = text;
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      textarea.remove();
      inspectorState.showToast(label);
    }
  }

  async function handleCopyFormat(fmt: CodeFormat) {
    if (!activeIcon) return;
    activeFormat = fmt;
    copyMenuOpen = false;
    const code = formatCode(activeIcon, fmt, renderOptions);
    const label = FORMAT_OPTIONS.find((f) => f.id === fmt)?.label ?? 'SVG';
    await copyTextToClipboard(code, `Copied as ${label}`);
    copyFlash = true;
    setTimeout(() => {
      copyFlash = false;
    }, 1200);
  }

  function handleDownloadSvg() {
    if (!activeIcon) return;
    const svg = renderCustomizedSvg(activeIcon, renderOptions);
    const blob = new Blob([svg], { type: 'image/svg+xml;charset=utf-8' });
    const filename = `${slugFilePart(activeIcon.librarySlug || 'iconstash')}-${slugFilePart(activeIcon.name)}.svg`;
    downloadBlob(blob, filename);
    inspectorState.showToast('SVG downloaded');
  }

  async function handleDownloadPng(size = activePngSize) {
    if (!activeIcon || exporting) return;
    activePngSize = size;
    downloadMenuOpen = false;
    exporting = true;
    try {
      const svgMarkup = renderCustomizedSvg(activeIcon, {
        ...renderOptions,
        size,
        width: size,
        height: size,
      });
      const filename = buildPngFilename(
        activeIcon.librarySlug || 'iconstash',
        activeIcon.name,
        size,
      );
      await exportPng({
        svgMarkup,
        filename,
        size,
        scale: typeof window !== 'undefined' ? Math.min(2, window.devicePixelRatio || 1) : 1,
      });
      inspectorState.showToast(`PNG ${size}px downloaded`);
    } catch {
      inspectorState.showToast('PNG export failed');
    } finally {
      exporting = false;
    }
  }

  async function handleDownloadZip() {
    if (!activeIcon || exporting) return;
    exporting = true;
    inspectorState.showToast('Packaging icon ZIP...');
    try {
      const svgMarkup = renderCustomizedSvg(activeIcon, renderOptions);
      const item: ExportSvgInput = {
        id: activeIcon.id,
        name: activeIcon.name,
        librarySlug: activeIcon.librarySlug || 'iconstash',
        library: libraryDisplay,
        tags: activeIcon.tags,
        license: activeIcon.license,
        svgMarkup,
      };
      await exportZip({
        icons: [item],
        pngSizes: DETAIL_ZIP_PNG_SIZES,
        archiveKind: 'detail',
        archiveTitle: activeIcon.name,
      });
      inspectorState.showToast('ZIP downloaded');
    } catch {
      inspectorState.showToast('ZIP export failed');
    } finally {
      exporting = false;
    }
  }

  function handleToggleFavorite() {
    if (!activeIcon) return;
    collectionsState.toggleFavorite(activeIcon.id);
    const nowFav = collectionsState.isFavorite(activeIcon.id);
    inspectorState.showToast(nowFav ? 'Added to Favorites' : 'Removed from Favorites');
  }

  function handleToggleCollection(colName: string) {
    if (!activeIcon) return;
    if (isInCollection(colName, activeIcon.id)) {
      collectionsState.removeFromCollection(colName, activeIcon.id);
      inspectorState.showToast(`Removed from ${colName}`);
    } else {
      collectionsState.addToCollection(colName, activeIcon.id);
      inspectorState.showToast(`Added to ${colName}`);
    }
  }

  function handleCreateAndAddCollection() {
    if (!activeIcon) return;
    const trimmed = newCollectionName.trim();
    if (!trimmed) return;
    collectionsState.createCollection(trimmed);
    collectionsState.addToCollection(trimmed, activeIcon.id);
    newCollectionName = '';
    inspectorState.showToast(`Added to ${trimmed}`);
  }

  function handleShare() {
    if (!activeIcon || typeof window === 'undefined') return;
    const url = `${window.location.origin}/#/icon/${encodeURIComponent(activeIcon.id)}`;
    copyTextToClipboard(url, 'Icon link copied');
  }

  function handleCompare() {
    if (!activeIcon) return;
    inspectorState.openCompare(activeIcon.name);
  }

  function handleGlobalClick(e: MouseEvent) {
    const target = e.target as HTMLElement | null;
    if (!target) return;
    if (!target.closest('#qa-copy-split')) copyMenuOpen = false;
    if (!target.closest('#qa-download-split')) downloadMenuOpen = false;
    if (!target.closest('.dp-collection-picker')) collectionDropdownOpen = false;
  }
</script>

<svelte:window onclick={handleGlobalClick} />

<aside
  id="detail-panel"
  class:closed={!activeIcon}
  aria-label="Icon detail panel"
  aria-hidden={!activeIcon}
>
  <div class="panel-header">
    <div>
      <span class="eyebrow" id="dp-library-name">
        {activeIcon ? `${libraryDisplay} / ${activeIcon.name}` : 'IconStash'}
      </span>
      <h2 id="dp-title">{activeIcon ? 'Customize' : 'Icon Details'}</h2>
    </div>
    <div class="panel-header-actions">
      <button
        type="button"
        class="advance-toggle"
        class:active={advanceOpen}
        id="dp-advance-toggle"
        aria-pressed={advanceOpen}
        title="Advanced effects and motion"
        onclick={() => (advanceOpen = !advanceOpen)}
      >
        Advance
      </button>
      <button
        type="button"
        class="close-btn"
        id="dp-close"
        aria-label="Close details"
        onclick={() => {
          advanceOpen = false;
          inspectorState.closeInspector();
        }}
      >
        <svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12" /></svg>
      </button>
    </div>
  </div>

  {#if activeIcon}
    <div class="panel-content">
      <section class="dp-preview-area">
        <div
          class="preview-box"
          class:bg-dark={effectivePreviewBg === 'dark'}
          class:bg-light={effectivePreviewBg === 'light'}
          class:checkered-dot={effectivePreviewBg === 'checkered'}
          id="dp-preview-box"
          data-preview-dim={Math.min(156, Math.max(96, custom.size))}
          style={'--dp-preview-dim:' + Math.min(156, Math.max(96, custom.size)) + 'px;' + (effectivePreviewBg === 'light'
            ? 'background:#ffffff;'
            : effectivePreviewBg === 'dark'
              ? 'background:#0a0a0a;'
              : '')}
        >
          {@html previewSvg}
        </div>

        <div class="preview-controls">
          <button
            type="button"
            class="bg-toggle"
            class:active={effectivePreviewBg === 'dark'}
            data-bg="dark"
            title="Dark background"
            aria-label="Dark preview background"
            onclick={() => setPreviewBg('dark')}
          ></button>
          <button
            type="button"
            class="bg-toggle"
            class:active={effectivePreviewBg === 'light'}
            data-bg="light"
            title="Light background"
            aria-label="Light preview background"
            onclick={() => setPreviewBg('light')}
          ></button>
          <button
            type="button"
            class="bg-toggle checkered-dot"
            class:active={effectivePreviewBg === 'checkered'}
            data-bg="checkered"
            title="Checkered background"
            aria-label="Checkered preview background"
            onclick={() => setPreviewBg('checkered')}
          ></button>
        </div>

        <label class="range-label" for="dp-size-slider">
          Preview Size <span id="dp-size-val">{custom.size}px</span>
        </label>
        <input
          type="range"
          id="dp-size-slider"
          aria-label="Preview size"
          class="neon-slider"
          min="16"
          max="256"
          value={custom.size}
          oninput={(e) => handleSizeSlider(Number((e.currentTarget as HTMLInputElement).value))}
        />

        <div class="dp-quick-actions" id="dp-quick-actions">
          <div class="qa-split" class:qa-success={copyFlash} id="qa-copy-split">
            <button
              type="button"
              class="qa-btn qa-main"
              id="qa-copy-btn"
              title="Copy icon code"
              onclick={() => handleCopyFormat(activeFormat)}
            >
              <svg
                viewBox="0 0 24 24"
                width="15"
                height="15"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                aria-hidden="true"
              >
                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
              </svg>
              <span id="qa-copy-label">
                {copyFlash
                  ? 'Copied!'
                  : `Copy ${FORMAT_OPTIONS.find((f) => f.id === activeFormat)?.label ?? 'SVG'}`}
              </span>
            </button>
            <button
              type="button"
              class="qa-btn qa-caret"
              id="qa-copy-caret"
              aria-haspopup="menu"
              aria-expanded={copyMenuOpen}
              aria-controls="qa-copy-menu"
              title="Copy as…"
              aria-label="Choose copy format"
              onclick={(e) => {
                e.stopPropagation();
                downloadMenuOpen = false;
                copyMenuOpen = !copyMenuOpen;
              }}
            >
              <svg
                viewBox="0 0 24 24"
                width="14"
                height="14"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                aria-hidden="true"
              >
                <path d="m6 9 6 6 6-6"></path>
              </svg>
            </button>
            <div
              class="qa-menu"
              class:hidden={!copyMenuOpen}
              id="qa-copy-menu"
              role="menu"
              aria-label="Copy format"
            >
              {#each FORMAT_OPTIONS as fmt}
                <button
                  type="button"
                  class="qa-menu-item"
                  class:active={activeFormat === fmt.id}
                  role="menuitem"
                  data-copy-fmt={fmt.id}
                  onclick={() => handleCopyFormat(fmt.id)}
                >
                  <span>{fmt.label}</span>
                  <em>{fmt.desc}</em>
                </button>
              {/each}
            </div>
          </div>

          <div class="qa-split" id="qa-download-split">
            <button
              type="button"
              class="qa-btn qa-main"
              id="qa-download-btn"
              title="Download PNG"
              disabled={exporting}
              onclick={() => handleDownloadPng(activePngSize)}
            >
              <svg
                viewBox="0 0 24 24"
                width="15"
                height="15"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                aria-hidden="true"
              >
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="7 10 12 15 17 10"></polyline>
                <line x1="12" y1="15" x2="12" y2="3"></line>
              </svg>
              <span id="qa-download-label">PNG {activePngSize}</span>
            </button>
            <button
              type="button"
              class="qa-btn qa-caret"
              id="qa-download-caret"
              aria-haspopup="menu"
              aria-expanded={downloadMenuOpen}
              aria-controls="qa-download-menu"
              title="PNG size"
              aria-label="Choose PNG size"
              onclick={(e) => {
                e.stopPropagation();
                copyMenuOpen = false;
                downloadMenuOpen = !downloadMenuOpen;
              }}
            >
              <svg
                viewBox="0 0 24 24"
                width="14"
                height="14"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                aria-hidden="true"
              >
                <path d="m6 9 6 6 6-6"></path>
              </svg>
            </button>
            <div
              class="qa-menu"
              class:hidden={!downloadMenuOpen}
              id="qa-download-menu"
              role="menu"
              aria-label="Download PNG size"
            >
              {#each PNG_EXPORT_SIZES as sz}
                <button
                  type="button"
                  class="qa-menu-item"
                  class:active={activePngSize === sz}
                  role="menuitem"
                  data-dl-size={sz}
                  onclick={() => handleDownloadPng(sz)}
                >
                  <span>PNG</span>
                  <em>{sz} px</em>
                </button>
              {/each}
            </div>
          </div>

          <label
            class="qa-color-btn"
            class:disabled={colorLocked}
            id="qa-color-btn"
            for="dp-color-input"
            title={colorLocked ? 'Color locked by material texture' : 'Change color'}
          >
            <span class="qa-color-wheel" aria-hidden="true">
              <span class="qa-color-dot" id="qa-color-dot" style={`background:${custom.color}`}></span>
            </span>
            <input
              type="color"
              id="dp-color-input"
              value={custom.color}
              disabled={colorLocked}
              title="Custom color"
              aria-label="Icon color"
              oninput={(e) => handleColorChange((e.currentTarget as HTMLInputElement).value)}
            />
          </label>
        </div>
      </section>

      <section class="dp-section">
        <h3>Customize</h3>
        <div class="chip-row" id="fill-mode-row">
          <button
            type="button"
            class="format-btn"
            class:active={!custom.gradient.on}
            data-fill-mode="solid"
            disabled={colorLocked}
            onclick={() => patchGradient({ on: false })}
          >
            Solid
          </button>
          <button
            type="button"
            class="format-btn"
            class:active={custom.gradient.on}
            data-fill-mode="gradient"
            disabled={colorLocked}
            onclick={() => patchGradient({ on: true })}
          >
            Gradient
          </button>
        </div>

        {#if !custom.gradient.on}
          <div class="color-swatches-row" aria-label="Color presets">
            {#each COLOR_SWATCHES as swatch}
              <button
                type="button"
                class="color-preset"
                class:active={custom.color.toLowerCase() === swatch.toLowerCase()}
                class:bordered={swatch === '#ffffff' || swatch === '#111111'}
                style={`background:${swatch}`}
                title={swatch}
                aria-label={`Set color ${swatch}`}
                disabled={colorLocked}
                onclick={() => handleColorChange(swatch)}
              ></button>
            {/each}
          </div>
        {/if}

        <div id="gradient-controls" class:hidden={!custom.gradient.on || colorLocked}>
          <div class="grad-preview" id="grad-preview" style={`background:${gradBarCss}`}></div>
          <div id="gradient-stops">
            {#each custom.gradient.stops as stop, idx}
              <div class="grad-stop-row">
                <input
                  type="color"
                  aria-label={`Gradient stop ${idx + 1} color`}
                  value={stop.c}
                  oninput={(e) =>
                    handleStopColor(idx, (e.currentTarget as HTMLInputElement).value)}
                />
                <input
                  type="number"
                  class="grad-stop-pos"
                  min="0"
                  max="100"
                  aria-label={`Gradient stop ${idx + 1} position`}
                  value={stop.p}
                  oninput={(e) =>
                    handleStopPos(idx, Number((e.currentTarget as HTMLInputElement).value))}
                />
                <span class="muted">%</span>
                {#if custom.gradient.stops.length > MIN_GRADIENT_STOPS}
                  <button
                    type="button"
                    class="grad-remove"
                    title="Remove stop"
                    aria-label={`Remove gradient stop ${idx + 1}`}
                    onclick={() => handleRemoveStop(idx)}
                  >
                    &times;
                  </button>
                {:else}
                  <span class="grad-remove-spacer"></span>
                {/if}
              </div>
            {/each}
          </div>

          <div class="chip-row">
            <button
              type="button"
              class="format-btn"
              id="grad-add-stop"
              title="Add gradient stop"
              disabled={custom.gradient.stops.length >= MAX_GRADIENT_STOPS}
              onclick={handleAddStop}
            >
              + Stop
            </button>
            <button
              type="button"
              class="format-btn"
              class:active={custom.gradient.projection === 'linear'}
              data-projection="linear"
              onclick={() => patchGradient({ projection: 'linear' as GradientProjection })}
            >
              Linear
            </button>
            <button
              type="button"
              class="format-btn"
              class:active={custom.gradient.projection === 'radial'}
              data-projection="radial"
              onclick={() => patchGradient({ projection: 'radial' as GradientProjection })}
            >
              Radial
            </button>
          </div>

          {#if custom.gradient.projection === 'linear'}
            <label class="range-label" for="grad-angle">
              Angle <span id="grad-angle-val">{custom.gradient.angle}°</span>
            </label>
            <input
              type="range"
              id="grad-angle"
              aria-label="Gradient angle"
              class="neon-slider"
              min="0"
              max="360"
              value={custom.gradient.angle}
              oninput={(e) =>
                patchGradient({ angle: Number((e.currentTarget as HTMLInputElement).value) })}
            />
          {:else}
            <div id="grad-radial-rows">
              <label class="range-label" for="grad-cx">
                Center X <span id="grad-cx-val">{custom.gradient.cx}</span>
              </label>
              <input
                type="range"
                id="grad-cx"
                aria-label="Gradient centre X"
                class="neon-slider"
                min="0"
                max="100"
                value={custom.gradient.cx}
                oninput={(e) =>
                  patchGradient({ cx: Number((e.currentTarget as HTMLInputElement).value) })}
              />
              <label class="range-label" for="grad-cy">
                Center Y <span id="grad-cy-val">{custom.gradient.cy}</span>
              </label>
              <input
                type="range"
                id="grad-cy"
                aria-label="Gradient centre Y"
                class="neon-slider"
                min="0"
                max="100"
                value={custom.gradient.cy}
                oninput={(e) =>
                  patchGradient({ cy: Number((e.currentTarget as HTMLInputElement).value) })}
              />
              <label class="range-label" for="grad-r">
                Radius <span id="grad-r-val">{custom.gradient.r}</span>
              </label>
              <input
                type="range"
                id="grad-r"
                aria-label="Gradient radius"
                class="neon-slider"
                min="5"
                max="150"
                value={custom.gradient.r}
                oninput={(e) =>
                  patchGradient({ r: Number((e.currentTarget as HTMLInputElement).value) })}
              />
            </div>
          {/if}
        </div>

        <label class="range-label" for="dp-stroke-slider">
          Stroke Width <span id="dp-stroke-val">{custom.strokeWidth}px</span>
        </label>
        <input
          type="range"
          id="dp-stroke-slider"
          aria-label="Stroke width"
          class="neon-slider"
          min="0.1"
          max="3"
          step="0.1"
          value={custom.strokeWidth}
          oninput={(e) => handleStrokeChange(Number((e.currentTarget as HTMLInputElement).value))}
        />

        <div class="exact-size-grid">
          <label class="exact-size-row" for="dp-exact-size">
            W
            <input
              id="dp-exact-size"
              type="number"
              min="16"
              max="512"
              aria-label="Export width in pixels"
              value={exportWidth}
              oninput={(e) => handleWidthInput(Number((e.currentTarget as HTMLInputElement).value))}
            />
            px
          </label>
          <label class="exact-size-row" for="dp-exact-height">
            H
            <input
              id="dp-exact-height"
              type="number"
              min="16"
              max="512"
              aria-label="Export height in pixels"
              value={exportHeight}
              oninput={(e) => handleHeightInput(Number((e.currentTarget as HTMLInputElement).value))}
            />
            px
          </label>
        </div>
      </section>

      <section class="dp-section">
        <h3>This icon in other libraries</h3>
        <div class="matches-grid" id="dp-matches">
          {#if matchesLoading}
            <span class="muted">Finding matches...</span>
          {:else if matches.length === 0}
            <span class="muted">No cross-library matches found</span>
          {:else}
            {#each matches as match (match.id)}
              <button
                type="button"
                class="match-card"
                title={`${match.library || match.librarySlug} / ${match.name}`}
                onclick={() => inspectorState.openInspector(match)}
              >
                {@html renderCustomizedSvg(match, {
                  size: 22,
                  width: 22,
                  height: 22,
                  color: 'currentColor',
                  strokeWidth: match.strokeWidth ?? 1.75,
                })}
              </button>
            {/each}
          {/if}
        </div>
      </section>

      <section class="dp-tabs">
        <div class="tab-headers">
          <button
            type="button"
            class="tab-btn"
            class:active={activeTab === 'copy'}
            data-tab="copy"
            onclick={() => (activeTab = 'copy')}
          >
            Code
          </button>
          <button
            type="button"
            class="tab-btn"
            class:active={activeTab === 'download'}
            data-tab="download"
            onclick={() => (activeTab = 'download')}
          >
            Download
          </button>
          <button
            type="button"
            class="tab-btn"
            class:active={activeTab === 'project'}
            data-tab="project"
            onclick={() => (activeTab = 'project')}
          >
            Use
          </button>
          <button
            type="button"
            class="tab-btn"
            class:active={activeTab === 'meta'}
            data-tab="meta"
            onclick={() => (activeTab = 'meta')}
          >
            Info
          </button>
        </div>

        <div class="tab-content" class:active={activeTab === 'copy'} id="tab-copy">
          <div class="code-formats">
            {#each FORMAT_OPTIONS as fmt}
              <button
                type="button"
                class="format-btn"
                class:active={activeFormat === fmt.id}
                data-fmt={fmt.id}
                onclick={() => (activeFormat = fmt.id)}
              >
                {fmt.label}
              </button>
            {/each}
          </div>
          <div class="code-preview-box">
            <code id="dp-code-preview">{codePreview}</code>
            <button
              type="button"
              class="copy-btn"
              id="dp-copy-code"
              onclick={() => handleCopyFormat(activeFormat)}
            >
              Copy {FORMAT_OPTIONS.find((f) => f.id === activeFormat)?.label ?? 'SVG'}
            </button>
          </div>
        </div>

        <div class="tab-content" class:active={activeTab === 'download'} id="tab-download">
          <div class="png-sizes">
            {#each PNG_EXPORT_SIZES as sz}
              <button
                type="button"
                class="size-btn"
                class:active={activePngSize === sz}
                data-size={sz}
                onclick={() => (activePngSize = sz)}
              >
                {sz}
              </button>
            {/each}
          </div>
          <div class="download-buttons-group">
            <button
              type="button"
              class="outlined-neon-btn"
              id="dp-dl-svg"
              onclick={handleDownloadSvg}
            >
              Download SVG
            </button>
            <button
              type="button"
              class="outlined-neon-btn"
              id="dp-dl-png"
              disabled={exporting}
              onclick={() => handleDownloadPng(activePngSize)}
            >
              Download PNG ({activePngSize}px)
            </button>
            <button
              type="button"
              class="gradient-btn"
              id="dp-dl-zip"
              disabled={exporting}
              onclick={handleDownloadZip}
            >
              Download ZIP
            </button>
          </div>
        </div>

        <div class="tab-content" class:active={activeTab === 'project'} id="tab-project">
          <div class="code-preview-box slim">
            <code id="dp-install-code">{installCommand}</code>
            <button
              type="button"
              class="copy-btn"
              data-copy-target="dp-install-code"
              onclick={() => copyTextToClipboard(installCommand, 'Install command copied')}
            >
              Copy
            </button>
          </div>
          <div class="code-preview-box slim">
            <code id="dp-import-code">{importStatement}</code>
            <button
              type="button"
              class="copy-btn"
              data-copy-target="dp-import-code"
              onclick={() => copyTextToClipboard(importStatement, 'Import statement copied')}
            >
              Copy
            </button>
          </div>
          <a
            id="dp-docs-link"
            class="docs-link"
            href={docsUrl}
            target="_blank"
            rel="noreferrer"
          >
            Open official docs
          </a>
        </div>

        <div class="tab-content" class:active={activeTab === 'meta'} id="tab-meta">
          <div class="meta-badges">
            <span class="meta-badge" id="dp-lib-badge">
              {`${libraryDisplay} ${libraryVersion}`.trim()}
            </span>
          </div>
          <div class="dp-tags-label">Tags</div>
          <div class="tags-container" id="dp-tags">
            {#each (activeIcon.tags ?? []).slice(0, 14) as tag}
              <span class="tag-chip" data-tag={tag}>{tag}</span>
            {/each}
          </div>
          <button
            type="button"
            class="monospace-id"
            id="dp-icon-id"
            title="Copy icon ID"
            onclick={() => copyTextToClipboard(activeIcon.id, 'Icon ID copied')}
          >
            {activeIcon.id}
          </button>

          <div class="detail-actions-row">
            <button
              type="button"
              class="glass-btn"
              class:active={isFav}
              id="dp-favorite"
              title="Toggle favorite"
              onclick={handleToggleFavorite}
            >
              <svg
                viewBox="0 0 24 24"
                width="16"
                height="16"
                fill={isFav ? 'currentColor' : 'none'}
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                style="vertical-align: middle; margin-right: 4px;"
              >
                <path
                  d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"
                />
              </svg>
              <span>{isFav ? 'Favorited' : 'Favorite'}</span>
            </button>

            <div class="dp-collection-picker" style="position: relative;">
              <button
                type="button"
                class="glass-btn"
                id="dp-add-collection"
                aria-expanded={collectionDropdownOpen}
                onclick={(e) => {
                  e.stopPropagation();
                  collectionDropdownOpen = !collectionDropdownOpen;
                }}
              >
                + Collection
              </button>
              {#if collectionDropdownOpen}
                <div class="qa-menu" role="menu" aria-label="Add to collection" style="min-width: 200px; right: 0;">
                  {#if collectionNames.length === 0}
                    <div class="muted" style="padding: 6px 10px; font-size: 12px;">
                      No named collections yet
                    </div>
                  {:else}
                    {#each collectionNames as colName}
                      {@const included = isInCollection(colName, activeIcon.id)}
                      <button
                        type="button"
                        class="qa-menu-item"
                        class:active={included}
                        role="menuitemcheckbox"
                        aria-checked={included}
                        onclick={() => handleToggleCollection(colName)}
                      >
                        <span>{colName}</span>
                        <em>{included ? '✓' : '+'}</em>
                      </button>
                    {/each}
                  {/if}
                  <div style="display: flex; gap: 4px; padding: 6px;">
                    <input
                      type="text"
                      class="mini-search"
                      placeholder="New collection..."
                      bind:value={newCollectionName}
                      onkeydown={(e) => {
                        if (e.key === 'Enter') handleCreateAndAddCollection();
                      }}
                    />
                    <button
                      type="button"
                      class="format-btn"
                      onclick={handleCreateAndAddCollection}
                    >
                      Add
                    </button>
                  </div>
                </div>
              {/if}
            </div>

            <button type="button" class="glass-btn" id="dp-share" onclick={handleShare}>
              Share
            </button>
            <button type="button" class="glass-btn" id="dp-compare" onclick={handleCompare}>
              Compare across libraries
            </button>
          </div>
        </div>
      </section>
    </div>
  {/if}
</aside>

<aside
  id="advance-panel"
  class:open={advanceOpen && Boolean(activeIcon)}
  aria-label="Advanced customization"
  aria-hidden={!(advanceOpen && Boolean(activeIcon))}
>
  <div class="advance-inner">
    <div class="panel-header advance-header">
      <div>
        <span class="eyebrow">Advanced</span>
        <h2>Effects &amp; Motion</h2>
      </div>
      <button
        type="button"
        class="close-btn"
        id="advance-close"
        aria-label="Close advanced panel"
        onclick={() => (advanceOpen = false)}
      >
        <svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12" /></svg>
      </button>
    </div>

    <div class="advance-content">
      <section class="dp-section">
        <h3>Effects</h3>
        <div class="chip-row">
          <button
            type="button"
            class="format-btn"
            class:active={custom.effects.flipH}
            data-flip="h"
            onclick={() => patchEffects({ flipH: !custom.effects.flipH })}
          >
            Flip H
          </button>
          <button
            type="button"
            class="format-btn"
            class:active={custom.effects.flipV}
            data-flip="v"
            onclick={() => patchEffects({ flipV: !custom.effects.flipV })}
          >
            Flip V
          </button>
          <button
            type="button"
            class="format-btn"
            class:active={custom.effects.shadowOn}
            id="fx-shadow-toggle"
            onclick={toggleShadow}
          >
            Shadow
          </button>
        </div>

        <div id="fx-shadow-controls" class:hidden={!custom.effects.shadowOn}>
          <div class="fx-grid2">
            <div>
              <label class="range-label" for="fx-sh-op">
                Opacity <span id="fx-sh-op-val">{custom.effects.shadowOpacity}</span>
              </label>
              <input
                type="range"
                id="fx-sh-op"
                aria-label="Shadow opacity"
                class="neon-slider"
                min="0"
                max="100"
                value={custom.effects.shadowOpacity}
                oninput={(e) =>
                  patchEffects({ shadowOpacity: Number((e.currentTarget as HTMLInputElement).value) })}
              />
            </div>
            <div>
              <label class="range-label" for="fx-sh-blur">
                Blur <span id="fx-sh-blur-val">{custom.effects.shadowBlur}</span>
              </label>
              <input
                type="range"
                id="fx-sh-blur"
                aria-label="Shadow blur"
                class="neon-slider"
                min="0"
                max="8"
                value={custom.effects.shadowBlur}
                oninput={(e) =>
                  patchEffects({ shadowBlur: Number((e.currentTarget as HTMLInputElement).value) })}
              />
            </div>
            <div>
              <label class="range-label" for="fx-sh-x">
                X <span id="fx-sh-x-val">{custom.effects.shadowX}</span>
              </label>
              <input
                type="range"
                id="fx-sh-x"
                aria-label="Shadow X offset"
                class="neon-slider"
                min="-30"
                max="30"
                value={custom.effects.shadowX}
                oninput={(e) =>
                  patchEffects({ shadowX: Number((e.currentTarget as HTMLInputElement).value) })}
              />
            </div>
            <div>
              <label class="range-label" for="fx-sh-y">
                Y <span id="fx-sh-y-val">{custom.effects.shadowY}</span>
              </label>
              <input
                type="range"
                id="fx-sh-y"
                aria-label="Shadow Y offset"
                class="neon-slider"
                min="-30"
                max="30"
                value={custom.effects.shadowY}
                oninput={(e) =>
                  patchEffects({ shadowY: Number((e.currentTarget as HTMLInputElement).value) })}
              />
            </div>
          </div>
          <label class="range-label" for="fx-sh-color">
            Shadow Color
            <input
              type="color"
              id="fx-sh-color"
              aria-label="Shadow color"
              value={custom.effects.shadowColor || '#000000'}
              oninput={(e) =>
                patchEffects({ shadowColor: (e.currentTarget as HTMLInputElement).value })}
            />
          </label>
        </div>

        <label class="range-label" for="fx-rot">
          Rotation <span id="fx-rot-val">{custom.effects.rotation}°</span>
        </label>
        <input
          type="range"
          id="fx-rot"
          aria-label="Rotation"
          class="neon-slider"
          min="0"
          max="360"
          value={custom.effects.rotation}
          oninput={(e) =>
            patchEffects({ rotation: Number((e.currentTarget as HTMLInputElement).value) })}
        />

        <label class="range-label" for="fx-blur">
          Blur <span id="fx-blur-val">{custom.effects.blur}px</span>
        </label>
        <input
          type="range"
          id="fx-blur"
          aria-label="Blur"
          class="neon-slider"
          min="0"
          max="2"
          step="0.1"
          value={custom.effects.blur}
          oninput={(e) =>
            patchEffects({ blur: Number((e.currentTarget as HTMLInputElement).value) })}
        />

        <label class="range-label" for="fx-noise">
          Noise Grain <span id="fx-noise-val">{custom.effects.noise}</span>
        </label>
        <input
          type="range"
          id="fx-noise"
          aria-label="Noise grain"
          class="neon-slider"
          min="0"
          max="100"
          value={custom.effects.noise}
          oninput={(e) =>
            patchEffects({ noise: Number((e.currentTarget as HTMLInputElement).value) })}
        />

        <span class="range-label">Texture</span>
        <div class="chip-row" id="texture-row">
          {#each TEXTURE_OPTIONS as tex}
            <button
              type="button"
              class="format-btn"
              class:active={custom.effects.texture === tex.id}
              data-texture={tex.id}
              onclick={() => patchEffects({ texture: tex.id })}
            >
              {tex.label}
            </button>
          {/each}
        </div>
        <p class="texture-note" id="texture-note" hidden={!colorLocked}>
          Wood and Metal are real materials with their own colour, so the colour and gradient controls are switched off while either is selected.
        </p>

        <label class="range-label" for="tex-op">
          Texture Opacity <span id="tex-op-val">{custom.effects.textureOpacity}</span>
        </label>
        <input
          type="range"
          id="tex-op"
          aria-label="Texture opacity"
          class="neon-slider"
          min="0"
          max="100"
          value={custom.effects.textureOpacity}
          oninput={(e) =>
            patchEffects({ textureOpacity: Number((e.currentTarget as HTMLInputElement).value) })}
        />

        <label class="range-label" for="fx-round">
          Roundness <span id="fx-round-val">{ROUNDNESS_LABELS[custom.effects.roundness]}</span>
        </label>
        <input
          type="range"
          id="fx-round"
          aria-label="Corner roundness"
          class="neon-slider"
          min="0"
          max="3"
          step="1"
          value={roundnessIndex}
          oninput={(e) => handleRoundnessSlider(Number((e.currentTarget as HTMLInputElement).value))}
        />

        <button
          type="button"
          class="format-btn fx-reset-btn"
          id="fx-reset"
          onclick={() => {
            inspectorState.resetCustom();
            inspectorState.showToast('Customization reset');
          }}
        >
          Reset All
        </button>
      </section>

      <section class="dp-section">
        <h3>Animate</h3>
        <div class="anim-thumbs" id="anim-type-row">
          <button
            type="button"
            class="anim-thumb"
            class:active={!custom.motion.on}
            data-anim="off"
            onclick={() => selectMotionType('off')}
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="8"></circle>
            </svg>
            <span>Off</span>
          </button>
          <button
            type="button"
            class="anim-thumb"
            class:active={custom.motion.on && custom.motion.type === 'draw'}
            data-anim="draw"
            onclick={() => selectMotionType('draw')}
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path pathLength="1" d="M4 12l5 5L20 6"></path>
            </svg>
            <span>Draw</span>
          </button>
          <button
            type="button"
            class="anim-thumb"
            class:active={custom.motion.on && custom.motion.type === 'stroke'}
            data-anim="stroke"
            onclick={() => selectMotionType('stroke')}
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M4 12h16"></path>
            </svg>
            <span>Stroke</span>
          </button>
          <button
            type="button"
            class="anim-thumb"
            class:active={custom.motion.on && custom.motion.type === 'bounce'}
            data-anim="bounce"
            onclick={() => selectMotionType('bounce')}
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="7"></circle>
            </svg>
            <span>Bounce</span>
          </button>
          <button
            type="button"
            class="anim-thumb"
            class:active={custom.motion.on && custom.motion.type === 'shake'}
            data-anim="shake"
            onclick={() => selectMotionType('shake')}
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 3v18M5 8l14 8M19 8L5 16"></path>
            </svg>
            <span>Shake</span>
          </button>
          <button
            type="button"
            class="anim-thumb"
            class:active={custom.motion.on && custom.motion.type === 'jump'}
            data-anim="jump"
            onclick={() => selectMotionType('jump')}
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 3l9 18H3l9-18z"></path>
            </svg>
            <span>Jump</span>
          </button>
        </div>

        <label class="range-label" for="anim-dur">
          Duration <span id="anim-dur-val">{custom.motion.duration.toFixed(1)}s</span>
        </label>
        <input
          type="range"
          id="anim-dur"
          aria-label="Animation duration"
          class="neon-slider"
          min="0.5"
          max="5"
          step="0.1"
          value={custom.motion.duration}
          oninput={(e) =>
            patchMotion({ duration: Number((e.currentTarget as HTMLInputElement).value) })}
        />

        <div class="chip-row">
          <button
            type="button"
            class="format-btn"
            class:active={custom.motion.loop}
            id="anim-loop"
            onclick={() => patchMotion({ loop: !custom.motion.loop })}
          >
            Loop
          </button>
          {#each EASING_OPTIONS as ease}
            <button
              type="button"
              class="format-btn"
              class:active={custom.motion.easing === ease.id}
              data-ease={ease.id}
              onclick={() => patchMotion({ easing: ease.id })}
            >
              {ease.label}
            </button>
          {/each}
        </div>
      </section>
    </div>
  </div>
</aside>

<style>
  #dp-preview-box :global(svg) { width: var(--dp-preview-dim, 112px) !important; height: var(--dp-preview-dim, 112px) !important; max-width: 156px; max-height: 156px; flex-shrink: 0; }

  .color-swatches-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin: 8px 0;
  }
  .color-preset {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    border: 1px solid var(--glass-border-bright, #2a2a2a);
    cursor: pointer;
    padding: 0;
    transition: transform 140ms ease, box-shadow 140ms ease;
  }
  .color-preset:hover:not(:disabled) {
    transform: scale(1.12);
  }
  .color-preset.active {
    box-shadow: 0 0 0 2px var(--bg-surface, #111111), 0 0 0 4px var(--control-blue, #c1dd2d);
  }
  .color-preset:disabled {
    opacity: 0.35;
    cursor: not-allowed;
  }
  .exact-size-grid {
    display: flex;
    gap: 12px;
    align-items: center;
  }
  .qa-color-btn.disabled {
    opacity: 0.4;
    pointer-events: none;
  }
</style>
