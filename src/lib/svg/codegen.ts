import { renderCustomizedSvg } from "./effects.js";
import { escapeXml, normalizeSvgBody, slugFilePart } from "./normalize.js";
import {
  SVG_NS,
  type CodeFormat,
  type IconSvgInput,
  type SvgRenderOptions,
} from "./types.js";

/**
 * Converts an icon name into a valid PascalCase React/JSX identifier.
 */
export function toPascalCase(name: string | null | undefined): string {
  const cleaned = String(name || "icon")
    .split(/[^a-zA-Z0-9]+/)
    .filter(Boolean)
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join("");

  if (!cleaned) return "Icon";
  return /^[0-9]/.test(cleaned) ? `Icon${cleaned}` : cleaned;
}

/**
 * Escapes a string literal for safe inclusion inside single quotes in JS/JSX.
 */
function escapeJsSingleQuoted(value: string): string {
  return value
    .replace(/\\/g, "\\\\")
    .replace(/'/g, "\\'")
    .replace(/\r/g, "\\r")
    .replace(/\n/g, "\\n");
}

/**
 * Encodes a UTF-8 string into Base64 identically in both browser and Node runtimes.
 */
export function encodeBase64Utf8(input: string): string {
  if (typeof Buffer !== "undefined") {
    return Buffer.from(input, "utf8").toString("base64");
  }
  const bytes = new TextEncoder().encode(input);
  let binary = "";
  for (let i = 0; i < bytes.length; i += 1) {
    binary += String.fromCharCode(bytes[i]);
  }
  return btoa(binary);
}

/**
 * Converts SVG markup into a UTF-8 percent-encoded Data URL.
 */
export function svgToDataUrl(svg: string): string {
  return `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
}

/**
 * Generates code for all 9 IconStash export targets:
 * `svg`, `xml`, `jsx`, `vue`, `svelte`, `angular`, `html`, `css`, `base64`.
 */
export function formatCode(
  icon: IconSvgInput,
  format: CodeFormat,
  options: SvgRenderOptions = {},
): string {
  const svg = renderCustomizedSvg(icon, options);
  const encoded = encodeURIComponent(svg);
  const base64 = encodeBase64Utf8(svg);
  const componentName = toPascalCase(icon.name);

  const exportWidth = options.width ?? options.size ?? icon.width ?? 24;
  const exportHeight = options.height ?? options.size ?? icon.height ?? 24;
  const svelteSize = options.size ?? options.width ?? 24;
  const cssWidth = options.width ?? options.size ?? 24;
  const cssHeight = options.height ?? options.size ?? 24;

  switch (format) {
    case "jsx": {
      if (icon.jsxImport) return icon.jsxImport;
      const pkg = escapeJsSingleQuoted(
        icon.npmPackage || icon.librarySlug || "iconstash",
      );
      return `import { ${componentName} } from '${pkg}';`;
    }
    case "xml":
      return `<?xml version="1.0" encoding="UTF-8"?>\n${svg}`;
    case "vue":
      return `<template>\n  ${svg}\n</template>`;
    case "svelte": {
      const responsiveSvg = svg
        .replace(/width="[^"]+"/, 'width="{size}"')
        .replace(/height="[^"]+"/, 'height="{size}"');
      return `<script>\n  export let size = ${svelteSize};\n</script>\n${responsiveSvg}`;
    }
    case "angular":
      return `<span class="iconstash-icon" aria-hidden="true">${svg}</span>`;
    case "html":
      return `<img src="data:image/svg+xml,${encoded}" width="${escapeXml(exportWidth)}" height="${escapeXml(exportHeight)}" alt="${escapeXml(icon.name)} icon">`;
    case "css":
      return `.icon-${slugFilePart(icon.name)} {\n  width: ${cssWidth}px;\n  height: ${cssHeight}px;\n  background-color: currentColor;\n  mask: url("data:image/svg+xml,${encoded}") center / contain no-repeat;\n}`;
    case "base64":
      return `data:image/svg+xml;base64,${base64}`;
    case "svg":
    default:
      return svg;
  }
}

/**
 * Generates an SVG `<symbol>` sprite sheet for a list of icons.
 */
export function createSprite(icons: readonly IconSvgInput[]): string {
  const symbols = icons
    .map((icon) => {
      const body = normalizeSvgBody(icon);
      const viewBox =
        icon.viewBox || `0 0 ${icon.width || 24} ${icon.height || 24}`;
      return `<symbol id="${escapeXml(icon.id)}" viewBox="${escapeXml(viewBox)}">${body}</symbol>`;
    })
    .join("\n");
  return `<svg xmlns="${SVG_NS}" style="display:none" aria-hidden="true">\n${symbols}\n</svg>`;
}
