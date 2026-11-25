/// <reference types="svelte" />
/**
 * Explorer State Store (Svelte 5 Runes)
 *
 * Manages search query, 28-library / 16-category / 7-style bitmask facets,
 * sort order, worker-backed typed-array search results, and bounded 5-chunk
 * RAM LRU hydration via `ChunkLRUCache`.
 *
 * Singleton `search.worker.ts` lives on `globalThis.__ICONSTASH_SEARCH_WORKER__`
 * so Astro View Transitions reuse the loaded binary index without re-fetching.
 */

import {
  ChunkLRUCache,
  type LibraryChunkPayload,
  type PinnedIconRecord,
} from '../cache/chunk-lru';
import { resolveShardForIcon } from '../protocol/binary';
import {
  IconChunkFlags,
  type ChunkManifest,
  type SearchMeta,
  type SearchSortMode,
} from '../protocol/types';
import type { IconSvgInput } from '../svg/types';
import type {
  SearchWorkerRequest,
  SearchWorkerResponse,
} from '../../workers/search.worker';

export interface ResolvedIcon extends IconSvgInput {
  iconIndex?: number;
  id: string;
  name: string;
  svgPath?: string;
  svgBody?: string;
  viewBox?: string;
  strokeWidth?: number;
  flags?: number;
  isFilled?: boolean;
  hasVariants?: boolean;
  hasAnimatedElements?: boolean;
  libraryId?: number;
  library?: string;
  libraryName?: string;
  librarySlug?: string;
  version?: string;
  license?: string;
  attributionRequired?: boolean;
  npmPackage?: string;
  docsUrl?: string;
  docsUrlBase?: string;
  style?: string;
  category?: string;
  tags?: string[];
}

export interface InitExplorerOptions {
  initialLibrary?: string;
  initialCategory?: string;
  initialStyle?: string;
  initialQuery?: string;
}

interface PendingConceptRequest {
  resolve: (indices: Uint32Array) => void;
  reject: (err: Error) => void;
}

interface SearchWorkerSingleton {
  worker: Worker | null;
  ready: boolean;
  initPromise: Promise<void> | null;
  nextQueryId: number;
  activeQueryId: number;
  manifest: ChunkManifest | null;
  meta: SearchMeta | null;
  metaPromise: Promise<{ manifest: ChunkManifest; meta: SearchMeta }> | null;
  chunkCache: ChunkLRUCache<LibraryChunkPayload>;
  visibleIcons: Map<number, ResolvedIcon>;
  pendingConcept: Map<number, PendingConceptRequest>;
  pendingAdhocQuery: Map<number, PendingConceptRequest>;
  onResults: ((msg: Extract<SearchWorkerResponse, { type: 'RESULTS' }>) => void) | null;
  onError: ((msg: Extract<SearchWorkerResponse, { type: 'ERROR' }>) => void) | null;
}

declare global {
  var __ICONSTASH_SEARCH_WORKER__: SearchWorkerSingleton | undefined;
}

const DEFAULT_INDEX_URL = '/index/v1/search.bin';
const DEFAULT_META_URL = '/index/v1/search-meta.json';
const DEFAULT_MANIFEST_URL = '/chunks/v1/manifest.json';
const MAX_RAM_CHUNKS = 6;
const MAX_RAM_BYTES = 24 * 1024 * 1024;
const MAX_VISIBLE_ICON_CACHE = 1200;
const QUERY_DEBOUNCE_MS = 60;

const BASE_NAME_SUFFIX_RE =
  /(?:[-_](?:outline|regular|solid|filled|fill|bold|duotone|thin|light|sharp|round|linear|twotone|two-tone|24|20|16|12))+$/i;

export function sanitizeSearchQuery(raw: string): string {
  return String(raw || '')
    .replace(/<[^>]*>/g, ' ')
    .replace(/javascript:/gi, '')
    .replace(/[^a-zA-Z0-9\s\-_]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, 100);
}

export function extractConceptBaseName(name: string): string {
  const cleaned = String(name || '')
    .trim()
    .toLowerCase()
    .replace(BASE_NAME_SUFFIX_RE, '')
    .trim();
  return cleaned || String(name || '').trim().toLowerCase();
}

