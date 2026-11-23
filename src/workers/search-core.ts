/**
 * Pure TypeScript Binary Typed-Array Search Engine for IconStash v2.
 *
 * Runs identically in both Web Workers and Node/Vitest without DOM dependencies.
 * Parses the compact binary `/index/v1/search.bin` format defined in
 * `docs/architecture.md` §5.1 into zero-copy typed-array views over a single
 * ArrayBuffer, avoiding per-icon JS objects and GC pressure.
 */

export const SEARCH_INDEX_MAGIC = 0x32534349; // "ICS2" little-endian
export const SEARCH_INDEX_VERSION = 1;
export const SEARCH_HEADER_BYTES = 64;

export const LIBRARY_COUNT = 28;
export const CATEGORY_COUNT = 16;
export const STYLE_COUNT = 7;

export const STROKE_WIDTH_TABLE = [0, 1, 1.5, 2] as const;

export const MATCH_WEIGHT_EXACT_NAME = 4;
export const MATCH_WEIGHT_PREFIX_NAME = 2;
export const MATCH_WEIGHT_TAG = 1;

export type SearchSortMode =
  | 'relevance'
  | 'az'
  | 'za'
  | 'library'
  | 'alphabetical'
  | 'popularity';

export interface SearchQueryOptions {
  query: string;
  /** 28-bit bitmask (0 = all libraries) */
  libMask?: number;
  /** 16-bit bitmask (0 = all categories) */
  catMask?: number;
  /** 7-bit bitmask (0 = all styles) */
  styleMask?: number;
  sort?: SearchSortMode;
  /** 0 or undefined = return all matching indices */
  limit?: number;
}

export interface SearchQueryResult {
  indices: Uint32Array;
  totalMatches: number;
  elapsedMs: number;
  libraryCounts: Uint32Array;
  categoryCounts: Uint32Array;
  styleCounts: Uint32Array;
}

export interface SearchHeader {
  magic: number;
  version: number;
  flags: number;
  iconCount: number;
  vocabCount: number;
  postingsCount: number;
  offMetaPacked: number;
  offNameOffsets: number;
  offNameBuf: number;
  offVocabOffsets: number;
  offVocabBuf: number;
  offPostingsOffsets: number;
  offPostingsIds: number;
}

export interface UnpackedMeta {
  libId: number;
  catId: number;
  styleId: number;
  strokeIdx: number;
  strokeWidth: number;
  isFilled: boolean;
  hasVariants: boolean;
  rankScore: number;
}

export interface BinaryIndexIconInput {
  name: string;
  tags?: readonly string[];
  libId: number;
  catId: number;
  styleId: number;
  strokeIdx?: number;
  isFilled?: boolean;
  hasVariants?: boolean;
  rankScore?: number;
}

const textEncoder = new TextEncoder();
const textDecoder = new TextDecoder();

/** Pack per-icon metadata into a single 32-bit unsigned integer. */
export function packMeta(input: {
  libId: number;
  catId: number;
  styleId: number;
  strokeIdx?: number;
  isFilled?: boolean;
  hasVariants?: boolean;
  rankScore?: number;
}): number {
  const lib = input.libId & 0x1f;
  const cat = (input.catId & 0x0f) << 5;
  const style = (input.styleId & 0x07) << 9;
  const stroke = ((input.strokeIdx ?? 0) & 0x03) << 12;
  const filled = input.isFilled ? 1 << 14 : 0;
  const variants = input.hasVariants ? 1 << 15 : 0;
  const rank = ((input.rankScore ?? 0) & 0xffff) << 16;
  return (lib | cat | style | stroke | filled | variants | rank) >>> 0;
}

/** Unpack a 32-bit `metaPacked` entry into its constituent facet fields. */
export function unpackMeta(packed: number): UnpackedMeta {
  const strokeIdx = (packed >>> 12) & 0x03;
  return {
    libId: packed & 0x1f,
    catId: (packed >>> 5) & 0x0f,
    styleId: (packed >>> 9) & 0x07,
    strokeIdx,
    strokeWidth: STROKE_WIDTH_TABLE[strokeIdx] ?? 0,
    isFilled: ((packed >>> 14) & 0x01) === 1,
    hasVariants: ((packed >>> 15) & 0x01) === 1,
    rankScore: packed >>> 16,
  };
}

/** Pack a posting entry: 24-bit iconIndex + 4-bit matchWeight. */
export function packPosting(iconIndex: number, matchWeight: number): number {
  return ((iconIndex & 0x00ffffff) | ((matchWeight & 0x0f) << 24)) >>> 0;
}

/** Unpack a posting entry into iconIndex and matchWeight. */
export function unpackPosting(entry: number): { iconIndex: number; matchWeight: number } {
  return {
    iconIndex: entry & 0x00ffffff,
    matchWeight: (entry >>> 24) & 0x0f,
  };
}

/** Align a byte offset up to a 4-byte boundary. */
function align4(n: number): number {
  return (n + 3) & ~3;
}

/**
 * Lexicographically compare two UTF-8 byte slices.
 * Returns < 0 if a < b, 0 if equal, > 0 if a > b.
 */
