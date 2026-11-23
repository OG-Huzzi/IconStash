#!/usr/bin/env node
/**
 * IconStash v2 — Compile Compact Typed-Array Binary Search Index
 *
 * Compiles all 134,701 icons across 28 master data/*.json files into:
 *   - public/index/v1/search.bin        (Little-Endian binary index with 64-byte header)
 *   - public/index/v1/search-meta.json  (Lookup tables for libraries, categories, styles, viewBoxes, counts)
 *
 * Matches docs/architecture.md Section 5.
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
const OUT_DIR = path.join(ROOT, 'public', 'index', 'v1');

const SCHEMA_VERSION = 1;
/** Little-endian ASCII "ICS2" */
const SEARCH_INDEX_MAGIC = 0x32534349;
const SEARCH_INDEX_VERSION = 1;
const HEADER_BYTES = 64;

const STROKE_WIDTH_TABLE = [0, 1, 1.5, 2];
const WEIGHT_TAG = 1;
const WEIGHT_EXACT_NAME = 4;

const TOKEN_SPLIT_RE = /[^a-z0-9]+/;

function align4(offset) {
  return (offset + 3) & ~3;
}

function packIconMeta({ libId, catId, styleId, strokeIdx, isFilled, hasVariants, rankScore }) {
  return (
    ((libId & 0x1f) |
      ((catId & 0x0f) << 5) |
      ((styleId & 0x07) << 9) |
      ((strokeIdx & 0x03) << 12) |
      ((isFilled ? 1 : 0) << 14) |
      ((hasVariants ? 1 : 0) << 15) |
      ((Math.max(0, Math.min(0xffff, rankScore | 0)) & 0xffff) << 16)) >>>
    0
  );
}

function packPosting(iconIndex, matchWeight) {
  return ((iconIndex & 0x00ffffff) | ((matchWeight & 0x0f) << 24)) >>> 0;
}

function strokeWidthToIdx(sw) {
  const idx = STROKE_WIDTH_TABLE.indexOf(sw);
  return idx >= 0 ? idx : 3; // default to 2 (index 3)
}

function isFilledIcon(icon) {
  if (icon.style === 'fill' || icon.style === 'solid' || icon.strokeWidth === 0) {
    return true;
  }
  const svg = String(icon.svgPath || '');
  return svg.includes('fill="currentColor"') && !svg.includes('stroke="currentColor"');
}

function computeRankScore(tier, popularity) {
  const safeTier = Math.max(1, Math.min(4, Number(tier) || 4));
  const tierWeight = (5 - safeTier) * 12000; // Tier 1: 48000, Tier 2: 36000, Tier 3: 24000, Tier 4: 12000
  const pop = Math.max(0, Math.min(10000, Number(popularity) || 0));
  const popWeight = Math.round((pop / 10000) * 15000);
  return Math.min(0xffff, tierWeight + popWeight);
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
    // fallback
  }
  return map;
}

function tokenize(str) {
  if (!str) return [];
  const parts = String(str).toLowerCase().split(TOKEN_SPLIT_RE);
  const out = [];
  for (let i = 0; i < parts.length; i++) {
    if (parts[i].length > 0) out.push(parts[i]);
  }
  return out;
}

