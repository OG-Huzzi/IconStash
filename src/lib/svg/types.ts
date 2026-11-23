/**
 * Complete customization state and type definitions for the IconStash SVG
 * transform, effects, animation, and 9-target codegen pipeline.
 *
 * Schema mirrors legacy `localStorage["iconstash-custom"]` and `icons.js` 1:1.
 */

export const SVG_NS = "http://www.w3.org/2000/svg";
export const CUSTOM_STORAGE_KEY = "iconstash-custom";

export const MIN_GRADIENT_STOPS = 2;
export const MAX_GRADIENT_STOPS = 5;

export interface IconSvgInput {
  id: string;
  name: string;
  library?: string;
  librarySlug?: string;
  style?: string;
  svgPath?: string;
  svgContent?: string;
  viewBox?: string;
  width?: number;
  height?: number;
  strokeWidth?: number;
  npmPackage?: string;
  jsxImport?: string;
}

export type GradientProjection = "linear" | "radial";

export interface GradientStop {
  /** Hex or CSS color string for this stop. */
  c: string;
  /** Stop offset percentage (0–100). */
  p: number;
}

export interface GradientState {
  on: boolean;
  projection: GradientProjection;
  /** Linear gradient angle in degrees (0–360, default 90). */
  angle: number;
  /** Radial gradient center X percentage (0–100, default 50). */
  cx: number;
  /** Radial gradient center Y percentage (0–100, default 50). */
  cy: number;
  /** Radial gradient radius percentage (5–150, default 75). */
  r: number;
  /** 2 to 5 color stops. */
  stops: GradientStop[];
}

export type SurfaceTexture =
  | "none"
  | "paper"
  | "concrete"
  | "marble"
  | "wood"
  | "metal";

export type ActiveTexture = Exclude<SurfaceTexture, "none">;
export type MaterialTexture = "wood" | "metal";

export type RoundnessPreset = "soft" | "round" | "medium" | "sharp";

export interface RoundnessConfig {
  cap: "round" | "butt";
  join: "round" | "bevel" | "miter";
  widthScale: number;
}

export interface EffectsState {
  flipH: boolean;
  flipV: boolean;
  /** Rotation in degrees (0–360, default 0). */
  rotation: number;
  /** Gaussian blur stdDeviation (0–2, step 0.1, default 0). */
  blur: number;
  shadowOn: boolean;
  /** Drop shadow opacity percentage (0–100, default 40). */
  shadowOpacity: number;
  /** Drop shadow blur stdDeviation (0–8, default 2). */
  shadowBlur: number;
  /** Drop shadow X offset (-30..30 slider, clamped -20..20 in filter, default 0). */
  shadowX: number;
  /** Drop shadow Y offset (-30..30 slider, clamped -20..20 in filter, default 5). */
  shadowY: number;
  /** Drop shadow flood color (default "#000000"). */
  shadowColor?: string;
  /** Noise grain intensity (0–100, default 0). */
  noise: number;
  texture: SurfaceTexture;
  /** Surface texture opacity percentage (0–100, default 30). */
  textureOpacity: number;
  roundness: RoundnessPreset;
}

export type MotionType = "draw" | "stroke" | "bounce" | "shake" | "jump";
export type MotionEasing = "inout" | "in" | "out" | "linear";

export interface MotionState {
  on: boolean;
  type: MotionType;
  /** Animation duration in seconds (0.5–5.0, step 0.1, default 2). */
  duration: number;
  /** Loop infinitely when true, or play once when false. */
  loop: boolean;
  easing: MotionEasing;
}

/** Exact persisted shape stored in `localStorage["iconstash-custom"]`. */
export interface PersistedCustomState {
  gradient: GradientState;
  effects: EffectsState;
  motion: MotionState;
}

/** Complete inspector customization state including solid color, stroke, and dimensions. */
export interface CustomizationState extends PersistedCustomState {
  color: string;
  strokeWidth: number;
  /** Square export dimension in px (16–512, default 128). */
  size: number;
  /** Optional explicit export width (overrides `size` when set). */
  width?: number;
  /** Optional explicit export height (overrides `size` when set). */
  height?: number;
}

