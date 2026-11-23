import { describe, expect, it, vi } from 'vitest';
import {
  ChunkLRUCache,
  DEFAULT_MAX_BYTES,
  DEFAULT_MAX_CHUNKS,
  MAX_PINNED_ICONS,
  estimateChunkHeapBytes,
  type LibraryChunkPayload,
} from '../../src/lib/cache/chunk-lru.js';
import {
  createIdbChunkStore,
  makeChunkStorageKey,
} from '../../src/lib/cache/idb-store.js';

function makeMockChunk(
  slug: string,
  iconCount = 50,
  svgBodySize = 120,
): LibraryChunkPayload {
  const svgBody = `<path d="${'M0 0 '.repeat(Math.ceil(svgBodySize / 5)).slice(0, svgBodySize)}"/>`;
  const icons: LibraryChunkPayload['icons'] = [];
  for (let i = 0; i < iconCount; i++) {
    icons.push([`${slug}-icon-${i}`, svgBody, 0, 2, 0]);
  }
  return {
    schemaVersion: 1,
    librarySlug: slug,
    libraryName: slug.toUpperCase(),
    libraryId: 0,
    version: '1.0.0',
    license: 'MIT',
    attributionRequired: false,
    npmPackage: slug,
    docsUrlBase: `https://example.com/${slug}/`,
    defaultViewBox: '0 0 24 24',
    defaultStrokeWidth: 2,
    part: 0,
    totalParts: 1,
    startIndex: 0,
    count: iconCount,
    viewBoxes: ['0 0 24 24'],
    icons,
  };
}

function makeJsonResponse(payload: unknown, status = 200): Response {
  return new Response(JSON.stringify(payload), {
    status,
    headers: { 'content-type': 'application/json' },
  });
}

describe('idb-store (graceful fallback & quota hygiene)', () => {
  it('falls back gracefully to in-memory store when IndexedDB is unavailable', async () => {
    const store = createIdbChunkStore<{ ok: boolean }>({ maxEntries: 5 });
    expect(store.backend).toBe('memory');

    const key = makeChunkStorageKey('abc123', '/chunks/v1/lucide.json');
    await store.set(key, { ok: true }, 1024);
    expect(await store.has(key)).toBe(true);
    expect(await store.get(key)).toEqual({ ok: true });
    expect(await store.keys()).toEqual([key]);
  });

  it('prunes stale contentHash keys and enforces maxEntries quota', async () => {
    const store = createIdbChunkStore<number>({ maxEntries: 3, forceMemory: true });
    await store.set('oldhash:/chunks/v1/a.json', 1);
    await store.set('newhash:/chunks/v1/b.json', 2);
    await store.set('newhash:/chunks/v1/c.json', 3);

    const pruned = await store.pruneStaleHashes('newhash');
    expect(pruned).toBe(1);
    expect(await store.keys()).toEqual([
      'newhash:/chunks/v1/b.json',
      'newhash:/chunks/v1/c.json',
    ]);

    // Exceed maxEntries=3; oldest accessed entry should be evicted
    await new Promise((r) => setTimeout(r, 5));
    await store.get('newhash:/chunks/v1/b.json'); // refresh b
    await store.set('newhash:/chunks/v1/d.json', 4);
    await store.set('newhash:/chunks/v1/e.json', 5);

    const keys = await store.keys();
    expect(keys.length).toBe(3);
    expect(keys).not.toContain('newhash:/chunks/v1/c.json');
  });
});

