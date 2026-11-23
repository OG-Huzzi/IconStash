import { afterEach, describe, expect, it, vi } from 'vitest';
import { strFromU8, unzipSync } from 'fflate';
import {
  DETAIL_ZIP_PNG_SIZES,
  MAX_ZIP_ICONS,
  PNG_EXPORT_SIZES,
  StreamingZipBuilder,
  buildDefaultZipFilename,
  buildIconZipArchive,
  buildPngFilename,
  normalizePngSizes,
  packZipEntries,
  type ExportSvgInput,
} from '../../src/lib/export/zip-builder';
import {
  prepareSvgForRasterization,
  processExportRequest,
  rasterizeSvgToPngBuffer,
  type ExportWorkerResponse,
} from '../../src/workers/export.worker';
import {
  downloadBlob,
  exportPng,
  exportZip,
  rasterizeSvgFallback,
  terminateExportWorker,
} from '../../src/lib/export/client';

const SAMPLE_SVG =
  '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M4 12h16"/></svg>';

const FAKE_PNG_BYTES = new Uint8Array([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 1, 2, 3, 4]);

function makeSampleIcons(count = 2): ExportSvgInput[] {
  return Array.from({ length: count }, (_, idx) => ({
    id: `lucide-icon-${idx + 1}`,
    name: `icon-${idx + 1}`,
    library: 'Lucide',
    librarySlug: 'lucide',
    tags: ['ui', `tag-${idx + 1}`],
    svgMarkup: SAMPLE_SVG,
  }));
}

afterEach(() => {
  terminateExportWorker();
  vi.restoreAllMocks();
  vi.unstubAllGlobals();
});

describe('PNG export sizes & naming conventions', () => {
  it('exposes all 7 exact PNG export sizes (16px-512px)', () => {
    expect([...PNG_EXPORT_SIZES]).toEqual([16, 32, 48, 64, 128, 256, 512]);
    expect(PNG_EXPORT_SIZES).toHaveLength(7);
    expect([...DETAIL_ZIP_PNG_SIZES]).toEqual([16, 32, 64, 128, 256, 512]);
  });

  it('normalizes, deduplicates, and filters PNG sizes', () => {
    expect(normalizePngSizes([512, 16, 64, 16, 4, 4096, 128])).toEqual([16, 64, 128, 512]);
    expect(normalizePngSizes([])).toEqual([]);
  });

  it('formats canonical PNG and ZIP filenames', () => {
    expect(buildPngFilename('Lucide', 'Arrow Up!', 256)).toBe('lucide-arrow-up-256.png');
    expect(buildDefaultZipFilename('bulk')).toBe('IconStash-icons.zip');
    expect(buildDefaultZipFilename('compare', 'Search')).toBe('IconStash-compare-search.zip');
    expect(buildDefaultZipFilename('collection', 'My Favorites', false)).toBe('my-favorites.zip');
    expect(buildDefaultZipFilename('collection', 'My Favorites', true)).toBe('my-favorites-png.zip');
  });
});

