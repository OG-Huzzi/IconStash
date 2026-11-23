# IconStash Phase 0 SEO, URL, Sitemap & API/MCP Parity Specification

> **Audit Baseline:** `/working_dir/c_89ae266b383b2b88/iconstash` (branch `rebuild/astro-svelte-v2`)  
> **Canonical Origin:** `https://iconstash.io` (lowercase, HTTPS, apex domain, trailing slash on all HTML routes)  
> **Catalog Baseline:** 28 open-source libraries · 134,701 indexed icons (`api/v1/index.json` / `data/index.json`, snapshot `2026-05-05T15:07:40.341Z`) · 137,871 pre-rendered `icons/*/index.html` pages (134,125 individual icon pages + 3,746 cross-library concept pages) · 14,915 retired `icons/*/index.php` 301 redirect stubs.

This specification is the single source of truth for:
1. Preserving 100% URL, redirect, sitemap, structured-data, and API/MCP parity in the Astro + Svelte v2 rebuild.
2. Driving the automated **Phase 4 SEO parity diff script** against the built `dist/` output.

---

## 1. Root Files, Configs, Verification Assets & Top-Level Directories

### 1.1 Root Static, Config & Verification Files

Every file below lives at the repository root and must be preserved byte-for-byte (or with equivalent server rules) in the new build's `public/` / hosting root:

| File | Size | Purpose / Exact Content Contract | Parity Requirement |
|---|---:|---|---|
| `.htaccess` | 5,577 B | Apache routing, canonical redirects, UTF-8, compression, security headers, CORS, and Cache-Control (see §1.2) | **MUST preserve** all redirect, CORS, security, and `DirectoryIndex` rules (or translate 1:1 to target host config) |
| `robots.txt` | 1,876 B | `User-agent: *` with `Allow: /`, `Allow: /data/index.json`, `Allow: /api/`, `Disallow: /data/`, `Disallow: /vendor/`, `Disallow: /*?query=`, `Disallow: /*?q=`, `Disallow: /search.worker.js`; explicit `Allow: /` for 22 AI/LLM crawlers (`GPTBot`, `ChatGPT-User`, `OAI-SearchBot`, `Google-Extended`, `ClaudeBot`, `Claude-Web`, `anthropic-ai`, `PerplexityBot`, `Perplexity-User`, `bingbot`, `Applebot`, `Applebot-Extended`, `CCBot`, `FacebookBot`, `meta-externalagent`, `Amazonbot`, `Bytespider`, `cohere-ai`, `MistralAI-User`, `DuckAssistBot`, `Diffbot`, `Omgilibot`, `Webzio-Extended`); `Sitemap: https://iconstash.io/sitemap.xml` | **MUST preserve verbatim** |
| `sitemap.xml` | 847 B | Sitemap index referencing 7 child sitemaps (see §1.3) | **MUST preserve** exact `<sitemapindex>` structure and child URLs |
| `articles-sitemap.xml` | 24,965 B | 187 URLs (`articles/`: 157, `Glossary/`: 17, `Listicles/`: 13) | **MUST preserve** exact URL set and trailing slashes |
| `llms.txt` | 33,661 B | 279-line AEO/GEO directory index for AI assistants (key facts, 28 library hubs, top concept pages, 16 categories, styles, comparisons, articles) | **MUST preserve** at `/llms.txt` |
| `llms-full.txt` | 7,528 B | 111-line full AI reference sheet (28-library table, license breakdown, features, citable facts, comparisons, FAQ) | **MUST preserve** at `/llms-full.txt` |
| `ads.txt` | 294 B | `OWNERDOMAIN=iconstash.io` (AdSense/GAM placeholder) | **MUST preserve verbatim** |
| `BingSiteAuth.xml` | 85 B | `<users><user>F420F1F875B1C5C48265BC69D3DEFF1A</user></users>` | **MUST preserve verbatim** |
| `naver3487674ab8e7c64ca2ca2862ae597316.html` | 68 B | `naver-site-verification: naver3487674ab8e7c64ca2ca2862ae597316.html` | **MUST preserve verbatim** |
| `yandex_c4d8a8062ca7c1e5.html` | 162 B | `Verification: c4d8a8062ca7c1e5` HTML document | **MUST preserve verbatim** |
| `e11c5bc79c6d4824bb883b2723c0fa6a.txt` | 33 B | IndexNow API key (`e11c5bc79c6d4824bb883b2723c0fa6a`) | **MUST preserve verbatim** |
| `deploy-check.txt` | 299 B | VPS live-root deployment marker (`customize-preview-vps-root-check-20260529`) | Preserve if deploying to same VPS |
| `404.html` | 5,435 B | `<title>Page Not Found (404) \| IconStash</title>`, `<meta name="robots" content="noindex, follow">`, links to `/library/`, `/category/`, `/style/`, `/compare/`, `/articles/`, `/stats/`, `/` | **MUST preserve** `noindex, follow` and hub links. **Legacy bug note:** current `404.html` contains an inline `<script>` that redirects unknown `/icons/<slug>/` paths to `/icons/<cleanId>-icon-svg/`, which can loop because canonical icon URLs are `/icons/{lib}-{slug}/`. Remove or fix that redirect script in v2. |
| `favicon.svg` | 245 B | 24×24 SVG geometric cube mark (`stroke="#00c3ff"`) | **MUST preserve** at `/favicon.svg` |
| `favicon.jpeg` | 3,328 B | 250×250 RGBA PNG (despite `.jpeg` extension) | **MUST preserve** at `/favicon.jpeg` (referenced by `apple-touch-icon` across articles/static pages) |
| `apple-touch-icon.png` | 3,328 B | 250×250 RGBA PNG | **MUST preserve** at `/apple-touch-icon.png` |
| `logo.png` | 3,328 B | 250×250 RGBA PNG (referenced in `og:image` on some older Glossary pages and `Organization.logo` JSON-LD) | **MUST preserve** at `/logo.png` |
| `og-default.png` | 79,327 B | 1200×630 RGB PNG default Open Graph / Twitter Card image | **MUST preserve** at `/og-default.png` |

**Legacy app runtime files at root** (replaced by Astro + Svelte v2 bundle, not SEO routes): `index.html` (280,382 B), `app.js`, `collections.js`, `icons.js`, `search.js`, `search.worker.js`, `style.css`, `sw.js`, `ui.js`, `vendor/fuse.min.js`, `vendor/jszip.min.js`.

### 1.2 `.htaccess` Ruleset Contract

All of the following HTTP behaviors are currently enforced by `.htaccess` and must remain intact:

1. **DirectoryIndex precedence:** `DirectoryIndex index.php index.html` — required so the 14,915 retired `icons/*/index.php` redirect stubs execute before falling through to `index.html`.
2. **Host & Protocol Canonicalization (301):**
   - `www.iconstash.io` → `https://iconstash.io/$1` (`301`)
   - Plain `http://` (and `X-Forwarded-Proto != https`) → `https://%{HTTP_HOST}/$1` (`301`)
