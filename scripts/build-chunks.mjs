#!/usr/bin/env node
/**
 * IconStash v2 — Build Compact Sharded Per-Library Chunks
 *
 * Reads all 28 master data/*.json files + data/index.json (+ api/v1/libraries.json for licenses),
 * normalizes SVG inner markup at build time, and emits:
 *   - public/chunks/v1/{library}.json           (libraries <= 8,000 icons)
 *   - public/chunks/v1/{library}-{part}.json    (4,000-icon shards for mega-libraries > 8,000 icons)
 *   - public/chunks/v1/manifest.json            (hashes, counts, byte sizes, global index ranges)
 *
 * Matches docs/architecture.md Section 4.
 */

import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');

const DATA_DIR = path.join(ROOT, 'data');
const API_LIBRARIES_PATH = path.join(ROOT, 'api', 'v1', 'libraries.json');
const OUT_DIR = path.join(ROOT, 'public', 'chunks', 'v1');

const CHUNK_SCHEMA_VERSION = 1;
const CHUNK_SIZE_CAP = 4000;
const MEGA_LIBRARY_THRESHOLD = 8000;

const FLAG_IS_FILLED = 1 << 0;
const FLAG_HAS_VARIANTS = 1 << 1;
const FLAG_HAS_ANIMATED = 1 << 2;

const SVG_ELEMENT_RE =
  /<(path|g|circle|rect|line|polyline|polygon|ellipse|defs|use|clipPath|mask)\b/i;
const OUTER_SVG_OPEN_RE = /^\s*<svg\b[^>]*>/i;
const OUTER_SVG_CLOSE_RE = /<\/svg>\s*$/i;
const FILL_STROKE_DOUBLE_RE =
  /\s(fill|stroke)="(?!none\b|transparent\b|url\(|freeze\b|remove\b|currentColor\b)[^"]*"/gi;
const FILL_STROKE_SINGLE_RE =
  /\s(fill|stroke)='(?!none\b|transparent\b|url\(|freeze\b|remove\b|currentColor\b)[^']*'/gi;
const STROKE_WIDTH_DOUBLE_RE = /\sstroke-width="[^"]*"/gi;
const STROKE_WIDTH_SINGLE_RE = /\sstroke-width='[^']*'/gi;
const ANIMATED_ELEMENT_RE = /<(animate|animateTransform|animateMotion|set)\b/i;

