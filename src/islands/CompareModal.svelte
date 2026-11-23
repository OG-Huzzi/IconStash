<script lang="ts">
  import { inspectorState } from '../lib/state/inspector.svelte';
  import { explorerState, type ResolvedIcon } from '../lib/state/explorer.svelte';
  import { renderCustomizedSvg } from '../lib/svg/effects';
  import { createDefaultCustomizationState } from '../lib/svg/types';
  import { exportCompareZip, type ExportSvgInput } from '../lib/export/client';

  type CompareCandidate = ResolvedIcon & { tags?: string[] };

  const FALLBACK_CUSTOM = createDefaultCustomizationState();

  let showLabels = $state(true);
  let compareBg = $state<'dark' | 'light'>('dark');
  let matches = $state<CompareCandidate[]>([]);
  let loading = $state(false);
  let downloading = $state(false);

  const isOpen = $derived(Boolean(inspectorState.compareOpen));
  const custom = $derived(inspectorState.custom ?? FALLBACK_CUSTOM);
  const concept = $derived(
    (inspectorState.compareConcept || inspectorState.activeIcon?.name || '').trim(),
  );


  $effect(() => {
    if (!isOpen) return;
    const targetConcept = concept;
    if (!targetConcept) {
      matches = [];
      return;
    }

    let cancelled = false;
    loading = true;

    (async () => {
      try {
        const list = await explorerState.findConceptMatches(targetConcept);
        if (!cancelled) {
          matches = list.slice(0, 80);
        }
      } catch {
        if (!cancelled) matches = [];
      } finally {
        if (!cancelled) loading = false;
      }
    })();

    return () => {
      cancelled = true;
    };
  });

  function renderVariantSvg(candidate: CompareCandidate): string {
    return renderCustomizedSvg(candidate, {
      color: custom.color,
      strokeWidth: custom.strokeWidth,
      gradient: custom.gradient,
      size: 44,
      width: 44,
      height: 44,
      title: candidate.library || candidate.librarySlug,
    });
  }

  function handleInspectVariant(candidate: CompareCandidate) {
    inspectorState.openInspector(candidate);
    inspectorState.closeCompare();
  }

  async function handleDownloadAll() {
    if (!matches.length || downloading) return;
    downloading = true;
    inspectorState.showToast(`Packaging ${Math.min(matches.length, 200)} icons...`);
    try {
      const exportIcons: ExportSvgInput[] = matches.map((candidate) => ({
        id: candidate.id,
        name: candidate.name,
        librarySlug: candidate.librarySlug || 'iconstash',
        library: candidate.library || candidate.librarySlug || 'IconStash',
        tags: candidate.tags,
        license: candidate.license,
        svgMarkup: renderCustomizedSvg(candidate, {
          color: custom.color,
          strokeWidth: custom.strokeWidth,
          size: custom.size,
          width: custom.width ?? custom.size,
          height: custom.height ?? custom.size,
          gradient: custom.gradient,
          effects: custom.effects,
          motion: custom.motion,
        }),
      }));
      await exportCompareZip(exportIcons, concept || 'compare');
      inspectorState.showToast('Compare ZIP downloaded');
    } catch {
      inspectorState.showToast('Compare ZIP export failed');
    } finally {
      downloading = false;
    }
  }

  function handleKeydown(e: KeyboardEvent) {
    if (isOpen && e.key === 'Escape') {
      inspectorState.closeCompare();
    }
  }
</script>

<svelte:window onkeydown={handleKeydown} />

