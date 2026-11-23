import {
  clampNumber,
  escapeXml,
  expandViewBoxForRotation,
  normalizeSvgBody,
  parseViewBox,
} from "./normalize.js";
import {
  isActiveTexture,
  MOTION_EASING_MAP,
  normalizeRoundness,
  ROUNDNESS_PRESETS,
  SVG_NS,
  textureUsesMaterial,
  type ActiveTexture,
  type EffectsState,
  type GradientState,
  type IconSvgInput,
  type MaterialTexture,
  type MotionState,
  type SvgRenderOptions,
} from "./types.js";

interface RadialMaterialGradient {
  type: "radial";
  cx: string;
  cy: string;
  r: string;
  fx: string;
  fy: string;
  stops: ReadonlyArray<readonly [string, number]>;
}

interface LinearMaterialGradient {
  type: "linear";
  x1: number;
  y1: number;
  x2: number;
  y2: number;
  stops: ReadonlyArray<readonly [string, number]>;
}

type MaterialGradientDef = RadialMaterialGradient | LinearMaterialGradient;

/**
 * Real-material gradients matching legacy `icons.js:MATERIAL_GRADIENTS` 1:1.
 * Wood: 24-stop concentric growth rings; Metal: 15-stop diagonal brushed silver.
 */
export const MATERIAL_GRADIENTS: Record<MaterialTexture, MaterialGradientDef> = {
  wood: {
    type: "radial",
    cx: "50%",
    cy: "50%",
    r: "78%",
    fx: "43%",
    fy: "39%",
    stops: [
      ["#E0BB8C", 0],
      ["#D2A572", 4],
      ["#8A5930", 9],
      ["#D3A778", 10],
      ["#DAB27F", 16],
      ["#7E5029", 21],
      ["#CB9C68", 22],
      ["#D9B482", 29],
      ["#8D5C31", 34],
      ["#C79A66", 35],
      ["#D7AC76", 42],
      ["#7A4C27", 47],
      ["#C39562", 48],
      ["#D2A56E", 56],
      ["#85552C", 61],
      ["#BE915D", 62],
      ["#CFA06A", 70],
      ["#744824", 76],
      ["#B98B57", 77],
      ["#C79A66", 84],
      ["#6B4020", 90],
      ["#A87848", 91],
      ["#7A4C26", 96],
      ["#4E2F16", 100],
    ],
  },
  metal: {
    type: "linear",
    x1: 0,
    y1: 0,
    x2: 1,
    y2: 1,
    stops: [
      ["#3E4650", 0],
      ["#9AA6B3", 6],
      ["#FFFFFF", 12],
      ["#DDE6EF", 17],
      ["#8C97A4", 24],
      ["#3C444E", 33],
      ["#79838F", 42],
      ["#FFFFFF", 50],
      ["#C9D3DD", 55],
      ["#5A636E", 63],
      ["#A8B3BF", 72],
      ["#FFFFFF", 80],
      ["#C2CCD6", 86],
      ["#5A636E", 93],
      ["#98A3B0", 100],
    ],
  },
};

const FILL_STYLES = new Set(["fill", "solid", "bold"]);

let renderCounter = 0;

/**
 * Resets the internal SVG def ID counter (intended for deterministic unit tests).
 */
export function resetRenderCounter(): void {
  renderCounter = 0;
}

/**
 * Builds the `<linearGradient>` or `<radialGradient>` markup for user gradients.
 */
export function buildGradientDefs(gradient: GradientState, id: string): string {
  const safeId = escapeXml(id);
  const stops = (gradient.stops || [])
    .map(
      (stop) =>
        `<stop offset="${clampNumber(stop.p, 0, 100)}%" stop-color="${escapeXml(stop.c)}"/>`,
    )
    .join("");

  if (gradient.projection === "radial") {
    const cx = clampNumber(gradient.cx ?? 50, 0, 100);
    const cy = clampNumber(gradient.cy ?? 50, 0, 100);
    const r = clampNumber(gradient.r ?? 75, 5, 150);
    return `<radialGradient id="${safeId}" cx="${cx}%" cy="${cy}%" r="${r}%">${stops}</radialGradient>`;
  }

  const rad = ((Number(gradient.angle ?? 90) - 90) * Math.PI) / 180;
  const x1 = ((0.5 - Math.cos(rad) / 2) * 100).toFixed(1);
  const y1 = ((0.5 - Math.sin(rad) / 2) * 100).toFixed(1);
  const x2 = ((0.5 + Math.cos(rad) / 2) * 100).toFixed(1);
  const y2 = ((0.5 + Math.sin(rad) / 2) * 100).toFixed(1);
  return `<linearGradient id="${safeId}" x1="${x1}%" y1="${y1}%" x2="${x2}%" y2="${y2}%">${stops}</linearGradient>`;
}

