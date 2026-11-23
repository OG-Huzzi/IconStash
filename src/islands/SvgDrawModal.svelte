<script lang="ts">
  import { inspectorState } from '../lib/state/inspector.svelte';
  import { renderCustomizedSvg } from '../lib/svg/effects';
  import { formatCode } from '../lib/svg/codegen';
  import type { IconSvgInput } from '../lib/svg/types';
  import { downloadBlob, exportPng } from '../lib/export/client';

  type DrawTool = 'pen' | 'rect' | 'ellipse' | 'line' | 'eraser';

  interface Point {
    x: number;
    y: number;
  }

  interface DrawnPath {
    d: string;
  }

  interface ActiveSession {
    tool: Exclude<DrawTool, 'eraser'>;
    start: Point;
    points: Point[];
    end: Point | null;
  }

  const DRAW_DRAFT_KEY = 'iconstash-draw-draft';
  const MAX_HISTORY = 80;
  const GRID_LINES = [4, 8, 12, 16, 20] as const;

  let canvasEl = $state<SVGSVGElement | null>(null);
  let tool = $state<DrawTool>('pen');
  let paths = $state<DrawnPath[]>([]);
  let strokeColor = $state('#C1DD2D');
  let strokeWidth = $state(2);
  let showGrid = $state(true);
  let showRef = $state(false);
  let previewD = $state('');
  let undoStack = $state<string[]>([]);
  let redoStack = $state<string[]>([]);
  let draftLoaded = $state(false);
  let exportingPng = $state(false);

  let activeSession: ActiveSession | null = null;
  let beforeEraseSnapshot: string | null = null;
  let eraseChanged = false;

  const isOpen = $derived(Boolean(inspectorState.drawOpen));
  const refIcon = $derived(inspectorState.activeIcon as IconSvgInput | null);
  const refSvgMarkup = $derived.by(() => {
    if (!showRef || !refIcon) return '';
    return renderCustomizedSvg(refIcon, {
      size: 24,
      width: 24,
      height: 24,
      color: 'currentColor',
    });
  });

  const strokeCountLabel = $derived(
    `${paths.length} ${paths.length === 1 ? 'stroke' : 'strokes'}`,
  );

  const refLabelText = $derived.by(() => {
    if (showRef && refIcon) {
      return `Tracing: ${refIcon.library || refIcon.librarySlug || 'Icon'} / ${refIcon.name}`;
    }
    return refIcon ? 'Trace the icon you have open' : 'Open any icon first to trace it';
  });

  $effect(() => {
    if (isOpen && !draftLoaded) {
      loadDraft();
      draftLoaded = true;
    }
  });

  function roundCoord(value: number): number {
    return Math.round(value * 100) / 100;
  }

  function snapshot(): string {
    return JSON.stringify(paths);
  }

  function pushUndo(snap: string) {
    const next = [...undoStack, snap];
    if (next.length > MAX_HISTORY) next.shift();
    undoStack = next;
    redoStack = [];
  }

  function saveDraft() {
    try {
      localStorage.setItem(
        DRAW_DRAFT_KEY,
        JSON.stringify({ paths, color: strokeColor, strokeWidth }),
      );
    } catch {
      // Storage unavailable
    }
  }

  function loadDraft() {
    try {
      const raw = localStorage.getItem(DRAW_DRAFT_KEY);
      if (!raw) return;
      const saved = JSON.parse(raw) as {
        paths?: unknown[];
        color?: string;
        strokeWidth?: number;
      };
      if (Array.isArray(saved.paths)) {
        paths = saved.paths.filter(
          (p): p is DrawnPath =>
            Boolean(p && typeof (p as DrawnPath).d === 'string'),
        );
      }
      if (typeof saved.color === 'string') strokeColor = saved.color;
      if (Number.isFinite(saved.strokeWidth)) strokeWidth = Number(saved.strokeWidth);
    } catch {
      // Ignore corrupted draft
    }
  }

  function pointFromEvent(event: PointerEvent): Point {
    if (!canvasEl) return { x: 12, y: 12 };
    const rect = canvasEl.getBoundingClientRect();
    if (!rect.width || !rect.height) return { x: 12, y: 12 };
    const x = ((event.clientX - rect.left) / rect.width) * 24;
    const y = ((event.clientY - rect.top) / rect.height) * 24;
    return {
      x: roundCoord(Math.min(24, Math.max(0, x))),
      y: roundCoord(Math.min(24, Math.max(0, y))),
    };
  }

  function simplifyPoints(points: Point[], tolerance: number): Point[] {
    if (points.length <= 2) return points.slice();
    const sqSegDist = (p: Point, a: Point, b: Point): number => {
      let x = a.x;
      let y = a.y;
      let dx = b.x - x;
      let dy = b.y - y;
      if (dx !== 0 || dy !== 0) {
        const t = ((p.x - x) * dx + (p.y - y) * dy) / (dx * dx + dy * dy);
        if (t > 1) {
          x = b.x;
          y = b.y;
        } else if (t > 0) {
          x += dx * t;
          y += dy * t;
        }
      }
      dx = p.x - x;
      dy = p.y - y;
      return dx * dx + dy * dy;
    };

    const tolSq = tolerance * tolerance;
    const keep = new Array<boolean>(points.length).fill(false);
    keep[0] = true;
    keep[points.length - 1] = true;

    const stack: Array<[number, number]> = [[0, points.length - 1]];
    while (stack.length) {
      const [first, last] = stack.pop()!;
      let maxDist = -1;
      let idx = -1;
      for (let i = first + 1; i < last; i += 1) {
        const dist = sqSegDist(points[i], points[first], points[last]);
        if (dist > maxDist) {
          maxDist = dist;
          idx = i;
        }
      }
      if (maxDist > tolSq && idx > 0) {
        keep[idx] = true;
        stack.push([first, idx], [idx, last]);
      }
    }

    return points.filter((_, i) => keep[i]);
  }

  function pointsToSmoothPath(points: Point[]): string {
    const r = roundCoord;
    if (points.length === 1) {
      return `M ${r(points[0].x)} ${r(points[0].y)} L ${r(points[0].x + 0.01)} ${r(points[0].y)}`;
    }
    if (points.length === 2) {
      return `M ${r(points[0].x)} ${r(points[0].y)} L ${r(points[1].x)} ${r(points[1].y)}`;
    }
    let d = `M ${r(points[0].x)} ${r(points[0].y)}`;
    for (let i = 0; i < points.length - 1; i += 1) {
      const p0 = points[i - 1] || points[i];
      const p1 = points[i];
      const p2 = points[i + 1];
      const p3 = points[i + 2] || p2;
      const c1x = p1.x + (p2.x - p0.x) / 6;
      const c1y = p1.y + (p2.y - p0.y) / 6;
      const c2x = p2.x - (p3.x - p1.x) / 6;
      const c2y = p2.y - (p3.y - p1.y) / 6;
      d += ` C ${r(c1x)} ${r(c1y)}, ${r(c2x)} ${r(c2y)}, ${r(p2.x)} ${r(p2.y)}`;
    }
    return d;
  }

  function constrainPoint(
    start: Point,
    end: Point,
    shiftKey: boolean,
    activeTool: Exclude<DrawTool, 'eraser'>,
  ): Point {
    if (!shiftKey) return end;
    const dx = end.x - start.x;
    const dy = end.y - start.y;
    if (activeTool === 'line') {
      const angle = Math.atan2(dy, dx);
      const snapped = Math.round(angle / (Math.PI / 4)) * (Math.PI / 4);
      const len = Math.hypot(dx, dy);
      return {
        x: roundCoord(start.x + Math.cos(snapped) * len),
        y: roundCoord(start.y + Math.sin(snapped) * len),
      };
    }
    const size = Math.max(Math.abs(dx), Math.abs(dy));
    return {
      x: roundCoord(start.x + Math.sign(dx || 1) * size),
      y: roundCoord(start.y + Math.sign(dy || 1) * size),
    };
  }

  function buildShapePath(activeTool: Exclude<DrawTool, 'eraser'>, a: Point, b: Point): string {
    const r = roundCoord;
    if (activeTool === 'rect') {
      const x = Math.min(a.x, b.x);
      const y = Math.min(a.y, b.y);
      const w = Math.max(0.01, Math.abs(b.x - a.x));
      const h = Math.max(0.01, Math.abs(b.y - a.y));
      return `M ${r(x)} ${r(y)} H ${r(x + w)} V ${r(y + h)} Z`;
    }
    if (activeTool === 'ellipse') {
      const cx = (a.x + b.x) / 2;
      const cy = (a.y + b.y) / 2;
      const rx = Math.max(0.01, Math.abs(b.x - a.x) / 2);
      const ry = Math.max(0.01, Math.abs(b.y - a.y) / 2);
      return `M ${r(cx - rx)} ${r(cy)} A ${r(rx)} ${r(ry)} 0 1 1 ${r(cx + rx)} ${r(cy)} A ${r(rx)} ${r(ry)} 0 1 1 ${r(cx - rx)} ${r(cy)} Z`;
    }
    return `M ${r(a.x)} ${r(a.y)} L ${r(b.x)} ${r(b.y)}`;
  }

  function eraseAt(event: PointerEvent) {
    const hit = document.elementFromPoint(event.clientX, event.clientY) as HTMLElement | null;
    const pathEl = hit?.closest ? (hit.closest('[data-draw-path]') as HTMLElement | null) : null;
    if (!pathEl) return;
    const idx = Number(pathEl.dataset.drawPath);
    if (Number.isNaN(idx) || !paths[idx]) return;
    paths = paths.filter((_, i) => i !== idx);
    eraseChanged = true;
  }

  function handlePointerDown(event: PointerEvent) {
    if (event.button !== 0 && event.pointerType === 'mouse') return;
    event.preventDefault();

    if (tool === 'eraser') {
      beforeEraseSnapshot = snapshot();
      eraseChanged = false;
      eraseAt(event);
      return;
    }

    const pt = pointFromEvent(event);
    activeSession = { tool, start: pt, points: [pt], end: null };
    try {
      (event.currentTarget as SVGSVGElement).setPointerCapture(event.pointerId);
    } catch {
      // Pointer capture unavailable
    }
  }

  function handlePointerMove(event: PointerEvent) {
    if (tool === 'eraser') {
      if (beforeEraseSnapshot !== null) eraseAt(event);
      return;
    }
    if (!activeSession) return;
    event.preventDefault();
    const pt = pointFromEvent(event);
    if (activeSession.tool === 'pen') {
      const last = activeSession.points[activeSession.points.length - 1];
      if (Math.hypot(pt.x - last.x, pt.y - last.y) < 0.12) return;
      activeSession.points.push(pt);
      previewD = activeSession.points
        .map((p, i) => `${i ? 'L' : 'M'} ${p.x} ${p.y}`)
        .join(' ');
    } else {
      activeSession.end = constrainPoint(
        activeSession.start,
        pt,
        event.shiftKey,
        activeSession.tool,
      );
      previewD = buildShapePath(activeSession.tool, activeSession.start, activeSession.end);
    }
  }

  function handlePointerUp() {
    if (tool === 'eraser') {
      if (beforeEraseSnapshot !== null) {
        if (eraseChanged) {
          pushUndo(beforeEraseSnapshot);
          saveDraft();
        }
        beforeEraseSnapshot = null;
        eraseChanged = false;
      }
      return;
    }
    if (!activeSession) return;
    const session = activeSession;
    activeSession = null;
    previewD = '';

    let dAttr = '';
    if (session.tool === 'pen') {
      const simplified = simplifyPoints(session.points, 0.15);
      dAttr = pointsToSmoothPath(simplified);
    } else if (session.end) {
      dAttr = buildShapePath(session.tool, session.start, session.end);
    }
    if (!dAttr) return;

    pushUndo(snapshot());
    paths = [...paths, { d: dAttr }];
    saveDraft();
  }

  function handleUndo() {
    if (!undoStack.length) return;
    const nextUndo = undoStack.slice();
    const prev = nextUndo.pop()!;
    redoStack = [...redoStack, snapshot()];
    undoStack = nextUndo;
    paths = JSON.parse(prev) as DrawnPath[];
    saveDraft();
  }

  function handleRedo() {
    if (!redoStack.length) return;
    const nextRedo = redoStack.slice();
    const next = nextRedo.pop()!;
    undoStack = [...undoStack, snapshot()];
    redoStack = nextRedo;
    paths = JSON.parse(next) as DrawnPath[];
    saveDraft();
  }

  function handleClear() {
    if (!paths.length) return;
    pushUndo(snapshot());
    paths = [];
    saveDraft();
    inspectorState.showToast('Canvas cleared');
  }

  function buildDrawnIcon(): IconSvgInput {
    return {
      id: 'iconstash-drawn-icon',
      name: 'drawn icon',
      librarySlug: 'iconstash',
      style: 'outline',
      viewBox: '0 0 24 24',
      svgPath: paths.map((p) => `<path d="${p.d}"></path>`).join(''),
    };
  }

  function buildExportSvg(size = 24): string {
    return formatCode(buildDrawnIcon(), 'svg', {
      color: strokeColor,
      strokeWidth,
      size,
      width: size,
      height: size,
    });
  }

  async function handleCopySvg() {
    if (!paths.length) {
      inspectorState.showToast('Draw something first');
      return;
    }
    const svg = buildExportSvg(24);
    try {
      await navigator.clipboard.writeText(svg);
      inspectorState.showToast('Drawn icon copied as SVG');
    } catch {
      inspectorState.showToast('Clipboard copy failed');
    }
  }

  function handleDownloadSvg() {
    if (!paths.length) {
      inspectorState.showToast('Draw something first');
      return;
    }
    const svg = buildExportSvg(24);
    const blob = new Blob([svg], { type: 'image/svg+xml;charset=utf-8' });
    downloadBlob(blob, 'iconstash-drawn-icon.svg');
    inspectorState.showToast('SVG downloaded');
  }

  async function handleDownloadPng() {
    if (!paths.length || exportingPng) {
      if (!paths.length) inspectorState.showToast('Draw something first');
      return;
    }
    exportingPng = true;
    inspectorState.showToast('Generating 256px PNG...');
    try {
      const svgMarkup = buildExportSvg(256);
      await exportPng({
        svgMarkup,
        filename: 'iconstash-drawn-icon-256.png',
        size: 256,
        scale: typeof window !== 'undefined' ? Math.min(2, window.devicePixelRatio || 1) : 1,
      });
      inspectorState.showToast('PNG downloaded');
    } catch {
      inspectorState.showToast('PNG export failed');
    } finally {
      exportingPng = false;
    }
  }

  function handleKeydown(event: KeyboardEvent) {
    if (!isOpen) return;
    if (event.key === 'Escape') {
      inspectorState.closeDraw();
      return;
    }
    const mod = event.ctrlKey || event.metaKey;
    if (!mod) return;
    const key = event.key.toLowerCase();
    if (key === 'z' && !event.shiftKey) {
      event.preventDefault();
      handleUndo();
    } else if ((key === 'z' && event.shiftKey) || key === 'y') {
      event.preventDefault();
      handleRedo();
    }
  }
