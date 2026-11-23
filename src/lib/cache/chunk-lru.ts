/**
 * Strict Bounded LRU Chunk Cache with Two-Tier IndexedDB Persistence
 * (`docs/memory-budget.md` §3.1–3.2).
 *
 * Guarantees:
 * - Holds at most `maxChunks` (default 5, configurable 4–6) library chunks in
 *   JS RAM AND stays within `maxBytes` (default 28 MB).
 * - O(1) LRU promotion and eviction via ES `Map` insertion order.
 * - Evicting a chunk from RAM NEVER deletes it from IndexedDB, so scrolling
 *   back to a previously visited library re-hydrates locally with zero network.
 * - Deduplicates concurrent in-flight fetches for the same chunk URL with
 *   ref-counted `AbortSignal` support.
 * - Tracks hits, IDB hits, misses, evictions, and estimated JS heap bytes.
 */

import {
  createIdbChunkStore,
  makeChunkStorageKey,
  type ChunkPersistenceStore,
} from './idb-store.js';

export const DEFAULT_MAX_CHUNKS = 5;
export const MIN_CONFIGURABLE_CHUNKS = 4;
export const MAX_CONFIGURABLE_CHUNKS = 6;
export const DEFAULT_MAX_BYTES = 28 * 1024 * 1024; // 28 MB desktop ceiling
export const MOBILE_MAX_BYTES = 16 * 1024 * 1024; // 16 MB mobile ceiling
export const MAX_PINNED_ICONS = 50;

/** Compact 5-element icon tuple from `/chunks/v1/{library}.json` (`docs/architecture.md` §4.2). */
export type IconChunkTuple = [
  name: string,
  svgBody: string,
  viewBoxIdx: number,
  strokeWidth: number,
  flags: number,
];

export interface LibraryChunkPayload {
  schemaVersion: number;
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
  icons: IconChunkTuple[];
  idOverrides?: Record<string, string>;
}

export interface PinnedIconRecord {
  id: string;
  iconIndex: number;
  name: string;
  svgBody: string;
  viewBox: string;
  strokeWidth: number;
  flags: number;
  librarySlug: string;
  libraryName: string;
}

export interface ChunkCacheStats {
  hits: number;
  idbHits: number;
  misses: number;
  evictions: number;
  residentChunks: number;
  estimatedBytes: number;
  maxChunks: number;
  maxBytes: number;
  inFlightCount: number;
}

export interface ChunkLRUCacheOptions<T = LibraryChunkPayload> {
  /** Max resident chunks in RAM (clamped to 4..6 by default unless `allowUnclamped` is set). */
  maxChunks?: number;
  /** Max estimated JS heap bytes in RAM (default 28 MB). */
  maxBytes?: number;
  /** Content hash prefix for IndexedDB cache-busting (e.g. manifest.contentHash). */
  contentHash?: string;
  /** Optional persistence backend (defaults to `createIdbChunkStore()`). */
  idbStore?: ChunkPersistenceStore<T>;
  /** Optional custom fetch function (defaults to `globalThis.fetch`). */
  fetchImpl?: typeof fetch;
  /** Optional custom byte-size estimator for payloads. */
  estimateBytes?: (payload: T) => number;
  /** Optional eviction callback (for telemetry/testing). */
  onEvict?: (key: string, byteSize: number) => void;
}

interface ResidentEntry<T> {
  payload: T;
  byteSize: number;
}

interface InFlightEntry<T> {
  promise: Promise<T>;
  controller: AbortController;
  subscribers: number;
}

/**
 * Determine adaptive RAM limits based on device memory and viewport width
 * (`docs/memory-budget.md` §3.1).
 */
