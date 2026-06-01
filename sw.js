const CHUNK_CACHE = "iconstash-prerender-chunks-v20260601-mobilefast";
const CACHEABLE_CHUNK = /^\/data\/(?:prerender\/libraries\/[^/]+\/chunk-\d+\.html|meta\/[^/]+-meta\.json|[^/]+(?:-\d+)?\.json)$/;

self.addEventListener("install", (event) => {
  event.waitUntil(self.skipWaiting());
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(
      names
        .filter((name) => name.startsWith("iconstash-prerender-chunks-") && name !== CHUNK_CACHE)
        .map((name) => caches.delete(name))
    );
    await self.clients.claim();
  })());
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin || !CACHEABLE_CHUNK.test(url.pathname)) return;

  event.respondWith((async () => {
    const cache = await caches.open(CHUNK_CACHE);
    const cached = await cache.match(request);
    const network = fetch(request)
      .then((response) => {
        if (response && response.ok) {
          cache.put(request, response.clone());
        }
        return response;
      })
      .catch(() => cached);

    return cached || network;
  })());
});
