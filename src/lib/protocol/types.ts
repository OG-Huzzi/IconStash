/**
 * IconStash v2 Protocol Types & Schema Constants
 * Matches docs/architecture.md Sections 4, 5, and 6.
 */

// ---------------------------------------------------------------------------
// Schema Constants
// ---------------------------------------------------------------------------

export const CHUNK_SCHEMA_VERSION = 1 as const;
export const CHUNK_SIZE_CAP = 4000;
export const MEGA_LIBRARY_THRESHOLD = 8000;

/** Little-endian ASCII "ICS2" (0x49, 0x43, 0x53, 0x32) */
export const SEARCH_INDEX_MAGIC = 0x32534349;
export const SEARCH_INDEX_VERSION = 1;
export const SEARCH_INDEX_HEADER_BYTES = 64;

export const STROKE_WIDTH_TABLE = [0, 1, 1.5, 2] as const;
export type StrokeWidthValue = (typeof STROKE_WIDTH_TABLE)[number];

/** Chunk icon tuple flags bitmask (docs/architecture.md §4.2) */
export const IconChunkFlags = {
  IS_FILLED: 1 << 0,
  HAS_VARIANTS: 1 << 1,
  HAS_ANIMATED_ELEMENTS: 1 << 2,
} as const;

/** Posting match weights packed into bits 24..27 of postingsIds (docs/architecture.md §5.1) */
export const PostingMatchWeight = {
  TAG_OR_SYNONYM: 1,
  PREFIX_OR_SUBTOKEN: 2,
  EXACT_NAME: 4,
} as const;

// ---------------------------------------------------------------------------
// Section 4: Sharded Per-Library Chunk Schema (/chunks/v1/*.json)
// ---------------------------------------------------------------------------

/**
 * 5-element positional tuple for a single icon inside a library chunk:
 * [0] name        - Canonical icon name
 * [1] svgBody     - Build-time normalized inner SVG markup
 * [2] viewBoxIdx  - Index into chunk.viewBoxes[]
 * [3] strokeWidth - 0 for filled/solid; 1 | 1.5 | 2 for stroke icons
 * [4] flags       - Bitmask (IconChunkFlags)
 */
export type ChunkIconTuple = [
  name: string,
  svgBody: string,
  viewBoxIdx: number,
  strokeWidth: number,
  flags: number,
];

export interface LibraryChunk {
  schemaVersion: typeof CHUNK_SCHEMA_VERSION;
  librarySlug: string;
  libraryName: string;
  libraryId: number;
  version: string;
  license: string;
  attributionRequired: boolean;
  npmPackage: string;
  docsUrlBase: string;
  defaultViewBox: string;
  defaultStrokeWidth: number;
  part: number;
  totalParts: number;
  startIndex: number;
  count: number;
  viewBoxes: string[];
  icons: ChunkIconTuple[];
  /** Optional map of localOffset (stringified integer) -> canonical icon id when id !== `${librarySlug}-${name}` */
  idOverrides?: Record<string, string>;
}

export interface ChunkShardManifestEntry {
  url: string;
  start: number;
  count: number;
  bytes: number;
  sha256: string;
}

export interface LibraryManifestEntry {
  id: number;
  slug: string;
  name: string;
  count: number;
  startIndex: number;
  endIndex: number;
  shards: ChunkShardManifestEntry[];
}

export interface ChunkManifest {
  schemaVersion: typeof CHUNK_SCHEMA_VERSION;
  generatedAt: string;
  contentHash: string;
  totalIcons: number;
  chunkSizeCap: number;
  libraries: LibraryManifestEntry[];
}

export interface ResolvedShardLocation {
  library: LibraryManifestEntry;
  shard: ChunkShardManifestEntry;
  shardIndex: number;
  localOffset: number;
}

// ---------------------------------------------------------------------------
// Section 5: Binary Search Index Schema (/index/v1/search.bin & search-meta.json)
// ---------------------------------------------------------------------------

