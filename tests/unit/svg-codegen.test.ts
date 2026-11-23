import { beforeEach, describe, expect, it } from "vitest";
import {
  createSprite,
  encodeBase64Utf8,
  formatCode,
  svgToDataUrl,
  toPascalCase,
} from "../../src/lib/svg/codegen.js";
import {
  buildEffectFilter,
  buildGradientDefs,
  buildMotionCss,
  MATERIAL_GRADIENTS,
  renderCustomizedSvg,
  resetRenderCounter,
} from "../../src/lib/svg/effects.js";
import {
  clampNumber,
  escapeXml,
  expandViewBoxForRotation,
  normalizeSvgBody,
  parseViewBox,
  sanitizeInnerSvg,
  slugFilePart,
} from "../../src/lib/svg/normalize.js";
import {
  addGradientStop,
  CODE_FORMATS,
  createDefaultCustomizationState,
  createDefaultEffectsState,
  createDefaultGradientState,
  createDefaultMotionState,
  MOTION_TYPES,
  removeGradientStop,
  ROUNDNESS_PRESETS,
  sanitizePersistedCustomState,
  textureUsesMaterial,
  type ActiveTexture,
  type IconSvgInput,
  type MotionEasing,
  type MotionType,
  type RoundnessPreset,
} from "../../src/lib/svg/types.js";

const OUTLINE_ICON: IconSvgInput = {
  id: "lucide:arrow-right",
  name: "arrow-right",
  library: "Lucide",
  librarySlug: "lucide",
  style: "outline",
  svgPath: '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
  viewBox: "0 0 24 24",
  width: 24,
  height: 24,
  strokeWidth: 2,
  npmPackage: "lucide",
};

const SOLID_ICON: IconSvgInput = {
  id: "material:star-solid",
  name: "star-solid",
  library: "Material Design Icons",
  librarySlug: "material",
  style: "solid",
  svgPath: '<path fill="#111111" d="M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z"/>',
  viewBox: "0 0 24 24",
  width: 24,
  height: 24,
  npmPackage: "@mdi/js",
};

describe("SVG normalization & viewBox utilities", () => {
  it("parses valid and fallback viewBox strings", () => {
    expect(parseViewBox("0 0 24 24")).toEqual({ x: 0, y: 0, width: 24, height: 24 });
    expect(parseViewBox("-4, -8, 32, 48")).toEqual({ x: -4, y: -8, width: 32, height: 48 });
    expect(parseViewBox(undefined, 32, 32)).toEqual({ x: 0, y: 0, width: 32, height: 32 });
    expect(parseViewBox("invalid", 16, 20)).toEqual({ x: 0, y: 0, width: 16, height: 20 });
  });

  it("wraps bare path d strings and converts hard-coded fills/strokes to currentColor", () => {
    expect(normalizeSvgBody({ svgPath: "M0 0L24 24" })).toBe(
      '<path d="M0 0L24 24"></path>',
    );

    const normalized = normalizeSvgBody({
      svgPath:
        '<path fill="#ff0000" stroke="#00ff00" d="M0 0h24"/><circle fill="none" stroke="url(#g1)" cx="12" cy="12" r="5"/>',
    });
    expect(normalized).toContain('fill="currentColor"');
    expect(normalized).toContain('stroke="currentColor"');
    expect(normalized).toContain('fill="none"');
    expect(normalized).toContain('stroke="url(#g1)"');
  });

  it("rewrites explicit stroke-width when strokeWidth option is passed", () => {
    const body = normalizeSvgBody(
      { svgPath: '<path stroke-width="2" d="M0 0h10"/>' },
      { strokeWidth: 1.5 },
    );
    expect(body).toContain('stroke-width="1.5"');
  });

  it("sanitizes unsafe scripts, foreignObject, inline event handlers, and javascript: URIs", () => {
    const dirty =
      '<svg viewBox="0 0 24 24"><script>alert(1)</script><foreignObject><div>x</div></foreignObject><path onload="evil()" onclick=\'bad()\' href="javascript:alert(1)" d="M0 0h24"/></svg>';
    const clean = sanitizeInnerSvg(dirty);
    expect(clean).not.toContain("<script");
    expect(clean).not.toContain("foreignObject");
    expect(clean).not.toContain("onload");
    expect(clean).not.toContain("onclick");
    expect(clean).not.toContain("javascript:");
    expect(clean).toContain('<path d="M0 0h24"/>');
  });

  it("escapes XML special characters and clamps numbers safely", () => {
    expect(escapeXml(`a & b <c> "d" 'e'`)).toBe(
      "a &amp; b &lt;c&gt; &quot;d&quot; &#039;e&#039;",
    );
    expect(clampNumber(NaN, 0, 10)).toBe(0);
    expect(clampNumber(999, 0, 100)).toBe(100);
    expect(clampNumber(-50, -20, 20)).toBe(-20);
    expect(slugFilePart("Arrow Right / 24px!")).toBe("arrow-right-24px");
  });
});