function getSingleton(): SearchWorkerSingleton {
  if (!globalThis.__ICONSTASH_SEARCH_WORKER__) {
    globalThis.__ICONSTASH_SEARCH_WORKER__ = {
      worker: null,
      ready: false,
      initPromise: null,
      nextQueryId: 1,
      activeQueryId: 0,
      manifest: null,
      meta: null,
      metaPromise: null,
      chunkCache: new ChunkLRUCache<LibraryChunkPayload>({
        maxChunks: MAX_RAM_CHUNKS,
        maxBytes: MAX_RAM_BYTES,
      }),
      visibleIcons: new Map(),
      pendingConcept: new Map(),
      pendingAdhocQuery: new Map(),
      onResults: null,
      onError: null,
    };
  }
  return globalThis.__ICONSTASH_SEARCH_WORKER__;
}

function decodeResolvedIcon(
  chunk: LibraryChunkPayload,
  iconIndex: number,
  localOffset: number,
): ResolvedIcon | null {
  const tuple = chunk.icons[localOffset];
  if (!tuple) return null;

  const [name, svgBody, viewBoxIdx, strokeWidth, flags] = tuple;
  const id = chunk.idOverrides?.[String(localOffset)] ?? `${chunk.librarySlug}-${name}`;
  const viewBox = chunk.viewBoxes[viewBoxIdx] ?? chunk.defaultViewBox ?? '0 0 24 24';
  const isFilled = (flags & IconChunkFlags.IS_FILLED) !== 0;
  const hasVariants = (flags & IconChunkFlags.HAS_VARIANTS) !== 0;
  const hasAnimatedElements = (flags & IconChunkFlags.HAS_ANIMATED_ELEMENTS) !== 0;
  const docsUrl = chunk.docsUrlBase
    ? `${chunk.docsUrlBase.replace(/\/+$/, '')}/${encodeURIComponent(name)}`
    : '';

  return {
    iconIndex,
    id,
    name,
    svgPath: svgBody,
    svgBody,
    viewBox,
    strokeWidth: strokeWidth || chunk.defaultStrokeWidth || 0,
    flags,
    isFilled,
    hasVariants,
    hasAnimatedElements,
    libraryId: chunk.libraryId,
    library: chunk.libraryName,
    libraryName: chunk.libraryName,
    librarySlug: chunk.librarySlug,
    version: chunk.version,
    license: chunk.license,
    attributionRequired: chunk.attributionRequired,
    npmPackage: chunk.npmPackage,
    docsUrl,
    docsUrlBase: chunk.docsUrlBase,
  };
}

class ExplorerStore {
  query = $state('');
  selectedLibMask = $state(0);
  selectedCatMask = $state(0);
  selectedStyleMask = $state(0);
  sort = $state<SearchSortMode>('relevance');

  resultIndices = $state.raw<Uint32Array>(new Uint32Array(0));
  totalMatches = $state(0);
  libraryCounts = $state.raw<Uint32Array>(new Uint32Array(28));
  categoryCounts = $state.raw<Uint32Array>(new Uint32Array(16));
  styleCounts = $state.raw<Uint32Array>(new Uint32Array(7));

  loading = $state(false);
  ready = $state(false);
  error = $state<string | null>(null);
  elapsedMs = $state(0);

  manifest = $state.raw<ChunkManifest | null>(null);
  meta = $state.raw<SearchMeta | null>(null);

  /** Incremented whenever a new chunk enters RAM so virtual rows re-read synchronously. */
  chunkVersion = $state(0);

  private queryTimer: ReturnType<typeof setTimeout> | null = null;

  constructor() {
    const singleton = getSingleton();
    if (singleton.manifest) this.manifest = singleton.manifest;
    if (singleton.meta) {
      this.meta = singleton.meta;
      this.seedCountsFromMeta(singleton.meta);
    }
    if (singleton.ready) {
      this.ready = true;
    }
  }

  private seedCountsFromMeta(meta: SearchMeta): void {
    if (meta.counts?.byLibrary?.length) {
      const libs = new Uint32Array(28);
      for (let i = 0; i < Math.min(28, meta.counts.byLibrary.length); i++) {
        libs[i] = meta.counts.byLibrary[i];
      }
      this.libraryCounts = libs;
    }
    if (meta.counts?.byCategory?.length) {
      const cats = new Uint32Array(16);
      for (let i = 0; i < Math.min(16, meta.counts.byCategory.length); i++) {
        cats[i] = meta.counts.byCategory[i];
      }
      this.categoryCounts = cats;
    }
    if (meta.counts?.byStyle?.length) {
      const styles = new Uint32Array(7);
      for (let i = 0; i < Math.min(7, meta.counts.byStyle.length); i++) {
        styles[i] = meta.counts.byStyle[i];
      }
      this.styleCounts = styles;
    }
  }

