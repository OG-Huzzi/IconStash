/**
 * Persistent IndexedDB chunk store backed by `idb-keyval` (`iconstash-v2`),
 * with automatic in-memory fallback for SSR, Node/Vitest, or restricted
 * browser storage environments.
 *
 * Implements the Tier-2 persistence and quota hygiene policy in
 * `docs/memory-budget.md` §3.2:
 * - Keys are prefixed by `${contentHash}:${shardUrl}`.
 * - `pruneStaleHashes(activeHash)` deletes entries from outdated builds.
 * - Caps stored chunks at `maxEntries` (default 40), evicting oldest `lastAccessedAt`.
 */

import {
  clear as idbClear,
  createStore,
  del as idbDel,
  get as idbGet,
  keys as idbKeys,
  set as idbSet,
  type UseStore,
} from 'idb-keyval';

export const IDB_DATABASE_NAME = 'iconstash-v2';
export const IDB_STORE_NAME = 'chunks';
export const DEFAULT_MAX_IDB_CHUNKS = 40;

export interface PersistedChunkRecord<T = unknown> {
  payload: T;
  storedAt: number;
  lastAccessedAt: number;
  byteSize?: number;
}

export interface ChunkPersistenceStore<T = unknown> {
  readonly backend: 'indexeddb' | 'memory';
  get(key: string): Promise<T | undefined>;
  set(key: string, payload: T, byteSize?: number): Promise<void>;
  delete(key: string): Promise<void>;
  has(key: string): Promise<boolean>;
  keys(): Promise<string[]>;
  clear(): Promise<void>;
  pruneStaleHashes(activeContentHash: string): Promise<number>;
}

export interface IdbStoreOptions {
  dbName?: string;
  storeName?: string;
  maxEntries?: number;
  /** Force in-memory fallback (useful in tests). */
  forceMemory?: boolean;
}

/** Build the canonical storage key `${contentHash}:${shardUrl}`. */
export function makeChunkStorageKey(contentHash: string, shardUrl: string): string {
  return contentHash ? `${contentHash}:${shardUrl}` : shardUrl;
}

function isIndexedDbAvailable(): boolean {
  try {
    return typeof globalThis !== 'undefined' && typeof globalThis.indexedDB !== 'undefined' && globalThis.indexedDB !== null;
  } catch {
    return false;
  }
}

/**
 * Create a persistent chunk store using `idb-keyval` with graceful fallback
 * to an in-memory Map when IndexedDB is unavailable or fails at runtime.
 */