describe("Customization state helpers & legacy persistence migration", () => {
  it("adds up to 5 gradient stops by splitting the largest gap and keeps minimum 2", () => {
    let stops = createDefaultGradientState().stops;
    expect(stops).toHaveLength(2);

    stops = addGradientStop(stops);
    expect(stops).toHaveLength(3);
    expect(stops[1].p).toBe(50);

    stops = addGradientStop(stops);
    stops = addGradientStop(stops);
    expect(stops).toHaveLength(5);

    // Capped at 5
    const capped = addGradientStop(stops);
    expect(capped).toHaveLength(5);

    // Removes down to 2 and stops
    let reduced = removeGradientStop(stops, 1);
    reduced = removeGradientStop(reduced, 1);
    reduced = removeGradientStop(reduced, 1);
    expect(reduced).toHaveLength(2);
    expect(removeGradientStop(reduced, 0)).toHaveLength(2);
  });

  it("migrates legacy persisted state safely (e.g. unknown texture 'fabric' and capitalized roundness)", () => {
    const migrated = sanitizePersistedCustomState({
      gradient: { on: true, projection: "radial", stops: [{ c: "#fff", p: 0 }] },
      effects: { texture: "fabric", roundness: "Sharp" },
      motion: { on: true, type: "invalid", easing: "unknown" },
    });

    expect(migrated.gradient.stops).toHaveLength(2);
    expect(migrated.effects.texture).toBe("none");
    expect(migrated.effects.roundness).toBe("sharp");
    expect(migrated.motion.type).toBe("draw");
    expect(migrated.motion.easing).toBe("inout");
  });
});

