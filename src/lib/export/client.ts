import {
  DEFAULT_ZIP_ROOT_FOLDER,
  DETAIL_ZIP_PNG_SIZES,
  MAX_ZIP_ICONS,
  PNG_EXPORT_SIZES,
  buildDefaultZipFilename,
  buildIconZipArchive,
  buildPngFilename,
  normalizePngSizes,
  type ExportSvgInput,
  type ZipArchiveKind,
} from './zip-builder';
import type {
  ExportWorkerRequest,
  ExportWorkerResponse,
} from '../../workers/export.worker';

export {
  DEFAULT_ZIP_ROOT_FOLDER,
  DETAIL_ZIP_PNG_SIZES,
  MAX_ZIP_ICONS,
  PNG_EXPORT_SIZES,
  buildDefaultZipFilename,
  buildPngFilename,
};
export type { ExportSvgInput, ZipArchiveKind };

export interface ExportProgress {
  completed: number;
  total: number;
}

export interface ExportResult {
  blob: Blob;
  filename: string;
  mimeType: string;
}

export interface ExportPngOptions {
  svgMarkup: string;
  filename: string;
  size: number;
  scale?: number;
  background?: string;
  autoDownload?: boolean;
  onProgress?: (progress: ExportProgress) => void;
  signal?: AbortSignal;
}

export interface ExportZipOptions {
  icons: ExportSvgInput[];
  pngSizes?: readonly number[];
  includeManifest?: boolean;
  includeReadme?: boolean;
  archiveKind?: ZipArchiveKind;
  archiveTitle?: string;
  rootFolder?: string;
  readmeText?: string;
  scale?: number;
  background?: string;
  filename?: string;
  autoDownload?: boolean;
  onProgress?: (progress: ExportProgress) => void;
  signal?: AbortSignal;
}

interface PendingJob {
  resolve: (result: ExportResult) => void;
  reject: (error: Error) => void;
  onProgress?: (progress: ExportProgress) => void;
  abortCleanup?: () => void;
}

interface ExportClientRegistry {
  worker: Worker | null;
  pendingJobs: Map<number, PendingJob>;
  nextJobId: number;
  messageHandler: ((event: MessageEvent<ExportWorkerResponse>) => void) | null;
  errorHandler: ((event: ErrorEvent) => void) | null;
  swapListenerAttached: boolean;
  swapHandler: (() => void) | null;
}

declare global {
  // Singleton registry persisted across Astro View Transitions (docs/memory-budget.md §5.3).
  var __ICONSTASH_EXPORT_WORKER__: ExportClientRegistry | undefined;
}

function getRegistry(): ExportClientRegistry {
  if (!globalThis.__ICONSTASH_EXPORT_WORKER__) {
    globalThis.__ICONSTASH_EXPORT_WORKER__ = {
      worker: null,
      pendingJobs: new Map<number, PendingJob>(),
      nextJobId: 1,
      messageHandler: null,
      errorHandler: null,
      swapListenerAttached: false,
      swapHandler: null,
    };
  }
  return globalThis.__ICONSTASH_EXPORT_WORKER__;
}

/**
 * Returns true if the current environment supports OffscreenCanvas + createImageBitmap
 * inside a Web Worker.
 */
export function supportsOffscreenCanvas(): boolean {
  return (
    typeof OffscreenCanvas !== 'undefined' &&
    typeof createImageBitmap === 'function' &&
    typeof OffscreenCanvas.prototype.convertToBlob === 'function'
  );
}

/**
 * Triggers a browser file download for `blob` and immediately schedules
 * `URL.revokeObjectURL(url)` on a microtask (or optional short timeout)
 * so zero Object URLs leak (docs/memory-budget.md §5.1).
 */
export function downloadBlob(blob: Blob, filename: string, revokeDelayMs = 0): void {
  if (typeof URL === 'undefined' || typeof URL.createObjectURL !== 'function') {
    throw new Error('URL.createObjectURL is unavailable in this environment.');
  }
  if (typeof document === 'undefined' || !document.body) {
    throw new Error('Document body is unavailable for triggering downloads.');
  }

  const url = URL.createObjectURL(blob);
  const anchor = document.createElement('a');
  let scheduledRevoke = false;

  try {
    anchor.href = url;
    anchor.download = filename;
    anchor.rel = 'noopener';
    anchor.style.display = 'none';
    document.body.appendChild(anchor);
    anchor.click();

    if (revokeDelayMs > 0) {
      setTimeout(() => {
        URL.revokeObjectURL(url);
      }, revokeDelayMs);
    } else {
      queueMicrotask(() => {
        URL.revokeObjectURL(url);
      });
    }
    scheduledRevoke = true;
  } finally {
    anchor.remove();
    if (!scheduledRevoke) {
      URL.revokeObjectURL(url);
    }
  }
}

