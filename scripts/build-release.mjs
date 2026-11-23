#!/usr/bin/env node
/**
 * One-command Production Release Builder for IconStash v2
 *
 * 1. Builds sharded library chunks & binary search index (public/chunks/v1, public/index/v1)
 * 2. Builds Astro 7 static MPA shell & all 546 core/editorial/hub/compare/SEO routes (dist/)
 * 3. Copies the 28 canonical master data/{slug}.json + data/index.json into dist/data/
 *    for 100% @iconstash/sdk & iconstash-mcp compatibility (excluding legacy duplicates)
 * 4. Streams all 134,701 individual icon HTML pages directly into release/iconstash-icons.tar.gz
 *    (or pass --smoke to generate 500 pages into dist/icons for quick verification)
 */

import fs from 'node:fs';
import path from 'node:path';
import { execSync } from 'node:child_process';
import { generateIconPages } from './generate-icon-pages.mjs';

const ROOT = process.cwd();
const args = process.argv.slice(2);
const smoke = args.includes('--smoke');

console.log('[1/4] Building sharded chunks & binary search index...');
execSync('npm run build:data', { stdio: 'inherit' });

console.log('[2/4] Building Astro 7 static MPA (546 routes)...');
execSync('npm run build', { stdio: 'inherit' });

console.log('[3/4] Copying 28 canonical master data/*.json files to dist/data/ for SDK & MCP...');
const indexJson = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/index.json'), 'utf8'));
const distDataDir = path.join(ROOT, 'dist/data');
fs.mkdirSync(distDataDir, { recursive: true });
fs.copyFileSync(path.join(ROOT, 'data/index.json'), path.join(distDataDir, 'index.json'));
let copied = 1;
for (const lib of indexJson.libraries || []) {
  const src = path.join(ROOT, 'data', `${lib.slug}.json`);
  if (fs.existsSync(src)) {
    fs.copyFileSync(src, path.join(distDataDir, `${lib.slug}.json`));
    copied++;
  }
}
console.log(`Copied ${copied} canonical JSON files into dist/data/`);

if (smoke) {
  console.log('[4/4] Generating 500 smoke icon pages into dist/icons/...');
  const stats = await generateIconPages({ limit: 500, outDir: path.join(ROOT, 'dist/icons') });
  console.log('Smoke generation complete:', stats);
} else {
  console.log('[4/4] Streaming all 134,701 icon HTML pages into release/iconstash-icons.tar.gz...');
  const stats = await generateIconPages({
    tarballPath: path.join(ROOT, 'release/iconstash-icons.tar.gz'),
  });
  console.log('Full release tarball complete:', stats);
}