function main() {
  const t0 = performance.now();
  const indexData = JSON.parse(fs.readFileSync(path.join(DATA_DIR, 'index.json'), 'utf8'));
  const licenseMap = loadLicenseMap();

  fs.mkdirSync(OUT_DIR, { recursive: true });

  // Pass 1: Discover canonical taxonomy tables (categories, subCategories, styles, viewBoxes) and total count
  const categorySet = new Set();
  const subCategorySet = new Set();
  const styleSet = new Set();
  const viewBoxCounts = new Map();
  let totalIcons = 0;

  for (const libMeta of indexData.libraries) {
    const rawIcons = JSON.parse(
      fs.readFileSync(path.join(DATA_DIR, `${libMeta.slug}.json`), 'utf8'),
    );
    totalIcons += rawIcons.length;
    for (let i = 0; i < rawIcons.length; i++) {
      const icon = rawIcons[i];
      if (icon.category) categorySet.add(icon.category);
      if (icon.subCategory) subCategorySet.add(icon.subCategory);
      if (icon.style) styleSet.add(icon.style);
      const vb = icon.viewBox || '0 0 24 24';
      viewBoxCounts.set(vb, (viewBoxCounts.get(vb) || 0) + 1);
    }
  }

  const categories = [...categorySet].sort();
  const subCategories = [...subCategorySet].sort();
  const styles = [...styleSet].sort();
  const viewBoxes = [...viewBoxCounts.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .map(([vb]) => vb);

  const catToId = new Map(categories.map((c, i) => [c, i]));
  const styleToId = new Map(styles.map((s, i) => [s, i]));

  // Pass 2: Build typed arrays, flat UTF-8 name buffer, and inverted postings map
  const metaPacked = new Uint32Array(totalIcons);
  const nameOffsets = new Uint32Array(totalIcons + 1);
  const nameChunks = [];
  let nameByteOffset = 0;

  const postingsMap = new Map(); // token -> number[] (packed postings, strictly ascending iconIndex)
  const byLibrary = new Array(indexData.libraries.length).fill(0);
  const byCategory = new Array(categories.length).fill(0);
  const byStyle = new Array(styles.length).fill(0);
  const metaLibraries = [];

  let iconIndex = 0;
  const iconTokenWeights = new Map();

  for (let libId = 0; libId < indexData.libraries.length; libId++) {
    const libMeta = indexData.libraries[libId];
    const slug = libMeta.slug;
    const licInfo = licenseMap.get(slug) || {
      license: 'MIT',
      attributionRequired: false,
    };

    const rawIcons = JSON.parse(
      fs.readFileSync(path.join(DATA_DIR, `${slug}.json`), 'utf8'),
    );

    const startIndex = iconIndex;
    byLibrary[libId] = rawIcons.length;

    for (let i = 0; i < rawIcons.length; i++) {
      const icon = rawIcons[i];
      const catId = catToId.get(icon.category) ?? 0;
      const styleId = styleToId.get(icon.style) ?? 0;
      const strokeIdx = strokeWidthToIdx(
        typeof icon.strokeWidth === 'number' ? icon.strokeWidth : 2,
      );
      const isFilled = isFilledIcon(icon);
      const hasVariants = Boolean(icon.hasVariants);
      const rankScore = computeRankScore(libMeta.tier, icon.popularity);

      metaPacked[iconIndex] = packIconMeta({
        libId,
        catId,
        styleId,
        strokeIdx,
        isFilled,
        hasVariants,
        rankScore,
      });

      byCategory[catId]++;
      byStyle[styleId]++;

      // Flat lowercase UTF-8 name table
      const lowerName = String(icon.name || '').toLowerCase();
      const nameBytes = Buffer.from(lowerName, 'utf8');
      nameOffsets[iconIndex] = nameByteOffset;
      nameChunks.push(nameBytes);
      nameByteOffset += nameBytes.byteLength;

      // Tokenize name (weight 4) and tags (weight 1), deduplicating per icon with max weight
      iconTokenWeights.clear();
      const nameTokens = tokenize(lowerName);
      for (let t = 0; t < nameTokens.length; t++) {
        iconTokenWeights.set(nameTokens[t], WEIGHT_EXACT_NAME);
      }

      if (Array.isArray(icon.tags)) {
        for (let t = 0; t < icon.tags.length; t++) {
          const tagTokens = tokenize(icon.tags[t]);
          for (let k = 0; k < tagTokens.length; k++) {
            const tok = tagTokens[k];
            const prev = iconTokenWeights.get(tok);
            if (prev === undefined || WEIGHT_TAG > prev) {
              iconTokenWeights.set(tok, WEIGHT_TAG);
            }
          }
        }
      }

      for (const [tok, weight] of iconTokenWeights.entries()) {
        let list = postingsMap.get(tok);
        if (!list) {
          list = [];
          postingsMap.set(tok, list);
        }
        list.push(packPosting(iconIndex, weight));
      }

      iconIndex++;
    }

    metaLibraries.push({
      id: libId,
      slug,
      name: libMeta.name,
      count: rawIcons.length,
      startIndex,
      endIndex: iconIndex - 1,
      tier: libMeta.tier || 4,
      color: libMeta.color || '#64748b',
      version: libMeta.version || '1.0.0',
      license: licInfo.license,
      attributionRequired: licInfo.attributionRequired,
      npmPackage: libMeta.npmPackage || '',
      docsUrl: libMeta.docsUrl || '',
    });
  }
  nameOffsets[totalIcons] = nameByteOffset;
  const nameBuf = Buffer.concat(nameChunks, nameByteOffset);

  // Sort vocabulary by UTF-8 byte order (matches compareBytes in src/lib/protocol/binary.ts)
  const vocabEntries = new Array(postingsMap.size);
  let vIdx = 0;
  let totalPostings = 0;
  for (const [token, postings] of postingsMap.entries()) {
    vocabEntries[vIdx++] = {
      buf: Buffer.from(token, 'utf8'),
      postings,
    };
    totalPostings += postings.length;
  }
  vocabEntries.sort((a, b) => Buffer.compare(a.buf, b.buf));

  const vocabCount = vocabEntries.length;
  const vocabOffsets = new Uint32Array(vocabCount + 1);
  const vocabBufChunks = new Array(vocabCount);
  const postingsOffsets = new Uint32Array(vocabCount + 1);
  const postingsIds = new Uint32Array(totalPostings);

  let vocabByteOffset = 0;
  let postingCursor = 0;
  for (let i = 0; i < vocabCount; i++) {
    const entry = vocabEntries[i];
    vocabOffsets[i] = vocabByteOffset;
    vocabBufChunks[i] = entry.buf;
    vocabByteOffset += entry.buf.byteLength;

    postingsOffsets[i] = postingCursor;
    const list = entry.postings;
    for (let p = 0; p < list.length; p++) {
      postingsIds[postingCursor++] = list[p];
    }
  }
  vocabOffsets[vocabCount] = vocabByteOffset;
  postingsOffsets[vocabCount] = postingCursor;
  const vocabBuf = Buffer.concat(vocabBufChunks, vocabByteOffset);

  // Compute 4-byte-aligned binary layout
  const offMetaPacked = HEADER_BYTES;
  const offNameOffsets = align4(offMetaPacked + totalIcons * 4);
  const offNameBuf = align4(offNameOffsets + (totalIcons + 1) * 4);
  const offVocabOffsets = align4(offNameBuf + nameBuf.byteLength);
  const offVocabBuf = align4(offVocabOffsets + (vocabCount + 1) * 4);
  const offPostingsOffsets = align4(offVocabBuf + vocabBuf.byteLength);
  const offPostingsIds = align4(offPostingsOffsets + (vocabCount + 1) * 4);
  const totalBytes = align4(offPostingsIds + totalPostings * 4);

  const outBuf = Buffer.alloc(totalBytes);
  // 64-byte Little-Endian Header
  outBuf.writeUInt32LE(SEARCH_INDEX_MAGIC, 0);
  outBuf.writeUInt16LE(SEARCH_INDEX_VERSION, 4);
  outBuf.writeUInt16LE(0, 6); // flags
  outBuf.writeUInt32LE(totalIcons, 8);
  outBuf.writeUInt32LE(vocabCount, 12);
  outBuf.writeUInt32LE(totalPostings, 16);
  outBuf.writeUInt32LE(offMetaPacked, 20);
  outBuf.writeUInt32LE(offNameOffsets, 24);
  outBuf.writeUInt32LE(offNameBuf, 28);
  outBuf.writeUInt32LE(offVocabOffsets, 32);
  outBuf.writeUInt32LE(offVocabBuf, 36);
  outBuf.writeUInt32LE(offPostingsOffsets, 40);
  outBuf.writeUInt32LE(offPostingsIds, 44);

  // Copy sections into output buffer
  Buffer.from(metaPacked.buffer, metaPacked.byteOffset, metaPacked.byteLength).copy(
    outBuf,
    offMetaPacked,
  );
  Buffer.from(nameOffsets.buffer, nameOffsets.byteOffset, nameOffsets.byteLength).copy(
    outBuf,
    offNameOffsets,
  );
  nameBuf.copy(outBuf, offNameBuf);
  Buffer.from(vocabOffsets.buffer, vocabOffsets.byteOffset, vocabOffsets.byteLength).copy(
    outBuf,
    offVocabOffsets,
  );
  vocabBuf.copy(outBuf, offVocabBuf);
  Buffer.from(
    postingsOffsets.buffer,
    postingsOffsets.byteOffset,
    postingsOffsets.byteLength,
  ).copy(outBuf, offPostingsOffsets);
  Buffer.from(postingsIds.buffer, postingsIds.byteOffset, postingsIds.byteLength).copy(
    outBuf,
    offPostingsIds,
  );

  const binPath = path.join(OUT_DIR, 'search.bin');
  fs.writeFileSync(binPath, outBuf);

  const contentHash = crypto.createHash('sha256').update(outBuf).digest('hex').slice(0, 8);
  const searchMeta = {
    schemaVersion: SCHEMA_VERSION,
    generatedAt: new Date().toISOString(),
    contentHash,
    totalIcons,
    vocabCount,
    postingsCount: totalPostings,
    indexBytes: totalBytes,
    libraries: metaLibraries,
    categories,
    subCategories,
    styles,
    strokeWidths: STROKE_WIDTH_TABLE,
    viewBoxes,
    counts: {
      byLibrary,
      byCategory,
      byStyle,
    },
  };

  const metaPath = path.join(OUT_DIR, 'search-meta.json');
  const metaBuf = Buffer.from(JSON.stringify(searchMeta, null, 2), 'utf8');
  fs.writeFileSync(metaPath, metaBuf);

  const elapsedMs = (performance.now() - t0).toFixed(0);
  const binMB = (totalBytes / (1024 * 1024)).toFixed(2);
  const metaKB = (metaBuf.byteLength / 1024).toFixed(2);
  console.log(
    `[build-search-index] Built search.bin (${binMB} MB, ${totalIcons.toLocaleString()} icons, ` +
      `${vocabCount.toLocaleString()} vocab tokens, ${totalPostings.toLocaleString()} postings, ` +
      `hash=${contentHash}) + search-meta.json (${metaKB} KB) in ${elapsedMs} ms`,
  );
}

main();