describe('fflate ZIP builder (sync & streaming)', () => {
  it('builds and decompresses a Bulk Selection ZIP with SVGs, manifest, and README', () => {
    const icons: ExportSvgInput[] = [
      {
        id: 'lucide-home',
        name: 'home',
        library: 'Lucide',
        librarySlug: 'lucide',
        tags: ['house', 'main'],
        svgMarkup: SAMPLE_SVG,
      },
      {
        id: 'tabler-home',
        name: 'home',
        library: 'Tabler Icons',
        librarySlug: 'tabler',
        tags: ['house'],
        svgMarkup: SAMPLE_SVG,
      },
    ];

    const zipBytes = buildIconZipArchive({
      icons,
      archiveKind: 'bulk',
    });

    const entries = unzipSync(zipBytes);
    expect(Object.keys(entries).sort()).toEqual([
      'IconStash/README.txt',
      'IconStash/icons.json',
      'IconStash/lucide-home.svg',
      'IconStash/tabler-home.svg',
    ]);

    expect(strFromU8(entries['IconStash/lucide-home.svg'])).toBe(SAMPLE_SVG);
    expect(strFromU8(entries['IconStash/README.txt'])).toContain('Bulk Selection Export');

    const manifest = JSON.parse(strFromU8(entries['IconStash/icons.json']));
    expect(manifest).toHaveLength(2);
    expect(manifest[0]).toMatchObject({
      id: 'lucide-home',
      name: 'home',
      library: 'Lucide',
      librarySlug: 'lucide',
      svgFile: 'lucide-home.svg',
    });
  });

  it('builds a Collection PNG ZIP containing all 7 PNG sizes and exact binary payloads', () => {
    const icon = makeSampleIcons(1)[0];
    const pngMap = new Map<number, Uint8Array>();
    for (const size of PNG_EXPORT_SIZES) {
      pngMap.set(size, new Uint8Array([...FAKE_PNG_BYTES, size & 0xff]));
    }
    const pngBuffers = new Map<string, Map<number, Uint8Array>>([[icon.id, pngMap]]);

    const zipBytes = buildIconZipArchive({
      icons: [icon],
      pngBuffers,
      archiveKind: 'collection',
      archiveTitle: 'Favorites',
    });

    const entries = unzipSync(zipBytes);
    for (const size of PNG_EXPORT_SIZES) {
      const key = `IconStash/lucide-icon-1-${size}.png`;
      expect(entries[key]).toBeDefined();
      expect(Array.from(entries[key])).toEqual([...FAKE_PNG_BYTES, size & 0xff]);
    }
    expect(strFromU8(entries['IconStash/README.txt'])).toContain('Collection Export');
    expect(strFromU8(entries['IconStash/README.txt'])).toContain('16px, 32px, 48px, 64px, 128px, 256px, 512px');
  });

  it('enforces the 200-icon archive cap and deduplicates colliding filenames', () => {
    const manyIcons = makeSampleIcons(MAX_ZIP_ICONS + 15);
    const cappedZip = buildIconZipArchive({ icons: manyIcons, includeReadme: false });
    const cappedEntries = unzipSync(cappedZip);
    const manifest = JSON.parse(strFromU8(cappedEntries['IconStash/icons.json']));
    expect(manifest).toHaveLength(MAX_ZIP_ICONS);

    const dupIcons: ExportSvgInput[] = [
      { id: 'a1', name: 'star', librarySlug: 'lucide', svgMarkup: SAMPLE_SVG },
      { id: 'a2', name: 'star', librarySlug: 'lucide', svgMarkup: SAMPLE_SVG },
    ];
    const dupEntries = unzipSync(buildIconZipArchive({ icons: dupIcons, includeReadme: false }));
    expect(dupEntries['IconStash/lucide-star.svg']).toBeDefined();
    expect(dupEntries['IconStash/lucide-star-2.svg']).toBeDefined();
  });

  it('packs arbitrary entries via packZipEntries and StreamingZipBuilder', () => {
    const packed = packZipEntries([
      { path: '/IconStash/a.svg', data: SAMPLE_SVG },
      { path: 'IconStash/a-64.png', data: FAKE_PNG_BYTES },
    ]);
    const unpacked = unzipSync(packed);
    expect(strFromU8(unpacked['IconStash/a.svg'])).toBe(SAMPLE_SVG);
    expect(Array.from(unpacked['IconStash/a-64.png'])).toEqual(Array.from(FAKE_PNG_BYTES));

    const stream = new StreamingZipBuilder();
    stream.addText('IconStash/readme.txt', 'hello stream');
    stream.addBytes('IconStash/icon-32.png', FAKE_PNG_BYTES, 0);
    const streamedZip = stream.finish();
    const streamedEntries = unzipSync(streamedZip);
    expect(strFromU8(streamedEntries['IconStash/readme.txt'])).toBe('hello stream');
    expect(Array.from(streamedEntries['IconStash/icon-32.png'])).toEqual(Array.from(FAKE_PNG_BYTES));
  });
});

