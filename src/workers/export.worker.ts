/// <reference lib="webworker" />

import {
  MAX_ZIP_ICONS,
  StreamingZipBuilder,
  buildArchiveReadme,
  createBaseNameAllocator,
  normalizePngSizes,
  normalizeRootPrefix,
  type ExportSvgInput,
  type ZipArchiveKind,
  type ZipManifestEntry,
} from '../lib/export/zip-builder';

export type { ExportSvgInput, ZipArchiveKind };

export type ExportWorkerRequest =
  | {
      type: 'EXPORT_PNG';
      jobId: number;
      svgMarkup: string;
      filename: string;
      size: number;
      scale?: number;
      background?: string;
    }
  | {
      type: 'EXPORT_ZIP';
      jobId: number;
      icons: ExportSvgInput[];
      pngSizes: number[];
      includeManifest: boolean;
      includeReadme?: boolean;
      archiveKind?: ZipArchiveKind;
      archiveTitle?: string;
      rootFolder?: string;
      readmeText?: string;
      scale?: number;
      background?: string;
      filename: string;
    }
  | { type: 'CANCEL'; jobId: number };

export type ExportWorkerResponse =
  | { type: 'PROGRESS'; jobId: number; completed: number; total: number }
  | {
      type: 'COMPLETE';
      jobId: number;
      filename: string;
      mimeType: string;
      buffer: ArrayBuffer;
    }
  | { type: 'ERROR'; jobId: number; message: string };

const MIN_PNG_SIZE = 16;
const MAX_PNG_SIZE = 2048;
const cancelledJobs = new Set<number>();

/**
 * Ensures the SVG markup has explicit XML namespace and pixel width/height attributes
 * so `createImageBitmap` rasterizes cleanly at the requested dimensions.
 */
