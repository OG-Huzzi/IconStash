import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import { describe, expect, it } from 'vitest';
import {
  encodeSearchIndex,
  findExactVocabIndex,
  findVocabPrefixRange,
  getMetaCatId,
  getMetaHasVariants,
  getMetaIsFilled,
  getMetaLibId,
  getMetaRankScore,
  getMetaStrokeIdx,
  getMetaStyleId,
  getPostingIconIndex,
  getPostingMatchWeight,
  matchesFacetMasks,
  packIconMeta,
  packPosting,
  parseSearchIndex,
  parseSearchIndexHeader,
  readIconName,
  readVocabToken,
  resolveShardForIcon,
  unpackIconMeta,
} from '../../src/lib/protocol/binary.ts';
import {
  CHUNK_SCHEMA_VERSION,
  CHUNK_SIZE_CAP,
  IconChunkFlags,
  MEGA_LIBRARY_THRESHOLD,
  PostingMatchWeight,
  SEARCH_INDEX_HEADER_BYTES,
  SEARCH_INDEX_MAGIC,
  SEARCH_INDEX_VERSION,
  type ChunkManifest,
  type LibraryChunk,
  type SearchMeta,
} from '../../src/lib/protocol/types.ts';

const ROOT = path.resolve(import.meta.dirname, '..', '..');
const CHUNKS_DIR = path.join(ROOT, 'public', 'chunks', 'v1');
const INDEX_DIR = path.join(ROOT, 'public', 'index', 'v1');
const EXPECTED_TOTAL_ICONS = 134_701;
const EXPECTED_LIBRARIES = 28;

function readArrayBuffer(filePath: string): ArrayBuffer {
  const buf = fs.readFileSync(filePath);
  return buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength);
}

describe('Protocol bit-packing & binary codec unit tests', () => {
  it('round-trips packIconMeta and unpackIconMeta across boundary values', () => {
    const cases = [
      {
        libId: 0,
        catId: 0,
        styleId: 0,
        strokeIdx: 0,
        isFilled: false,
        hasVariants: false,
        rankScore: 0,
      },
      {
        libId: 27,
        catId: 15,
        styleId: 6,
        strokeIdx: 3,
        isFilled: true,
        hasVariants: true,
        rankScore: 65535,
      },
      {
        libId: 14,
        catId: 9,
        styleId: 4,
        strokeIdx: 2,
        isFilled: false,
        hasVariants: true,
        rankScore: 42123,
      },
    ];

    for (const c of cases) {
      const packed = packIconMeta(c);
      expect(getMetaLibId(packed)).toBe(c.libId);
      expect(getMetaCatId(packed)).toBe(c.catId);
      expect(getMetaStyleId(packed)).toBe(c.styleId);
      expect(getMetaStrokeIdx(packed)).toBe(c.strokeIdx);
      expect(getMetaIsFilled(packed)).toBe(c.isFilled);
      expect(getMetaHasVariants(packed)).toBe(c.hasVariants);
      expect(getMetaRankScore(packed)).toBe(c.rankScore);

      const unpacked = unpackIconMeta(packed);
      expect(unpacked.libId).toBe(c.libId);
      expect(unpacked.catId).toBe(c.catId);
      expect(unpacked.styleId).toBe(c.styleId);
      expect(unpacked.strokeIdx).toBe(c.strokeIdx);
      expect(unpacked.isFilled).toBe(c.isFilled);
      expect(unpacked.hasVariants).toBe(c.hasVariants);
      expect(unpacked.rankScore).toBe(c.rankScore);
    }
  });

  it('evaluates matchesFacetMasks accurately for 0 (wildcard) and bitmasks', () => {
    const packed = packIconMeta({
      libId: 27,
      catId: 11,
      styleId: 5,
      strokeIdx: 1,
      isFilled: true,
      hasVariants: false,
      rankScore: 1000,
    });

    expect(matchesFacetMasks(packed, 0, 0, 0)).toBe(true);
    expect(matchesFacetMasks(packed, 1 << 27, 1 << 11, 1 << 5)).toBe(true);
    expect(matchesFacetMasks(packed, 1 << 0, 0, 0)).toBe(false);
    expect(matchesFacetMasks(packed, 0, 1 << 3, 0)).toBe(false);
    expect(matchesFacetMasks(packed, 0, 0, 1 << 2)).toBe(false);
  });

  it('round-trips packPosting / getPostingIconIndex / getPostingMatchWeight', () => {
    const p = packPosting(134_700, PostingMatchWeight.EXACT_NAME);
    expect(getPostingIconIndex(p)).toBe(134_700);
    expect(getPostingMatchWeight(p)).toBe(4);
  });

  it('rejects invalid magic, version, or truncated search.bin headers', () => {
    expect(() => parseSearchIndexHeader(new ArrayBuffer(16))).toThrow(/expected at least 64/);

    const badMagic = new ArrayBuffer(SEARCH_INDEX_HEADER_BYTES);
    expect(() => parseSearchIndexHeader(badMagic)).toThrow(/magic/i);

    const badVersion = new ArrayBuffer(SEARCH_INDEX_HEADER_BYTES);
    const dv = new DataView(badVersion);
    dv.setUint32(0, SEARCH_INDEX_MAGIC, true);
    dv.setUint16(4, 99, true);
    expect(() => parseSearchIndexHeader(badVersion)).toThrow(/version/i);
  });
});

