/// <reference types="svelte" />
/**
 * Inspector, Modals & Toast State Store (Svelte 5 Runes)
 *
 * Manages active icon selection, full SVG customization state (persisted to
 * `localStorage['iconstash-custom']` via `sanitizePersistedCustomState`),
 * modal visibility (Compare, Draw, Shortcuts, Collections), and toast alerts.
 */

import {
  CUSTOM_STORAGE_KEY,
  createDefaultCustomizationState,
  sanitizePersistedCustomState,
  type CustomizationState,
  type EffectsState,
  type GradientState,
  type MotionState,
  type PersistedCustomState,
} from '../svg/types';
import { explorerState, type ResolvedIcon } from './explorer.svelte';

export interface CustomizationPatch {
  color?: string;
  strokeWidth?: number;
  size?: number;
  width?: number;
  height?: number;
  gradient?: Partial<GradientState>;
  effects?: Partial<EffectsState>;
  motion?: Partial<MotionState>;
}

function loadInitialCustomState(): CustomizationState {
  const defaults = createDefaultCustomizationState();
  if (typeof window === 'undefined') return defaults;
  try {
    const raw = window.localStorage.getItem(CUSTOM_STORAGE_KEY);
    if (!raw) return defaults;
    const parsed: unknown = JSON.parse(raw);
    const persisted = sanitizePersistedCustomState(parsed);
    return {
      ...defaults,
      ...persisted,
    };
  } catch {
    return defaults;
  }
}

function persistCustomState(state: CustomizationState): void {
  if (typeof window === 'undefined') return;
  try {
    const payload: PersistedCustomState = sanitizePersistedCustomState({
      gradient: state.gradient,
      effects: state.effects,
      motion: state.motion,
    });
    window.localStorage.setItem(CUSTOM_STORAGE_KEY, JSON.stringify(payload));
  } catch {
    // Ignore storage quota / private mode errors
  }
}

class InspectorStore {
  activeIcon = $state.raw<ResolvedIcon | null>(null);
  custom = $state<CustomizationState>(loadInitialCustomState());

  compareOpen = $state(false);
  compareConcept = $state('');

  drawOpen = $state(false);
  shortcutsOpen = $state(false);
  collectionsOpen = $state(false);

  toastMessage = $state<string | null>(null);

  private toastTimer: ReturnType<typeof setTimeout> | null = null;

  openInspector(icon: ResolvedIcon): void {
    this.activeIcon = icon;
    explorerState.pinIcon(icon);
  }

  closeInspector(): void {
    this.activeIcon = null;
  }

  updateCustom(patch: CustomizationPatch): void {
    const next: CustomizationState = {
      ...this.custom,
      ...(patch.color !== undefined ? { color: patch.color } : {}),
      ...(patch.strokeWidth !== undefined ? { strokeWidth: patch.strokeWidth } : {}),
      ...(patch.size !== undefined ? { size: patch.size } : {}),
      ...(patch.width !== undefined ? { width: patch.width } : {}),
      ...(patch.height !== undefined ? { height: patch.height } : {}),
      gradient: patch.gradient
        ? { ...this.custom.gradient, ...patch.gradient }
        : this.custom.gradient,
      effects: patch.effects
        ? { ...this.custom.effects, ...patch.effects }
        : this.custom.effects,
      motion: patch.motion
        ? { ...this.custom.motion, ...patch.motion }
        : this.custom.motion,
    };

    const sanitized = sanitizePersistedCustomState({
      gradient: next.gradient,
      effects: next.effects,
      motion: next.motion,
    });

    this.custom = {
      ...next,
      ...sanitized,
    };
    persistCustomState(this.custom);
  }

  resetCustom(): void {
    this.custom = createDefaultCustomizationState();
    persistCustomState(this.custom);
  }

  openCompare(concept: string): void {
    this.compareConcept = concept;
    this.compareOpen = true;
  }

  closeCompare(): void {
    this.compareOpen = false;
  }

  openDraw(): void {
    this.drawOpen = true;
  }

  closeDraw(): void {
    this.drawOpen = false;
  }

  openShortcuts(): void {
    this.shortcutsOpen = true;
  }

  closeShortcuts(): void {
    this.shortcutsOpen = false;
  }

  openCollections(): void {
    this.collectionsOpen = true;
  }

  closeCollections(): void {
    this.collectionsOpen = false;
  }

  showToast(msg: string, durationMs = 2600): void {
    if (this.toastTimer !== null) {
      clearTimeout(this.toastTimer);
      this.toastTimer = null;
    }
    this.toastMessage = msg;
    if (typeof window !== 'undefined') {
      this.toastTimer = setTimeout(() => {
        this.toastTimer = null;
        this.toastMessage = null;
      }, durationMs);
    }
  }

  clearToast(): void {
    if (this.toastTimer !== null) {
      clearTimeout(this.toastTimer);
      this.toastTimer = null;
    }
    this.toastMessage = null;
  }
}

export const inspectorState = new InspectorStore();
