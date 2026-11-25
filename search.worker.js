// search.worker.js - Web Worker that indexes icons and performs searches off the main thread using Fuse.js.
// Resolves browser freezing issues during multi-key fuzzy search on 134k+ icons.

try {
  importScripts('vendor/fuse.min.js');
} catch (e) {
  try {
    importScripts('../vendor/fuse.min.js');
  } catch (err) {
    console.error("Failed to load Fuse.js in worker", err);
  }
}

let fuse = null;
let iconsList = [];
let searchRows = [];
let currentQueryId = null;

const FUSE_BUILD_CAP = 20000;

function buildFastRows(icons) {
  const len = icons.length;
  const rows = new Array(len);
  for (let i = 0; i < len; i++) {
    const icon = icons[i];
    const nameLower = String(icon.name || "").toLowerCase();
    const hay = [
      nameLower,
      icon.librarySlug || "",
      icon.category || "",
      icon.subCategory || "",
      ...(icon.tags || []),
      ...(icon.nameVariants || [])
    ].join(" ").toLowerCase();
    rows[i] = { icon, nameLower, hay };
  }
  return rows;
}

// Helper functions for matching
function tokenize(value) {
  return String(value || "")
    .toLowerCase()
    .split(/[^a-z0-9]+/)
    .filter(Boolean);
}

function fastSearch(rows, query, filters) {
  const words = tokenize(query);
  if (!words.length) return [];
  const slugs = filters && filters.librarySlugs ? new Set(filters.librarySlugs) : null;
  const styleFilter = filters && filters.style && filters.style !== "all" ? filters.style : "";
  const categoryFilter = filters && filters.category ? filters.category : "";
  const matches = [];
  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];
    const icon = row.icon;
    if (slugs && slugs.size > 0 && !slugs.has(icon.librarySlug)) continue;
    if (styleFilter && icon.style !== styleFilter) continue;
    if (categoryFilter && icon.category !== categoryFilter) continue;
    let score = 0;
    let allWordsMatch = true;
    for (let w = 0; w < words.length; w++) {
      const word = words[w];
      if (row.nameLower === word) score += 10;
      else if (row.nameLower.startsWith(word)) score += 6;
      else if (row.nameLower.includes(word)) score += 4;
      else if (row.hay.includes(word)) score += 1;
      else {
        allWordsMatch = false;
        break;
      }
    }
    if (allWordsMatch && score > 0) {
      matches.push({ icon, score });
    }
  }
  matches.sort((a, b) => b.score - a.score || (b.icon.popularity || 0) - (a.icon.popularity || 0));
  return matches.map((entry) => entry.icon);
}

self.onmessage = function (e) {
  const { type, data } = e.data;
  
  if (type === 'init') {
    iconsList = data || [];
    searchRows = buildFastRows(iconsList);
    if (typeof Fuse !== 'undefined' && iconsList.length <= FUSE_BUILD_CAP) {
      fuse = new Fuse(iconsList, {
        includeScore: true,
        threshold: 0.32,
        distance: 96,
        ignoreLocation: true,
        minMatchCharLength: 1,
        keys: [
          { name: "name", weight: 0.62 },
          { name: "nameVariants", weight: 0.2 },
          { name: "tags", weight: 0.48 },
          { name: "category", weight: 0.12 },
          { name: "subCategory", weight: 0.1 },
          { name: "library", weight: 0.08 },
          { name: "librarySlug", weight: 0.06 }
        ]
      });
    } else {
      // For full 25k–134k icon sets, Fuse index construction freezes the worker for 5–10s;
      // use linear pre-lowercased token scan (~15–30ms across 134k icons).
      fuse = null;
    }
    self.postMessage({ type: 'indexed' });
  } else if (type === 'search') {
    const { query, limit, filters, queryId } = data;
    currentQueryId = queryId;

    let results = Array.from(iconsList);

    // Apply library, style, category filters first
    if (filters) {
      if (filters.librarySlugs) {
        const slugs = Array.isArray(filters.librarySlugs) ? new Set(filters.librarySlugs) : (filters.librarySlugs instanceof Set ? filters.librarySlugs : new Set());
        if (slugs.size > 0) {
          results = results.filter((icon) => slugs.has(icon.librarySlug));
        }
      }
      if (filters.style && filters.style !== "all") {
        results = results.filter((icon) => icon.style === filters.style);
      }
      if (filters.category) {
        results = results.filter((icon) => icon.category === filters.category);
      }
    }

    // Apply search query
    const q = String(query || "").trim();
    if (q) {
      if (fuse && (!filters || !filters.librarySlugs || filters.librarySlugs.length === 0) && (!filters || !filters.style || filters.style === "all") && (!filters || !filters.category)) {
        // Global search using Fuse index directly
        const searchResults = fuse.search(q);
        results = searchResults.map(r => r.item);
      } else if (fuse) {
        const searchResults = fuse.search(q);
        const slugs = filters && filters.librarySlugs ? new Set(filters.librarySlugs) : null;
        results = [];
        for (let i = 0; i < searchResults.length; i++) {
          const item = searchResults[i].item;
          if (slugs && slugs.size > 0 && !slugs.has(item.librarySlug)) continue;
          if (filters && filters.style && filters.style !== "all" && item.style !== filters.style) continue;
          if (filters && filters.category && item.category !== filters.category) continue;
          results.push(item);
        }
      } else {
        results = fastSearch(searchRows, q, filters);
      }
    }

    // Apply sorting
    const sort = (filters && filters.sort) || "relevance";
    if (sort === "az") {
      results.sort((a, b) => a.name.localeCompare(b.name));
    } else if (sort === "za") {
      results.sort((a, b) => b.name.localeCompare(a.name));
    }

    // Limit results if query is non-empty and limit is specified
    if (q && limit && results.length > limit) {
      results = results.slice(0, limit);
    }

    // Respond back to the main thread if this request wasn't superseded
    if (currentQueryId === queryId) {
      self.postMessage({ type: 'results', data: results, queryId });
    }
  } else if (type === 'cancel') {
    if (currentQueryId === data.queryId) {
      currentQueryId = null;
    }
  }
};