describe('ChunkLRUCache (strict bounded 4–6 chunk RAM LRU + IDB)', () => {
  it('defaults to maxChunks=5 and clamps configurable maxChunks to 4..6', () => {
    const def = new ChunkLRUCache();
    expect(def.maxChunks).toBe(DEFAULT_MAX_CHUNKS);
    expect(def.maxBytes).toBe(DEFAULT_MAX_BYTES);

    const low = new ChunkLRUCache({ maxChunks: 1 });
    expect(low.maxChunks).toBe(4);

    const high = new ChunkLRUCache({ maxChunks: 20 });
    expect(high.maxChunks).toBe(6);
  });

  it('never exceeds maxChunks and evicts least-recently-used entries in O(1)', () => {
    const evicted: string[] = [];
    const cache = new ChunkLRUCache<LibraryChunkPayload>({
      maxChunks: 5,
      onEvict: (key) => evicted.push(key),
    });

    for (let i = 0; i < 12; i++) {
      cache.set(`/chunks/v1/lib-${i}.json`, makeMockChunk(`lib-${i}`, 10));
      expect(cache.getStats().residentChunks).toBeLessThanOrEqual(5);
    }

    expect(cache.getStats().residentChunks).toBe(5);
    expect(cache.getStats().evictions).toBe(7);
    expect(evicted.slice(0, 7)).toEqual([
      '/chunks/v1/lib-0.json',
      '/chunks/v1/lib-1.json',
      '/chunks/v1/lib-2.json',
      '/chunks/v1/lib-3.json',
      '/chunks/v1/lib-4.json',
      '/chunks/v1/lib-5.json',
      '/chunks/v1/lib-6.json',
    ]);

    // Promote lib-7 (oldest resident) via get(), then insert lib-12 -> lib-8 must be evicted
    expect(cache.get('/chunks/v1/lib-7.json')).toBeDefined();
    cache.set('/chunks/v1/lib-12.json', makeMockChunk('lib-12', 10));
    expect(cache.has('/chunks/v1/lib-7.json')).toBe(true);
    expect(cache.has('/chunks/v1/lib-8.json')).toBe(false);
    expect(cache.getStats().residentChunks).toBe(5);
    expect(cache.getStats().hits).toBe(1);
  });

  it('enforces maxBytes RAM ceiling even when residentChunks < maxChunks', () => {
    const cache = new ChunkLRUCache<LibraryChunkPayload>({
      maxChunks: 6,
      maxBytes: 100_000, // 100 KB cap for test
    });

    // Each chunk explicitly sized at 40 KB -> at most 2 fit in 100 KB
    for (let i = 0; i < 5; i++) {
      cache.set(`/chunks/v1/heavy-${i}.json`, makeMockChunk(`heavy-${i}`, 5), 40_000);
      expect(cache.getStats().estimatedBytes).toBeLessThanOrEqual(100_000);
      expect(cache.getStats().residentChunks).toBeLessThanOrEqual(2);
    }

    expect(cache.getStats().estimatedBytes).toBe(80_000);
    expect(cache.getStats().evictions).toBe(3);
  });

  it('preserves evicted chunks in IndexedDB and re-hydrates with zero network fetches', async () => {
    const idbStore = createIdbChunkStore<LibraryChunkPayload>({ forceMemory: true });
    const fetchMock = vi.fn(async (input: RequestInfo | URL) => {
      const url = String(input);
      const slug = url.replace('/chunks/v1/', '').replace('.json', '');
      return makeJsonResponse(makeMockChunk(slug, 20));
    });

    const cache = new ChunkLRUCache<LibraryChunkPayload>({
      maxChunks: 4,
      contentHash: 'hash-v2',
      idbStore,
      fetchImpl: fetchMock as unknown as typeof fetch,
    });

    // Load 6 distinct chunks (each hits network once; first 2 evicted from RAM)
    for (let i = 0; i < 6; i++) {
      await cache.load(`/chunks/v1/lib-${i}.json`);
    }
    expect(fetchMock).toHaveBeenCalledTimes(6);
    expect(cache.getStats().residentChunks).toBe(4);
    expect(cache.getStats().evictions).toBe(2);
    expect(cache.has('/chunks/v1/lib-0.json')).toBe(false);

    // Re-load evicted lib-0: must come from IndexedDB with ZERO additional network calls
    const rehydrated = await cache.load('/chunks/v1/lib-0.json');
    expect(rehydrated.librarySlug).toBe('lib-0');
    expect(fetchMock).toHaveBeenCalledTimes(6);
    expect(cache.getStats().idbHits).toBe(1);
    expect(cache.getStats().residentChunks).toBe(4);

    // Subsequent load of lib-0 is a synchronous Tier-1 RAM hit
    const ramHit = await cache.load('/chunks/v1/lib-0.json');
    expect(ramHit).toBe(rehydrated);
    expect(cache.getStats().hits).toBe(1);
    expect(fetchMock).toHaveBeenCalledTimes(6);
  });

  it('deduplicates concurrent in-flight fetches for the same chunk URL', async () => {
    let resolveFetch!: (res: Response) => void;
    const fetchMock = vi.fn(
      () =>
        new Promise<Response>((resolve) => {
          resolveFetch = resolve;
        }),
    );

    const cache = new ChunkLRUCache<LibraryChunkPayload>({
      idbStore: createIdbChunkStore({ forceMemory: true }),
      fetchImpl: fetchMock as unknown as typeof fetch,
    });

    // Fire 8 concurrent loads for the same chunk
    const promises = Array.from({ length: 8 }, () =>
      cache.load('/chunks/v1/lucide.json'),
    );

    // Wait a microtask so IDB lookup settles and fetch starts
    await new Promise((r) => setTimeout(r, 10));
    expect(fetchMock).toHaveBeenCalledTimes(1);
    expect(cache.getStats().inFlightCount).toBe(1);

    resolveFetch(makeJsonResponse(makeMockChunk('lucide', 15)));
    const results = await Promise.all(promises);

    // All 8 callers receive the exact same payload instance
    for (const r of results) {
      expect(r.librarySlug).toBe('lucide');
      expect(r).toBe(results[0]);
    }
    expect(fetchMock).toHaveBeenCalledTimes(1);
    expect(cache.getStats().misses).toBe(1);
    expect(cache.getStats().inFlightCount).toBe(0);
  });

  it('only aborts underlying fetch when all deduplicated subscribers abort', async () => {
    let capturedSignal: AbortSignal | undefined;
    let resolveFetch!: (res: Response) => void;
    const fetchMock = vi.fn((_url: RequestInfo | URL, init?: RequestInit) => {
      capturedSignal = init?.signal ?? undefined;
      return new Promise<Response>((resolve, reject) => {
        resolveFetch = resolve;
        capturedSignal?.addEventListener('abort', () => {
          const err = new Error('Aborted');
          err.name = 'AbortError';
          reject(err);
        });
      });
    });

    const cache = new ChunkLRUCache<LibraryChunkPayload>({
      idbStore: createIdbChunkStore({ forceMemory: true }),
      fetchImpl: fetchMock as unknown as typeof fetch,
    });

    const ac1 = new AbortController();
    const ac2 = new AbortController();

    const p1 = cache.load('/chunks/v1/fluent-0.json', { signal: ac1.signal });
    const p2 = cache.load('/chunks/v1/fluent-0.json', { signal: ac2.signal });

    await new Promise((r) => setTimeout(r, 10));
    expect(fetchMock).toHaveBeenCalledTimes(1);

    // Aborting only caller 1 must NOT abort the shared fetch
    ac1.abort();
    await expect(p1).rejects.toMatchObject({ name: 'AbortError' });
    expect(capturedSignal?.aborted).toBe(false);

    // Caller 2 still resolves cleanly
    resolveFetch(makeJsonResponse(makeMockChunk('fluent', 10)));
    const res2 = await p2;
    expect(res2.librarySlug).toBe('fluent');
  });

  it('maintains bounded pinnedIcons map (<= 50) independent of RAM chunk eviction', () => {
    const cache = new ChunkLRUCache<LibraryChunkPayload>();
    for (let i = 0; i < MAX_PINNED_ICONS + 10; i++) {
      cache.pinIcon({
        id: `lucide-icon-${i}`,
        iconIndex: i,
        name: `icon-${i}`,
        svgBody: '<path d="M0 0"/>',
        viewBox: '0 0 24 24',
        strokeWidth: 2,
        flags: 0,
        librarySlug: 'lucide',
        libraryName: 'Lucide',
      });
    }

    cache.clearRam();
    expect(cache.getPinnedIcon('lucide-icon-0')).toBeUndefined();
    expect(cache.getPinnedIcon(`lucide-icon-${MAX_PINNED_ICONS + 9}`)).toBeDefined();
    expect(estimateChunkHeapBytes(makeMockChunk('lucide', 10))).toBeGreaterThan(1000);
  });
});