3. **Case-Canonical Redirects (301):**
   - `/listicles/(.*)` (when `REQUEST_URI` does not start with `/Listicles/`) → `/Listicles/$1` (`301, NC`)
   - `/glossary/(.*)` (when `REQUEST_URI` does not start with `/Glossary/`) → `/Glossary/$1` (`301, NC`)
   - **Critical:** `/Listicles/` and `/Glossary/` are capitalized on disk and in sitemaps/canonicals. Never lowercase them without a full redirect migration.
4. **Directory Listing Suppression:** Any directory lacking both `index.html` and `index.php` (e.g. `/sitemaps/`, `/data/`, `/assets/`) returns `404` via `mod_rewrite`.
5. **MIME & UTF-8:** `AddDefaultCharset UTF-8`; `application/json .json`; `image/svg+xml .svg`; Brotli + Deflate compression.
6. **Security Headers:** `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Content-Security-Policy: frame-ancestors 'self'`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()`, `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`.
7. **Public Static API CORS (`\.json$`):**
   - `Access-Control-Allow-Origin: *`
   - `Access-Control-Allow-Methods: GET, HEAD, OPTIONS`
   - `Access-Control-Allow-Headers: Accept, Content-Type`
   - `Access-Control-Max-Age: 86400`
   - Applies to `/api/v1/*.json` AND `/data/{slug}.json`.
8. **Cache-Control:**
   - `.html`: `public, max-age=3600, must-revalidate`
   - `.js` (except `sw.js`), `.css`, `.json`: `public, max-age=3600, stale-while-revalidate=86400`
   - `sw.js`: `no-cache, no-store, must-revalidate`
   - `.svg|.jpg|.jpeg|.png|.webp|.ico|.woff2?`: `public, max-age=2592000` (30 days)

### 1.3 Complete XML Sitemap Inventory

`https://iconstash.io/sitemap.xml` is a `<sitemapindex>` with **7 child sitemaps** containing **138,266 total `<url>` entries** (100% trailing-slash URLs):

| Sitemap File | Size | URL Count | `<lastmod>` Sample | `<priority>` / `<changefreq>` | URL Prefix Breakdown |
|---|---:|---:|---|---|---|
| `sitemap.xml` | 847 B | 7 sitemaps | `2026-11-22` .. `2026-08-31` | N/A (index) | Points to the 7 XML files below |
| `articles-sitemap.xml` | 24,965 B | **187** | `2026-10-31` .. `2026-11-22` | `0.8` / `monthly` (24 entries; rest omit) | `articles/`: 157, `Glossary/`: 17, `Listicles/`: 13 |
| `sitemaps/hubs.xml` | 9,249 B | **63** | `2026-09-04` .. `2026-11-13` | `0.9` (3), `0.8` (52), `0.7` (3), `0.6` (1), `0.5` (2), `0.3` (2) · `weekly`/`monthly`/`yearly` | `library/`: 29, `category/`: 17, `style/`: 8, `api/`: 1, `about/`: 1, `contact/`: 1, `privacy/`: 1, `terms/`: 1, `stats/`: 1, `compare/`: 1, `alternatives/`: 1, `icons-for/`: 1 |
| `sitemaps/compare.xml` | 22,796 B | **144** | `2026-09-04` | `0.7` / `monthly` (all 144) | `compare/`: 120, `alternatives/`: 17, `icons-for/`: 7 |
| `sitemaps/concepts.xml` | 362,822 B | **3,746** | `2026-08-31` | omitted | `icons/{concept}-icon/`: 3,746 |
| `sitemaps/sitemap-1.xml` | 4,960,629 B | **44,996** | `2026-08-31` | omitted | `/` (homepage): 1, `icons/{lib}-{slug}/`: 44,995 |
| `sitemaps/sitemap-2.xml` | 4,954,278 B | **45,000** | `2026-08-31` | omitted | `icons/{lib}-{slug}/`: 45,000 |
| `sitemaps/sitemap-3.xml` | 4,883,414 B | **44,130** | `2026-08-31` | omitted | `icons/{lib}-{slug}/`: 44,130 |
| **Total Indexed URLs** | **14.8 MB** | **138,266** | — | — | **1** root + **134,125** icons + **3,746** concepts + **63** hubs/static + **144** compare/alt/stack + **187** editorial |

> **Note:** `/seo/` and `/seo/sitemap-1/`..`/seo/sitemap-150/` are intentionally **excluded** from XML sitemaps and carry `<meta name="robots" content="noindex, follow">`.

### 1.4 Non-Route Top-Level Directories

| Directory | Contents / Purpose |
|---|---|
| `assets/articles/` | Editorial article & `alternatives/font-awesome/` hero/OG images (`1200×675` `.jpg`) |
| `data/` | Public static icon JSON payloads (`index.json`, `{slug}.json` for all 28 libraries, chunked `{slug}-{n}.json`, `meta/`, `prerender/`) — **referenced directly by `/api/v1/` and SDK/MCP** |
| `packages/iconstash/` | Source for `@iconstash/sdk` (`index.js`, `mcp.js`, `package.json`, `README.md`) |
| `scripts/` | Build/generator scripts (`generate-pseo.js`, `generate-hubs.js`, `generate-compare.js`, `generate-api.js`, `prerender.js`, `submit_indexnow.js`, article generators & verifiers) |
| `vendor/` | Legacy `fuse.min.js`, `jszip.min.js` |
| `docs/` | Documentation directory (this file) |

---

## 2. Complete Route Inventory, Exact Counts & Trailing-Slash Patterns

**Global URL Rule:** Every HTML route resolves to a directory containing `index.html` and uses a **trailing slash** (`/path/`). Canonical `<link rel="canonical">` values are 100% absolute `https://iconstash.io/.../` with trailing slashes.

### 2.1 Master Route Count Table

| Directory / Route | Index Page | Subpages (`index.html`) | Total HTML Pages | Other Files / Stubs | URL Pattern |
|---|---:|---:|---:|---|---|
| `/` (root) | 1 | — | **1** | — | `/` |
| `icons/` | 0 | 137,871 | **137,871** | **14,915** `index.php` 301 redirect dirs (total 152,786 dirs) | `/icons/{lib}-{slug}/` (134,125) · `/icons/{concept}-icon/` (3,746) |
| `library/` | 1 | 28 | **29** | — | `/library/` · `/library/{slug}/` |
| `category/` | 1 | 16 | **17** | — | `/category/` · `/category/{slug}/` |
| `style/` | 1 | 7 | **8** | — | `/style/` · `/style/{slug}/` |
| `compare/` | 1 | 120 | **121** | — | `/compare/` · `/compare/{libA}-vs-{libB}/` |
| `alternatives/` | 1 | 17 | **18** | — | `/alternatives/` · `/alternatives/{slug}/` |
| `icons-for/` | 1 | 7 | **8** | — | `/icons-for/` · `/icons-for/{framework}/` |
| `articles/` | 1 | 156 | **157** | `README.md` | `/articles/` · `/articles/{slug}/` |
| `Glossary/` *(capital G)* | 1 | 16 | **17** | — | `/Glossary/` · `/Glossary/{slug}/` |
| `Listicles/` *(capital L)* | 1 | 12 | **13** | — | `/Listicles/` · `/Listicles/{slug}/` |
| `seo/` | 1 | 150 | **151** | `dim-check.ps1`, `run-audit-scan.ps1` | `/seo/` · `/seo/sitemap-{1..138}/` (active) · `/seo/sitemap-{139..150}/` (12 meta-refresh "Moved" stubs) |
| `stats/` | 1 | 0 | **1** | — | `/stats/` |
| `about/` | 1 | 0 | **1** | — | `/about/` |
| `contact/` | 1 | 0 | **1** | — | `/contact/` |
| `privacy/` | 1 | 0 | **1** | — | `/privacy/` |
| `terms/` | 1 | 0 | **1** | — | `/terms/` |
| `api/` | 1 | 0 | **1** | `iconstash-mcp.js`, `iconstash-sdk.js`, `v1/*.json` | `/api/` |
| **Grand Total** | **16** | **138,400** | **138,416** | **14,915** PHP 301s | **138,266** in XML sitemaps + **151** `noindex` `/seo/` pages − 1 overlap (`404.html` excluded) |

### 2.2 Deep Dive: `icons/` Directory (152,786 Subdirectories)

The `icons/` directory has **zero** root files and **152,786** subdirectories split cleanly into three categories:

1. **Individual Icon Pages — `134,125` directories (`index.html`)**
   - **Naming pattern:** `/icons/{librarySlug}-{iconSlug}/` (e.g. `/icons/lucide-home/`, `/icons/bootstrap-0-circle/`, `/icons/fluent-access-time-24-regular/`).
   - **Sitemaps:** Split across `sitemaps/sitemap-1.xml` (44,995), `sitemaps/sitemap-2.xml` (45,000), and `sitemaps/sitemap-3.xml` (44,130).
   - **Per-library page counts (prefix distribution):**
     `fluent` (20,170), `materialsymbols` (18,543), `materialsymbolslight` (15,965), `material` (14,000), `phosphor` (9,198), `solar` (7,413), `tabler` (6,323), `hugeicons` (5,115), `simpleicons` (3,710), `mingcute` (3,348), `remix` (3,243), `boxicons` (2,857), `iconparkoutline` (2,654), `carbon` (2,642), `ionicons` (2,607), `bootstrap` (2,091), `iconoir` (2,018), `lucide` (1,978), `iconparksolid` (1,967), `antdesign` (1,868), `heroicons` (1,293), `linemd` (1,279), `pixelarticons` (1,098), `octicons` (926), `cssgg` (704), `eva` (490), `radix` (345), `feather` (286).
   - **Count discrepancy note:** `api/v1/index.json` indexes 134,701 icons while `icons/` has 134,125 canonical icon pages (576 icons deduplicated on slug collision during `generate-pseo.js`).
   - **3 Sample Individual Icon Pages Inspected:**
     - `icons/lucide-home/index.html` (51,854 B) → Title: `Lucide Home Icon — Free SVG & PNG Download | IconStash` (template #1, ≤60 chars); Desc: template #0 (`hashCode % 3 === 0`).
     - `icons/bootstrap-0-circle/index.html` (52,314 B) → Title: `Bootstrap 0 Circle Icon — Free SVG & PNG Download` (template #2, brand suffix dropped to fit ≤60 chars); Desc: template #1 (`hashCode % 3 === 1`, clamped at 158 chars with `…`).
     - `icons/fluent-access-time-24-regular/index.html` (55,001 B) → Title: `Fluent UI Access Time 24 Regular Icon — SVG & PNG Download` (template #3, `Free` and `| IconStash` dropped to fit ≤60 chars); Desc: template #2 (`hashCode % 3 === 2`, clamped at 158 chars with `…`).

2. **Cross-Library Concept Pages — `3,746` directories (`index.html`)**
   - **Naming pattern:** `/icons/{conceptSlug}-icon/` (e.g. `/icons/home-icon/`, `/icons/star-icon/`, `/icons/arrow-left-icon/`). Included when ≥3 libraries ship the concept.
   - **Sitemap:** `sitemaps/concepts.xml` (3,746 entries).

3. **Retired Keyword-Variant 301 Redirect Stubs — `14,915` directories (`index.php`)**
   - Created on `2026-08-31` when 149,040 duplicate keyword-variant pages were collapsed onto the 134,125 canonical icon pages.
   - **Suffix breakdown:** `-icon` (3,662), `-icon-png` (2,991), `(other)` (2,871), `-icon-svg` (2,077), `-svg-and-png-download` (1,479), `-icon-figma` (655), `-icon-for-react` (655), `-outline-icon` (243), `-fill-icon` (150), `-bold-icon` (132).
   - **Exact stub template** (e.g. `icons/0-circle-fill-icon-figma/index.php`):
     ```php
     <?php
     header("Location: /icons/bootstrap-0-circle-fill/", true, 301);
     exit;
     ```
   - **Rebuild requirement:** Preserve all 14,915 301 redirects (either by copying `icons/*/index.php` into `dist/` on Apache or compiling them into a host redirect map).

### 2.3 Exact Slug Lists for Fixed-Taxonomy Directories

- **`library/` (28 subdirs + index):** `antdesign`, `bootstrap`, `boxicons`, `carbon`, `cssgg`, `eva`, `feather`, `fluent`, `heroicons`, `hugeicons`, `iconoir`, `iconparkoutline`, `iconparksolid`, `ionicons`, `linemd`, `lucide`, `material`, `materialsymbols`, `materialsymbolslight`, `mingcute`, `octicons`, `phosphor`, `pixelarticons`, `radix`, `remix`, `simpleicons`, `solar`, `tabler`.
- **`category/` (16 subdirs + index):** `commerce`, `communication`, `data`, `development`, `devices`, `editing`, `files`, `health`, `interface`, `media`, `navigation`, `security`, `social`, `time`, `transport`, `weather`.
- **`style/` (7 subdirs + index):** `bold`, `duotone`, `fill`, `light`, `outline`, `solid`, `thin`.
- **`alternatives/` (17 subdirs + index):** `bootstrap`, `boxicons`, `carbon`, `feather`, `fluent`, `font-awesome` *(hand-authored editorial `TechArticle`)*, `heroicons`, `iconoir`, `ionicons`, `lucide`, `material`, `materialsymbols`, `phosphor`, `radix`, `remix`, `solar`, `tabler`.
- **`icons-for/` (7 subdirs + index):** `angular`, `nextjs`, `react`, `react-native`, `svelte`, `tailwind`, `vue`.
- **`compare/` (120 subdirs + index):** `{libA}-vs-{libB}` (all pairwise combinations of the 16 primary libraries: $\binom{16}{2} = 120$).
- **`Glossary/` (16 subdirs + index):** `icon-file-formats-glossary`, `icon-performance-rendering-glossary`, `icon-svg-terminology`, `svg-accessibility-wcag-glossary`, `svg-animation-smil-and-motion-glossary`, `svg-attributes-glossary`, `svg-clipping-masking-and-compositing-glossary`, `svg-coordinate-systems-and-units-glossary`, `svg-dom-and-javascript-api-glossary`, `svg-elements-and-tags-glossary`, `svg-filters-and-filter-primitives-glossary`, `svg-gradients-patterns-paint-servers-glossary`, `svg-path-syntax-geometry-glossary`, `svg-stroke-fill-and-painting-glossary`, `svg-transforms-matrix-math-glossary`, `svg-typography-and-font-glyphs-glossary`.
- **`Listicles/` (12 subdirs + index):** `bad-svg-performance-practices`, `best-animated-svg-icon-libraries`, `best-dashboard-icon-packs`, `best-duotone-icon-packs`, `best-free-icon-sets-2026`, `best-minimal-line-icon-packs`, `best-react-icon-libraries-2026`, `enterprise-saas-icon-rules`, `free-social-media-icons`, `icon-mistakes-ruining-your-ui`, `icon-ux-bugs-hurting-conversion`, `ui-icons-nobody-can-name`.
- **`articles/` (156 subdirs + index):** Long-form technical guides, library guides, and SVG visualization tutorials (all listed in `articles-sitemap.xml`).
- **`seo/` (150 subdirs + index):** `seo/index.html` links to `seo/sitemap-1/`..`seo/sitemap-138/` (1,000 `/icons/` links each for 1–137, 871 links on 138 = 137,871 total). `seo/sitemap-139/`..`seo/sitemap-150/` are 478 B `<meta http-equiv="refresh" content="0;url=/seo/">` `noindex, follow` stubs.

---

## 3. Page Archetype SEO, Schema, Heading & Internal Linking Specification

### 3.1 Shared Tag Baseline (Programmatic Pages)

All programmatic pages (`icons/*`, `library/*`, `category/*`, `style/*`, `compare/*`, `alternatives/*` except `font-awesome`, `icons-for/*`) share:
- **Canonical:** `<link rel="canonical" href="https://iconstash.io{path}/">` (self-canonical, trailing slash).
- **Open Graph:** `og:type="website"`, `og:title={title}`, `og:description={description}`, `og:url={canonical}`, `og:image="https://iconstash.io/og-default.png"`, `og:image:width="1200"`, `og:image:height="630"`, `og:image:alt={title}`, `og:site_name="IconStash"` *(note: `icons/*` currently omits `og:site_name` in rendered files even though `generate-pseo.js` has it; include `og:site_name="IconStash"` consistently in v2)*.
- **Twitter Card:** `twitter:card="summary_large_image"`, `twitter:title={title}`, `twitter:description={description}`, `twitter:image="https://iconstash.io/og-default.png"`, `twitter:image:alt={title}`.
- **Note on Sidebar `<h2>`s:** In the legacy shell, the persistent left sidebar emits 7 `<h2>` elements (`Libraries`, `Libraries List`, `Styles`, `Categories`, `Preview Size: 24px`, `Sort By`, `Customize Preview`) before the main `<h1>`. In Astro v2, either preserve semantic outline or demote sidebar labels to `<div>`/`<span>` while preserving all main-content `<h1>`–`<h3>` headings below.

---

### 3.2 Per-Archetype Templates & Contracts

#### 1. Homepage (`/`)
- **`<title>`:** `IconStash - 134,701 Free SVG & PNG Icons | Search 28 Libraries`
- **`<meta name="description">`:** `Search, compare, customize, copy, and download 134,701 free SVG and PNG icons across 28 open-source libraries. Set any size, color, or export instantly.`
- **`<meta name="robots">`:** `index, follow, max-image-preview:large, max-snippet:-1`
- **`<link rel="canonical">`:** `https://iconstash.io/`
- **OG / Twitter:** `og:type="website"`, `og:title="IconStash - 134,701 Free SVG & PNG Icons"`, `og:image="https://iconstash.io/og-default.png"` (`1200×630`), `twitter:card="summary_large_image"`.
- **JSON-LD `@type`:** Top-level array `["WebSite", "Organization", "WebApplication"]`.
- **Main Headings:**
  - `H1`: `Compare, animate, export - 134,701 free, open-source icons`
  - `H2`: `Categories` (+ `H3` for each of the 16 categories) and library/feature sections.
- **Internal Linking Blocks:** Header/sidebar links to all 28 `/library/{slug}/`, 16 `/category/{slug}/`, 7 `/style/{slug}/`, plus footer/nav links to `/api/`, `/articles/`, `/compare/`, `/alternatives/`, `/icons-for/`, `/stats/`, `/about/`, `/contact/`, `/privacy/`, `/terms/`.

#### 2. Individual Icon Page (`/icons/{lib}-{slug}/` — 134,125 pages)
- **Generator:** `scripts/generate-pseo.js` (`TITLE_MAX = 60`, `DESC_MAX = 158`, `hashCode` = djb2 XOR).
- **`<title>` cascade** (first option `<= 60` chars wins, where `{Base} = titleCase(keyword)` e.g. `Lucide Home Icon`):
  1. `{Base} — Free SVG & PNG Download | IconStash`
  2. `{Base} — Free SVG & PNG Download`
  3. `{Base} — SVG & PNG Download`
  4. `{Base} | IconStash`
  5. Fallback: `{Base.slice(0, 47).trimWord()} | IconStash`
- **`<meta name="description">` rotation** (`hashCode(icon.id) % 3`, clamped to `158` chars with `…`):
  - `0`: `Download the free {name} icon from {lib} in SVG and PNG. Set any size from 16 to 512px, pick a color, copy the code in one click. No login required.`
  - `1`: `Free {name} icon from {lib} ({style} style). Export SVG, PNG, React JSX or CSS, preview on dark and light backgrounds, then download. No account needed.`
  - `2`: `Get the {lib} {name} icon as SVG or PNG. Adjust size, color and stroke width in the browser, copy clean code, download instantly. Free, no signup.`
- **`<link rel="canonical">`:** `https://iconstash.io/icons/{lib}-{slug}/`
- **OG / Twitter:** Standard programmatic baseline (`og:type="website"`, `og-default.png`).
- **JSON-LD `@type`:** Top-level array `["BreadcrumbList", "FAQPage", "HowTo", "SoftwareApplication", "ImageObject"]`.
  - `BreadcrumbList`: `IconStash` → `Icon libraries` → `{lib}` → *(optional concept hub `/icons/{concept}-icon/`)* → `{displayName}`.
  - `FAQPage`: 7 icon-specific Q&As.
  - `HowTo`: 3 `HowToStep` items.
  - `SoftwareApplication`: `price: "0"`, `author: Great Software Company`.
  - `ImageObject`: `creator: { "@type": "Organization", name: icon.library }`.
- **Main Headings:**
  - `H1`: `{LibShort} {DisplayName} Icon` (e.g. `Lucide Home Icon`)
  - `H2`: `Use the {Name} icon`, `Export formats`, `Aesthetic characteristics`, `UX best practices`, `React / npm — {Lib}`, `Inline SVG (copy & paste)`, `About {Lib}`, `Related searches`
  - `H3`: 7 FAQ questions (`What is the {Name} icon?`, `Is the {Name} icon free to use?`, `How do I use the {Name} icon in React?`, `What is the {Lib} icon library?`, etc.)
- **Internal Linking Blocks:** `nav.crumbs` (`/` → `/library/{lib}/` → `/icons/{concept}-icon/`), related icons grid (~16 `/icons/*` links), sidebar (`/library/*`, `/category/*`, `/style/*`), footer (`/terms/`, `/privacy/`).

#### 3. Cross-Library Concept Page (`/icons/{concept}-icon/` — 3,746 pages)
- **Generator:** `scripts/generate-pseo.js` (`TITLE_MAX = 60`, `DESC_MAX = 158`).
- **`<title>` cascade** (first option `<= 60` chars wins, where `{N}` = library count):
  1. `{Display} Icon — {N} Free SVG & PNG Downloads | IconStash`
  2. `{Display} Icon — {N} Free SVG & PNG Downloads`
  3. `{Display} Icon — {N} Free Downloads`
  4. `{Display} Icon — Free SVG & PNG`
  5. `{Display} Icon | IconStash`
  6. Fallback: `{Display.slice(0, 47).trimWord()} | IconStash`
- **`<meta name="description">` rotation** (`abs(hashCode("c-" + display)) % 3`, clamped to `158` chars):
  - `0`: `Compare {N} free {words} icons from {N} icon libraries. Download any as SVG or PNG, set the exact size and color, and copy the code. No login.`
  - `1`: `{N} free {Display} icons side by side, from {N} open-source libraries. Preview, recolor, download SVG or PNG, or copy React and CSS code instantly.`
  - `2`: `Browse {N} {words} icons across {N} libraries and pick the one that fits. Free SVG and PNG download, custom sizes to 512px, no account needed.`
- **`<link rel="canonical">`:** `https://iconstash.io/icons/{concept}-icon/`
- **OG / Twitter:** Standard programmatic baseline (`og:type="website"`, `og-default.png`).
- **JSON-LD `@type`:** `["BreadcrumbList", "CollectionPage", "FAQPage", "SoftwareApplication"]` (`CollectionPage.mainEntity` = `ItemList` of matching icons).
- **Main Headings:**
  - `H1`: `{Display} icon`
  - `H2`: `{Display} icons from {N} libraries`, `Which library should you use?`, `Inline SVG (copy & paste)`, `React component`, `Match the icon to the interface`, `Accessibility`
  - `H3`: 6 concept FAQ questions (`Where can I download a free {words} icon?`, `Are these {words} icons free for commercial use?`, etc.)
- **Internal Linking Blocks:** `nav.crumbs` (`/` → `/category/`), `.concept-grid` linking to every matching `/icons/{lib}-{slug}/` and `/library/{lib}/`, comparison table (`hub-table-scroll`), related concept links.

#### 4. Library Hub Pages (`/library/` & `/library/{slug}/` — 1 + 28 pages)
- **Generator:** `scripts/generate-hubs.js`.
- **Index (`/library/`):**
  - `<title>`: `28 Free Icon Libraries — 134,701 SVG Icons | IconStash`
  - `<meta name="description">`: `Compare 28 free open-source icon libraries — 134,701 SVG icons. Counts, styles, grids and licenses side by side. Search all at once.`
  - JSON-LD: `["BreadcrumbList", "CollectionPage", "FAQPage"]`
  - `H1`: `Icon Libraries`; `H2`: `Minimal outline sets`, `Multiple weights`, 4 FAQ questions, `Categories`, `Styles`.
- **Detail (`/library/{slug}/`):**
  - `<title>`: `{lib.fullName} — {lib.count} Free {lib.license} SVG Icons | IconStash`
  - `<meta name="description">`: `Browse {lib.count} {lib.fullName} — {lib.style.toLowerCase()} SVG icons, {lib.license} licensed. Copy SVG, export PNG, or install {lib.npm}. Free, no login.` *(drops `Free, no login.` if >158 chars)*
  - `<link rel="canonical">`: `https://iconstash.io/library/{slug}/`
  - JSON-LD: `["BreadcrumbList", "CollectionPage", "FAQPage"]`
  - `H1`: `{lib.fullName}`
  - `H2`: `What {lib.name} is`, `React`, `Plain SVG and other frameworks`, `Good fit`, `Consider alternatives`, `Licensing`, sample category icon grids, 6 FAQ questions.
  - Internal links: `nav.crumbs` (`/` → `/library/`), sample `/icons/{slug}-*/`, related `/compare/` pairs, sibling `/library/*`, `/category/*`, `/style/*`.

#### 5. Category Hub Pages (`/category/` & `/category/{slug}/` — 1 + 16 pages)
- **Generator:** `scripts/generate-hubs.js`.
- **Index (`/category/`):**
  - `<title>`: `Icon Categories — Browse by Topic | IconStash`
  - `<meta name="description">`: `Browse 16 icon categories across 28 open-source libraries. Compare how each library draws the same concept, then copy SVG or export PNG.`
  - JSON-LD: `["BreadcrumbList", "CollectionPage", "FAQPage"]`
  - `H1`: `Icon Categories`; `H2`: 3 FAQ questions.
- **Detail (`/category/{slug}/`):**
  - `<title>`: `{info.name} Icons — {total} Free SVG Icons | IconStash`
  - `<meta name="description">`: `{total} free {info.name.toLowerCase()} icons — {info.blurb}. Compare {libCount} libraries, copy SVG or export PNG. No login.` *(drops `No login.` if >158 chars)*
  - `<link rel="canonical">`: `https://iconstash.io/category/{slug}/`
  - JSON-LD: `["BreadcrumbList", "CollectionPage", "FAQPage"]`
  - `H1`: `{info.name} Icons`
  - `H2`: `What this category covers`, `Most searched`, `More in this category`, `Still more`, `Subcategories in this set`, 5 FAQ questions.
  - Internal links: `nav.crumbs` (`/` → `/category/`), concept/icon links (`/icons/*`), top `/library/*`, `/compare/*`, sibling `/category/*`, `/style/*`.

#### 6. Style Hub Pages (`/style/` & `/style/{slug}/` — 1 + 7 pages)
- **Generator:** `scripts/generate-hubs.js`.
- **Index (`/style/`):**
  - `<title>`: `Icon Styles — Outline, Solid, Duotone & More | IconStash`
  - `<meta name="description">`: `Browse icons by style across 28 open-source libraries — outline, solid, duotone, fill, bold, thin, light. Copy SVG or export PNG free.`
  - JSON-LD: `["BreadcrumbList", "CollectionPage", "FAQPage"]`
  - `H1`: `Icon Styles`; `H2`: 3 FAQ questions.
- **Detail (`/style/{slug}/`):**
  - `<title>`: `{style.title} — {total} Free SVG Icons | IconStash`
  - `<meta name="description">`: `{total} free {style.name.toLowerCase()} icons — {info.blurb}. Compare {libCount} libraries, copy SVG or export PNG. No login.` *(drops `No login.` if >158 chars)*
  - `<link rel="canonical">`: `https://iconstash.io/style/{slug}/`
  - JSON-LD: `["BreadcrumbList", "CollectionPage", "FAQPage"]`
  - `H1`: `{style.title}`
  - `H2`: `What this style means`, `Most searched`, `More examples`, `Across libraries`, `Still more`, 5 FAQ questions.
  - Internal links: `nav.crumbs` (`/` → `/style/`), `/icons/*`, `/library/*`, `/category/*`, sibling `/style/*`.

#### 7. Compare Pages (`/compare/` & `/compare/{libA}-vs-{libB}/` — 1 + 120 pages)
- **Generator:** `scripts/generate-compare.js`.
- **Index (`/compare/`):**
  - `<title>`: `Icon Library Comparisons` *(no brand suffix)*
  - `<meta name="description">`: `Side-by-side comparisons of the most-used open-source icon libraries, with real artwork previews, icon counts, licenses and package names.`
  - JSON-LD: `["BreadcrumbList", "CollectionPage"]`
  - `H1`: `Icon Library Comparisons`; links to all 120 `/compare/{a}-vs-{b}/` pages.
- **Detail (`/compare/{libA}-vs-{libB}/`):**
  - `<title>`: `{a.name} vs {b.name}: Icon Library Comparison` *(no brand suffix)*
  - `<meta name="description">`: `{a.fullName} ships {a.count} icons, {b.fullName} ships {b.count}. Compare grid, license, variants and real side-by-side previews to pick the right one.` (clamped)
  - `<link rel="canonical">`: `https://iconstash.io/compare/{libA}-vs-{libB}/`
  - JSON-LD: `["BreadcrumbList", "FAQPage", "Article"]`
  - `H1`: `{a.name} vs {b.name}`
  - `H2`: `The short answer`, `Specifications compared`, `Same icons, both libraries`, `Which one should you choose?` (`H3`: `Pick {a.fullName} when`, `Pick {b.fullName} when`), `Coverage`, `Licensing`, `Using them from IconStash`, `Frequently asked questions` (+ FAQ `H2`s).
  - Internal links: `nav.crumbs` (`/` → `/compare/`), `.cmp-grid` linking to `/icons/*`, `/library/{a}/`, `/library/{b}/`, `.hub-links` to ~8 related `/compare/*` pairs.

#### 8. Alternatives Pages (`/alternatives/` & `/alternatives/{slug}/` — 1 + 17 pages)
- **Index (`/alternatives/`):**
  - `<title>`: `Icon Library Alternatives`
  - `<meta name="description">`: `Looking for a replacement for your current icon set? Compare alternatives to every major open-source icon library.`
  - JSON-LD: `["BreadcrumbList", "CollectionPage"]`
- **16 Generated Library Alternatives (`/alternatives/{slug}/`, `generate-compare.js`):**
  - `<title>`: `Best {lib.name} Alternatives ({ranked.length} Compared)` *(typically 8 compared)*
  - `<meta name="description">`: `Looking for an alternative to {lib.fullName}? Compare {ranked.length} open-source icon libraries on icon count, license, variants and framework support — with real previews.` (clamped)
  - `<link rel="canonical">`: `https://iconstash.io/alternatives/{slug}/`
  - OG: `og:type="website"`, `og-default.png`.
  - JSON-LD: `["BreadcrumbList", "FAQPage", "ItemList"]` (`ItemList` of `SoftwareApplication` entries).
  - `H1`: `Best {lib.name} Alternatives`; `H2`: `Where {lib.name} is already the right answer`, `How to choose between them`, `Frequently asked questions` (+ FAQ `H2`s), `Explore`, `Popular {lib.name} icons`.
- **1 Editorial Exception (`/alternatives/font-awesome/`):**
  - Hand-authored long-form guide (`og:type="article"`, `og:image="https://iconstash.io/assets/articles/font-awesome-alternatives.jpg"`, `1200×675`).
  - `<title>`: `Best Font Awesome Alternatives 2026: 10 Free Open-Source SVG Replacements | IconStash`
  - JSON-LD: `["TechArticle", "BreadcrumbList", "ItemList", "FAQPage"]`
  - **Parity requirement:** Preserve as an editorial `TechArticle` rather than overwriting with the generated template.

#### 9. Framework ("Icons For") Pages (`/icons-for/` & `/icons-for/{framework}/` — 1 + 7 pages)
- **Generator:** `scripts/generate-compare.js`.
- **Index (`/icons-for/`):**
  - `<title>`: `Icons for Every Framework`
  - `<meta name="description">`: `Which icon library works best with React, Next.js, Vue, Svelte, Tailwind CSS, React Native and Angular.`
  - JSON-LD: `["BreadcrumbList", "CollectionPage"]`
- **Detail (`/icons-for/{framework}/`):**
  - `<title>`: `{stack.title}: Best Icon Libraries for {stack.name}` (e.g. `React Icons: Best Icon Libraries for React`)
  - `<meta name="description">`: `{stack.lead} Compare {picks.length} libraries that work well with {stack.name}, ...` (clamped)
  - `<link rel="canonical">`: `https://iconstash.io/icons-for/{framework}/`
  - JSON-LD: `["BreadcrumbList", "FAQPage", "ItemList"]`
  - `H1`: `{stack.title}`; `H2`: `What to watch for on {stack.name}`, `Recommended starting point`, `Frequently asked questions` (+ FAQ `H2`s), `Explore`, `Popular {stack.name} icons`.

#### 10. Editorial Articles (`/articles/` & `/articles/{slug}/` — 1 + 156 pages)
- **Index (`/articles/`):**
  - `<title>`: `Icon & SVG Articles, Guides & Comparisons | IconStash`
  - `<meta name="description">`: `Guides, comparisons, and deep dives on SVG icons, React icon components, icon systems, and web performance — plus open data on 28 icon libraries. By IconStash.`
  - JSON-LD: `["CollectionPage", "BreadcrumbList", "ItemList"]`
  - `H1`: `Icon & SVG Articles`; links to all 156 `/articles/*`, 16 `/Glossary/*`, 12 `/Listicles/*`, and `/stats/`.
- **Detail (`/articles/{slug}/` — 156 pages):**
  - `<title>`: `{Article Title} | IconStash` (139 pages include `| IconStash`; 17 older pages omit the suffix — preserve exact titles or normalize intentionally with a parity allowlist).
  - `<link rel="canonical">`: 100% `https://iconstash.io/articles/{slug}/` (all 156 have trailing slash).
  - OG / Twitter: `og:type="article"`, `article:published_time`, `article:modified_time`, `article:author`, `article:section`, `article:tag`, `og:image` = custom `/assets/articles/{slug}.jpg` (`1200×675`) or `/og-default.png` (`1200×630`), `twitter:card="summary_large_image"`.
  - **Existing drift to fix in v2:** 15 older articles have `og:url` missing the trailing slash (e.g. `https://iconstash.io/articles/best-open-source-icon-libraries-2026`), duplicate `og:site_name`, and relative `../favicon.svg`. Normalize `og:url` to match `canonical` (with trailing slash) and use root-relative `/favicon.svg`.
  - JSON-LD `@type` distribution across the 156 articles:
    - `TechArticle + BreadcrumbList + FAQPage` (124 pages — standard modern template)
    - `Article + BreadcrumbList` (18 pages)
    - `Article + BreadcrumbList + FAQPage` (11 pages)
    - `Article/TechArticle + BreadcrumbList + FAQPage + ItemList/HowTo` (3 pages)

#### 11. Glossary (`/Glossary/` & `/Glossary/{slug}/` — 1 + 16 pages)
- **Case sensitivity:** Capital `G` (`/Glossary/`). Lowercase `/glossary/*` 301-redirects to `/Glossary/*`.
- **Index (`/Glossary/`):**
  - `<title>`: `SVG & Icon Glossary — Terms, Attributes & Elements | IconStash`
  - JSON-LD: `["BreadcrumbList", "CollectionPage"]`; `H1`: `SVG & Icon Glossary`; links to all 16 `/Glossary/*` subpages.
- **Detail (`/Glossary/{slug}/` — 16 pages):**
  - `<title>`: `{Topic} Glossary: ... | IconStash` (100% carry `| IconStash`).
  - `<link rel="canonical">`: `https://iconstash.io/Glossary/{slug}/` (100% trailing slash; 1 page has `og:url` without trailing slash — normalize).
  - OG: `og:type="article"`, `twitter:card="summary_large_image"`.
  - JSON-LD: Always includes `BreadcrumbList` + `DefinedTermSet` (10 pages also `FAQPage`, 3 pages also `Article + FAQPage`, 3 pages `BreadcrumbList + DefinedTermSet` only).

#### 12. Listicles (`/Listicles/` & `/Listicles/{slug}/` — 1 + 12 pages)
- **Case sensitivity:** Capital `L` (`/Listicles/`). Lowercase `/listicles/*` 301-redirects to `/Listicles/*`.
- **Index (`/Listicles/`):**
  - `<title>`: `Icon Listicles & Ranked Roundups | IconStash`
  - JSON-LD: `["BreadcrumbList", "CollectionPage"]`; `H1`: `Icon Listicles`; links to all 12 `/Listicles/*` subpages.
- **Detail (`/Listicles/{slug}/` — 12 pages):**
  - `<title>`: `{Listicle Title} | IconStash` (100% carry `| IconStash`).
  - `<link rel="canonical">`: `https://iconstash.io/Listicles/{slug}/` (100% trailing slash; 1 page has `og:url` without trailing slash — normalize).
  - OG: `og:type="article"`, `twitter:card="summary_large_image"`.
  - JSON-LD: `Article + BreadcrumbList + FAQPage + ItemList` (8 pages), `Article + BreadcrumbList` (3 pages), `Article + BreadcrumbList + FAQPage` (1 page).

#### 13. HTML Sitemap Pages (`/seo/` & `/seo/sitemap-{1..150}/` — 1 + 150 pages)
- **Robots:** `<meta name="robots" content="noindex, follow">` on **every** `/seo/` page (critical — must NOT be indexed, must remain `follow`).
- **Index (`/seo/`):** `<title>IconStash HTML Sitemap</title>`, `<link rel="canonical" href="https://iconstash.io/seo/">`, `H1: IconStash HTML Sitemap`, 138 links to `/seo/sitemap-1/`..`/seo/sitemap-138/`, no JSON-LD.
- **Active Chunks (`/seo/sitemap-1/`..`/seo/sitemap-138/`):** `<title>IconStash Sitemap {N}</title>`, `<meta name="description" content="IconStash icon pages {start}–{end}.">`, `H1: IconStash Sitemap {N}`, up to 1,000 `/icons/*/` links per page, no JSON-LD.
- **Retired Chunks (`/seo/sitemap-139/`..`/seo/sitemap-150/`):** 12 `noindex, follow` meta-refresh stubs redirecting to `/seo/`.

#### 14. Static Info & Data Pages

| Route | Exact `<title>` | Exact `<link rel="canonical">` | JSON-LD `@type` | `H1` |
|---|---|---|---|---|
| `/stats/` | `Icon Library Statistics 2026: 134,701 Icons, 28 Sets \| IconStash` | `https://iconstash.io/stats/` | `["Dataset", "BreadcrumbList", "FAQPage"]` | `Icon Library Statistics 2026` |
| `/about/` | `About IconStash \| Open Source SVG Icon Engine` | `https://iconstash.io/about/` | `["AboutPage", "BreadcrumbList"]` | `About IconStash` |
| `/contact/` | `Contact & Support \| IconStash` | `https://iconstash.io/contact/` | `["ContactPage", "BreadcrumbList"]` | `Contact & Support` |
| `/privacy/` | `Privacy Policy \| IconStash` | `https://iconstash.io/privacy/` | `["WebPage", "BreadcrumbList"]` | `Privacy Policy` |
| `/terms/` | `Terms of Service \| IconStash` | `https://iconstash.io/terms/` | `["WebPage", "BreadcrumbList"]` | `Terms of Service` |
| `/api/` | `IconStash API - Free, keyless SVG icon API` | `https://iconstash.io/api/` | `WebAPI` (single object) | `IconStash API` |

