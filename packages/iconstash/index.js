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

  async function snippet(id, format = 'svg') {
    const icon = await getIcon(id);
    const markup = await svg(id);
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

module.exports = { createClient, svgMarkup, normalize, tokenize };
