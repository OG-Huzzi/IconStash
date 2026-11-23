import type { IconSvgInput } from "./types.js";

export interface ViewBoxRect {
  x: number;
  y: number;
  width: number;
  height: number;
}

export interface RotatedViewBoxResult {
  viewBox: string;
  rotation: number;
  cx: number;
  cy: number;
}

const SVG_SHAPE_TAG_RE =
  /<(path|g|circle|rect|line|polyline|polygon|ellipse|defs|use|clipPath|mask)\b/i;

/**
 * Escapes XML/HTML special characters matching legacy `icons.js:escapeHtml`.
 */
export function escapeXml(value: unknown): string {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

/**
 * Converts an icon name or library slug into a safe lowercase slug.
 */
export function slugFilePart(value: string | null | undefined): string {
  return (
    String(value || "icon")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "") || "icon"
  );
}

/**
 * Clamps a numeric value to `[min, max]`, returning `min` for NaN/non-finite inputs.
 */
export function clampNumber(value: unknown, min: number, max: number): number {
  const n = Number(value);
  if (Number.isNaN(n) || !Number.isFinite(n)) return min;
  return Math.min(max, Math.max(min, n));
}

/**
 * Parses an SVG `viewBox` string into numeric `{ x, y, width, height }` coordinates.
 */
export function parseViewBox(
  viewBox?: string | null,
  fallbackWidth = 24,
  fallbackHeight = 24,
): ViewBoxRect {
  const safeW =
    Number.isFinite(fallbackWidth) && fallbackWidth > 0 ? fallbackWidth : 24;
  const safeH =
    Number.isFinite(fallbackHeight) && fallbackHeight > 0 ? fallbackHeight : 24;

  if (!viewBox || typeof viewBox !== "string") {
    return { x: 0, y: 0, width: safeW, height: safeH };
  }

  const parts = viewBox
    .trim()
    .split(/[\s,]+/)
    .map(Number);

  const x = Number.isFinite(parts[0]) ? parts[0] : 0;
  const y = Number.isFinite(parts[1]) ? parts[1] : 0;
  const width =
    Number.isFinite(parts[2]) && parts[2] > 0 ? parts[2] : safeW;
  const height =
    Number.isFinite(parts[3]) && parts[3] > 0 ? parts[3] : safeH;

  return { x, y, width, height };
}

/**
 * Formats a `ViewBoxRect` into a standard `viewBox` attribute string.
 */
export function formatViewBox(rect: ViewBoxRect): string {
  return `${rect.x} ${rect.y} ${rect.width} ${rect.height}`;
}

/**
 * Computes the expanded `viewBox` bounding box for a rotated icon so rotated
 * corners never clip, matching legacy `icons.js:renderSVG` math 1:1.
 */
export function expandViewBoxForRotation(
  rect: ViewBoxRect,
  rotationDeg: number,
): RotatedViewBoxResult {
  const cx = rect.x + rect.width / 2;
  const cy = rect.y + rect.height / 2;
  const rot = clampNumber(rotationDeg, 0, 360) % 360;

  if (!rot) {
    return {
      viewBox: formatViewBox(rect),
      rotation: 0,
      cx,
      cy,
    };
  }

  const rad = (rot * Math.PI) / 180;
  const cosA = Math.abs(Math.cos(rad));
  const sinA = Math.abs(Math.sin(rad));
  const boxW = rect.width * cosA + rect.height * sinA;
  const boxH = rect.width * sinA + rect.height * cosA;
  const newX = rect.x - (boxW - rect.width) / 2;
  const newY = rect.y - (boxH - rect.height) / 2;

  return {
    viewBox: `${newX} ${newY} ${boxW.toFixed(4)} ${boxH.toFixed(4)}`,
    rotation: rot,
    cx,
    cy,
  };
}

/**
 * Strips potentially unsafe elements and event handlers from inner SVG markup
 * while keeping valid SVG vector geometry intact.
 */
export function sanitizeInnerSvg(raw: string): string {
  if (!raw) return "";
  let cleaned = raw.trim();

  // Unwrap an outer <svg ...>...</svg> container if full SVG markup was supplied.
  const outerSvgMatch = cleaned.match(/^<svg\b[^>]*>([\s\S]*)<\/svg>$/i);
  if (outerSvgMatch) {
    cleaned = outerSvgMatch[1].trim();
  }

  // Strip dangerous container elements and their contents.
  cleaned = cleaned.replace(
    /<(script|foreignObject|iframe|object|embed)\b[^>]*>[\s\S]*?<\/\1>/gi,
    "",
  );
  // Strip self-closing dangerous elements.
  cleaned = cleaned.replace(
    /<(script|foreignObject|iframe|object|embed)\b[^>]*\/?>/gi,
    "",
  );
  // Strip inline event handler attributes (e.g. onload="...", onclick='...').
  cleaned = cleaned.replace(/\s+on[a-z]+\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>]+)/gi, "");
  // Neutralize javascript: URIs in href / xlink:href attributes.
  cleaned = cleaned.replace(
    /\s+((?:xlink:)?href)\s*=\s*(?:"\s*javascript:[^"]*"|'\s*javascript:[^']*')/gi,
    "",
  );

  return cleaned;
}

/**
 * Normalizes an icon's inner SVG body:
 * - Sanitizes untrusted markup
 * - Wraps raw path `d` strings in `<path d="..."></path>`
 * - Rewrites explicit `fill` and `stroke` colors to `currentColor` (preserving
 *   `none`, `transparent`, `url(...)`, `freeze`, and `remove`)
 * - Optionally rewrites explicit `stroke-width` attributes
 */
export function normalizeSvgBody(
  icon: Pick<IconSvgInput, "svgPath" | "svgContent">,
  options: { strokeWidth?: number } = {},
): string {
  const rawBody = icon.svgPath || icon.svgContent || "";
  const sanitized = sanitizeInnerSvg(rawBody);

  let normalized = sanitized;
  if (!SVG_SHAPE_TAG_RE.test(sanitized)) {
    normalized = `<path d="${escapeXml(sanitized)}"></path>`;
  }

  normalized = normalized.replace(
    /\s(fill|stroke)="(?!none\b|transparent\b|url\(|freeze\b|remove\b)[^"]*"/gi,
    (_match, attr: string) => ` ${attr}="currentColor"`,
  );
  normalized = normalized.replace(
    /\s(fill|stroke)='(?!none\b|transparent\b|url\(|freeze\b|remove\b)[^']*'/gi,
    (_match, attr: string) => ` ${attr}="currentColor"`,
  );

  if (options.strokeWidth !== undefined && options.strokeWidth !== null) {
    if (/\sstroke-width=/i.test(normalized)) {
      const escapedWidth = escapeXml(options.strokeWidth);
      normalized = normalized
        .replace(/\sstroke-width="[^"]*"/gi, ` stroke-width="${escapedWidth}"`)
        .replace(/\sstroke-width='[^']*'/gi, ` stroke-width="${escapedWidth}"`);
    }
  }

  return normalized;
}