function compareBytes(
  aBuf: Uint8Array,
  aStart: number,
  aEnd: number,
  bBuf: Uint8Array,
  bStart: number,
  bEnd: number,
): number {
  const aLen = aEnd - aStart;
  const bLen = bEnd - bStart;
  const minLen = aLen < bLen ? aLen : bLen;
  for (let i = 0; i < minLen; i++) {
    const diff = aBuf[aStart + i]! - bBuf[bStart + i]!;
    if (diff !== 0) return diff;
  }
  return aLen - bLen;
}

/**
 * Check if slice `haystack[hStart..hEnd)` starts with `needle[0..needle.length)`.
 */
function startsWithBytes(
  haystack: Uint8Array,
  hStart: number,
  hEnd: number,
  needle: Uint8Array,
): boolean {
  const nLen = needle.length;
  if (hEnd - hStart < nLen) return false;
  for (let i = 0; i < nLen; i++) {
    if (haystack[hStart + i]! !== needle[i]!) return false;
  }
  return true;
}

/**
 * Check if slice `haystack[hStart..hEnd)` contains `needle[0..needle.length)`
 * (excluding position 0 since prefix matches are already handled by binary search).
 */
function containsBytesNonPrefix(
  haystack: Uint8Array,
  hStart: number,
  hEnd: number,
  needle: Uint8Array,
): boolean {
  const nLen = needle.length;
  const hLen = hEnd - hStart;
  if (nLen === 0 || hLen <= nLen) return false;
  const first = needle[0]!;
  const limit = hEnd - nLen;
  for (let pos = hStart + 1; pos <= limit; pos++) {
    if (haystack[pos]! !== first) continue;
    let matched = true;
    for (let j = 1; j < nLen; j++) {
      if (haystack[pos + j]! !== needle[j]!) {
        matched = false;
        break;
      }
    }
    if (matched) return true;
  }
  return false;
}

/** Tokenize a query or icon name into lowercase alphanumeric tokens. */
export function tokenize(input: string): string[] {
  const trimmed = input.trim().toLowerCase();
  if (!trimmed) return [];
  const raw = trimmed.split(/[^a-z0-9]+/);
  const out: string[] = [];
  for (let i = 0; i < raw.length; i++) {
    const t = raw[i]!;
    if (t.length > 0) out.push(t);
  }
  return out;
}

/** Parse and validate the 64-byte `search.bin` header. */
export function parseSearchHeader(buffer: ArrayBuffer): SearchHeader {
  if (buffer.byteLength < SEARCH_HEADER_BYTES) {
    throw new Error(
      `Invalid search.bin: buffer too small (${buffer.byteLength} bytes, expected >= ${SEARCH_HEADER_BYTES})`,
    );
  }
  const view = new DataView(buffer);
  const magic = view.getUint32(0, true);
  if (magic !== SEARCH_INDEX_MAGIC) {
    throw new Error(
      `Invalid search.bin magic: 0x${magic.toString(16)} (expected 0x${SEARCH_INDEX_MAGIC.toString(16)})`,
    );
  }
  const version = view.getUint16(4, true);
  if (version !== SEARCH_INDEX_VERSION) {
    throw new Error(
      `Unsupported search.bin version: ${version} (expected ${SEARCH_INDEX_VERSION})`,
    );
  }

  return {
    magic,
    version,
    flags: view.getUint16(6, true),
    iconCount: view.getUint32(8, true),
    vocabCount: view.getUint32(12, true),
    postingsCount: view.getUint32(16, true),
    offMetaPacked: view.getUint32(20, true),
    offNameOffsets: view.getUint32(24, true),
    offNameBuf: view.getUint32(28, true),
    offVocabOffsets: view.getUint32(32, true),
    offVocabBuf: view.getUint32(36, true),
    offPostingsOffsets: view.getUint32(40, true),
    offPostingsIds: view.getUint32(44, true),
  };
}

/**
 * Compile an array of icon metadata records into a spec-compliant `search.bin` ArrayBuffer.
 * Useful for build pipelines and deterministic unit/benchmark tests.
 */
