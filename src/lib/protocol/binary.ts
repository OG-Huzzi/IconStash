/**
 * IconStash v2 Binary Search Index Codec & Bitmask Helpers
 * Zero-copy TypedArray views over /index/v1/search.bin (Little-Endian).
 * Matches docs/architecture.md Sections 4 & 5.
 */

import {
  SEARCH_INDEX_HEADER_BYTES,
  SEARCH_INDEX_MAGIC,
  SEARCH_INDEX_VERSION,
  STROKE_WIDTH_TABLE,
  type ChunkManifest,
  type DecodedIconMeta,
  type IconMetaFields,
  type ParsedSearchIndex,
  type ResolvedShardLocation,
  type SearchIndexHeader,
} from './types.ts';

const sharedTextDecoder = new TextDecoder('utf-8');
const sharedTextEncoder = new TextEncoder();

// ---------------------------------------------------------------------------
// Alignment Helpers
// ---------------------------------------------------------------------------

export function align4(offset: number): number {
  return (offset + 3) & ~3;
}

// ---------------------------------------------------------------------------
// Per-Icon Bit-Packed Metadata (metaPacked[iconIndex], 32 bits)
// Bits 0..4   (5 bits): libId (0..27)
// Bits 5..8   (4 bits): catId (0..15)
// Bits 9..11  (3 bits): styleId (0..6)
// Bits 12..13 (2 bits): strokeIdx (0..3 -> [0, 1, 1.5, 2])
// Bit  14     (1 bit) : isFilled (0/1)
// Bit  15     (1 bit) : hasVariants (0/1)
// Bits 16..31 (16 bits): rankScore (0..65535)
// ---------------------------------------------------------------------------

export function packIconMeta(fields: IconMetaFields): number {
  const libId = fields.libId & 0x1f;
  const catId = fields.catId & 0x0f;
  const styleId = fields.styleId & 0x07;
  const strokeIdx = fields.strokeIdx & 0x03;
  const isFilled = fields.isFilled ? 1 : 0;
  const hasVariants = fields.hasVariants ? 1 : 0;
  const rankScore = Math.max(0, Math.min(0xffff, fields.rankScore | 0)) & 0xffff;

  return (
    (libId |
      (catId << 5) |
      (styleId << 9) |
      (strokeIdx << 12) |
      (isFilled << 14) |
      (hasVariants << 15) |
      (rankScore << 16)) >>>
    0
  );
}

export function getMetaLibId(packed: number): number {
  return packed & 0x1f;
}

export function getMetaCatId(packed: number): number {
  return (packed >>> 5) & 0x0f;
}

export function getMetaStyleId(packed: number): number {
  return (packed >>> 9) & 0x07;
}

export function getMetaStrokeIdx(packed: number): number {
  return (packed >>> 12) & 0x03;
}

export function getMetaIsFilled(packed: number): boolean {
  return ((packed >>> 14) & 1) === 1;
}

export function getMetaHasVariants(packed: number): boolean {
  return ((packed >>> 15) & 1) === 1;
}

export function getMetaRankScore(packed: number): number {
  return (packed >>> 16) & 0xffff;
}

export function unpackIconMeta(packed: number): DecodedIconMeta {
  const strokeIdx = getMetaStrokeIdx(packed);
  return {
    libId: getMetaLibId(packed),
    catId: getMetaCatId(packed),
    styleId: getMetaStyleId(packed),
    strokeIdx,
    strokeWidth: STROKE_WIDTH_TABLE[strokeIdx] ?? 0,
    isFilled: getMetaIsFilled(packed),
    hasVariants: getMetaHasVariants(packed),
    rankScore: getMetaRankScore(packed),
  };
}

/**
 * Fast bitmask facet check.
 * A mask value of 0 means "all values allowed" for that facet.
 */
export function matchesFacetMasks(
  packed: number,
  libMask: number,
  catMask: number,
  styleMask: number,
): boolean {
  if (libMask !== 0 && ((1 << (packed & 0x1f)) & libMask) === 0) {
    return false;
  }
  if (catMask !== 0 && ((1 << ((packed >>> 5) & 0x0f)) & catMask) === 0) {
    return false;
  }
  if (styleMask !== 0 && ((1 << ((packed >>> 9) & 0x07)) & styleMask) === 0) {
    return false;
  }
  return true;
}