/**
 * Builds the `<defs>` gradient markup for a real-material texture (`wood` or `metal`).
 */
export function buildMaterialDefs(texture: MaterialTexture, id: string): string {
  const safeId = escapeXml(id);
  const material = MATERIAL_GRADIENTS[texture];
  const stopMarkup = material.stops
    .map(
      ([c, p]) =>
        `<stop offset="${clampNumber(p, 0, 100)}%" stop-color="${escapeXml(c)}"/>`,
    )
    .join("");

  if (material.type === "radial") {
    return `<radialGradient id="${safeId}" cx="${material.cx}" cy="${material.cy}" r="${material.r}" fx="${material.fx}" fy="${material.fy}">${stopMarkup}</radialGradient>`;
  }
  return `<linearGradient id="${safeId}" x1="${material.x1}" y1="${material.y1}" x2="${material.x2}" y2="${material.y2}">${stopMarkup}</linearGradient>`;
}

/**
 * Builds the SVG filter primitives for one of the 5 surface textures
 * (`paper`, `concrete`, `marble`, `wood`, `metal`), clipping every overlay
 * to the icon shape via `feComposite operator="in"`.
 */
export function buildTexturePrims(
  texture: ActiveTexture,
  opacity: number | undefined,
  initialLast: string,
): { prims: string[]; last: string } {
  const op = clampNumber(opacity ?? 30, 0, 100) / 100;
  const prims: string[] = [];
  let last = initialLast;

  const tintLayer = (
    input: string,
    r: number,
    g: number,
    b: number,
    alpha: number,
    name: string,
  ): string => {
    prims.push(
      `<feColorMatrix in="${input}" type="matrix" values="0 0 0 0 ${r} 0 0 0 0 ${g} 0 0 0 0 ${b} 0 0 0 ${alpha.toFixed(3)} 0" result="${name}"/>`,
    );
    return name;
  };

  const overlay = (layers: string[], name: string): void => {
    prims.push(
      `<feMerge result="${name}n">${layers.map((n) => `<feMergeNode in="${n}"/>`).join("")}</feMerge>`,
    );
    prims.push(
      `<feComposite in="${name}n" in2="${last}" operator="in" result="${name}c"/>`,
    );
    prims.push(
      `<feMerge result="${name}m"><feMergeNode in="${last}"/><feMergeNode in="${name}c"/></feMerge>`,
    );
    last = `${name}m`;
  };

  const relief = (
    noise: string,
    surfaceScale: number,
    azimuth: number,
    elevation: number,
    slope: number,
    intercept: number,
    name: string,
  ): void => {
    prims.push(
      `<feDiffuseLighting in="${noise}" surfaceScale="${surfaceScale}" diffuseConstant="1" lighting-color="#FFFFFF" result="${name}l"><feDistantLight azimuth="${azimuth}" elevation="${elevation}"/></feDiffuseLighting>`,
    );
    prims.push(
      `<feComponentTransfer in="${name}l" result="${name}lr"><feFuncR type="linear" slope="${slope}" intercept="${intercept}"/><feFuncG type="linear" slope="${slope}" intercept="${intercept}"/><feFuncB type="linear" slope="${slope}" intercept="${intercept}"/></feComponentTransfer>`,
    );
    prims.push(
      `<feComposite in="${name}lr" in2="${last}" operator="in" result="${name}lc"/>`,
    );
    prims.push(
      `<feBlend in="${last}" in2="${name}lc" mode="multiply" result="${name}lm"/>`,
    );
    last = `${name}lm`;
  };

  if (texture === "metal") {
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.006 0.85" numOctaves="2" seed="11" stitchTiles="stitch" result="ist"/>`,
    );
    overlay([tintLayer("ist", 1, 1, 1, op * 0.22, "istw")], "ists");
    prims.push(
      `<feGaussianBlur in="SourceAlpha" stdDeviation="0.6" result="ismb"/>`,
    );
    prims.push(
      `<feSpecularLighting in="ismb" surfaceScale="1.6" specularConstant="0.6" specularExponent="26" lighting-color="#FFFFFF" result="isms"><feDistantLight azimuth="225" elevation="58"/></feSpecularLighting>`,
    );
    prims.push(
      `<feComposite in="isms" in2="SourceAlpha" operator="in" result="ismsc"/>`,
    );
    prims.push(
      `<feComposite in="${last}" in2="ismsc" operator="arithmetic" k1="0" k2="1" k3="1" k4="0" result="isml"/>`,
    );
    last = "isml";
  } else if (texture === "wood") {
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="3" seed="19" result="iswdn"/>`,
    );
    prims.push(
      `<feDisplacementMap in="${last}" in2="iswdn" scale="1.3" xChannelSelector="R" yChannelSelector="G" result="iswd"/>`,
    );
    last = "iswd";
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.62 0.014" numOctaves="3" seed="4" stitchTiles="stitch" result="ist"/>`,
    );
    const grain = tintLayer("ist", 0.16, 0.08, 0.03, op * 0.5, "istg");
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="3" seed="9" stitchTiles="stitch" result="isw"/>`,
    );
    const mottle = tintLayer("isw", 0.22, 0.11, 0.04, op * 0.18, "iswg");
    overlay([grain, mottle], "istx");
  } else if (texture === "paper") {
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.16" numOctaves="3" seed="5" stitchTiles="stitch" result="istb"/>`,
    );
    const blotch = tintLayer("istb", 0.1, 0.09, 0.08, op * 0.32, "istbc");
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.9 0.55" numOctaves="2" seed="12" stitchTiles="stitch" result="istf"/>`,
    );
    const fibre = tintLayer("istf", 1, 1, 1, op * 0.3, "istfc");
    const speck = tintLayer("istf", 0.15, 0.13, 0.11, op * 0.18, "istfk");
    overlay([blotch, fibre, speck], "istp");
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="3" seed="31" stitchTiles="stitch" result="ispb"/>`,
    );
    relief("ispb", 1.4, 55, 62, 0.28, 0.72, "ispr");
  } else if (texture === "concrete") {
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.13" numOctaves="4" seed="3" stitchTiles="stitch" result="istc"/>`,
    );
    const cement = tintLayer("istc", 0.12, 0.12, 0.13, op * 0.48, "istcc");
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="2" seed="17" stitchTiles="stitch" result="ists"/>`,
    );
    const aggregate = tintLayer("ists", 0.88, 0.89, 0.9, op * 0.4, "istsc");
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.32" numOctaves="2" seed="23" stitchTiles="stitch" result="istp"/>`,
    );
    const pits = tintLayer("istp", 0.05, 0.05, 0.06, op * 0.26, "istpc");
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="1.2" numOctaves="2" seed="8" stitchTiles="stitch" result="istsd"/>`,
    );
    const sand = tintLayer("istsd", 0.55, 0.56, 0.58, op * 0.22, "istsdc");
    overlay([cement, aggregate, pits, sand], "istccx");
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.18" numOctaves="4" seed="41" stitchTiles="stitch" result="iscb"/>`,
    );
    relief("iscb", 2.6, 70, 48, 0.45, 0.55, "iscr");
  } else if (texture === "marble") {
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.014 0.045" numOctaves="6" seed="7" stitchTiles="stitch" result="ismn"/>`,
    );
    prims.push(
      `<feColorMatrix in="ismn" type="matrix" values="0 0 0 0 0.06 0 0 0 0 0.07 0 0 0 0 0.10 1 0 0 0 0" result="ismna"/>`,
    );
    prims.push(
      `<feComponentTransfer in="ismna" result="ismvd"><feFuncA type="table" tableValues="0 0 0 0 0.22 1 0.22 0 0 0 0 0 0"/></feComponentTransfer>`,
    );
    prims.push(
      `<feComposite in="ismvd" in2="${last}" operator="in" result="ismvdc"/>`,
    );
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.024 0.07" numOctaves="5" seed="23" stitchTiles="stitch" result="ismln"/>`,
    );
    prims.push(
      `<feColorMatrix in="ismln" type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0" result="ismlna"/>`,
    );
    prims.push(
      `<feComponentTransfer in="ismlna" result="ismlv"><feFuncA type="table" tableValues="0 0 0 0 0 0 0.3 0 0 0 0 0 0"/></feComponentTransfer>`,
    );
    prims.push(
      `<feComposite in="ismlv" in2="${last}" operator="in" result="ismlvc"/>`,
    );
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="3" seed="41" stitchTiles="stitch" result="ismc"/>`,
    );
    const shade = tintLayer("ismc", 0.08, 0.09, 0.12, op * 0.14, "ismcs");
    overlay(["ismvdc", "ismlvc", shade], "ismvx");
  }

  return { prims, last };
}

/**
 * Builds the chained `<filter>` definition:
 *   1. Blur (`feGaussianBlur`)
 *   2. Drop Shadow (`feDropShadow`)
 *   3. Noise Grain (`feTurbulence` + `feColorMatrix` + `feComposite` + `feMerge`)
 *   4. Surface Texture (`paper`, `concrete`, `marble`, `wood`, `metal`)
 */
export function buildEffectFilter(
  effects: Partial<EffectsState>,
  id: string,
): string {
  const prims: string[] = [];
  let last = "SourceGraphic";

  if ((effects.blur ?? 0) > 0) {
    prims.push(
      `<feGaussianBlur in="${last}" stdDeviation="${clampNumber(effects.blur, 0, 2)}" result="isb"/>`,
    );
    last = "isb";
  }

  if (effects.shadowOn && (effects.shadowOpacity ?? 0) > 0) {
    const shadowColor = escapeXml(effects.shadowColor || "#000000");
    prims.push(
      `<feDropShadow in="${last}" dx="${clampNumber(effects.shadowX ?? 0, -20, 20)}" dy="${clampNumber(effects.shadowY ?? 5, -20, 20)}" stdDeviation="${clampNumber(effects.shadowBlur ?? 2, 0, 8)}" flood-color="${shadowColor}" flood-opacity="${(clampNumber(effects.shadowOpacity ?? 40, 0, 100) / 100).toFixed(2)}" result="iss"/>`,
    );
    last = "iss";
  }

  if ((effects.noise ?? 0) > 0) {
    prims.push(
      `<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" result="isn"/>`,
    );
    prims.push(
      `<feColorMatrix in="isn" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ${(clampNumber(effects.noise, 0, 100) / 100).toFixed(2)} 0" result="isna"/>`,
    );
    prims.push(
      `<feComposite in="isna" in2="${last}" operator="in" result="isnc"/>`,
    );
    prims.push(
      `<feMerge result="isnm"><feMergeNode in="${last}"/><feMergeNode in="isnc"/></feMerge>`,
    );
    last = "isnm";
  }

  if (isActiveTexture(effects.texture)) {
    const built = buildTexturePrims(effects.texture, effects.textureOpacity, last);
    prims.push(...built.prims);
    last = built.last;
  }

  if (!prims.length) return "";
  return `<filter id="${escapeXml(id)}" x="-45%" y="-45%" width="190%" height="190%">${prims.join("")}</filter>`;
}

