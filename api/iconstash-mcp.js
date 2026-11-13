#!/usr/bin/env node
// IconStash MCP server — generated single-file build. Do not edit.
// Source: packages/iconstash/{index.js,mcp.js}. Regenerate: node scripts/generate-api.js
// Usage: node iconstash-mcp.js (Node 18+, no install, no API key)
'use strict';

/**
 * IconStash SDK — zero dependencies, works in Node 18+ and browsers.
 *
 * The API is entirely static: no key, no signup, no rate limit.
 * Search runs locally over a small compact index; full SVG data is fetched
 * only for the library of the icon you actually pick.
 *
 *   const { createClient } = require('@iconstash/sdk');
 *   const icons = createClient();
 *   const hits = await icons.search('camera', { limit: 5 });
 *   const svg  = await icons.svg(hits[0].id, { color: '#2563eb', size: 32 });
 */

const DEFAULT_BASE = 'https://iconstash.io/api/v1';
const TOKEN_SPLIT = /[^a-z0-9]+/;

function normalize(value) {
  return String(value == null ? '' : value).toLowerCase();
}

function tokenize(value) {
  return normalize(value).split(TOKEN_SPLIT).filter(Boolean);
}

function expandIndex(raw) {
  const out = [];
  for (const row of raw.icons) {
    out.push({
      id: row[0],
      name: row[1],
      librarySlug: raw.libraries[row[2]] || '',
      category: raw.categories[row[3]] || '',
      style: raw.styles[row[4]] || '',
      tags: row[5] ? row[5].split(' ').filter(Boolean) : [],
      // Precomputed haystack for scoring (tags already exclude name tokens).
      _hay: `${normalize(row[1])} ${row[5] || ''} ${normalize(raw.categories[row[3]] || '')} ${normalize(raw.styles[row[4]] || '')}`
    });
  }
  return out;
}

function scoreIcon(icon, words, query) {
  const name = normalize(icon.name);
  const nameTokens = new Set(name.split(TOKEN_SPLIT).filter(Boolean));
  let score = 0;
  if (name === query) score += 100;
  else if (name.startsWith(query)) score += 55;
  else if (name.includes(query)) score += 35;
  for (const word of words) {
    if (nameTokens.has(word)) score += 18;
    else if (icon._hay.includes(word)) score += 5;
  }
  return score;
}

function svgMarkup(icon, options) {
  const size = options.size || 24;
  const color = options.color || 'currentColor';
  const strokeWidth = options.strokeWidth == null ? (icon.strokeWidth || 2) : options.strokeWidth;
  const viewBox = icon.viewBox || '0 0 24 24';
  const filled = /fill|solid|bold/i.test(String(icon.style || ''));
  const paint = filled
    ? `fill="${color}" stroke="none"`
    : `fill="none" stroke="${color}" stroke-width="${strokeWidth}" stroke-linecap="round" stroke-linejoin="round"`;
  const body = icon.svgPath || '';
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${viewBox}" width="${size}" height="${size}" ${paint} role="img" aria-label="${icon.name} icon">${body}</svg>`;
}