// ---------------------------------------------------------------------------
// Posting Entry Encoding (postingsIds[k], 32 bits)
// Bits 0..23  (24 bits): iconIndex (0..16,777,215)
// Bits 24..27 (4 bits) : matchWeight (4 = exact name, 2 = prefix/sub-token, 1 = tag/synonym)
// Bits 28..31 (4 bits) : reserved (0)
// ---------------------------------------------------------------------------

export function packPosting(iconIndex: number, matchWeight: number): number {
  return ((iconIndex & 0x00ffffff) | ((matchWeight & 0x0f) << 24)) >>> 0;
}

export function getPostingIconIndex(posting: number): number {
  return posting & 0x00ffffff;
}

export function getPostingMatchWeight(posting: number): number {
  return (posting >>> 24) & 0x0f;
}

// ---------------------------------------------------------------------------
// Binary Header & Full Index Parser (Zero-Copy TypedArray Views)
// ---------------------------------------------------------------------------

export function parseSearchIndexHeader(buffer: ArrayBuffer): SearchIndexHeader {
  if (buffer.byteLength < SEARCH_INDEX_HEADER_BYTES) {
    throw new Error(
      `Invalid search.bin: expected at least ${SEARCH_INDEX_HEADER_BYTES} bytes, got ${buffer.byteLength}`,
    );
  }

  const view = new DataView(buffer, 0, SEARCH_INDEX_HEADER_BYTES);
  const magic = view.getUint32(0, true);
  if (magic !== SEARCH_INDEX_MAGIC) {
    throw new Error(
      `Invalid search.bin magic: expected 0x${SEARCH_INDEX_MAGIC.toString(16)}, got 0x${magic.toString(16)}`,
    );
  }

  const version = view.getUint16(4, true);
  if (version !== SEARCH_INDEX_VERSION) {
    throw new Error(
      `Unsupported search.bin version: expected ${SEARCH_INDEX_VERSION}, got ${version}`,
    );
  }

  const flags = view.getUint16(6, true);
  const iconCount = view.getUint32(8, true);
  const vocabCount = view.getUint32(12, true);
  const postingsCount = view.getUint32(16, true);
  const offMetaPacked = view.getUint32(20, true);
  const offNameOffsets = view.getUint32(24, true);
  const offNameBuf = view.getUint32(28, true);
  const offVocabOffsets = view.getUint32(32, true);
  const offVocabBuf = view.getUint32(36, true);
  const offPostingsOffsets = view.getUint32(40, true);
  const offPostingsIds = view.getUint32(44, true);

  return {
    magic,
    version,
    flags,
    iconCount,
    vocabCount,
    postingsCount,
    offMetaPacked,
    offNameOffsets,
    offNameBuf,
    offVocabOffsets,
    offVocabBuf,
    offPostingsOffsets,
    offPostingsIds,
  };
}

function assertAlignedSection(
  name: string,
  offset: number,
  byteLength: number,
  totalBytes: number,
): void {
  if ((offset & 3) !== 0) {
    throw new Error(`Section ${name} offset ${offset} is not 4-byte aligned`);
  }
  if (offset < SEARCH_INDEX_HEADER_BYTES || offset + byteLength > totalBytes) {
    throw new Error(
      `Section ${name} out of bounds: offset=${offset}, bytes=${byteLength}, total=${totalBytes}`,
    );
  }
}

export function parseSearchIndex(buffer: ArrayBuffer): ParsedSearchIndex {
  const header = parseSearchIndexHeader(buffer);
  const totalBytes = buffer.byteLength;

  const {
    iconCount,
    vocabCount,
    postingsCount,
    offMetaPacked,
    offNameOffsets,
    offNameBuf,
    offVocabOffsets,
    offVocabBuf,
    offPostingsOffsets,
    offPostingsIds,
  } = header;

  assertAlignedSection('metaPacked', offMetaPacked, iconCount * 4, totalBytes);
  assertAlignedSection('nameOffsets', offNameOffsets, (iconCount + 1) * 4, totalBytes);
  assertAlignedSection('vocabOffsets', offVocabOffsets, (vocabCount + 1) * 4, totalBytes);
  assertAlignedSection('postingsOffsets', offPostingsOffsets, (vocabCount + 1) * 4, totalBytes);
  assertAlignedSection('postingsIds', offPostingsIds, postingsCount * 4, totalBytes);

  const metaPacked = new Uint32Array(buffer, offMetaPacked, iconCount);
  const nameOffsets = new Uint32Array(buffer, offNameOffsets, iconCount + 1);
  const nameBufLen = nameOffsets[iconCount] ?? 0;
  assertAlignedSection('nameBuf', offNameBuf, nameBufLen, totalBytes);
  const nameBuf = new Uint8Array(buffer, offNameBuf, nameBufLen);

  const vocabOffsets = new Uint32Array(buffer, offVocabOffsets, vocabCount + 1);
  const vocabBufLen = vocabOffsets[vocabCount] ?? 0;
  assertAlignedSection('vocabBuf', offVocabBuf, vocabBufLen, totalBytes);
  const vocabBuf = new Uint8Array(buffer, offVocabBuf, vocabBufLen);

  const postingsOffsets = new Uint32Array(buffer, offPostingsOffsets, vocabCount + 1);
  const postingsIds = new Uint32Array(buffer, offPostingsIds, postingsCount);

  return {
    header,
    metaPacked,
    nameOffsets,
    nameBuf,
    vocabOffsets,
    vocabBuf,
    postingsOffsets,
    postingsIds,
    byteLength: totalBytes,
  };
}