function prepareFallbackSvg(svgMarkup: string, pixelSize: number): string {
  const trimmed = svgMarkup.trim();
  if (!trimmed.toLowerCase().includes('<svg')) {
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${pixelSize}" height="${pixelSize}" viewBox="0 0 24 24">${trimmed}</svg>`;
  }

  return trimmed.replace(/<svg\b([^>]*)>/i, (_match, rawAttrs: string) => {
    let attrs = rawAttrs;
    if (!/\bxmlns\s*=/i.test(attrs)) {
      attrs += ' xmlns="http://www.w3.org/2000/svg"';
    }
    if (/\bwidth\s*=/i.test(attrs)) {
      attrs = attrs.replace(/\bwidth\s*=\s*["'][^"']*["']/i, `width="${pixelSize}"`);
    } else {
      attrs += ` width="${pixelSize}"`;
    }
    if (/\bheight\s*=/i.test(attrs)) {
      attrs = attrs.replace(/\bheight\s*=\s*["'][^"']*["']/i, `height="${pixelSize}"`);
    } else {
      attrs += ` height="${pixelSize}"`;
    }
    return `<svg${attrs}>`;
  });
}

/**
 * Clean fallback PNG rasterizer using a DOM `<canvas>` for older browsers where
 * `OffscreenCanvas` or Web Workers are unavailable.
 *
 * Guarantees:
 * - Revokes any temporary Object URL in `finally`.
 * - Resets `canvas.width = 0; canvas.height = 0;` in `finally` to release GPU/RAM buffers.
 */
export async function rasterizeSvgFallback(
  svgMarkup: string,
  size: number,
  scale = 1,
  background?: string,
): Promise<Blob> {
  if (typeof document === 'undefined') {
    throw new Error('Canvas fallback requires a browser document.');
  }

  const targetSize = Math.min(2048, Math.max(16, Math.round(size || 128)));
  const pixelRatio = Math.min(4, Math.max(1, Number(scale) || 1));
  const pixelSize = Math.round(targetSize * pixelRatio);

  const preparedSvg = prepareFallbackSvg(svgMarkup, pixelSize);
  const svgBlob = new Blob([preparedSvg], { type: 'image/svg+xml;charset=utf-8' });
  const objectUrl = URL.createObjectURL(svgBlob);

  const canvas = document.createElement('canvas');
  canvas.width = pixelSize;
  canvas.height = pixelSize;

  try {
    const ctx = canvas.getContext('2d');
    if (!ctx) {
      throw new Error('Failed to acquire 2D context on fallback <canvas>.');
    }

    const img = await new Promise<HTMLImageElement>((resolve, reject) => {
      const el = new Image();
      el.crossOrigin = 'anonymous';
      el.onload = () => resolve(el);
      el.onerror = () => reject(new Error('Failed to load SVG into fallback Image element.'));
      el.src = objectUrl;
    });

    ctx.clearRect(0, 0, pixelSize, pixelSize);
    if (background && background !== 'transparent') {
      ctx.fillStyle = background;
      ctx.fillRect(0, 0, pixelSize, pixelSize);
    }
    ctx.drawImage(img, 0, 0, pixelSize, pixelSize);

    const pngBlob = await new Promise<Blob>((resolve, reject) => {
      canvas.toBlob((blob) => {
        if (blob) resolve(blob);
        else reject(new Error('Fallback canvas.toBlob returned null.'));
      }, 'image/png');
    });

    return pngBlob;
  } finally {
    URL.revokeObjectURL(objectUrl);
    canvas.width = 0;
    canvas.height = 0;
  }
}

/**
 * Terminates the lazy export worker (if running), rejects any in-flight jobs,
 * and cleans up all attached listeners so zero references survive navigation.
 */
export function terminateExportWorker(reason = 'Export worker terminated.'): void {
  const registry = getRegistry();

  if (registry.worker) {
    if (registry.messageHandler) {
      registry.worker.removeEventListener('message', registry.messageHandler);
    }
    if (registry.errorHandler) {
      registry.worker.removeEventListener('error', registry.errorHandler);
    }
    registry.worker.terminate();
    registry.worker = null;
    registry.messageHandler = null;
    registry.errorHandler = null;
  }

  for (const [jobId, pending] of registry.pendingJobs.entries()) {
    pending.abortCleanup?.();
    pending.reject(new Error(reason));
    registry.pendingJobs.delete(jobId);
  }

  if (registry.swapListenerAttached && registry.swapHandler && typeof document !== 'undefined') {
    document.removeEventListener('astro:before-swap', registry.swapHandler);
    registry.swapListenerAttached = false;
    registry.swapHandler = null;
  }
}