describe("Gradients, effects, textures, transforms & animations", () => {
  beforeEach(() => {
    resetRenderCounter();
  });

  it("renders multi-stop linear and radial gradients and binds currentColor to url(#id)", () => {
    const linearGrad = {
      ...createDefaultGradientState(),
      on: true,
      projection: "linear" as const,
      angle: 90,
      stops: [
        { c: "#C1DD2D", p: 0 },
        { c: "#00C3FF", p: 50 },
        { c: "#2563eb", p: 100 },
      ],
    };

    const linearSvg = renderCustomizedSvg(OUTLINE_ICON, {
      uid: "t1",
      size: 128,
      gradient: linearGrad,
    });
    expect(linearSvg).toContain('<linearGradient id="t1-grad" x1="0.0%" y1="50.0%" x2="100.0%" y2="50.0%">');
    expect(linearSvg).toContain('<stop offset="0%" stop-color="#C1DD2D"/>');
    expect(linearSvg).toContain('<stop offset="50%" stop-color="#00C3FF"/>');
    expect(linearSvg).toContain('<stop offset="100%" stop-color="#2563eb"/>');
    expect(linearSvg).toContain('stroke="url(#t1-grad)"');

    const radialGrad = {
      ...createDefaultGradientState(),
      on: true,
      projection: "radial" as const,
      cx: 40,
      cy: 60,
      r: 85,
    };
    const radialDef = buildGradientDefs(radialGrad, "rad1");
    expect(radialDef).toContain('<radialGradient id="rad1" cx="40%" cy="60%" r="85%">');
  });

  it("expands viewBox on rotation so rotated corners never clip and applies flip transforms", () => {
    const expanded45 = expandViewBoxForRotation({ x: 0, y: 0, width: 24, height: 24 }, 45);
    const expectedSide = 24 * Math.SQRT2;
    expect(expanded45.viewBox).toContain(expectedSide.toFixed(4));

    const svg = renderCustomizedSvg(OUTLINE_ICON, {
      uid: "tr1",
      effects: {
        ...createDefaultEffectsState(),
        rotation: 45,
        flipH: true,
        flipV: true,
      },
    });
    expect(svg).toContain(`viewBox="${expanded45.viewBox}"`);
    expect(svg).toContain('transform="rotate(45 12 12) translate(12 12) scale(-1 -1) translate(-12 -12)"');
  });

  it("chains blur, drop shadow (with custom color), and noise grain filters in order", () => {
    const filter = buildEffectFilter(
      {
        blur: 1.2,
        shadowOn: true,
        shadowOpacity: 60,
        shadowBlur: 4,
        shadowX: 3,
        shadowY: 6,
        shadowColor: "#1e293b",
        noise: 35,
      },
      "fx1",
    );

    expect(filter).toContain('<filter id="fx1" x="-45%" y="-45%" width="190%" height="190%">');
    expect(filter).toContain('<feGaussianBlur in="SourceGraphic" stdDeviation="1.2" result="isb"/>');
    expect(filter).toContain(
      '<feDropShadow in="isb" dx="3" dy="6" stdDeviation="4" flood-color="#1e293b" flood-opacity="0.60" result="iss"/>',
    );
    expect(filter).toContain('<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" result="isn"/>');
    expect(filter).toContain('0.35 0" result="isna"/>');
    expect(filter).toContain('<feComposite in="isna" in2="iss" operator="in" result="isnc"/>');
  });

  it("supports all 5 surface textures and enforces Wood/Metal color-lock behavior", () => {
    const allTextures: ActiveTexture[] = ["paper", "concrete", "marble", "wood", "metal"];

    expect(textureUsesMaterial("wood")).toBe(true);
    expect(textureUsesMaterial("metal")).toBe(true);
    expect(textureUsesMaterial("paper")).toBe(false);
    expect(textureUsesMaterial("concrete")).toBe(false);
    expect(textureUsesMaterial("marble")).toBe(false);
    expect(MATERIAL_GRADIENTS.wood.stops).toHaveLength(24);
    expect(MATERIAL_GRADIENTS.metal.stops).toHaveLength(15);

    const userGradient = { ...createDefaultGradientState(), on: true };

    for (const texture of allTextures) {
      const svg = renderCustomizedSvg(SOLID_ICON, {
        uid: `tex-${texture}`,
        color: "#ff00aa",
        gradient: userGradient,
        effects: {
          ...createDefaultEffectsState(),
          texture,
          textureOpacity: 50,
        },
      });

      expect(svg).toContain(`filter="url(#tex-${texture}-fx)"`);
      expect(svg).toContain(`<filter id="tex-${texture}-fx"`);

      if (texture === "wood" || texture === "metal") {
        // Real material locks color and ignores user gradient
        expect(svg).toContain(`id="tex-${texture}-mat"`);
        expect(svg).toContain(`fill="url(#tex-${texture}-mat)"`);
        expect(svg).not.toContain(`id="tex-${texture}-grad"`);
        expect(svg).not.toContain("#ff00aa");
        expect(svg).toContain("color:#8A8A8A");
      } else {
        // Surface finish preserves user color / gradient
        expect(svg).toContain(`id="tex-${texture}-grad"`);
        expect(svg).toContain("color:#ff00aa");
        expect(svg).not.toContain(`id="tex-${texture}-mat"`);
      }
    }
  });

  it("applies all 4 roundness presets and strips inline stroke attributes", () => {
    const iconWithInlineStroke: IconSvgInput = {
      ...OUTLINE_ICON,
      svgPath: '<path stroke-linecap="butt" stroke-linejoin="miter" stroke-width="3" d="M5 12h14"/>',
    };

    for (const preset of Object.keys(ROUNDNESS_PRESETS) as RoundnessPreset[]) {
      const cfg = ROUNDNESS_PRESETS[preset];
      const svg = renderCustomizedSvg(iconWithInlineStroke, {
        uid: `rnd-${preset}`,
        strokeWidth: 2,
        effects: { ...createDefaultEffectsState(), roundness: preset },
      });
      expect(svg).toContain(`stroke-linecap="${cfg.cap}"`);
      expect(svg).toContain(`stroke-linejoin="${cfg.join}"`);
      expect(svg).toContain(`stroke-width="${2 * cfg.widthScale}"`);
      // Inline path stroke-width="3" stripped
      expect(svg).not.toContain('stroke-width="3"');
    }
  });

  it("renders all 5 loop animations with duration, loop, and easing presets", () => {
    expect(MOTION_TYPES).toEqual(["draw", "stroke", "bounce", "shake", "jump"]);

    const easings: MotionEasing[] = ["inout", "in", "out", "linear"];
    const expectedCssEasings: Record<MotionEasing, string> = {
      inout: "ease-in-out",
      in: "ease-in",
      out: "ease-out",
      linear: "linear",
    };

    for (const type of MOTION_TYPES) {
      const svg = renderCustomizedSvg(OUTLINE_ICON, {
        uid: `an-${type}`,
        motion: {
          ...createDefaultMotionState(),
          on: true,
          type,
          duration: 1.5,
          loop: true,
          easing: "out",
        },
      });
      expect(svg).toContain("<style>");
      expect(svg).toContain(`class="is-m is-m-${type}"`);
      expect(svg).toContain("style=\"transform-box:fill-box;transform-origin:center\"");
      expect(svg).toContain("1.5s");
      expect(svg).toContain("infinite");
      if (type === "draw") {
        expect(svg).toContain('pathLength="1"');
      } else {
        expect(svg).not.toContain('pathLength="1"');
      }
    }

    for (const easing of easings) {
      const css = buildMotionCss({
        on: true,
        type: "jump",
        duration: 2.5,
        loop: false,
        easing,
      });
      expect(css).toContain(`animation:is-jump 2.5s ${expectedCssEasings[easing]} 1`);
    }
  });

  it("supports separate export width and height dimensions", () => {
    const svg = renderCustomizedSvg(OUTLINE_ICON, {
      uid: "dim1",
      width: 64,
      height: 48,
    });
    expect(svg).toContain('width="64"');
    expect(svg).toContain('height="48"');
  });
});