export function resolveAdaptiveCacheLimits(): { maxChunks: number; maxBytes: number } {
  const nav =
    typeof navigator !== 'undefined'
      ? (navigator as Navigator & { deviceMemory?: number })
      : undefined;
  const win = typeof window !== 'undefined' ? window : undefined;

  const lowMemory = typeof nav?.deviceMemory === 'number' && nav.deviceMemory < 4;
  const narrowViewport = typeof win?.innerWidth === 'number' && win.innerWidth < 768;

  if (lowMemory || narrowViewport) {
    return { maxChunks: MIN_CONFIGURABLE_CHUNKS, maxBytes: MOBILE_MAX_BYTES };
  }
  return { maxChunks: MAX_CONFIGURABLE_CHUNKS, maxBytes: DEFAULT_MAX_BYTES };
}

/**
 * Estimate in-memory V8 JS heap footprint (bytes) of a chunk payload.
 * Strings in V8 occupy ~2 bytes/char (UTF-16) plus small header/tuple overhead.
 */
export function estimateChunkHeapBytes(payload: unknown): number {
  if (payload == null) return 0;

  if (typeof payload === 'string') {
    return payload.length * 2 + 32;
  }

  // Fast path for canonical LibraryChunkPayload
  if (
    typeof payload === 'object' &&
    'icons' in payload &&
    Array.isArray((payload as LibraryChunkPayload).icons)
  ) {
    const chunk = payload as LibraryChunkPayload;
    let bytes = 512; // Header metadata + viewBoxes
    const icons = chunk.icons;
    for (let i = 0; i < icons.length; i++) {
      const tuple = icons[i];
      if (Array.isArray(tuple)) {
        const nameLen = typeof tuple[0] === 'string' ? tuple[0].length : 0;
        const svgLen = typeof tuple[1] === 'string' ? tuple[1].length : 0;
        // 2 bytes/char for UTF-16 strings + ~96 B V8 array & element slot overhead
        bytes += (nameLen + svgLen) * 2 + 96;
      }
    }
    return bytes;
  }

  // Generic fallback for arbitrary JSON objects
  try {
    return JSON.stringify(payload).length * 2 + 64;
  } catch {
    return 1024;
  }
}

export class ChunkLRUCache<T = LibraryChunkPayload> {
  readonly maxChunks: number;
  readonly maxBytes: number;
  private contentHash: string;
  private readonly idbStore: ChunkPersistenceStore<T>;
  private readonly fetchImpl: typeof fetch;
  private readonly estimateBytesFn: (payload: T) => number;
  private readonly onEvict?: (key: string, byteSize: number) => void;

  // ES Map maintains insertion order: oldest = first key, newest (MRU) = last key
  private readonly entries = new Map<string, ResidentEntry<T>>();
  private readonly inFlight = new Map<string, InFlightEntry<T>>();
  private readonly pinnedIcons = new Map<string, PinnedIconRecord>();

  private estimatedBytes = 0;
  private hits = 0;
  private idbHits = 0;
  private misses = 0;
  private evictions = 0;

  constructor(options: ChunkLRUCacheOptions<T> = {}) {
    const requestedChunks = options.maxChunks ?? DEFAULT_MAX_CHUNKS;
    this.maxChunks = Math.min(
      MAX_CONFIGURABLE_CHUNKS,
      Math.max(MIN_CONFIGURABLE_CHUNKS, Math.floor(requestedChunks)),
    );
    this.maxBytes = Math.min(
      DEFAULT_MAX_BYTES,
      Math.max(1024, Math.floor(options.maxBytes ?? DEFAULT_MAX_BYTES)),
    );
    this.contentHash = options.contentHash ?? 'v1';
    this.idbStore = options.idbStore ?? createIdbChunkStore<T>();
    this.fetchImpl = options.fetchImpl ?? ((...args) => globalThis.fetch(...args));
    this.estimateBytesFn = options.estimateBytes ?? estimateChunkHeapBytes;
    this.onEvict = options.onEvict;
  }

