# IconStash v2 Memory Budget & Performance Specification

> **Purpose:** Document the forensic root causes of the legacy ~1 GB browser RAM spike and define hard, CI-enforced runtime memory, DOM, search-latency, and frame-rate budgets for the v2 rebuild.

---

## 1. Forensic Root-Cause Analysis: Why Legacy IconStash Spikes to ~1 GB RAM

Inspection of `app.js` (5,007 lines), `icons.js` (601 lines), `search.js` (203 lines), `search.worker.js` (146 lines), and `sw.js` (124 lines) identifies **seven compounding memory defects**:

### 1.1 Unbounded Background Preload of All 28 Libraries (`app.js:1387-1389`, `1470-1507`)
- `triggerBackgroundSync()` -> `loadAllLibrariesInBackground()` fetches all 28 `data/{slug}.json` files (**140.06 MB raw JSON**, 134,701 icon objects with 18+ keys each) into `state.icons` (`new Map()`).
- In V8, 134,701 parsed JS objects with nested `tags[]`, `nameVariants[]`, `variantIds[]`, and `svgPath` strings (64.38 MB raw UTF-8) expand to **~320–400 MB** of live heap on the main thread.
- No library is ever evicted from `state.icons` for the lifetime of the tab.

### 1.2 Repeated Full-Dataset Structured Cloning & Fuse.js Duplication (`app.js:1756`, `search.js:89,121`, `search.worker.js:55-73,79,138`)
- Every time *any* of the 28 libraries finishes loading, `loadLibrary()` calls `scheduleSearchIndex()` (`app.js:1394`), which runs:
  ```js
  window.IconStashSearch.buildSearchIndex(Array.from(state.icons.values()));
  ```
- `search.js:89` stores `allIcons = Array.from(icons)` and immediately calls `worker.postMessage({ type: 'init', data: allIcons })` (`search.js:121`).
- **This structured-clones up to 134,701 full icon objects — including all 64.38 MB of `svgPath` strings — across the Web Worker boundary**, up to 28 times during startup!
- Inside `search.worker.js:57`, `new Fuse(iconsList, ...)` builds a 7-key fuzzy index (`name`, `nameVariants`, `tags`, `category`, `subCategory`, `library`, `librarySlug`) over all 134,701 objects, consuming an additional **~180–260 MB** in the worker heap.
- On **every single search or filter change**, `search.worker.js:79,138` clones `iconsList` and posts the full array of matching icon objects back via `self.postMessage({ type: 'results', data: results, queryId })` into `state.filteredIcons` (`app.js:1825`) — creating a transient **~200–300 MB** structured-clone spike per query!

### 1.3 Unbounded SVG DOM Node Cache (`app.js:1926-1939`)
- `const svgCache = new Map()` caches a parsed `<svg>` DOM subtree for every icon ever rendered in the virtual grid:
  ```js
  svgCache.set(icon.id, cached);
  return cached ? cached.cloneNode(true) : null;
  ```
- `svgCache` has **no size cap and no eviction**. Scrolling through 15,000–30,000 icons retains tens of thousands of detached `<svg>` DOM subtrees in Blink/C++ memory (~40–100 MB).

### 1.4 Unbounded Prerender HTML String Cache & Non-Virtualized DOM Accumulation (`app.js:194, 808-838, 1011, 1128`)
- `state.prerender.chunkCache` (`new Map()`) stores raw HTML strings for fetched 160-icon prerender chunks (up to 856 chunks / **175 MB** total) with zero eviction.
- While in prerender browse mode, `appendNextPrerenderChunk()` (`app.js:1011`) and `checkViewportFill()` (`app.js:1128`) call `els.iconGrid.insertAdjacentHTML("beforeend", html)` continuously on scroll, accumulating **thousands of live `<article>` + `<svg>` DOM nodes** without ever unmounting off-screen tiles.

### 1.5 Runtime `svgPath` String Duplication (`icons.js:21-34`)
- `normalizeSvgBody(icon)` mutates every icon object in `state.icons` with `icon._normalizedBody = normalized`, storing a second full copy of every rendered icon's SVG markup in RAM.

### 1.6 Main-Thread Canvas & Base64 Explosion in Bulk Export (`icons.js:506-575`)
- `exportZIP()` rasterizes up to 200 icons × multiple PNG sizes on the main thread using DOM `<canvas>` elements + `canvas.toDataURL("image/png")` (base64 strings +33% overhead) + `JSZip` in-memory zipping, blocking the UI thread and spiking memory by 100–250 MB during bulk downloads.

### 1.7 Cumulative Legacy Peak RAM Summary

