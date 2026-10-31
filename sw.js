// sw.js — offline support for the IconStash app shell plus progressive caching
// of the pre-rendered icon chunks.
//
// Strategy:
//   • App shell (HTML, CSS, JS) — precached on install, then cache-first. These
//     URLs carry a ?v= version token, so a new deploy produces new URLs and the
//     cache cannot go stale.
//   • Navigations — network-first, with the cached shell as the offline
//     fallback, so a deploy is visible immediately and the app still boots
//     offline.
//   • Pre-rendered library chunks — cache-first with a background refresh.
//
// Library JSON is deliberately NOT cached here: app.js already stores it in
// IndexedDB, and caching it twice duplicated up to ~280 MB per origin.

const VERSION = "20261030-fixes";
const SHELL_CACHE = `iconstash-shell-${VERSION}`;
const CHUNK_CACHE = `iconstash-prerender-chunks-${VERSION}`;

const SHELL_ASSETS = [
  "index.html",
  `style.css?v=${VERSION}`,
  `icons.js?v=${VERSION}`,
  `ui.js?v=${VERSION}`,
  `search.js?v=${VERSION}`,
  `search.worker.js?v=${VERSION}`,
  `collections.js?v=${VERSION}`,
  `app.js?v=${VERSION}`,
  "vendor/fuse.min.js?v=20260530-preloadall",
  "favicon.svg"
];

// Only the pre-rendered chunk HTML is cached by the fetch handler.
const CHUNK_PATH = /^\/data\/prerender\/libraries\/[^/]+\/chunk-\d+\.html$/;

// Shell asset paths (query string ignored when matching).
const SHELL_PATH = /^\/(?:index\.html|style\.css|icons\.js|ui\.js|search\.js|search\.worker\.js|collections\.js|app\.js|favicon\.svg|vendor\/fuse\.min\.js)$/;

self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(SHELL_CACHE);
    // Best-effort: a single missing asset must not abort the whole install.
    await Promise.all(SHELL_ASSETS.map((url) => (
      cache.add(new Request(url, { cache: "reload" })).catch(() => {})
    )));
    await self.skipWaiting();
  })());
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(
      names
        .filter((name) => (
          (name.startsWith("iconstash-prerender-chunks-") || name.startsWith("iconstash-shell-")) &&
          name !== CHUNK_CACHE &&
          name !== SHELL_CACHE
        ))
        .map((name) => caches.delete(name))
    );
    await self.clients.claim();
  })());
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  // Pre-rendered library chunks: serve from cache, refresh in the background.
  if (CHUNK_PATH.test(url.pathname)) {
    event.respondWith((async () => {
      const cache = await caches.open(CHUNK_CACHE);
      const cached = await cache.match(request);
      const network = fetch(request)
        .then((response) => {
          if (response && response.ok) cache.put(request, response.clone());
          return response;
        })
        .catch(() => cached);

      return cached || network;
    })());
    return;
  }

  // Navigations: always try the network first so a deploy is picked up on the
  // next load; fall back to the cached shell when offline.
  if (request.mode === "navigate") {
    event.respondWith((async () => {
      try {
        const response = await fetch(request);
        if (response && response.ok && (url.pathname === "/" || url.pathname === "/index.html")) {
          const cache = await caches.open(SHELL_CACHE);
          cache.put("index.html", response.clone());
        }
        return response;
      } catch (error) {
        const cache = await caches.open(SHELL_CACHE);
        return (await cache.match(request))
          || (await cache.match("index.html"))
          || Response.error();
      }
    })());
    return;
  }

  // Versioned app-shell assets: cache-first, since the ?v= token versions them.
  if (SHELL_PATH.test(url.pathname)) {
    event.respondWith((async () => {
      const cache = await caches.open(SHELL_CACHE);
      const cached = await cache.match(request);
      if (cached) return cached;

      const response = await fetch(request);
      if (response && response.ok) cache.put(request, response.clone());
      return response;
    })());
  }
});