describe('Sharded per-library chunks (public/chunks/v1/)', () => {
  const manifestPath = path.join(CHUNKS_DIR, 'manifest.json');
  const manifest: ChunkManifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

  it('contains all 134,701 icons across 28 libraries with contiguous global indices', () => {
    expect(manifest.schemaVersion).toBe(CHUNK_SCHEMA_VERSION);
    expect(manifest.totalIcons).toBe(EXPECTED_TOTAL_ICONS);
    expect(manifest.chunkSizeCap).toBe(CHUNK_SIZE_CAP);
    expect(manifest.libraries).toHaveLength(EXPECTED_LIBRARIES);
    expect(manifest.contentHash).toMatch(/^[0-9a-f]{8}$/);

    let expectedStart = 0;
    for (let i = 0; i < manifest.libraries.length; i++) {
      const lib = manifest.libraries[i];
      expect(lib.id).toBe(i);
      expect(lib.startIndex).toBe(expectedStart);
      expect(lib.endIndex).toBe(expectedStart + lib.count - 1);

      let shardSum = 0;
      for (const shard of lib.shards) {
        expect(shard.start).toBe(expectedStart + shardSum);
        expect(shard.count).toBeGreaterThan(0);
        if (lib.count > MEGA_LIBRARY_THRESHOLD) {
          expect(shard.count).toBeLessThanOrEqual(CHUNK_SIZE_CAP);
        }
        shardSum += shard.count;
      }
      expect(shardSum).toBe(lib.count);
      expectedStart += lib.count;
    }
    expect(expectedStart).toBe(EXPECTED_TOTAL_ICONS);
  });

  it('sub-shards only the 5 mega-libraries (> 8,000 icons) and keeps every shard compact', () => {
    const megaSlugs = manifest.libraries
      .filter((l) => l.shards.length > 1)
      .map((l) => l.slug)
      .sort();
    expect(megaSlugs).toEqual([
      'fluent',
      'material',
      'materialsymbols',
      'materialsymbolslight',
      'phosphor',
    ]);

    let totalBytes = 0;
    let totalIconsLoaded = 0;
    let maxShardBytes = 0;

    for (const lib of manifest.libraries) {
      for (let s = 0; s < lib.shards.length; s++) {
        const shardEntry = lib.shards[s];
        const filename = path.basename(shardEntry.url);
        const fullPath = path.join(CHUNKS_DIR, filename);
        expect(fs.existsSync(fullPath)).toBe(true);

        const stat = fs.statSync(fullPath);
        expect(stat.size).toBe(shardEntry.bytes);
        totalBytes += stat.size;
        if (stat.size > maxShardBytes) maxShardBytes = stat.size;

        // Every individual shard should stay well under 7 MB raw (fits in 4-6 chunk LRU budget)
        expect(stat.size).toBeLessThan(7 * 1024 * 1024);

        const chunk: LibraryChunk = JSON.parse(fs.readFileSync(fullPath, 'utf8'));
        expect(chunk.schemaVersion).toBe(CHUNK_SCHEMA_VERSION);
        expect(chunk.librarySlug).toBe(lib.slug);
        expect(chunk.libraryId).toBe(lib.id);
        expect(chunk.part).toBe(s);
        expect(chunk.totalParts).toBe(lib.shards.length);
        expect(chunk.startIndex).toBe(shardEntry.start);
        expect(chunk.count).toBe(shardEntry.count);
        expect(chunk.icons).toHaveLength(shardEntry.count);
        expect(chunk.viewBoxes.length).toBeGreaterThan(0);

        totalIconsLoaded += chunk.icons.length;
      }
    }

    expect(totalIconsLoaded).toBe(EXPECTED_TOTAL_ICONS);
    // Compact footprint: master JSONs are ~140 MB; normalized tuple shards should be < 85 MB raw
    expect(totalBytes).toBeLessThan(85 * 1024 * 1024);
    expect(maxShardBytes).toBeGreaterThan(0);
  });

  it('normalizes SVG markup at build time and preserves animated SMIL attributes & idOverrides', () => {
    const lucide: LibraryChunk = JSON.parse(
      fs.readFileSync(path.join(CHUNKS_DIR, 'lucide.json'), 'utf8'),
    );
    const firstLucide = lucide.icons[0];
    expect(firstLucide[0]).toBe('a-arrow-down');
    expect(firstLucide[1]).not.toMatch(/<svg\b/i);
    expect(firstLucide[1]).toContain('stroke="currentColor"');
    // Inline stroke-width stripped on stroke icons so CSS custom property applies cleanly
    expect(firstLucide[1]).not.toMatch(/\sstroke-width=/i);

    const linemd: LibraryChunk = JSON.parse(
      fs.readFileSync(path.join(CHUNKS_DIR, 'linemd.json'), 'utf8'),
    );
    const animatedIcons = linemd.icons.filter(
      (t) => (t[4] & IconChunkFlags.HAS_ANIMATED_ELEMENTS) !== 0,
    );
    expect(animatedIcons.length).toBeGreaterThan(1000);
    // SMIL fill="freeze" must be preserved, NOT rewritten to currentColor
    expect(animatedIcons[0][1]).toContain('fill="freeze"');

    // Verify idOverrides restores non-standard canonical IDs (e.g., tabler-baseline-density-large)
    const tabler: LibraryChunk = JSON.parse(
      fs.readFileSync(path.join(CHUNKS_DIR, 'tabler.json'), 'utf8'),
    );
    expect(tabler.idOverrides).toBeDefined();
    expect(Object.values(tabler.idOverrides || {})).toContain('tabler-baseline-density-large');
  });

  it('resolves any global iconIndex to its exact shard and localOffset via resolveShardForIcon', () => {
    const first = resolveShardForIcon(manifest, 0);
    expect(first).not.toBeNull();
    expect(first!.library.slug).toBe('lucide');
    expect(first!.localOffset).toBe(0);

    const last = resolveShardForIcon(manifest, EXPECTED_TOTAL_ICONS - 1);
    expect(last).not.toBeNull();
    expect(last!.library.slug).toBe('simpleicons');
    expect(last!.localOffset).toBe(last!.shard.count - 1);

    // Check inside a mega-library second shard (fluent has 20,170 icons -> 6 shards)
    const fluentLib = manifest.libraries.find((l) => l.slug === 'fluent')!;
    const fluentMidIdx = fluentLib.startIndex + 4500;
    const fluentLoc = resolveShardForIcon(manifest, fluentMidIdx);
    expect(fluentLoc).not.toBeNull();
    expect(fluentLoc!.shardIndex).toBe(1);
    expect(fluentLoc!.localOffset).toBe(500);

    expect(resolveShardForIcon(manifest, -1)).toBeNull();
    expect(resolveShardForIcon(manifest, EXPECTED_TOTAL_ICONS)).toBeNull();
  });
});