function escapeAttr(value) {
  return String(value ?? '')
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

/**
 * Build-time SVG normalization (eliminates runtime regex surgery in icons.js):
 * - Strips outer <svg> wrapper if present
 * - Wraps bare path data in <path d="..."/>
 * - Normalizes non-preserved fill/stroke attributes to currentColor
 * - Strips redundant inline stroke-width on outline/stroke icons so CSS vars apply cleanly
 */
function normalizeSvgBody(rawSvg, strokeWidth) {
  let body = String(rawSvg ?? '').trim();
  if (OUTER_SVG_OPEN_RE.test(body) && OUTER_SVG_CLOSE_RE.test(body)) {
    body = body.replace(OUTER_SVG_OPEN_RE, '').replace(OUTER_SVG_CLOSE_RE, '').trim();
  }
  if (!SVG_ELEMENT_RE.test(body)) {
    body = `<path d="${escapeAttr(body)}"/>`;
  }
  body = body
    .replace(FILL_STROKE_DOUBLE_RE, (_m, attr) => ` ${attr}="currentColor"`)
    .replace(FILL_STROKE_SINGLE_RE, (_m, attr) => ` ${attr}="currentColor"`);

  if (strokeWidth > 0) {
    body = body
      .replace(STROKE_WIDTH_DOUBLE_RE, '')
      .replace(STROKE_WIDTH_SINGLE_RE, '');
  }
  return body;
}

function isFilledIcon(icon, normalizedSvg) {
  if (icon.style === 'fill' || icon.style === 'solid' || icon.strokeWidth === 0) {
    return true;
  }
  return (
    normalizedSvg.includes('fill="currentColor"') &&
    !normalizedSvg.includes('stroke="currentColor"')
  );
}

function mostFrequent(countsMap, fallback) {
  let bestKey = fallback;
  let bestCount = -1;
  for (const [key, count] of countsMap.entries()) {
    if (count > bestCount) {
      bestCount = count;
      bestKey = key;
    }
  }
  return bestKey;
}

function loadLicenseMap() {
  const map = new Map();
  if (!fs.existsSync(API_LIBRARIES_PATH)) return map;
  try {
    const apiLibs = JSON.parse(fs.readFileSync(API_LIBRARIES_PATH, 'utf8'));
    for (const lib of apiLibs) {
      map.set(lib.slug, {
        license: lib.license || 'MIT',
        attributionRequired: Boolean(lib.attributionRequired),
      });
    }
  } catch {
    // Fallback to defaults if api/v1/libraries.json is unavailable
  }
  return map;
}

function main() {
  const t0 = performance.now();
  const indexData = JSON.parse(fs.readFileSync(path.join(DATA_DIR, 'index.json'), 'utf8'));
  const licenseMap = loadLicenseMap();

  fs.mkdirSync(OUT_DIR, { recursive: true });
  // Remove stale chunk files from previous runs
  for (const file of fs.readdirSync(OUT_DIR)) {
    if (file.endsWith('.json')) {
      fs.unlinkSync(path.join(OUT_DIR, file));
    }
  }

  const manifestLibraries = [];
  const overallHasher = crypto.createHash('sha256');
  let globalIndex = 0;
  let totalShardFiles = 0;
  let totalShardBytes = 0;
  let totalIdOverrides = 0;

  for (let libId = 0; libId < indexData.libraries.length; libId++) {
    const libMeta = indexData.libraries[libId];
    const slug = libMeta.slug;
    const rawIcons = JSON.parse(
      fs.readFileSync(path.join(DATA_DIR, `${slug}.json`), 'utf8'),
    );

    const licInfo = licenseMap.get(slug) || {
      license: 'MIT',
      attributionRequired: false,
    };

    // Determine library-level defaults (most frequent viewBox and strokeWidth)
    const vbFreq = new Map();
    const swFreq = new Map();
    for (const icon of rawIcons) {
      const vb = icon.viewBox || '0 0 24 24';
      const sw = typeof icon.strokeWidth === 'number' ? icon.strokeWidth : 2;
      vbFreq.set(vb, (vbFreq.get(vb) || 0) + 1);
      swFreq.set(sw, (swFreq.get(sw) || 0) + 1);
    }
    const defaultViewBox = mostFrequent(vbFreq, '0 0 24 24');
    const defaultStrokeWidth = mostFrequent(swFreq, 2);

    const libStartIndex = globalIndex;
    const isMega = rawIcons.length > MEGA_LIBRARY_THRESHOLD;
    const totalParts = isMega ? Math.ceil(rawIcons.length / CHUNK_SIZE_CAP) : 1;
    const shards = [];

    for (let part = 0; part < totalParts; part++) {
      const sliceStart = part * CHUNK_SIZE_CAP;
      const sliceEnd = isMega
        ? Math.min(sliceStart + CHUNK_SIZE_CAP, rawIcons.length)
        : rawIcons.length;
      const shardStartIndex = libStartIndex + sliceStart;
      const shardCount = sliceEnd - sliceStart;

      // Chunk-local viewBox table with defaultViewBox at index 0
      const viewBoxes = [defaultViewBox];
      const viewBoxToIdx = new Map([[defaultViewBox, 0]]);
      const tuples = new Array(shardCount);
      let idOverrides = null;

      for (let i = 0; i < shardCount; i++) {
        const icon = rawIcons[sliceStart + i];
        const sw = typeof icon.strokeWidth === 'number' ? icon.strokeWidth : defaultStrokeWidth;
        const normalizedSvg = normalizeSvgBody(icon.svgPath, sw);
        const vb = icon.viewBox || defaultViewBox;

        let vbIdx = viewBoxToIdx.get(vb);
        if (vbIdx === undefined) {
          vbIdx = viewBoxes.length;
          viewBoxes.push(vb);
          viewBoxToIdx.set(vb, vbIdx);
        }

        let flags = 0;
        if (isFilledIcon(icon, normalizedSvg)) flags |= FLAG_IS_FILLED;
        if (icon.hasVariants) flags |= FLAG_HAS_VARIANTS;
        if (ANIMATED_ELEMENT_RE.test(normalizedSvg)) flags |= FLAG_HAS_ANIMATED;

        const name = icon.name;
        const expectedId = `${slug}-${name}`;
        if (icon.id && icon.id !== expectedId) {
          if (!idOverrides) idOverrides = {};
          idOverrides[String(i)] = icon.id;
          totalIdOverrides++;
        }

        tuples[i] = [name, normalizedSvg, vbIdx, sw, flags];
      }

      const chunkObj = {
        schemaVersion: CHUNK_SCHEMA_VERSION,
        librarySlug: slug,
        libraryName: libMeta.name,
        libraryId: libId,
        version: libMeta.version || '1.0.0',
        license: licInfo.license,
        attributionRequired: licInfo.attributionRequired,
        npmPackage: libMeta.npmPackage || '',
        docsUrlBase: libMeta.docsUrl || '',
        defaultViewBox,
        defaultStrokeWidth,
        part,
        totalParts,
        startIndex: shardStartIndex,
        count: shardCount,
        viewBoxes,
        icons: tuples,
      };
      if (idOverrides) {
        chunkObj.idOverrides = idOverrides;
      }

      const filename = isMega ? `${slug}-${part}.json` : `${slug}.json`;
      const filePath = path.join(OUT_DIR, filename);
      const jsonStr = JSON.stringify(chunkObj);
      const buf = Buffer.from(jsonStr, 'utf8');
      fs.writeFileSync(filePath, buf);

      const sha256 = crypto.createHash('sha256').update(buf).digest('hex').slice(0, 12);
      overallHasher.update(filename);
      overallHasher.update(sha256);

      shards.push({
        url: `/chunks/v1/${filename}`,
        start: shardStartIndex,
        count: shardCount,
        bytes: buf.byteLength,
        sha256,
      });

      totalShardFiles++;
      totalShardBytes += buf.byteLength;
    }

    const libEndIndex = libStartIndex + rawIcons.length - 1;
    manifestLibraries.push({
      id: libId,
      slug,
      name: libMeta.name,
      count: rawIcons.length,
      startIndex: libStartIndex,
      endIndex: libEndIndex,
      shards,
    });

    globalIndex += rawIcons.length;
  }

  const contentHash = overallHasher.digest('hex').slice(0, 8);
  const manifest = {
    schemaVersion: CHUNK_SCHEMA_VERSION,
    generatedAt: new Date().toISOString(),
    contentHash,
    totalIcons: globalIndex,
    chunkSizeCap: CHUNK_SIZE_CAP,
    libraries: manifestLibraries,
  };

  const manifestBuf = Buffer.from(JSON.stringify(manifest, null, 2), 'utf8');
  fs.writeFileSync(path.join(OUT_DIR, 'manifest.json'), manifestBuf);

  const elapsedMs = (performance.now() - t0).toFixed(0);
  const totalMB = (totalShardBytes / (1024 * 1024)).toFixed(2);
  console.log(
    `[build-chunks] Built ${totalShardFiles} shard files across ${manifestLibraries.length} libraries ` +
      `(${globalIndex.toLocaleString()} icons, ${totalMB} MB raw, ${totalIdOverrides} id overrides, ` +
      `hash=${contentHash}) in ${elapsedMs} ms`,
  );
}

main();
