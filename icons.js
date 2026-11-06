(function () {
  const VOID_NS = "http://www.w3.org/2000/svg";
  let zipLibraryPromise = null;

  function escapeHtml(value) {
    return String(value ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function slugFilePart(value) {
    return String(value || "icon")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "") || "icon";
  }

  function normalizeSvgBody(icon, options = {}) {
    if (!options.strokeWidth && icon._normalizedBody) {
      return icon._normalizedBody;
    }
    const body = icon.svgPath || icon.svgContent || "";
    let normalized = body;
    if (!/<(path|g|circle|rect|line|polyline|polygon|ellipse|defs|use|clipPath|mask)\b/i.test(body)) {
      normalized = `<path d="${escapeHtml(body)}"></path>`;
    }
    normalized = normalized.replace(/\s(fill|stroke)="(?!none\b|transparent\b|url\(|freeze\b|remove\b)[^"]*"/gi, (_match, attr) => ` ${attr}="currentColor"`);
    normalized = normalized.replace(/\s(fill|stroke)='(?!none\b|transparent\b|url\(|freeze\b|remove\b)[^']*'/gi, (_match, attr) => ` ${attr}="currentColor"`);
    if (!options.strokeWidth) {
      icon._normalizedBody = normalized;
    }
    if (options.strokeWidth) {
      if (/\sstroke-width=/i.test(normalized)) {
        normalized = normalized
          .replace(/\sstroke-width="[^"]*"/gi, ` stroke-width="${escapeHtml(options.strokeWidth)}"`)
          .replace(/\sstroke-width='[^']*'/gi, ` stroke-width="${escapeHtml(options.strokeWidth)}"`);
      }
    }
    return normalized;
  }

  function clampNumber(value, min, max) {
    const n = Number(value);
    if (Number.isNaN(n)) return min;
    return Math.min(max, Math.max(min, n));
  }

  // A texture is either a real material (supplies its own colour, so the
  // chosen icon colour / gradient is ignored) or a surface finish applied on
  // top of the chosen colour.
  const MATERIAL_TEXTURES = new Set(["wood", "metal"]);

  function textureUsesMaterial(texture) {
    return MATERIAL_TEXTURES.has(texture);
  }

  // Polished silver: sharp, high-contrast specular reflection bands in cool
  // neutral greys. Wood: concentric growth rings of a cut trunk — pale
  // earlywood followed by a thin dark latewood line, unevenly spaced, with a
  // dark bark rim at the outer edge.
  const MATERIAL_GRADIENTS = {
    wood: {
      type: "radial",
      cx: "50%", cy: "50%", r: "78%", fx: "43%", fy: "39%",
      stops: [
        ["#E0BB8C", 0], ["#D2A572", 4], ["#8A5930", 9],
        ["#D3A778", 10], ["#DAB27F", 16], ["#7E5029", 21],
        ["#CB9C68", 22], ["#D9B482", 29], ["#8D5C31", 34],
        ["#C79A66", 35], ["#D7AC76", 42], ["#7A4C27", 47],
        ["#C39562", 48], ["#D2A56E", 56], ["#85552C", 61],
        ["#BE915D", 62], ["#CFA06A", 70], ["#744824", 76],
        ["#B98B57", 77], ["#C79A66", 84], ["#6B4020", 90],
        ["#A87848", 91], ["#7A4C26", 96], ["#4E2F16", 100]
      ]
    },
    metal: {
      type: "linear",
      x1: 0, y1: 0, x2: 1, y2: 1,
      stops: [
        ["#3E4650", 0], ["#9AA6B3", 6], ["#FFFFFF", 12], ["#DDE6EF", 17],
        ["#8C97A4", 24], ["#3C444E", 33], ["#79838F", 42], ["#FFFFFF", 50],
        ["#C9D3DD", 55], ["#5A636E", 63], ["#A8B3BF", 72], ["#FFFFFF", 80],
        ["#C2CCD6", 86], ["#5A636E", 93], ["#98A3B0", 100]
      ]
    }
  };

  const VALID_TEXTURES = new Set(["paper", "concrete", "wood", "metal"]);

  // Each recipe builds a self-contained SVG filter chain. `last` is the result
  // name of the preceding effect; every overlay is clipped to the icon shape
  // with feComposite operator="in" so nothing spills outside the strokes.
  function buildTexturePrims(texture, opacity, last) {
    const op = clampNumber(opacity ?? 30, 0, 100) / 100;
    const prims = [];
    const tintLayer = (input, r, g, b, alpha, name) => {
      prims.push(`<feColorMatrix in="${input}" type="matrix" values="0 0 0 0 ${r} 0 0 0 0 ${g} 0 0 0 0 ${b} 0 0 0 ${alpha.toFixed(3)} 0" result="${name}"/>`);
      return name;
    };
    const overlay = (layers, name) => {
      prims.push(`<feMerge result="${name}n">${layers.map((n) => `<feMergeNode in="${n}"/>`).join("")}</feMerge>`);
      prims.push(`<feComposite in="${name}n" in2="${last}" operator="in" result="${name}c"/>`);
      prims.push(`<feMerge result="${name}m"><feMergeNode in="${last}"/><feMergeNode in="${name}c"/></feMerge>`);
      last = `${name}m`;
    };
    // Bump-lit relief multiplies the chosen colour instead of replacing it, so
    // the surface texture is visible while the user's colour stays in charge.
    const relief = (noise, surfaceScale, azimuth, elevation, slope, intercept, name) => {
      prims.push(`<feDiffuseLighting in="${noise}" surfaceScale="${surfaceScale}" diffuseConstant="1" lighting-color="#FFFFFF" result="${name}l"><feDistantLight azimuth="${azimuth}" elevation="${elevation}"/></feDiffuseLighting>`);
      prims.push(`<feComponentTransfer in="${name}l" result="${name}lr"><feFuncR type="linear" slope="${slope}" intercept="${intercept}"/><feFuncG type="linear" slope="${slope}" intercept="${intercept}"/><feFuncB type="linear" slope="${slope}" intercept="${intercept}"/></feComponentTransfer>`);
      prims.push(`<feComposite in="${name}lr" in2="${last}" operator="in" result="${name}lc"/>`);
      prims.push(`<feBlend in="${last}" in2="${name}lc" mode="multiply" result="${name}lm"/>`);
      last = `${name}lm`;
    };

    if (texture === "metal") {
      // Fine horizontal brushed streaks across the silver bands.
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.006 0.85" numOctaves="2" seed="11" stitchTiles="stitch" result="ist"/>`);
      overlay([tintLayer("ist", 1, 1, 1, op * 0.22, "istw")], "ists");
      // A bevelled specular highlight clipped to the shape is what makes the
      // bands read as polished metal instead of flat grey stripes.
      prims.push(`<feGaussianBlur in="SourceAlpha" stdDeviation="0.6" result="ismb"/>`);
      prims.push(`<feSpecularLighting in="ismb" surfaceScale="1.6" specularConstant="0.6" specularExponent="26" lighting-color="#FFFFFF" result="isms"><feDistantLight azimuth="225" elevation="58"/></feSpecularLighting>`);
      prims.push(`<feComposite in="isms" in2="SourceAlpha" operator="in" result="ismsc"/>`);
      prims.push(`<feComposite in="${last}" in2="ismsc" operator="arithmetic" k1="0" k2="1" k3="1" k4="0" result="isml"/>`);
      last = "isml";
    } else if (texture === "wood") {
      // Growth rings in a real trunk are never perfect circles. A gentle
      // displacement warps the painted bands into irregular, organic rings.
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="3" seed="19" result="iswdn"/>`);
      prims.push(`<feDisplacementMap in="${last}" in2="iswdn" scale="1.3" xChannelSelector="R" yChannelSelector="G" result="iswd"/>`);
      last = "iswd";
      // Longitudinal pores / grain laid over the concentric growth rings.
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.62 0.014" numOctaves="3" seed="4" stitchTiles="stitch" result="ist"/>`);
      const grain = tintLayer("ist", 0.16, 0.08, 0.03, op * 0.50, "istg");
      // Low-frequency mottling breaks up the perfect symmetry of the rings.
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="3" seed="9" stitchTiles="stitch" result="isw"/>`);
      const mottle = tintLayer("isw", 0.22, 0.11, 0.04, op * 0.18, "iswg");
      overlay([grain, mottle], "istx");
    } else if (texture === "paper") {
      // Frequencies are tuned for a 24-unit viewBox: a period of a few units
      // is visible on the strokes, a period of 80+ units is a flat wash.
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.16" numOctaves="3" seed="5" stitchTiles="stitch" result="istb"/>`);
      const blotch = tintLayer("istb", 0.10, 0.09, 0.08, op * 0.32, "istbc");
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.9 0.55" numOctaves="2" seed="12" stitchTiles="stitch" result="istf"/>`);
      const fibre = tintLayer("istf", 1, 1, 1, op * 0.30, "istfc");
      const speck = tintLayer("istf", 0.15, 0.13, 0.11, op * 0.18, "istfk");
      overlay([blotch, fibre, speck], "istp");
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="3" seed="31" stitchTiles="stitch" result="ispb"/>`);
      relief("ispb", 1.4, 55, 62, 0.28, 0.72, "ispr");
    } else if (texture === "concrete") {
      // Four scales of aggregate, from broad cement mottling to fine sand.
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.13" numOctaves="4" seed="3" stitchTiles="stitch" result="istc"/>`);
      const cement = tintLayer("istc", 0.12, 0.12, 0.13, op * 0.48, "istcc");
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="2" seed="17" stitchTiles="stitch" result="ists"/>`);
      const aggregate = tintLayer("ists", 0.88, 0.89, 0.90, op * 0.40, "istsc");
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.32" numOctaves="2" seed="23" stitchTiles="stitch" result="istp"/>`);
      const pits = tintLayer("istp", 0.05, 0.05, 0.06, op * 0.26, "istpc");
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="1.2" numOctaves="2" seed="8" stitchTiles="stitch" result="istsd"/>`);
      const sand = tintLayer("istsd", 0.55, 0.56, 0.58, op * 0.22, "istsdc");
      overlay([cement, aggregate, pits, sand], "istccx");
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.18" numOctaves="4" seed="41" stitchTiles="stitch" result="iscb"/>`);
      relief("iscb", 2.6, 70, 48, 0.45, 0.55, "iscr");
    }
    return { prims, last };
  }

  function buildGradientDefs(gradient, id) {
    const stops = (gradient.stops || [])
      .map((stop) => `<stop offset="${clampNumber(stop.p, 0, 100)}%" stop-color="${escapeHtml(stop.c)}"/>`)
      .join("");
    let el;
    if (gradient.projection === "radial") {
      el = `<radialGradient id="${id}" cx="${clampNumber(gradient.cx ?? 50, 0, 100)}%" cy="${clampNumber(gradient.cy ?? 50, 0, 100)}%" r="${clampNumber(gradient.r ?? 75, 5, 150)}%">${stops}</radialGradient>`;
    } else {
      const rad = ((Number(gradient.angle ?? 90) - 90) * Math.PI) / 180;
      const x1 = ((0.5 - Math.cos(rad) / 2) * 100).toFixed(1);
      const y1 = ((0.5 - Math.sin(rad) / 2) * 100).toFixed(1);
      const x2 = ((0.5 + Math.cos(rad) / 2) * 100).toFixed(1);
      const y2 = ((0.5 + Math.sin(rad) / 2) * 100).toFixed(1);
      el = `<linearGradient id="${id}" x1="${x1}%" y1="${y1}%" x2="${x2}%" y2="${y2}%">${stops}</linearGradient>`;
    }
    return el;
  }

  const ROUNDNESS_PRESETS = {
    soft: { cap: "round", join: "round", widthScale: 0.75 },
    round: { cap: "round", join: "round", widthScale: 1 },
    medium: { cap: "round", join: "bevel", widthScale: 1 },
    sharp: { cap: "butt", join: "miter", widthScale: 1 }
  };

  function buildEffectFilter(effects, id) {
    const prims = [];
    let last = "SourceGraphic";
    if (effects.blur > 0) {
      prims.push(`<feGaussianBlur in="${last}" stdDeviation="${clampNumber(effects.blur, 0, 2)}" result="isb"/>`);
      last = "isb";
    }
    if (effects.shadowOn && effects.shadowOpacity > 0) {
      prims.push(
        `<feDropShadow in="${last}" dx="${clampNumber(effects.shadowX, -20, 20)}" dy="${clampNumber(effects.shadowY, -20, 20)}" stdDeviation="${clampNumber(effects.shadowBlur, 0, 8)}" flood-color="#000000" flood-opacity="${(clampNumber(effects.shadowOpacity, 0, 100) / 100).toFixed(2)}" result="iss"/>`
      );
      last = "iss";
    }
    if (effects.noise > 0) {
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" result="isn"/>`);
      prims.push(`<feColorMatrix in="isn" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ${(clampNumber(effects.noise, 0, 100) / 100).toFixed(2)} 0" result="isna"/>`);
      prims.push(`<feComposite in="isna" in2="${last}" operator="in" result="isnc"/>`);
      prims.push(`<feMerge result="isnm"><feMergeNode in="${last}"/><feMergeNode in="isnc"/></feMerge>`);
      last = "isnm";
    }
    if (effects.texture && VALID_TEXTURES.has(effects.texture)) {
      const built = buildTexturePrims(effects.texture, effects.textureOpacity, last);
      prims.push(...built.prims);
      last = built.last;
    }
    if (!prims.length) return "";
    return `<filter id="${id}" x="-45%" y="-45%" width="190%" height="190%">${prims.join("")}</filter>`;
  }

  let renderCounter = 0;

  function buildMotionCss(motion) {
    const shapes = ":is(path,circle,rect,line,polyline,polygon,ellipse)";
    const dur = clampNumber(motion.duration, 0.5, 5);
    const timing = MOTION_EASING[motion.easing] || "ease-in-out";
    const iter = motion.loop ? "infinite" : "1";
    let type = "";
    if (motion.type === "draw") {
      type = `.is-m-draw ${shapes}{stroke-dasharray:1;stroke-dashoffset:1;animation:is-draw ${dur}s ${timing} ${iter} forwards}@keyframes is-draw{to{stroke-dashoffset:0}}`;
    } else if (motion.type === "stroke") {
      type = `.is-m-stroke ${shapes}{stroke-dasharray:5 3;animation:is-flow ${dur}s linear ${iter}}@keyframes is-flow{to{stroke-dashoffset:-32}}`;
    } else if (motion.type === "shake") {
      type = `.is-m-shake{animation:is-shake ${dur}s ease-in-out ${iter}}@keyframes is-shake{0%,100%{transform:rotate(0deg)}25%{transform:rotate(-9deg)}75%{transform:rotate(9deg)}}`;
    } else if (motion.type === "jump") {
      type = `.is-m-jump{animation:is-jump ${dur}s ${timing} ${iter}}@keyframes is-jump{0%,100%{transform:translateY(0)}35%{transform:translateY(-18%)}55%{transform:translateY(0)}70%{transform:translateY(-7%)}85%{transform:translateY(0)}}`;
    } else if (motion.type === "bounce") {
      type = `.is-m-bounce{animation:is-bounce ${dur}s ${timing} ${iter}}@keyframes is-bounce{0%,100%{transform:translateY(0) scale(1,1)}30%{transform:translateY(-22%) scale(.96,1.06)}55%{transform:translateY(0) scale(1.05,.92)}75%{transform:translateY(-7%) scale(1,1)}}`;
    }
    return type;
  }

  const MOTION_EASING = { linear: "linear", in: "ease-in", out: "ease-out", inout: "ease-in-out" };

  function renderSVG(icon, options = {}) {
    if (!icon) return "";
    // SVG ids are document-global. Several icons can be rendered on one page,
    // so every def/filter gets a unique id — otherwise two different textures
    // both resolve to the first `is-mat` gradient in DOM order.
    const uid = `is${(++renderCounter).toString(36)}`;
    const gradId = `${uid}-grad`;
    const matId = `${uid}-mat`;
    const fxId = `${uid}-fx`;
    const viewBox = icon.viewBox || `0 0 ${icon.width || 24} ${icon.height || 24}`;
    const size = options.size || "100%";
    const strokeWidth = options.strokeWidth ?? icon.strokeWidth ?? 2;
    const effects = options.effects;
    // Wood and metal are real materials: they supply their own colour, so the
    // chosen icon colour and gradient must not tint them.
    const usesMaterial = textureUsesMaterial(effects?.texture);
    const color = usesMaterial ? "#8A8A8A" : (options.color || "currentColor");
    const fillStyles = new Set(["fill", "solid", "bold"]);
    const fill = options.fill || (fillStyles.has(icon.style) ? "currentColor" : "none");
    const roundPreset = options.effects && ROUNDNESS_PRESETS[options.effects.roundness] ? ROUNDNESS_PRESETS[options.effects.roundness] : null;
    const material = usesMaterial ? MATERIAL_GRADIENTS[effects.texture] : null;
    const gradient = usesMaterial ? null : options.gradient;
    const paintAttr = material ? `url(#${matId})` : (gradient && gradient.on && Array.isArray(gradient.stops) && gradient.stops.length >= 2 ? `url(#${gradId})` : null);
    const hasCustomStroke = Object.prototype.hasOwnProperty.call(options, "strokeWidth");
    const stroke = options.stroke || (fill === "none" || hasCustomStroke ? (paintAttr || "currentColor") : "none");
    const fillPaint = material ? `url(#${matId})` : (paintAttr && fill === "currentColor" ? paintAttr : (fillStyles.has(icon.style) && !paintAttr ? "currentColor" : fill));
    const linecap = roundPreset ? roundPreset.cap : "round";
    const linejoin = roundPreset ? roundPreset.join : "round";
    const effectiveStrokeWidth = roundPreset ? (strokeWidth * roundPreset.widthScale) : strokeWidth;
    let viewBoxOut = viewBox;
    const attrs = [
      `viewBox="${escapeHtml(viewBoxOut)}"`,
      `width="${escapeHtml(size)}"`,
      `height="${escapeHtml(size)}"`,
      `role="img"`,
      `aria-label="${escapeHtml(icon.name || icon.id)} icon"`,
      `fill="${fillPaint}"`,
      `stroke="${stroke}"`,
      `stroke-width="${escapeHtml(effectiveStrokeWidth)}"`,
      `stroke-linecap="${linecap}"`,
      `stroke-linejoin="${linejoin}"`,
      `paint-order="stroke fill markers"`,
      `style="color:${escapeHtml(color)};fill:${escapeHtml(fillPaint)};stroke:${escapeHtml(stroke)};stroke-width:${escapeHtml(effectiveStrokeWidth)}"`
    ];
    if (options.title) {
      attrs.push(`title="${escapeHtml(options.title)}"`);
    }
    const titleTag = options.title ? `<title>${escapeHtml(options.title)}</title>` : "";

    let body = normalizeSvgBody(icon, options);
    let defsMarkup = "";
    let outerAttrs = "";
    let innerAttrs = "";
    let styleMarkup = "";


    if (material) {
      // Material colours are used pure — never blended with the chosen colour.
      const stopMarkup = material.stops
        .map(([c, p]) => `<stop offset="${clampNumber(p, 0, 100)}%" stop-color="${escapeHtml(c)}"/>`)
        .join("");
      if (material.type === "radial") {
        defsMarkup += `<radialGradient id="${matId}" cx="${material.cx}" cy="${material.cy}" r="${material.r}" fx="${material.fx}" fy="${material.fy}">${stopMarkup}</radialGradient>`;
      } else {
        defsMarkup += `<linearGradient id="${matId}" x1="${material.x1}" y1="${material.y1}" x2="${material.x2}" y2="${material.y2}">${stopMarkup}</linearGradient>`;
      }
      body = body.replace(/fill="currentColor"/g, `fill="url(#${matId})"`);
      body = body.replace(/stroke="currentColor"/g, `stroke="url(#${matId})"`);
    } else if (gradient && gradient.on && Array.isArray(gradient.stops) && gradient.stops.length >= 2) {
      defsMarkup += buildGradientDefs(gradient, gradId);
      body = body.replace(/fill="currentColor"/g, `fill="url(#${gradId})"`);
      body = body.replace(/stroke="currentColor"/g, `stroke="url(#${gradId})"`);
    }

    const effectsLocal = effects;
    if (effectsLocal) {
      if (roundPreset) {
        body = body.replace(/\sstroke-linecap="[^"]*"/gi, "").replace(/\sstroke-linejoin="[^"]*"/gi, "");
        body = body.replace(/\sstroke-width="[^"]*"/gi, "");
      }
      const dims = String(viewBox).split(/[\s,]+/).map(Number);
      const vbX = Number.isFinite(dims[0]) ? dims[0] : 0;
      const vbY = Number.isFinite(dims[1]) ? dims[1] : 0;
      const vw = (Number.isFinite(dims[2]) ? dims[2] : 24) || 24;
      const vh = (Number.isFinite(dims[3]) ? dims[3] : 24) || 24;
      const cx = vbX + vw / 2;
      const cy = vbY + vh / 2;
      const transforms = [];
      if (effects.rotation) {
        const rot = clampNumber(effects.rotation, 0, 360) % 360;
        if (rot) {
          transforms.push(`rotate(${rot} ${cx} ${cy})`);
          const rad = (rot * Math.PI) / 180;
          const cosA = Math.abs(Math.cos(rad));
          const sinA = Math.abs(Math.sin(rad));
          const boxW = vw * cosA + vh * sinA;
          const boxH = vw * sinA + vh * cosA;
          const newCx = vbX - (boxW - vw) / 2;
          const newCy = vbY - (boxH - vh) / 2;
          viewBoxOut = `${newCx} ${newCy} ${boxW.toFixed(4)} ${boxH.toFixed(4)}`;
        }
      }
      if (effects.flipH || effects.flipV) {
        transforms.push(`translate(${cx} ${cy}) scale(${effects.flipH ? -1 : 1} ${effects.flipV ? -1 : 1}) translate(${-cx} ${-cy})`);
      }
      if (transforms.length) outerAttrs += ` transform="${transforms.join(" ")}"`;
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
        body = body.replace(/<(path|circle|rect|line|polyline|polygon|ellipse)\b/g, '<$1 pathLength="1"');
      }
      innerAttrs = ` class="is-m is-m-${escapeHtml(motion.type)}" style="transform-box:fill-box;transform-origin:center"`;
    }

    let wrapped = body;
    if (innerAttrs) wrapped = `<g${innerAttrs}>${wrapped}</g>`;
    if (outerAttrs) wrapped = `<g${outerAttrs}>${wrapped}</g>`;
    const attrMap = new Map();
    attrs.forEach((attr) => {
      const name = attr.slice(0, attr.indexOf("="));
      attrMap.set(name, attr);
    });
    attrMap.set("viewBox", `viewBox="${escapeHtml(viewBoxOut)}"`);
    return `<svg xmlns="${VOID_NS}" ${[...attrMap.values()].join(" ")}>${titleTag}${defsMarkup ? `<defs>${defsMarkup}</defs>` : ""}${styleMarkup}${wrapped}</svg>`;
  }

  function formatCode(icon, format, options = {}) {
    const svg = renderSVG(icon, options);
    const encoded = encodeURIComponent(svg);
    const base64 = btoa(unescape(encodeURIComponent(svg)));
    const componentName = (icon.name || "icon")
      .split(/[-_\s]+/)
      .filter(Boolean)
      .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
      .join("") || "Icon";
    if (format === "jsx") {
      return icon.jsxImport || `import { ${componentName} } from '${icon.npmPackage || icon.librarySlug}';`;
    }
    if (format === "xml") {
      return `<?xml version="1.0" encoding="UTF-8"?>\n${svg}`;
    }
    if (format === "vue") {
      return `<template>\n  ${svg}\n</template>`;
    }
    if (format === "svelte") {
      return `<script>\n  export let size = ${options.size || 24};\n</script>\n${svg.replace(/width="[^"]+"/, 'width="{size}"').replace(/height="[^"]+"/, 'height="{size}"')}`;
    }
    if (format === "angular") {
      return `<span class="iconstash-icon" aria-hidden="true">${svg}</span>`;
    }
    if (format === "html") {
      return `<img src="data:image/svg+xml,${encoded}" width="${options.size || icon.width || 24}" height="${options.size || icon.height || 24}" alt="${escapeHtml(icon.name)} icon">`;
    }
    if (format === "css") {
      return `.icon-${slugFilePart(icon.name)} {\n  width: ${options.size || 24}px;\n  height: ${options.size || 24}px;\n  background-color: currentColor;\n  mask: url("data:image/svg+xml,${encoded}") center / contain no-repeat;\n}`;
    }
    if (format === "base64") {
      return `data:image/svg+xml;base64,${base64}`;
    }
    return svg;
  }

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.setAttribute("readonly", "");
    textarea.style.position = "fixed";
    textarea.style.left = "-9999px";
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand("copy");
      return Promise.resolve();
    } catch (error) {
      return Promise.reject(error);
    } finally {
      textarea.remove();
    }
  }

  function downloadBlob(blob, filename) {
    if (window.saveAs) {
      window.saveAs(blob, filename);
      return;
    }
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  function svgToDataUrl(svg) {
    return `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
  }

  function loadScript(src) {
    return new Promise((resolve, reject) => {
      const existing = document.querySelector(`script[src="${src}"]`);
      if (existing) {
        if (typeof JSZip !== "undefined") resolve();
        else {
          existing.addEventListener("load", resolve, { once: true });
          existing.addEventListener("error", reject, { once: true });
        }
        return;
      }
      const script = document.createElement("script");
      script.src = src;
      script.defer = true;
      script.onload = resolve;
      script.onerror = () => reject(new Error(`Unable to load ${src}`));
      document.head.appendChild(script);
    });
  }

  async function ensureJSZip() {
    if (typeof JSZip !== "undefined") return JSZip;
    if (!zipLibraryPromise) zipLibraryPromise = loadScript("vendor/jszip.min.js");
    await zipLibraryPromise;
    if (typeof JSZip === "undefined") throw new Error("ZIP support could not be loaded.");
    return JSZip;
  }

  function svgToCanvas(svg, size) {
    return new Promise((resolve, reject) => {
      const canvas = document.createElement("canvas");
      const scale = window.devicePixelRatio || 1;
      canvas.width = size * scale;
      canvas.height = size * scale;
      canvas.style.width = `${size}px`;
      canvas.style.height = `${size}px`;
      const ctx = canvas.getContext("2d");
      ctx.scale(scale, scale);
      const img = new Image();
      img.crossOrigin = "anonymous";
      img.onload = () => {
        ctx.clearRect(0, 0, size, size);
        ctx.drawImage(img, 0, 0, size, size);
        resolve(canvas);
      };
      img.onerror = reject;
      img.src = svgToDataUrl(svg);
    });
  }

  async function exportPNG(icon, size = 512, options = {}) {
    const svg = renderSVG(icon, { ...options, size });
    const canvas = await svgToCanvas(svg, size);
    return new Promise((resolve) => {
      canvas.toBlob((blob) => {
        downloadBlob(blob, `${slugFilePart(icon.librarySlug)}-${slugFilePart(icon.name)}-${size}.png`);
        resolve(blob);
      }, "image/png");
    });
  }

  function exportSVG(icon, options = {}) {
    const svg = renderSVG(icon, options);
    const blob = new Blob([svg], { type: "image/svg+xml;charset=utf-8" });
    downloadBlob(blob, `${slugFilePart(icon.librarySlug)}-${slugFilePart(icon.name)}.svg`);
  }

  async function exportZIP(icons, options = {}) {
    if (!icons || !icons.length) return;
    const Zip = await ensureJSZip();
    const capped = icons.slice(0, 200);
    const zip = new Zip();
    const folder = zip.folder("IconStash");
    const sizes = options.pngSizes || [];
    for (const icon of capped) {
      const base = `${slugFilePart(icon.librarySlug)}-${slugFilePart(icon.name)}`;
      const svg = renderSVG(icon, options);
      folder.file(`${base}.svg`, svg);
      for (const size of sizes) {
        try {
          const canvas = await svgToCanvas(renderSVG(icon, { ...options, size }), size);
          const dataUrl = canvas.toDataURL("image/png");
          folder.file(`${base}-${size}.png`, dataUrl.split(",")[1], { base64: true });
        } catch (err) {
          console.error(`Failed to export PNG for ${icon.id} at ${size}px:`, err);
        }
      }
    }
    const manifest = capped.map((icon) => ({
      id: icon.id,
      name: icon.name,
      library: icon.library,
      tags: icon.tags
    }));
    folder.file("icons.json", JSON.stringify(manifest, null, 2));
    const blob = await zip.generateAsync({ type: "blob" });
    downloadBlob(blob, options.filename || "IconStash-icons.zip");
  }

  function createSprite(icons, options = {}) {
    const symbols = icons.map((icon) => {
      const body = normalizeSvgBody(icon);
      const viewBox = icon.viewBox || `0 0 ${icon.width || 24} ${icon.height || 24}`;
      return `<symbol id="${escapeHtml(icon.id)}" viewBox="${escapeHtml(viewBox)}">${body}</symbol>`;
    }).join("\n");
    return `<svg xmlns="${VOID_NS}" style="display:none" aria-hidden="true">\n${symbols}\n</svg>`;
  }

  window.IconStashIcons = {
    escapeHtml,
    slugFilePart,
    normalizeSvgBody,
    textureUsesMaterial,
    renderSVG,
    formatCode,
    copyText,
    downloadBlob,
    exportPNG,
    exportSVG,
    exportZIP,
    createSprite
  };
})();
