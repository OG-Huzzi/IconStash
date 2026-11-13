/**
 * generate-api.js — builds the small static files for the public IconStash API.
 *
 * The API deliberately adds NO icon data. Library payloads are the site's
 * existing public data/<slug>.json files served directly (no rewrite, no copy),
 * so this script only writes the small metadata documents under api/v1/:
 *
 *   api/v1/manifest.json   service metadata, counts, licences, endpoints
 *   api/v1/libraries.json  the 28-library catalogue (with licences)
 *   api/v1/index.json      compact search index (no SVG data)
 *   api/v1/openapi.json    OpenAPI 3.1 description
 *
 * The compact index is intentionally small: it carries only the fields needed
 * to find an icon. Full svgPath data stays in the existing library payloads.
 *
 * Run:  node scripts/generate-api.js
 * It is idempotent and safe to re-run whenever the icon data changes.
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const API_DIR = path.join(ROOT, 'api', 'v1');
const SITE = 'https://iconstash.io';
const BASE = `${SITE}/api/v1`;
const VERSION = '1.0.0';

// Source of truth for these fields is scripts/generate-hubs.js (LIBRARIES).
// Kept here so the API generator has no dependency on that build script.
const META = {
  lucide:               { license: 'ISC',         style: 'Outline',                    grid: '24x24' },
  tabler:               { license: 'MIT',         style: 'Outline',                    grid: '24x24' },
  phosphor:             { license: 'MIT',         style: 'Six weights',                grid: '24x24' },
  material:             { license: 'Apache 2.0',  style: 'Five themes',                grid: '24x24' },
  remix:                { license: 'Apache 2.0',  style: 'Line & fill',                grid: '24x24' },
  iconoir:              { license: 'MIT',         style: 'Outline',                    grid: '24x24' },
  heroicons:            { license: 'MIT',         style: 'Outline & solid',            grid: '16/20/24' },
  bootstrap:            { license: 'MIT',         style: 'Multi-style',                grid: '16x16' },
  feather:              { license: 'MIT',         style: 'Outline',                    grid: '24x24' },
  mingcute:             { license: 'Apache 2.0',  style: 'Line & fill',                grid: '24x24' },
  solar:                { license: 'CC BY 4.0',   style: 'Six styles',                 grid: '24x24' },
  octicons:             { license: 'MIT',         style: 'Outline',                    grid: '16x16' },
  cssgg:                { license: 'MIT',         style: 'Outline',                    grid: '24x24' },
  radix:                { license: 'MIT',         style: 'Outline',                    grid: '15x15' },
  antdesign:            { license: 'MIT',         style: 'Outlined, filled & two-tone',grid: '24x24' },
  fluent:               { license: 'MIT',         style: 'Regular & filled',           grid: '12-48' },
  carbon:               { license: 'Apache 2.0',  style: 'Outline',                    grid: '32x32' },
  ionicons:             { license: 'MIT',         style: 'Outline, filled & sharp',    grid: '24x24' },
  eva:                  { license: 'MIT',         style: 'Fill & outline',             grid: '24x24' },
  boxicons:             { license: 'MIT',         style: 'Regular, solid & logos',     grid: '24x24' },
  materialsymbols:      { license: 'Apache 2.0',  style: 'Variable',                   grid: '24x24' },
  materialsymbolslight: { license: 'Apache 2.0',  style: 'Light (300 weight)',         grid: '24x24' },
  iconparkoutline:      { license: 'Apache 2.0',  style: 'Outline',                    grid: '24x24' },
  iconparksolid:        { license: 'Apache 2.0',  style: 'Filled',                     grid: '24x24' },
  hugeicons:            { license: 'MIT',         style: 'Six styles',                 grid: '24x24' },
  pixelarticons:        { license: 'MIT',         style: 'Pixel',                      grid: '24x24' },
  linemd:               { license: 'MIT',         style: 'Animated',                   grid: '24x24' },
  simpleicons:          { license: 'CC0 1.0',     style: 'Filled (brand)',             grid: '24x24' }
};

const ATTRIBUTION_REQUIRED = new Set(['CC BY 4.0']);

function readJson(rel) {
  return JSON.parse(fs.readFileSync(path.join(ROOT, rel), 'utf8'));
}

function writeJson(rel, value) {
  const dest = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  const body = JSON.stringify(value, null, 2) + '\n';
  fs.writeFileSync(dest, body, 'utf8');
  return Buffer.byteLength(body);
}

function writeRaw(rel, body) {
  const dest = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.writeFileSync(dest, body, 'utf8');
  return Buffer.byteLength(body);
}

// Build the two one-file downloads the docs point at. The npm package is the
// source of truth; these bundles just make the SDK and MCP server usable
// without a package manager (the API stays frontend-only either way).
function buildStandaloneFiles() {
  const sdk = fs.readFileSync(path.join(ROOT, 'packages', 'iconstash', 'index.js'), 'utf8');
  const mcp = fs.readFileSync(path.join(ROOT, 'packages', 'iconstash', 'mcp.js'), 'utf8');

  const sdkBundle = '// IconStash SDK — generated single-file build. Do not edit.\n' +
    '// Source: packages/iconstash/index.js. Regenerate: node scripts/generate-api.js\n\n' +
    sdk;

  const sdkBody = sdk
    .replace(/^'use strict';\s*/, '')
    .replace(/\nmodule\.exports\s*=\s*\{[\s\S]*?\};\s*$/, '\n');
  const mcpBody = mcp
    .replace(/^#![^\n]*\n/, '')
    .replace(/^'use strict';\s*/, '')
    .replace(/const \{ createClient \} = require\('\.\/index\.js'\);\s*/, '');

  const mcpBundle = '#!/usr/bin/env node\n' +
    '// IconStash MCP server — generated single-file build. Do not edit.\n' +
    '// Source: packages/iconstash/{index.js,mcp.js}. Regenerate: node scripts/generate-api.js\n' +
    '// Usage: node iconstash-mcp.js (Node 18+, no install, no API key)\n' +
    "'use strict';\n\n" + sdkBody + '\n' + mcpBody;

  return {
    'api/iconstash-sdk.js': writeRaw('api/iconstash-sdk.js', sdkBundle),
    'api/iconstash-mcp.js': writeRaw('api/iconstash-mcp.js', mcpBundle)
  };
}