  /** Update active manifest contentHash and prune outdated IndexedDB entries. */
  async setContentHash(contentHash: string): Promise<number> {
    this.contentHash = contentHash;
    return this.idbStore.pruneStaleHashes(contentHash);
  }

  /**
   * Synchronous Tier-1 RAM lookup.
   * Promotes the entry to Most-Recently-Used on hit.
   */
  get(key: string): T | undefined {
    const entry = this.entries.get(key);
    if (!entry) return undefined;
    // O(1) LRU promotion
    this.entries.delete(key);
    this.entries.set(key, entry);
    this.hits++;
    return entry.payload;
  }

  /** Check whether `key` is currently resident in RAM without mutating LRU order. */
  has(key: string): boolean {
    return this.entries.has(key);
  }

  /** List currently resident chunk keys from LRU (oldest) to MRU (newest). */
  keys(): string[] {
    return Array.from(this.entries.keys());
  }

  /**
   * Insert or update a chunk in RAM, enforcing strict `maxChunks` and `maxBytes`
   * eviction policies. Does NOT remove evicted entries from IndexedDB.
   */
  set(key: string, payload: T, explicitByteSize?: number): void {
    const byteSize =
      explicitByteSize !== undefined
        ? Math.max(0, explicitByteSize)
        : this.estimateBytesFn(payload);

    const existing = this.entries.get(key);
    if (existing) {
      this.estimatedBytes -= existing.byteSize;
      this.entries.delete(key);
    }

    // Evict LRU entries BEFORE inserting if inserting would exceed capacity
    while (
      this.entries.size > 0 &&
      (this.entries.size >= this.maxChunks || this.estimatedBytes + byteSize > this.maxBytes)
    ) {
      this.evictOldest();
    }

    this.entries.set(key, { payload, byteSize });
    this.estimatedBytes += byteSize;

    // Post-insert guard in case maxChunks/maxBytes still exceeded
    while (
      this.entries.size > 1 &&
      (this.entries.size > this.maxChunks || this.estimatedBytes > this.maxBytes)
    ) {
      this.evictOldest();
    }
  }

  /**
   * Two-tier load with in-flight request deduplication:
   * 1. Tier 1: RAM LRU (`< 0.05 ms`)
   * 2. Deduplicated in-flight promise (shared across concurrent callers)
   * 3. Tier 2: IndexedDB (`iconstash-v2`, zero network)
   * 4. Tier 3: Network `fetch(shardUrl)` -> persisted to IndexedDB + cached in RAM
   */
  async load(shardUrl: string, options: { signal?: AbortSignal } = {}): Promise<T> {
    const signal = options.signal;
    if (signal?.aborted) {
      throw createAbortError();
    }

    // Tier 1: RAM LRU hit
    const ramHit = this.get(shardUrl);
    if (ramHit !== undefined) {
      return ramHit;
    }

    // Check for an active in-flight load for this exact shardUrl
    let flight = this.inFlight.get(shardUrl);
    if (!flight) {
      const controller = new AbortController();
      const promise = this.loadFromIdbOrNetwork(shardUrl, controller.signal).finally(() => {
        if (this.inFlight.get(shardUrl)?.promise === promise) {
          this.inFlight.delete(shardUrl);
        }
      });
      flight = { promise, controller, subscribers: 0 };
      this.inFlight.set(shardUrl, flight);
    }

    flight.subscribers++;
    return this.attachSubscriber(flight, signal);
  }

  /** Evict all chunks from RAM (leaves IndexedDB intact). */
  clearRam(): void {
    this.entries.clear();
    this.estimatedBytes = 0;
  }

  /** Pin a single icon record so Inspector/Compare survives chunk eviction (max 50). */
  pinIcon(record: PinnedIconRecord): void {
    if (this.pinnedIcons.has(record.id)) {
      this.pinnedIcons.delete(record.id);
    } else if (this.pinnedIcons.size >= MAX_PINNED_ICONS) {
      const oldest = this.pinnedIcons.keys().next().value;
      if (oldest !== undefined) this.pinnedIcons.delete(oldest);
    }
    this.pinnedIcons.set(record.id, record);
  }

