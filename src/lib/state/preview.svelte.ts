/// <reference types="svelte" />
/**
 * Preview & Theme State Store (Svelte 5 Runes)
 *
 * Controls live grid icon preview styling (`--ic-color`, `--ic-stroke`,
 * `--ic-size`, `--ic-rot`, `--ic-flip-x`, `--ic-flip-y`, `--ic-blur`) via
 * `requestAnimationFrame`-coalesced `style.setProperty()` calls on the grid
 * container with ZERO grid DOM re-renders.
 *
 * Syncs theme to BOTH `localStorage['iconvault-theme']` and `localStorage['theme']`
 * for 100% backward compatibility with legacy IconStash routes.
 */

export type GridDensity = 'compact' | 'default' | 'comfortable';
export type ThemeMode = 'dark' | 'light';

const LEGACY_THEME_KEY = 'iconvault-theme';
const STATIC_THEME_KEY = 'theme';

const DEFAULT_COLOR = '';
const DEFAULT_STROKE_WIDTH = 1.75;
const DEFAULT_GRID_SIZE = 24;
const DEFAULT_DENSITY: GridDensity = 'compact';

function readInitialTheme(): ThemeMode {
  if (typeof window === 'undefined') return 'dark';
  try {
    const primary = window.localStorage.getItem(LEGACY_THEME_KEY);
    if (primary === 'light' || primary === 'dark') return primary;
    const secondary = window.localStorage.getItem(STATIC_THEME_KEY);
    if (secondary === 'light' || secondary === 'dark') return secondary;
  } catch {
    // Ignore storage access errors in private browsing
  }
  return 'dark';
}

function writeThemeToStorage(theme: ThemeMode): void {
  if (typeof window === 'undefined') return;
  try {
    window.localStorage.setItem(LEGACY_THEME_KEY, theme);
    window.localStorage.setItem(STATIC_THEME_KEY, theme);
  } catch {
    // Ignore storage write errors
  }
}

function applyThemeToDocument(theme: ThemeMode): void {
  if (typeof document === 'undefined') return;
  document.documentElement.setAttribute('data-theme', theme);
}

class PreviewStore {
  color = $state<string>(DEFAULT_COLOR);
  strokeWidth = $state<number>(DEFAULT_STROKE_WIDTH);
  gridSize = $state<number>(DEFAULT_GRID_SIZE);
  density = $state<GridDensity>(DEFAULT_DENSITY);
  theme = $state<ThemeMode>(readInitialTheme());

  rot = $state<number>(0);
  flipH = $state<boolean>(false);
  flipV = $state<boolean>(false);
  blur = $state<number>(0);

  private targetEl: HTMLElement | null = null;
  private rafId: number | null = null;

  constructor() {
    if (typeof document !== 'undefined') {
      applyThemeToDocument(this.theme);
      writeThemeToStorage(this.theme);
    }
  }

  private scheduleCssVarFlush(): void {
    if (typeof window === 'undefined') return;
    if (this.rafId !== null) {
      window.cancelAnimationFrame(this.rafId);
    }
    this.rafId = window.requestAnimationFrame(() => {
      this.rafId = null;
      this.flushCssVarsNow(this.targetEl);
    });
  }

  private flushCssVarsNow(el: HTMLElement | null): void {
    const target = el ?? this.targetEl;
    if (!target) return;

    const resolvedColor = this.color.trim() || 'currentColor';
    const clampedSize = Math.min(128, Math.max(16, Math.round(this.gridSize)));
    const clampedStroke = Math.min(3, Math.max(0.1, Number(this.strokeWidth) || DEFAULT_STROKE_WIDTH));
    const clampedRot = ((Number(this.rot) || 0) % 360 + 360) % 360;
    const clampedBlur = Math.min(10, Math.max(0, Number(this.blur) || 0));

    target.style.setProperty('--ic-color', resolvedColor);
    target.style.setProperty('--ic-stroke', String(clampedStroke));
    target.style.setProperty('--ic-stroke-width', String(clampedStroke));
    target.style.setProperty('--ic-size', `${clampedSize}px`);
    target.style.setProperty('--preview-size', `${clampedSize}px`);
    target.style.setProperty('--ic-rot', `${clampedRot}deg`);
    target.style.setProperty('--ic-flip-x', this.flipH ? '-1' : '1');
    target.style.setProperty('--ic-flip-y', this.flipV ? '-1' : '1');
    target.style.setProperty('--ic-blur', `${clampedBlur}px`);

    if (this.color.trim()) {
      target.style.setProperty('--custom-icon-color', this.color.trim());
      target.classList.add('customized-preview-color');
    } else {
      target.style.removeProperty('--custom-icon-color');
      target.classList.remove('customized-preview-color');
    }
  }

  /**
   * Bind and apply all `--ic-*` CSS custom properties to the grid container
   * via a single `requestAnimationFrame`-coalesced update.
   */
  applyCssVars(el?: HTMLElement | null): void {
    if (el !== undefined) {
      this.targetEl = el;
    }
    if (!this.targetEl) return;
    this.scheduleCssVarFlush();
  }

  setColor(color: string): void {
    this.color = color;
    this.scheduleCssVarFlush();
  }

  setStrokeWidth(width: number): void {
    const next = Math.min(3, Math.max(0.1, Number(width)));
    if (!Number.isFinite(next)) return;
    this.strokeWidth = Math.round(next * 10) / 10;
    this.scheduleCssVarFlush();
  }

  setGridSize(size: number): void {
    const next = Math.min(128, Math.max(16, Math.round(Number(size))));
    if (!Number.isFinite(next)) return;
    this.gridSize = next;
    this.scheduleCssVarFlush();
  }

  setDensity(density: GridDensity): void {
    if (density !== 'compact' && density !== 'default' && density !== 'comfortable') return;
    this.density = density;
  }

  setTheme(theme: ThemeMode): void {
    const next: ThemeMode = theme === 'light' ? 'light' : 'dark';
    this.theme = next;
    applyThemeToDocument(next);
    writeThemeToStorage(next);
  }

  toggleTheme(): void {
    this.setTheme(this.theme === 'dark' ? 'light' : 'dark');
  }

  setRot(rot: number): void {
    const next = Number(rot);
    if (!Number.isFinite(next)) return;
    this.rot = ((next % 360) + 360) % 360;
    this.scheduleCssVarFlush();
  }

  setFlipH(flipH: boolean): void {
    this.flipH = Boolean(flipH);
    this.scheduleCssVarFlush();
  }

  setFlipV(flipV: boolean): void {
    this.flipV = Boolean(flipV);
    this.scheduleCssVarFlush();
  }

  setBlur(blur: number): void {
    const next = Math.min(10, Math.max(0, Number(blur)));
    if (!Number.isFinite(next)) return;
    this.blur = Math.round(next * 10) / 10;
    this.scheduleCssVarFlush();
  }

  resetPreview(): void {
    this.color = DEFAULT_COLOR;
    this.strokeWidth = DEFAULT_STROKE_WIDTH;
    this.gridSize = DEFAULT_GRID_SIZE;
    this.rot = 0;
    this.flipH = false;
    this.flipV = false;
    this.blur = 0;
    this.scheduleCssVarFlush();
  }

  cleanup(): void {
    if (this.rafId !== null && typeof window !== 'undefined') {
      window.cancelAnimationFrame(this.rafId);
      this.rafId = null;
    }
    this.targetEl = null;
  }
}

export const previewState = new PreviewStore();
