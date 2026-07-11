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
let currentQueryId = null;

// Helper functions for matching
function tokenize(value) {
  return String(value || "")
    .toLowerCase()
    .split(/[^a-z0-9]+/)
    .filter(Boolean);
}

function textFallback(list, query) {
  const words = tokenize(query);
  if (!words.length) return list;
  return list
    .map((icon) => {
      const haystack = [
        icon.name,
        icon.library,
        icon.librarySlug,
        icon.category,
        icon.subCategory,
        ...(icon.tags || []),
        ...(icon.nameVariants || [])
      ].join(" ").toLowerCase();
      let score = 0;
      for (const word of words) {
        if (haystack.includes(word)) score += icon.name.toLowerCase().includes(word) ? 4 : 1;
      }
      return score ? { icon, score } : null;
    })
    .filter(Boolean)
    .sort((a, b) => b.score - a.score || (b.icon.popularity || 0) - (a.icon.popularity || 0))
    .map((entry) => entry.icon);
}

self.onmessage = function (e) {
  const { type, data } = e.data;
  
  if (type === 'init') {
    iconsList = data || [];
    if (typeof Fuse !== 'undefined') {
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
      } else {
        if (fuse) {
          // If we have filters, search the subset using Fuse results filtered, or fall back
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
          results = textFallback(results, q);
        }
      }
    }

    // Apply sorting
    const sort = (filters && filters.sort) || "relevance";
    if (sort === "popular") {
      results.sort((a, b) => (b.popularity || 0) - (a.popularity || 0));
    } else if (sort === "newest") {
      results.sort((a, b) => String(b.dateAdded || "").localeCompare(String(a.dateAdded || "")));
    } else if (sort === "az") {
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
