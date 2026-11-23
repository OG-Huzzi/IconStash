import {
  Zip,
  ZipDeflate,
  ZipPassThrough,
  strToU8,
  zipSync,
  type Zippable,
  type ZippableFile,
} from 'fflate';

/**
 * All 7 canonical PNG export sizes (16px–512px) defined in docs/baseline-audit.md.
 */
export const PNG_EXPORT_SIZES = [16, 32, 48, 64, 128, 256, 512] as const;

/**
 * Legacy detail-panel ZIP PNG sizes (omits 48px for backward compatibility when requested).
 */
export const DETAIL_ZIP_PNG_SIZES = [16, 32, 64, 128, 256, 512] as const;

export type PngExportSize = (typeof PNG_EXPORT_SIZES)[number];

/** Maximum number of icons permitted in a single ZIP archive (docs/baseline-audit.md §3.7). */
export const MAX_ZIP_ICONS = 200;

/** Default root directory inside every IconStash ZIP archive. */
export const DEFAULT_ZIP_ROOT_FOLDER = 'IconStash';

/** Supported ZIP archive presets. */
export type ZipArchiveKind = 'bulk' | 'compare' | 'collection' | 'detail';

export interface ExportSvgInput {
  id: string;
  name: string;
  librarySlug: string;
  svgMarkup: string;
  library?: string;
  tags?: string[];
  license?: string;
}

export interface ZipManifestEntry {
  id: string;
  name: string;
  library: string;
  librarySlug: string;
  tags: string[];
  svgFile: string;
  pngFiles?: string[];
}

export interface ZipEntryInput {
  /** Relative path inside the archive (normalized to forward slashes). */
  path: string;
  /** UTF-8 string or raw binary payload. */
  data: string | Uint8Array;
  /**
   * Compression level (0 = store/passthrough, 1-9 = deflate).
   * Defaults to 0 for already-compressed formats (.png, .jpg, .webp, .woff2) and 6 for text/SVG.
   */
  level?: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;
}

export interface BuildIconZipOptions {
  icons: ExportSvgInput[];
  /** Optional map of icon.id -> Map<size, Uint8Array> of pre-rasterized PNG bytes. */
  pngBuffers?: Map<string, Map<number, Uint8Array>>;
  /** Root folder inside the archive (defaults to 'IconStash'). */
  rootFolder?: string;
  /** Archive preset used for default README text and structure. */
  archiveKind?: ZipArchiveKind;
  /** Optional human-readable title (e.g. collection name or compared concept). */
  archiveTitle?: string;
  /** Include `icons.json` manifest inside the root folder (default: true). */
  includeManifest?: boolean;
  /** Include `README.txt` inside the root folder (default: true). */
  includeReadme?: boolean;
  /** Optional custom README content overriding the generated template. */
  readmeText?: string;
  /** Compression level for text files (SVG, JSON, README). Defaults to 6. */
  compressionLevel?: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;
}

/**
 * Sanitizes an icon or library identifier into a safe lowercase filename segment.
 * Mirrors legacy `slugFilePart` in `icons.js`.
 */
export function slugFilePart(value: string | undefined | null): string {
  const cleaned = String(value ?? 'icon')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
  return cleaned || 'icon';
}

/**
 * Returns the canonical filename for a single PNG export:
 * `{librarySlug}-{nameSlug}-{size}.png`.
 */
export function buildPngFilename(librarySlug: string, name: string, size: number): string {
  return `${slugFilePart(librarySlug)}-${slugFilePart(name)}-${Math.round(size)}.png`;
}

/**
 * Returns the canonical filename for a single SVG export:
 * `{librarySlug}-{nameSlug}.svg`.
 */
export function buildSvgFilename(librarySlug: string, name: string): string {
  return `${slugFilePart(librarySlug)}-${slugFilePart(name)}.svg`;
}

/**
 * Returns the default ZIP filename for a given archive preset.
 */
export function buildDefaultZipFilename(
  kind: ZipArchiveKind,
  title?: string,
  hasPngs = false,
): string {
  if (kind === 'collection') {
    const slug = slugFilePart(title || 'collection');
    return hasPngs ? `${slug}-png.zip` : `${slug}.zip`;
  }
  if (kind === 'compare') {
    const slug = title ? slugFilePart(title) : '';
    return slug ? `IconStash-compare-${slug}.zip` : 'IconStash-icons.zip';
  }
  if (kind === 'detail') {
    const slug = slugFilePart(title || 'icon');
    return `${slug}.zip`;
  }
  return 'IconStash-icons.zip';
}

/**
 * Validates and normalizes a list of requested PNG sizes (16..2048px, unique, ascending).
 */