describe('Export Worker (OffscreenCanvas PNG + streaming fflate ZIP)', () => {
  it('calls bitmap.close() and resets OffscreenCanvas to 0x0 on success and failure', async () => {
    const bitmapClose = vi.fn();
    const drawImage = vi.fn();
    const clearRect = vi.fn();
    const fillRect = vi.fn();
    let lastCanvas: { width: number; height: number } | null = null;
    let shouldFailConvert = false;

    class MockOffscreenCanvas {
      width: number;
      height: number;
      constructor(w: number, h: number) {
        this.width = w;
        this.height = h;
        lastCanvas = this;
      }
      getContext() {
        return {
          clearRect,
          fillRect,
          drawImage,
          fillStyle: '',
        };
      }
      async convertToBlob() {
        if (shouldFailConvert) {
          throw new Error('GPU context lost');
        }
        return new Blob([FAKE_PNG_BYTES], { type: 'image/png' });
      }
    }

    vi.stubGlobal('OffscreenCanvas', MockOffscreenCanvas);
    vi.stubGlobal(
      'createImageBitmap',
      vi.fn(async () => ({ close: bitmapClose })),
    );

    const pngBuf = await rasterizeSvgToPngBuffer(SAMPLE_SVG, 128, 2, '#0A0A0A');
    expect(Array.from(new Uint8Array(pngBuf))).toEqual(Array.from(FAKE_PNG_BYTES));
    expect(bitmapClose).toHaveBeenCalledTimes(1);
    expect(drawImage).toHaveBeenCalledTimes(1);
    expect(fillRect).toHaveBeenCalledWith(0, 0, 256, 256);
    expect(lastCanvas).toMatchObject({ width: 0, height: 0 });

    // Verify cleanup still runs when convertToBlob rejects.
    shouldFailConvert = true;
    await expect(rasterizeSvgToPngBuffer(SAMPLE_SVG, 64)).rejects.toThrow('GPU context lost');
    expect(bitmapClose).toHaveBeenCalledTimes(2);
    expect(lastCanvas).toMatchObject({ width: 0, height: 0 });
  });

  it('injects xmlns, width, and height into SVG markup for rasterization', () => {
    const prepared = prepareSvgForRasterization('<svg viewBox="0 0 24 24"><path d="M0 0"/></svg>', 256);
    expect(prepared).toContain('xmlns="http://www.w3.org/2000/svg"');
    expect(prepared).toContain('width="256"');
    expect(prepared).toContain('height="256"');
  });

  it('processes EXPORT_PNG and transfers the ArrayBuffer', async () => {
    const messages: Array<{ msg: ExportWorkerResponse; transfer?: Transferable[] }> = [];
    const fakeRasterizer = vi.fn(async () => {
      const copy = new Uint8Array(FAKE_PNG_BYTES);
      return copy.buffer;
    });

    await processExportRequest(
      {
        type: 'EXPORT_PNG',
        jobId: 7,
        svgMarkup: SAMPLE_SVG,
        filename: 'lucide-home-128.png',
        size: 128,
      },
      {
        postMessage: (msg, transfer) => messages.push({ msg, transfer }),
      },
      fakeRasterizer,
    );

    const complete = messages.find((m) => m.msg.type === 'COMPLETE');
    expect(complete).toBeDefined();
    if (complete?.msg.type === 'COMPLETE') {
      expect(complete.msg.filename).toBe('lucide-home-128.png');
      expect(complete.msg.mimeType).toBe('image/png');
      expect(complete.transfer).toEqual([complete.msg.buffer]);
    }
  });

  it('processes EXPORT_ZIP sequentially, streams via fflate, and transfers Uint8Array.buffer', async () => {
    const messages: Array<{ msg: ExportWorkerResponse; transfer?: Transferable[] }> = [];
    let activeRasterizers = 0;
    let maxConcurrency = 0;

    const fakeRasterizer = vi.fn(async (_svg: string, size: number) => {
      activeRasterizers += 1;
      maxConcurrency = Math.max(maxConcurrency, activeRasterizers);
      await Promise.resolve();
      activeRasterizers -= 1;
      const bytes = new Uint8Array([...FAKE_PNG_BYTES, size & 0xff]);
      return bytes.buffer;
    });

    await processExportRequest(
      {
        type: 'EXPORT_ZIP',
        jobId: 42,
        icons: makeSampleIcons(2),
        pngSizes: [16, 64],
        includeManifest: true,
        includeReadme: true,
        archiveKind: 'compare',
        archiveTitle: 'arrow',
        filename: 'IconStash-compare-arrow.zip',
      },
      {
        postMessage: (msg, transfer) => messages.push({ msg, transfer }),
      },
      fakeRasterizer,
    );

    expect(maxConcurrency).toBe(1);
    expect(fakeRasterizer).toHaveBeenCalledTimes(4);

    const complete = messages.find((m) => m.msg.type === 'COMPLETE');
    expect(complete).toBeDefined();
    if (complete?.msg.type === 'COMPLETE') {
      expect(complete.msg.mimeType).toBe('application/zip');
      expect(complete.transfer).toEqual([complete.msg.buffer]);

      const unzipped = unzipSync(new Uint8Array(complete.msg.buffer));
      expect(Object.keys(unzipped).sort()).toEqual([
        'IconStash/README.txt',
        'IconStash/icons.json',
        'IconStash/lucide-icon-1-16.png',
        'IconStash/lucide-icon-1-64.png',
        'IconStash/lucide-icon-1.svg',
        'IconStash/lucide-icon-2-16.png',
        'IconStash/lucide-icon-2-64.png',
        'IconStash/lucide-icon-2.svg',
      ]);
      expect(strFromU8(unzipped['IconStash/README.txt'])).toContain('Cross-Library Compare Set');
    }
  });
});