All 5 info pages (`/stats/`, `/about/`, `/contact/`, `/privacy/`, `/terms/`) include full OG (`og:type="website"`, `og-default.png`) and `twitter:card="summary_large_image"` tags. `/api/` currently omits OG/Twitter tags (adding them in v2 is safe and additive).

---

## 4. Full API, SDK & MCP Parity Inventory (`/api/` & `/data/`)

The IconStash API is a **100% static, keyless, read-only JSON API** with `Access-Control-Allow-Origin: *` (enforced by `.htaccess` for all `*.json` files). No server runtime is required; every path and schema below must remain byte-compatible so existing SDK, MCP, and third-party consumers never break.

### 4.1 File & Endpoint Inventory

| Public Path | Disk Size | Content-Type | Role & Schema Summary |
|---|---:|---|---|
| `/api/` (`api/index.html`) | 10,094 B | `text/html` | Human API/SDK/MCP docs page; `WebAPI` JSON-LD; `H1: IconStash API`; `H2`: `Quick start`, `Endpoints`, `JavaScript SDK`, `MCP server for AI assistants`, `Licences`, `Terms of use`. |
| `/api/v1/manifest.json` | 1,771 B | `application/json` | Service metadata (`name`, `version: "1.0.0"`, `apiBase`, `docs`, `website`, `description`, `licenseNote`, `dataSnapshot`, `generatedAt`, `counts: { libraries: 28, icons: 134701, zeroAttributionIcons: 127291, attributionRequiredIcons: 7410 }`, `endpoints[]`, `sdk`, `mcp`, `terms`). |
| `/api/v1/libraries.json` | 13,049 B | `application/json` | JSON array of **28 library objects**: `{ slug, name, count, version, description, license, attributionRequired, style, grid, npm, docsUrl, hubUrl, dataUrl }`. |
| `/api/v1/index.json` | 19,533,487 B (~19.5 MB raw) | `application/json` | Compact columnar search index: `{ version: 1, format: ["id", "name", "library", "category", "style", "tags"], libraries: string[28], categories: string[16], styles: string[7], icons: [id, name, libIdx, catIdx, styleIdx, tagsString][134701] }`. |
| `/api/v1/openapi.json` | 6,983 B | `application/json` | OpenAPI `3.1.0` spec documenting `GET` operations: `getManifest` (`/api/v1/manifest.json`), `listLibraries` (`/api/v1/libraries.json`), `getIndex` (`/api/v1/index.json`), `getLibrary` (`/data/{slug}.json`), `getOpenApi` (`/api/v1/openapi.json`). |
| `/data/{slug}.json` (28 files) | 204 KB – 24.3 MB each | `application/json` | Full per-library icon array referenced by `libraries[].dataUrl`, SDK, and MCP: `{ id, name, library, librarySlug, libraryVersion, category, subCategory, style, tags[], svgPath, viewBox, strokeWidth, docsUrl, npmPackage, jsxImport }`. |
| `/data/index.json` | 10,277 B | `application/json` | App catalog metadata (`generatedAt`, `marketingTotal: 134701`, `actualIndexed: 134701`, `libraries[28]` with `color`, `tier`, `chunks`, `remotePrefix`). Explicitly allowed in `robots.txt`. |
| `/api/iconstash-sdk.js` | 8,053 B | `application/javascript` | Zero-dependency single-file CommonJS build of `packages/iconstash/index.js` (`@iconstash/sdk` v1.0.0, Node 18+ & browsers). |
| `/api/iconstash-mcp.js` | 15,409 B | `application/javascript` | Zero-dependency single-file runnable stdio JSON-RPC 2.0 MCP server (`#!/usr/bin/env node`), bundling `packages/iconstash/{index.js,mcp.js}`. |

