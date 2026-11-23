# IconStash Phase 0 Baseline Audit (UI, CSS, Features & Storage)

**Source repo:** `/working_dir/c_89ae266b383b2b88/iconstash` (branch `rebuild/astro-svelte-v2`)  
**Catalog baseline:** 134,701 SVG icons across 28 open-source libraries (snapshot `2026-05-05`)  
**Purpose:** Single-source-of-truth specification so downstream Astro + Svelte v2 implementation subagents can achieve 100% visual, behavioral, and storage parity without re-reading the legacy codebase.

---

## 1. Architecture & Page Shell (`index.html`)

### 1.1 Document Head, Analytics & Preloads
- Root element: `<html lang="en" data-prerendered="true" data-theme="dark">`
- Analytics: Plausible (`https://plausible.io/js/pa--bfaHBAPFGUV3yUn96sF4.js`) with inline `window.plausible` queue stub.
- Meta: `theme-color: #0A0A0A`, canonical `https://iconstash.io/`, OG (`og-default.png` 1200×630) & Twitter (`summary_large_image`), `favicon.svg` + `favicon.jpeg` apple-touch-icon.
- JSON-LD (3 entities in `@graph` array): `WebSite` (`#website`), `Organization` (`#organization`, founder `Jouni Flemming`, parent `Great Software Company`), `WebApplication` (`#webapp`, `DesignApplication`, price `0`).
- Preloads/prefetches: `style.css`, `vendor/fuse.min.js` (deferred), `icons.js`, `search.js`, `search.worker.js`, `collections.js`, `ui.js`, `app.js`, plus `data/prerender/libraries/lucide/chunk-1.html` & `chunk-2.html`.
- Inline bootstrap globals (`<script id="prerender-data">`):
  - `window.__INDEX_DATA__` (28 library definitions, `marketingTotal: 134701`, `actualIndexed: 134701`).
  - `window.__PRERENDER_MANIFEST__` (`chunkSize: 160`, `totalCount: 134701`, 28 libraries with `chunks` counts).

### 1.2 Top-Level DOM Skeleton
1. `#network-gate.network-gate.hidden` (`role="alert"`): Local-files-ready overlay with `.network-card`, `.network-mark`, and `#network-retry` button (auto-hidden on `ui.init()`).
2. `.bg-canvas` (`aria-hidden="true"`, fixed `z-index: -2`, hidden on `<=767px` and `prefers-reduced-motion`):
   - 4 blurred orbs: `.mesh-orb.orb-1`..`orb-4` (`filter: blur(120px)`, `opacity: 0.09` dark / `0.04` light).
   - 2 corner glows: `.corner-glow.glow-tl` (`400px`) & `.glow-br` (`500px`, hidden in light mode).
   - `.scanlines` (2px repeating horizontal lines, hidden in light mode) and `.noise` (inline SVG `feTurbulence` fractalNoise data URI, `opacity: 0.025` dark / `0.015` light).