const index = readJson('data/index.json');
const libraries = (index.libraries || []).map((lib) => {
  const meta = META[lib.slug] || {};
  const license = meta.license || 'See upstream project';
  return {
    slug: lib.slug,
    name: lib.name,
    count: Number(lib.count) || 0,
    version: lib.version || null,
    description: lib.description || '',
    license,
    attributionRequired: ATTRIBUTION_REQUIRED.has(license),
    style: meta.style || null,
    grid: meta.grid || null,
    npm: lib.npmPackage || null,
    docsUrl: lib.docsUrl || null,
    hubUrl: `${SITE}/library/${lib.slug}/`,
    dataUrl: `${SITE}/data/${lib.slug}.json`
  };
});

const totalIcons = libraries.reduce((sum, lib) => sum + lib.count, 0);
const zeroAttribution = libraries
  .filter((lib) => !lib.attributionRequired)
  .reduce((sum, lib) => sum + lib.count, 0);

const endpoints = [
  { path: '/api/v1/manifest.json', description: 'Service metadata, version and endpoint list.' },
  { path: '/api/v1/libraries.json', description: 'The 28-library catalogue with licences.' },
  { path: '/api/v1/index.json', description: 'Compact search index over all icons (no SVG data).' },
  { path: '/data/{slug}.json', description: 'Full icon array for one library (existing public data file, no copy).' },
  { path: '/api/v1/openapi.json', description: 'OpenAPI 3.1 description of this API.' }
];

const manifest = {
  name: 'IconStash API',
  version: VERSION,
  apiBase: BASE,
  docs: `${SITE}/api/`,
  website: `${SITE}/`,
  description: 'Free, keyless, read-only access to 134,701 open-source SVG icons across 28 libraries. No signup, no rate limit, CORS enabled.',
  licenseNote: 'Icons belong to their upstream authors. Check the per-library licence; only CC BY 4.0 sets require attribution.',
  dataSnapshot: index.generatedAt || null,
  generatedAt: new Date().toISOString().slice(0, 10),
  counts: {
    libraries: libraries.length,
    icons: totalIcons,
    zeroAttributionIcons: zeroAttribution,
    attributionRequiredIcons: totalIcons - zeroAttribution
  },
  endpoints,
  sdk: {
    name: '@iconstash/sdk',
    location: 'packages/iconstash/',
    downloadUrl: `${SITE}/api/iconstash-sdk.js`
  },
  mcp: {
    name: 'iconstash-mcp',
    location: 'packages/iconstash/mcp.js',
    downloadUrl: `${SITE}/api/iconstash-mcp.js`
  },
  terms: {
    authentication: 'none',
    rateLimit: 'none',
    cors: '*',
    methods: ['GET', 'HEAD', 'OPTIONS'],
    cost: 'free'
  }
};

const iconSchema = {
  type: 'object',
  properties: {
    id: { type: 'string', description: 'Globally unique icon id, e.g. lucide-camera' },
    name: { type: 'string' },
    library: { type: 'string' },
    librarySlug: { type: 'string' },
    libraryVersion: { type: 'string' },
    category: { type: 'string' },
    subCategory: { type: 'string' },
    style: { type: 'string' },
    tags: { type: 'array', items: { type: 'string' } },
    svgPath: { type: 'string', description: 'Inner SVG markup (paths/shapes), without the <svg> wrapper' },
    viewBox: { type: 'string' },
    strokeWidth: { type: 'number' },
    docsUrl: { type: 'string' },
    npmPackage: { type: 'string' },
    jsxImport: { type: 'string' }
  }
};

const librarySchema = {
  type: 'object',
  properties: {
    slug: { type: 'string' }, name: { type: 'string' }, count: { type: 'integer' },
    version: { type: 'string', nullable: true }, description: { type: 'string' },
    license: { type: 'string' }, attributionRequired: { type: 'boolean' },
    style: { type: 'string', nullable: true }, grid: { type: 'string', nullable: true },
    npm: { type: 'string', nullable: true }, docsUrl: { type: 'string', nullable: true },
    hubUrl: { type: 'string' }, dataUrl: { type: 'string' }
  }
};