### 4.2 SDK (`api/iconstash-sdk.js`) Public Interface

- **Exports:** `{ createClient, svgMarkup, normalize, tokenize }`
- **Default Base:** `https://iconstash.io/api/v1` (derives `siteRoot` by stripping `/api/v1` to fetch `/data/{slug}.json`)
- **Client Methods:**
  - `manifest()` → `GET /api/v1/manifest.json`
  - `libraries()` → `GET /api/v1/libraries.json`
  - `library(slug)` → `GET /data/{slug}.json`
  - `search(query, { library?, category?, style?, limit? })` → local scoring over `/api/v1/index.json` (limit `1–500`, default `20`), returns `{ id, name, library, category, style, tags, score, url: "https://iconstash.io/icons/{id}/" }`
  - `getIcon(id)` → derives library slug via `id.split('-')[0]`, fetches `/data/{slug}.json` + merges license metadata from `libraries.json`
  - `svg(id, { size?, color?, strokeWidth? })` → renders `<svg ...>`
  - `snippet(id, format = 'svg' | 'jsx' | 'css' | 'html' | 'datauri', options)`
  - `compare(concept, { limit? })` → deduplicates top search hits across up to 28 libraries

### 4.3 MCP Server (`api/iconstash-mcp.js`) Protocol Contract

