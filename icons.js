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

  function hexToRgbaMix(hexColor, baseColor, opacity) {
    const parse = (h) => {
      const v = String(h).replace("#", "");
      const full = v.length === 3 ? v.split("").map((ch) => ch + ch).join("") : v;
      return [parseInt(full.slice(0, 2), 16), parseInt(full.slice(2, 4), 16), parseInt(full.slice(4, 6), 16)];
    };
    const [r1, g1, b1] = parse(hexColor);
    const [r2, g2, b2] = parse(baseColor);
    const mix = (a, b) => Math.round(a * opacity + b * (1 - opacity));
    return `rgb(${mix(r1, r2)},${mix(g1, g2)},${mix(b1, b2)})`;
  }

  function buildGradientDefs(gradient) {
    const stops = (gradient.stops || [])
      .map((stop) => `<stop offset="${clampNumber(stop.p, 0, 100)}%" stop-color="${escapeHtml(stop.c)}"/>`)
      .join("");
    let el;
    if (gradient.projection === "radial") {
      el = `<radialGradient id="is-grad" cx="${clampNumber(gradient.cx ?? 50, 0, 100)}%" cy="${clampNumber(gradient.cy ?? 50, 0, 100)}%" r="${clampNumber(gradient.r ?? 75, 5, 150)}%">${stops}</radialGradient>`;
    } else {
      const rad = ((Number(gradient.angle ?? 90) - 90) * Math.PI) / 180;
      const x1 = ((0.5 - Math.cos(rad) / 2) * 100).toFixed(1);
      const y1 = ((0.5 - Math.sin(rad) / 2) * 100).toFixed(1);
      const x2 = ((0.5 + Math.cos(rad) / 2) * 100).toFixed(1);
      const y2 = ((0.5 + Math.sin(rad) / 2) * 100).toFixed(1);
      el = `<linearGradient id="is-grad" x1="${x1}%" y1="${y1}%" x2="${x2}%" y2="${y2}%">${stops}</linearGradient>`;
    }
    return el;
  }

  const ROUNDNESS_PRESETS = {
    soft: { cap: "round", join: "round", widthScale: 0.75 },
    round: { cap: "round", join: "round", widthScale: 1 },
    medium: { cap: "round", join: "bevel", widthScale: 1 },
    sharp: { cap: "butt", join: "miter", widthScale: 1 }
  };

  const TEXTURE_PRESETS = {
    paper: { freq: "0.9 0.9", octaves: 2 },
    fabric: { freq: "0.18 0.18", octaves: 5 },
    concrete: { freq: "0.08 0.08", octaves: 3 },
    wood: { freq: "0.32 0.015", octaves: 4, tint: "wood" },
    metal: { freq: "0.55 0.008", octaves: 2, tint: "metal" }
  };

  const MATERIAL_GRADIENTS = {
    wood: { x1: 0, y1: 0, x2: 0, y2: 1, stops: [["#A97B4B", 0], ["#7A4E28", 30], ["#8B5E34", 55], ["#5F3D1E", 100]] },
    metal: { x1: 0, y1: 0, x2: 1, y2: 0, stops: [["#FDFEFE", 0], ["#C3CCD6", 28], ["#EDF1F5", 50], ["#8E99A6", 72], ["#D7DEE6", 100]] }
  };

  function textureTintMatrix(tint, op) {
    const alpha = `${(0.2126 * op).toFixed(3)} ${(0.7152 * op).toFixed(3)} ${(0.0722 * op).toFixed(3)} 0 0`;
    if (tint === "wood") {
      return `values="0.42 0.42 0.42 0 0.05 0.24 0.24 0.24 0 0.02 0.10 0.10 0.10 0 0 ${alpha}"`;
    }
    if (tint === "metal") {
      return `values="0.90 0.90 0.90 0 0 0.93 0.93 0.93 0 0 1 1 1 0 0 ${alpha}"`;
    }
    return `values="0.33 0.33 0.33 0 0 0.33 0.33 0.33 0 0 0.33 0.33 0.33 0 0 ${alpha}"`;
  }

  function buildEffectFilter(effects) {
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
    if (effects.texture && effects.texture !== "none" && TEXTURE_PRESETS[effects.texture]) {
      const tex = TEXTURE_PRESETS[effects.texture];
      const op = clampNumber(effects.textureOpacity ?? 30, 0, 100) / 100;
      prims.push(`<feTurbulence type="fractalNoise" baseFrequency="${tex.freq}" numOctaves="${tex.octaves}" stitchTiles="stitch" result="ist"/>`);
      prims.push(`<feColorMatrix in="ist" type="matrix" ${textureTintMatrix(tex.tint, op)} result="istg"/>`);
      prims.push(`<feComposite in="istg" in2="${last}" operator="in" result="istc"/>`);
      prims.push(`<feMerge result="istm"><feMergeNode in="${last}"/><feMergeNode in="istc"/></feMerge>`);
      last = "istm";
    }
    if (!prims.length) return "";
    return `<filter id="is-fx" x="-45%" y="-45%" width="190%" height="190%">${prims.join("")}</filter>`;
  }

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
    const viewBox = icon.viewBox || `0 0 ${icon.width || 24} ${icon.height || 24}`;
    const size = options.size || "100%";
    const strokeWidth = options.strokeWidth ?? icon.strokeWidth ?? 2;
    const color = options.color || "currentColor";
    const fillStyles = new Set(["fill", "solid", "bold"]);
    const fill = options.fill || (fillStyles.has(icon.style) ? "currentColor" : "none");
    const roundPreset = options.effects && ROUNDNESS_PRESETS[options.effects.roundness] ? ROUNDNESS_PRESETS[options.effects.roundness] : null;
    const material = options.effects && options.effects.texture && MATERIAL_GRADIENTS[options.effects.texture] ? MATERIAL_GRADIENTS[options.effects.texture] : null;
    const gradient = options.gradient;
    const effects = options.effects;
    const texOpacity = clampNumber(effects?.textureOpacity ?? 100, 0, 100) / 100;
    const paintAttr = material ? "url(#is-mat)" : (gradient && gradient.on && Array.isArray(gradient.stops) && gradient.stops.length >= 2 ? "url(#is-grad)" : null);
    const hasCustomStroke = Object.prototype.hasOwnProperty.call(options, "strokeWidth");
    const stroke = options.stroke || (fill === "none" || hasCustomStroke ? (paintAttr || "currentColor") : "none");
    const fillPaint = material ? "url(#is-mat)" : (paintAttr && fill === "currentColor" ? paintAttr : (fillStyles.has(icon.style) && !paintAttr ? "currentColor" : fill));
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
      const matStops = material.stops.map(([c, p]) => {
        if (texOpacity >= 1) return [c, p];
        const blended = hexToRgbaMix(c, color === "currentColor" ? "#F2F2F2" : color, texOpacity);
        return [blended, p];
      });
      defsMarkup += `<linearGradient id="is-mat" x1="${material.x1}" y1="${material.y1}" x2="${material.x2}" y2="${material.y2}">${matStops.map((s) => `<stop offset="${s[1]}%" stop-color="${s[0]}"/>`).join("")}</linearGradient>`;
      body = body.replace(/fill="currentColor"/g, 'fill="url(#is-mat)"');
      body = body.replace(/stroke="currentColor"/g, 'stroke="url(#is-mat)"');
    } else if (gradient && gradient.on && Array.isArray(gradient.stops) && gradient.stops.length >= 2) {
      defsMarkup += buildGradientDefs(gradient);
      body = body.replace(/fill="currentColor"/g, 'fill="url(#is-grad)"');
      body = body.replace(/stroke="currentColor"/g, 'stroke="url(#is-grad)"');
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
      const filterMarkup = buildEffectFilter(effects);
      if (filterMarkup) {
        defsMarkup += filterMarkup;
        outerAttrs += ` filter="url(#is-fx)"`;
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