describe('Binary search index (public/index/v1/search.bin & search-meta.json)', () => {
  const binPath = path.join(INDEX_DIR, 'search.bin');
  const metaPath = path.join(INDEX_DIR, 'search-meta.json');
  const manifestPath = path.join(CHUNKS_DIR, 'manifest.json');

  const binArrayBuffer = readArrayBuffer(binPath);
  const parsed = parseSearchIndex(binArrayBuffer);
  const meta: SearchMeta = JSON.parse(fs.readFileSync(metaPath, 'utf8'));
  const manifest: ChunkManifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

  it('parses cleanly through src/lib/protocol/binary.ts and stays compact', () => {
    expect(parsed.header.magic).toBe(SEARCH_INDEX_MAGIC);
    expect(parsed.header.version).toBe(SEARCH_INDEX_VERSION);
    expect(parsed.header.iconCount).toBe(EXPECTED_TOTAL_ICONS);
    expect(parsed.header.vocabCount).toBe(meta.vocabCount);
    expect(parsed.header.postingsCount).toBe(meta.postingsCount);
    expect(parsed.byteLength).toBe(meta.indexBytes);

    // Uncompressed search.bin should be compact (< 10 MB) and gzipped < 3.5 MB
    expect(parsed.byteLength).toBeLessThan(10 * 1024 * 1024);
    const gzipped = zlib.gzipSync(Buffer.from(binArrayBuffer));
    expect(gzipped.byteLength).toBeLessThan(3.5 * 1024 * 1024);
  });

  it('round-trips byte-for-byte through encodeSearchIndex -> parseSearchIndex', () => {
    const reencoded = encodeSearchIndex({
      metaPacked: parsed.metaPacked,
      nameOffsets: parsed.nameOffsets,
      nameBuf: parsed.nameBuf,
      vocabOffsets: parsed.vocabOffsets,
      vocabBuf: parsed.vocabBuf,
      postingsOffsets: parsed.postingsOffsets,
      postingsIds: parsed.postingsIds,
      flags: parsed.header.flags,
    });

    expect(reencoded.byteLength).toBe(binArrayBuffer.byteLength);
    expect(Buffer.compare(Buffer.from(reencoded), Buffer.from(binArrayBuffer))).toBe(0);
  });

  it('has complete and consistent search-meta.json taxonomies and counts', () => {
    expect(meta.schemaVersion).toBe(1);
    expect(meta.totalIcons).toBe(EXPECTED_TOTAL_ICONS);
    expect(meta.libraries).toHaveLength(EXPECTED_LIBRARIES);
    expect(meta.categories).toHaveLength(16);
    expect(meta.subCategories).toHaveLength(16);
    expect(meta.styles).toHaveLength(7);
    expect(meta.strokeWidths).toEqual([0, 1, 1.5, 2]);
    expect(meta.viewBoxes.length).toBeGreaterThanOrEqual(40);

    const sum = (arr: number[]) => arr.reduce((a, b) => a + b, 0);
    expect(sum(meta.counts.byLibrary)).toBe(EXPECTED_TOTAL_ICONS);
    expect(sum(meta.counts.byCategory)).toBe(EXPECTED_TOTAL_ICONS);
    expect(sum(meta.counts.byStyle)).toBe(EXPECTED_TOTAL_ICONS);
  });

  it('matches chunk names and library IDs across all 28 libraries', () => {
    for (const lib of manifest.libraries) {
      const firstShardPath = path.join(CHUNKS_DIR, path.basename(lib.shards[0].url));
      const firstChunk: LibraryChunk = JSON.parse(fs.readFileSync(firstShardPath, 'utf8'));

      // First icon of library
      expect(getMetaLibId(parsed.metaPacked[lib.startIndex])).toBe(lib.id);
      expect(readIconName(parsed, lib.startIndex)).toBe(firstChunk.icons[0][0].toLowerCase());

      // Last icon of library
      const lastShard = lib.shards[lib.shards.length - 1];
      const lastChunk: LibraryChunk =
        lib.shards.length === 1
          ? firstChunk
          : JSON.parse(
              fs.readFileSync(path.join(CHUNKS_DIR, path.basename(lastShard.url)), 'utf8'),
            );
      expect(getMetaLibId(parsed.metaPacked[lib.endIndex])).toBe(lib.id);
      expect(readIconName(parsed, lib.endIndex)).toBe(
        lastChunk.icons[lastChunk.icons.length - 1][0].toLowerCase(),
      );
    }
  });

  it('stores vocabulary in strictly sorted UTF-8 byte order with valid ascending postings', () => {
    const V = parsed.header.vocabCount;
    expect(V).toBeGreaterThan(8000);

    let emptyTokens = 0;
    let outOfOrderTokens = 0;
    let emptyPostingLists = 0;
    let invalidPostingOrder = 0;
    let invalidIconIndices = 0;
    let invalidWeights = 0;
    let totalPostingsChecked = 0;

    let prevTokenBuf: Buffer | null = null;
    for (let i = 0; i < V; i++) {
      const start = parsed.vocabOffsets[i];
      const end = parsed.vocabOffsets[i + 1];
      if (end <= start) emptyTokens++;

      const tokBuf = Buffer.from(
        parsed.vocabBuf.buffer,
        parsed.vocabBuf.byteOffset + start,
        end - start,
      );
      if (prevTokenBuf !== null && Buffer.compare(prevTokenBuf, tokBuf) >= 0) {
        outOfOrderTokens++;
      }
      prevTokenBuf = tokBuf;

      const pStart = parsed.postingsOffsets[i];
      const pEnd = parsed.postingsOffsets[i + 1];
      if (pEnd <= pStart) emptyPostingLists++;

      let prevIconIdx = -1;
      for (let p = pStart; p < pEnd; p++) {
        const posting = parsed.postingsIds[p];
        const iconIdx = getPostingIconIndex(posting);
        const weight = getPostingMatchWeight(posting);
        if (iconIdx <= prevIconIdx) invalidPostingOrder++;
        if (iconIdx >= EXPECTED_TOTAL_ICONS) invalidIconIndices++;
        if (weight !== 1 && weight !== 2 && weight !== 4) invalidWeights++;
        prevIconIdx = iconIdx;
        totalPostingsChecked++;
      }
    }

    expect(emptyTokens).toBe(0);
    expect(outOfOrderTokens).toBe(0);
    expect(emptyPostingLists).toBe(0);
    expect(invalidPostingOrder).toBe(0);
    expect(invalidIconIndices).toBe(0);
    expect(invalidWeights).toBe(0);
    expect(totalPostingsChecked).toBe(parsed.header.postingsCount);
  });

  it('supports exact and prefix binary search lookups over vocabBuf', () => {
    for (const token of ['arrow', 'home', 'heart', 'lucide', 'calendar']) {
      const idx = findExactVocabIndex(parsed, token);
      expect(idx).toBeGreaterThanOrEqual(0);
      expect(readVocabToken(parsed, idx)).toBe(token);

      const pStart = parsed.postingsOffsets[idx];
      const pEnd = parsed.postingsOffsets[idx + 1];
      expect(pEnd - pStart).toBeGreaterThan(50);
    }

    const [start, end] = findVocabPrefixRange(parsed, 'arr');
    expect(end).toBeGreaterThan(start);
    for (let i = start; i < end; i++) {
      expect(readVocabToken(parsed, i).startsWith('arr')).toBe(true);
    }
  });
});