export function buildBinarySearchIndex(icons: readonly BinaryIndexIconInput[]): ArrayBuffer {
  const N = icons.length;
  const metaPacked = new Uint32Array(N);
  const nameOffsets = new Uint32Array(N + 1);

  const encodedNames: Uint8Array[] = new Array(N);
  let totalNameBytes = 0;

  // Map token -> array of packed posting entries
  const postingsMap = new Map<string, number[]>();

  for (let i = 0; i < N; i++) {
    const icon = icons[i]!;
    metaPacked[i] = packMeta(icon);

    const lowerName = icon.name.toLowerCase();
    const nameBytes = textEncoder.encode(lowerName);
    encodedNames[i] = nameBytes;
    nameOffsets[i] = totalNameBytes;
    totalNameBytes += nameBytes.length;

    // Deduplicate tokens per icon keeping highest matchWeight
    const iconTokenWeights = new Map<string, number>();

    // Full name as exact token if single word, plus split name tokens
    const nameTokens = tokenize(lowerName);
    if (nameTokens.length === 1) {
      iconTokenWeights.set(nameTokens[0]!, MATCH_WEIGHT_EXACT_NAME);
    } else {
      for (let t = 0; t < nameTokens.length; t++) {
        const tok = nameTokens[t]!;
        const w = t === 0 ? MATCH_WEIGHT_EXACT_NAME : MATCH_WEIGHT_PREFIX_NAME;
        const prev = iconTokenWeights.get(tok) ?? 0;
        if (w > prev) iconTokenWeights.set(tok, w);
      }
    }

    if (icon.tags) {
      for (let t = 0; t < icon.tags.length; t++) {
        const tagTokens = tokenize(icon.tags[t]!);
        for (let k = 0; k < tagTokens.length; k++) {
          const tok = tagTokens[k]!;
          const prev = iconTokenWeights.get(tok) ?? 0;
          if (MATCH_WEIGHT_TAG > prev) iconTokenWeights.set(tok, MATCH_WEIGHT_TAG);
        }
      }
    }

    for (const [tok, weight] of iconTokenWeights) {
      let list = postingsMap.get(tok);
      if (!list) {
        list = [];
        postingsMap.set(tok, list);
      }
      list.push(packPosting(i, weight));
    }
  }
  nameOffsets[N] = totalNameBytes;

  // Sort vocabulary lexicographically by UTF-8 bytes
  const vocabEntries: { token: string; bytes: Uint8Array; postings: number[] }[] = [];
  for (const [token, postings] of postingsMap) {
    vocabEntries.push({
      token,
      bytes: textEncoder.encode(token),
      postings,
    });
  }
  vocabEntries.sort((a, b) =>
    compareBytes(a.bytes, 0, a.bytes.length, b.bytes, 0, b.bytes.length),
  );

  const V = vocabEntries.length;
  const vocabOffsets = new Uint32Array(V + 1);
  const postingsOffsets = new Uint32Array(V + 1);

  let totalVocabBytes = 0;
  let totalPostings = 0;
  for (let v = 0; v < V; v++) {
    vocabOffsets[v] = totalVocabBytes;
    totalVocabBytes += vocabEntries[v]!.bytes.length;
    postingsOffsets[v] = totalPostings;
    totalPostings += vocabEntries[v]!.postings.length;
  }
  vocabOffsets[V] = totalVocabBytes;
  postingsOffsets[V] = totalPostings;

  // Compute 4-byte aligned section offsets
  const offMetaPacked = SEARCH_HEADER_BYTES;
  const offNameOffsets = offMetaPacked + N * 4;
  const offNameBuf = offNameOffsets + (N + 1) * 4;
  const offVocabOffsets = align4(offNameBuf + totalNameBytes);
  const offVocabBuf = offVocabOffsets + (V + 1) * 4;
  const offPostingsOffsets = align4(offVocabBuf + totalVocabBytes);
  const offPostingsIds = offPostingsOffsets + (V + 1) * 4;
  const totalBytes = offPostingsIds + totalPostings * 4;

  const buffer = new ArrayBuffer(totalBytes);
  const view = new DataView(buffer);
  const u8 = new Uint8Array(buffer);

  // Write 64-byte header
  view.setUint32(0, SEARCH_INDEX_MAGIC, true);
  view.setUint16(4, SEARCH_INDEX_VERSION, true);
  view.setUint16(6, 0, true);
  view.setUint32(8, N, true);
  view.setUint32(12, V, true);
  view.setUint32(16, totalPostings, true);
  view.setUint32(20, offMetaPacked, true);
  view.setUint32(24, offNameOffsets, true);
  view.setUint32(28, offNameBuf, true);
  view.setUint32(32, offVocabOffsets, true);
  view.setUint32(36, offVocabBuf, true);
  view.setUint32(40, offPostingsOffsets, true);
  view.setUint32(44, offPostingsIds, true);

  // Copy typed arrays
  new Uint32Array(buffer, offMetaPacked, N).set(metaPacked);
  new Uint32Array(buffer, offNameOffsets, N + 1).set(nameOffsets);

  let cursor = offNameBuf;
  for (let i = 0; i < N; i++) {
    const b = encodedNames[i]!;
    u8.set(b, cursor);
    cursor += b.length;
  }

  new Uint32Array(buffer, offVocabOffsets, V + 1).set(vocabOffsets);
  cursor = offVocabBuf;
  for (let v = 0; v < V; v++) {
    const b = vocabEntries[v]!.bytes;
    u8.set(b, cursor);
    cursor += b.length;
  }

  new Uint32Array(buffer, offPostingsOffsets, V + 1).set(postingsOffsets);
  const postingsView = new Uint32Array(buffer, offPostingsIds, totalPostings);
  let pCursor = 0;
  for (let v = 0; v < V; v++) {
    const list = vocabEntries[v]!.postings;
    for (let j = 0; j < list.length; j++) {
      postingsView[pCursor++] = list[j]!;
    }
  }

  return buffer;
}

const STYLE_SUFFIX_RE =
  /[-_](filled|fill|outline|outlined|solid|light|bold|thin|duotone|regular|rounded|sharp|two-tone|twotone)$/i;