3. `.app-shell` (`height: 100vh; display: flex; flex-direction: column`):
   - `<header id="main-header">` (height `58px`, 3-column grid `minmax(190px,260px) minmax(280px,1fr) minmax(150px,260px)`):
     - `.header-left`: `#sidebar-toggle.icon-btn.mobile-only` (hamburger, `aria-controls="left-sidebar"`), `<a class="logo" id="logo-btn" href="/">` (24×24 cube SVG + `IconStash` + `<span class="logo-io">.io</span>`).
     - `.header-center`: `.search-container#search-shell` containing `.search-input-wrapper` (14px search icon, `<input id="main-search" type="search" placeholder="Search 134,701 icons... ( press / )">`, `#search-clear.search-clear.hidden` button `x`), `#search-autocomplete.autocomplete.hidden` (currently disabled via CSS `display: none !important` and no-op JS), and `#result-count.search-results-count.hidden`.
     - `.header-right`:
       - `#nav-icons-btn.nav-link.active` ("Icons")
       - `#draw-open.nav-link` ("Draw")
       - `#compare-toggle.nav-link` ("Compare")
       - `#collections-toggle.nav-link` ("Favorites" + `<span class="badge hidden" id="collection-badge">0</span>`)
       - `#theme-toggle.nav-link` ("Light" when dark / "Dark" when light)
       - `#nav-menu-btn.icon-btn.nav-menu-btn` (shown `<=767px`, toggles `#nav-menu` dropdown with 5 `role="menuitem"` buttons delegating click via `data-nav`).
   - `.workspace` (`flex: 1; display: flex; min-height: 0; overflow: hidden; position: relative`):
     - `#sidebar-collapse.sidebar-collapse` (30×30 circular floating toggle at `left: calc(var(--sidebar-width) + 2px); top: 8px`; desktop only `>=1200px`).
     - `<aside id="left-sidebar">` (`width: 260px`, fixed slide-over drawer `280px` at `<=1199px`):
       - **Libraries** (`.filter-section`): header + `#selected-libs-count` ("All" or `N selected`), `#lib-search.mini-search` ("Filter libraries..."), `#lib-list-container.lib-list` with `.all-icons-row` ("All Icons" `134,701`) + collapsible `.sidebar-card#lib-card-section` (`#lib-toggle`, `#lib-collapse-list`, 28 `<label class="lib-row" data-slug="...">` with visually-hidden `<input class="lib-check" type="checkbox">`).
       - **Styles** (`.sidebar-card.expandable#style-section`): `#style-toggle`, `#style-pills-container.style-pills` (8 buttons: `all`, `outline`, `solid`, `duotone`, `fill`, `bold`, `thin`, `light`).
       - **Categories** (`.sidebar-card.expandable#category-section`): `#category-toggle`, `#category-list-container.category-list` (16 pills populated by JS).
       - **Preview Size** (`.filter-section`): `#preview-size-label` (`Preview Size: 24px`), `#preview-size-slider.neon-slider` (`min=16 max=128 value=24`).
       - **Sort By** (`.filter-section`): `#sort-select.glass-select` (`relevance`, `az`, `za`) + `.unlocked-badge` ("All filters unlocked").
       - **Customize Preview** (`.sidebar-card.expandable#customize-section`): `#customize-toggle`, `#customize-content` with Fill Color (`#cust-color-hex`, `#cust-color-btn.color-wheel-btn`, `#cust-color-wheel` hidden color input), Stroke Width (`#cust-stroke-label` `0.7px`, `#cust-stroke-slider` `min=0.1 max=3 step=0.1 value=0.7`), `#cust-reset-btn` ("Reset").
       - `#clear-filters-btn.outlined-neon-btn` ("Clear All Filters").
     - `<main id="main-content">` containing 4 `.route-view` sections:
       1. `#homepage-view`: Hero (`h1.hero-heading` "Compare, animate, export - 134,701 free, open-source icons" + `.hero-copy`), Categories band (`#home-categories` 16 `.category-card` + `#browse-all-btn`), Featured Libraries band (`#featured-libraries` top 8 `.lib-card`), Featured Free Icons band (`#trending-icons` 24 `.trend-card` + about copy), `.api-promo` developer band (API & MCP quick start), `.home-footer`.
       2. `#privacy-view`: `.legal-document` + `.home-footer`.
       3. `#terms-view`: `.legal-document` + `.home-footer`.
       4. `#grid-view`: `.sr-only` h2, `#seo-header.hidden` (`#seo-title`, `#seo-description`), `.main-toolbar` (`#grid-status` live region, `#load-status`, `.toolbar-api-link` "API & MCP", `.density-toggle` with `compact`/`default`/`comfortable` buttons, `#select-mode-btn` "Select"), `.ad-slot.top-ad.has-api-banner` (house `.api-strip.api-strip-ad` banner linking `/api/`), `#library-error-card.hidden` + `#library-retry-btn`, `#virtual-grid-container` (`tabindex="0"`) containing `#virtual-grid-spacer`, `#icon-grid.density-compact` (prerendered initial Lucide cards), `#loading-more.hidden`, `#no-results.hidden` (broken-glass SVG, `#no-results-text`, `#suggestion-chips`).
     - `<aside id="detail-panel" class="closed">` (`width: 360px` desktop right drawer; mobile `<=767px` fixed bottom sheet `height: min(82vh, 720px)`):
       - `.panel-header`: `#dp-library-name` (`{library} / {name}`), `#dp-title` ("Customize"), `#dp-advance-toggle.advance-toggle` ("Advance", pulsing lime CTA, hidden `<1024px`), `#dp-close.close-btn`.
       - `.panel-content`:
         - `.dp-preview-area`: `#dp-preview-box.preview-box` (`height: 176px`), `.preview-controls` (3 `.bg-toggle`: `dark`, `light`, `checkered`), Preview Size slider (`#dp-size-slider` `16–256`, default `128`, `#dp-size-val`), `.dp-quick-actions` (split Copy button `#qa-copy-btn`/`#qa-copy-caret`/`#qa-copy-menu` with 9 formats; split PNG Download button `#qa-download-btn`/`#qa-download-caret`/`#qa-download-menu` with 7 sizes; color swatch label `#qa-color-btn` wrapping `#dp-color-input` default `#2563eb`).
         - **Customize** (`.dp-section`): `#fill-mode-row` (`solid` | `gradient`), `#gradient-controls.hidden` (`#grad-preview`, `#gradient-stops`, `#grad-add-stop`, `linear`/`radial` toggles, `#grad-angle` `0–360` default `90`, `#grad-radial-rows.hidden` with `#grad-cx` `0–100` / `#grad-cy` `0–100` / `#grad-r` `5–150` default `75`), `#dp-stroke-slider` (`0.1–3` step `0.1` default `0.7`), `#dp-exact-size` number input (`16–512` default `128`).
         - **This icon in other libraries** (`.dp-section`): `#dp-matches.matches-grid` (up to 8 cross-library matches by `baseName`).
         - **Tabs** (`.dp-tabs`): 4-column `.tab-headers` (`Code`, `Download`, `Use`, `Info`):
           - `#tab-copy`: 9 `.format-btn` (`svg`, `xml`, `jsx`, `vue`, `svelte`, `angular`, `html`, `css`, `base64`), `.code-preview-box` (`#dp-code-preview`, `#dp-copy-code`).
           - `#tab-download`: 7 `.size-btn` (`16, 32, 48, 64, 128, 256, 512`), `.download-buttons-group` (`#dp-dl-svg`, `#dp-dl-png`, `#dp-dl-zip`).
           - `#tab-project`: `#dp-install-code` + Copy, `#dp-import-code` + Copy, `#dp-docs-link`.
           - `#tab-meta`: `#dp-lib-badge`, `#dp-tags` (up to 14 clickable `.tag-chip`), `#dp-icon-id` (click-to-copy monospace ID), `.detail-actions-row` (`#dp-favorite`, `#dp-share`, `#dp-compare`).
     - `<aside id="advance-panel">` (`--advance-w: 350px`, desktop `>=1024px` only, collapses to `width: 0` when closed):
       - Header ("Advanced" / "Effects & Motion", `#advance-close`).
       - **Effects**: `Flip H` (`data-flip="h"`), `Flip V` (`data-flip="v"`), `#fx-shadow-toggle` + `#fx-shadow-controls.hidden` (2×2 `.fx-grid2`: Opacity `0–100` def `40`, Blur `0–8` def `2`, X `-30..30` def `0`, Y `-30..30` def `5`), Rotation `#fx-rot` (`0–360` def `0`), Blur `#fx-blur` (`0–2` step `0.1` def `0`), Noise Grain `#fx-noise` (`0–100` def `0`), `#texture-row` (6 chips: `none`, `paper`, `concrete`, `marble`, `wood`, `metal`), `#texture-note` (shown when wood/metal locks color), Texture Opacity `#tex-op` (`0–100` def `30`), Roundness `#fx-round` (`0–3` step `1` def `1` → Soft/Round/Medium/Sharp), `#fx-reset` ("Reset All").
       - **Animate**: 3×2 `#anim-type-row.anim-thumbs` (`off`, `draw`, `stroke`, `bounce`, `shake`, `jump`), Duration `#anim-dur` (`0.5–5` step `0.1` def `2`), `#anim-loop` toggle, 4 easing chips (`inout`, `in`, `out`, `linear`).
   - `#bulk-action-bar.hidden`: fixed bottom bar (`#bulk-num`, `#bulk-color` default `#00c3ff`, `#bulk-download`, `#bulk-collect`, `#bulk-clear`).
4. Modals & Overlay (outside `.app-shell` so `.app-shell` can be marked `inert = true`):
   - `#modal-backdrop.modal-backdrop.hidden` (`z-index: 100`)
   - `#collections-modal.modal.hidden` (`z-index: 110`): `#collection-name-input`, `#collection-create-btn`, `#collections-list`.
   - `#compare-modal.modal.compare-modal.hidden` (`width: min(80vw, 1100px)`): `#compare-title`, `.compare-toolbar` (`With labels`/`Without labels`, `Dark bg`/`Light bg`, `#compare-download`), `#compare-grid`.
   - `#draw-modal.modal.draw-modal.hidden`: `.draw-toolbar` (5 tools: `pen`, `rect`, `ellipse`, `line`, `eraser`; `#draw-ref-toggle`, `#draw-grid-toggle`; `#draw-undo`, `#draw-redo`, `#draw-clear`, `#draw-status`), `#draw-canvas` (`viewBox="0 0 24 24"`, layers `#draw-grid`, `#draw-reference`, `#draw-shapes`, `#draw-preview`), `.draw-options` (`#draw-width` `0.5–4` step `0.25` def `2`, `#draw-color` def `#C1DD2D`, `#draw-ref-label`), `.draw-actions` (`#draw-copy`, `#draw-download-svg`, `#draw-download-png`).
   - `#shortcuts-modal.modal.hidden`: 8 `.shortcut-row` items.
   - `#toast-container` (`aria-live="polite"`, fixed `right: 18px; bottom: 18px; z-index: 130`).

