# AGENTS.md — IconStash v2 Repository Memory & Execution Rules

> Read this file first before modifying any code or spawning subagents in `/working_dir/c_89ae266b383b2b88/iconstash`.

---

## 1. Persistent Project Context

- **Product:** [IconStash](https://iconstash.io) — free, open-source SVG icon search engine, browser, customizer, and static API covering **134,701 SVG icons across 28 libraries** (16 categories, 7 styles).
- **Architecture:** 100% static site deployed to a VPS (Apache `.htaccess` + CDN). Zero runtime backend.
- **v2 Target Stack:** Astro 5 (static MPA + View Transitions) + Svelte 5 (Runes islands) + Tailwind CSS v4 + `@tanstack/svelte-virtual` + Dedicated Web Workers (`search.worker.ts`, `export.worker.ts`) + IndexedDB (`iconstash-v2`) + minimal Service Worker.
- **Public API Compatibility (Do Not Break):**
  - `@iconstash/sdk` (`packages/iconstash/index.js`) and `iconstash-mcp` (`packages/iconstash/mcp.js`) depend on `/api/v1/{manifest,libraries,index,openapi}.json` and `/data/{slug}.json`. Keep these endpoints intact and tested.
- **Canonical Reference Docs:**
  - `docs/architecture.md` — Phase 0 audit, exact `/chunks/v1/{library}.json` schema, binary `/index/v1/search.bin` layout, Web Worker protocols, Astro vs. Svelte island boundaries, and streaming 134k+ `--tarball` generator design.
  - `docs/memory-budget.md` — Forensic root causes of the legacy ~1 GB RAM spike, hard runtime budgets (`<= 45 MB` initial, `<= 100 MB` steady, `<= 140 MB` peak, `<= 180` DOM tiles, `< 15 ms` search, `60 fps`), bounded 4–6 chunk LRU policy, CSS-variable zero-re-render spec, and leak-prevention checklist.

---

## 2. Git Isolation Rules (NON-NEGOTIABLE)

1. **Active Branch Only:** Keep isolated v2 work on `rebuild/astro-svelte-v2` unless working on another branch at the user's request.
2. **No Unprompted Pushes to `main` or `origin`:**
   - Do **NOT** `git checkout main`, `git merge`, `git rebase` onto `main`, or `git push origin ...` unprompted.
   - **Explicit User Push Exception:** When the user explicitly instructs you to commit and/or push changes to GitHub (including to `main` or `origin`), run the requested `git add`, `git commit`, and `git push` commands directly.
   - `.github/workflows/deploy.yml` triggers an immediate production VPS webhook (`https://iconstash.io/deploy.php`) on any push to `main`.
3. **Never Commit Generated Build Outputs:**
   - Keep `dist/`, `release/`, `public/chunks/v1/`, `public/index/v1/`, `node_modules/`, and generated 134k+ `icons/` HTML pages out of Git (`.gitignore`).
   - Source-of-truth icon data remains in `data/*.json` (28 master files + `data/index.json`).
4. **Strict File Ownership:** Every subagent must edit ONLY the paths assigned to its phase/task in Section 4 below.

---

## 3. Target Repository Directory Layout (v2)

```text
iconstash/
├── AGENTS.md                        # This file (repo memory & rules)
├── docs/
│   ├── architecture.md              # Target architecture & binary/chunk schemas
│   └── memory-budget.md             # RAM budgets, LRU policy, leak checklist
├── data/                            # Source-of-truth 28 master library JSONs + index.json (read-only)
├── packages/
│   └── iconstash/                   # @iconstash/sdk + iconstash-mcp (preserve contract)
├── scripts/
│   ├── build-chunks.mjs             # Builds public/chunks/v1/{library}*.json + manifest.json
│   ├── build-search-index.mjs       # Compiles public/index/v1/search.bin + search-meta.json
│   ├── generate-icon-pages.mjs      # Streaming 134k+ icon/concept HTML + --tarball + sitemaps
│   ├── generate-api.js              # Existing public /api/v1/* + standalone SDK/MCP bundles
│   └── legacy/                      # Archived v1 scripts (do not run in v2 builds)
├── src/
│   ├── layouts/                     # BaseLayout.astro, EditorialLayout.astro
│   ├── pages/                       # Astro MPA routes (index, library/, category/, style/, compare/, articles/, etc.)
│   ├── content/                     # Astro Content Collections (articles, glossary, listicles)
│   ├── components/                  # Zero-JS Astro components (Header, Footer, SeoHead, SvgPreview)
│   ├── islands/                     # Svelte 5 interactive islands
│   │   ├── ExplorerShell.svelte     # Search bar, sidebar filters, toolbar
│   │   ├── VirtualIconGrid.svelte   # @tanstack/svelte-virtual (<= 180 DOM tiles)
│   │   ├── InspectorDrawer.svelte   # Single-icon preview, effects, codegen, export
│   │   ├── CollectionsTray.svelte   # Saved collections + bulk compare/ZIP bar
│   │   └── SvgDrawModal.svelte      # Lazy-loaded vector draw studio
│   ├── workers/
│   │   ├── search.worker.ts         # Binary typed-array search & bitmask filter worker
│   │   └── export.worker.ts         # OffscreenCanvas PNG + fflate ZIP worker
│   ├── lib/
│   │   ├── state/                   # Svelte 5 rune stores (*.svelte.ts)
│   │   ├── cache/                   # chunk-lru.ts (4–6 chunk RAM LRU) + idb-store.ts
│   │   ├── svg/                     # normalize.ts, render-effects.ts, codegen.ts
│   │   └── protocol/                # Typed worker message & binary header definitions
│   └── styles/
│       └── app.css                  # Tailwind v4 @import + @theme tokens + --ic-* grid rules
├── public/
│   ├── sw.js                        # Minimal app-shell + search.bin SW (excludes /chunks/v1/*)
│   ├── .htaccess                    # Canonical redirects, caching headers, retired-URL router
│   └── robots.txt, favicon.svg, ...
├── tests/
│   ├── unit/                        # Vitest unit tests (LRU, binary codec, SVG normalizer)
│   ├── workers/                     # Search accuracy, <15ms latency, export worker tests
│   └── perf/                        # Playwright CDP memory/DOM/60fps/leak test suite
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

---

## 4. Subagent File-Ownership Matrix (Phases 1–4)

| Phase | Subagent Role | Exclusive Write Paths | Read-Only Inputs | Forbidden Paths |
|---|---|---|---|---|
| **Phase 0** *(Complete)* | Architecture & Memory Auditor | `docs/architecture.md`, `docs/memory-budget.md`, `AGENTS.md` | Entire repo | All other files, `.git/` |
| **Phase 1** | Data Pipeline & Binary Index Engineer | `package.json`, `tsconfig.json`, `scripts/build-chunks.mjs`, `scripts/build-search-index.mjs`, `src/lib/protocol/**`, `tests/unit/**` | `data/*.json`, `docs/*.md`, `scripts/generate-api.js` | `data/*.json` (never mutate source), `packages/iconstash/`, `src/islands/` |
| **Phase 2A** | Astro Shell & Styling Engineer | `astro.config.mjs`, `src/layouts/**`, `src/components/**`, `src/styles/**`, `src/pages/index.astro`, `src/pages/library/**`, `src/pages/category/**`, `src/pages/style/**`, `public/sw.js` | `docs/*.md`, `src/lib/protocol/**` | `scripts/`, `src/workers/`, `src/islands/InspectorDrawer.svelte` |
| **Phase 2B** | Search, Cache & Virtual Grid Engineer | `src/workers/search.worker.ts`, `src/lib/cache/**`, `src/lib/state/explorer.svelte.ts`, `src/lib/state/preview.svelte.ts`, `src/islands/ExplorerShell.svelte`, `src/islands/VirtualIconGrid.svelte`, `tests/workers/search.test.ts` | `docs/*.md`, `src/lib/protocol/**`, `public/index/v1/*`, `public/chunks/v1/*` | `src/pages/`, `src/styles/`, `scripts/` |
| **Phase 3A** | Inspector, Export & Collections Engineer | `src/workers/export.worker.ts`, `src/lib/svg/**`, `src/lib/state/inspector.svelte.ts`, `src/lib/state/collections.svelte.ts`, `src/islands/InspectorDrawer.svelte`, `src/islands/CollectionsTray.svelte`, `src/islands/SvgDrawModal.svelte`, `tests/workers/export.test.ts` | `docs/*.md`, `icons.js` (reference), `app.js` (reference), `src/lib/protocol/**` | `src/workers/search.worker.ts`, `src/islands/VirtualIconGrid.svelte`, `scripts/` |
| **Phase 3B** | Editorial & Comparison MPA Migration Engineer | `src/content/**`, `src/pages/articles/**`, `src/pages/Glossary/**`, `src/pages/Listicles/**`, `src/pages/compare/**`, `src/pages/alternatives/**`, `src/pages/icons-for/**`, `src/pages/about.astro`, `src/pages/privacy.astro`, `src/pages/terms.astro`, `src/pages/contact.astro`, `src/pages/api.astro` | Existing static HTML directories, `scripts/generate-compare.js`, `scripts/generate-hubs.js` | `src/islands/`, `src/workers/`, `scripts/build-*.mjs` |
| **Phase 4** | Streaming 134k Generator & Perf Gate Engineer | `scripts/generate-icon-pages.mjs`, `tests/perf/**`, `public/.htaccess`, `.gitignore` | `dist/`, `public/chunks/v1/*`, `public/index/v1/*`, `docs/memory-budget.md`, `packages/iconstash/*` | `main` branch, `.github/workflows/deploy.yml`, `data/*.json` |

---

## 5. Exact Build, Test & Verification Commands

*(Commands below are wired into `package.json` in Phase 1 and enforced through Phase 4.)*

### Data & Index Pipeline
```bash
# 1. Build compact sharded per-library chunks + manifest
npm run build:chunks          # node scripts/build-chunks.mjs

# 2. Compile binary typed-array search index (/index/v1/search.bin)
npm run build:index           # node scripts/build-search-index.mjs

# 3. Rebuild public static API & standalone SDK/MCP bundles
npm run build:api             # node scripts/generate-api.js

# 4. Run full data pipeline
npm run build:data            # build:chunks && build:index && build:api
```

### Astro Site Build & Streaming 134k+ Icon Generator
```bash
# Local dev server
npm run dev                   # astro dev

# Production Astro MPA + Svelte 5 islands build
npm run build                 # astro check && astro build

# Smoke-test streaming icon page generator (500 pages)
npm run build:icons:smoke     # node scripts/generate-icon-pages.mjs --limit 500 --out dist/icons

# Full 134,701+ icon & concept pages streamed directly to compressed tarball (CI/release)
npm run build:icons:tarball   # node scripts/generate-icon-pages.mjs --tarball release/iconstash-icons.tar.zst

# Local preview server
npm run preview               # astro preview
```

### Verification & Hard Memory Budget Gates
```bash
# TypeScript + Astro + Svelte 5 static check
npm run check                 # astro check && tsc --noEmit

# Unit tests (LRU eviction, binary search codec, SVG normalization)
npm run test:unit             # vitest run tests/unit

# Web Worker tests (search accuracy, <15ms P95 latency, OffscreenCanvas/fflate export)
npm run test:workers          # vitest run tests/workers

# Public SDK & MCP server regression check
npm run test:sdk              # node --test tests/unit/sdk-compat.test.mjs

# Playwright CDP memory, DOM tile cap (<=180), 60fps & leak-detection suite
npm run test:perf             # playwright test tests/perf
```