  /** Retrieve a pinned icon record (promotes it in the pinned LRU). */
  getPinnedIcon(id: string): PinnedIconRecord | undefined {
    const rec = this.pinnedIcons.get(id);
    if (!rec) return undefined;
    this.pinnedIcons.delete(id);
    this.pinnedIcons.set(id, rec);
    return rec;
  }

  /** Remove a pinned icon record. */
  unpinIcon(id: string): void {
    this.pinnedIcons.delete(id);
  }

  /** Return live cache telemetry and memory metrics. */
  getStats(): ChunkCacheStats {
    return {
      hits: this.hits,
      idbHits: this.idbHits,
      misses: this.misses,
      evictions: this.evictions,
      residentChunks: this.entries.size,
      estimatedBytes: this.estimatedBytes,
      maxChunks: this.maxChunks,
      maxBytes: this.maxBytes,
      inFlightCount: this.inFlight.size,
    };
  }

  private evictOldest(): void {
    const oldestKey = this.entries.keys().next().value;
    if (oldestKey === undefined) return;
    const oldest = this.entries.get(oldestKey)!;
    this.entries.delete(oldestKey);
    this.estimatedBytes = Math.max(0, this.estimatedBytes - oldest.byteSize);
    this.evictions++;
    this.onEvict?.(oldestKey, oldest.byteSize);
  }

  private async loadFromIdbOrNetwork(shardUrl: string, signal: AbortSignal): Promise<T> {
    const storageKey = makeChunkStorageKey(this.contentHash, shardUrl);

    // Tier 2: IndexedDB lookup
    const persisted = await this.idbStore.get(storageKey);
    if (signal.aborted) {
      throw createAbortError();
    }
    if (persisted !== undefined) {
      this.idbHits++;
      this.set(shardUrl, persisted);
      return persisted;
    }

    // Tier 3: Network fetch
    this.misses++;
    const response = await this.fetchImpl(shardUrl, { signal });
    if (!response.ok) {
      throw new Error(
        `Failed to fetch chunk (${response.status} ${response.statusText}): ${shardUrl}`,
      );
    }
    const payload = (await response.json()) as T;
    if (signal.aborted) {
      throw createAbortError();
    }

    const byteSize = this.estimateBytesFn(payload);
    // Persist to IndexedDB so future RAM evictions re-hydrate without network
    await this.idbStore.set(storageKey, payload, byteSize);
    this.set(shardUrl, payload, byteSize);
    return payload;
  }

  private attachSubscriber(flight: InFlightEntry<T>, signal?: AbortSignal): Promise<T> {
    if (!signal) {
      return flight.promise.finally(() => {
        flight.subscribers = Math.max(0, flight.subscribers - 1);
      });
    }

    return new Promise<T>((resolve, reject) => {
      let settled = false;

      const onAbort = () => {
        if (settled) return;
        settled = true;
        flight.subscribers = Math.max(0, flight.subscribers - 1);
        if (flight.subscribers === 0) {
          flight.controller.abort();
        }
        reject(createAbortError());
      };

      if (signal.aborted) {
        onAbort();
        return;
      }

      signal.addEventListener('abort', onAbort, { once: true });

      flight.promise.then(
        (value) => {
          if (settled) return;
          settled = true;
          signal.removeEventListener('abort', onAbort);
          flight.subscribers = Math.max(0, flight.subscribers - 1);
          resolve(value);
        },
        (err) => {
          if (settled) return;
          settled = true;
          signal.removeEventListener('abort', onAbort);
          flight.subscribers = Math.max(0, flight.subscribers - 1);
          reject(err);
        },
      );
    });
  }
}

function createAbortError(): Error {
  const err = new Error('The operation was aborted.');
  err.name = 'AbortError';
  return err;
}