/**
 * High-performance binary typed-array search engine.
 * Holds zero per-icon JS objects and reuses pre-allocated scratch buffers
 * across queries for < 15ms latency across 134,701+ icons.
 */
export class BinarySearchEngine {
  readonly header: SearchHeader;
  readonly iconCount: number;
  readonly vocabCount: number;
  readonly postingsCount: number;
  readonly byteLength: number;

  // Zero-copy typed-array views over the binary buffer
  readonly metaPacked: Uint32Array;
  readonly nameOffsets: Uint32Array;
  readonly nameBuf: Uint8Array;
  readonly vocabOffsets: Uint32Array;
  readonly vocabBuf: Uint8Array;
  readonly postingsOffsets: Uint32Array;
  readonly postingsIds: Uint32Array;

  // Pre-allocated reusable scratch buffers (zero GC per query)
  private readonly scores: Uint16Array;
  private readonly tokenBestScore: Uint16Array;
  private readonly seenGen: Uint32Array;
  private readonly tokenHits: Uint8Array;
  private readonly touched: Uint32Array;
  private readonly sortScratch: Uint32Array;
  private readonly radixCounts: Uint32Array;
  private queryGen = 0;

  // Precomputed/lazy order arrays for O(N) zero-sort empty-query scans
  private popularityOrder: Uint32Array | null = null;
  private azOrder: Uint32Array | null = null;
  private azRank: Uint32Array | null = null;

  constructor(buffer: ArrayBuffer) {
    const header = parseSearchHeader(buffer);
    this.header = header;
    this.iconCount = header.iconCount;
    this.vocabCount = header.vocabCount;
    this.postingsCount = header.postingsCount;
    this.byteLength = buffer.byteLength;

    const N = header.iconCount;
    const V = header.vocabCount;
    const P = header.postingsCount;

    this.metaPacked = new Uint32Array(buffer, header.offMetaPacked, N);
    this.nameOffsets = new Uint32Array(buffer, header.offNameOffsets, N + 1);
    const nameByteLen = N > 0 ? this.nameOffsets[N]! : 0;
    this.nameBuf = new Uint8Array(buffer, header.offNameBuf, nameByteLen);

    this.vocabOffsets = new Uint32Array(buffer, header.offVocabOffsets, V + 1);
    const vocabByteLen = V > 0 ? this.vocabOffsets[V]! : 0;
    this.vocabBuf = new Uint8Array(buffer, header.offVocabBuf, vocabByteLen);

    this.postingsOffsets = new Uint32Array(buffer, header.offPostingsOffsets, V + 1);
    this.postingsIds = new Uint32Array(buffer, header.offPostingsIds, P);

    // Reusable scratch buffers (~1.9 MB for 134,701 icons)
    this.scores = new Uint16Array(N);
    this.tokenBestScore = new Uint16Array(N);
    this.seenGen = new Uint32Array(N);
    this.tokenHits = new Uint8Array(N);
    this.touched = new Uint32Array(N);
    this.sortScratch = new Uint32Array(N);
    this.radixCounts = new Uint32Array(256);
  }

  /** Decode the icon name at `iconIndex` (intended for diagnostics/concept lookup). */
  getIconName(iconIndex: number): string {
    const start = this.nameOffsets[iconIndex]!;
    const end = this.nameOffsets[iconIndex + 1]!;
    return textDecoder.decode(this.nameBuf.subarray(start, end));
  }

  /** Read the unpacked metadata for `iconIndex`. */
  getIconMeta(iconIndex: number): UnpackedMeta {
    return unpackMeta(this.metaPacked[iconIndex]!);
  }

  /**
   * Execute a search + multi-facet bitmask filter + sort query.
   * Returns freshly sliced `Uint32Array` buffers ready for zero-copy Transferable postMessage.
   */
  query(options: SearchQueryOptions): SearchQueryResult {
    const t0 = performance.now();
    const libMask = (options.libMask ?? 0) >>> 0;
    const catMask = (options.catMask ?? 0) >>> 0;
    const styleMask = (options.styleMask ?? 0) >>> 0;
    const sort: SearchSortMode = options.sort ?? 'relevance';
    const limit = options.limit && options.limit > 0 ? options.limit : 0;

    const libraryCounts = new Uint32Array(LIBRARY_COUNT);
    const categoryCounts = new Uint32Array(CATEGORY_COUNT);
    const styleCounts = new Uint32Array(STYLE_COUNT);

    const tokens = tokenize(options.query);

    if (tokens.length === 0) {
      return this.executeFacetOnlyQuery(
        libMask,
        catMask,
        styleMask,
        sort === 'relevance' ? 'library' : sort,
        limit,
        libraryCounts,
        categoryCounts,
        styleCounts,
        t0,
      );
    }

    return this.executeKeywordQuery(
      tokens,
      options.query.trim().toLowerCase(),
      libMask,
      catMask,
      styleMask,
      sort,
      limit,
      libraryCounts,
      categoryCounts,
      styleCounts,
      t0,
    );
  }