  private bindWorkerCallbacks(): void {
    const singleton = getSingleton();
    singleton.onResults = (msg) => {
      if (msg.queryId !== singleton.activeQueryId) return;
      this.resultIndices = msg.indices;
      this.totalMatches = msg.totalMatches;
      this.elapsedMs = msg.elapsedMs;
      this.libraryCounts = msg.libraryCounts;
      this.categoryCounts = msg.categoryCounts;
      this.styleCounts = msg.styleCounts;
      this.loading = false;
      this.error = null;
    };
    singleton.onError = (msg) => {
      if (msg.queryId !== undefined && msg.queryId !== singleton.activeQueryId) return;
      this.error = msg.message;
      this.loading = false;
    };
  }

  private async ensureManifestAndMeta(): Promise<{
    manifest: ChunkManifest;
    meta: SearchMeta;
  }> {
    const singleton = getSingleton();
    if (singleton.manifest && singleton.meta) {
      this.manifest = singleton.manifest;
      this.meta = singleton.meta;
      return { manifest: singleton.manifest, meta: singleton.meta };
    }

    if (!singleton.metaPromise) {
      singleton.metaPromise = (async () => {
        const [manifestRes, metaRes] = await Promise.all([
          fetch(DEFAULT_MANIFEST_URL),
          fetch(DEFAULT_META_URL),
        ]);
        if (!manifestRes.ok) {
          throw new Error(`Failed to fetch chunk manifest (${manifestRes.status})`);
        }
        if (!metaRes.ok) {
          throw new Error(`Failed to fetch search metadata (${metaRes.status})`);
        }
        const [manifest, meta] = (await Promise.all([
          manifestRes.json(),
          metaRes.json(),
        ])) as [ChunkManifest, SearchMeta];

        singleton.manifest = manifest;
        singleton.meta = meta;
        void singleton.chunkCache.setContentHash(manifest.contentHash).catch(() => {
          // IndexedDB may be unavailable in restricted/private contexts
        });
        return { manifest, meta };
      })().catch((err) => {
        singleton.metaPromise = null;
        throw err;
      });
    }

    const loaded = await singleton.metaPromise;
    this.manifest = loaded.manifest;
    this.meta = loaded.meta;
    this.seedCountsFromMeta(loaded.meta);
    return loaded;
  }

  private async ensureWorkerReady(): Promise<Worker> {
    const singleton = getSingleton();
    if (singleton.worker && singleton.ready) {
      return singleton.worker;
    }

    if (typeof Worker === 'undefined') {
      throw new Error('Web Workers are unavailable in this environment.');
    }

    if (!singleton.worker) {
      const worker = new Worker(
        new URL('../../workers/search.worker.ts', import.meta.url),
        { type: 'module' },
      );

      worker.addEventListener('message', (event: MessageEvent<SearchWorkerResponse>) => {
        const msg = event.data;
        if (!msg) return;

        if (msg.type === 'RESULTS') {
          const adhoc = singleton.pendingAdhocQuery.get(msg.queryId);
          if (adhoc) {
            singleton.pendingAdhocQuery.delete(msg.queryId);
            adhoc.resolve(msg.indices);
            return;
          }
          singleton.onResults?.(msg);
          return;
        }

        if (msg.type === 'CONCEPT_MATCHES') {
          const pending = singleton.pendingConcept.get(msg.queryId);
          if (pending) {
            singleton.pendingConcept.delete(msg.queryId);
            pending.resolve(msg.indices);
          }
          return;
        }

        if (msg.type === 'ERROR') {
          if (msg.queryId !== undefined) {
            const pendingConcept = singleton.pendingConcept.get(msg.queryId);
            if (pendingConcept) {
              singleton.pendingConcept.delete(msg.queryId);
              pendingConcept.reject(new Error(msg.message));
              return;
            }
            const pendingAdhoc = singleton.pendingAdhocQuery.get(msg.queryId);
            if (pendingAdhoc) {
              singleton.pendingAdhocQuery.delete(msg.queryId);
              pendingAdhoc.reject(new Error(msg.message));
              return;
            }
          }
          singleton.onError?.(msg);
        }
      });

      singleton.worker = worker;
    }

    if (!singleton.initPromise) {
      const worker = singleton.worker;
      singleton.initPromise = new Promise<void>((resolve, reject) => {
        const onInitMessage = (event: MessageEvent<SearchWorkerResponse>) => {
          const msg = event.data;
          if (!msg) return;
          if (msg.type === 'READY') {
            worker.removeEventListener('message', onInitMessage);
            worker.removeEventListener('error', onInitError);
            singleton.ready = true;
            resolve();
          } else if (msg.type === 'ERROR' && msg.queryId === undefined) {
            worker.removeEventListener('message', onInitMessage);
            worker.removeEventListener('error', onInitError);
            reject(new Error(msg.message));
          }
        };
        const onInitError = (event: ErrorEvent) => {
          worker.removeEventListener('message', onInitMessage);
          worker.removeEventListener('error', onInitError);
          reject(new Error(event.message || 'Search worker failed to initialize.'));
        };

        worker.addEventListener('message', onInitMessage);
        worker.addEventListener('error', onInitError);

        const initReq: SearchWorkerRequest = {
          type: 'INIT',
          indexUrl: DEFAULT_INDEX_URL,
          metaUrl: DEFAULT_META_URL,
        };
        worker.postMessage(initReq);
      }).catch((err) => {
        singleton.initPromise = null;
        throw err;
      });
    }

    await singleton.initPromise;
    return singleton.worker!;
  }