export interface SearchIndexHeader {
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

export interface ParsedSearchIndex {
  header: SearchIndexHeader;
  metaPacked: Uint32Array;
  nameOffsets: Uint32Array;
  nameBuf: Uint8Array;
  vocabOffsets: Uint32Array;
  vocabBuf: Uint8Array;
  postingsOffsets: Uint32Array;
  postingsIds: Uint32Array;
  byteLength: number;
}

export interface IconMetaFields {
  libId: number;
  catId: number;
  styleId: number;
  strokeIdx: number;
  isFilled: boolean;
  hasVariants: boolean;
  rankScore: number;
}

export interface DecodedIconMeta extends IconMetaFields {
  strokeWidth: StrokeWidthValue;
}

export interface SearchMetaLibrary {
  id: number;
  slug: string;
  name: string;
  count: number;
  startIndex: number;
  endIndex: number;
  tier: number;
  color: string;
  version: string;
  license: string;
  attributionRequired: boolean;
  npmPackage: string;
  docsUrl: string;
}

export interface SearchMeta {
  schemaVersion: typeof CHUNK_SCHEMA_VERSION;
  generatedAt: string;
  contentHash: string;
  totalIcons: number;
  vocabCount: number;
  postingsCount: number;
  indexBytes: number;
  libraries: SearchMetaLibrary[];
  categories: string[];
  subCategories: string[];
  styles: string[];
  strokeWidths: number[];
  viewBoxes: string[];
  counts: {
    byLibrary: number[];
    byCategory: number[];
    byStyle: number[];
  };
}

// ---------------------------------------------------------------------------
// Section 6: Web Worker Message Protocols
// ---------------------------------------------------------------------------

export type SearchSortMode = 'relevance' | 'az' | 'za' | 'library';

/** Main Thread -> Search Worker */
export type SearchWorkerRequest =
  | { type: 'INIT'; indexUrl: string; metaUrl: string }
  | {
      type: 'QUERY';
      queryId: number;
      query: string;
      libMask: number;   // 28-bit bitmask (0 = all libraries)
      catMask: number;   // 16-bit bitmask (0 = all categories)
      styleMask: number; // 7-bit bitmask  (0 = all styles)
      sort: SearchSortMode;
      limit?: number;    // 0 = return all matching indices (default)
    }
  | {
      type: 'CONCEPT_MATCHES';
      queryId: number;
      iconIndex: number;
      maxPerLibrary?: number;
    }
  | { type: 'CANCEL'; queryId: number };

/** Search Worker -> Main Thread */
export type SearchWorkerResponse =
  | { type: 'READY'; iconCount: number; indexBytes: number; initMs: number }
  | {
      type: 'RESULTS';
      queryId: number;
      indices: Uint32Array;       // Transferred buffer (zero-copy)
      totalMatches: number;
      elapsedMs: number;
      libraryCounts: Uint32Array; // 28-element facet counts (transferred)
    }
  | {
      type: 'CONCEPT_MATCHES';
      queryId: number;
      indices: Uint32Array;       // Cross-library matching iconIndices (transferred)
    }
  | { type: 'ERROR'; queryId?: number; message: string };

export interface ExportSvgInput {
  id: string;
  name: string;
  librarySlug: string;
  svgMarkup: string;
}

/** Main Thread -> Export Worker */
export type ExportWorkerRequest =
  | {
      type: 'EXPORT_PNG';
      jobId: number;
      svgMarkup: string;
      filename: string;
      size: number;        // 16..2048 px
      scale?: number;      // 1 | 2 | 3
      background?: string; // 'transparent' | hex
    }
  | {
      type: 'EXPORT_ZIP';
      jobId: number;
      icons: ExportSvgInput[]; // Capped at 200 icons per archive
      pngSizes: number[];      // e.g. [64, 256] or []
      includeManifest: boolean;
      filename: string;
    }
  | { type: 'CANCEL'; jobId: number };

/** Export Worker -> Main Thread */
export type ExportWorkerResponse =
  | { type: 'PROGRESS'; jobId: number; completed: number; total: number }
  | {
      type: 'COMPLETE';
      jobId: number;
      filename: string;
      mimeType: string;
      buffer: ArrayBuffer; // Transferred buffer (zero-copy)
    }
  | { type: 'ERROR'; jobId: number; message: string };