const openapi = {
  openapi: '3.1.0',
  info: {
    title: 'IconStash API',
    version: VERSION,
    description: manifest.description,
    contact: { name: 'IconStash', url: `${SITE}/contact/` },
    license: { name: 'See per-library licence', url: `${SITE}/terms/` }
  },
  servers: [{ url: SITE, description: 'Production (static, CDN-cached)' }],
  tags: [{ name: 'catalogue' }, { name: 'icons' }],
  paths: {
    '/api/v1/manifest.json': {
      get: { tags: ['catalogue'], summary: 'Service manifest', operationId: 'getManifest',
        responses: { 200: { description: 'OK', content: { 'application/json': { schema: { type: 'object' } } } } } }
    },
    '/api/v1/libraries.json': {
      get: { tags: ['catalogue'], summary: 'List all icon libraries', operationId: 'listLibraries',
        responses: { 200: { description: 'OK', content: { 'application/json': { schema: { type: 'array', items: librarySchema } } } } } }
    },
    '/api/v1/index.json': {
      get: { tags: ['icons'], summary: 'Compact search index over all icons', operationId: 'getIndex',
        responses: { 200: { description: 'OK', content: { 'application/json': { schema: { type: 'object' } } } } } }
    },
    '/data/{slug}.json': {
      get: { tags: ['icons'], summary: 'All icons in one library (existing public data file)', operationId: 'getLibrary',
        parameters: [{ name: 'slug', in: 'path', required: true, schema: { type: 'string' }, description: 'Library slug, e.g. lucide' }],
        responses: {
          200: { description: 'OK', content: { 'application/json': { schema: { type: 'array', items: iconSchema } } } },
          404: { description: 'Unknown library' }
        } }
    },
    '/api/v1/openapi.json': {
      get: { tags: ['catalogue'], summary: 'This document', operationId: 'getOpenApi',
        responses: { 200: { description: 'OK', content: { 'application/json': { schema: { type: 'object' } } } } } }
    }
  }
};

// Compact search index. Positional arrays keep it small:
//   [id, name, libraryIndex, categoryIndex, styleIndex, "tag1 tag2 ..."]
// Categories/styles are shared dictionaries; tags are a single space-joined
// string. The SDK expands these back into objects.
function buildCompactIndex(libraries) {
  const slugs = libraries.map((lib) => lib.slug);
  const categories = [];
  const styles = [];
  const catIds = new Map();
  const styleIds = new Map();
  const rows = [];

  const intern = (value, list, ids) => {
    const key = String(value || '').toLowerCase();
    if (!ids.has(key)) { ids.set(key, list.length); list.push(key); }
    return ids.get(key);
  };

  for (let libIndex = 0; libIndex < slugs.length; libIndex += 1) {
    const slug = slugs[libIndex];
    const file = path.join(ROOT, 'data', `${slug}.json`);
    if (!fs.existsSync(file)) continue;
    let icons;
    try { icons = JSON.parse(fs.readFileSync(file, 'utf8')); } catch (_) { continue; }
    if (!Array.isArray(icons)) continue;
    for (const icon of icons) {
      if (!icon || !icon.id || !icon.name) continue;
      // Tags that are already tokens of the name add no search signal but are
      // the bulk of the index size, so drop them.
      const nameTokens = new Set(String(icon.name).toLowerCase().split(/[^a-z0-9]+/).filter(Boolean));
      const tags = Array.isArray(icon.tags)
        ? [...new Set(icon.tags.map((tag) => String(tag).toLowerCase()))]
            .filter((tag) => tag && !nameTokens.has(tag))
            .join(' ')
        : '';
      rows.push([
        icon.id,
        icon.name,
        libIndex,
        intern(icon.category, categories, catIds),
        intern(icon.style, styles, styleIds),
        tags
      ]);
    }
  }
  return {
    version: 1,
    format: ['id', 'name', 'library', 'category', 'style', 'tags'],
    libraries: slugs,
    categories,
    styles,
    icons: rows
  };
}

const compactIndex = buildCompactIndex(libraries);

const sizes = {
  'api/v1/manifest.json': writeJson('api/v1/manifest.json', manifest),
  'api/v1/libraries.json': writeJson('api/v1/libraries.json', libraries),
  'api/v1/index.json': writeJson('api/v1/index.json', compactIndex),
  'api/v1/openapi.json': writeJson('api/v1/openapi.json', openapi),
  ...buildStandaloneFiles()
};

console.log('IconStash static API generated:');
for (const [file, bytes] of Object.entries(sizes)) console.log(`  ${file}  ${(bytes / 1024).toFixed(1)} KB`);
console.log(`  libraries: ${libraries.length}, icons: ${totalIcons.toLocaleString('en-US')}`);
console.log('  library payloads are the existing data/<slug>.json files (no copy, no rewrite)');
console.log('  standalone SDK/MCP downloads are generated from packages/iconstash');