---

## 2. Design System & CSS Tokens (`style.css`, 3,780 lines)

### 2.1 Theme Tokens (`:root` Dark vs `[data-theme="light"]`)

| Token | Dark (`:root`) | Light (`[data-theme="light"]`) | Notes |
|---|---|---|---|
| `--bg-void` | `#0A0A0A` | `#F9F9F9` | Page void / canvas background |
| `--bg-base` | `#0A0A0A` | `#F9F9F9` | Header / sidebar base |
| `--bg-surface` | `#111111` | `#FFFFFF` | Cards, panels, modals |
| `--bg-elevated` | `#161616` | `#F1F1F1` | Elevated pills, inputs |
| `--bg-hover` | `#141414` | `#ECECEC` | Card hover / selected bg |
| `--glass-1` | `rgba(255,255,255,0.015)` | `rgba(0,0,0,0.01)` | On `<=767px`: `var(--bg-surface)` |
| `--glass-2` | `rgba(255,255,255,0.03)` | `rgba(0,0,0,0.02)` | On `<=767px`: `var(--bg-surface)` |
| `--glass-3` | `rgba(255,255,255,0.045)` | `rgba(0,0,0,0.03)` | On `<=767px`: `var(--bg-elevated)` |
| `--glass-4` | `rgba(255,255,255,0.06)` | `rgba(0,0,0,0.04)` | On `<=767px`: `var(--bg-hover)` |
| `--border` / `--glass-border` | `#1F1F1F` | `#E5E5E5` | Mobile light: `#E0E0E0` |
| `--border-hover` / `--glass-border-bright` | `#2A2A2A` | `#CCCCCC` | Mobile light: `#D0D0D0` |
| `--text-primary` | `#F2F2F2` | `#111111` | Primary ink |
| `--text-secondary` | `#888888` | `#555555` | Secondary copy |
| `--text-muted` | `#8A8A8A` | `#6B6B6B` | WCAG AA >= 5.0:1; `.logo-io`, `.category-count`, `.ad-placeholder`, `.dp-tags-label`, `.sitemap-link` overridden to `#767693` (dark) / `#767696` (light) |
| `--text-subtle` | `#333333` | `#CCCCCC` | Dividers / missing indicators |
| `--icon-color` | `#888888` | `#555555` | Grid icon default color |
| `--icon-strong` | `#F2F2F2` | `#111111` | Grid icon hover/focus color |
| `--neon-blue` / `--accent-blue` | `#C1DD2D` | `#4A6B00` | Light override for 5.87:1 AA contrast |
| `--control-blue` | `#C1DD2D` | `#9EB822` | Active tabs, sliders, focus rings |
| `--neon-green` / `--neon-teal` | `#C1DD2D` | `#9EB822` | Accent family (lime-yellow) |
| `--neon-pink` / `--neon-purple` / `--neon-orange` / `--neon-yellow` | `#C1DD2D` | (inherited `#C1DD2D`) | Unified lime accent |
| `--neon-red` | `#FF6B6B` | (inherited `#FF6B6B`) | Destructive / error |
| `--btn-primary-bg` | `#C1DD2D` | `#9EB822` | Primary CTA fill |
| `--btn-primary-hover` | `#D2ED3E` | `#89A01C` | Primary CTA hover |
| `--btn-primary-text` | `#0A0A0A` | `#0A0A0A` | Dark ink on lime (8.8:1) |
| `--btn-primary-glow` | `0 2px 10px rgba(193,221,45,0.15)` | `none` (line 2916 override) | Glows stripped in light mode |
| `--neon-home-header` | `#C1DD2D` | `#9EB822` | Hero H1 color |
| `--grad-cyber` (and `acid`/`fire`/`toxic`/`aurora`/`sunset`/`ice`) | `linear-gradient(135deg, #C1DD2D 0%, #9EB822 100%)` | inherited | Primary gradient |
| `--grad-void` | `linear-gradient(135deg, #C1DD2D 0%, #FF6B6B 100%)` | inherited | Network gate mark |
| `--glow-blue/pink/green/purple/multi` | `none` | `none` | Flat dark aesthetic |

### 2.2 Typography, Layout & Radii Tokens
- `--font-primary`: `"Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif` (base `14px/1.45` on app shell; static pages load Google Fonts Inter 400–900 + JetBrains Mono 400–500).
- `--font-mono`: `"JetBrains Mono", "SFMono-Regular", Consolas, monospace`.
- Layout dimensions: `--header-height: 58px`, `--sidebar-width: 260px` (`0px` when `body.sidebar-collapsed`), `--detail-width: 360px`, `--advance-w: 350px`.
- Radii: `--radius-badge: 4px`, `--radius-button: 6px`, `--radius-card: 8px`, `--radius-panel: 10px`.
- Grid density tokens:
  - `.density-compact` (default): `--card-size: 60px; --card-row-height: 68px` (no card name shown).
  - `.density-default`: `--card-size: 80px; --card-row-height: 88px` (no card name shown).
  - `.density-comfortable`: `--card-size: 100px; --card-row-height: 118px` (`padding-bottom: 20px`, shows `.card-name` 10px).
  - Gap: `8px`. Custom preview size: `--preview-size` (default `24px`, range `16–128px`).
- Syntax highlighting (`.code-preview-box code`):
  - Dark: base `var(--neon-green)`, `.code-str: #85e89d`, `.code-cmt: #959da5`, `.code-kw: #f97583`.
  - Light: base `var(--neon-green)`, `.code-str: #006400`, `.code-cmt: #555577`, `.code-kw: #0000aa`.
- Light mode global override (lines 2914–2946): strips all `text-shadow`, `.corner-glow`, and neon glows.

### 2.3 Breakpoints & Responsive Behavior
- `<=1199px`: `#left-sidebar` becomes fixed off-canvas drawer (`width: 280px`, `top: 58px`, toggled by `body.sidebar-open`); `#sidebar-collapse` hidden; `#sidebar-toggle.mobile-only` shown; `#bulk-action-bar` `left: 18px`.
- `<=1023px`: `#dp-advance-toggle` and `#advance-panel` hidden (`display: none`).
- `<=900px`: `.api-promo` collapses from 2-col to 1-col.
- `<=768px`: `.collection-row` stacks vertically.
- `<=767px`:
  - `.bg-canvas` hidden; all `backdrop-filter` disabled; `--glass-*` mapped to opaque surface tokens.
  - Header becomes `auto 1fr auto`, `.logo-icon` & `.logo-text` hidden, `.header-right .nav-link` hidden, `#nav-menu-btn` shown, `.search-results-count` hidden.
  - `#detail-panel` becomes bottom sheet (`height: min(82vh, 720px)`, `border-radius: 18px 18px 0 0`, closes on outside click).
  - `.modal` & `.compare-modal` become bottom sheets (`max-height: 90vh`, `border-radius: 16px 16px 0 0`, `modalInMobile` animation).
  - `.tab-headers` becomes 2×2 grid; `.detail-actions-row` 1-col; `.stats-bar` & `.how-band` 1-col; `.category-card-grid` & `.featured-libraries` 2-col.
  - `.hero-heading` scales to `clamp(28px, 7.5vw, 40px)`.