  /**
   * Find cross-library concept matches for a given iconIndex (up to `maxPerLibrary` per library).
   */
  findConceptMatches(iconIndex: number, maxPerLibrary = 2): Uint32Array {
    if (iconIndex < 0 || iconIndex >= this.iconCount) {
      return new Uint32Array(0);
    }
    const sourceMeta = this.metaPacked[iconIndex]!;
    const sourceLib = sourceMeta & 0x1f;
    const rawName = this.getIconName(iconIndex);
    const baseName = rawName.replace(STYLE_SUFFIX_RE, '');
    const res = this.query({
      query: baseName,
      sort: 'relevance',
      limit: 512,
    });

    const perLib = new Uint16Array(LIBRARY_COUNT);
    const out: number[] = [];
    for (let i = 0; i < res.indices.length; i++) {
      const idx = res.indices[i]!;
      if (idx === iconIndex) continue;
      const lib = this.metaPacked[idx]! & 0x1f;
      if (lib === sourceLib) continue;
      if (perLib[lib]! < maxPerLibrary) {
        perLib[lib] = perLib[lib]! + 1;
        out.push(idx);
      }
    }
    return Uint32Array.from(out);
  }

  private executeFacetOnlyQuery(
    libMask: number,
    catMask: number,
    styleMask: number,
    sort: SearchSortMode,
    limit: number,
    libraryCounts: Uint32Array,
    categoryCounts: Uint32Array,
    styleCounts: Uint32Array,
    t0: number,
  ): SearchQueryResult {
    const N = this.iconCount;
    const meta = this.metaPacked;
    const out = this.touched;
    let count = 0;

    // Choose pre-sorted iteration order so zero sorting is needed at query time
    let order: Uint32Array | null = null;
    let reverse = false;
    if (sort === 'popularity' || sort === 'relevance') {
      order = this.ensurePopularityOrder();
    } else if (sort === 'az' || sort === 'alphabetical') {
      order = this.ensureAzOrder();
    } else if (sort === 'za') {
      order = this.ensureAzOrder();
      reverse = true;
    }

    const noFilter = libMask === 0 && catMask === 0 && styleMask === 0;

    if (order === null) {
      // 'library' sort: iterate 0..N-1 (or sort by libId if interleaved)
      for (let i = 0; i < N; i++) {
        const m = meta[i]!;
        const lib = m & 0x1f;
        const cat = (m >>> 5) & 0x0f;
        const style = (m >>> 9) & 0x07;
        if (
          noFilter ||
          ((libMask === 0 || ((1 << lib) & libMask) !== 0) &&
            (catMask === 0 || ((1 << cat) & catMask) !== 0) &&
            (styleMask === 0 || ((1 << style) & styleMask) !== 0))
        ) {
          libraryCounts[lib] = libraryCounts[lib]! + 1;
          categoryCounts[cat] = categoryCounts[cat]! + 1;
          styleCounts[style] = styleCounts[style]! + 1;
          out[count++] = i;
        }
      }
      if (sort === 'library' && count > 1) {
        this.radixSortByLibrary(out, count);
      }
    } else if (!reverse) {
      for (let k = 0; k < N; k++) {
        const i = order[k]!;
        const m = meta[i]!;
        const lib = m & 0x1f;
        const cat = (m >>> 5) & 0x0f;
        const style = (m >>> 9) & 0x07;
        if (
          noFilter ||
          ((libMask === 0 || ((1 << lib) & libMask) !== 0) &&
            (catMask === 0 || ((1 << cat) & catMask) !== 0) &&
            (styleMask === 0 || ((1 << style) & styleMask) !== 0))
        ) {
          libraryCounts[lib] = libraryCounts[lib]! + 1;
          categoryCounts[cat] = categoryCounts[cat]! + 1;
          styleCounts[style] = styleCounts[style]! + 1;
          out[count++] = i;
        }
      }
    } else {
      for (let k = N - 1; k >= 0; k--) {
        const i = order[k]!;
        const m = meta[i]!;
        const lib = m & 0x1f;
        const cat = (m >>> 5) & 0x0f;
        const style = (m >>> 9) & 0x07;
        if (
          noFilter ||
          ((libMask === 0 || ((1 << lib) & libMask) !== 0) &&
            (catMask === 0 || ((1 << cat) & catMask) !== 0) &&
            (styleMask === 0 || ((1 << style) & styleMask) !== 0))
        ) {
          libraryCounts[lib] = libraryCounts[lib]! + 1;
          categoryCounts[cat] = categoryCounts[cat]! + 1;
          styleCounts[style] = styleCounts[style]! + 1;
          out[count++] = i;
        }
      }
    }

    const resultLen = limit > 0 && limit < count ? limit : count;
    const indices = out.slice(0, resultLen);

    return {
      indices,
      totalMatches: count,
      elapsedMs: performance.now() - t0,
      libraryCounts,
      categoryCounts,
      styleCounts,
    };
  }