{#if isOpen}
  <!-- svelte-ignore a11y_click_events_have_key_events -->
  <!-- svelte-ignore a11y_no_static_element_interactions -->
  <div
    class="modal-backdrop"
    id="compare-modal-backdrop"
    onclick={() => inspectorState.closeCompare()}
  ></div>
{/if}

<div
  class="modal compare-modal"
  class:hidden={!isOpen}
  id="compare-modal"
  aria-modal="true"
  role="dialog"
  aria-labelledby="compare-title"
>
  <div class="modal-header">
    <h2 class="gradient-text" id="compare-title">
      {#if concept && matches.length > 0}
        {concept} - across {matches.length} libraries
      {:else if concept}
        Compare: {concept}
      {:else}
        Compare Mode
      {/if}
    </h2>
    <button
      type="button"
      class="close-btn modal-close"
      aria-label="Close compare"
      onclick={() => inspectorState.closeCompare()}
    >
      <svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12" /></svg>
    </button>
  </div>

  <div class="modal-content">
    {#if concept && (loading || matches.length > 0)}
      <div class="compare-toolbar">
        <button
          type="button"
          class="style-pill"
          class:active={showLabels}
          data-compare-labels="on"
          onclick={() => (showLabels = true)}
        >
          With labels
        </button>
        <button
          type="button"
          class="style-pill"
          class:active={!showLabels}
          data-compare-labels="off"
          onclick={() => (showLabels = false)}
        >
          Without labels
        </button>
        <button
          type="button"
          class="style-pill"
          class:active={compareBg === 'dark'}
          data-compare-bg="dark"
          onclick={() => (compareBg = 'dark')}
        >
          Dark bg
        </button>
        <button
          type="button"
          class="style-pill"
          class:active={compareBg === 'light'}
          data-compare-bg="light"
          onclick={() => (compareBg = 'light')}
        >
          Light bg
        </button>
        <button
          type="button"
          class="gradient-btn"
          id="compare-download"
          disabled={downloading || loading || matches.length === 0}
          onclick={handleDownloadAll}
        >
          {downloading ? 'Packaging…' : 'Download all as ZIP'}
        </button>
      </div>

      <div
        class="compare-grid"
        class:no-labels={!showLabels}
        class:bg-dark={compareBg === 'dark'}
        class:bg-light={compareBg === 'light'}
        id="compare-grid"
      >
        {#if loading}
          <p class="muted" style="grid-column: 1 / -1; text-align: center; padding: 24px;">
            Loading cross-library variants…
          </p>
        {:else}
          {#each matches as candidate (candidate.id)}
            <button
              type="button"
              class="compare-item"
              data-icon-id={candidate.id}
              title={candidate.library || candidate.librarySlug}
              onclick={() => handleInspectVariant(candidate)}
            >
              {@html renderVariantSvg(candidate)}
              <span>
                {candidate.library || candidate.librarySlug}
                {#if candidate.style}
                  <br />{candidate.style}
                {/if}
              </span>
            </button>
          {/each}
        {/if}
      </div>
    {:else}
      <div class="compare-grid" id="compare-grid">
        <div class="compare-placeholder-card">
          <div class="placeholder-icon">
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path d="M7 3H3v4M21 7V3h-4M3 17v4h4M17 21h4v-4M8 8l8 8M16 8l-8 8" />
            </svg>
          </div>
          <h3>Audit &amp; Compare Across Libraries</h3>
          <p class="placeholder-desc">
            Compare Mode lets you cross-examine the same icon concept across all 28 open-source icon libraries in real-time. Customize stroke weights, colors, compare layouts, and download the full matching bundle in one click.
          </p>

          <div class="placeholder-steps">
            <div class="placeholder-step">
              <span class="step-badge">1</span>
              <div>
                <h4>Select an Icon</h4>
                <p>Close this modal and click any icon card in the main grid to view its details.</p>
              </div>
            </div>
            <div class="placeholder-step">
              <span class="step-badge">2</span>
              <div>
                <h4>Click Compare Mode</h4>
                <p>With the icon open, click Compare in the header or inside the Inspector Info tab.</p>
              </div>
            </div>
            <div class="placeholder-step">
              <span class="step-badge">3</span>
              <div>
                <h4>Audit and Download</h4>
                <p>Toggle labels or background contrast, click any variant to inspect, or download all as a ZIP.</p>
              </div>
            </div>
          </div>

          <button
            type="button"
            class="gradient-btn close-compare-btn"
            id="close-compare-placeholder"
            onclick={() => inspectorState.closeCompare()}
          >
            Start Browsing Icons
          </button>
        </div>
      </div>
    {/if}
  </div>
</div>