describe('Export Client (URL.revokeObjectURL cleanup, lazy worker, fallback)', () => {
  it('immediately revokes Object URL on microtask inside downloadBlob so zero URLs leak', async () => {
    const createdUrls: string[] = [];
    const revokedUrls: string[] = [];
    const click = vi.fn();
    const remove = vi.fn();
    const appendChild = vi.fn();

    const createObjectURL = vi.spyOn(URL, 'createObjectURL').mockImplementation(() => {
      const url = `blob:iconstash-${createdUrls.length + 1}`;
      createdUrls.push(url);
      return url;
    });
    const revokeObjectURL = vi.spyOn(URL, 'revokeObjectURL').mockImplementation((url) => {
      revokedUrls.push(String(url));
    });

    vi.stubGlobal('document', {
      body: { appendChild },
      createElement: vi.fn(() => ({
        href: '',
        download: '',
        rel: '',
        style: { display: '' },
        click,
        remove,
      })),
    });

    downloadBlob(new Blob(['<svg/>'], { type: 'image/svg+xml' }), 'test.svg');

    expect(createObjectURL).toHaveBeenCalledTimes(1);
    expect(appendChild).toHaveBeenCalledTimes(1);
    expect(click).toHaveBeenCalledTimes(1);
    expect(remove).toHaveBeenCalledTimes(1);

    // Flush microtask queue
    await Promise.resolve();

    expect(revokeObjectURL).toHaveBeenCalledTimes(1);
    expect(revokedUrls).toEqual(createdUrls);
  });

  it('revokes Object URL synchronously in finally if anchor.click() throws', () => {
    const revokeObjectURL = vi.spyOn(URL, 'revokeObjectURL').mockImplementation(() => {});
    vi.spyOn(URL, 'createObjectURL').mockReturnValue('blob:iconstash-throw');

    const remove = vi.fn();
    vi.stubGlobal('document', {
      body: { appendChild: vi.fn() },
      createElement: vi.fn(() => ({
        href: '',
        download: '',
        rel: '',
        style: { display: '' },
        click: () => {
          throw new Error('Click blocked');
        },
        remove,
      })),
    });

    expect(() => downloadBlob(new Blob(['x']), 'fail.svg')).toThrow('Click blocked');
    expect(remove).toHaveBeenCalledTimes(1);
    expect(revokeObjectURL).toHaveBeenCalledWith('blob:iconstash-throw');
  });

  it('falls back to <canvas> PNG rasterizer when OffscreenCanvas is unavailable and cleans up resources', async () => {
    vi.stubGlobal('Worker', undefined);
    vi.stubGlobal('OffscreenCanvas', undefined);

    const revoked: string[] = [];
    vi.spyOn(URL, 'createObjectURL').mockReturnValue('blob:svg-fallback');
    vi.spyOn(URL, 'revokeObjectURL').mockImplementation((u) => revoked.push(String(u)));

    const mockCanvas = {
      width: 0,
      height: 0,
      getContext: vi.fn(() => ({
        clearRect: vi.fn(),
        fillRect: vi.fn(),
        drawImage: vi.fn(),
        fillStyle: '',
      })),
      toBlob: vi.fn((cb: (b: Blob | null) => void) => {
        cb(new Blob([FAKE_PNG_BYTES], { type: 'image/png' }));
      }),
    };

    vi.stubGlobal('document', {
      createElement: vi.fn(() => mockCanvas),
    });

    class MockImage {
      crossOrigin = '';
      onload: (() => void) | null = null;
      onerror: (() => void) | null = null;
      set src(_value: string) {
        queueMicrotask(() => this.onload?.());
      }
    }
    vi.stubGlobal('Image', MockImage);

    const blob = await rasterizeSvgFallback(SAMPLE_SVG, 64, 1);
    expect(blob.type).toBe('image/png');
    expect(Array.from(new Uint8Array(await blob.arrayBuffer()))).toEqual(Array.from(FAKE_PNG_BYTES));
    expect(revoked).toEqual(['blob:svg-fallback']);
    expect(mockCanvas.width).toBe(0);
    expect(mockCanvas.height).toBe(0);

    // Also verify exportPng uses fallback cleanly when Worker/OffscreenCanvas are absent.
    const pngResult = await exportPng({
      svgMarkup: SAMPLE_SVG,
      filename: 'lucide-fallback-64.png',
      size: 64,
      autoDownload: false,
    });
    expect(pngResult.filename).toBe('lucide-fallback-64.png');
    expect(pngResult.mimeType).toBe('image/png');
  });

  it('lazy-spawns the export worker and terminates it on Astro View Transition navigation', async () => {
    const docListeners = new Map<string, Set<() => void>>();
    const workerTerminate = vi.fn();
    let workerInstances = 0;

    class MockWorker {
      private listeners = new Map<string, Set<(ev: unknown) => void>>();
      constructor() {
        workerInstances += 1;
      }
      addEventListener(type: string, cb: (ev: unknown) => void) {
        if (!this.listeners.has(type)) this.listeners.set(type, new Set());
        this.listeners.get(type)!.add(cb);
      }
      removeEventListener(type: string, cb: (ev: unknown) => void) {
        this.listeners.get(type)?.delete(cb);
      }
      postMessage(req: { jobId: number; filename: string }) {
        const zip = buildIconZipArchive({ icons: makeSampleIcons(1) });
        const buf = zip.buffer.slice(zip.byteOffset, zip.byteOffset + zip.byteLength);
        queueMicrotask(() => {
          for (const cb of this.listeners.get('message') ?? []) {
            cb({
              data: {
                type: 'COMPLETE',
                jobId: req.jobId,
                filename: req.filename,
                mimeType: 'application/zip',
                buffer: buf,
              },
            });
          }
        });
      }
      terminate = workerTerminate;
    }

    vi.stubGlobal('Worker', MockWorker);
    vi.stubGlobal('document', {
      addEventListener: (type: string, cb: () => void) => {
        if (!docListeners.has(type)) docListeners.set(type, new Set());
        docListeners.get(type)!.add(cb);
      },
      removeEventListener: (type: string, cb: () => void) => {
        docListeners.get(type)?.delete(cb);
      },
    });

    expect(workerInstances).toBe(0);

    const res = await exportZip({
      icons: makeSampleIcons(1),
      autoDownload: false,
    });
    expect(workerInstances).toBe(1);
    expect(res.mimeType).toBe('application/zip');
    expect(docListeners.get('astro:before-swap')?.size).toBe(1);

    // Simulate Astro View Transition navigation
    for (const cb of [...(docListeners.get('astro:before-swap') ?? [])]) {
      cb();
    }

    expect(workerTerminate).toHaveBeenCalledTimes(1);
    expect(docListeners.get('astro:before-swap')?.size).toBe(0);
  });
});