</script>

<svelte:window onkeydown={handleKeydown} />

{#if isOpen}
  <!-- svelte-ignore a11y_click_events_have_key_events -->
  <!-- svelte-ignore a11y_no_static_element_interactions -->
  <div
    class="modal-backdrop"
    id="draw-modal-backdrop"
    onclick={() => inspectorState.closeDraw()}
  ></div>
{/if}

<div
  class="modal draw-modal"
  class:hidden={!isOpen}
  id="draw-modal"
  aria-modal="true"
  role="dialog"
  aria-label="Draw an Icon"
>
  <div class="modal-header">
    <h2 class="gradient-text">Draw an Icon</h2>
    <button
      type="button"
      class="close-btn modal-close"
      aria-label="Close draw studio"
      onclick={() => inspectorState.closeDraw()}
    >
      <svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12" /></svg>
    </button>
  </div>

  <div class="modal-content draw-layout">
    <div class="draw-toolbar">
      <button
        type="button"
        class="draw-tool"
        class:active={tool === 'pen'}
        data-dtool="pen"
        title="Pen — draw freehand"
        aria-label="Pen tool"
        onclick={() => (tool = 'pen')}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 20h9"></path>
          <path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"></path>
        </svg>
      </button>

      <button
        type="button"
        class="draw-tool"
        class:active={tool === 'rect'}
        data-dtool="rect"
        title="Rectangle — hold Shift for square"
        aria-label="Rectangle tool"
        onclick={() => (tool = 'rect')}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="4" y="6" width="16" height="12" rx="1"></rect>
        </svg>
      </button>

      <button
        type="button"
        class="draw-tool"
        class:active={tool === 'ellipse'}
        data-dtool="ellipse"
        title="Ellipse — hold Shift for circle"
        aria-label="Circle and ellipse tool"
        onclick={() => (tool = 'ellipse')}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <ellipse cx="12" cy="12" rx="9" ry="6.5"></ellipse>
        </svg>
      </button>

      <button
        type="button"
        class="draw-tool"
        class:active={tool === 'line'}
        data-dtool="line"
        title="Line — hold Shift to snap 45°"
        aria-label="Line tool"
        onclick={() => (tool = 'line')}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
          <path d="M5 19 19 5"></path>
        </svg>
      </button>

      <button
        type="button"
        class="draw-tool"
        class:active={tool === 'eraser'}
        data-dtool="eraser"
        title="Eraser — click or drag over a stroke to remove it"
        aria-label="Eraser tool"
        onclick={() => (tool = 'eraser')}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20 20H9L4 15a1.5 1.5 0 0 1 0-2.1L12.9 4a1.5 1.5 0 0 1 2.1 0l5 5a1.5 1.5 0 0 1 0 2.1L13 18"></path>
        </svg>
      </button>

      <span class="draw-toolbar-sep"></span>

      <button
        type="button"
        class="draw-tool"
        class:active={showRef && Boolean(refIcon)}
        id="draw-ref-toggle"
        title="Trace over the icon you have open"
        aria-label="Toggle trace reference"
        disabled={!refIcon}
        onclick={() => (showRef = !showRef)}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7Z"></path>
          <circle cx="12" cy="12" r="3"></circle>
        </svg>
      </button>

      <button
        type="button"
        class="draw-tool"
        class:active={showGrid}
        id="draw-grid-toggle"
        title="Toggle grid"
        aria-label="Toggle canvas grid"
        onclick={() => (showGrid = !showGrid)}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M3 9h18M3 15h18M9 3v18M15 3v18"></path>
        </svg>
      </button>

      <span class="draw-toolbar-sep"></span>

      <button
        type="button"
        class="draw-tool"
        id="draw-undo"
        title="Undo (Ctrl+Z)"
        aria-label="Undo"
        disabled={undoStack.length === 0}
        onclick={handleUndo}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M9 14 4 9l5-5"></path>
          <path d="M4 9h10a6 6 0 0 1 6 6v1"></path>
        </svg>
      </button>

      <button
        type="button"
        class="draw-tool"
        id="draw-redo"
        title="Redo (Ctrl+Y)"
        aria-label="Redo"
        disabled={redoStack.length === 0}
        onclick={handleRedo}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="m15 14 5-5-5-5"></path>
          <path d="M20 9H10a6 6 0 0 0-6 6v1"></path>
        </svg>
      </button>

      <button
        type="button"
        class="draw-tool"
        id="draw-clear"
        title="Clear canvas"
        aria-label="Clear canvas"
        disabled={paths.length === 0}
        onclick={handleClear}
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M3 6h18"></path>
          <path d="M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2"></path>
          <path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"></path>
        </svg>
      </button>

      <span class="draw-status" id="draw-status">{strokeCountLabel}</span>
    </div>

    <div class="draw-canvas-wrap">
      <!-- svelte-ignore a11y_no_static_element_interactions -->
      <svg
        bind:this={canvasEl}
        id="draw-canvas"
        class:erasing={tool === 'eraser'}
        viewBox="0 0 24 24"
        preserveAspectRatio="xMidYMid meet"
        style="touch-action: none;"
        onpointerdown={handlePointerDown}
        onpointermove={handlePointerMove}
        onpointerup={handlePointerUp}
        onpointercancel={handlePointerUp}
      >
        {#if showGrid}
          <g id="draw-grid">
            <defs>
              <pattern id="draw-dots" width="1" height="1" patternUnits="userSpaceOnUse">
                <circle class="draw-grid-dot" cx="0.5" cy="0.5" r="0.07" stroke="none"></circle>
              </pattern>
            </defs>
            <rect x="0" y="0" width="24" height="24" fill="url(#draw-dots)" stroke="none"></rect>
            {#each GRID_LINES as pos}
              <line class="draw-grid-line" x1={pos} y1="0" x2={pos} y2="24" vector-effect="non-scaling-stroke"></line>
              <line class="draw-grid-line" x1="0" y1={pos} x2="24" y2={pos} vector-effect="non-scaling-stroke"></line>
            {/each}
            <line class="draw-grid-center" x1="12" y1="0" x2="12" y2="24" vector-effect="non-scaling-stroke"></line>
            <line class="draw-grid-center" x1="0" y1="12" x2="24" y2="12" vector-effect="non-scaling-stroke"></line>
          </g>
        {/if}

        <g id="draw-reference" class="draw-reference" style={showRef && refIcon ? '' : 'display:none;'}>
          {@html refSvgMarkup}
        </g>

        <g id="draw-shapes">
          {#each paths as p, i (i)}
            <path
              data-draw-path={i}
              d={p.d}
              fill="none"
              stroke={strokeColor}
              stroke-width={strokeWidth}
              stroke-linecap="round"
              stroke-linejoin="round"
            ></path>
          {/each}
        </g>

        <path
          id="draw-preview"
          fill="none"
          stroke={strokeColor}
          stroke-width={strokeWidth}
          stroke-linecap="round"
          stroke-linejoin="round"
          opacity="0.45"
          d={previewD}
        ></path>
      </svg>
    </div>

    <div class="draw-options">
      <label class="draw-option" for="draw-width">
        Stroke
        <input
          type="range"
          id="draw-width"
          class="neon-slider"
          aria-label="Draw stroke width"
          min="0.5"
          max="4"
          step="0.25"
          value={strokeWidth}
          oninput={(e) => {
            strokeWidth = Number((e.currentTarget as HTMLInputElement).value);
            saveDraft();
          }}
        />
        <span id="draw-width-val">{strokeWidth}</span>
      </label>

      <label class="draw-option" for="draw-color">
        Color
        <input
          type="color"
          id="draw-color"
          value={strokeColor}
          aria-label="Stroke color"
          oninput={(e) => {
            strokeColor = (e.currentTarget as HTMLInputElement).value;
            saveDraft();
          }}
        />
      </label>

      <span class="draw-ref-label" id="draw-ref-label">{refLabelText}</span>
    </div>

    <div class="draw-actions">
      <button type="button" class="gradient-btn" id="draw-copy" onclick={handleCopySvg}>
        Copy SVG
      </button>
      <button type="button" class="outlined-neon-btn" id="draw-download-svg" onclick={handleDownloadSvg}>
        Download SVG
      </button>
      <button
        type="button"
        class="outlined-neon-btn"
        id="draw-download-png"
        disabled={exportingPng}
        onclick={handleDownloadPng}
      >
        {exportingPng ? 'Exporting PNG…' : 'Download PNG'}
      </button>
    </div>
  </div>
</div>
