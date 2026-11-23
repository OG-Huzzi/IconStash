/**
 * Dedicated Web Worker wrapping `BinarySearchEngine` with zero-copy Transferable
 * `Uint32Array` responses and clean request/cancellation handling.
 *
 * Protocol matches `docs/architecture.md` §6.1.
 */

import {
  BinarySearchEngine,
  type SearchSortMode,
} from './search-core.js';

export type SearchWorkerRequest =
  | { type: 'INIT'; indexUrl: string; metaUrl?: string }
  | { type: 'INIT_BUFFER'; buffer: ArrayBuffer }
  | {
      type: 'QUERY';
      queryId: number;
      query: string;
      libMask: number;
      catMask: number;
      styleMask: number;
      sort: SearchSortMode;
      limit?: number;
    }
  | { type: 'CONCEPT_MATCHES'; queryId: number; iconIndex: number; maxPerLibrary?: number }
  | { type: 'CANCEL'; queryId: number };

export type SearchWorkerResponse =
  | { type: 'READY'; iconCount: number; indexBytes: number; initMs: number }
  | {
      type: 'RESULTS';
      queryId: number;
      indices: Uint32Array;
      totalMatches: number;
      elapsedMs: number;
      libraryCounts: Uint32Array;
      categoryCounts: Uint32Array;
      styleCounts: Uint32Array;
    }
  | {
      type: 'CONCEPT_MATCHES';
      queryId: number;
      indices: Uint32Array;
    }
  | { type: 'ERROR'; queryId?: number; message: string };

export type WorkerPostMessage = (
  message: SearchWorkerResponse,
  transfer?: Transferable[],
) => void;

export interface SearchWorkerHandler {
  handleMessage(msg: SearchWorkerRequest): Promise<void>;
  getEngine(): BinarySearchEngine | null;
}

const MAX_CANCELLED_IDS = 256;

/**
 * Create a testable, environment-agnostic message handler for the search worker.
 */
export function createSearchWorkerHandler(
  post: WorkerPostMessage,
  fetchImpl: typeof fetch = globalThis.fetch,
): SearchWorkerHandler {
  let engine: BinarySearchEngine | null = null;
  const cancelledQueries = new Set<number>();

  function markCancelled(queryId: number): void {
    if (cancelledQueries.size >= MAX_CANCELLED_IDS) {
      const oldest = cancelledQueries.values().next().value;
      if (oldest !== undefined) cancelledQueries.delete(oldest);
    }
    cancelledQueries.add(queryId);
  }

  function consumeCancelled(queryId: number): boolean {
    if (cancelledQueries.has(queryId)) {
      cancelledQueries.delete(queryId);
      return true;
    }
    return false;
  }

  async function handleMessage(msg: SearchWorkerRequest): Promise<void> {
    try {
      switch (msg.type) {
        case 'CANCEL': {
          markCancelled(msg.queryId);
          return;
        }

        case 'INIT_BUFFER': {
          const t0 = performance.now();
          engine = new BinarySearchEngine(msg.buffer);
          post({
            type: 'READY',
            iconCount: engine.iconCount,
            indexBytes: engine.byteLength,
            initMs: performance.now() - t0,
          });
          return;
        }

        case 'INIT': {
          const t0 = performance.now();
          const res = await fetchImpl(msg.indexUrl);
          if (!res.ok) {
            throw new Error(
              `Failed to fetch search index (${res.status} ${res.statusText}): ${msg.indexUrl}`,
            );
          }
          const buffer = await res.arrayBuffer();
          engine = new BinarySearchEngine(buffer);
          post({
            type: 'READY',
            iconCount: engine.iconCount,
            indexBytes: engine.byteLength,
            initMs: performance.now() - t0,
          });
          return;
        }

        case 'QUERY': {
          if (consumeCancelled(msg.queryId)) return;
          if (!engine) {
            post({
              type: 'ERROR',
              queryId: msg.queryId,
              message: 'Search index is not initialized. Send INIT first.',
            });
            return;
          }

          const result = engine.query({
            query: msg.query,
            libMask: msg.libMask,
            catMask: msg.catMask,
            styleMask: msg.styleMask,
            sort: msg.sort,
            limit: msg.limit,
          });

          if (consumeCancelled(msg.queryId)) return;

          post(
            {
              type: 'RESULTS',
              queryId: msg.queryId,
              indices: result.indices,
              totalMatches: result.totalMatches,
              elapsedMs: result.elapsedMs,
              libraryCounts: result.libraryCounts,
              categoryCounts: result.categoryCounts,
              styleCounts: result.styleCounts,
            },
            [
              result.indices.buffer,
              result.libraryCounts.buffer,
              result.categoryCounts.buffer,
              result.styleCounts.buffer,
            ],
          );
          return;
        }

        case 'CONCEPT_MATCHES': {
          if (consumeCancelled(msg.queryId)) return;
          if (!engine) {
            post({
              type: 'ERROR',
              queryId: msg.queryId,
              message: 'Search index is not initialized. Send INIT first.',
            });
            return;
          }

          const indices = engine.findConceptMatches(msg.iconIndex, msg.maxPerLibrary);
          if (consumeCancelled(msg.queryId)) return;

          post(
            {
              type: 'CONCEPT_MATCHES',
              queryId: msg.queryId,
              indices,
            },
            [indices.buffer],
          );
          return;
        }
      }
    } catch (err) {
      const message = err instanceof Error ? err.message : String(err);
      const queryId = 'queryId' in msg ? msg.queryId : undefined;
      post({ type: 'ERROR', queryId, message });
    }
  }

  return {
    handleMessage,
    getEngine: () => engine,
  };
}

// Automatically attach to DedicatedWorkerGlobalScope when running inside a Web Worker.
interface WorkerScopeLike {
  postMessage(message: unknown, transfer?: Transferable[]): void;
  onmessage: ((ev: MessageEvent<SearchWorkerRequest>) => void) | null;
}

const workerScope = globalThis as unknown as Partial<WorkerScopeLike>;
if (
  typeof workerScope.postMessage === 'function' &&
  typeof (globalThis as { window?: unknown }).window === 'undefined' &&
  typeof (globalThis as { process?: { versions?: { node?: string } } }).process?.versions?.node ===
    'undefined'
) {
  const handler = createSearchWorkerHandler((message, transfer) => {
    if (transfer && transfer.length > 0) {
      workerScope.postMessage!(message, transfer);
    } else {
      workerScope.postMessage!(message);
    }
  });

  workerScope.onmessage = (event: MessageEvent<SearchWorkerRequest>) => {
    void handler.handleMessage(event.data);
  };
}