  async initExplorer(opts: InitExplorerOptions = {}): Promise<void> {
    if (typeof window === 'undefined') return;
    this.loading = true;
    this.error = null;
    this.bindWorkerCallbacks();

    try {
      // Fetch tiny manifest + meta first so the initial grid has zero bandwidth
      // contention against the 6.7 MB search.bin index on slow links.
      const { manifest, meta } = await this.ensureManifestAndMeta();

      if (opts.initialQuery !== undefined) {
        this.query = sanitizeSearchQuery(opts.initialQuery);
      } else {
        this.query = '';
      }

      if (opts.initialLibrary) {
        const slug = opts.initialLibrary.trim().toLowerCase();
        const lib = meta.libraries.find((l) => l.slug.toLowerCase() === slug);
        this.selectedLibMask = lib ? (1 << lib.id) >>> 0 : 0;
      } else {
        this.selectedLibMask = 0;
      }

      if (opts.initialCategory) {
        const target = opts.initialCategory.trim().toLowerCase();
        const catIdx = meta.categories.findIndex((c) => c.toLowerCase() === target);
        this.selectedCatMask = catIdx >= 0 ? (1 << catIdx) >>> 0 : 0;
      } else {
        this.selectedCatMask = 0;
      }

      if (opts.initialStyle) {
        const target = opts.initialStyle.trim().toLowerCase();
        const styleIdx = meta.styles.findIndex((s) => s.toLowerCase() === target);
        this.selectedStyleMask = styleIdx >= 0 ? (1 << styleIdx) >>> 0 : 0;
      } else {
        this.selectedStyleMask = 0;
      }

      const canFastSeed =
        !this.query &&
        this.selectedCatMask === 0 &&
        this.selectedStyleMask === 0 &&
        this.sort === 'relevance';

      if (canFastSeed) {
        const seeded = this.buildSeedIndicesFromManifest(manifest, opts.initialLibrary);
        this.resultIndices = seeded;
        this.totalMatches = seeded.length;
        this.loading = false;
        this.ready = true;

        // Give the first visible icon chunk full network bandwidth (capped at 400ms),
        // then stream the full 6.7 MB search.bin index in the background worker.
        if (seeded.length > 0) {
          const firstWarm = this.ensureChunksForIndices(
            Array.from(seeded.subarray(0, Math.min(120, seeded.length))),
          );
          await Promise.race([firstWarm, new Promise<void>((r) => setTimeout(r, 400))]);
        }

        const seededLibMask = this.selectedLibMask;
        await this.ensureWorkerReady();
        if (
          this.query ||
          this.selectedCatMask !== 0 ||
          this.selectedStyleMask !== 0 ||
          this.sort !== 'relevance' ||
          this.selectedLibMask !== seededLibMask
        ) {
          this.dispatchQuery();
        }
        return;
      }

      await this.ensureWorkerReady();
      this.ready = true;
      this.dispatchQuery();
    } catch (err) {
      this.error = err instanceof Error ? err.message : String(err);
      this.loading = false;
    }
  }

