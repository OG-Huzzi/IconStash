// search.js - Wraps the search.worker.js Web Worker to delegate fuzzy searching off the main thread.
// Exposes a Promise-based searchIcons API and maintains backwards-compatible helpers.
// Implements try-catch fallback to run synchronously on the main thread if worker creation is blocked.
// Optimizations: Instantiates Web Worker using a relative path to avoid import.meta parse errors in classic scripts.

(function () {
  let worker = null;
  let workerFailed = false;
  const searchPromises = new Map();
  let latestQueryId = 0;
  let allIcons = [];

  function tokenize(value) {
    return String(value || "")
      .toLowerCase()
      .split(/[^a-z0-9]+/)
      .filter(Boolean);
  }

  function baseName(name) {
    return String(name || "")
      .toLowerCase()
      .replace(/[-_\s]?(outline|regular|solid|filled|fill|bold|duotone|thin|light|sharp|round|linear|twotone|two-tone|24|20|16|12)$/g, "")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "");
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

  function buildSearchIndex(icons) {
    initSearch(icons);
  }

  function suggestions(icons, query, limit = 5) {
    const list = Array.from(icons || []);
    const q = String(query || "").trim();
    if (!q) return list.slice(0, limit);
    return textFallback(list, q).slice(0, limit);
  }

  function filterAndSort(icons, filters) {
    let result = Array.from(icons || []);
    if (filters.librarySlugs && filters.librarySlugs.size) {
      result = result.filter((icon) => filters.librarySlugs.has(icon.librarySlug));
    }
    if (filters.style && filters.style !== "all") {
      result = result.filter((icon) => icon.style === filters.style);
    }
    if (filters.category) {
      result = result.filter((icon) => icon.category === filters.category);
    }
    if (filters.query) {
      result = textFallback(result, filters.query);
    }
    const sort = filters.sort || "relevance";
    if (sort === "popular") {
      result.sort((a, b) => (b.popularity || 0) - (a.popularity || 0));
    } else if (sort === "newest") {
      result.sort((a, b) => String(b.dateAdded || "").localeCompare(String(a.dateAdded || "")));
    } else if (sort === "az") {
      result.sort((a, b) => a.name.localeCompare(b.name));
    } else if (sort === "za") {
      result.sort((a, b) => b.name.localeCompare(a.name));
    }
    return result;
  }

  function initSearch(icons) {
    if (icons) {
      allIcons = Array.from(icons);
    }

    if (workerFailed) return;

    if (!worker && typeof Worker !== 'undefined') {
      try {
        worker = new Worker('search.worker.js?v=20260606-mobilelag');
        worker.onmessage = function (e) {
          const { type, data, queryId } = e.data;
          if (type === 'results') {
            const promiseObj = searchPromises.get(queryId);
            if (promiseObj) {
              promiseObj.resolve(data);
              searchPromises.delete(queryId);
            }
          }
        };
        worker.onerror = function (err) {
          console.warn("Search worker error, falling back to main thread:", err);
          workerFailed = true;
        };
      } catch (err) {
        console.warn("Failed to initialize Search worker, falling back to main-thread search:", err);
        workerFailed = true;
      }
    } else if (typeof Worker === 'undefined') {
      workerFailed = true;
    }

    if (worker && !workerFailed && allIcons.length > 0) {
      try {
        worker.postMessage({ type: 'init', data: allIcons });
      } catch (err) {
        console.warn("Failed to send icons to Search worker, falling back to main-thread search:", err);
        workerFailed = true;
      }
    }
  }

  function searchIcons(query, options = {}) {
    if (workerFailed || (!worker && typeof Worker === 'undefined')) {
      return Promise.resolve(filterAndSort(allIcons, {
        ...options.filters,
        query: query
      }));
    }

    if (!worker) {
      initSearch();
    }

    latestQueryId++;
    const queryId = latestQueryId;

    // Send a cancel signal for previous queryIds
    for (const [id, promiseObj] of searchPromises.entries()) {
      if (id < queryId) {
        if (worker && !workerFailed) {
          try {
            worker.postMessage({ type: 'cancel', data: { queryId: id } });
          } catch (e) {}
        }
        promiseObj.resolve([]); // Resolve stale search promises with empty array
        searchPromises.delete(id);
      }
    }

    return new Promise((resolve, reject) => {
      searchPromises.set(queryId, { resolve, reject });
      
      const filters = options.filters ? { ...options.filters } : {};
      if (filters.librarySlugs instanceof Set) {
        filters.librarySlugs = Array.from(filters.librarySlugs);
      }

      if (worker && !workerFailed) {
        try {
          worker.postMessage({
            type: 'search',
            data: {
              query,
              limit: options.limit || 0,
              filters: filters,
              queryId
            }
          });
        } catch (err) {
          console.warn("Worker search failed, falling back to main thread:", err);
          workerFailed = true;
          resolve(filterAndSort(allIcons, {
            ...options.filters,
            query: query
          }));
        }
      } else {
        resolve(filterAndSort(allIcons, {
          ...options.filters,
          query: query
        }));
      }
    });
  }

  window.IconStashSearch = {
    baseName,
    tokenize,
    buildSearchIndex,
    filterAndSort,
    suggestions,
    initSearch,
    searchIcons
  };
})();
