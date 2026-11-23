// public/sw.js — Minimal Service Worker for IconStash v2
//
// Caching strategy (per docs/memory-budget.md):
//   - App shell & hashed Astro assets (/_astro/*, favicons, fonts): Cache-first
//   - Binary search index (/index/v1/search.bin, /index/v1/search-meta.json):
//       Stale-while-revalidate (content-hashed metadata + fast offline search)
//   - HTML navigations: Network-first with cached shell fallback
//   - /chunks/v1/* & /data/*: EXPLICITLY EXCLUDED — owned exclusively by
//       IndexedDB (iconstash-v2) so browser storage is never doubled.

const VERSION = "v2-20261123";
const SHELL_CACHE = `iconstash-v2-shell-${VERSION}`;
const INDEX_CACHE = `iconstash-v2-index-${VERSION}`;

const PRECACHE_URLS = [
  "/",
  "/favicon.svg",
  "/apple-touch-icon.png",
  "/og-default.png"
];

const EXCLUDED_PATHS = /^\/(?:chunks\/v1\/|data\/|api\/v1\/index\.json$)/;
const INDEX_PATHS = /^\/index\/v1\/(?:search\.bin|search-meta\.json)$/;
const IMMUTABLE_ASSETS = /^\/(?:_astro\/|favicon\.svg$|favicon\.jpeg$|apple-touch-icon\.png$|logo\.png$|og-default\.png$)/;

self.addEventListener("install", (event) => {
  event.waitUntil(
    (async () => {
      const cache = await caches.open(SHELL_CACHE);
      await Promise.all(
        PRECACHE_URLS.map((url) =>
          cache.add(new Request(url, { cache: "reload" })).catch(() => {})
        )
      );
      await self.skipWaiting();
    })()
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      const keep = new Set([SHELL_CACHE, INDEX_CACHE]);
      const names = await caches.keys();
      await Promise.all(
        names
          .filter(
            (name) =>
              (name.startsWith("iconstash-v2-") ||
                name.startsWith("iconstash-shell-") ||
                name.startsWith("iconstash-prerender-chunks-")) &&
              !keep.has(name)
          )
          .map((name) => caches.delete(name))
      );
      await self.clients.claim();
    })()
  );
});

self.addEventListener("fetch", (event) => {
  const { request } = event;
  if (request.method !== "GET") return;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  // Hard exclusion: /chunks/v1/* and /data/* are owned by IndexedDB only.
  if (EXCLUDED_PATHS.test(url.pathname)) return;

  // Binary search index & metadata: stale-while-revalidate.
  if (INDEX_PATHS.test(url.pathname)) {
    event.respondWith(
      (async () => {
        const cache = await caches.open(INDEX_CACHE);
        const cached = await cache.match(request);
        const networkPromise = fetch(request)
          .then((response) => {
            if (response && response.ok) {
              cache.put(request, response.clone());
            }
            return response;
          })
          .catch(() => cached);

        return cached || networkPromise;
      })()
    );
    return;
  }

  // Hashed Astro build assets & static brand icons: cache-first.
  if (IMMUTABLE_ASSETS.test(url.pathname)) {
    event.respondWith(
      (async () => {
        const cache = await caches.open(SHELL_CACHE);
        const cached = await cache.match(request);
        if (cached) return cached;

        const response = await fetch(request);
        if (response && response.ok) {
          cache.put(request, response.clone());
        }
        return response;
      })()
    );
    return;
  }

  // Document navigations: network-first with offline fallback to cached page or "/".
  if (request.mode === "navigate") {
    event.respondWith(
      (async () => {
        const cache = await caches.open(SHELL_CACHE);
        try {
          const response = await fetch(request);
          if (response && response.ok && url.pathname === "/") {
            cache.put("/", response.clone());
          }
          return response;
        } catch {
          return (
            (await cache.match(request)) ||
            (await cache.match("/")) ||
            Response.error()
          );
        }
      })()
    );
  }
});