export function normalizePngSizes(sizes: readonly number[] | undefined): number[] {
  if (!sizes || sizes.length === 0) return [];
  const seen = new Set<number>();
  for (const raw of sizes) {
    const n = Math.round(Number(raw));
    if (Number.isFinite(n) && n >= 16 && n <= 2048) {
      seen.add(n);
    }
  }
  return Array.from(seen).sort((a, b) => a - b);
}

/**
 * Normalizes an archive entry path to clean POSIX forward slashes with no leading slash
 * or parent-directory traversal segments.
 */
export function normalizeArchivePath(rawPath: string): string {
  const parts = String(rawPath)
    .replace(/\\/g, '/')
    .split('/')
    .filter((segment) => segment.length > 0 && segment !== '.' && segment !== '..');
  return parts.join('/');
}

/**
 * Builds the root folder prefix (`IconStash/` or empty string if rootFolder is blank).
 */
export function normalizeRootPrefix(rootFolder: string | undefined): string {
  const cleaned = normalizeArchivePath(rootFolder ?? DEFAULT_ZIP_ROOT_FOLDER);
  return cleaned ? `${cleaned}/` : '';
}

/**
 * Allocates a unique base filename (`{librarySlug}-{nameSlug}`, or `-2`, `-3`, ...)
 * so duplicate icon names within a ZIP archive never overwrite each other.
 */
export function createBaseNameAllocator(): (librarySlug: string, name: string) => string {
  const counts = new Map<string, number>();
  return (librarySlug: string, name: string): string => {
    const base = `${slugFilePart(librarySlug)}-${slugFilePart(name)}`;
    const prev = counts.get(base) ?? 0;
    counts.set(base, prev + 1);
    return prev === 0 ? base : `${base}-${prev + 1}`;
  };
}

/**
 * Generates a concise README.txt describing the IconStash ZIP export.
 */
export function buildArchiveReadme(params: {
  kind: ZipArchiveKind;
  title?: string;
  iconCount: number;
  pngSizes: readonly number[];
  includeManifest: boolean;
}): string {
  const kindLabel: Record<ZipArchiveKind, string> = {
    bulk: 'Bulk Selection Export',
    compare: 'Cross-Library Compare Set',
    collection: 'Collection Export',
    detail: 'Icon Asset Pack',
  };

  const lines: string[] = [
    `IconStash — ${kindLabel[params.kind]}`,
    ...(params.title ? [`Set: ${params.title}`] : []),
    `Icons: ${params.iconCount}`,
    `Formats: SVG${params.pngSizes.length > 0 ? ` + PNG (${params.pngSizes.map((s) => `${s}px`).join(', ')})` : ''}`,
    ...(params.includeManifest ? ['Manifest: icons.json'] : []),
    '',
    'Source: https://iconstash.io',
    'Note: Icons remain under their respective open-source library licenses.',
  ];

  return `${lines.join('\n')}\n`;
}

function isPrecompressedPath(path: string): boolean {
  return /\.(png|jpe?g|webp|gif|woff2|zip|gz|br)$/i.test(path);
}

/**
 * Packs an arbitrary list of entries (SVGs, PNGs, README, manifests) into a compact
 * `Uint8Array` ZIP archive using `fflate.zipSync`, clearing temporary references before returning.
 */
export function packZipEntries(
  entries: readonly ZipEntryInput[],
  defaultLevel: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 = 6,
): Uint8Array {
  let files: Zippable | null = Object.create(null) as Zippable;

  try {
    for (const entry of entries) {
      const cleanPath = normalizeArchivePath(entry.path);
      if (!cleanPath) continue;

      const bytes = typeof entry.data === 'string' ? strToU8(entry.data) : entry.data;
      const level = entry.level ?? (isPrecompressedPath(cleanPath) ? 0 : defaultLevel);
      const spec: ZippableFile = [bytes, { level }];
      files[cleanPath] = spec;
    }

    return zipSync(files);
  } finally {
    // Release every key/buffer reference immediately so GC can reclaim intermediates.
    if (files) {
      for (const key of Object.keys(files)) {
        delete files[key];
      }
      files = null;
    }
  }
}

/**
 * Builds a complete IconStash ZIP archive (SVGs, optional PNGs, `icons.json`, `README.txt`)
 * synchronously via `fflate.zipSync` with zero leftover references.
 */