- **Transport:** `stdio` newline-delimited JSON-RPC 2.0 (`PROTOCOL_VERSION = "2024-11-05"`, `SERVER_INFO = { name: "iconstash", version: "1.0.0" }`).
- **Env override:** `ICONSTASH_API_BASE` (defaults to `https://iconstash.io/api/v1`).
- **Handled JSON-RPC Methods:** `initialize`, `notifications/initialized`, `notifications/cancelled`, `ping`, `tools/list`, `resources/list` (returns `[]`), `resources/templates/list` (returns `[]`), `tools/call`.
- **5 Exposed MCP Tools:**
  1. `search_icons` — required: `query`; optional: `library`, `category`, `style`, `limit` (`1–500`, default `20`).
  2. `get_icon` — required: `id` (e.g. `lucide-camera`).
  3. `get_svg` — required: `id`; optional: `color`, `size`, `strokeWidth`, `format` (`svg` | `jsx` | `css` | `html` | `datauri`).
  4. `compare_concept` — required: `concept`; optional: `limit` (default `28`).
  5. `list_libraries` — no parameters; returns all 28 libraries.

---

## 5. Automated Phase 4 SEO Parity Diff Checklist

Use these exact assertions in the Phase 4 verification script comparing the v2 build (`dist/`) against this baseline:

1. **Zero Lost URLs (Hard Gate):**
   - Parse all 7 child XML sitemaps in baseline → collect exact set of **138,266** URLs.
   - Assert every single URL maps to an existing `index.html` in `dist/` with exact path casing (preserving `/Glossary/` and `/Listicles/`).
   - Assert all **14,915** retired `icons/*/index.php` 301 redirect stubs (or equivalent host redirect rules) are present and target the exact same `/icons/{lib}-{slug}/` destination.
2. **Root & Verification Assets (Hard Gate):**
   - Assert byte-for-byte presence of `robots.txt`, `ads.txt`, `BingSiteAuth.xml`, `naver3487674ab8e7c64ca2ca2862ae597316.html`, `yandex_c4d8a8062ca7c1e5.html`, `e11c5bc79c6d4824bb883b2723c0fa6a.txt`, `favicon.svg`, `favicon.jpeg`, `apple-touch-icon.png`, `logo.png`, `og-default.png`, `llms.txt`, `llms-full.txt`, `.htaccess`.
3. **Meta & Canonical Parity (Sampled + Exhaustive Check):**
   - Every indexable HTML page has a non-empty `<title>`, `<meta name="description">`, `<link rel="canonical">` matching `https://iconstash.io{path}/` (with trailing slash), `og:title`, `og:description`, `og:url` (matching canonical), `og:image`, and `twitter:card="summary_large_image"`.
   - Every `/seo/` and `/seo/sitemap-*/` page and `404.html` has `<meta name="robots" content="noindex, follow">`.
   - Zero indexable pages carry `noindex`.
   - All programmatic `icons/*` titles stay `<= 60` chars and descriptions stay `<= 158` chars.