export function createIdbChunkStore<T = unknown>(
  options: IdbStoreOptions = {},
): ChunkPersistenceStore<T> {
  const dbName = options.dbName ?? IDB_DATABASE_NAME;
  const storeName = options.storeName ?? IDB_STORE_NAME;
  const maxEntries = Math.max(1, options.maxEntries ?? DEFAULT_MAX_IDB_CHUNKS);

  let useMemory = Boolean(options.forceMemory) || !isIndexedDbAvailable();
  let customStore: UseStore | null = null;
  const memoryFallback = new Map<string, PersistedChunkRecord<T>>();

  if (!useMemory) {
    try {
      customStore = createStore(dbName, storeName);
    } catch {
      useMemory = true;
      customStore = null;
    }
  }

  function switchToMemory(): void {
    useMemory = true;
    customStore = null;
  }

  async function enforceMemoryQuota(): Promise<void> {
    if (memoryFallback.size <= maxEntries) return;
    const sorted = Array.from(memoryFallback.entries()).sort(
      (a, b) => a[1].lastAccessedAt - b[1].lastAccessedAt,
    );
    const excess = memoryFallback.size - maxEntries;
    for (let i = 0; i < excess; i++) {
      memoryFallback.delete(sorted[i]![0]);
    }
  }

  async function enforceIdbQuota(store: UseStore): Promise<void> {
    const allKeys = (await idbKeys(store)) as string[];
    if (allKeys.length <= maxEntries) return;

    const entries: { key: string; lastAccessedAt: number }[] = [];
    for (const k of allKeys) {
      const rec = await idbGet<PersistedChunkRecord<T>>(k, store);
      entries.push({ key: k, lastAccessedAt: rec?.lastAccessedAt ?? 0 });
    }
    entries.sort((a, b) => a.lastAccessedAt - b.lastAccessedAt);
    const excess = allKeys.length - maxEntries;
    for (let i = 0; i < excess; i++) {
      await idbDel(entries[i]!.key, store);
    }
  }

  return {
    get backend(): 'indexeddb' | 'memory' {
      return useMemory ? 'memory' : 'indexeddb';
    },

    async get(key: string): Promise<T | undefined> {
      if (useMemory || !customStore) {
        const rec = memoryFallback.get(key);
        if (!rec) return undefined;
        rec.lastAccessedAt = Date.now();
        return rec.payload;
      }

      try {
        const rec = await idbGet<PersistedChunkRecord<T>>(key, customStore);
        if (!rec) return undefined;
        // Touch lastAccessedAt asynchronously without blocking the read
        const updated: PersistedChunkRecord<T> = {
          ...rec,
          lastAccessedAt: Date.now(),
        };
        void idbSet(key, updated, customStore).catch(() => {});
        return rec.payload;
      } catch {
        switchToMemory();
        const rec = memoryFallback.get(key);
        return rec?.payload;
      }
    },

    async set(key: string, payload: T, byteSize?: number): Promise<void> {
      const now = Date.now();
      const record: PersistedChunkRecord<T> = {
        payload,
        storedAt: now,
        lastAccessedAt: now,
        byteSize,
      };

      if (useMemory || !customStore) {
        memoryFallback.set(key, record);
        await enforceMemoryQuota();
        return;
      }

      try {
        await idbSet(key, record, customStore);
        await enforceIdbQuota(customStore);
      } catch {
        switchToMemory();
        memoryFallback.set(key, record);
        await enforceMemoryQuota();
      }
    },

    async delete(key: string): Promise<void> {
      if (useMemory || !customStore) {
        memoryFallback.delete(key);
        return;
      }
      try {
        await idbDel(key, customStore);
      } catch {
        switchToMemory();
        memoryFallback.delete(key);
      }
    },

    async has(key: string): Promise<boolean> {
      if (useMemory || !customStore) {
        return memoryFallback.has(key);
      }
      try {
        const val = await idbGet<PersistedChunkRecord<T>>(key, customStore);
        return val !== undefined;
      } catch {
        switchToMemory();
        return memoryFallback.has(key);
      }
    },

    async keys(): Promise<string[]> {
      if (useMemory || !customStore) {
        return Array.from(memoryFallback.keys());
      }
      try {
        return (await idbKeys(customStore)).map(String);
      } catch {
        switchToMemory();
        return Array.from(memoryFallback.keys());
      }
    },

    async clear(): Promise<void> {
      memoryFallback.clear();
      if (useMemory || !customStore) return;
      try {
        await idbClear(customStore);
      } catch {
        switchToMemory();
      }
    },

    async pruneStaleHashes(activeContentHash: string): Promise<number> {
      if (!activeContentHash) return 0;
      const prefix = `${activeContentHash}:`;
      let pruned = 0;

      if (useMemory || !customStore) {
        for (const k of Array.from(memoryFallback.keys())) {
          if (!k.startsWith(prefix)) {
            memoryFallback.delete(k);
            pruned++;
          }
        }
        return pruned;
      }

      try {
        const allKeys = (await idbKeys(customStore)).map(String);
        for (const k of allKeys) {
          if (!k.startsWith(prefix)) {
            await idbDel(k, customStore);
            pruned++;
          }
        }
        return pruned;
      } catch {
        switchToMemory();
        for (const k of Array.from(memoryFallback.keys())) {
          if (!k.startsWith(prefix)) {
            memoryFallback.delete(k);
            pruned++;
          }
        }
        return pruned;
      }
    },
  };
}

/** Default singleton store instance for `/chunks/v1/*.json` payloads. */
export const defaultChunkIdbStore = createIdbChunkStore();