  private buildSeedIndicesFromManifest(
    manifest: ChunkManifest,
    initialLibrary?: string,
  ): Uint32Array {
    if (initialLibrary) {
      const target = initialLibrary.trim().toLowerCase();
      const lib = manifest.libraries.find((l) => l.slug.toLowerCase() === target);
      if (lib && lib.count > 0) {
        const out = new Uint32Array(lib.count);
        for (let i = 0; i < lib.count; i++) {
          out[i] = lib.startIndex + i;
        }
        return out;
      }
    }
    const total = manifest.totalIcons;
    const out = new Uint32Array(total);
    for (let i = 0; i < total; i++) {
      out[i] = i;
    }
    return out;
  }

  private dispatchQuery(): void {
    const singleton = getSingleton();
    if (!singleton.worker || !singleton.ready) {
      void this.ensureWorkerReady()
        .then(() => {
          if (singleton.ready) this.dispatchQuery();
        })
        .catch(() => {});
      return;
    }

    if (singleton.activeQueryId > 0) {
      const cancelMsg: SearchWorkerRequest = {
        type: 'CANCEL',
        queryId: singleton.activeQueryId,
      };
      singleton.worker.postMessage(cancelMsg);
    }

    const queryId = singleton.nextQueryId++;
    singleton.activeQueryId = queryId;
    this.loading = true;

    const req: SearchWorkerRequest = {
      type: 'QUERY',
      queryId,
      query: this.query,
      libMask: this.selectedLibMask,
      catMask: this.selectedCatMask,
      styleMask: this.selectedStyleMask,
      sort: this.sort,
      limit: 0,
    };
    singleton.worker.postMessage(req);
  }

  private scheduleQuery(immediate = false): void {
    if (this.queryTimer !== null) {
      clearTimeout(this.queryTimer);
      this.queryTimer = null;
    }
    if (immediate) {
      this.dispatchQuery();
      return;
    }
    this.queryTimer = setTimeout(() => {
      this.queryTimer = null;
      this.dispatchQuery();
    }, QUERY_DEBOUNCE_MS);
  }

  setQuery(q: string): void {
    const clean = sanitizeSearchQuery(q);
    if (clean === this.query) return;
    this.query = clean;
    this.scheduleQuery(clean.length === 0);
  }

  toggleLibrary(idx: number): void {
    if (idx < 0 || idx >= 28) return;
    this.selectedLibMask = (this.selectedLibMask ^ (1 << idx)) >>> 0;
    this.scheduleQuery(true);
  }

  selectSingleLibrary(slug: string | null): void {
    if (!slug || slug === 'all') {
      this.selectedLibMask = 0;
      this.scheduleQuery(true);
      return;
    }
    const target = slug.trim().toLowerCase();
    const lib =
      this.meta?.libraries.find((l) => l.slug.toLowerCase() === target) ??
      this.manifest?.libraries.find((l) => l.slug.toLowerCase() === target);
    this.selectedLibMask = lib ? (1 << lib.id) >>> 0 : 0;
    this.scheduleQuery(true);
  }

  toggleCategory(idx: number): void {
    if (idx < 0 || idx >= 16) return;
    this.selectedCatMask = (this.selectedCatMask ^ (1 << idx)) >>> 0;
    this.scheduleQuery(true);
  }

  toggleStyle(idx: number): void {
    if (idx < 0 || idx >= 7) return;
    this.selectedStyleMask = (this.selectedStyleMask ^ (1 << idx)) >>> 0;
    this.scheduleQuery(true);
  }

  clearStyles(): void {
    if (this.selectedStyleMask === 0) return;
    this.selectedStyleMask = 0;
    this.scheduleQuery(true);
  }

  setSort(s: string): void {
    const valid: readonly SearchSortMode[] = ['relevance', 'az', 'za', 'library'];
    const next: SearchSortMode = (valid as readonly string[]).includes(s)
      ? (s as SearchSortMode)
      : 'relevance';
    if (next === this.sort) return;
    this.sort = next;
    this.scheduleQuery(true);
  }

  clearFilters(): void {
    this.query = '';
    this.selectedLibMask = 0;
    this.selectedCatMask = 0;
    this.selectedStyleMask = 0;
    this.sort = 'relevance';
    this.scheduleQuery(true);
  }