export function buildIconZipArchive(options: BuildIconZipOptions): Uint8Array {
  const capped = options.icons.slice(0, MAX_ZIP_ICONS);
  const prefix = normalizeRootPrefix(options.rootFolder);
  const includeManifest = options.includeManifest !== false;
  const includeReadme = options.includeReadme !== false;
  const level = options.compressionLevel ?? 6;
  const archiveKind = options.archiveKind ?? 'bulk';
  const allocateBase = createBaseNameAllocator();

  const entries: ZipEntryInput[] = [];
  const manifest: ZipManifestEntry[] = [];
  const pngSizeSet = new Set<number>();

  for (const icon of capped) {
    const base = allocateBase(icon.librarySlug, icon.name);
    const svgFile = `${base}.svg`;
    entries.push({
      path: `${prefix}${svgFile}`,
      data: icon.svgMarkup,
      level,
    });

    const pngFiles: string[] = [];
    const iconPngs = options.pngBuffers?.get(icon.id);
    if (iconPngs && iconPngs.size > 0) {
      const sortedSizes = Array.from(iconPngs.keys()).sort((a, b) => a - b);
      for (const size of sortedSizes) {
        const bytes = iconPngs.get(size);
        if (!bytes) continue;
        pngSizeSet.add(size);
        const pngFile = `${base}-${size}.png`;
        pngFiles.push(pngFile);
        entries.push({
          path: `${prefix}${pngFile}`,
          data: bytes,
          level: 0, // PNGs are already compressed; store directly for speed & low RAM.
        });
      }
    }

    if (includeManifest) {
      const manifestItem: ZipManifestEntry = {
        id: icon.id,
        name: icon.name,
        library: icon.library ?? icon.librarySlug,
        librarySlug: icon.librarySlug,
        tags: icon.tags ? [...icon.tags] : [],
        svgFile,
      };
      if (pngFiles.length > 0) {
        manifestItem.pngFiles = pngFiles;
      }
      manifest.push(manifestItem);
    }
  }

  if (includeManifest) {
    entries.push({
      path: `${prefix}icons.json`,
      data: JSON.stringify(manifest, null, 2),
      level,
    });
  }

  if (includeReadme) {
    const readme =
      options.readmeText ??
      buildArchiveReadme({
        kind: archiveKind,
        title: options.archiveTitle,
        iconCount: capped.length,
        pngSizes: Array.from(pngSizeSet).sort((a, b) => a - b),
        includeManifest,
      });
    entries.push({
      path: `${prefix}README.txt`,
      data: readme,
      level,
    });
  }

  const archive = packZipEntries(entries, level);
  entries.length = 0;
  manifest.length = 0;
  return archive;
}

/**
 * Streaming ZIP builder backed by `fflate.Zip`.
 *
 * Allows the export worker to push each SVG and sequentially rasterized PNG directly
 * into the compressed output chunks without retaining uncompressed PNG buffers across icons.
 */
export class StreamingZipBuilder {
  private zip: Zip | null;
  private chunks: Uint8Array[] = [];
  private totalBytes = 0;
  private streamError: Error | null = null;
  private finalized = false;

  constructor() {
    this.zip = new Zip((err, chunk, final) => {
      if (err) {
        this.streamError = err;
        return;
      }
      if (chunk && chunk.byteLength > 0) {
        this.chunks.push(chunk);
        this.totalBytes += chunk.byteLength;
      }
      if (final) {
        this.finalized = true;
      }
    });
  }

  /** Appends a UTF-8 text entry (compressed via Deflate). */
  addText(
    path: string,
    text: string,
    level: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 = 6,
  ): void {
    this.addBytes(path, strToU8(text), level);
  }

  /** Appends a binary entry (stores with ZipPassThrough when level === 0). */
  addBytes(
    path: string,
    bytes: Uint8Array,
    level: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 = 0,
  ): void {
    if (!this.zip || this.finalized) {
      throw new Error('Cannot add entry after StreamingZipBuilder has been finalized or disposed.');
    }
    if (this.streamError) {
      throw this.streamError;
    }

    const cleanPath = normalizeArchivePath(path);
    if (!cleanPath) return;

    if (level === 0 || isPrecompressedPath(cleanPath)) {
      const file = new ZipPassThrough(cleanPath);
      this.zip.add(file);
      file.push(bytes, true);
    } else {
      const file = new ZipDeflate(cleanPath, { level });
      this.zip.add(file);
      file.push(bytes, true);
    }

    if (this.streamError) {
      throw this.streamError;
    }
  }

  /**
   * Finalizes the ZIP archive, concatenates output chunks into a single compact `Uint8Array`,
   * and immediately clears internal chunk references.
   */
  finish(): Uint8Array {
    if (!this.zip) {
      throw new Error('StreamingZipBuilder has already been finalized or disposed.');
    }

    try {
      this.zip.end();
      if (this.streamError) {
        throw this.streamError;
      }

      const output = new Uint8Array(this.totalBytes);
      let offset = 0;
      for (let i = 0; i < this.chunks.length; i += 1) {
        const chunk = this.chunks[i];
        output.set(chunk, offset);
        offset += chunk.byteLength;
      }
      return output;
    } finally {
      this.dispose();
    }
  }

  /** Releases all internal buffers and stream state immediately. */
  dispose(): void {
    this.chunks.length = 0;
    this.totalBytes = 0;
    this.zip = null;
    this.finalized = true;
  }
}