function createClient(options = {}) {
  const base = String(options.base || DEFAULT_BASE).replace(/\/+$/, '');
  const fetchImpl = options.fetch || (typeof fetch !== 'undefined' ? fetch : null);
  if (!fetchImpl) throw new Error('No fetch implementation available; pass options.fetch.');

  const caches = { manifest: null, libraries: null, index: null, payloads: new Map() };

  async function getJson(url) {
    const response = await fetchImpl(url, { headers: { Accept: 'application/json' } });
    if (!response.ok) throw new Error(`IconStash API ${response.status} for ${url}`);
    return response.json();
  }

  async function manifest() {
    if (!caches.manifest) caches.manifest = await getJson(`${base}/manifest.json`);
    return caches.manifest;
  }

  async function libraries() {
    if (!caches.libraries) caches.libraries = await getJson(`${base}/libraries.json`);
    return caches.libraries;
  }

  async function library(slug) {
    const key = normalize(slug);
    if (!caches.payloads.has(key)) {
      // Library payloads are the site's existing public data files — no copy,
      // no rewrite, fully static and CDN-cached.
      const siteRoot = base.replace(/\/api\/v1\/?$/, '');
      caches.payloads.set(key, getJson(`${siteRoot}/data/${encodeURIComponent(key)}.json`));
    }
    return caches.payloads.get(key);
  }

  async function search(query, searchOptions = {}) {
    const q = normalize(String(query || '').trim());
    if (!q) return [];
    if (!caches.index) {
      const raw = await getJson(`${base}/index.json`);
      caches.index = expandIndex(raw);
    }
    const words = tokenize(q);
    const libFilter = searchOptions.library ? normalize(searchOptions.library) : null;
    const catFilter = searchOptions.category ? normalize(searchOptions.category) : null;
    const styleFilter = searchOptions.style ? normalize(searchOptions.style) : null;

    const scored = [];
    for (const icon of caches.index) {
      if (libFilter && icon.librarySlug !== libFilter) continue;
      if (catFilter && normalize(icon.category) !== catFilter) continue;
      if (styleFilter && normalize(icon.style) !== styleFilter) continue;
      const score = scoreIcon(icon, words, q);
      if (score > 0) scored.push({ icon, score });
    }
    scored.sort((a, b) => b.score - a.score || a.icon.name.localeCompare(b.icon.name));
    const limit = Math.max(1, Math.min(Number(searchOptions.limit) || 20, 500));
    return scored.slice(0, limit).map(({ icon, score }) => ({
      id: icon.id,
      name: icon.name,
      library: icon.librarySlug,
      category: icon.category,
      style: icon.style,
      tags: icon.tags,
      score,
      url: `https://iconstash.io/icons/${icon.id}/`
    }));
  }

  async function getIcon(id) {
    const key = String(id || '');
    if (!key) throw new Error('An icon id is required, e.g. lucide-camera');
    const slug = key.split('-')[0];
    const payload = await library(slug);
    const icon = payload.find((entry) => entry && entry.id === key);
    if (!icon) throw new Error(`Icon not found: ${key}`);
    const libs = await libraries();
    const meta = libs.find((entry) => entry.slug === slug) || {};
    const siteRoot = base.replace(/\/api\/v1\/?$/, '');
    return {
      ...icon,
      license: meta.license || null,
      attributionRequired: meta.attributionRequired === true,
      libraryName: meta.name || slug,
      url: `https://iconstash.io/icons/${key}/`,
      dataUrl: `${siteRoot}/data/${slug}.json`
    };
  }

  async function svg(id, svgOptions = {}) {
    const icon = await getIcon(id);
    return svgMarkup(icon, svgOptions);
  }

  async function snippet(id, format = 'svg', snippetOptions = {}) {
    const icon = await getIcon(id);
    const markup = svgMarkup(icon, snippetOptions);
    switch (normalize(format)) {
      case 'jsx': {
        const parts = String(icon.name).split(/[-_\s]+/).filter(Boolean)
          .map((part) => part.charAt(0).toUpperCase() + part.slice(1)).join('');
        return `export const ${parts || 'Icon'} = (props) => (${markup.replace('<svg ', '<svg {...props} ')});`;
      }
      case 'css':
        return `.icon-${icon.name} { width: 1em; height: 1em; background-color: currentColor; mask: url("data:image/svg+xml,${encodeURIComponent(markup)}") center / contain no-repeat; }`;
      case 'html':
        return `<img src="data:image/svg+xml,${encodeURIComponent(markup)}" width="24" height="24" alt="${icon.name} icon">`;
      case 'datauri':
        return `data:image/svg+xml,${encodeURIComponent(markup)}`;
      default:
        return markup;
    }
  }

  async function compare(concept, compareOptions = {}) {
    const raw = await search(concept, { limit: 400 });
    const libs = await libraries();
    const byLibrary = new Map();
    for (const hit of raw) {
      if (!byLibrary.has(hit.library)) byLibrary.set(hit.library, hit);
    }
    const limit = Math.max(1, Math.min(Number(compareOptions.limit) || 28, 28));
    return libs
      .filter((lib) => byLibrary.has(lib.slug))
      .slice(0, limit)
      .map((lib) => ({ ...byLibrary.get(lib.slug), libraryName: lib.name, license: lib.license, attributionRequired: lib.attributionRequired }));
  }

  return { base, manifest, libraries, library, search, getIcon, svg, snippet, compare };
}