- `<=640px`: `.api-strip-cta` hidden; `.concept-grid` minmax `96px`; `.cmp-grid-head`/`.cmp-cell` `1fr 1fr 64px`.
- `<=520px`: `#compare-toggle` and `#theme-toggle` hidden (redundant with `<=767px` nav menu).
- `<=420px`: `.category-card-grid` & `.featured-libraries` 1-col; `.density-toggle` hidden; `.hero-heading` `26px`.

### 2.4 Keyframe Animations & Accessibility
- Keyframes in `style.css`: `bgLoad`, `lissajousA`–`D`, `scanlines`, `grainShift`, `cornerPulse`, `headerSlide`, `drawLine`, `spinSlow`, `searchGrow`, `rotateBorder` (`@property --angle`), `dropdownIn`, `numberPop`, `pulseBadge`, `sidebarIn`, `libSpinnerRotate`, `libRowPulse`, `libSlide`, `checkDraw`, `wordIn`, `hueSpin`, `marqueeLeft`, `marqueeRight`, `floatIcon`, `shimmer`, `cardFlip`, `iconBreath`, `drawCheck`, `ripple`, `brokenFloat`, `chipIn`, `swatchIn`, `panelContentIn`, `particleBurst`, `bulkIn`, `backdropIn`, `modalIn`, `modalInMobile`, `toastIn`, `toastOut`, `toastBar`, `popoverFadeIn`, `spin`, `qaMenuIn`, `an-draw`, `an-flow`, `an-bounce`, `an-shake`, `an-jump`, `advancePulse`.
- Accessibility: `.sr-only` utility; `:focus-visible` `outline: 2px solid var(--control-blue) !important; outline-offset: 2px`; `.lib-check` visually hidden (`1px×1px, opacity: 0`) so all 28 checkboxes stay keyboard-focusable; `@media (prefers-reduced-motion: reduce)` collapses all animation/transition durations to `1ms`, hides `.bg-canvas` layers, stops `.anim-thumb` & `.advance-toggle` animations, and skips JS rAF count-up & particle bursts in `ui.js`.

---

## 3. Complete Feature & Data Inventory

### 3.1 All 28 Icon Libraries (Exact Order & Metadata)

| # | Name | Slug | Count | Version | License | Tier | JSON Chunks (500) | Prerender Chunks (160) | npm Package | `remotePrefix` |
|---|---|---|---|---|---|---|---:|---:|---|---|
| 1 | Lucide | `lucide` | 1,979 | 0.468.0 | ISC | 1 | 4 | 13 | `lucide` | `lucide` |
| 2 | Tabler Icons | `tabler` | 6,324 | 3.24.0 | MIT | 1 | 13 | 40 | `@tabler/icons` | `tabler` |
| 3 | Phosphor | `phosphor` | 9,198 | 2.1.0 | MIT | 2 | 19 | 58 | `@phosphor-icons/core` | `ph` |
| 4 | Material Design Icons | `material` | 14,001 | 7.4.47 | Apache 2.0 | 2 | 29 | 88 | `@mdi/js` | `mdi` |
| 5 | Remix Icons | `remix` | 3,244 | 4.6.0 | Apache 2.0 | 2 | 7 | 21 | `remixicon` | `ri` |
| 6 | Iconoir | `iconoir` | 2,020 | 7.10.0 | MIT | 2 | 5 | 13 | `iconoir` | `iconoir` |
| 7 | Heroicons | `heroicons` | 1,297 | 2.2.0 | MIT | 1 | 3 | 9 | `heroicons` | `heroicons` |
| 8 | Bootstrap Icons | `bootstrap` | 2,090 | 1.11.3 | MIT | 2 | 5 | 14 | `bootstrap-icons` | `bi` |
| 9 | Feather | `feather` | 286 | 4.29.2 | MIT | 2 | — | 2 | `feather-icons` | `feather` |
| 10 | Mingcute | `mingcute` | 3,352 | 2.97.0 | Apache 2.0 | 2 | 7 | 21 | `mingcute_icon` | `mingcute` |
| 11 | Solar Icons | `solar` | 7,410 | 1.0.0 | CC BY 4.0 | 2 | 15 | 47 | `solar-icon-set` | `solar` |
| 12 | Octicons | `octicons` | 929 | 19.13.0 | MIT | 2 | 2 | 6 | `@primer/octicons` | `octicon` |
| 13 | CSS.gg | `cssgg` | 705 | 2.1.1 | MIT | 2 | 2 | 5 | `css.gg` | `gg` |
| 14 | Radix Icons | `radix` | 345 | 1.3.2 | MIT | 2 | — | 3 | `@radix-ui/react-icons` | `radix-icons` |
| 15 | Ant Design Icons | `antdesign` | 1,870 | 5.5.2 | MIT | 2 | 4 | 12 | `@ant-design/icons` | `ant-design` |
| 16 | Fluent UI Icons | `fluent` | 20,170 | 2.0.293 | MIT | 3 | 41 | 127 | `@fluentui/svg-icons` | `fluent` |
| 17 | Carbon Icons | `carbon` | 2,644 | 11.57.0 | Apache 2.0 | 3 | 6 | 17 | `@carbon/icons` | `carbon` |
| 18 | Ionicons | `ionicons` | 2,607 | 7.4.0 | MIT | 3 | 6 | 17 | `ionicons` | `ion` |
| 19 | Eva Icons | `eva` | 490 | 1.1.3 | MIT | 3 | 1 | 4 | `eva-icons` | `eva` |
| 20 | Boxicons | `boxicons` | 3,389 | 2.1.4 | MIT | 3 | 7 | 22 | `boxicons` | `bx,bxs,bxl` |
| 21 | Material Symbols | `materialsymbols` | 18,547 | current | Apache 2.0 | 4 | 38 | 116 | `material-symbols` | `material-symbols` |
| 22 | Material Symbols Light | `materialsymbolslight` | 15,969 | current | Apache 2.0 | 4 | 32 | 100 | `material-symbols` | `material-symbols-light` |
| 23 | IconPark Outline | `iconparkoutline` | 2,658 | 1.4.2 | Apache 2.0 | 4 | 6 | 17 | `@icon-park/svg` | `icon-park-outline` |
| 24 | IconPark Solid | `iconparksolid` | 1,970 | 1.4.2 | Apache 2.0 | 4 | 4 | 13 | `@icon-park/svg` | `icon-park-solid` |
| 25 | Huge Icons | `hugeicons` | 5,115 | current | MIT | 4 | 11 | 32 | `hugeicons` | `hugeicons` |
| 26 | Pixel Art Icons | `pixelarticons` | 1,099 | 2.1.0 | MIT | 4 | — | 7 | `pixelarticons` | `pixelarticons` |
| 27 | Line MD | `linemd` | 1,279 | 3.0.5 | MIT | 4 | 3 | 8 | `line-md` | `line-md` |
| 28 | Simple Icons | `simpleicons` | 3,714 | 16.18.0 | CC0 1.0 | 4 | 8 | 24 | `simple-icons` | `simple-icons` |