  /**
   * Synchronous Tier-1 RAM lookup from `ChunkLRUCache` (zero network / zero IDB).
   * Returns `null` if the icon's shard is not currently resident in RAM.
   */
  getIconPayload(iconIndex: number): ResolvedIcon | null {
    const sg = getSingleton();
    const cached = sg.visibleIcons.get(iconIndex);
    if (cached) return cached;
    const manifest = this.manifest;
    if (!manifest || iconIndex < 0) return null;

    const loc = resolveShardForIcon(manifest, iconIndex);
    if (!loc) return null;

    const chunk = getSingleton().chunkCache.get(loc.shard.url);
    if (!chunk) return null;

    return decodeResolvedIcon(chunk, iconIndex, loc.localOffset);
  }

  /**
   * Two-tier async hydration (RAM LRU -> IndexedDB -> Network) for a single icon.
   */
  async ensureChunkForIcon(
    iconIndex: number,
    signal?: AbortSignal,
  ): Promise<ResolvedIcon | null> {
    if (!this.manifest) {
      await this.ensureManifestAndMeta();
    }
    const manifest = this.manifest;
    if (!manifest || iconIndex < 0) return null;

    const loc = resolveShardForIcon(manifest, iconIndex);
    if (!loc) return null;

    const cache = getSingleton().chunkCache;
    const existing = cache.get(loc.shard.url);
    if (existing) {
      return decodeResolvedIcon(existing, iconIndex, loc.localOffset);
    }

    const chunk = await cache.load(loc.shard.url, { signal });
    this.chunkVersion++;
    return decodeResolvedIcon(chunk, iconIndex, loc.localOffset);
  }

  /**
   * Batch-hydrates all unique shards needed for a set of visible icon indices.
   * Respects the 5-chunk LRU cap and aborts cleanly on fast scroll-away.
   */
  async ensureChunksForIndices(
    iconIndices: readonly number[],
    signal?: AbortSignal,
  ): Promise<void> {
    const manifest = this.manifest;
    if (!manifest || iconIndices.length === 0) return;

    const sg = getSingleton();
    const cache = sg.chunkCache;
    const vMap = sg.visibleIcons;

    const byShardUrl = new Map<string, Array<{ iconIndex: number; localOffset: number }>>();
    const urlsToLoad: string[] = [];

    for (let i = 0; i < iconIndices.length; i++) {
      const idx = iconIndices[i];
      if (vMap.has(idx)) continue;
      const loc = resolveShardForIcon(manifest, idx);
      if (!loc) continue;

      const existing = cache.get(loc.shard.url);
      if (existing) {
        const decoded = decodeResolvedIcon(existing, idx, loc.localOffset);
        if (decoded) {
          vMap.set(idx, decoded);
          if (vMap.size > MAX_VISIBLE_ICON_CACHE) {
            const firstKey = vMap.keys().next().value;
            if (firstKey !== undefined) vMap.delete(firstKey);
          }
        }
        continue;
      }

      let list = byShardUrl.get(loc.shard.url);
      if (!list) {
        list = [];
        byShardUrl.set(loc.shard.url, list);
        urlsToLoad.push(loc.shard.url);
      }
      list.push({ iconIndex: idx, localOffset: loc.localOffset });
    }

    if (urlsToLoad.length === 0) return;

    for (let b = 0; b < urlsToLoad.length; b += 4) {
      if (signal?.aborted) return;
      const batch = urlsToLoad.slice(b, b + 4);
      let loadedInBatch = false;

      await Promise.allSettled(
        batch.map(async (url) => {
          try {
            const chunk = await cache.load(url, { signal });
            if (signal?.aborted || !chunk) return;
            const items = byShardUrl.get(url);
            if (items) {
              for (let j = 0; j < items.length; j++) {
                const { iconIndex, localOffset } = items[j];
                const decoded = decodeResolvedIcon(chunk, iconIndex, localOffset);
                if (decoded) {
                  vMap.set(iconIndex, decoded);
                  if (vMap.size > MAX_VISIBLE_ICON_CACHE) {
                    const firstKey = vMap.keys().next().value;
                    if (firstKey !== undefined) vMap.delete(firstKey);
                  }
                }
              }
            }
            loadedInBatch = true;
          } catch (err) {
            if (err instanceof Error && err.name === 'AbortError') return;
          }
        }),
      );

      if (loadedInBatch && !signal?.aborted) {
        this.chunkVersion++;
      }
    }
  }