export function prepareSvgForRasterization(svgMarkup: string, pixelSize: number): string {
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

function clampPngSize(size: number): number {
  const rounded = Math.round(Number(size));
  if (!Number.isFinite(rounded)) return 128;
  return Math.min(MAX_PNG_SIZE, Math.max(MIN_PNG_SIZE, rounded));
}

function clampScale(scale: number | undefined): number {
  const n = Number(scale ?? 1);
  if (!Number.isFinite(n) || n <= 0) return 1;
  return Math.min(4, Math.max(1, n));
}

/**
 * Returns a standalone `ArrayBuffer` matching the exact byte range of `bytes`
 * so it can be safely transferred via `postMessage(..., [buffer])`.
 */
export function toTransferableArrayBuffer(bytes: Uint8Array): ArrayBuffer {
  if (
    bytes.byteOffset === 0 &&
    bytes.byteLength === bytes.buffer.byteLength &&
    bytes.buffer instanceof ArrayBuffer
  ) {
    return bytes.buffer;
  }
  const copy = new Uint8Array(bytes.byteLength);
  copy.set(bytes);
  return copy.buffer;
}

/**
 * Rasterizes an SVG string into a PNG `ArrayBuffer` using `OffscreenCanvas` + `createImageBitmap`.
 *
 * Zero-leak guarantees (docs/memory-budget.md §5.2):
 * 1. `bitmap.close()` is ALWAYS invoked in a `finally` block immediately after `ctx.drawImage()`.
 * 2. `canvas.width = 0; canvas.height = 0;` is ALWAYS invoked in a `finally` block after `convertToBlob()`
 *    to release GPU/RAM backing textures immediately.
 */
export async function rasterizeSvgToPngBuffer(
  svgMarkup: string,
  size: number,
  scale = 1,
  background?: string,
): Promise<ArrayBuffer> {
  if (typeof OffscreenCanvas === 'undefined' || typeof createImageBitmap !== 'function') {
    throw new Error('OffscreenCanvas or createImageBitmap is unavailable in this environment.');
  }

  const targetSize = clampPngSize(size);
  const pixelRatio = clampScale(scale);
  const pixelSize = Math.round(targetSize * pixelRatio);

  const preparedSvg = prepareSvgForRasterization(svgMarkup, pixelSize);
  const svgBlob = new Blob([preparedSvg], { type: 'image/svg+xml;charset=utf-8' });

  const canvas = new OffscreenCanvas(pixelSize, pixelSize);
  try {
    const ctx = canvas.getContext('2d');
    if (!ctx) {
      throw new Error('Failed to acquire 2D context on OffscreenCanvas.');
    }

    ctx.clearRect(0, 0, pixelSize, pixelSize);
    if (background && background !== 'transparent') {
      ctx.fillStyle = background;
      ctx.fillRect(0, 0, pixelSize, pixelSize);
    }

    const bitmap = await createImageBitmap(svgBlob);
    try {
      ctx.drawImage(bitmap, 0, 0, pixelSize, pixelSize);
    } finally {
      bitmap.close();
    }

    const pngBlob = await canvas.convertToBlob({ type: 'image/png' });
    return await pngBlob.arrayBuffer();
  } finally {
    // Release GPU/RAM backing store immediately.
    canvas.width = 0;
    canvas.height = 0;
  }
}

export interface ExportWorkerEmitter {
  postMessage(message: ExportWorkerResponse, transfer?: Transferable[]): void;
}

function assertNotCancelled(jobId: number): void {
  if (cancelledJobs.has(jobId)) {
    throw new Error('Export job cancelled.');
  }
}

/**
 * Handles a single `EXPORT_PNG` or `EXPORT_ZIP` request and emits progress/complete/error messages.
 * Exported for direct unit testing alongside the worker `onmessage` hook.
 */
export async function processExportRequest(
  request: ExportWorkerRequest,
  emitter: ExportWorkerEmitter,
  rasterizer: typeof rasterizeSvgToPngBuffer = rasterizeSvgToPngBuffer,
): Promise<void> {
  if (request.type === 'CANCEL') {
    cancelledJobs.add(request.jobId);
    return;
  }

  const { jobId } = request;
  cancelledJobs.delete(jobId);

  try {
    if (request.type === 'EXPORT_PNG') {
      emitter.postMessage({ type: 'PROGRESS', jobId, completed: 0, total: 1 });
      const buffer = await rasterizer(
        request.svgMarkup,
        request.size,
        request.scale ?? 1,
        request.background,
      );
      assertNotCancelled(jobId);
      emitter.postMessage({ type: 'PROGRESS', jobId, completed: 1, total: 1 });
      emitter.postMessage(
        {
          type: 'COMPLETE',
          jobId,
          filename: request.filename,
          mimeType: 'image/png',
          buffer,
        },
        [buffer],
      );
      return;
    }

    if (request.type === 'EXPORT_ZIP') {
      const cappedIcons = request.icons.slice(0, MAX_ZIP_ICONS);
      const pngSizes = normalizePngSizes(request.pngSizes);
      const prefix = normalizeRootPrefix(request.rootFolder);
      const includeManifest = request.includeManifest !== false;
      const includeReadme = request.includeReadme !== false;
      const archiveKind = request.archiveKind ?? 'bulk';
      const allocateBase = createBaseNameAllocator();

      const totalSteps = Math.max(1, cappedIcons.length * (1 + pngSizes.length));
      let completedSteps = 0;

      emitter.postMessage({ type: 'PROGRESS', jobId, completed: 0, total: totalSteps });

      const builder = new StreamingZipBuilder();
      const manifest: ZipManifestEntry[] = [];

      try {
        // Sequential processing (concurrency = 1) guarantees at most one OffscreenCanvas
        // backing store exists in GPU/RAM at any instant (docs/memory-budget.md §5.2).
        for (const icon of cappedIcons) {
          assertNotCancelled(jobId);

          const base = allocateBase(icon.librarySlug, icon.name);
          const svgFile = `${base}.svg`;
          builder.addText(`${prefix}${svgFile}`, icon.svgMarkup, 6);
          completedSteps += 1;
          emitter.postMessage({
            type: 'PROGRESS',
            jobId,
            completed: completedSteps,
            total: totalSteps,
          });

          const pngFiles: string[] = [];
          for (const size of pngSizes) {
            assertNotCancelled(jobId);
            const pngBuffer = await rasterizer(
              icon.svgMarkup,
              size,
              request.scale ?? 1,
              request.background,
            );
            const pngFile = `${base}-${size}.png`;
            builder.addBytes(`${prefix}${pngFile}`, new Uint8Array(pngBuffer), 0);
            pngFiles.push(pngFile);
            completedSteps += 1;
            emitter.postMessage({
              type: 'PROGRESS',
              jobId,
              completed: completedSteps,
              total: totalSteps,
            });
          }

          if (includeManifest) {
            const entry: ZipManifestEntry = {
              id: icon.id,
              name: icon.name,
              library: icon.library ?? icon.librarySlug,
              librarySlug: icon.librarySlug,
              tags: icon.tags ? [...icon.tags] : [],
              svgFile,
            };
            if (pngFiles.length > 0) {
              entry.pngFiles = pngFiles;
            }
            manifest.push(entry);
          }
        }

        assertNotCancelled(jobId);

        if (includeManifest) {
          builder.addText(`${prefix}icons.json`, JSON.stringify(manifest, null, 2), 6);
        }

        if (includeReadme) {
          const readme =
            request.readmeText ??
            buildArchiveReadme({
              kind: archiveKind,
              title: request.archiveTitle,
              iconCount: cappedIcons.length,
              pngSizes,
              includeManifest,
            });
          builder.addText(`${prefix}README.txt`, readme, 6);
        }

        const zipBytes = builder.finish();
        manifest.length = 0;

        const transferBuffer = toTransferableArrayBuffer(zipBytes);
        emitter.postMessage(
          {
            type: 'COMPLETE',
            jobId,
            filename: request.filename,
            mimeType: 'application/zip',
            buffer: transferBuffer,
          },
          [transferBuffer],
        );
      } catch (err) {
        builder.dispose();
        manifest.length = 0;
        throw err;
      }
    }
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    emitter.postMessage({ type: 'ERROR', jobId, message });
  } finally {
    cancelledJobs.delete(jobId);
  }
}

// Register worker message handler only when executing inside a DedicatedWorkerGlobalScope.
const workerScope =
  typeof self !== 'undefined' &&
  typeof (self as unknown as { document?: unknown }).document === 'undefined' &&
  typeof self.postMessage === 'function'
    ? (self as unknown as DedicatedWorkerGlobalScope)
    : null;

if (workerScope) {
  workerScope.onmessage = (event: MessageEvent<ExportWorkerRequest>) => {
    void processExportRequest(event.data, {
      postMessage: (msg, transfer) => {
        if (transfer && transfer.length > 0) {
          workerScope.postMessage(msg, transfer);
        } else {
          workerScope.postMessage(msg);
        }
      },
    });
  };
}