  private executeKeywordQuery(
    tokens: string[],
    normalizedQuery: string,
    libMask: number,
    catMask: number,
    styleMask: number,
    sort: SearchSortMode,
    limit: number,
    libraryCounts: Uint32Array,
    categoryCounts: Uint32Array,
    styleCounts: Uint32Array,
    t0: number,
  ): SearchQueryResult {
    // Advance generation counter (handles wrap-around safely)
    this.queryGen = (this.queryGen + 1) >>> 0;
    if (this.queryGen === 0) {
      this.seenGen.fill(0);
      this.queryGen = 1;
    }
    const gen = this.queryGen;

    const meta = this.metaPacked;
    const scores = this.scores;
    const tokenBestScore = this.tokenBestScore;
    const seenGen = this.seenGen;
    const tokenHits = this.tokenHits;
    const touched = this.touched;
    const postingsOffsets = this.postingsOffsets;
    const postingsIds = this.postingsIds;
    const vocabOffsets = this.vocabOffsets;
    const vocabBuf = this.vocabBuf;
    const V = this.vocabCount;

    const maxTokens = tokens.length > 16 ? 16 : tokens.length;
    const noFilter = libMask === 0 && catMask === 0 && styleMask === 0;
    let touchedCount = 0;

    for (let t = 0; t < maxTokens; t++) {
      const tokBytes = textEncoder.encode(tokens[t]!);
      const { start: prefixStart, end: prefixEnd } = this.findPrefixRange(tokBytes);

      let matchedPostingsForToken = 0;

      // 1. Score exact + prefix vocab matches from binary-searched range
      for (let v = prefixStart; v < prefixEnd; v++) {
        const vStart = vocabOffsets[v]!;
        const vEnd = vocabOffsets[v + 1]!;
        const isExact = vEnd - vStart === tokBytes.length;
        const vocabMultiplier = isExact ? 8 : 4;

        const pStart = postingsOffsets[v]!;
        const pEnd = postingsOffsets[v + 1]!;
        matchedPostingsForToken += pEnd - pStart;

        for (let p = pStart; p < pEnd; p++) {
          const entry = postingsIds[p]!;
          const idx = entry & 0x00ffffff;
          const weight = (entry >>> 24) & 0x0f;
          const contrib = weight * vocabMultiplier;

          if (t === 0) {
            if (!noFilter) {
              const m = meta[idx]!;
              const lib = m & 0x1f;
              const cat = (m >>> 5) & 0x0f;
              const style = (m >>> 9) & 0x07;
              if (
                (libMask !== 0 && ((1 << lib) & libMask) === 0) ||
                (catMask !== 0 && ((1 << cat) & catMask) === 0) ||
                (styleMask !== 0 && ((1 << style) & styleMask) === 0)
              ) {
                continue;
              }
            }
            if (seenGen[idx] !== gen) {
              seenGen[idx] = gen;
              scores[idx] = contrib;
              tokenBestScore[idx] = contrib;
              tokenHits[idx] = 1;
              touched[touchedCount++] = idx;
            } else if (contrib > tokenBestScore[idx]!) {
              scores[idx] = contrib;
              tokenBestScore[idx] = contrib;
            }
          } else {
            if (seenGen[idx] !== gen) continue;
            const hits = tokenHits[idx]!;
            if (hits === t) {
              tokenHits[idx] = t + 1;
              tokenBestScore[idx] = contrib;
              const sum = scores[idx]! + contrib;
              scores[idx] = sum > 65535 ? 65535 : sum;
            } else if (hits === t + 1 && contrib > tokenBestScore[idx]!) {
              const sum = scores[idx]! - tokenBestScore[idx]! + contrib;
              scores[idx] = sum > 65535 ? 65535 : sum;
              tokenBestScore[idx] = contrib;
            }
          }
        }
      }

      // 2. Substring fallback across vocab tokens (when no prefix hits or >= 3 chars with sparse hits)
      if (
        tokBytes.length >= 2 &&
        (prefixStart === prefixEnd || (tokBytes.length >= 3 && matchedPostingsForToken < 400))
      ) {
        const subMultiplier = 2;
        for (let v = 0; v < V; v++) {
          if (v >= prefixStart && v < prefixEnd) continue;
          const vStart = vocabOffsets[v]!;
          const vEnd = vocabOffsets[v + 1]!;
          if (!containsBytesNonPrefix(vocabBuf, vStart, vEnd, tokBytes)) continue;

          const pStart = postingsOffsets[v]!;
          const pEnd = postingsOffsets[v + 1]!;
          for (let p = pStart; p < pEnd; p++) {
            const entry = postingsIds[p]!;
            const idx = entry & 0x00ffffff;
            const weight = (entry >>> 24) & 0x0f;
            const contrib = weight * subMultiplier;

            if (t === 0) {
              if (!noFilter) {
                const m = meta[idx]!;
                const lib = m & 0x1f;
                const cat = (m >>> 5) & 0x0f;
                const style = (m >>> 9) & 0x07;
                if (
                  (libMask !== 0 && ((1 << lib) & libMask) === 0) ||
                  (catMask !== 0 && ((1 << cat) & catMask) === 0) ||
                  (styleMask !== 0 && ((1 << style) & styleMask) === 0)
                ) {
                  continue;
                }
              }
              if (seenGen[idx] !== gen) {
                seenGen[idx] = gen;
                scores[idx] = contrib;
                tokenBestScore[idx] = contrib;
                tokenHits[idx] = 1;
                touched[touchedCount++] = idx;
              } else if (contrib > tokenBestScore[idx]!) {
                scores[idx] = contrib;
                tokenBestScore[idx] = contrib;
              }
            } else {
              if (seenGen[idx] !== gen) continue;
              const hits = tokenHits[idx]!;
              if (hits === t) {
                tokenHits[idx] = t + 1;
                tokenBestScore[idx] = contrib;
                const sum = scores[idx]! + contrib;
                scores[idx] = sum > 65535 ? 65535 : sum;
              } else if (hits === t + 1 && contrib > tokenBestScore[idx]!) {
                const sum = scores[idx]! - tokenBestScore[idx]! + contrib;
                scores[idx] = sum > 65535 ? 65535 : sum;
                tokenBestScore[idx] = contrib;
              }
            }
          }
        }
      }

      if (t === 0 && touchedCount === 0) {
        return {
          indices: new Uint32Array(0),
          totalMatches: 0,
          elapsedMs: performance.now() - t0,
          libraryCounts,
          categoryCounts,
          styleCounts,
        };
      }
    }

    // 3. Compact matched indices (AND across all tokens) & compute facet counts
    const queryBytes = textEncoder.encode(normalizedQuery);
    const nameOffsets = this.nameOffsets;
    const nameBuf = this.nameBuf;
    let matchCount = 0;

    for (let i = 0; i < touchedCount; i++) {
      const idx = touched[i]!;
      if (tokenHits[idx] !== maxTokens) continue;

      const m = meta[idx]!;
      const lib = m & 0x1f;
      const cat = (m >>> 5) & 0x0f;
      const style = (m >>> 9) & 0x07;
      libraryCounts[lib] = libraryCounts[lib]! + 1;
      categoryCounts[cat] = categoryCounts[cat]! + 1;
      styleCounts[style] = styleCounts[style]! + 1;

      // Exact full-name or name-prefix boost
      const nStart = nameOffsets[idx]!;
      const nEnd = nameOffsets[idx + 1]!;
      if (startsWithBytes(nameBuf, nStart, nEnd, queryBytes)) {
        const bonus = nEnd - nStart === queryBytes.length ? 64 : 24;
        const boosted = scores[idx]! + bonus;
        scores[idx] = boosted > 65535 ? 65535 : boosted;
      }

      touched[matchCount++] = idx;
    }

    if (matchCount === 0) {
      return {
        indices: new Uint32Array(0),
        totalMatches: 0,
        elapsedMs: performance.now() - t0,
        libraryCounts,
        categoryCounts,
        styleCounts,
      };
    }

    // 4. Sort matched indices
    this.sortMatchedIndices(touched, matchCount, sort);

    const resultLen = limit > 0 && limit < matchCount ? limit : matchCount;
    const indices = touched.slice(0, resultLen);

    return {
      indices,
      totalMatches: matchCount,
      elapsedMs: performance.now() - t0,
      libraryCounts,
      categoryCounts,
      styleCounts,
    };
  }