/**
 * IconStash MCP server — zero dependencies, stdio JSON-RPC 2.0.
 *
 * Run directly:  node packages/iconstash/mcp.js
 * Or in an MCP client config:
 *   { "mcpServers": { "iconstash": { "command": "npx", "args": ["-y", "@iconstash/sdk", "iconstash-mcp"] } } }
 *
 * It is a client-side process on the user's machine: nothing is hosted, no
 * API key is needed, and it reads the same static API as the website.
 */

const SERVER_INFO = { name: 'iconstash', version: '1.0.0' };
const PROTOCOL_VERSION = '2024-11-05';

const TOOLS = [
  {
    name: 'search_icons',
    description: 'Search 134,701 free open-source SVG icons across 28 libraries by keyword. Returns ids, names, libraries, licences and canonical URLs.',
    inputSchema: {
      type: 'object',
      properties: {
        query: { type: 'string', description: 'Search term, e.g. "camera", "arrow down", "shopping cart"' },
        library: { type: 'string', description: 'Optional library slug filter, e.g. lucide, tabler, phosphor' },
        category: { type: 'string', description: 'Optional category filter, e.g. media, navigation' },
        style: { type: 'string', description: 'Optional style filter, e.g. outline, fill, bold' },
        limit: { type: 'number', description: 'Max results (1-500, default 20)' }
      },
      required: ['query']
    }
  },
  {
    name: 'get_icon',
    description: 'Get the full record for one icon by id, including svgPath, viewBox, tags and licence.',
    inputSchema: {
      type: 'object',
      properties: { id: { type: 'string', description: 'Icon id, e.g. lucide-camera' } },
      required: ['id']
    }
  },
  {
    name: 'get_svg',
    description: 'Render one icon as ready-to-use SVG markup (or JSX / CSS / HTML / data URI).',
    inputSchema: {
      type: 'object',
      properties: {
        id: { type: 'string', description: 'Icon id, e.g. lucide-camera' },
        color: { type: 'string', description: 'Stroke/fill colour, e.g. #2563eb' },
        size: { type: 'number', description: 'Width/height in px (default 24)' },
        strokeWidth: { type: 'number', description: 'Stroke width for outline icons' },
        format: { type: 'string', description: 'svg (default), jsx, css, html or datauri' }
      },
      required: ['id']
    }
  },
  {
    name: 'compare_concept',
    description: 'Unique to IconStash: show how all 28 libraries draw the same concept (e.g. "camera", "trash", "home"), with each library\'s licence.',
    inputSchema: {
      type: 'object',
      properties: {
        concept: { type: 'string', description: 'Concept name, e.g. camera, trash, home' },
        limit: { type: 'number', description: 'Max libraries (default 28)' }
      },
      required: ['concept']
    }
  },
  {
    name: 'list_libraries',
    description: 'List all 28 icon libraries with icon counts, licences, npm packages and attribution requirements.',
    inputSchema: { type: 'object', properties: {} }
  }
];

function textResult(value) {
  return { content: [{ type: 'text', text: typeof value === 'string' ? value : JSON.stringify(value, null, 2) }] };
}