// ---------------------------------------------------------------------------
// Binary Encoder (for build script & round-trip tests)
// ---------------------------------------------------------------------------

export interface EncodeSearchIndexInput {
  metaPacked: Uint32Array;
  nameOffsets: Uint32Array;
  nameBuf: Uint8Array;
  vocabOffsets: Uint32Array;
  vocabBuf: Uint8Array;
  postingsOffsets: Uint32Array;
  postingsIds: Uint32Array;
  flags?: number;
}

export function encodeSearchIndex(input: EncodeSearchIndexInput): ArrayBuffer {
  const iconCount = input.metaPacked.length;
  const vocabCount = input.vocabOffsets.length - 1;
  const postingsCount = input.postingsIds.length;

  const offMetaPacked = SEARCH_INDEX_HEADER_BYTES;
  const offNameOffsets = align4(offMetaPacked + iconCount * 4);
  const offNameBuf = align4(offNameOffsets + (iconCount + 1) * 4);
  const offVocabOffsets = align4(offNameBuf + input.nameBuf.byteLength);
  const offVocabBuf = align4(offVocabOffsets + (vocabCount + 1) * 4);
  const offPostingsOffsets = align4(offVocabBuf + input.vocabBuf.byteLength);
  const offPostingsIds = align4(offPostingsOffsets + (vocabCount + 1) * 4);
  const totalBytes = align4(offPostingsIds + postingsCount * 4);

  const buffer = new ArrayBuffer(totalBytes);
  const headerView = new DataView(buffer, 0, SEARCH_INDEX_HEADER_BYTES);
  headerView.setUint32(0, SEARCH_INDEX_MAGIC, true);
  headerView.setUint16(4, SEARCH_INDEX_VERSION, true);
  headerView.setUint16(6, (input.flags ?? 0) & 0xffff, true);
  headerView.setUint32(8, iconCount, true);
  headerView.setUint32(12, vocabCount, true);
  headerView.setUint32(16, postingsCount, true);
  headerView.setUint32(20, offMetaPacked, true);
  headerView.setUint32(24, offNameOffsets, true);
  headerView.setUint32(28, offNameBuf, true);
  headerView.setUint32(32, offVocabOffsets, true);
  headerView.setUint32(36, offVocabBuf, true);
  headerView.setUint32(40, offPostingsOffsets, true);
  headerView.setUint32(44, offPostingsIds, true);

  new Uint32Array(buffer, offMetaPacked, iconCount).set(input.metaPacked);
  new Uint32Array(buffer, offNameOffsets, iconCount + 1).set(input.nameOffsets);
  new Uint8Array(buffer, offNameBuf, input.nameBuf.byteLength).set(input.nameBuf);
  new Uint32Array(buffer, offVocabOffsets, vocabCount + 1).set(input.vocabOffsets);
  new Uint8Array(buffer, offVocabBuf, input.vocabBuf.byteLength).set(input.vocabBuf);
  new Uint32Array(buffer, offPostingsOffsets, vocabCount + 1).set(input.postingsOffsets);
  new Uint32Array(buffer, offPostingsIds, postingsCount).set(input.postingsIds);

  return buffer;
}

// ---------------------------------------------------------------------------
// UTF-8 String Readers & Binary Search Over Sorted Vocab
// ---------------------------------------------------------------------------