4. **JSON-LD Schema Parity (Per Archetype):**
   - Validate JSON parses cleanly (`JSON.parse`) on 100% of sampled pages per archetype and contains all required `@type` nodes from §3.2 (`WebSite/Organization/WebApplication` on `/`; `BreadcrumbList/FAQPage/HowTo/SoftwareApplication/ImageObject` on individual icons; `BreadcrumbList/CollectionPage/FAQPage/SoftwareApplication` on concepts; `BreadcrumbList/CollectionPage/FAQPage` on library/category/style hubs; `BreadcrumbList/FAQPage/Article` on compare; `BreadcrumbList/FAQPage/ItemList` on generated alternatives & icons-for; `TechArticle/Article` on editorial; `DefinedTermSet` on Glossary; `Dataset` on `/stats/`; `WebAPI` on `/api/`).
5. **API / SDK / MCP Parity (Hard Gate):**
   - Assert `/api/index.html`, `/api/iconstash-sdk.js`, `/api/iconstash-mcp.js`, `/api/v1/manifest.json`, `/api/v1/libraries.json` (len 28), `/api/v1/index.json` (`icons.length === 134701`), `/api/v1/openapi.json`, and all 28 `/data/{slug}.json` files exist and pass schema validation.
   - Smoke-test `node dist/api/iconstash-mcp.js` with `initialize` + `tools/list` (assert 5 tools) over stdio JSON-RPC 2.0.