| Subsystem | Legacy Peak RAM | v2 Target RAM |
|---|---:|---:|
| Main-thread icon store (`state.icons` + `_normalizedBody`) | 350–450 MB | **<= 28 MB** (4–6 chunk LRU) |
| Search worker (`iconsList` clone + `Fuse.js` index) | 300–450 MB | **<= 10 MB** (binary typed-array index) |
| Transient `postMessage` search result clones | 150–300 MB | **<= 0.6 MB** (Transferable `Uint32Array`) |
| `svgCache` + Prerender `chunkCache` + live DOM nodes | 80–180 MB | **<= 8 MB** (`<= 180` DOM tiles, no node cache) |
| Framework / UI / Inspector / Export worker | 15–40 MB | **<= 20 MB** |
| **Total Browser Tab Memory (Peak)** | **~900 MB – 1.3 GB** | **<= 100 MB steady / <= 140 MB ceiling** |

---

## 2. Hard Runtime Budgets (CI-Enforced)

Every pull request in Phases 2–4 must satisfy all six hard budgets measured in headless Chromium (desktop 1440×900 & mobile 390×844 throttled 4x CPU) via Playwright CDP:

| Metric | Hard Budget | Measurement Method |
|---|---:|---|
| **Initial JS Heap (cold load)** | **`<= 45 MB`** | `Performance.getMetrics().JSHeapUsedSize` after initial paint + search index ready |
| **Steady-State JS Heap** | **`<= 100 MB`** | After 5 searches, switching 8 libraries, scrolling 50,000px, opening/closing inspector 10x |
| **Hard Peak Ceiling** | **`<= 140 MB`** | Absolute max `JSHeapUsedSize` during bulk 200-icon ZIP export or rapid random jumps |
| **Mounted DOM Icon Tiles** | **`<= 180` tiles** | `document.querySelectorAll('[data-icon-tile]').length` during any scroll position |
| **Search Latency (P95)** | **`< 15 ms`** | Worker `QUERY` -> `RESULTS` round-trip across all 134,701 icons (tested with 1-char, multi-word, and facet filters) |
| **Frame Rate (Scroll & Styling)** | **`60 fps`** | `>= 58 fps` sustained (`<= 16.6 ms` frame time) during continuous scroll and live color/stroke slider drag |

---

## 3. Bounded LRU Chunk Cache Policy

### 3.1 Cache Capacity & Adaptive Sizing

The main thread manages SVG chunk payloads through a dedicated `ChunkLRUCache` (`src/lib/cache/chunk-lru.ts`):

- **Max resident chunks in RAM:**
  - **Desktop (`navigator.deviceMemory >= 4` or unset):** `maxChunks = 6`, `maxBytes = 28 * 1024 * 1024` (28 MB).
  - **Mobile / constrained (`navigator.deviceMemory < 4` or viewport `< 768px`):** `maxChunks = 4`, `maxBytes = 16 * 1024 * 1024` (16 MB).
- **Eviction Policy:** Strict O(1) Least-Recently-Used using ES `Map` insertion order (`delete` + `set` on every `get()` hit). When `entries.size > maxChunks` or `totalBytes > maxBytes`, evict the oldest key(s) until both limits are satisfied.
- **Pinned Single-Icon Records:** Opening an icon in `InspectorDrawer` or adding it to `CompareModal` copies only that single icon's compact record (~600 B) into a separate bounded `pinnedIcons` map (`max = 50` entries). Evicting a 4,000-icon library chunk therefore **never** invalidates the active inspector or comparison view.

### 3.2 Two-Tier Hydration (RAM LRU + IndexedDB)

1. **Tier 1 — RAM `ChunkLRUCache` (`< 0.05 ms`):** Instant synchronous lookup for visible virtual rows.
2. **Tier 2 — IndexedDB `iconstash-v2` (`5–15 ms`):** Persists fetched raw chunk JSON payloads keyed by `${contentHash}:${shardUrl}`. On RAM eviction, the chunk remains in IndexedDB so scrolling back to a previously visited library re-hydrates locally with **zero network traffic**.
3. **Tier 3 — Network `/chunks/v1/{shard}.json` (`50–250 ms`):** Fetches with `AbortController`; in-flight requests are deduplicated by `shardUrl` and canceled if the user scrolls past the shard before it resolves.
4. **No Service Worker Duplication:** `sw.js` MUST NOT intercept or cache `/chunks/v1/*` requests. IndexedDB is the sole persistent cache for icon chunks, preventing the 2x storage bloat noted in legacy `sw.js:13-14`.
5. **IndexedDB Quota Hygiene:** On app startup, delete any `iconstash-v2` entries whose `contentHash` prefix does not match `manifest.contentHash`, and cap total stored IDB chunks at 40 shards (evicting oldest `lastAccessedAt` on write).

---

## 4. CSS-Variable Zero-Re-Render Grid Styling Spec

### 4.1 Architecture

Live customization controls (color picker, stroke-width slider, icon size slider, tile density) MUST **never** trigger Svelte component re-renders, SVG string re-serialization, or DOM node mutations across the icon grid.