- **Data record schema** (`data/{slug}.json` & `data/{slug}-{n}.json`):
  `{ id, name, nameVariants, library, librarySlug, libraryVersion, style, tags, category, subCategory, svgPath, viewBox, width, height, strokeWidth, hasVariants, variantIds, docsUrl, npmPackage, jsxImport, popularity, dateAdded }`.
- **Loading strategy**:
  - Prerender browse mode (`shouldUsePrerenderBrowse()`): active when no search/category/style/non-relevance sort and library not yet in memory; streams `data/prerender/libraries/{slug}/chunk-{n}.html` (160 cards/chunk) with 3-chunk lookahead (8 on mobile).
  - Desktop full JSON (`data/{slug}.json`); mobile chunked JSON (`data/{slug}-1.json` foreground, remaining chunks background with 120ms yield, 2 retry attempts, 400ms backoff, fallback to full JSON).
  - Background sync (`triggerBackgroundSync()`): starts 2s after boot (or immediately on search/filter/deep-link), delays 2.5s desktop / 3.5s mobile, loads tiers 1→4 with concurrency 4 desktop / 2 mobile, caches in IndexedDB (7-day TTL).

### 3.2 All 8 Style Filters & Classification
- Pills (`data-style`): `all`, `outline`, `solid`, `duotone`, `fill`, `bold`, `thin`, `light`.
- `deriveStyle(name, prefix)` precedence: `duotone|two-tone|twotone` → `duotone`; `bold|filled|fill|solid|bxs-` → `bold`; `thin` → `thin`; `light` → `light`; `sharp` → `solid`; `regular|outline|linear|stroke|lucide|tabler|feather|iconoir|radix|hugeicons|line-md` → `outline`; `bxl-|brand` → `fill`; fallback → `fill`.

### 3.3 All 16 Category Filters (`CATEGORY_META`)
1. `Media` ("Photography") — `/camera|image|photo|video|film|play|pause|music|mic|speaker|audio|volume|gallery|picture|podcast/`
2. `Communication` ("Messaging") — `/mail|message|chat|comment|phone|call|send|inbox|reply|share|bell|notification/`
3. `Commerce` ("Payments") — `/cart|shop|bag|store|cash|coin|credit|card|wallet|bank|receipt|ticket|tag|gift/`
4. `Navigation` ("Maps") — `/map|pin|location|compass|route|arrow|chevron|direction|sign|road|globe/`
5. `Files` ("Documents") — `/file|folder|document|book|note|clipboard|archive|copy|paper|pdf|code/`
6. `Editing` ("Design") — `/edit|pen|pencil|brush|crop|palette|color|magic|wand|scissors|ruler|layout/`
7. `Devices` ("Hardware") — `/phone|mobile|tablet|laptop|desktop|monitor|keyboard|mouse|printer|watch|cpu|server|database/`
8. `Development` ("Code") — `/code|terminal|bug|git|branch|merge|api|webhook|cloud|database|server|package/`
9. `Security` ("Privacy") — `/lock|unlock|shield|key|fingerprint|scan|secure|vpn|password|verified/`
10. `Health` ("Medical") — `/heart|pulse|medical|hospital|doctor|pill|virus|health|first|aid|stethoscope/`
11. `Weather` ("Nature") — `/sun|moon|cloud|rain|snow|wind|leaf|tree|flower|fire|water|earth/`
12. `Transport` ("Travel") — `/car|bus|train|plane|ship|bike|truck|taxi|rocket|suitcase|luggage/`
13. `Social` ("People") — `/user|person|people|team|group|face|smile|emoji|profile|account/`
14. `Time` ("Productivity") — `/clock|time|calendar|timer|alarm|hour|watch|schedule|history/`
15. `Data` ("Charts") — `/chart|graph|analytics|stats|database|table|trend|activity|bar|pie/`
16. `Interface` ("Controls") — default fallback when no regex matches.

### 3.4 Search Engine & Virtual Grid (`search.js`, `search.worker.js`, `app.js`)
- **Web Worker (`search.worker.js`)**: Loads `vendor/fuse.min.js`. Fuse config: `includeScore: true`, `threshold: 0.32`, `distance: 96`, `ignoreLocation: true`, `minMatchCharLength: 1`.
  - Weighted keys: `name` (`0.62`), `tags` (`0.48`), `nameVariants` (`0.20`), `category` (`0.12`), `subCategory` (`0.10`), `library` (`0.08`), `librarySlug` (`0.06`).
  - Stale-query cancellation via incrementing `queryId` + `{ type: 'cancel' }` message.
  - Main-thread fallback (`textFallback`): tokenizes on `/[^a-z0-9]+/`, scores `+4` if in `name`, `+1` if in haystack, tie-breaks by `popularity`.
- **Query sanitization (`sanitizeQuery`)**: strips HTML tags, `javascript:`, `<script>`, any char outside `[a-zA-Z0-9\s\-_]`, max 100 chars. Input debounced `300ms`.
- **`baseName(name)`**: strips trailing style/size suffixes (`outline|regular|solid|filled|fill|bold|duotone|thin|light|sharp|round|linear|twotone|two-tone|24|20|16|12`) for cross-library matching and Compare Mode.
- **Virtual Grid**:
  - **Grouped search mode** (`isGroupedSearchMode()`): active when `searchQuery` is non-empty, `sort === "relevance"`, and `selectedLibraries.size !== 1`. Buckets results by `librarySlug`, inserts `.library-break` header rows, virtualizes with ±4 row overscan.
  - **Flat virtual mode**: virtualizes with ±6 row overscan, recycles DOM nodes in-place (`updateCardElement`), clones cached SVG nodes (`svgCache`), updates `#virtual-grid-spacer` height and `translateY`.
  - Empty state (`#no-results`): shows 6 clickable suggestion chips (`camera`, `arrow`, `user`, `chart`, `download`, `lock`).