function attachAstroNavigationCleanup(registry: ExportClientRegistry): void {
  if (registry.swapListenerAttached || typeof document === 'undefined') {
    return;
  }
  const onBeforeSwap = () => {
    terminateExportWorker('Navigation occurred during export.');
  };
  document.addEventListener('astro:before-swap', onBeforeSwap);
  registry.swapHandler = onBeforeSwap;
  registry.swapListenerAttached = true;
}

/**
 * Lazily spawns the dedicated `export.worker.ts` singleton only when an export is requested,
 * and binds Astro View Transition (`astro:before-swap`) teardown.
 */
function ensureExportWorker(): Worker {
  const registry = getRegistry();
  if (registry.worker) {
    return registry.worker;
  }
  if (typeof Worker === 'undefined') {
    throw new Error('Web Workers are unavailable in this environment.');
  }

  const worker = new Worker(new URL('../../workers/export.worker.ts', import.meta.url), {
    type: 'module',
  });

  const onMessage = (event: MessageEvent<ExportWorkerResponse>) => {
    const msg = event.data;
    const pending = registry.pendingJobs.get(msg.jobId);
    if (!pending) return;

    if (msg.type === 'PROGRESS') {
      pending.onProgress?.({ completed: msg.completed, total: msg.total });
      return;
    }

    registry.pendingJobs.delete(msg.jobId);
    pending.abortCleanup?.();

    if (msg.type === 'COMPLETE') {
      const blob = new Blob([msg.buffer], { type: msg.mimeType });
      pending.resolve({
        blob,
        filename: msg.filename,
        mimeType: msg.mimeType,
      });
    } else if (msg.type === 'ERROR') {
      pending.reject(new Error(msg.message));
    }
  };

  const onError = (event: ErrorEvent) => {
    const errMsg = event.message || 'Export worker encountered an unexpected error.';
    terminateExportWorker(errMsg);
  };

  worker.addEventListener('message', onMessage);
  worker.addEventListener('error', onError);

  registry.worker = worker;
  registry.messageHandler = onMessage;
  registry.errorHandler = onError;

  attachAstroNavigationCleanup(registry);
  return worker;
}

/**
 * Sends a cancellation signal to the active export worker for `jobId`.
 */
export function cancelExportJob(jobId: number): void {
  const registry = getRegistry();
  const pending = registry.pendingJobs.get(jobId);
  if (pending) {
    pending.abortCleanup?.();
    pending.reject(new Error('Export job cancelled.'));
    registry.pendingJobs.delete(jobId);
  }
  if (registry.worker) {
    const msg: ExportWorkerRequest = { type: 'CANCEL', jobId };
    registry.worker.postMessage(msg);
  }
}

function dispatchToWorker(
  requestFactory: (jobId: number) => ExportWorkerRequest,
  onProgress?: (progress: ExportProgress) => void,
  signal?: AbortSignal,
): Promise<ExportResult> {
  if (signal?.aborted) {
    return Promise.reject(new Error('Export job cancelled.'));
  }

  const registry = getRegistry();
  const worker = ensureExportWorker();
  const jobId = registry.nextJobId++;

  return new Promise<ExportResult>((resolve, reject) => {
    const pending: PendingJob = { resolve, reject, onProgress };

    if (signal) {
      const onAbort = () => {
        cancelExportJob(jobId);
      };
      signal.addEventListener('abort', onAbort, { once: true });
      pending.abortCleanup = () => signal.removeEventListener('abort', onAbort);
    }

    registry.pendingJobs.set(jobId, pending);
    worker.postMessage(requestFactory(jobId));
  });
}

/**
 * Exports a single SVG as a PNG `Blob` (and optionally downloads it).
 * Uses `export.worker.ts` + `OffscreenCanvas` when available, and automatically falls back
 * to a DOM `<canvas>` rasterizer in older browsers.
 */
export async function exportPng(options: ExportPngOptions): Promise<ExportResult> {
  const autoDownload = options.autoDownload !== false;
  let result: ExportResult;

  if (typeof Worker !== 'undefined' && supportsOffscreenCanvas()) {
    result = await dispatchToWorker(
      (jobId) => ({
        type: 'EXPORT_PNG',
        jobId,
        svgMarkup: options.svgMarkup,
        filename: options.filename,
        size: options.size,
        scale: options.scale,
        background: options.background,
      }),
      options.onProgress,
      options.signal,
    );
  } else {
    options.onProgress?.({ completed: 0, total: 1 });
    const blob = await rasterizeSvgFallback(
      options.svgMarkup,
      options.size,
      options.scale ?? 1,
      options.background,
    );
    options.onProgress?.({ completed: 1, total: 1 });
    result = {
      blob,
      filename: options.filename,
      mimeType: 'image/png',
    };
  }

  if (autoDownload) {
    downloadBlob(result.blob, result.filename);
  }
  return result;
}