1. **Build-Time SVG Normalization:**
   - Every `svgBody` in `/chunks/v1/*.json` has hardcoded `fill`/`stroke` colors normalized to `currentColor` at build time.
   - Outline/stroke icons strip redundant per-path `stroke-width="..."` attributes so all child shapes inherit `stroke-width` from the parent `<svg>`.
2. **Grid-Root CSS Custom Properties:**
   The virtual grid container (`<div class="ic-grid-root">`) owns four CSS variables updated via a single `requestAnimationFrame`-coalesced `.style.setProperty()` call:
   ```css
   .ic-grid-root {
     --ic-color: currentColor;
     --ic-stroke-width: 1.75;
     --ic-size: 24px;
     --ic-tile-size: 72px;
   }

   .ic-tile svg {
     width: var(--ic-size);
     height: var(--ic-size);
     color: var(--ic-color);
   }

   .ic-tile[data-filled="false"] svg {
     fill: none;
     stroke: currentColor;
     stroke-width: var(--ic-stroke-width);
     stroke-linecap: round;
     stroke-linejoin: round;
   }

   .ic-tile[data-filled="true"] svg {
     fill: currentColor;
     stroke: none;
   }
   ```
3. **Scoped Heavy Effects:**
   - Expensive SVG `<defs>` (gradients, `feTurbulence` wood/metal/marble/concrete/paper textures, drop shadows, blur, CSS keyframe motion) are **strictly forbidden inside the virtual grid**. They render only on the single active `<svg>` inside `InspectorDrawer.svelte` and during export.

### 4.2 Expected Cost
- Dragging the color wheel or stroke slider at 120 Hz executes **1 `style.setProperty` call per animation frame** (`< 0.3 ms` style recalc across `<= 180` tiles) — **0 Svelte reactivity cycles, 0 GC allocations, locked 60 fps**.

---

## 5. Memory Leak-Prevention Checklist

Every contributor and subagent MUST verify these five leak vectors before marking any Phase 2–4 task complete:

### 5.1 `URL.createObjectURL` / `URL.revokeObjectURL`
- [ ] Every `URL.createObjectURL(blob)` has a paired `URL.revokeObjectURL(url)` in a `finally` block or immediately after download trigger (`setTimeout(() => URL.revokeObjectURL(url), 1000)`).
- [ ] Never store `blob:` URLs in Svelte `$state`, `localStorage`, or module-level caches.

### 5.2 `OffscreenCanvas` & `ImageBitmap` Cleanup (`export.worker.ts`)
- [ ] Every `ImageBitmap` created via `createImageBitmap(blob)` MUST be explicitly closed (`bitmap.close()`) inside `try { ... } finally { bitmap.close(); }` immediately after `ctx.drawImage()`.
- [ ] After `canvas.convertToBlob()`, release GPU backing textures by setting `canvas.width = 0; canvas.height = 0;` before dropping the `OffscreenCanvas` reference.
- [ ] Bulk ZIP exports process icons **sequentially** (concurrency `= 1` for rasterization) so at most one `OffscreenCanvas` backing store exists in GPU/RAM at any instant.

### 5.3 Astro View Transitions & Listener Cleanup
- [ ] Every `window` / `document` listener (`keydown`, `resize`, `scroll`, `storage`) and every `ResizeObserver` / `IntersectionObserver` registered inside a Svelte 5 island MUST return a teardown callback from `$effect(() => { ...; return () => cleanup(); })`.
- [ ] Any non-Svelte page script listening to `astro:page-load` MUST tear down its observers/timers on `astro:before-swap`.
- [ ] Web Workers (`search.worker.ts`, `export.worker.ts`) are module singletons stored on `globalThis`; never instantiate a `new Worker(...)` inside a component mount without checking the singleton registry.

### 5.4 In-Flight Fetch & Timer Cancellation
- [ ] Chunk fetches use `AbortController` tied to the current viewport window and cancel immediately on route change or rapid scroll-away.
- [ ] All `setTimeout` / `requestAnimationFrame` handles are cleared in `$effect` cleanup functions.

### 5.5 Automated Leak-Detection Gate (Playwright CDP)
Before Phase 4 sign-off, `npm run test:perf` runs a 10-cycle stress script:
1. Navigate `/` -> `/library/fluent/` -> `/library/materialsymbols/` -> `/` (10 cycles via View Transitions).
2. Execute 20 searches, scroll 100,000px across multiple libraries, open/close inspector 10 times, export 1 PNG + 1 20-icon ZIP.
3. Force GC (`HeapProfiler.collectGarbage` via CDP) and assert:
   - `JSHeapUsedSize <= 100 MB` (steady state) and `<= 140 MB` (peak throughout run)
   - `DOMNodes` delta between Cycle 2 and Cycle 10 `< 5%` (proves zero detached DOM / View Transition leaks)
   - `JSEventListeners` delta between Cycle 2 and Cycle 10 `<= 10` (proves zero leaked listeners)
   - `[data-icon-tile]` count never exceeds `180` at any sampled scroll offset.