export interface SvgRenderOptions {
  size?: number | string;
  width?: number | string;
  height?: number | string;
  color?: string;
  fill?: string;
  stroke?: string;
  strokeWidth?: number;
  title?: string;
  gradient?: GradientState | null;
  effects?: Partial<EffectsState> | null;
  motion?: MotionState | null;
  /** Optional deterministic UID prefix for `<defs>` IDs (useful for SSR/tests). */
  uid?: string;
}

export type CodeFormat =
  | "svg"
  | "xml"
  | "jsx"
  | "vue"
  | "svelte"
  | "angular"
  | "html"
  | "css"
  | "base64";

export const CODE_FORMATS: readonly CodeFormat[] = [
  "svg",
  "xml",
  "jsx",
  "vue",
  "svelte",
  "angular",
  "html",
  "css",
  "base64",
] as const;

export const VALID_TEXTURES: ReadonlySet<ActiveTexture> = new Set<ActiveTexture>([
  "paper",
  "concrete",
  "marble",
  "wood",
  "metal",
]);

/**
 * Wood and metal are real materials that supply their own color gradients.
 * While active, solid color and custom gradient controls are locked.
 */
export const MATERIAL_TEXTURES: ReadonlySet<MaterialTexture> =
  new Set<MaterialTexture>(["wood", "metal"]);

export const ROUNDNESS_ORDER: readonly RoundnessPreset[] = [
  "soft",
  "round",
  "medium",
  "sharp",
] as const;

export const ROUNDNESS_PRESETS: Record<RoundnessPreset, RoundnessConfig> = {
  soft: { cap: "round", join: "round", widthScale: 0.75 },
  round: { cap: "round", join: "round", widthScale: 1 },
  medium: { cap: "round", join: "bevel", widthScale: 1 },
  sharp: { cap: "butt", join: "miter", widthScale: 1 },
};

export const MOTION_TYPES: readonly MotionType[] = [
  "draw",
  "stroke",
  "bounce",
  "shake",
  "jump",
] as const;

export const MOTION_EASING_MAP: Record<MotionEasing, string> = {
  linear: "linear",
  in: "ease-in",
  out: "ease-out",
  inout: "ease-in-out",
};

export function textureUsesMaterial(
  texture: string | null | undefined,
): texture is MaterialTexture {
  return (
    typeof texture === "string" &&
    MATERIAL_TEXTURES.has(texture as MaterialTexture)
  );
}

export function isActiveTexture(
  texture: string | null | undefined,
): texture is ActiveTexture {
  return (
    typeof texture === "string" && VALID_TEXTURES.has(texture as ActiveTexture)
  );
}

export function normalizeRoundness(
  value: string | null | undefined,
): RoundnessPreset | null {
  if (!value) return null;
  const lower = value.toLowerCase() as RoundnessPreset;
  return lower in ROUNDNESS_PRESETS ? lower : null;
}

export function createDefaultGradientState(): GradientState {
  return {
    on: false,
    projection: "linear",
    angle: 90,
    cx: 50,
    cy: 50,
    r: 75,
    stops: [
      { c: "#C1DD2D", p: 0 },
      { c: "#2563eb", p: 100 },
    ],
  };
}

export function createDefaultEffectsState(): EffectsState {
  return {
    flipH: false,
    flipV: false,
    rotation: 0,
    blur: 0,
    shadowOn: false,
    shadowOpacity: 40,
    shadowBlur: 2,
    shadowX: 0,
    shadowY: 5,
    shadowColor: "#000000",
    noise: 0,
    texture: "none",
    textureOpacity: 30,
    roundness: "round",
  };
}

export function createDefaultMotionState(): MotionState {
  return {
    on: false,
    type: "draw",
    duration: 2,
    loop: true,
    easing: "inout",
  };
}