export function readIconName(
  index: ParsedSearchIndex,
  iconIndex: number,
  decoder: TextDecoder = sharedTextDecoder,
): string {
  const start = index.nameOffsets[iconIndex];
  const end = index.nameOffsets[iconIndex + 1];
  return decoder.decode(index.nameBuf.subarray(start, end));
}

export function readVocabToken(
  index: ParsedSearchIndex,
  vocabIndex: number,
  decoder: TextDecoder = sharedTextDecoder,
): string {
  const start = index.vocabOffsets[vocabIndex];
  const end = index.vocabOffsets[vocabIndex + 1];
  return decoder.decode(index.vocabBuf.subarray(start, end));
}

/** Lexicographic unsigned byte comparison between vocabBuf[start..end) and needle bytes */
function compareBytes(
  buf: Uint8Array,
  start: number,
  end: number,
  needle: Uint8Array,
): number {
  const lenA = end - start;
  const lenB = needle.length;
  const minLen = lenA < lenB ? lenA : lenB;
  for (let i = 0; i < minLen; i++) {
    const diff = buf[start + i] - needle[i];
    if (diff !== 0) return diff;
  }
  return lenA - lenB;
}

/** Returns true if buf[start..end) starts with prefix bytes */
function startsWithBytes(
  buf: Uint8Array,
  start: number,
  end: number,
  prefix: Uint8Array,
): boolean {
  if (end - start < prefix.length) return false;
  for (let i = 0; i < prefix.length; i++) {
    if (buf[start + i] !== prefix[i]) return false;
  }
  return true;
}

/** Binary search for exact lowercase token in vocabBuf; returns vocab index or -1 */
export function findExactVocabIndex(index: ParsedSearchIndex, token: string): number {
  const needle = sharedTextEncoder.encode(token);
  const { vocabOffsets, vocabBuf } = index;
  let lo = 0;
  let hi = index.header.vocabCount - 1;

  while (lo <= hi) {
    const mid = (lo + hi) >>> 1;
    const cmp = compareBytes(vocabBuf, vocabOffsets[mid], vocabOffsets[mid + 1], needle);
    if (cmp === 0) return mid;
    if (cmp < 0) lo = mid + 1;
    else hi = mid - 1;
  }
  return -1;
}

/**
 * Binary search for the [startIdx, endIdx) range of sorted vocab tokens
 * starting with the given lowercase UTF-8 prefix.
 */
export function findVocabPrefixRange(
  index: ParsedSearchIndex,
  prefix: string,
): [startIdx: number, endIdx: number] {
  const needle = sharedTextEncoder.encode(prefix);
  const { vocabOffsets, vocabBuf } = index;
  const n = index.header.vocabCount;

  // Lower bound: first token >= needle
  let lo = 0;
  let hi = n;
  while (lo < hi) {
    const mid = (lo + hi) >>> 1;
    const cmp = compareBytes(vocabBuf, vocabOffsets[mid], vocabOffsets[mid + 1], needle);
    if (cmp < 0) lo = mid + 1;
    else hi = mid;
  }
  const startIdx = lo;

  // Advance upper bound while tokens start with prefix (binary search on prefix match)
  let endLo = startIdx;
  let endHi = n;
  while (endLo < endHi) {
    const mid = (endLo + endHi) >>> 1;
    if (startsWithBytes(vocabBuf, vocabOffsets[mid], vocabOffsets[mid + 1], needle)) {
      endLo = mid + 1;
    } else {
      endHi = mid;
    }
  }
  return [startIdx, endLo];
}

// ---------------------------------------------------------------------------
// Manifest Shard Lookup (O(log 28) Binary Search)
// ---------------------------------------------------------------------------

export function resolveShardForIcon(
  manifest: ChunkManifest,
  iconIndex: number,
): ResolvedShardLocation | null {
  const libs = manifest.libraries;
  let lo = 0;
  let hi = libs.length - 1;

  while (lo <= hi) {
    const mid = (lo + hi) >>> 1;
    const lib = libs[mid];
    if (iconIndex < lib.startIndex) {
      hi = mid - 1;
    } else if (iconIndex > lib.endIndex) {
      lo = mid + 1;
    } else {
      // Found library; locate shard (usually 1..6 shards)
      const shards = lib.shards;
      for (let s = 0; s < shards.length; s++) {
        const shard = shards[s];
        if (iconIndex >= shard.start && iconIndex < shard.start + shard.count) {
          return {
            library: lib,
            shard,
            shardIndex: s,
            localOffset: iconIndex - shard.start,
          };
        }
      }
      return null;
    }
  }
  return null;
}