/**
 * Builds the embedded `<style>` CSS keyframes for all 5 IconStash animations:
 * `draw`, `stroke`, `bounce`, `shake`, `jump`.
 */
export function buildMotionCss(motion: MotionState): string {
  const shapes = ":is(path,circle,rect,line,polyline,polygon,ellipse)";
  const dur = clampNumber(motion.duration, 0.5, 5);
  const timing = MOTION_EASING_MAP[motion.easing] || "ease-in-out";
  const iter = motion.loop ? "infinite" : "1";

  switch (motion.type) {
    case "draw":
      return `.is-m-draw ${shapes}{stroke-dasharray:1;stroke-dashoffset:1;animation:is-draw ${dur}s ${timing} ${iter} forwards}@keyframes is-draw{to{stroke-dashoffset:0}}`;
    case "stroke":
      return `.is-m-stroke ${shapes}{stroke-dasharray:5 3;animation:is-flow ${dur}s linear ${iter}}@keyframes is-flow{to{stroke-dashoffset:-32}}`;
    case "shake":
      return `.is-m-shake{animation:is-shake ${dur}s ease-in-out ${iter}}@keyframes is-shake{0%,100%{transform:rotate(0deg)}25%{transform:rotate(-9deg)}75%{transform:rotate(9deg)}}`;
    case "jump":
      return `.is-m-jump{animation:is-jump ${dur}s ${timing} ${iter}}@keyframes is-jump{0%,100%{transform:translateY(0)}35%{transform:translateY(-18%)}55%{transform:translateY(0)}70%{transform:translateY(-7%)}85%{transform:translateY(0)}}`;
    case "bounce":
      return `.is-m-bounce{animation:is-bounce ${dur}s ${timing} ${iter}}@keyframes is-bounce{0%,100%{transform:translateY(0) scale(1,1)}30%{transform:translateY(-22%) scale(.96,1.06)}55%{transform:translateY(0) scale(1.05,.92)}75%{transform:translateY(-7%) scale(1,1)}}`;
    default:
      return "";
  }
}