### 3.5 SVG Rendering & Customization Studio (`icons.js`, `app.js`)
- **Solid color & global preview sync**: Detail color (`#dp-color-input`, default `#2563eb`) syncs live to `#icon-grid` and `#trending-icons` via `--custom-icon-color` + `.customized-preview-color` and sidebar `#cust-color-hex`/`#cust-color-wheel`. Sidebar auto-color defaults to `#ffffff` (dark) / `#000000` (light).
- **Multi-stop Gradients**: 2 to 5 stops (`{ c: hex, p: 0..100 }`), default `[{ c: "#C1DD2D", p: 0 }, { c: "#2563eb", p: 100 }]`. Adding a stop splits the largest percentage gap.
  - **Linear**: `angle` `0–360°` (default `90°`), mapped to `x1/y1/x2/y2` percentages via `rad = (angle - 90) * π / 180`.
  - **Radial**: `cx` (`0–100%`, def `50`), `cy` (`0–100%`, def `50`), `r` (`5–150%`, def `75`).
  - Replaces `fill="currentColor"` and `stroke="currentColor"` with `url(#{uid}-grad)`.
- **Stroke Width**: `0.1–3.0px` (step `0.1`, default `0.7px`).
- **Export Dimensions**: Exact Size `16–512px` (default `128px`), synced with Detail Preview Size slider (`16–256px`). Grid Preview Size slider: `16–128px` (default `24px`, CSS `--preview-size`).
- **Transforms**:
  - Flip H (`scale(-1 1)` around viewBox center), Flip V (`scale(1 -1)`).
  - Rotation (`0–360°`): `rotate(rot cx cy)` AND dynamically expands `viewBox` bounding box (`boxW = vw*|cos| + vh*|sin|`, `boxH = vw*|sin| + vh*|cos|`) so rotated corners never clip.
- **SVG Filter Chain (`<filter id="{uid}-fx" x="-45%" y="-45%" width="190%" height="190%">`)**, chained sequentially:
  1. **Blur**: `feGaussianBlur stdDeviation` (`0–2`, step `0.1`).
  2. **Drop Shadow**: `feDropShadow` (`dx`: `-20..20` clamped from slider `-30..30`, `dy`: `-20..20` def `5`, `stdDeviation`: `0–8` def `2`, `flood-color="#000000"`, `flood-opacity`: `0–1` def `0.40`). Enabling shadow while preview bg is `dark` auto-switches preview bg to `light`.
  3. **Noise Grain**: `feTurbulence` (`fractalNoise`, `baseFrequency="0.9"`, `numOctaves="2"`) → `feColorMatrix` alpha `noise/100` → `feComposite operator="in"` → `feMerge`.
  4. **5 Surface Textures** (`textureOpacity` `0–100`, default `30`):
     - `paper` (surface finish): blotch (`0.16`, 3 oct, seed 5), fibre & speck (`0.9 0.55`, 2 oct, seed 12), plus `feDiffuseLighting` bump relief (`0.75`, surfaceScale `1.4`, azimuth `55`, elevation `62`, multiply blend).
     - `concrete` (surface finish): 4 aggregate scales (`0.13`, `0.5`, `0.32`, `1.2`) + `feDiffuseLighting` bump relief (`0.18`, surfaceScale `2.6`, azimuth `70`, elevation `48`, multiply blend).
     - `marble` (surface finish): dark mineral veins (`0.014 0.045`, 6 oct, seed 7 + `feComponentTransfer` table), light calcite threads (`0.024 0.07`, 5 oct, seed 23), clouding (`0.05`, 3 oct, seed 41).
     - `wood` (**real material — locks color/gradient controls**): 24-stop radial growth-ring gradient (`cx:50% cy:50% r:78% fx:43% fy:39%`, `#E0BB8C`..`#4E2F16`) + `feDisplacementMap` (`0.045`, scale `1.3`) + longitudinal grain (`0.62 0.014`) + mottling (`0.03`).
     - `metal` (**real material — locks color/gradient controls**): 15-stop diagonal linear silver specular gradient (`#3E4650`..`#FFFFFF`..`#98A3B0`) + horizontal brushed streaks (`0.006 0.85`) + `feSpecularLighting` bevel highlight (`surfaceScale="1.6"`, `specularConstant="0.6"`, `specularExponent="26"`, `azimuth="225"`, `elevation="58"`, arithmetic composite).
- **Roundness presets** (`#fx-round` `0–3`):
  - `0` `soft`: `cap="round"`, `join="round"`, `widthScale: 0.75`
  - `1` `round` (default): `cap="round"`, `join="round"`, `widthScale: 1`
  - `2` `medium`: `cap="round"`, `join="bevel"`, `widthScale: 1`
  - `3` `sharp`: `cap="butt"`, `join="miter"`, `widthScale: 1`
  - Strips inline `stroke-linecap`, `stroke-linejoin`, `stroke-width` from inner paths when active.
- **Animations** (embedded `<style>` inside SVG + `<g class="is-m is-m-{type}" style="transform-box:fill-box;transform-origin:center">`):
  - **5 active animation types** (plus `off`): `draw` (`pathLength="1"`, `stroke-dasharray: 1; stroke-dashoffset: 1 → 0`), `stroke` (`stroke-dasharray: 5 3; stroke-dashoffset: 0 → -32`), `bounce` (`translateY(-22%)` + squash/stretch `scale`), `shake` (`rotate(-9deg / 9deg)`), `jump` (`translateY(-18% / -7%)`).
  - Controls: `duration` `0.5–5.0s` (step `0.1`, def `2.0s`), `loop` boolean (`infinite` vs `1`, def `true`), `easing` (`inout` → `ease-in-out`, `in` → `ease-in`, `out` → `ease-out`, `linear` → `linear`).

### 3.6 Draw an Icon Studio (`#draw-modal`)
- Canvas: `<svg id="draw-canvas" viewBox="0 0 24 24">` with pointer capture (`touch-action: none`).
- 5 tools:
  - `pen`: records points (`>=0.12` unit spacing), simplifies on pointer-up via Ramer-Douglas-Peucker (`tolerance: 0.15`), converts to smooth Catmull-Rom cubic Bezier (`C` commands).
  - `rect`: `M x y H ... V ... Z` (Shift constrains square).
  - `ellipse`: dual-arc `A` path (Shift constrains circle).
  - `line`: `M x1 y1 L x2 y2` (Shift snaps to 45° increments).
  - `eraser`: hit-tests `[data-draw-path]` via `document.elementFromPoint` on pointerdown/move; groups entire drag into 1 undo snapshot.
- Overlays: toggleable 24×24 dot grid + 4-unit major lines + lime center crosshairs (`#draw-grid`); toggleable trace reference of currently open icon at `opacity: 0.16` (`#draw-reference`).
- History: 80-step `undoStack` / `redoStack` (`Ctrl/Cmd+Z`, `Ctrl/Cmd+Shift+Z`, `Ctrl/Cmd+Y`).
- Options: stroke width `0.5–4` (step `0.25`, def `2`), color `#C1DD2D`.
- Exports: Copy SVG, Download `iconstash-drawn-icon.svg`, Download 256px PNG (`iconstash-drawn-icon-256.png`). Auto-persists to `localStorage["iconstash-draw-draft"]`.