  /**
   * Finds cross-library concept matches for an icon name (e.g. "home", "arrow-right").
   * Uses the search worker's concept-matching engine and hydrates up to 48 matches.
   */
  pinIcon(icon: ResolvedIcon): void {
    const rec: PinnedIconRecord = {
      iconIndex: icon.iconIndex ?? -1,
      flags: icon.flags ?? 0,
      id: icon.id,
      name: icon.name,
      svgBody: icon.svgBody ?? '',
      viewBox: icon.viewBox ?? '0 0 24 24',
      strokeWidth: icon.strokeWidth ?? 2,
      librarySlug: icon.librarySlug ?? '',
      libraryName: icon.libraryName ?? '',
    };
    getSingleton().chunkCache.pinIcon(rec);
  }

  getPinnedIcon(id: string): PinnedIconRecord | undefined {
    return getSingleton().chunkCache.getPinnedIcon(id);
  }

  async findConceptMatches(name: string): Promise<ResolvedIcon[]> {
    const base = extractConceptBaseName(name);
    if (!base) return [];

    await this.ensureManifestAndMeta();
    const worker = await this.ensureWorkerReady();
    const singleton = getSingleton();

    const seedQueryId = singleton.nextQueryId++;
    const seedIndices = await new Promise<Uint32Array>((resolve, reject) => {
      singleton.pendingAdhocQuery.set(seedQueryId, { resolve, reject });
      const req: SearchWorkerRequest = {
        type: 'QUERY',
        queryId: seedQueryId,
        query: base,
        libMask: 0,
        catMask: 0,
        styleMask: 0,
        sort: 'relevance',
        limit: 80,
      };
      worker.postMessage(req);
    });

    let matchIndices: Uint32Array = seedIndices;

    if (seedIndices.length > 0) {
      const conceptQueryId = singleton.nextQueryId++;
      try {
        const conceptIndices = await new Promise<Uint32Array>((resolve, reject) => {
          singleton.pendingConcept.set(conceptQueryId, { resolve, reject });
          const req: SearchWorkerRequest = {
            type: 'CONCEPT_MATCHES',
            queryId: conceptQueryId,
            iconIndex: seedIndices[0],
            maxPerLibrary: 2,
          };
          worker.postMessage(req);
        });
        if (conceptIndices.length > 0) {
          matchIndices = conceptIndices;
        }
      } catch {
        // Fall back to seedIndices if CONCEPT_MATCHES fails
      }
    }

    const manifest = this.manifest;
    if (!manifest || matchIndices.length === 0) return [];

    const cappedCount = Math.min(matchIndices.length, 48);
    const byShard = new Map<string, number[]>();
    for (let i = 0; i < cappedCount; i++) {
      const idx = matchIndices[i];
      const loc = resolveShardForIcon(manifest, idx);
      if (!loc) continue;
      let list = byShard.get(loc.shard.url);
      if (!list) {
        list = [];
        byShard.set(loc.shard.url, list);
      }
      list.push(idx);
    }

    const resolvedMap = new Map<number, ResolvedIcon>();
    const cache = singleton.chunkCache;

    for (const [shardUrl, indices] of byShard.entries()) {
      try {
        const chunk = await cache.load(shardUrl);
        for (const idx of indices) {
          const loc = resolveShardForIcon(manifest, idx);
          if (!loc) continue;
          const icon = decodeResolvedIcon(chunk, idx, loc.localOffset);
          if (icon) {
            resolvedMap.set(idx, icon);
            this.pinIcon(icon);
          }
        }
      } catch {
        // Skip shards that fail to load
      }
    }

    const ordered: ResolvedIcon[] = [];
    for (let i = 0; i < cappedCount; i++) {
      const icon = resolvedMap.get(matchIndices[i]);
      if (icon) ordered.push(icon);
    }
    return ordered;
  }

  getChunkCache(): ChunkLRUCache<LibraryChunkPayload> {
    return getSingleton().chunkCache;
  }

  disposeTimers(): void {
    if (this.queryTimer !== null) {
      clearTimeout(this.queryTimer);
      this.queryTimer = null;
    }
  }
}

export const explorerState = new ExplorerStore();

if (typeof window !== "undefined") {
  window.addEventListener("pagehide", () => {
    const sg = globalThis.__ICONSTASH_SEARCH_WORKER__;
    if (sg?.worker) {
      sg.worker.terminate();
      sg.worker = null;
      sg.ready = false;
    }
  });
}