function errorResult(message) {
  return { content: [{ type: 'text', text: `IconStash error: ${message}` }], isError: true };
}

async function callTool(client, name, args) {
  switch (name) {
    case 'search_icons': {
      if (!args || !String(args.query || '').trim()) throw new Error('query is required');
      const results = await client.search(args.query, args);
      return textResult({ query: args.query, count: results.length, results });
    }
    case 'get_icon': {
      if (!args || !args.id) throw new Error('id is required');
      return textResult(await client.getIcon(args.id));
    }
    case 'get_svg': {
      if (!args || !args.id) throw new Error('id is required');
      const format = String(args.format || 'svg').toLowerCase();
      const opts = {};
      if (args.color) opts.color = args.color;
      if (args.size) opts.size = Number(args.size);
      if (args.strokeWidth != null) opts.strokeWidth = Number(args.strokeWidth);
      const markup = await client.svg(args.id, opts);
      return textResult(format === 'svg' ? markup : await client.snippet(args.id, format, opts));
    }
    case 'compare_concept': {
      if (!args || !String(args.concept || '').trim()) throw new Error('concept is required');
      const variants = await client.compare(args.concept, args);
      return textResult({ concept: args.concept, libraries: variants.length, variants });
    }
    case 'list_libraries': {
      const libs = await client.libraries();
      return textResult({ count: libs.length, libraries: libs });
    }
    default:
      throw new Error(`Unknown tool: ${name}`);
  }
}

function reply(id, result) {
  process.stdout.write(`${JSON.stringify({ jsonrpc: '2.0', id, result })}\n`);
}

function replyError(id, code, message) {
  process.stdout.write(`${JSON.stringify({ jsonrpc: '2.0', id, error: { code, message } })}\n`);
}

async function handle(message, client) {
  const { id, method, params } = message || {};
  const isNotification = id === undefined || id === null;

  if (method === 'initialize') {
    return reply(id, {
      protocolVersion: PROTOCOL_VERSION,
      capabilities: { tools: { listChanged: false } },
      serverInfo: SERVER_INFO
    });
  }
  if (method === 'notifications/initialized' || method === 'notifications/cancelled') return;
  if (method === 'ping') return reply(id, {});
  if (method === 'tools/list') return reply(id, { tools: TOOLS });
  if (method === 'resources/list') return reply(id, { resources: [] });
  if (method === 'resources/templates/list') return reply(id, { resourceTemplates: [] });
  if (method === 'tools/call') {
    try {
      const result = await callTool(client, params && params.name, (params && params.arguments) || {});
      return reply(id, result);
    } catch (error) {
      return reply(id, errorResult(error.message));
    }
  }
  if (isNotification) return;
  return replyError(id, -32601, `Method not found: ${method}`);
}

function main() {
  const client = createClient({ base: process.env.ICONSTASH_API_BASE || undefined });
  let buffer = '';
  let pending = 0;
  let stdinEnded = false;
  // Do not exit on stdin end while a tool call is still fetching: a client that
  // writes a request and immediately closes stdin would otherwise lose the reply.
  const maybeExit = () => {
    if (stdinEnded && pending === 0) process.exit(0);
  };
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', (chunk) => {
    buffer += chunk;
    let newline;
    while ((newline = buffer.indexOf('\n')) !== -1) {
      const line = buffer.slice(0, newline).trim();
      buffer = buffer.slice(newline + 1);
      if (!line) continue;
      let message;
      try { message = JSON.parse(line); } catch (_) { continue; }
      pending += 1;
      Promise.resolve(handle(message, client))
        .catch((error) => {
          if (message && message.id !== undefined && message.id !== null) {
            replyError(message.id, -32603, String(error && error.message ? error.message : error));
          }
        })
        .finally(() => {
          pending -= 1;
          maybeExit();
        });
    }
  });
  process.stdin.on('end', () => {
    stdinEnded = true;
    maybeExit();
  });
}

main();