  /**
   * Binary search `vocabBuf` for all tokens starting with `prefixBytes`.
   * Returns half-open range `[start, end)`.
   */
  private findPrefixRange(prefixBytes: Uint8Array): { start: number; end: number } {
    const V = this.vocabCount;
    if (V === 0 || prefixBytes.length === 0) return { start: 0, end: 0 };

    const offsets = this.vocabOffsets;
    const buf = this.vocabBuf;

    // Lower bound: first vocab entry >= prefixBytes
    let lo = 0;
    let hi = V;
    while (lo < hi) {
      const mid = (lo + hi) >>> 1;
      const cmp = compareBytes(
        buf,
        offsets[mid]!,
        offsets[mid + 1]!,
        prefixBytes,
        0,
        prefixBytes.length,
      );
      if (cmp < 0) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    const start = lo;

    // Upper bound: first vocab entry that does NOT start with prefixBytes
    hi = V;
    while (lo < hi) {
      const mid = (lo + hi) >>> 1;
      if (startsWithBytes(buf, offsets[mid]!, offsets[mid + 1]!, prefixBytes)) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return { start, end: lo };
  }

  /** Sort `arr[0..count)` in place according to `sort`. */
  private sortMatchedIndices(arr: Uint32Array, count: number, sort: SearchSortMode): void {
    if (count <= 1) return;

    if (sort === 'relevance') {
      if (count <= 2048) {
        const sub = arr.subarray(0, count);
        const scores = this.scores;
        const meta = this.metaPacked;
        sub.sort((a, b) => {
          const sd = scores[b]! - scores[a]!;
          if (sd !== 0) return sd;
          const rd = (meta[b]! >>> 16) - (meta[a]! >>> 16);
          if (rd !== 0) return rd;
          return a - b;
        });
      } else {
        // Stable LSD radix sort: first by rankScore desc, then by score desc
        this.radixSort16Desc(arr, count, (idx) => this.metaPacked[idx]! >>> 16);
        this.radixSort16Desc(arr, count, (idx) => this.scores[idx]!);
      }
      return;
    }

    if (sort === 'popularity') {
      if (count <= 2048) {
        const sub = arr.subarray(0, count);
        const scores = this.scores;
        const meta = this.metaPacked;
        sub.sort((a, b) => {
          const rd = (meta[b]! >>> 16) - (meta[a]! >>> 16);
          if (rd !== 0) return rd;
          const sd = scores[b]! - scores[a]!;
          if (sd !== 0) return sd;
          return a - b;
        });
      } else {
        this.radixSort16Desc(arr, count, (idx) => this.scores[idx]!);
        this.radixSort16Desc(arr, count, (idx) => this.metaPacked[idx]! >>> 16);
      }
      return;
    }

    if (sort === 'library') {
      this.radixSortByLibrary(arr, count);
      return;
    }

    if (sort === 'az' || sort === 'alphabetical' || sort === 'za') {
      const rank = this.ensureAzRank();
      const sub = arr.subarray(0, count);
      if (sort === 'za') {
        sub.sort((a, b) => rank[b]! - rank[a]!);
      } else {
        sub.sort((a, b) => rank[a]! - rank[b]!);
      }
    }
  }

  /**
   * 2-pass 8-bit LSD radix sort descending by a 16-bit unsigned key.
   * O(N) time (~1.2 ms for 134,701 items), zero allocations.
   */
  private radixSort16Desc(
    arr: Uint32Array,
    count: number,
    keyFn: (idx: number) => number,
  ): void {
    const scratch = this.sortScratch;
    const counts = this.radixCounts;

    // Pass 1: low 8 bits (inverted for descending order)
    counts.fill(0);
    for (let i = 0; i < count; i++) {
      const k = 255 - (keyFn(arr[i]!) & 0xff);
      counts[k] = counts[k]! + 1;
    }
    let sum = 0;
    for (let b = 0; b < 256; b++) {
      const c = counts[b]!;
      counts[b] = sum;
      sum += c;
    }
    for (let i = 0; i < count; i++) {
      const idx = arr[i]!;
      const k = 255 - (keyFn(idx) & 0xff);
      scratch[counts[k]!] = idx;
      counts[k] = counts[k]! + 1;
    }

    // Pass 2: high 8 bits (inverted for descending order)
    counts.fill(0);
    for (let i = 0; i < count; i++) {
      const k = 255 - ((keyFn(scratch[i]!) >>> 8) & 0xff);
      counts[k] = counts[k]! + 1;
    }
    sum = 0;
    for (let b = 0; b < 256; b++) {
      const c = counts[b]!;
      counts[b] = sum;
      sum += c;
    }
    for (let i = 0; i < count; i++) {
      const idx = scratch[i]!;
      const k = 255 - ((keyFn(idx) >>> 8) & 0xff);
      arr[counts[k]!] = idx;
      counts[k] = counts[k]! + 1;
    }
  }

  /** Counting sort ascending by libId (0..27), preserving relative order within each library. */
  private radixSortByLibrary(arr: Uint32Array, count: number): void {
    const scratch = this.sortScratch;
    const counts = this.radixCounts;
    const meta = this.metaPacked;

    counts.fill(0, 0, LIBRARY_COUNT);
    for (let i = 0; i < count; i++) {
      const lib = meta[arr[i]!]! & 0x1f;
      counts[lib] = counts[lib]! + 1;
    }
    let sum = 0;
    for (let b = 0; b < LIBRARY_COUNT; b++) {
      const c = counts[b]!;
      counts[b] = sum;
      sum += c;
    }
    for (let i = 0; i < count; i++) {
      const idx = arr[i]!;
      const lib = meta[idx]! & 0x1f;
      scratch[counts[lib]!] = idx;
      counts[lib] = counts[lib]! + 1;
    }
    arr.set(scratch.subarray(0, count), 0);
  }

  private ensurePopularityOrder(): Uint32Array {
    if (this.popularityOrder) return this.popularityOrder;
    const N = this.iconCount;
    const order = new Uint32Array(N);
    for (let i = 0; i < N; i++) order[i] = i;
    if (N > 1) {
      this.radixSort16Desc(order, N, (idx) => this.metaPacked[idx]! >>> 16);
    }
    this.popularityOrder = order;
    return order;
  }

  private ensureAzOrder(): Uint32Array {
    if (this.azOrder) return this.azOrder;
    const N = this.iconCount;
    const order = new Uint32Array(N);
    for (let i = 0; i < N; i++) order[i] = i;
    const offsets = this.nameOffsets;
    const buf = this.nameBuf;
    order.sort((a, b) => {
      const cmp = compareBytes(buf, offsets[a]!, offsets[a + 1]!, buf, offsets[b]!, offsets[b + 1]!);
      return cmp !== 0 ? cmp : a - b;
    });
    this.azOrder = order;

    const rank = new Uint32Array(N);
    for (let i = 0; i < N; i++) {
      rank[order[i]!] = i;
    }
    this.azRank = rank;
    return order;
  }

  private ensureAzRank(): Uint32Array {
    if (!this.azRank) {
      this.ensureAzOrder();
    }
    return this.azRank!;
  }
}