/**
 * Builds the full customized standalone `<svg>` markup on-demand for inspector
 * preview and export. Never called on virtualized grid tiles.
 */
export function renderCustomizedSvg(
  icon: IconSvgInput | null | undefined,
  options: SvgRenderOptions = {},
): string {
  if (!icon) return "";

  const uid = options.uid || `is${(++renderCounter).toString(36)}`;
  const gradId = `${uid}-grad`;
  const matId = `${uid}-mat`;
  const fxId = `${uid}-fx`;

  const baseViewBox =
    icon.viewBox || `0 0 ${icon.width || 24} ${icon.height || 24}`;
  const defaultSize = options.size ?? "100%";
  const outWidth = options.width ?? defaultSize;
  const outHeight = options.height ?? defaultSize;

  const hasCustomStroke =
    Object.prototype.hasOwnProperty.call(options, "strokeWidth") &&
    options.strokeWidth !== undefined;
  const strokeWidth = options.strokeWidth ?? icon.strokeWidth ?? 2;

  const effects = options.effects ?? null;
  const usesMaterial = textureUsesMaterial(effects?.texture);
  const color = usesMaterial ? "#8A8A8A" : options.color || "currentColor";

  const isFillStyle = Boolean(icon.style && FILL_STYLES.has(icon.style));
  const fill = options.fill || (isFillStyle ? "currentColor" : "none");

  const roundKey = normalizeRoundness(effects?.roundness);
  const roundPreset = roundKey ? ROUNDNESS_PRESETS[roundKey] : null;

  const activeMaterial: MaterialTexture | null = usesMaterial
    ? (effects!.texture as MaterialTexture)
    : null;
  const gradient = usesMaterial ? null : options.gradient ?? null;
  const hasGradient = Boolean(
    gradient &&
      gradient.on &&
      Array.isArray(gradient.stops) &&
      gradient.stops.length >= 2,
  );

  const paintAttr = activeMaterial
    ? `url(#${matId})`
    : hasGradient
      ? `url(#${gradId})`
      : null;

  const stroke =
    options.stroke ||
    (fill === "none" || hasCustomStroke ? paintAttr || "currentColor" : "none");

  const fillPaint = activeMaterial
    ? `url(#${matId})`
    : paintAttr && fill === "currentColor"
      ? paintAttr
      : isFillStyle && !paintAttr
        ? "currentColor"
        : fill;

  const linecap = roundPreset ? roundPreset.cap : "round";
  const linejoin = roundPreset ? roundPreset.join : "round";
  const effectiveStrokeWidth = roundPreset
    ? strokeWidth * roundPreset.widthScale
    : strokeWidth;

  let viewBoxOut = baseViewBox;
  let body = normalizeSvgBody(icon, {
    strokeWidth: hasCustomStroke ? options.strokeWidth : undefined,
  });
  let defsMarkup = "";
  let outerAttrs = "";
  let innerAttrs = "";
  let styleMarkup = "";

  if (activeMaterial) {
    defsMarkup += buildMaterialDefs(activeMaterial, matId);
    body = body.replace(/fill="currentColor"/g, `fill="url(#${matId})"`);
    body = body.replace(/stroke="currentColor"/g, `stroke="url(#${matId})"`);
  } else if (hasGradient && gradient) {
    defsMarkup += buildGradientDefs(gradient, gradId);
    body = body.replace(/fill="currentColor"/g, `fill="url(#${gradId})"`);
    body = body.replace(/stroke="currentColor"/g, `stroke="url(#${gradId})"`);
  }

  if (effects) {
    if (roundPreset) {
      body = body
        .replace(/\sstroke-linecap="[^"]*"/gi, "")
        .replace(/\sstroke-linejoin="[^"]*"/gi, "")
        .replace(/\sstroke-width="[^"]*"/gi, "");
    }

    const rect = parseViewBox(baseViewBox, icon.width, icon.height);
    const cx = rect.x + rect.width / 2;
    const cy = rect.y + rect.height / 2;
    const transforms: string[] = [];

    if (effects.rotation) {
      const expanded = expandViewBoxForRotation(rect, effects.rotation);
      if (expanded.rotation) {
        transforms.push(`rotate(${expanded.rotation} ${expanded.cx} ${expanded.cy})`);
        viewBoxOut = expanded.viewBox;
      }
    }

    if (effects.flipH || effects.flipV) {
      const sx = effects.flipH ? -1 : 1;
      const sy = effects.flipV ? -1 : 1;
      transforms.push(
        `translate(${cx} ${cy}) scale(${sx} ${sy}) translate(${-cx} ${-cy})`,
      );
    }

    if (transforms.length) {
      outerAttrs += ` transform="${transforms.join(" ")}"`;
    }

    const filterMarkup = buildEffectFilter(effects, fxId);
    if (filterMarkup) {
      defsMarkup += filterMarkup;
      outerAttrs += ` filter="url(#${fxId})"`;
    }
  }

  const motion = options.motion;
  if (motion && motion.on) {
    styleMarkup = `<style>${buildMotionCss(motion)}</style>`;
    if (motion.type === "draw") {
      body = body.replace(
        /<(path|circle|rect|line|polyline|polygon|ellipse)\b/g,
        '<$1 pathLength="1"',
      );
    }
    innerAttrs = ` class="is-m is-m-${escapeXml(motion.type)}" style="transform-box:fill-box;transform-origin:center"`;
  }

  let wrapped = body;
  if (innerAttrs) wrapped = `<g${innerAttrs}>${wrapped}</g>`;
  if (outerAttrs) wrapped = `<g${outerAttrs}>${wrapped}</g>`;

  const attrs: string[] = [
    `viewBox="${escapeXml(viewBoxOut)}"`,
    `width="${escapeXml(outWidth)}"`,
    `height="${escapeXml(outHeight)}"`,
    `role="img"`,
    `aria-label="${escapeXml(icon.name || icon.id)} icon"`,
    `fill="${escapeXml(fillPaint)}"`,
    `stroke="${escapeXml(stroke)}"`,
    `stroke-width="${escapeXml(effectiveStrokeWidth)}"`,
    `stroke-linecap="${linecap}"`,
    `stroke-linejoin="${linejoin}"`,
    `paint-order="stroke fill markers"`,
    `style="color:${escapeXml(color)};fill:${escapeXml(fillPaint)};stroke:${escapeXml(stroke)};stroke-width:${escapeXml(effectiveStrokeWidth)}"`,
  ];

  if (options.title) {
    attrs.push(`title="${escapeXml(options.title)}"`);
  }

  const titleTag = options.title
    ? `<title>${escapeXml(options.title)}</title>`
    : "";

  return `<svg xmlns="${SVG_NS}" ${attrs.join(" ")}>${titleTag}${defsMarkup ? `<defs>${defsMarkup}</defs>` : ""}${styleMarkup}${wrapped}</svg>`;
}

/** Alias matching legacy `icons.js:renderSVG`. */
export const renderSVG = renderCustomizedSvg;