export function createDefaultPersistedCustomState(): PersistedCustomState {
  return {
    gradient: createDefaultGradientState(),
    effects: createDefaultEffectsState(),
    motion: createDefaultMotionState(),
  };
}

export function createDefaultCustomizationState(): CustomizationState {
  return {
    color: "#2563eb",
    strokeWidth: 0.7,
    size: 128,
    ...createDefaultPersistedCustomState(),
  };
}

/**
 * Adds a new gradient stop by splitting the largest percentage gap, capped at 5 stops.
 * Mirrors legacy `app.js` `#grad-add-stop` behavior.
 */
export function addGradientStop(stops: readonly GradientStop[]): GradientStop[] {
  if (stops.length >= MAX_GRADIENT_STOPS) {
    return stops.map((s) => ({ ...s }));
  }
  const next = stops.map((s) => ({ ...s }));
  if (next.length < 2) {
    return createDefaultGradientState().stops;
  }
  let insertAt = next.length;
  let largestGap = -1;
  for (let i = 0; i < next.length - 1; i += 1) {
    const gap = next[i + 1].p - next[i].p;
    if (gap > largestGap) {
      largestGap = gap;
      insertAt = i + 1;
    }
  }
  const midPos = Math.round((next[insertAt - 1].p + next[insertAt].p) / 2);
  next.splice(insertAt, 0, { c: next[0].c, p: midPos });
  return next;
}

/**
 * Removes a gradient stop at `index`, preserving at least 2 stops.
 */
export function removeGradientStop(
  stops: readonly GradientStop[],
  index: number,
): GradientStop[] {
  if (stops.length <= MIN_GRADIENT_STOPS) {
    return stops.map((s) => ({ ...s }));
  }
  if (index < 0 || index >= stops.length) {
    return stops.map((s) => ({ ...s }));
  }
  return stops.filter((_, i) => i !== index).map((s) => ({ ...s }));
}

/**
 * Safely merges and validates a persisted `localStorage["iconstash-custom"]` payload.
 * Migrates unknown textures (e.g. legacy "fabric") to "none" and enforces 2–5 gradient stops.
 */
export function sanitizePersistedCustomState(
  raw: unknown,
): PersistedCustomState {
  const defaults = createDefaultPersistedCustomState();
  if (!raw || typeof raw !== "object") return defaults;

  const saved = raw as Partial<Record<keyof PersistedCustomState, unknown>>;

  const gradient: GradientState = {
    ...defaults.gradient,
    ...(saved.gradient && typeof saved.gradient === "object"
      ? (saved.gradient as Partial<GradientState>)
      : {}),
  };
  if (!Array.isArray(gradient.stops) || gradient.stops.length < MIN_GRADIENT_STOPS) {
    gradient.stops = defaults.gradient.stops;
  } else {
    gradient.stops = gradient.stops.slice(0, MAX_GRADIENT_STOPS).map((stop) => ({
      c: typeof stop?.c === "string" ? stop.c : "#2563eb",
      p: Number.isFinite(Number(stop?.p))
        ? Math.min(100, Math.max(0, Number(stop.p)))
        : 0,
    }));
  }
  if (gradient.projection !== "linear" && gradient.projection !== "radial") {
    gradient.projection = "linear";
  }

  const effects: EffectsState = {
    ...defaults.effects,
    ...(saved.effects && typeof saved.effects === "object"
      ? (saved.effects as Partial<EffectsState>)
      : {}),
  };
  if (
    effects.texture !== "none" &&
    !isActiveTexture(effects.texture)
  ) {
    effects.texture = "none";
  }
  effects.roundness = normalizeRoundness(effects.roundness) ?? "round";

  const motion: MotionState = {
    ...defaults.motion,
    ...(saved.motion && typeof saved.motion === "object"
      ? (saved.motion as Partial<MotionState>)
      : {}),
  };
  if (!MOTION_TYPES.includes(motion.type)) {
    motion.type = "draw";
  }
  if (!(motion.easing in MOTION_EASING_MAP)) {
    motion.easing = "inout";
  }

  return { gradient, effects, motion };
}
