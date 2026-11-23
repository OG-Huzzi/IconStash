import { describe, it, expect } from 'vitest';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import zlib from 'node:zlib';
import {
  buildIconTitle,
  buildIconDescription,
  generateIconPages,
} from '../../scripts/generate-icon-pages.mjs';

describe('Streaming 134k+ Icon HTML Generator', () => {
  it('enforces SEO title and description budgets', () => {
    const title = buildIconTitle('Lucide', 'A Arrow Down');
    expect(title.length).toBeLessThanOrEqual(60);
    expect(title).toContain('A Arrow Down');

    const longTitle = buildIconTitle('Material Symbols Light', 'Very Long Compound Multi Word Icon Name Example');
    expect(longTitle.length).toBeLessThanOrEqual(60);

    const desc = buildIconDescription('Lucide', 'A Arrow Down');
    expect(desc.length).toBeLessThanOrEqual(158);
    expect(desc).toContain('SVG and PNG');
  });

  it('streams icon HTML pages directly into a valid gzipped tar archive with low RAM', async () => {
    const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'iconstash-gen-'));
    const outDir = path.join(tmpDir, 'icons');
    const tarball = path.join(tmpDir, 'icons.tar.gz');

    const stats = await generateIconPages({
      limit: 50,
      outDir,
      tarballPath: tarball,
    });

    expect(stats.generated).toBe(50);
    expect(stats.tarballBytes).toBeGreaterThan(1000);
    expect(stats.peakRssMB).toBeLessThan(350);

    // Decompress tar.gz and verify POSIX ustar magic & HTML content
    const tarBuf = zlib.gunzipSync(fs.readFileSync(tarball));
    expect(tarBuf.subarray(257, 262).toString('ascii')).toBe('ustar');
    expect(tarBuf.toString('utf8')).toContain('https://iconstash.io/icons/');
    expect(tarBuf.toString('utf8')).toContain('application/ld+json');

    // Verify directory output has 50 icon folders with index.html
    const dirs = fs.readdirSync(outDir);
    expect(dirs.length).toBe(50);
    const sampleHtml = fs.readFileSync(path.join(outDir, dirs[0], 'index.html'), 'utf8');
    expect(sampleHtml).toContain('<link rel="canonical" href="https://iconstash.io/icons/');
    expect(sampleHtml).toContain('BreadcrumbList');

    fs.rmSync(tmpDir, { recursive: true, force: true });
  });
});