/**
 * Exports up to 200 icons as a ZIP archive (SVGs, optional PNGs, `icons.json`, `README.txt`).
 * Uses `export.worker.ts` when available; falls back cleanly to main-thread `fflate` + `<canvas>`
 * if Workers or `OffscreenCanvas` (when PNGs are requested) are unavailable.
 */
export async function exportZip(options: ExportZipOptions): Promise<ExportResult> {
  const cappedIcons = options.icons.slice(0, MAX_ZIP_ICONS);
  if (cappedIcons.length === 0) {
    throw new Error('Cannot build ZIP archive with zero icons.');
  }

  const pngSizes = normalizePngSizes(options.pngSizes);
  const archiveKind = options.archiveKind ?? 'bulk';
  const filename =
    options.filename || buildDefaultZipFilename(archiveKind, options.archiveTitle, pngSizes.length > 0);
  const includeManifest = options.includeManifest !== false;
  const includeReadme = options.includeReadme !== false;
  const autoDownload = options.autoDownload !== false;

  const canUseWorker =
    typeof Worker !== 'undefined' && (pngSizes.length === 0 || supportsOffscreenCanvas());

  let result: ExportResult;

  if (canUseWorker) {
    result = await dispatchToWorker(
      (jobId) => ({
        type: 'EXPORT_ZIP',
        jobId,
        icons: cappedIcons,
        pngSizes,
        includeManifest,
        includeReadme,
        archiveKind,
        archiveTitle: options.archiveTitle,
        rootFolder: options.rootFolder,
        readmeText: options.readmeText,
        scale: options.scale,
        background: options.background,
        filename,
      }),
      options.onProgress,
      options.signal,
    );
  } else {
    const total = Math.max(1, cappedIcons.length * (1 + pngSizes.length));
    let completed = 0;
    options.onProgress?.({ completed: 0, total });

    const pngBuffers = new Map<string, Map<number, Uint8Array>>();
    for (const icon of cappedIcons) {
      if (options.signal?.aborted) {
        throw new Error('Export job cancelled.');
      }
      completed += 1;
      options.onProgress?.({ completed, total });

      if (pngSizes.length > 0) {
        const iconMap = new Map<number, Uint8Array>();
        for (const size of pngSizes) {
          if (options.signal?.aborted) {
            throw new Error('Export job cancelled.');
          }
          const pngBlob = await rasterizeSvgFallback(
            icon.svgMarkup,
            size,
            options.scale ?? 1,
            options.background,
          );
          iconMap.set(size, new Uint8Array(await pngBlob.arrayBuffer()));
          completed += 1;
          options.onProgress?.({ completed, total });
        }
        pngBuffers.set(icon.id, iconMap);
      }
    }

    const zipBytes = buildIconZipArchive({
      icons: cappedIcons,
      pngBuffers,
      rootFolder: options.rootFolder,
      archiveKind,
      archiveTitle: options.archiveTitle,
      includeManifest,
      includeReadme,
      readmeText: options.readmeText,
    });
    pngBuffers.clear();

    const exactBytes = new Uint8Array(zipBytes.byteLength);
    exactBytes.set(zipBytes);
    result = {
      blob: new Blob([exactBytes], { type: 'application/zip' }),
      filename,
      mimeType: 'application/zip',
    };
  }

  if (autoDownload) {
    downloadBlob(result.blob, result.filename);
  }
  return result;
}

/** Exports a Bulk Selection ZIP (SVGs + manifest + README, capped at 200 icons). */
export function exportBulkZip(
  icons: ExportSvgInput[],
  options: Omit<ExportZipOptions, 'icons' | 'archiveKind'> = {},
): Promise<ExportResult> {
  return exportZip({
    ...options,
    icons,
    archiveKind: 'bulk',
    pngSizes: options.pngSizes ?? [],
  });
}

/** Exports a Compare Set ZIP (cross-library icons sharing a concept). */
export function exportCompareZip(
  icons: ExportSvgInput[],
  conceptTitle?: string,
  options: Omit<ExportZipOptions, 'icons' | 'archiveKind' | 'archiveTitle'> = {},
): Promise<ExportResult> {
  return exportZip({
    ...options,
    icons,
    archiveKind: 'compare',
    archiveTitle: conceptTitle,
    pngSizes: options.pngSizes ?? [],
  });
}

/** Exports a Collection ZIP (SVGs only, or SVGs + all 7 PNG sizes when `includePngs` is true). */
export function exportCollectionZip(
  icons: ExportSvgInput[],
  collectionName: string,
  includePngs = false,
  options: Omit<ExportZipOptions, 'icons' | 'archiveKind' | 'archiveTitle' | 'pngSizes'> = {},
): Promise<ExportResult> {
  return exportZip({
    ...options,
    icons,
    archiveKind: 'collection',
    archiveTitle: collectionName,
    pngSizes: includePngs ? PNG_EXPORT_SIZES : [],
  });
}