describe("9-target code generator & escaping", () => {
  beforeEach(() => {
    resetRenderCounter();
  });

  it("generates all 9 code formats identically to IconStash", () => {
    expect(CODE_FORMATS).toHaveLength(9);

    const defaults = createDefaultCustomizationState();
    const opts = {
      uid: "cg1",
      size: defaults.size,
      color: defaults.color,
      strokeWidth: defaults.strokeWidth,
      gradient: defaults.gradient,
      effects: defaults.effects,
      motion: defaults.motion,
    };

    const rawSvg = formatCode(OUTLINE_ICON, "svg", opts);
    expect(rawSvg.startsWith('<svg xmlns="http://www.w3.org/2000/svg"')).toBe(true);
    expect(rawSvg.endsWith("</svg>")).toBe(true);

    const xml = formatCode(OUTLINE_ICON, "xml", opts);
    expect(xml).toBe(`<?xml version="1.0" encoding="UTF-8"?>\n${rawSvg}`);

    const jsx = formatCode(OUTLINE_ICON, "jsx", opts);
    expect(jsx).toBe("import { ArrowRight } from 'lucide';");

    const customJsxIcon: IconSvgInput = {
      ...OUTLINE_ICON,
      jsxImport: "import { ArrowRight } from 'lucide-react';",
    };
    expect(formatCode(customJsxIcon, "jsx", opts)).toBe(
      "import { ArrowRight } from 'lucide-react';",
    );

    const vue = formatCode(OUTLINE_ICON, "vue", opts);
    expect(vue).toBe(`<template>\n  ${rawSvg}\n</template>`);

    const svelte = formatCode(OUTLINE_ICON, "svelte", opts);
    expect(svelte).toContain("<script>\n  export let size = 128;\n</script>");
    expect(svelte).toContain('width="{size}"');
    expect(svelte).toContain('height="{size}"');

    const angular = formatCode(OUTLINE_ICON, "angular", opts);
    expect(angular).toBe(
      `<span class="iconstash-icon" aria-hidden="true">${rawSvg}</span>`,
    );

    const html = formatCode(OUTLINE_ICON, "html", opts);
    expect(html).toContain('<img src="data:image/svg+xml,');
    expect(html).toContain('width="128" height="128"');
    expect(html).toContain('alt="arrow-right icon">');

    const css = formatCode(OUTLINE_ICON, "css", opts);
    expect(css).toContain(".icon-arrow-right {");
    expect(css).toContain("width: 128px;");
    expect(css).toContain("height: 128px;");
    expect(css).toContain('mask: url("data:image/svg+xml,');

    const base64 = formatCode(OUTLINE_ICON, "base64", opts);
    expect(base64.startsWith("data:image/svg+xml;base64,")).toBe(true);
    const decoded = Buffer.from(
      base64.replace("data:image/svg+xml;base64,", ""),
      "base64",
    ).toString("utf8");
    expect(decoded).toBe(rawSvg);
  });

  it("properly escapes XML attributes, HTML alt text, JSX identifiers, and UTF-8 Base64", () => {
    const trickyIcon: IconSvgInput = {
      id: 'custom:3d-"cube"&<1>',
      name: '3d-"cube" & <tag>',
      librarySlug: "my'pkg",
      style: "outline",
      svgPath: '<path d="M2 2h20v20H2z"/>',
      viewBox: "0 0 24 24",
    };

    expect(toPascalCase(trickyIcon.name)).toBe("Icon3dCubeTag");

    const jsx = formatCode(trickyIcon, "jsx", { uid: "esc1" });
    expect(jsx).toBe("import { Icon3dCubeTag } from 'my\\'pkg';");

    const xml = formatCode(trickyIcon, "xml", {
      uid: "esc2",
      title: 'Cube & "Box" <1>',
    });
    expect(xml).toContain('aria-label="3d-&quot;cube&quot; &amp; &lt;tag&gt; icon"');
    expect(xml).toContain("<title>Cube &amp; &quot;Box&quot; &lt;1&gt;</title>");

    const html = formatCode(trickyIcon, "html", { uid: "esc3", size: 32 });
    expect(html).toContain('alt="3d-&quot;cube&quot; &amp; &lt;tag&gt; icon"');

    // UTF-8 Base64 round-trip with non-ASCII characters
    const utf8Svg = formatCode(trickyIcon, "svg", {
      uid: "esc4",
      title: "Icône 日本語 ★",
    });
    const b64 = encodeBase64Utf8(utf8Svg);
    expect(Buffer.from(b64, "base64").toString("utf8")).toBe(utf8Svg);
    expect(svgToDataUrl(utf8Svg)).toContain("data:image/svg+xml;charset=utf-8,");
  });

  it("builds a valid SVG <symbol> sprite sheet", () => {
    const sprite = createSprite([OUTLINE_ICON, SOLID_ICON]);
    expect(sprite).toContain('<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">');
    expect(sprite).toContain('<symbol id="lucide:arrow-right" viewBox="0 0 24 24">');
    expect(sprite).toContain('<symbol id="material:star-solid" viewBox="0 0 24 24">');
  });
});
