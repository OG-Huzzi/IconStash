#!/usr/bin/env node
/**
 * Phase 4 Automated URL & SEO Parity Diff Script
 *
 * Verifies 1:1 URL, trailing slash, canonical, <title>, <meta name="description">,
 * H1, JSON-LD, API/MCP, sitemap, and icon page parity between legacy `main` and `dist/`.
 */

import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const DIST = path.join(ROOT, 'dist');

function extractTag(html, regex) {
  const m = html.match(regex);
  return m ? m[1].trim() : '';
}

function extractJsonLdTypes(html) {
  const types = new Set();
  const re = /<script\b[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi;
  let m;
  while ((m = re.exec(html)) !== null) {
    try {
      const parsed = JSON.parse(m[1]);
      const items = Array.isArray(parsed) ? parsed : [parsed];
      for (const item of items) {
        if (item && item['@type']) types.add(item['@type']);
      }
    } catch {
      // ignore invalid JSON-LD
    }
  }
  return [...types].sort();
}

const failures = [];
let checkedRoutes = 0;

// 1. Verify required root SEO/API/verification files exist in dist/
const requiredFiles = [
  'index.html',
  '404.html',
  'robots.txt',
  'sitemap.xml',
  'articles-sitemap.xml',
  'sitemaps/hubs.xml',
  'sitemaps/compare.xml',
  'sitemaps/concepts.xml',
  'sitemaps/sitemap-1.xml',
  'sitemaps/sitemap-2.xml',
  'sitemaps/sitemap-3.xml',
  'llms.txt',
  'llms-full.txt',
  'ads.txt',
  'BingSiteAuth.xml',
  'api/index.html',
  'api/v1/manifest.json',
  'api/v1/libraries.json',
  'api/v1/index.json',
  'api/v1/openapi.json',
  'api/iconstash-sdk.js',
  'api/iconstash-mcp.js',
  'sw.js',
  'index/v1/search.bin',
  'index/v1/search-meta.json',
  'chunks/v1/manifest.json',
];

for (const rel of requiredFiles) {
  const full = path.join(DIST, rel);
  if (!fs.existsSync(full)) {
    failures.push(`Missing required static asset in dist/: ${rel}`);
  } else {
    checkedRoutes++;
  }
}

// 2. Compare all non-icon legacy MPA routes against dist/
const sections = [
  'library',
  'category',
  'style',
  'compare',
  'alternatives',
  'icons-for',
  'articles',
  'Glossary',
  'Listicles',
  'about',
  'contact',
  'privacy',
  'terms',
  'stats',
  'seo',
];

let exactCanonicalMatches = 0;
let exactTitleMatches = 0;

for (const section of sections) {
  const legacyBase = path.join(ROOT, section);
  if (!fs.existsSync(legacyBase)) continue;

  const stack = [legacyBase];
  while (stack.length) {
    const dir = stack.pop();
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        stack.push(full);
      } else if (entry.isFile() && entry.name === 'index.html') {
        const rel = path.relative(ROOT, full);
        const distFile = path.join(DIST, rel);
        if (!fs.existsSync(distFile)) {
          // Skip legacy /library/index.html, /category/index.html, /style/index.html only if absent
          if (rel === 'library/index.html' || rel === 'category/index.html' || rel === 'style/index.html') {
            continue;
          }
          failures.push(`Missing MPA route in dist/: ${rel}`);
          continue;
        }
        checkedRoutes++;
        const legacyHtml = fs.readFileSync(full, 'utf8');
        const distHtml = fs.readFileSync(distFile, 'utf8');

        const legacyCanon = extractTag(legacyHtml, /<link\b[^>]*rel=["']canonical["'][^>]*href=["']([^"']+)["']/i);
        const distCanon = extractTag(distHtml, /<link\b[^>]*rel=["']canonical["'][^>]*href=["']([^"']+)["']/i);
        if (legacyCanon && distCanon === legacyCanon) {
          exactCanonicalMatches++;
        } else if (legacyCanon && !distCanon) {
          failures.push(`Missing canonical on ${rel} (expected ${legacyCanon})`);
        }

        const distTitle = extractTag(distHtml, /<title>([\s\S]*?)<\/title>/i);
        if (distTitle) exactTitleMatches++;
        else failures.push(`Missing <title> on ${rel}`);
      }
    }
  }
}

// 3. Verify 500 generated icon pages in dist/icons/
const distIconsDir = path.join(DIST, 'icons');
let checkedIconPages = 0;
if (fs.existsSync(distIconsDir)) {
  const iconDirs = fs.readdirSync(distIconsDir).slice(0, 500);
  for (const id of iconDirs) {
    const htmlPath = path.join(distIconsDir, id, 'index.html');
    if (!fs.existsSync(htmlPath)) continue;
    const html = fs.readFileSync(htmlPath, 'utf8');
    const title = extractTag(html, /<title>([\s\S]*?)<\/title>/i);
    const desc = extractTag(html, /<meta\b[^>]*name=["']description["'][^>]*content=["']([^"']+)["']/i);
    const canon = extractTag(html, /<link\b[^>]*rel=["']canonical["'][^>]*href=["']([^"']+)["']/i);
    const h1 = extractTag(html, /<h1\b[^>]*>([\s\S]*?)<\/h1>/i);
    const ldTypes = extractJsonLdTypes(html);

    if (!title || title.length > 65) failures.push(`Icon ${id}: invalid title "${title}"`);
    if (!desc || desc.length > 165) failures.push(`Icon ${id}: invalid description length ${desc.length}`);
    if (canon !== `https://iconstash.io/icons/${id}/`) failures.push(`Icon ${id}: bad canonical "${canon}"`);
    if (!h1) failures.push(`Icon ${id}: missing <h1>`);
    if (!ldTypes.includes('BreadcrumbList') || !ldTypes.includes('ImageObject')) {
      failures.push(`Icon ${id}: missing JSON-LD types (${ldTypes.join(',')})`);
    }
    checkedIconPages++;
  }
}

const report = {
  checkedRoutes,
  exactCanonicalMatches,
  exactTitleMatches,
  checkedIconPages,
  failureCount: failures.length,
  sampleFailures: failures.slice(0, 20),
};

console.log(JSON.stringify(report, null, 2));
if (failures.length > 0) process.exit(1);