### 3.7 Export Formats, PNG Sizes, Bulk ZIP & Collections
- **9 Code formats** (`icons.js:formatCode`):
  1. `svg`: full standalone `<svg xmlns="http://www.w3.org/2000/svg" ...>`
  2. `xml`: `<?xml version="1.0" encoding="UTF-8"?>\n` + SVG
  3. `jsx`: `icon.jsxImport` or `import { PascalName } from '{npmPackage}';`
  4. `vue`: `<template>\n  {svg}\n</template>`
  5. `svelte`: `<script>\n  export let size = {size};\n</script>\n` + SVG with `width="{size}" height="{size}"`
  6. `angular`: `<span class="iconstash-icon" aria-hidden="true">{svg}</span>`
  7. `html`: `<img src="data:image/svg+xml,{encoded}" width="{size}" height="{size}" alt="{name} icon">`
  8. `css`: `.icon-{slug} { width; height; background-color: currentColor; mask: url("data:image/svg+xml,{encoded}") center / contain no-repeat; }`
  9. `base64`: `data:image/svg+xml;base64,{btoa(...)}`
- **7 PNG export sizes**: `16, 32, 48, 64, 128, 256, 512` (rendered via HiDPI `devicePixelRatio` `<canvas>`, filename `{librarySlug}-{nameSlug}-{size}.png`).
- **ZIP exports** (lazy-loads `vendor/jszip.min.js`, caps at **200 icons**, folder `IconStash/`, includes `icons.json` manifest with `{ id, name, library, tags }`):
  - Detail panel ZIP: SVG + PNGs at `[16, 32, 64, 128, 256, 512]` (note: omits 48).
  - Collection "Download ZIP": SVGs only.
  - Collection "Download PNG ZIP": SVGs + PNGs at `[16, 32, 48, 64, 128, 256, 512]`, filename `{collectionSlug}-png.zip`.
  - Bulk Selection ZIP & Compare Modal ZIP: SVGs only (`IconStash-icons.zip`).
- **Collections (`collections.js`)**: Default `"favorites"` collection (non-deletable) + user-created named folders (create, rename via `prompt`, delete, add/remove/reorder icons). Developer exports per collection:
  - `React JSX` (`{slug}.jsx`), `Vue` (`{slug}.vue-snippets`), `SVG Sprite` (`{slug}-sprite.svg` with `<symbol id="{icon.id}">`), `CSS Sprite` (`{slug}.css` mask rules), `JSON list` (`{slug}.json`).
- **Multi-select & Bulk Bar**: `#select-mode-btn` toggles `select-mode-active` (hides heart buttons, shows `.select-check` badges). `#bulk-action-bar` supports Set Color (`#bulk-color`), Download ZIP, Add to Collection (popover), Clear.
- **Compare Mode**: Opens `#compare-modal` with up to 80 cross-library matches sharing `baseName(icon.name)`, applying current detail color/stroke/gradient. Toolbar toggles `With/Without labels`, `Dark/Light bg`, and `Download all as ZIP`. If no icon is open, renders 3-step instructional placeholder card.

### 3.8 Keyboard Shortcuts
- `/`: Focus search input (when not in `INPUT`/`TEXTAREA`/`SELECT`).
- `Esc`: Close quick-action menus → close mobile nav menu → close open modal → close detail panel → clear search query.
- `ArrowRight` / `ArrowLeft` / `ArrowDown` / `ArrowUp`: Navigate grid by `±1` / `±cols` (moves real DOM focus and scrolls into view).
- `Enter` / `Space` (on focused `.icon-card`): Activates card click.
- `Ctrl/Cmd + C`: Copy focused icon SVG.
- `Ctrl/Cmd + D`: Download focused icon SVG.
- `Ctrl/Cmd + A` (when `selectMode` active): Select all `filteredIcons`.
- `F`: Add focused icon to `"favorites"` collection.
- `?`: Open `#shortcuts-modal`.
- `Ctrl/Cmd + Z`, `Ctrl/Cmd + Shift + Z`, `Ctrl/Cmd + Y` (when `#draw-modal` open): Undo / Redo.
- `Tab` / `Shift+Tab` (when modal open): Focus trap inside active modal (`ui.js`).

### 3.9 Routing, Startup & `404.html`
- Hash routes in `app.js`:
  - Fresh visit with no hash → `history.replaceState` to `#/search` (so users land in the workspace while raw `index.html` keeps marketing homepage SEO for crawlers).
  - `#/` → Homepage view; `#/search`, `#/all`, `#/icons` (with optional `?query=...`) → Grid view; `#/library/{slug}` → Single library view; `#/category/{slug}` → Category view; `#/icon/{id}` → Opens library + detail panel + injects `ImageObject` JSON-LD; `#/collections` → Grid + Collections modal; `#/privacy` / `#/legal/privacy` → Privacy view; `#/terms` / `#/legal/terms` → Terms view.
  - Deep-link editor intent query params checked on startup: `?icon=`, `?iconId=`, `?editor=`, `?openEditor=` (in either `location.search` or hash query).
- `404.html`: Dark-mode standalone page (`noindex, follow`) with inline redirect script: any `/icons/{slug}` URL strips `-icon-svg`, `-icon-png`, or `-svg-and-png-download` and redirects via `window.location.replace("/icons/" + encodeURIComponent(cleanId) + "-icon-svg/")`. Links to `/library/`, `/category/`, `/style/`, `/compare/`, `/articles/`, `/stats/`, `/`.

### 3.10 Service Worker (`sw.js`)
- Version token: `20261113-api-mcp`.
- Caches:
  - `iconstash-shell-20261113-api-mcp`: precaches `index.html`, versioned `style.css`, `icons.js`, `ui.js`, `search.js`, `search.worker.js`, `collections.js`, `app.js`, `vendor/fuse.min.js?v=20260530-preloadall`, `favicon.svg`. Cache-first for shell assets; network-first with shell fallback for navigations.
  - `iconstash-prerender-chunks-20261113-api-mcp`: stale-while-revalidate for `/data/prerender/libraries/{slug}/chunk-{n}.html`.
- Deliberately does **not** cache `data/*.json` (handled by IndexedDB to avoid ~280 MB double storage).

---

## 4. Complete Client-Side Storage & Cache Schema

**Preserve these exact keys** during migration so returning users keep their theme, collections, studio customization, and drawing drafts:

| Storage | Key / Name | Owner File(s) | Default / TTL | Exact Data Schema |
|---|---|---|---|---|
| `localStorage` | `iconvault-theme` | `app.js` | `"dark"` | `"dark" \| "light"` (main app theme key — legacy name!) |
| `localStorage` | `theme` | `about/`, `contact/`, `privacy/`, `terms/` | `"dark"` | `"dark" \| "light"` (static pages theme key — **diverges from `iconvault-theme`**; unify or dual-sync in v2) |
| `localStorage` | `iconstash-collections` | `collections.js` | `[{ id: "favorites", name: "Favorites", icons: [] }]` | `Array<{ id: string, name: string, icons: string[] }>` (`favorites` always kept at index 0) |
| `localStorage` | `iconstash-custom` | `app.js` | See defaults below | `{ gradient: { on: boolean, projection: "linear"\|"radial", angle: number, cx: number, cy: number, r: number, stops: Array<{ c: string, p: number }> }, effects: { flipH: boolean, flipV: boolean, rotation: number, blur: number, shadowOn: boolean, shadowOpacity: number, shadowBlur: number, shadowX: number, shadowY: number, noise: number, texture: "none"\|"paper"\|"concrete"\|"marble"\|"wood"\|"metal", textureOpacity: number, roundness: "soft"\|"round"\|"medium"\|"sharp" }, motion: { on: boolean, type: "draw"\|"stroke"\|"bounce"\|"shake"\|"jump", duration: number, loop: boolean, easing: "inout"\|"in"\|"out"\|"linear" } }` |
| `localStorage` | `iconstash-draw-draft` | `app.js` | `{ paths: [], color: "#C1DD2D", strokeWidth: 2 }` | `{ paths: Array<{ d: string }>, color: string, strokeWidth: number }` |
| `sessionStorage` & `localStorage` | `iconstash-open-editor`, `iconstash-editor-icon`, `openEditorIcon` | `app.js` | Consumed & removed on boot | `string` (iconId) or JSON `{ iconId?: string, id?: string }` (cross-page handoff from PSEO pages into editor) |
| `IndexedDB` | DB `IconStashDB` (v1), Store `libraries` | `app.js` | 7-day TTL (`604800000` ms) | Key `<slug>` → `Icon[]`; Key `cached-at:<slug>` → `number` (epoch ms) |
| `CacheStorage` | `iconstash-shell-20261113-api-mcp` | `sw.js` | Purged on version bump | Versioned app shell responses |
| `CacheStorage` | `iconstash-prerender-chunks-20261113-api-mcp` | `sw.js` | Purged on version bump | Prerendered HTML chunk responses |

---

## 5. Static Info Pages Inventory

| Route | CSS Approach | Theme Toggle | JSON-LD Schemas | Key Content & Notes |
|---|---|---|---|---|
| `/stats/` (`stats/index.html`) | Standalone inline `<style>`, dark-only (`#0A0A0A` / `#C1DD2D`), loads Inter + JetBrains Mono from Google Fonts | None | `Dataset` (CC BY 4.0, snapshot `2026-05-05`, updated `2026-07-19`), `BreadcrumbList`, `FAQPage` (5 Qs) | 4 KPI cards (`134,701`, `28`, `94.5%`, `5`), At-a-Glance list, License Breakdown bar + legend (Apache 2.0 `46.3%`, MIT `44.0%`, CC BY 4.0 `5.5%`, CC0 `2.8%`, ISC `1.5%` — note: MIT bar span is missing in legacy HTML bar div!), 28-library ranked table, Notable Facts, Methodology, Citation box, FAQ, Explore Further, CTA banner. |
| `/about/` (`about/index.html`) | Standalone inline `<style>` with `html[data-theme="light"]` overrides (`#FAFAFA` bg, `#6D8200` accent) | Yes (`#themeToggle`, uses `localStorage['theme']`) | `AboutPage` (`Organization`, founder `Jouni Flemming`, parent `Great Software Company`), `BreadcrumbList` | Breadcrumb, Hero, 4 stat boxes, Why We Built IconStash, Leadership & Engineering, 3 Core Principles cards, Supported Families, CTA banner. |
| `/contact/` (`contact/index.html`) | Same standalone template as `/about/` | Yes (`localStorage['theme']`) | `ContactPage` (`ContactPoint` email `contact@iconstash.io`), `BreadcrumbList` | 3 contact cards (General Inquiries `contact@iconstash.io`, GitHub `OG-Huzzi/IconStash`, Suggest a Library GitHub Issues) + Response Time info box (24–48h). |
| `/privacy/` (`privacy/index.html`) | Same standalone template as `/about/` | Yes (`localStorage['theme']`) | `WebPage`, `BreadcrumbList` | 4 `.policy-card` sections (Zero-surveillance, Client-side `localStorage`, Cloudflare CDN & Google Fonts, Contact `contact@iconstash.io`), Last Modified `August 15, 2026`. |
| `/terms/` (`terms/index.html`) | Same standalone template as `/about/` | Yes (`localStorage['theme']`) | `WebPage`, `BreadcrumbList` | 5 `.terms-card` sections (Overview, Open Source Icon Licensing, Permitted/Prohibited Use, Disclaimer, Contact `contact@iconstash.io`), Last Modified `August 15, 2026`. |
| `/api/` (`api/index.html`) | Shared `/style.css` + `.pseo-page` shell + inline `.api-*` styles | None | `WebAPI` | Free keyless static JSON API (`/api/v1/manifest.json`, `libraries.json`, `index.json`, `openapi.json`, `/data/{slug}.json`), zero-dep JS SDK (`/api/iconstash-sdk.js`), single-file MCP server (`/api/iconstash-mcp.js` with 5 tools: `search_icons`, `get_icon`, `get_svg`, `compare_concept`, `list_libraries`), contact `heybro@iconstash.io`. |

### Legacy Discrepancies to Be Aware Of in v2
1. **Theme storage key split**: Main SPA reads/writes `localStorage["iconvault-theme"]`, whereas `/about/`, `/contact/`, `/privacy/`, `/terms/` read/write `localStorage["theme"]`, and `/stats/`, `/api/`, `404.html` have no theme toggle. v2 should read both keys on boot (preferring `iconvault-theme` or syncing both) for seamless migration.
2. **Contact email split**: `index.html` footer and `/api/` list `heybro@iconstash.io`, while `/contact/`, `/privacy/`, `/terms/` list `contact@iconstash.io`.
3. **Animation count**: There are **5** animations (`draw`, `stroke`, `bounce`, `shake`, `jump`) plus `off` in `index.html` and `icons.js`.
4. **Stats license bar bug**: In `stats/index.html` lines 229–234, the MIT `44.0%` (`#5AA9E6`) `<span>` is missing from `.license-bar` even though it is present in `.license-legend`.
5. **ZIP PNG sizes**: Detail panel ZIP exports `[16, 32, 64, 128, 256, 512]` (6 sizes, skipping 48), while Collection PNG ZIP exports all 7 `[16, 32, 48, 64, 128, 256, 512]`.
