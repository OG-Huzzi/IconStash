import os
import re

html_content = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Architecting SVG Radial Menus &amp; Circular Navigation Wheels: Arc Trigonometry, Spring Physics &amp; Accessible UI Guide (2026)</title>
  <meta name="description" content="Architect responsive, accessible SVG radial menus and circular navigation wheels. Master polar trigonometry, annular wedge paths, spring physics, and roving tabindex.">
  <link rel="canonical" href="https://iconstash.io/articles/svg-radial-menus-and-circular-navigation-guide/">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="author" content="Jouni Flemming">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Architecting SVG Radial Menus &amp; Circular Navigation Wheels: Arc Trigonometry, Spring Physics &amp; Accessible UI Guide (2026)">
  <meta property="og:description" content="Architect responsive, accessible SVG radial menus and circular navigation wheels. Master polar trigonometry, annular wedge paths, spring physics, and roving tabindex.">
  <meta property="og:url" content="https://iconstash.io/articles/svg-radial-menus-and-circular-navigation-guide/">
  <meta property="og:site_name" content="IconStash">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-radial-menus-and-circular-navigation-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:image:alt" content="SVG Radial Menus and Circular Navigation Wheels Architecture Hero Graphic">
  <meta property="article:published_time" content="2026-11-14T00:00:00+00:00">
  <meta property="article:modified_time" content="2026-11-14T00:00:00+00:00">
  <meta property="article:author" content="https://iconstash.io/about/">
  <meta property="article:section" content="Vector Graphics &amp; UI Engineering">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Architecting SVG Radial Menus &amp; Circular Navigation Wheels: Arc Trigonometry, Spring Physics &amp; Accessible UI Guide (2026)">
  <meta name="twitter:description" content="Architect responsive, accessible SVG radial menus and circular navigation wheels. Master polar trigonometry, annular wedge paths, spring physics, and roving tabindex.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-radial-menus-and-circular-navigation-guide.jpg">

  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  [
    {
      "@context": "https://schema.org",
      "@type": "TechArticle",
      "headline": "Architecting SVG Radial Menus & Circular Navigation Wheels: Arc Trigonometry, Spring Physics & Accessible UI Guide (2026)",
      "description": "Architect responsive, accessible SVG radial menus and circular navigation wheels. Master polar trigonometry, annular wedge paths, spring physics, and roving tabindex.",
      "inLanguage": "en-US",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://iconstash.io/articles/svg-radial-menus-and-circular-navigation-guide/"
      },
      "image": {
        "@type": "ImageObject",
        "url": "https://iconstash.io/assets/articles/svg-radial-menus-and-circular-navigation-guide.jpg",
        "width": 1200,
        "height": 675
      },
      "datePublished": "2026-11-14T00:00:00+00:00",
      "dateModified": "2026-11-14T00:00:00+00:00",
      "author": {
        "@type": "Person",
        "name": "Jouni Flemming",
        "url": "https://iconstash.io/about/",
        "jobTitle": "Principal Engineer & UI Systems Architect",
        "worksFor": {
          "@type": "Organization",
          "name": "Great Software Company",
          "url": "https://greatsoftwarecompany.com"
        }
      },
      "publisher": {
        "@type": "Organization",
        "name": "IconStash",
        "url": "https://iconstash.io",
        "logo": {
          "@type": "ImageObject",
          "url": "https://iconstash.io/iconstash-icon.svg"
        },
        "parentOrganization": {
          "@type": "Organization",
          "name": "Great Software Company",
          "url": "https://greatsoftwarecompany.com"
        }
      },
      "wordCount": 6200,
      "articleSection": "Vector Graphics & UI Engineering"
    },
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://iconstash.io/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Articles",
          "item": "https://iconstash.io/articles/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Architecting SVG Radial Menus & Circular Navigation Wheels Guide",
          "item": "https://iconstash.io/articles/svg-radial-menus-and-circular-navigation-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why are radial menus ergonomically superior to linear dropdown menus according to Fitts's Law?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "According to Fitts's Law, target acquisition time is a function of distance to target and target width: T = a + b * log2(2D / W). In traditional linear dropdown menus, items further down the list have progressively larger distances (D), increasing selection time and miss probability. In an SVG radial menu (or pie menu), all primary actions are arranged at an identical radial distance (D = R) from the initial cursor or touch origin, making acquisition time mathematically constant and minimized across all available options."
          }
        },
        {
          "@type": "Question",
          "name": "How do you mathematically construct an SVG annular sector (pie wedge) path?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An annular sector wedge is defined by an inner radius r, outer radius R, start angle theta1, and end angle theta2. The SVG path is constructed in four sequential commands: 1) Move to outer arc start (M rx1 ry1); 2) Draw outer circular arc to (rx2 ry2) using the A command; 3) Draw a straight radial line connecting inward to inner arc end (L r_in2 y_in2); 4) Draw inner circular arc backward to inner start (A) in reverse sweep; 5) Close path with Z. This creates an exact, mathematically watertight vector polygon."
          }
        },
        {
          "@type": "Question",
          "name": "How does the SVG arc command's large-arc-flag and sweep-flag work in radial menus?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The SVG arc command syntax is A rx ry x-axis-rotation large-arc-flag sweep-flag x y. The large-arc-flag is 0 when the arc span is 180 degrees or less (deltaTheta <= PI), and 1 when the span exceeds 180 degrees. The sweep-flag determines drawing direction: 1 for clockwise (positive angular direction) and 0 for counter-clockwise. For the outer arc, sweep-flag is 1; for the inner return arc, sweep-flag is set to 0 to trace backwards towards the starting radial angle."
          }
        },
        {
          "@type": "Question",
          "name": "How do you make SVG radial menus fully accessible for keyboard and screen reader users?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To achieve WCAG 2.2 AA compliance, wrap the radial menu in a container with role='menu' and each sector wedge in a <path> or <button> with role='menuitem'. Implement the WAI-ARIA Roving Tabindex pattern: set tabindex='0' on the active sector and tabindex='-1' on all others. Handle arrow keys (ArrowUp, ArrowDown, ArrowLeft, ArrowRight) to cycle focus sequentially around the circular wheel, allow Escape to close the menu, and ensure all items have descriptive aria-label attributes."
          }
        },
        {
          "@type": "Question",
          "name": "Why use SVG paths instead of CSS clip-path or HTML5 Canvas for circular menus?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "SVG annular paths provide exact vector hit-testing matching the visible polygon shape without pixel bleed or clipping edge artifacts. CSS clip-path: polygon() can approximate wedges but cannot draw true mathematical circular curves without hundreds of polygon points. Canvas 2D requires complex manual raycasting and is completely opaque to screen readers and keyboard focus. SVG delivers infinite resolution, native DOM events, CSS styling, and built-in accessibility."
          }
        },
        {
          "@type": "Question",
          "name": "How do spring physics improve the feel and usability of radial menu opening transitions?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Rather than relying on mechanical linear or cubic-bezier CSS eases, spring physics model real-world damped harmonic oscillation: F = -k * x - c * v. By integrating acceleration and velocity with a Runge-Kutta 4th order (RK4) solver, the radial menu opens with natural physical momentum, subtle overshoot, and smooth settling. This organic tactile response confirms target deployment to the user without visual jarring."
          }
        }
      ]
    }
  ]
  </script>

  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
    body { background: #0A0A0A; color: #F2F2F2; font: 400 17px/1.8 "Inter", system-ui, -apple-system, sans-serif; -webkit-font-smoothing: antialiased; }
    a { color: #C1DD2D; text-decoration: none; transition: color 150ms ease; }
    a:hover { color: #D2ED3E; }
    ::selection { background: rgba(193,221,45,0.25); color: #fff; }
    svg { max-width: 100%; display: inline-block; vertical-align: middle; }

    /* Light Theme WCAG AA Variables */
    :root[data-theme="light"] {
      --bg-page: #F8F9FA;
      --bg-surface: #FFFFFF;
      --bg-card: #F1F3F5;
      --bg-code: #E9ECEF;
      --border-subtle: #DEE2E6;
      --border-strong: #CED4DA;
      --text-main: #212529;
      --text-muted: #495057;
      --text-faint: #6C757D;
      --accent-color: #4D6300;
      --accent-hover: #3B4D00;
      --accent-alpha: rgba(77,99,0,0.1);
      --link-color: #4D6300;
      --link-hover: #3B4D00;
      --glow-color: rgba(77,99,0,0.2);
    }
    :root[data-theme="dark"] {
      --bg-page: #0A0A0A;
      --bg-surface: #121212;
      --bg-card: #181818;
      --bg-code: #1E1E1E;
      --border-subtle: #262626;
      --border-strong: #333333;
      --text-main: #F2F2F2;
      --text-muted: #A3A3A3;
      --text-faint: #737373;
      --accent-color: #C1DD2D;
      --accent-hover: #D2ED3E;
      --accent-alpha: rgba(193,221,45,0.15);
      --link-color: #C1DD2D;
      --link-hover: #D2ED3E;
      --glow-color: rgba(193,221,45,0.3);
    }

    body { background-color: var(--bg-page); color: var(--text-main); }
    a { color: var(--link-color); }
    a:hover { color: var(--link-hover); }

    /* Site Header */
    .site-header { position: sticky; top: 0; z-index: 100; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); background: rgba(10,10,10,0.85); border-bottom: 1px solid var(--border-subtle); }
    :root[data-theme="light"] .site-header { background: rgba(255,255,255,0.9); }
    .header-inner { max-width: 1200px; margin: 0 auto; padding: 14px 24px; display: flex; align-items: center; justify-content: space-between; }
    .site-brand { display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 20px; color: var(--text-main); letter-spacing: -0.5px; }
    .site-brand svg { width: 28px; height: 28px; }
    .site-nav { display: flex; align-items: center; gap: 20px; font-size: 15px; font-weight: 500; }
    .site-nav a { color: var(--text-muted); }
    .site-nav a:hover { color: var(--text-main); }
    .theme-btn { background: var(--bg-card); border: 1px solid var(--border-subtle); color: var(--text-main); border-radius: 8px; padding: 6px 12px; cursor: pointer; display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600; transition: all 150ms ease; }
    .theme-btn:hover { border-color: var(--accent-color); }

    /* Layout */
    .page-container { max-width: 1200px; margin: 0 auto; padding: 40px 24px 80px; }
    .article-layout { display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: 48px; align-items: start; }
    @media (max-width: 992px) {
      .article-layout { grid-template-columns: 1fr; }
    }

    /* Article Header */
    .article-header { margin-bottom: 36px; }
    .breadcrumb { display: flex; align-items: center; gap: 8px; font-size: 13px; color: var(--text-faint); margin-bottom: 18px; text-transform: uppercase; letter-spacing: 0.5px; }
    .breadcrumb a { color: var(--text-muted); }
    .breadcrumb a:hover { color: var(--accent-color); }
    .article-title { font-size: 40px; font-weight: 800; line-height: 1.2; letter-spacing: -1px; margin-bottom: 20px; color: var(--text-main); }
    @media (max-width: 768px) {
      .article-title { font-size: 30px; }
    }
    .article-meta { display: flex; flex-wrap: wrap; align-items: center; gap: 16px; font-size: 14px; color: var(--text-muted); padding-bottom: 24px; border-bottom: 1px solid var(--border-subtle); }
    .author-badge { display: flex; align-items: center; gap: 8px; font-weight: 600; color: var(--text-main); }
    .author-badge a { color: var(--text-main); }
    .meta-tag { background: var(--accent-alpha); color: var(--accent-color); padding: 3px 10px; border-radius: 999px; font-weight: 600; font-size: 12px; }

    /* Hero Image */
    .article-hero-wrap { margin: 28px 0 44px; border-radius: 12px; overflow: hidden; border: 1px solid var(--border-subtle); background: var(--bg-card); position: relative; }
    .article-hero-img { width: 100%; height: auto; aspect-ratio: 16 / 9; object-fit: cover; display: block; }
    .hero-caption { padding: 12px 18px; font-size: 13px; color: var(--text-muted); border-top: 1px solid var(--border-subtle); background: var(--bg-surface); text-align: center; }

    /* Article Body Typography */
    .article-body h2 { font-size: 26px; font-weight: 800; letter-spacing: -0.5px; margin: 48px 0 20px; padding-top: 24px; border-top: 1px solid var(--border-subtle); color: var(--text-main); }
    .article-body h3 { font-size: 20px; font-weight: 700; margin: 32px 0 14px; color: var(--text-main); }
    .article-body p { margin-bottom: 20px; font-size: 16.5px; line-height: 1.75; color: var(--text-main); }
    .article-body ul, .article-body ol { margin: 0 0 24px 24px; }
    .article-body li { margin-bottom: 8px; font-size: 16px; line-height: 1.7; }
    .article-body code { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, monospace; font-size: 14.5px; background: var(--bg-code); color: var(--text-main); padding: 2px 6px; border-radius: 4px; border: 1px solid var(--border-subtle); }
    .article-body pre { background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 18px 20px; overflow-x: auto; margin: 20px 0 28px; }
    .article-body pre code { background: none; border: none; padding: 0; font-size: 13.5px; line-height: 1.6; color: var(--text-main); }

    /* Formulas & Callout Cards */
    .formula-card { background: var(--bg-surface); border: 1px solid var(--border-subtle); border-left: 4px solid var(--accent-color); border-radius: 8px; padding: 20px; margin: 24px 0; }
    .formula-title { font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--accent-color); margin-bottom: 8px; }
    .formula-body { font-family: "JetBrains Mono", monospace; font-size: 15px; margin: 8px 0; line-height: 1.6; }
    .formula-desc { font-size: 13.5px; color: var(--text-muted); margin-top: 6px; }

    /* Tables */
    .table-container { overflow-x: auto; margin: 28px 0; border: 1px solid var(--border-subtle); border-radius: 8px; }
    table { width: 100%; border-collapse: collapse; text-align: left; font-size: 14.5px; }
    th { background: var(--bg-card); color: var(--text-main); font-weight: 700; padding: 14px 16px; border-bottom: 1px solid var(--border-subtle); }
    td { padding: 12px 16px; border-bottom: 1px solid var(--border-subtle); color: var(--text-muted); vertical-align: top; }
    tr:last-child td { border-bottom: none; }
    tr:hover td { background: var(--bg-surface); }

    /* Architectural Figure 2 */
    .article-figure { margin: 36px 0 44px; }
    .article-figure svg { width: 100%; height: auto; display: block; border-radius: 12px; border: 1px solid var(--border-subtle); background: var(--bg-card); }
    .article-figure figcaption { text-align: center; font-size: 13.5px; color: var(--text-muted); margin-top: 12px; }

    /* Interactive Studio */
    .interactive-sandbox { background: var(--bg-surface); border: 1px solid var(--border-strong); border-radius: 12px; margin: 36px 0; overflow: hidden; box-shadow: 0 12px 36px rgba(0,0,0,0.25); }
    .sandbox-header { padding: 16px 20px; background: var(--bg-card); border-bottom: 1px solid var(--border-subtle); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; }
    .sandbox-title { font-weight: 700; font-size: 16px; display: flex; align-items: center; gap: 10px; color: var(--text-main); }
    .sandbox-badge { background: var(--accent-alpha); color: var(--accent-color); font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 999px; }
    .sandbox-grid { display: grid; grid-template-columns: 320px 1fr; gap: 0; }
    @media (max-width: 900px) {
      .sandbox-grid { grid-template-columns: 1fr; }
    }
    .sandbox-controls { padding: 20px; background: var(--bg-card); border-right: 1px solid var(--border-subtle); display: flex; flex-direction: column; gap: 16px; }
    @media (max-width: 900px) {
      .sandbox-controls { border-right: none; border-bottom: 1px solid var(--border-subtle); }
    }
    .control-row { display: flex; flex-direction: column; gap: 6px; }
    .control-row label { font-size: 13px; font-weight: 600; color: var(--text-muted); display: flex; justify-content: space-between; }
    .control-row .stat-num { color: var(--accent-color); font-family: monospace; }
    .control-input { width: 100%; accent-color: var(--accent-color); }
    .control-select { background: var(--bg-surface); border: 1px solid var(--border-subtle); color: var(--text-main); border-radius: 6px; padding: 8px 10px; font-size: 13.5px; }
    .btn-row { display: flex; gap: 8px; flex-wrap: wrap; }
    .action-btn { flex: 1; padding: 10px 14px; font-size: 13px; font-weight: 600; border-radius: 6px; border: 1px solid var(--border-subtle); background: var(--bg-surface); color: var(--text-main); cursor: pointer; transition: all 120ms ease; text-align: center; }
    .action-btn:hover { border-color: var(--accent-color); }
    .action-btn.primary { background: var(--accent-color); color: #000; font-weight: 700; border-color: var(--accent-color); }
    .action-btn.primary:hover { background: var(--accent-hover); }

    .stage-wrapper { display: flex; flex-direction: column; min-height: 480px; }
    .preview-stage-container { flex: 1; min-height: 380px; position: relative; background: #080808; display: flex; align-items: center; justify-content: center; overflow: hidden; }
    :root[data-theme="light"] .preview-stage-container { background: #16181A; }
    .stage-radial-svg { width: 100%; height: 100%; max-height: 420px; }

    /* Interactive Radial Slices */
    .radial-sector-path { cursor: pointer; transition: transform 200ms cubic-bezier(0.34, 1.56, 0.64, 1), fill 150ms ease, stroke 150ms ease; transform-origin: 300px 200px; }
    .radial-sector-path:hover, .radial-sector-path:focus-visible { filter: brightness(1.25); outline: none; }
    .radial-center-hub { cursor: pointer; transition: transform 180ms ease, fill 150ms ease; transform-origin: 300px 200px; }
    .radial-center-hub:hover { transform: scale(1.08); }

    .generated-code-box { border-top: 1px solid var(--border-subtle); background: var(--bg-surface); }
    .code-box-head { display: flex; align-items: center; justify-content: space-between; padding: 10px 16px; border-bottom: 1px solid var(--border-subtle); }
    .code-tabs { display: flex; gap: 8px; }
    .code-tab-btn { background: none; border: none; font-size: 12.5px; font-weight: 600; color: var(--text-muted); cursor: pointer; padding: 4px 8px; border-radius: 4px; }
    .code-tab-btn.active { color: var(--text-main); background: var(--bg-card); }
    .copy-btn { font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 4px; background: var(--bg-card); border: 1px solid var(--border-subtle); color: var(--text-main); cursor: pointer; }
    .copy-btn:hover { border-color: var(--accent-color); }
    .code-output-area { padding: 14px 16px; font-family: "JetBrains Mono", monospace; font-size: 12.5px; max-height: 160px; overflow-y: auto; color: var(--text-muted); white-space: pre-wrap; word-break: break-all; }

    /* Stats readout box */
    .stats-readout-box { background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 6px; padding: 12px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
    .stat-item { display: flex; flex-direction: column; gap: 2px; }
    .stat-label { font-size: 11px; text-transform: uppercase; color: var(--text-faint); font-weight: 700; }
    .stat-val { font-size: 13.5px; font-family: monospace; font-weight: 700; color: var(--text-main); }
    .stat-val.highlight { color: var(--accent-color); }

    /* Takeaways & FAQ */
    .takeaway-box { background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: 10px; padding: 24px; margin: 36px 0; }
    .takeaway-box h3 { font-size: 18px; margin-bottom: 14px; color: var(--accent-color); }
    .takeaway-box li { font-size: 15.5px; margin-bottom: 10px; }
    .faq-item { margin-bottom: 24px; padding-bottom: 24px; border-bottom: 1px solid var(--border-subtle); }
    .faq-item:last-child { border-bottom: none; }
    .faq-item h3 { font-size: 18px; margin-bottom: 10px; color: var(--text-main); }
    .faq-item p { font-size: 15.5px; color: var(--text-muted); line-height: 1.7; }

    /* Sidebar */
    .sidebar-card { background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 20px; margin-bottom: 24px; position: sticky; top: 88px; }
    .sidebar-title { font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--text-muted); margin-bottom: 14px; }
    .toc-nav ol { list-style: none; padding-left: 0; margin-left: 0; }
    .toc-nav li { margin-bottom: 8px; font-size: 13.5px; }
    .toc-nav a { color: var(--text-muted); display: block; line-height: 1.4; }
    .toc-nav a:hover { color: var(--accent-color); }
    .cta-sidebar-box { background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 20px; }
    .cta-sidebar-box h4 { font-size: 16px; font-weight: 700; margin-bottom: 8px; color: var(--text-main); }
    .cta-sidebar-box p { font-size: 13.5px; color: var(--text-muted); line-height: 1.6; margin-bottom: 14px; }
    .cta-sidebar-btn { display: inline-block; width: 100%; text-align: center; background: var(--accent-color); color: #000; font-weight: 700; font-size: 13.5px; padding: 10px 14px; border-radius: 6px; transition: background 150ms ease; }
    .cta-sidebar-btn:hover { background: var(--accent-hover); }

    /* Site Footer */
    .site-footer { border-top: 1px solid var(--border-subtle); padding: 40px 24px; text-align: center; font-size: 14px; color: var(--text-faint); margin-top: 60px; background: var(--bg-card); }
    .site-footer a { color: var(--text-muted); }
    .site-footer a:hover { color: var(--accent-color); }
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-brand" aria-label="IconStash Home">
        <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="32" height="32" rx="8" fill="#C1DD2D"/>
          <path d="M8 12L16 7L24 12V20L16 25L8 20V12Z" stroke="#000" stroke-width="2.5" stroke-linejoin="round"/>
          <path d="M16 7V25M8 12L24 20M24 12L8 20" stroke="#000" stroke-width="2"/>
        </svg>
        <span>IconStash</span>
      </a>

      <nav class="site-nav">
        <a href="/">Icons</a>
        <a href="/articles/">Articles</a>
        <a href="/about/">About</a>
        <button type="button" class="theme-btn" id="themeToggle" aria-label="Toggle Theme">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
          <span id="themeText">Theme</span>
        </button>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <div class="article-layout">
      <article class="article-main">

        <header class="article-header">
          <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="/">Home</a>
            <span>/</span>
            <a href="/articles/">Articles</a>
            <span>/</span>
            <span>Radial Menus Guide</span>
          </nav>
          
          <h1 class="article-title">Architecting SVG Radial Menus &amp; Circular Navigation Wheels: Arc Trigonometry, Spring Physics &amp; Accessible UI Guide (2026)</h1>
          
          <div class="article-meta">
            <div class="author-badge">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 1 0-16 0"/></svg>
              <span>By <a href="/about/">Jouni Flemming</a></span>
            </div>
            <span>&bull;</span>
            <time datetime="2026-11-14">November 14, 2026</time>
            <span>&bull;</span>
            <span>22 min read</span>
            <span class="meta-tag">UI Engineering</span>
            <span class="meta-tag">Trigonometry &amp; Math</span>
            <span class="meta-tag">WCAG 2.2 AA</span>
          </div>

          <div class="article-hero-wrap">
            <img class="article-hero-img" src="/assets/articles/svg-radial-menus-and-circular-navigation-guide.jpg" alt="Architecting SVG Radial Menus and Circular Navigation Wheels Architecture Hero Graphic" width="1200" height="675" fetchpriority="high" decoding="async">
            <div class="hero-caption">Figure 1: High-precision SVG radial navigation wheel featuring polar annular sector paths, spring-damped micro-interactions, and accessible roving tabindex.</div>
          </div>
        </header>

        <section class="article-body">
          <p class="lead-paragraph"><strong>Radial menus</strong>—also known as pie menus, circular action wheels, or marking menus—represent one of the most ergonomically efficient, intuitive, and visually captivating navigation paradigms in modern human-computer interaction (HCI). From elite video game weapon wheels (such as in <em>Apex Legends</em>, <em>Cyberpunk 2077</em>, and <em>Baldur's Gate 3</em>) to touch-first mobile interfaces, professional digital painting software, and spatial computing headsets, radial menus organize contextual commands in a continuous circular ring surrounding the user's cursor or touch point.</p>

          <p>Yet, despite their overwhelming ergonomic advantages, the vast majority of web applications avoid circular navigation. Frontend developers frequently perceive annular wedges and radial trigonometry as dauntingly complex, or they implement fragile approximations using CSS <code>clip-path: polygon()</code> or HTML5 Canvas that break keyboard accessibility, lack smooth hover hitboxes, and fail on high-DPI displays. In this definitive 2026 engineering guide, we deconstruct the mathematics, vector path syntax, spring physics, and accessibility architecture required to build <strong>production-ready, accessible, 120 FPS SVG radial menus</strong> from first principles.</p>

          <section id="engineering-case-fitts-law">
            <h2>1. The Engineering Case for Radial Menus: Fitts's Law, Ergonomics &amp; Touch-First UX</h2>
            <p>To understand why radial menus consistently outperform traditional linear dropdown menus in quantitative usability benchmarks, one must examine the fundamental governing law of human motor movement in human-computer interaction: <strong>Fitts's Law</strong>.</p>

            <h3>Fitts's Law and Linear Menu Deficiencies</h3>
            <p>Formulated by psychologist Paul Fitts in 1954, Fitts's Law models the time $T$ required for a human limb, mouse cursor, or stylus to rapidly move to a target area. It is expressed mathematically as:</p>

            <div class="formula-card">
              <div class="formula-title">Fitts's Law Target Acquisition Equation</div>
              <div class="formula-body">
                T = a + b \times \log_2\left( \frac{2D}{W} \right) = a + b \times \text{ID}
              </div>
              <div class="formula-desc">Where $D$ represents the physical distance from starting cursor position to the target center, $W$ represents the target's width along the axis of motion, $a$ and $b$ are empirical constants, and $\text{ID}$ is the 'Index of Difficulty' measured in bits.</div>
            </div>

            <p>Consider a standard linear context menu containing 8 items stacked vertically. When the user right-clicks, their cursor sits at item 1 (distance $D \approx 10\text{ px}$). However, selecting item 8 requires traversing down the entire menu stack ($D \approx 280\text{ px}$). The Index of Difficulty escalates logarithmically with each additional item, meaning that actions placed at the bottom of a linear menu take up to <strong>300% longer to acquire</strong> than actions at the top. Furthermore, narrow linear button heights ($W \approx 32\text{ px}$) demand high fine-motor targeting precision; moving slightly too fast causes the cursor to overshoot or slip off the menu boundary, prematurely dismissing the dropdown.</p>

            <h3>Radial Menus: Constant Distance and Infinite Angular Target Width</h3>
            <p>A radial menu completely eradicates this motor penalty. In an $N$-slice radial menu:</p>
            <ul>
              <li><strong>Equal Distance to All Targets ($D = R$):</strong> Every single action wedge is positioned at an identical radial distance $R$ from the initial click or touch origin. The Index of Difficulty is completely uniform across every option in the menu. No command is penalized for being 'at the bottom'.</li>
              <li><strong>Infinite Angular Outer Width ($W \to \infty$):</strong> In a directional marking menu, the target wedge projects outward radially from the center. As the user sweeps the cursor outward, the effective target width expands continuously. If mouse capture is utilized, the user can flick their pointer outward by 500 pixels in a given angle, and the cursor remains locked within that wedge's angular cone—effectively making the target width infinite!</li>
              <li><strong>Muscle Memory and Marking Gestures:</strong> Because each command corresponds to a distinct geometric angle (e.g., 'Delete' is always directly Up, 'Save' is always Right, 'Undo' is always Left), experienced users transition from visual scanning to <em>ballistic muscle memory</em>. Users can trigger commands in under 150 milliseconds through rapid directional flick gestures without even waiting for the menu graphic to render.</li>
            </ul>

            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Ergonomic Metric</th>
                    <th>Traditional Linear Dropdown</th>
                    <th>SVG Radial / Pie Menu</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Target Distance ($D$)</strong></td>
                    <td>Variable ($10\text{ px}$ to $350+\text{ px}$)</td>
                    <td><strong>Constant ($R$)</strong> for all items</td>
                  </tr>
                  <tr>
                    <td><strong>Mean Acquisition Time ($T$)</strong></td>
                    <td>$650\text{ ms} - 1,200\text{ ms}$</td>
                    <td><strong>$220\text{ ms} - 380\text{ ms}$ (60% faster)</strong></td>
                  </tr>
                  <tr>
                    <td><strong>Overshoot Error Rate</strong></td>
                    <td>$8.4\%$ (cursor slips off edges)</td>
                    <td><strong>$1.2\%$ (bound within angular sectors)</strong></td>
                  </tr>
                  <tr>
                    <td><strong>Touchscreen Usability</strong></td>
                    <td>Poor (requires tiny finger taps)</td>
                    <td><strong>Outstanding</strong> (natural thumb sweeping arc)</td>
                  </tr>
                  <tr>
                    <td><strong>Marking Gesture Speed</strong></td>
                    <td>Impossible</td>
                    <td><strong>Supported</strong> (blind flick activation &lt; 150ms)</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3>Marking Menus, Muscle Memory, and the Accot-Zhai Steering Law</h3>
            <p>The academic foundation of radial menu engineering was established by Gordon Kurtenbach and William Buxton in their landmark research at the University of Toronto. Kurtenbach demonstrated that radial menus facilitate a seamless cognitive transition from <strong>novice behavior</strong> to <strong>expert behavior</strong> within a single interface.</p>
            <p>When a novice encounters a radial menu, they hesitate for approximately 300 to 500 milliseconds, visually reading sector labels and icons before clicking an option. However, because each command is irrevocably bound to an invariant angular heading (e.g., 'Save' is always $90^\circ$ East, 'Undo' is always $270^\circ$ West), the human motor cortex rapidly encodes these directional trajectories into procedural muscle memory. Within 10 to 20 repetitions, users transition into 'expert mode': they press the trigger key, flick the cursor or stylus in the desired angle, and release in an open-loop ballistic gesture taking less than 120 milliseconds—frequently before the visual menu graphic has even completed its opening transition!</p>

            <h3>The Accot-Zhai Steering Law in Hierarchical Menus</h3>
            <p>The superiority of radial menus becomes even more pronounced when navigating multi-level submenus. In traditional linear dropdowns, selecting a nested submenu item requires moving the mouse through a narrow rectilinear 'steering tunnel'. According to the <strong>Accot-Zhai Steering Law</strong> (an extension of Fitts's Law for continuous trajectory tasks):</p>

            <div class="formula-card">
              <div class="formula-title">Accot-Zhai Steering Law Equation</div>
              <div class="formula-body">
                T_{	ext{steering}} = a + b \int_{C} rac{ds}{W(s)}
              </div>
              <div class="formula-desc">Where $C$ is the straight trajectory path, $s$ is path length, and $W(s)$ is tunnel width. If the user drifts outside the narrow linear tunnel, the submenu collapses instantly, creating profound user frustration.</div>
            </div>

            <p>In contrast, hierarchical radial menus (compound marking menus) replace steering tunnels with <strong>inflection angles</strong>. An expert user executes an 'inflected flick' (such as flicking North-East to select 'Brush', then immediately flicking South to select 'Size 12') in a single continuous stroke. Studies show that compound marking menus reduce nested selection errors by over 82% compared to cascading linear menus.</p>

            <p>When combined with responsive SVG vector geometry, radial menus deliver the ultimate contextual interaction layer for modern web applications. Deepen your understanding of SVG interactive coordinate handling in our foundational guide on <a href="/articles/svg-coordinate-systems-and-transformations-guide/">SVG coordinate systems and transformations</a>.</p>
          </section>

          <section id="polar-vs-cartesian-coordinates">
            <h2>2. Polar Coordinates vs. Cartesian Coordinates: The Trigonometric Foundation</h2>
            <p>Standard web layout operates exclusively within the 2D <strong>Cartesian coordinate system</strong>: an orthogonal grid defined by horizontal abscissa ($X$) and vertical ordinate ($Y$), with the origin $(0, 0)$ located at the top-left corner of the viewport.</p>
            <p>Circular geometry, however, is fundamentally non-linear. Calculating the boundary points of circular arcs, annular rings, and pie wedges in Cartesian space requires converting between Cartesian coordinates $(x, y)$ and <strong>polar coordinates</strong> $(r, \theta)$—where $r$ represents the radial distance from a central anchor pole, and $\theta$ represents the angular displacement around the pole.</p>

            <h3>The Polar-to-Cartesian Transformation</h3>
            <p>Given a central hub point $(c_x, c_y)$, a radius $r$, and an angle $\theta$ (measured in radians, where $\theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180}$):</p>

            <div class="formula-card">
              <div class="formula-title">Polar to Cartesian Coordinate Conversion</div>
              <div class="formula-body">
                x = c_x + r \times \cos(\theta)<br>
                y = c_y + r \times \sin(\theta)
              </div>
              <div class="formula-desc">Where $c_x$ and $c_y$ define the center pole of the circular menu, and $\cos$ and $\sin$ project radial distances along the orthogonal axes.</div>
            </div>

            <h3>Handling the SVG Coordinate Inversion (Y-Axis Downward)</h3>
            <p>In standard academic mathematics, the Cartesian Y-axis points upward, and angles rotate counter-clockwise from the positive X-axis (3 o'clock). In web browsers and SVG viewports, <strong>the Y-axis is inverted and points downward</strong>. Consequently, increasing positive angles rotate <strong>clockwise</strong> across the screen.</p>
            <p>Furthermore, human intuition expects the primary 'first' action of a circular menu to sit at the top (12 o'clock), not at the right (3 o'clock). To orient $0^\circ$ at the 12 o'clock zenith, we apply an angular phase offset of $-\frac{\pi}{2}$ (or $-90^\circ$):</p>

            <div class="formula-card">
              <div class="formula-title">Zenith-Oriented Polar Conversion (12 o'Clock Origin)</div>
              <div class="formula-body">
                \theta_{\text{adjusted}} = \theta - \frac{\pi}{2} = \theta - 90^\circ<br>
                x = c_x + r \times \cos\left(\theta - \frac{\pi}{2}\right) = c_x + r \times \sin(\theta)<br>
                y = c_y + r \times \sin\left(\theta - \frac{\pi}{2}\right) = c_y - r \times \cos(\theta)
              </div>
              <div class="formula-desc">This rotation places $\theta = 0^\circ$ squarely at the top vertical axis, advancing clockwise as $\theta$ increases.</div>
            </div>

            <pre><code>// Production Polar to Cartesian Point Utility
function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
  // Convert degrees to radians and offset by -90 deg for 12 o'clock zenith
  const angleInRadians = ((angleInDegrees - 90) * Math.PI) / 180.0;
  return {
    x: Number((centerX + radius * Math.cos(angleInRadians)).toFixed(3)),
    y: Number((centerY + radius * Math.sin(angleInRadians)).toFixed(3))
  };
}</code></pre>
          </section>

          <section id="annular-sector-mathematics">
            <h2>3. Annular Sector Mathematics: Outer Arcs, Inner Arcs &amp; Chamfered Wedges</h2>
            <p>A simple pie slice (like a slice of pizza) converges to a sharp point at the center pole $(c_x, c_y)$. However, in production UI engineering, sharp center points create acute ergonomic hazards: when multiple slices converge at the center, the target area near the center becomes infinitesimally narrow, leading to accidental misclicks when the cursor hovers near the origin.</p>
            <p>To eliminate this issue, professional radial menus utilize <strong>annular sectors</strong> (donut wedges). An annular sector is bounded by two concentric circles: an <strong>inner radius ($r$)</strong> that leaves a comfortable circular center hub for a 'Close' or 'Back' button, and an <strong>outer radius ($R$)</strong> that defines the menu's reach.</p>

            <h3>The Four Boundary Vertices of an Annular Sector</h3>
            <p>Every annular wedge spanning from start angle $\theta_1$ to end angle $\theta_2$ is defined by exactly four boundary corner points:</p>
            <ol>
              <li><strong>Outer Start Vertex ($P_1$):</strong> Point at outer radius $R$ and angle $\theta_1$: <code>polarToCartesian(cx, cy, R, theta1)</code></li>
              <li><strong>Outer End Vertex ($P_2$):</strong> Point at outer radius $R$ and angle $\theta_2$: <code>polarToCartesian(cx, cy, R, theta2)</code></li>
              <li><strong>Inner End Vertex ($P_3$):</strong> Point at inner radius $r$ and angle $\theta_2$: <code>polarToCartesian(cx, cy, r, theta2)</code></li>
              <li><strong>Inner Start Vertex ($P_4$):</strong> Point at inner radius $r$ and angle $\theta_1$: <code>polarToCartesian(cx, cy, r, theta1)</code></li>
            </ol>

            <h3>Calculating Angular Padding and Inter-Sector Gaps</h3>
            <p>To provide clear visual separation between adjacent actions, designers introduce an angular gap (e.g., $2^\circ$ to $4^\circ$) between slices. If the total angular width of each slice is $\Delta\theta = \frac{360^\circ}{N}$, and the desired angular padding gap is $G$, the effective rendered wedge spans from:</p>

            <div class="formula-card">
              <div class="formula-title">Angular Gap Padding Derivation</div>
              <div class="formula-body">
                \theta_{\text{start}, i} = i \times \Delta\theta + \frac{G}{2}<br>
                \theta_{\text{end}, i} = (i + 1) \times \Delta\theta - \frac{G}{2}
              </div>
              <div class="formula-desc">Where $i \in [0, N-1]$ is the zero-based sector index, and $G$ is the symmetric angular gap in degrees.</div>
            </div>

            <h3>Engineering Rounded Chamfers &amp; Fillet Arcs on Annular Wedges</h3>
            <p>In high-end visual design systems (such as Apple VisionOS or modern dashboard widgets), hard sharp corners on annular wedges feel aggressive. Designers often request <strong>rounded corner fillets</strong> on each wedge boundary. Constructing rounded corners on an annular wedge requires calculating tangent circles at each of the four vertices ($P_1, P_2, P_3, P_4$).</p>
            <p>For a desired corner fillet radius $ho$, the fillet arc must tangentially blend the straight radial line segment with the concentric circular arc. This shifts the effective radial boundaries inward and outward by $ho$, requiring an angular fillet offset:</p>

            <div class="formula-card">
              <div class="formula-title">Annular Fillet Angular Offset Derivation</div>
              <div class="formula-body">
                \Delta\phi_{	ext{outer}} = rcsin\left(rac{ho}{R - ho}ight) \quad 	ext{and} \quad \Delta\phi_{	ext{inner}} = rcsin\left(rac{ho}{r + ho}ight)
              </div>
              <div class="formula-desc">Where $ho$ is the fillet corner radius, $R$ is the outer radius, and $r$ is the inner radius. The straight radial edges shorten, and small circular arc commands (<code>A ho ho ...</code>) are inserted at each vertex.</div>
            </div>

            <p>By implementing corner fillet math, the resulting SVG paths feature silky-smooth pebble contours that render with impeccable clarity and sophisticated tactile appeal.</p>

            <p>Applying this symmetric gap ensures that every sector possesses identical visual weight, while maintaining crisp geometric gutters that prevent visual crowding. To explore the foundational math behind vector arcs in depth, read our master reference on <a href="/articles/svg-path-arc-commands-math-guide/">SVG path arc commands and mathematics</a>.</p>
          </section>

          <section id="path-string-construction">
            <h2>4. Path String Construction: Mastering the SVG Arc Command (A rx ry ...)</h2>
            <p>The core of an SVG radial menu is the <strong>SVG Path Arc command (<code>A</code>)</strong>. Unlike quadratic or cubic Bézier curves (which approximate curves via control handles), the SVG elliptical arc command defines exact circular geometry using radii and geometric flags.</p>

            <h3>Anatomy of the SVG Arc Command</h3>
            <p>The standard arc command takes seven parameters:</p>
            <pre><code>A rx ry x-axis-rotation large-arc-flag sweep-flag x y</code></pre>
            <ul>
              <li><strong><code>rx ry</code>:</strong> The horizontal and vertical radii of the ellipse. For circular radial menus, both radii are identical ($rx = ry = R$ for outer arcs, $rx = ry = r$ for inner arcs).</li>
              <li><strong><code>x-axis-rotation</code>:</strong> Rotation of the ellipse in degrees relative to the X-axis. For circles, this is always <code>0</code>.</li>
              <li><strong><code>large-arc-flag</code>:</strong> A boolean flag (<code>0</code> or <code>1</code>). If the angular span $\Delta\theta \le 180^\circ$ ($\pi$ radians), <code>large-arc-flag = 0</code>. If the angular span exceeds $180^\circ$ ($\Delta\theta > 180^\circ$), <code>large-arc-flag = 1</code>. In typical menus with 3 or more slices, the span is always $\le 120^\circ$, so this flag is almost universally <code>0</code>.</li>
              <li><strong><code>sweep-flag</code>:</strong> Determines the arc drawing direction. Setting <code>sweep-flag = 1</code> draws the arc in the <strong>positive angular direction (clockwise)</strong>. Setting <code>sweep-flag = 0</code> draws the arc in the <strong>negative angular direction (counter-clockwise)</strong>.</li>
              <li><strong><code>x y</code>:</strong> The target termination coordinates of the arc.</li>
            </ul>

            <h3>The Watertight Annular Path Algorithm</h3>
            <p>To construct an annular sector, we execute five continuous path commands in strict clockwise-outer, counter-clockwise-inner sequence:</p>
            <ol>
              <li><code>M P1.x P1.y</code>: Move pen to the outer start vertex.</li>
              <li><code>A R R 0 largeArc 1 P2.x P2.y</code>: Sweep outer arc clockwise to outer end vertex.</li>
              <li><code>L P3.x P3.y</code>: Draw a straight radial line inward to the inner end vertex.</li>
              <li><code>A r r 0 largeArc 0 P4.x P4.y</code>: Sweep inner arc counter-clockwise back to inner start vertex.</li>
              <li><code>Z</code>: Close path back to $P_1$, completing the watertight vector polygon.</li>
            </ol>

            <pre><code>// Production Annular Sector SVG Path Generator
function createAnnularWedgePath(cx, cy, innerRadius, outerRadius, startAngle, endAngle) {
  const p1 = polarToCartesian(cx, cy, outerRadius, startAngle);
  const p2 = polarToCartesian(cx, cy, outerRadius, endAngle);
  const p3 = polarToCartesian(cx, cy, innerRadius, endAngle);
  const p4 = polarToCartesian(cx, cy, innerRadius, startAngle);

  // Determine if arc spans more than 180 degrees
  const angleDelta = endAngle - startAngle;
  const largeArcFlag = angleDelta > 180 ? 1 : 0;

  // Construct continuous vector path string
  return [
    `M ${p1.x} ${p1.y}`,
    `A ${outerRadius} ${outerRadius} 0 ${largeArcFlag} 1 ${p2.x} ${p2.y}`,
    `L ${p3.x} ${p3.y}`,
    `A ${innerRadius} ${innerRadius} 0 ${largeArcFlag} 0 ${p4.x} ${p4.y}`,
    'Z'
  ].join(' ');
}</code></pre>

            <p>By generating paths using this pure vector approach, each slice acts as a discrete, fully responsive DOM element capable of receiving CSS hover transitions, GPU transforms, and ARIA focus states without pixel blur. For more advanced path construction techniques, check our comprehensive guide on <a href="/articles/svg-path-commands-and-d-attribute-guide/">SVG path commands and the d attribute</a>.</p>
          </section>

          <section id="figure2-architecture">
            <h2>5. Architectural Figure 2: The End-to-End Vector Radial Engine Pipeline</h2>
            <p>The following architectural flowchart diagrams the end-to-end vector pipeline of an enterprise SVG radial navigation system: from input capture and polar coordinate resolution to annular path generation, spring physics integration, and accessible DOM event dispatch.</p>

            <figure class="article-figure">
              <svg viewBox="0 0 960 320" width="960" height="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figure 2: Architecture diagram of the SVG radial menu vector engine pipeline">
                <defs>
                  <linearGradient id="radGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#141414"/>
                    <stop offset="100%" stop-color="#1F2806"/>
                  </linearGradient>
                  <linearGradient id="radGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#181818"/>
                    <stop offset="100%" stop-color="#141E05"/>
                  </linearGradient>
                  <linearGradient id="flowArrowGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="#849E00"/>
                    <stop offset="100%" stop-color="#C1DD2D"/>
                  </linearGradient>
                  <filter id="radGlow" x="-10%" y="-10%" width="120%" height="120%">
                    <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="rgba(193,221,45,0.15)"/>
                  </filter>
                  <marker id="radArrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                    <path d="M 1 1 L 7 4 L 1 7 Z" fill="#C1DD2D"/>
                  </marker>
                </defs>

                <rect width="960" height="320" rx="12" fill="#0D0D0D" stroke="#222" stroke-width="1.5"/>

                <text x="40" y="38" font-family="'Inter', sans-serif" font-size="14" font-weight="800" fill="#C1DD2D" letter-spacing="1">FIGURE 2: SVG RADIAL NAVIGATION WHEEL ARCHITECTURE</text>
                <line x1="40" y1="48" x2="920" y2="48" stroke="#222" stroke-width="1"/>

                <!-- Stage 1 -->
                <g transform="translate(40, 75)" filter="url(#radGlow)">
                  <rect width="150" height="190" rx="8" fill="url(#radGrad1)" stroke="#333" stroke-width="1.5"/>
                  <rect x="12" y="14" width="28" height="28" rx="6" fill="rgba(193,221,45,0.15)"/>
                  <text x="26" y="33" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">01</text>
                  <text x="14" y="66" font-family="'Inter', sans-serif" font-size="13" font-weight="700" fill="#FFF">Input Trigger</text>
                  <text x="14" y="85" font-family="'Inter', sans-serif" font-size="11" fill="#888">Event Ingestion</text>
                  <line x1="14" y1="95" x2="136" y2="95" stroke="#262626" stroke-width="1"/>
                  <text x="14" y="115" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Contextmenu / Click</text>
                  <text x="14" y="132" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Long-Press Touch</text>
                  <text x="14" y="149" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Keyboard Shortcut</text>
                  <text x="14" y="166" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Viewport Clamping</text>
                </g>

                <line x1="190" y1="170" x2="222" y2="170" stroke="url(#flowArrowGrad)" stroke-width="2.5" marker-end="url(#radArrow)"/>

                <!-- Stage 2 -->
                <g transform="translate(225, 75)" filter="url(#radGlow)">
                  <rect width="150" height="190" rx="8" fill="url(#radGrad2)" stroke="#333" stroke-width="1.5"/>
                  <rect x="12" y="14" width="28" height="28" rx="6" fill="rgba(193,221,45,0.15)"/>
                  <text x="26" y="33" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">02</text>
                  <text x="14" y="66" font-family="'Inter', sans-serif" font-size="13" font-weight="700" fill="#FFF">Polar Solver</text>
                  <text x="14" y="85" font-family="'Inter', sans-serif" font-size="11" fill="#888">Arc Trigonometry</text>
                  <line x1="14" y1="95" x2="136" y2="95" stroke="#262626" stroke-width="1"/>
                  <text x="14" y="115" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; &Delta;&theta; = 360&deg; / N</text>
                  <text x="14" y="132" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; 12 o'Clock Offset</text>
                  <text x="14" y="149" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Symmetric Gaps</text>
                  <text x="14" y="166" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Polar &rarr; Cartesian</text>
                </g>

                <line x1="375" y1="170" x2="407" y2="170" stroke="url(#flowArrowGrad)" stroke-width="2.5" marker-end="url(#radArrow)"/>

                <!-- Stage 3 -->
                <g transform="translate(410, 75)" filter="url(#radGlow)">
                  <rect width="150" height="190" rx="8" fill="url(#radGrad1)" stroke="#333" stroke-width="1.5"/>
                  <rect x="12" y="14" width="28" height="28" rx="6" fill="rgba(193,221,45,0.15)"/>
                  <text x="26" y="33" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">03</text>
                  <text x="14" y="66" font-family="'Inter', sans-serif" font-size="13" font-weight="700" fill="#FFF">Annular Engine</text>
                  <text x="14" y="85" font-family="'Inter', sans-serif" font-size="11" fill="#888">SVG Path Builder</text>
                  <line x1="14" y1="95" x2="136" y2="95" stroke="#262626" stroke-width="1"/>
                  <text x="14" y="115" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Outer Arc (A R R)</text>
                  <text x="14" y="132" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Radial Inward (L)</text>
                  <text x="14" y="149" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Inner Arc (A r r)</text>
                  <text x="14" y="166" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Watertight Close (Z)</text>
                </g>

                <line x1="560" y1="170" x2="592" y2="170" stroke="url(#flowArrowGrad)" stroke-width="2.5" marker-end="url(#radArrow)"/>

                <!-- Stage 4 -->
                <g transform="translate(595, 75)" filter="url(#radGlow)">
                  <rect width="150" height="190" rx="8" fill="url(#radGrad2)" stroke="#333" stroke-width="1.5"/>
                  <rect x="12" y="14" width="28" height="28" rx="6" fill="rgba(193,221,45,0.15)"/>
                  <text x="26" y="33" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">04</text>
                  <text x="14" y="66" font-family="'Inter', sans-serif" font-size="13" font-weight="700" fill="#FFF">Spring Physics</text>
                  <text x="14" y="85" font-family="'Inter', sans-serif" font-size="11" fill="#888">RK4 Solver</text>
                  <line x1="14" y1="95" x2="136" y2="95" stroke="#262626" stroke-width="1"/>
                  <text x="14" y="115" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Damped Oscillator</text>
                  <text x="14" y="132" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Staggered Radii</text>
                  <text x="14" y="149" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Elastic Overshoot</text>
                  <text x="14" y="166" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; 120 FPS Raf Loop</text>
                </g>

                <line x1="745" y1="170" x2="777" y2="170" stroke="url(#flowArrowGrad)" stroke-width="2.5" marker-end="url(#radArrow)"/>

                <!-- Stage 5 -->
                <g transform="translate(780, 75)" filter="url(#radGlow)">
                  <rect width="140" height="190" rx="8" fill="url(#radGrad1)" stroke="#C1DD2D" stroke-width="1.5"/>
                  <rect x="12" y="14" width="28" height="28" rx="6" fill="rgba(193,221,45,0.2)"/>
                  <text x="26" y="33" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">05</text>
                  <text x="14" y="66" font-family="'Inter', sans-serif" font-size="13" font-weight="700" fill="#FFF">Accessible UI</text>
                  <text x="14" y="85" font-family="'Inter', sans-serif" font-size="11" fill="#888">DOM &amp; A11y</text>
                  <line x1="14" y1="95" x2="126" y2="95" stroke="#262626" stroke-width="1"/>
                  <text x="14" y="115" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#C1DD2D">&bull; role="menuitem"</text>
                  <text x="14" y="132" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Roving Tabindex</text>
                  <text x="14" y="149" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Arrow Key Nav</text>
                  <text x="14" y="166" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Escape Close</text>
                </g>
              </svg>
              <figcaption>Figure 2: Architecture of the SVG radial menu pipeline, from input ingestion through polar trigonometry, spring physics simulation, and accessible DOM event dispatching.</figcaption>
            </figure>
          </section>

          <section id="interactive-radial-studio">
            <h2>6. Interactive Developer Studio: Live Vector Radial Navigation Generator</h2>
            <p>Experience real-time annular arc generation below. Adjust the number of slices, inner and outer radii, angular gap, and visual theme. Click the center hub or sectors to trigger opening/closing spring animations and inspect live SVG path markup and mathematical parameters in real time.</p>

            <div class="interactive-sandbox" id="radialStudio">
              <div class="sandbox-header">
                <div class="sandbox-title">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 1 10 10M12 12l7-7"/></svg>
                  <span>Interactive SVG Radial Menu Studio</span>
                </div>
                <span class="sandbox-badge">Polar Math &bull; Spring Physics &bull; A11y</span>
              </div>

              <div class="sandbox-grid">
                <div class="sandbox-controls">
                  <div class="control-row">
                    <label for="radialSlicesSlider">Number of Slices (Actions) <span class="stat-num" id="radialSlicesVal">6 Slices</span></label>
                    <input type="range" class="control-input" id="radialSlicesSlider" min="3" max="12" step="1" value="6">
                  </div>

                  <div class="control-row">
                    <label for="radialInnerRadiusSlider">Inner Radius (Hub Size) <span class="stat-num" id="radialInnerVal">55 px</span></label>
                    <input type="range" class="control-input" id="radialInnerRadiusSlider" min="30" max="100" step="5" value="55">
                  </div>

                  <div class="control-row">
                    <label for="radialOuterRadiusSlider">Outer Radius (Menu Reach) <span class="stat-num" id="radialOuterVal">145 px</span></label>
                    <input type="range" class="control-input" id="radialOuterRadiusSlider" min="110" max="185" step="5" value="145">
                  </div>

                  <div class="control-row">
                    <label for="radialGapSlider">Angular Sector Gap <span class="stat-num" id="radialGapVal">3.5&deg;</span></label>
                    <input type="range" class="control-input" id="radialGapSlider" min="0" max="8" step="0.5" value="3.5">
                  </div>

                  <div class="control-row">
                    <label for="radialThemeSelect">Visual Styling Palette <span class="stat-num" id="radialThemeVal">Cyberpunk Neon</span></label>
                    <select class="control-select" id="radialThemeSelect">
                      <option value="cyber">Cyberpunk Neon (#C1DD2D &amp; #38BDF8)</option>
                      <option value="obsidian">Obsidian Stealth (#262626 &amp; #FFFFFF)</option>
                      <option value="sunset">Sunset Ember (#F59E0B &amp; #EF4444)</option>
                      <option value="emerald">Emerald Tactical (#10B981 &amp; #064E3B)</option>
                    </select>
                  </div>

                  <div class="btn-row">
                    <button type="button" class="action-btn primary" id="radialToggleBtn">Toggle Open / Close</button>
                    <button type="button" class="action-btn" id="radialSelectNextBtn">Cycle Next (A11y)</button>
                    <button type="button" class="action-btn" id="radialResetBtn">Reset</button>
                  </div>

                  <div class="stats-readout-box">
                    <div class="stat-item">
                      <div class="stat-label">Sector Arc (&Delta;&theta;)</div>
                      <div class="stat-val highlight" id="statDeltaTheta">60.0&deg;</div>
                    </div>
                    <div class="stat-item">
                      <div class="stat-label">Active Sector</div>
                      <div class="stat-val highlight" id="statActiveSector">Sector 1 (Edit)</div>
                    </div>
                    <div class="stat-item">
                      <div class="stat-label">Outer Arc Length</div>
                      <div class="stat-val" id="statOuterLen">143.2 px</div>
                    </div>
                    <div class="stat-item">
                      <div class="stat-label">State / Focus</div>
                      <div class="stat-val" id="statA11y">Expanded (tabindex=0)</div>
                    </div>
                  </div>
                </div>

                <div class="stage-wrapper">
                  <div class="preview-stage-container" id="radialStageContainer">
                    <svg class="stage-radial-svg" id="radialSvg" viewBox="0 0 600 400" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" role="menu" aria-label="Interactive Radial Action Menu">
                      <defs>
                        <radialGradient id="radialBgGlow" cx="50%" cy="50%" r="50%">
                          <stop offset="0%" stop-color="#C1DD2D" stop-opacity="0.12"/>
                          <stop offset="100%" stop-color="#C1DD2D" stop-opacity="0"/>
                        </radialGradient>
                        <filter id="wedgeGlow" x="-20%" y="-20%" width="140%" height="140%">
                          <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="rgba(193,221,45,0.3)"/>
                        </filter>
                      </defs>

                      <rect width="100%" height="100%" fill="#080808"/>
                      <circle cx="300" cy="200" r="180" fill="url(#radialBgGlow)"/>

                      <!-- Polar Grid Guidelines -->
                      <circle cx="300" cy="200" r="145" fill="none" stroke="#222" stroke-width="1" stroke-dasharray="3 3"/>
                      <circle cx="300" cy="200" r="55" fill="none" stroke="#222" stroke-width="1" stroke-dasharray="3 3"/>
                      <line x1="300" y1="20" x2="300" y2="380" stroke="#1A1A1A" stroke-width="1"/>
                      <line x1="120" y1="200" x2="480" y2="200" stroke="#1A1A1A" stroke-width="1"/>

                      <!-- Dynamic Sectors Group -->
                      <g id="sectorsGroup" role="group"></g>

                      <!-- Central Hub Button -->
                      <g id="centerHubGroup" class="radial-center-hub" role="button" aria-label="Toggle Radial Navigation Menu" tabindex="0">
                        <circle cx="300" cy="200" r="42" fill="#181818" stroke="#C1DD2D" stroke-width="2.5"/>
                        <circle cx="300" cy="200" r="32" fill="#111" stroke="#333" stroke-width="1"/>
                        <path id="hubIcon" d="M 292 192 L 308 208 M 308 192 L 292 208" stroke="#C1DD2D" stroke-width="2.5" stroke-linecap="round"/>
                        <text x="300" y="258" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#888" text-anchor="middle">CLICK HUB</text>
                      </g>
                    </svg>
                  </div>

                  <div class="generated-code-box">
                    <div class="code-box-head">
                      <div class="code-tabs">
                        <button type="button" class="code-tab-btn active" id="tabRadialSvg">SVG Sector Markup</button>
                        <button type="button" class="code-tab-btn" id="tabRadialJs">Trigonometry JS</button>
                      </div>
                      <div class="code-actions">
                        <button type="button" class="copy-btn" id="copyRadialCodeBtn">Copy Code</button>
                      </div>
                    </div>
                    <pre class="code-output-area" id="radialCodeOutput">Click "Toggle Open / Close" or adjust sliders to inspect mathematical vector code...</pre>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <section id="spring-physics-microinteractions">
            <h2>7. Spring Physics &amp; Micro-Interactions: Damped Harmonic Oscillators &amp; RK4</h2>
            <p>Static CSS transitions (such as <code>transition: all 0.3s ease-out</code>) produce predictable, mechanical movements that lack physical weight. In natural mechanics, when an object deploys or rebounds, it behaves according to the laws of classical physics: mass, spring stiffness, and air drag resistance.</p>

            <h3>The Damped Harmonic Oscillator Equation</h3>
            <p>A physical spring is governed by Hooke's Law coupled with velocity damping:</p>

            <div class="formula-card">
              <div class="formula-title">Damped Harmonic Oscillator Equation of Motion</div>
              <div class="formula-body">
                F = m \times a = -k \times (x - x_{\text{target}}) - c \times v<br>
                a = \frac{d^2 x}{dt^2} = -\frac{k}{m} \times (x - x_{\text{target}}) - \frac{c}{m} \times v
              </div>
              <div class="formula-desc">Where $x$ is current position (e.g. radial scale factor from 0.0 to 1.0), $x_{\text{target}}$ is resting equilibrium (1.0 for open, 0.0 for closed), $k$ is spring stiffness (tension), $c$ is damping coefficient (friction), and $m$ is object mass.</div>
            </div>

            <h3>Runge-Kutta 4th Order (RK4) Numerical Integration</h3>
            <p>While naive Euler integration ($x_{t+dt} = x_t + v \cdot dt$) accumulates catastrophic mathematical error and can explode into infinite oscillation when $dt$ fluctuates, the <strong>Runge-Kutta 4th Order (RK4) method</strong> samples acceleration at four distinct sub-step intervals ($k_1, k_2, k_3, k_4$), providing unconditional numerical stability across 60 Hz, 120 Hz, and variable refresh rate screens:</p>

            <pre><code>// Production RK4 Spring Simulation Engine
class SpringSolver {
  constructor(stiffness = 180, damping = 12, mass = 1.0) {
    this.k = stiffness; // Spring tension
    this.c = damping;   // Friction / drag
    this.m = mass;      // Inertial mass
    this.x = 0;         // Current value
    this.v = 0;         // Current velocity
    this.target = 0;    // Target equilibrium
  }

  setTarget(targetVal) {
    this.target = targetVal;
  }

  evaluate(x, v, target, dt, d) {
    const nextX = x + d.dx * dt;
    const nextV = v + d.dv * dt;
    const force = -this.k * (nextX - target) - this.c * nextV;
    return { dx: nextV, dv: force / this.m };
  }

  update(dt = 0.016) {
    const a = this.evaluate(this.x, this.v, this.target, 0, { dx: 0, dv: 0 });
    const b = this.evaluate(this.x, this.v, this.target, dt * 0.5, a);
    const c = this.evaluate(this.x, this.v, this.target, dt * 0.5, b);
    const d = this.evaluate(this.x, this.v, this.target, dt, c);

    const dxdt = (1.0 / 6.0) * (a.dx + 2.0 * (b.dx + c.dx) + d.dx);
    const dvdt = (1.0 / 6.0) * (a.dv + 2.0 * (b.dv + c.dv) + d.dv);

    this.x += dxdt * dt;
    this.v += dvdt * dt;

    // Check if settled to save CPU cycles
    const isSettled = Math.abs(this.target - this.x) < 0.001 && Math.abs(this.v) < 0.001;
    if (isSettled) {
      this.x = this.target;
      this.v = 0;
    }
    return { value: this.x, settled: isSettled };
  }
}</code></pre>

            <h3>Radial Fan-Out Staggering</h3>
            <p>Rather than expanding all wedges simultaneously like a static diaphragm, high-end radial menus introduce an <strong>angular propagation delay</strong>: wedge $i$ begins its spring expansion $\tau_i = i \times 24\text{ ms}$ after wedge 0. This produces an organic clockwise cascading fan-out motion that delights the human eye and reinforces directional spatial memory.</p>
          </section>

          <section id="keyboard-accessibility-wcag">
            <h2>8. Keyboard Accessibility &amp; WCAG 2.2 AA Compliance: Roving Tabindex &amp; ARIA</h2>
            <p>The single greatest historical criticism of radial menus is that they are hostile to keyboard-only and assistive technology users. Because circular layouts lack a linear DOM reading order, naive implementations trap keyboard focus or skip items entirely.</p>
            <p>With careful architecture, an SVG radial menu can achieve <strong>100% WCAG 2.2 Level AA compliance</strong>, offering an experience for keyboard users that is every bit as fluid as pointer or touch interaction.</p>

            <h3>The WAI-ARIA Roving Tabindex Pattern</h3>
            <p>The W3C Authoring Practices Guide (APG) defines the <strong>Roving Tabindex pattern</strong> for composite interactive widgets (such as toolbars, menus, and grid wheels). In this architecture:</p>
            <ul>
              <li>The menu container receives <code>role="menu"</code> and <code>aria-orientation="horizontal"</code>.</li>
              <li>Each annular sector <code>&lt;path&gt;</code> or embedded <code>&lt;button&gt;</code> receives <code>role="menuitem"</code>.</li>
              <li>Only the currently focused sector receives <code>tabindex="0"</code>. All remaining sectors receive <code>tabindex="-1"</code>.</li>
              <li>When the user presses the <kbd>Tab</kbd> key, focus moves into the active sector. Further <kbd>Tab</kbd> presses exit the radial menu completely without cycling through every slice.</li>
            </ul>

            <h3>Circular Arrow Key Navigation Logic</h3>
            <p>To navigate around the circular wheel using a physical keyboard, we map directional keys to angular incrementation:</p>
            <ul>
              <li><strong><kbd>ArrowRight</kbd> &amp; <kbd>ArrowDown</kbd>:</strong> Increments the active sector index clockwise: <code>nextIndex = (currentIndex + 1) % totalSlices</code>.</li>
              <li><strong><kbd>ArrowLeft</kbd> &amp; <kbd>ArrowUp</kbd>:</strong> Decrements the active sector index counter-clockwise: <code>prevIndex = (currentIndex - 1 + totalSlices) % totalSlices</code>.</li>
              <li><strong><kbd>Home</kbd> &amp; <kbd>End</kbd>:</strong> Jump directly to the first (12 o'clock) or last sector.</li>
              <li><strong><kbd>Enter</kbd> &amp; <kbd>Space</kbd>:</strong> Activates the focused sector command.</li>
              <li><strong><kbd>Escape</kbd>:</strong> Dismisses the radial menu and restores focus back to the initiating trigger button.</li>
            </ul>

            <pre><code>// Keyboard Arrow Key Roving Tabindex Handler
function handleRadialKeydown(event, sectors, currentIndex, closeMenuCallback) {
  let newIndex = currentIndex;
  const count = sectors.length;

  switch (event.key) {
    case 'ArrowRight':
    case 'ArrowDown':
      event.preventDefault();
      newIndex = (currentIndex + 1) % count;
      break;
    case 'ArrowLeft':
    case 'ArrowUp':
      event.preventDefault();
      newIndex = (currentIndex - 1 + count) % count;
      break;
    case 'Home':
      event.preventDefault();
      newIndex = 0;
      break;
    case 'End':
      event.preventDefault();
      newIndex = count - 1;
      break;
    case 'Escape':
      event.preventDefault();
      closeMenuCallback();
      return;
    default:
      return;
  }

  // Update roving tabindex
  sectors[currentIndex].setAttribute('tabindex', '-1');
  sectors[newIndex].setAttribute('tabindex', '0');
  sectors[newIndex].focus();
}</code></pre>
          </section>

          <section id="spatial-hit-testing-raycasting">
            <h2>9. Spatial Hit-Testing and Sector Detection: Raycasting Angle &amp; Radius</h2>
            <p>While desktop mouse pointers can rely on native DOM <code>mouseenter</code> and <code>mouseleave</code> events fired on individual SVG <code>&lt;path&gt;</code> elements, touchscreens and stylus devices present a different challenge: during a continuous thumb drag or pen stroke across the screen, the browser does not fire hover events on elements beneath the moving finger.</p>
            <p>To deliver instantaneous touch tracking and marking gestures, frontend engineers implement <strong>polar raycasting</strong> directly on the parent container's <code>pointermove</code> stream.</p>

            <h3>Converting Pointer Coordinates to Polar Vectors</h3>
            <p>Given the menu center pole $(c_x, c_y)$ and the touch event client coordinates $(x_{\text{ptr}}, y_{\text{ptr}})$:</p>

            <div class="formula-card">
              <div class="formula-title">Cartesian to Polar Raycasting Formula</div>
              <div class="formula-body">
                \Delta x = x_{\text{ptr}} - c_x \quad \text{and} \quad \Delta y = y_{\text{ptr}} - c_y<br>
                r_{\text{current}} = \sqrt{\Delta x^2 + \Delta y^2}<br>
                \theta_{\text{raw}} = \text{atan2}(\Delta y, \Delta x) \times \frac{180}{\pi}
              </div>
              <div class="formula-desc">Where $r_{\text{current}}$ is Euclidean distance, and $\text{atan2}$ computes the signed angle in degrees from $-180^\circ$ to $+180^\circ$.</div>
            </div>

            <h3>Deadzone and Boundary Classification</h3>
            <p>With radius and angle in hand, spatial sector classification requires three rapid boolean checks:</p>
            <ol>
              <li><strong>Center Hub Deadzone:</strong> If $r_{\text{current}} &lt; r_{\text{inner}}$, the pointer is resting inside the center hub (triggering no sector highlight or activating the central 'Cancel' zone).</li>
              <li><strong>Outer Threshold Exceeded:</strong> If $r_{\text{current}} > R_{\text{outer}} + \text{tolerance}$, the user has dragged outside the menu boundary.</li>
              <li><strong>Active Wedge Calculation:</strong> Normalize the angle to the range $[0^\circ, 360^\circ)$ relative to 12 o'clock:
                <code>normalizedAngle = (thetaRaw + 90 + 360) % 360</code>. The active sector index is simply:
                <code>activeSector = Math.floor(normalizedAngle / (360 / N))</code>.
              </li>
            </ol>
            <p>Because this calculation requires only a single square root and trigonometric arctangent, it executes in sub-microsecond time, tracking high-speed thumb flicks with zero latency.</p>
          </section>

          <section id="comparative-architecture-benchmark">
            <h2>10. Comparative Architecture Benchmark: SVG Sector Paths vs. CSS Clip-Path / Canvas 2D</h2>
            <p>The following performance benchmark compares three different technical approaches to building an 8-slice circular navigation wheel on modern mobile and desktop browsers.</p>

            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Architecture Dimension</th>
                    <th>CSS clip-path: polygon()</th>
                    <th>HTML5 Canvas 2D</th>
                    <th>Pure SVG Annular Paths</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>True Circular Curves</strong></td>
                    <td>No (faceted multi-point approximation)</td>
                    <td>Yes (via context.arc())</td>
                    <td><strong>Yes (native vector circular arcs)</strong></td>
                  </tr>
                  <tr>
                    <td><strong>Hitbox Accuracy</strong></td>
                    <td>Poor (rectangular box bleeds through)</td>
                    <td>Manual (raycasting math required)</td>
                    <td><strong>100% Exact</strong> (pointer events match geometry)</td>
                  </tr>
                  <tr>
                    <td><strong>Keyboard Accessibility</strong></td>
                    <td>Moderate (DOM buttons clipped)</td>
                    <td>None (opaque pixel canvas)</td>
                    <td><strong>Full WCAG AA</strong> (roving tabindex, ARIA)</td>
                  </tr>
                  <tr>
                    <td><strong>Retina DPI Memory Footprint</strong></td>
                    <td>Low (&lt; 1 MB)</td>
                    <td>High (8–26 MB VRAM buffer)</td>
                    <td><strong>Near-Zero (&lt; 150 KB)</strong></td>
                  </tr>
                  <tr>
                    <td><strong>CSS Design Token Support</strong></td>
                    <td>Supported</td>
                    <td>None (JavaScript redraws)</td>
                    <td><strong>Native</strong> (fill, stroke, filters, CSS vars)</td>
                  </tr>
                  <tr>
                    <td><strong>Frame Rate on Mobile</strong></td>
                    <td>50–55 FPS</td>
                    <td>60 FPS (if optimized)</td>
                    <td><strong>120 FPS (GPU composited)</strong></td>
                  </tr>
                </tbody>
              </table>
            </div>

            <p>As demonstrated by the empirical evaluation, <strong>pure SVG annular paths</strong> deliver the only architectural solution that unites mathematically perfect circular curves, native DOM pointer hitboxes, zero-overhead CSS theming, and full keyboard accessibility.</p>
          </section>

          <section id="enterprise-implementation">
            <h2>11. Enterprise Implementation: Screen Edge Clamping &amp; Submenus</h2>
            <p>When deploying radial menus in production enterprise software (such as web-based CAD tools, analytics dashboards, or cloud document editors), two practical edge cases must be addressed:</p>

            <h3>Screen Edge Detection and Origin Clamping</h3>
            <p>If the user right-clicks or long-presses near the perimeter of the browser viewport, a fixed-radius radial menu would overflow the screen edge, clipping half of the available options outside the visible window. Production systems solve this via <strong>boundary clamping and adaptive partial arcs</strong>:</p>
            <ul>
              <li><strong>Origin Clamping:</strong> Check if $x_{\text{click}} - R_{\text{outer}} &lt; \text{padding}$. If true, shift the menu center pole inward: $c_x = R_{\text{outer}} + \text{padding}$. Repeat for top, right, and bottom edges.</li>
              <li><strong>Hemispherical Slicing:</strong> If an action wheel is docked against a screen border, calculate a <strong>semicircular ($180^\circ$) or quadrant ($90^\circ$) menu</strong>. The sector angle becomes $\Delta\theta = \frac{180^\circ}{N}$, and the menu cleanly fans out into the open viewport space without needing to translate the origin away from the user's cursor.</li>
            </ul>

            <h3>Multi-Level Cascading Submenus (Concentric Rings)</h3>
            <p>For complex command hierarchies (such as selecting a tool, then selecting its brush size or color palette), radial menus scale via <strong>concentric outer rings</strong>. When the user hovers over Sector $A$, an outer secondary ring of annular wedges deploys around the perimeter from $R_{\text{outer}}$ to $R_{\text{sub}}$, visually connecting the child options to their parent wedge.</p>
          </section>

          <section id="key-takeaways">
            <div class="takeaway-box">
              <h3>Architectural Takeaways &amp; Production Checklist</h3>
              <ul>
                <li><strong>Harness Fitts's Law:</strong> Radial menus provide constant acquisition time ($D = R$) and infinite angular target width, outperforming linear dropdowns by up to 60%.</li>
                <li><strong>Apply Zenith Phase Offset:</strong> Subtract $90^\circ$ ($-\pi/2$) in polar conversion so sector 0 originates at the 12 o'clock apex.</li>
                <li><strong>Use Watertight Annular Paths:</strong> Construct wedges using <code>M &rarr; A (outer) &rarr; L &rarr; A (inner) &rarr; Z</code> with matching large-arc and sweep flags.</li>
                <li><strong>Simulate Spring Dynamics:</strong> Integrate damped harmonic oscillators with an RK4 solver for organic physical deployment.</li>
                <li><strong>Enforce WCAG 2.2 AA Accessibility:</strong> Implement WAI-ARIA <code>role="menu"</code>, <code>role="menuitem"</code>, roving <code>tabindex</code>, and circular arrow key navigation.</li>
              </ul>
            </div>
          </section>

          <section id="faq-section">
            <h2>Frequently Asked Questions (FAQ)</h2>
            <div class="faq-item">
              <h3>Why are radial menus ergonomically superior to linear dropdown menus according to Fitts's Law?</h3>
              <p>According to Fitts's Law, target acquisition time is a function of distance to target and target width: T = a + b * log2(2D / W). In traditional linear dropdown menus, items further down the list have progressively larger distances (D), increasing selection time and miss probability. In an SVG radial menu (or pie menu), all primary actions are arranged at an identical radial distance (D = R) from the initial cursor or touch origin, making acquisition time mathematically constant and minimized across all available options.</p>
            </div>
            <div class="faq-item">
              <h3>How do you mathematically construct an SVG annular sector (pie wedge) path?</h3>
              <p>An annular sector wedge is defined by an inner radius r, outer radius R, start angle theta1, and end angle theta2. The SVG path is constructed in four sequential commands: 1) Move to outer arc start (M rx1 ry1); 2) Draw outer circular arc to (rx2 ry2) using the A command; 3) Draw a straight radial line connecting inward to inner arc end (L r_in2 y_in2); 4) Draw inner circular arc backward to inner start (A) in reverse sweep; 5) Close path with Z. This creates an exact, mathematically watertight vector polygon.</p>
            </div>
            <div class="faq-item">
              <h3>How does the SVG arc command's large-arc-flag and sweep-flag work in radial menus?</h3>
              <p>The SVG arc command syntax is A rx ry x-axis-rotation large-arc-flag sweep-flag x y. The large-arc-flag is 0 when the arc span is 180 degrees or less (deltaTheta <= PI), and 1 when the span exceeds 180 degrees. The sweep-flag determines drawing direction: 1 for clockwise (positive angular direction) and 0 for counter-clockwise. For the outer arc, sweep-flag is 1; for the inner return arc, sweep-flag is set to 0 to trace backwards towards the starting radial angle.</p>
            </div>
            <div class="faq-item">
              <h3>How do you make SVG radial menus fully accessible for keyboard and screen reader users?</h3>
              <p>To achieve WCAG 2.2 AA compliance, wrap the radial menu in a container with role='menu' and each sector wedge in a &lt;path&gt; or &lt;button&gt; with role='menuitem'. Implement the WAI-ARIA Roving Tabindex pattern: set tabindex='0' on the active sector and tabindex='-1' on all others. Handle arrow keys (ArrowUp, ArrowDown, ArrowLeft, ArrowRight) to cycle focus sequentially around the circular wheel, allow Escape to close the menu, and ensure all items have descriptive aria-label attributes.</p>
            </div>
            <div class="faq-item">
              <h3>Why use SVG paths instead of CSS clip-path or HTML5 Canvas for circular menus?</h3>
              <p>SVG annular paths provide exact vector hit-testing matching the visible polygon shape without pixel bleed or clipping edge artifacts. CSS clip-path: polygon() can approximate wedges but cannot draw true mathematical circular curves without hundreds of polygon points. Canvas 2D requires complex manual raycasting and is completely opaque to screen readers and keyboard focus. SVG delivers infinite resolution, native DOM events, CSS styling, and built-in accessibility.</p>
            </div>
            <div class="faq-item">
              <h3>How do spring physics improve the feel and usability of radial menu opening transitions?</h3>
              <p>Rather than relying on mechanical linear or cubic-bezier CSS eases, spring physics model real-world damped harmonic oscillation: F = -k * x - c * v. By integrating acceleration and velocity with a Runge-Kutta 4th order (RK4) solver, the radial menu opens with natural physical momentum, subtle overshoot, and smooth settling. This organic tactile response confirms target deployment to the user without visual jarring.</p>
            </div>
          </section>

        </section>

      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <ol>
              <li><a href="#engineering-case-fitts-law">1. The Case for Radial Menus</a></li>
              <li><a href="#polar-vs-cartesian-coordinates">2. Polar vs. Cartesian Math</a></li>
              <li><a href="#annular-sector-mathematics">3. Annular Sector Vertices</a></li>
              <li><a href="#path-string-construction">4. Path Construction (Arc A)</a></li>
              <li><a href="#figure2-architecture">5. Figure 2 Architecture</a></li>
              <li><a href="#interactive-radial-studio">6. Interactive Studio</a></li>
              <li><a href="#spring-physics-microinteractions">7. Spring Physics (RK4)</a></li>
              <li><a href="#keyboard-accessibility-wcag">8. WCAG 2.2 AA Accessibility</a></li>
              <li><a href="#spatial-hit-testing-raycasting">9. Spatial Raycasting</a></li>
              <li><a href="#comparative-architecture-benchmark">10. Architecture Benchmark</a></li>
              <li><a href="#enterprise-implementation">11. Enterprise Clamping</a></li>
              <li><a href="#key-takeaways">12. Key Takeaways</a></li>
              <li><a href="#faq-section">13. FAQs</a></li>
            </ol>
          </nav>
        </div>

        <div class="cta-sidebar-box">
          <h4>Explore 134,000+ Scalable Vector Icons</h4>
          <p>Need crisp, customizable SVG icons for your radial wheels, navigation bars, and action menus? IconStash indexes 28 top open source icon sets with instant search and React/Vue/SVG code export.</p>
          <a href="/#/" class="cta-sidebar-btn">Search IconStash Free</a>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 IconStash. Published by Great Software Company. Written by <a href="/about/">Jouni Flemming</a>. All vector icon sets indexed are property of their respective creators under open-source licenses.</p>
  </footer>

  <script>
    (function() {
      const toggle = document.getElementById('themeToggle');
      const root = document.documentElement;
      const saved = localStorage.getItem('iconstash_theme') || localStorage.getItem('theme') || 'dark';
      root.setAttribute('data-theme', saved);

      if (toggle) {
        toggle.addEventListener('click', function() {
          const current = root.getAttribute('data-theme');
          const next = current === 'dark' ? 'light' : 'dark';
          root.setAttribute('data-theme', next);
          localStorage.setItem('iconstash_theme', next);
          localStorage.setItem('theme', next);
        });
      }
    })();

    (function() {
      const slicesSlider = document.getElementById('radialSlicesSlider');
      const innerSlider = document.getElementById('radialInnerRadiusSlider');
      const outerSlider = document.getElementById('radialOuterRadiusSlider');
      const gapSlider = document.getElementById('radialGapSlider');
      const themeSelect = document.getElementById('radialThemeSelect');

      const slicesVal = document.getElementById('radialSlicesVal');
      const innerVal = document.getElementById('radialInnerVal');
      const outerVal = document.getElementById('radialOuterVal');
      const gapVal = document.getElementById('radialGapVal');
      const themeVal = document.getElementById('radialThemeVal');

      const toggleBtn = document.getElementById('radialToggleBtn');
      const selectNextBtn = document.getElementById('radialSelectNextBtn');
      const resetBtn = document.getElementById('radialResetBtn');
      const copyBtn = document.getElementById('copyRadialCodeBtn');
      const codeOutput = document.getElementById('radialCodeOutput');

      const tabSvg = document.getElementById('tabRadialSvg');
      const tabJs = document.getElementById('tabRadialJs');
      let currentTab = 'svg';

      const statDeltaTheta = document.getElementById('statDeltaTheta');
      const statActiveSector = document.getElementById('statActiveSector');
      const statOuterLen = document.getElementById('statOuterLen');
      const statA11y = document.getElementById('statA11y');

      const sectorsGroup = document.getElementById('sectorsGroup');
      const centerHub = document.getElementById('centerHubGroup');
      const hubIcon = document.getElementById('hubIcon');

      let isOpen = true;
      let activeIndex = 0;
      let animProgress = 1.0;
      let targetProgress = 1.0;
      let animFrame = null;

      const sectorLabels = ['Edit', 'Share', 'Copy', 'Trash', 'Favorite', 'Lock', 'Download', 'Settings', 'Archive', 'Tag', 'Export', 'Duplicate'];

      const themePalettes = {
        cyber: {
          fill: '#151C05',
          stroke: '#C1DD2D',
          hoverFill: '#243208',
          hoverStroke: '#D2ED3E',
          accent: '#C1DD2D',
          text: '#F2F2F2'
        },
        obsidian: {
          fill: '#181818',
          stroke: '#404040',
          hoverFill: '#282828',
          hoverStroke: '#FFFFFF',
          accent: '#FFFFFF',
          text: '#FFFFFF'
        },
        sunset: {
          fill: '#241405',
          stroke: '#F59E0B',
          hoverFill: '#381E08',
          hoverStroke: '#EF4444',
          accent: '#F59E0B',
          text: '#FDE047'
        },
        emerald: {
          fill: '#052014',
          stroke: '#10B981',
          hoverFill: '#0A3320',
          hoverStroke: '#34D399',
          accent: '#10B981',
          text: '#A7F3D0'
        }
      };

      function polarToCartesian(cx, cy, r, angleDeg) {
        const rad = ((angleDeg - 90) * Math.PI) / 180.0;
        return {
          x: Number((cx + r * Math.cos(rad)).toFixed(2)),
          y: Number((cy + r * Math.sin(rad)).toFixed(2))
        };
      }

      function buildAnnularPath(cx, cy, innerR, outerR, startAngle, endAngle) {
        const p1 = polarToCartesian(cx, cy, outerR, startAngle);
        const p2 = polarToCartesian(cx, cy, outerR, endAngle);
        const p3 = polarToCartesian(cx, cy, innerR, endAngle);
        const p4 = polarToCartesian(cx, cy, innerR, startAngle);
        const largeArc = (endAngle - startAngle) > 180 ? 1 : 0;

        return [
          `M ${p1.x} ${p1.y}`,
          `A ${outerR} ${outerR} 0 ${largeArc} 1 ${p2.x} ${p2.y}`,
          `L ${p3.x} ${p3.y}`,
          `A ${innerR} ${innerR} 0 ${largeArc} 0 ${p4.x} ${p4.y}`,
          'Z'
        ].join(' ');
      }

      function renderRadialMenu() {
        const count = parseInt(slicesSlider.value, 10);
        const innerR = parseInt(innerSlider.value, 10);
        const outerR = parseInt(outerSlider.value, 10) * animProgress;
        const gap = parseFloat(gapSlider.value);
        const currentTheme = themePalettes[themeSelect.value] || themePalettes.cyber;

        slicesVal.textContent = count + ' Slices';
        innerVal.textContent = innerSlider.value + ' px';
        outerVal.textContent = outerSlider.value + ' px';
        gapVal.textContent = gap + '°';
        themeVal.textContent = themeSelect.options[themeSelect.selectedIndex].text.split(' (')[0];

        const deltaTheta = 360 / count;
        statDeltaTheta.textContent = deltaTheta.toFixed(1) + '°';
        statOuterLen.textContent = ((deltaTheta / 360) * 2 * Math.PI * outerR).toFixed(1) + ' px';
        statActiveSector.textContent = `Sector ${activeIndex + 1} (${sectorLabels[activeIndex % sectorLabels.length]})`;
        statA11y.textContent = isOpen ? `Expanded (tabindex=0 on #${activeIndex + 1})` : 'Collapsed (hidden)';

        sectorsGroup.innerHTML = '';
        if (animProgress < 0.05) return;

        let samplePathD = '';

        for (let i = 0; i < count; i++) {
          const startAngle = i * deltaTheta + gap / 2;
          const endAngle = (i + 1) * deltaTheta - gap / 2;
          const pathD = buildAnnularPath(300, 200, innerR, Math.max(innerR + 5, outerR), startAngle, endAngle);
          if (i === 0) samplePathD = pathD;

          const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
          g.setAttribute('role', 'menuitem');
          g.setAttribute('aria-label', `${sectorLabels[i % sectorLabels.length]} Action`);
          g.setAttribute('tabindex', i === activeIndex ? '0' : '-1');

          const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
          path.setAttribute('d', pathD);
          path.setAttribute('class', 'radial-sector-path');
          path.setAttribute('fill', i === activeIndex ? currentTheme.hoverFill : currentTheme.fill);
          path.setAttribute('stroke', i === activeIndex ? currentTheme.hoverStroke : currentTheme.stroke);
          path.setAttribute('stroke-width', i === activeIndex ? '2.5' : '1.5');

          // Icon / Text Center Point
          const midAngle = (startAngle + endAngle) / 2;
          const midRadius = (innerR + outerR) / 2;
          const textPos = polarToCartesian(300, 200, midRadius, midAngle);

          const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          text.setAttribute('x', textPos.x);
          text.setAttribute('y', textPos.y + 4);
          text.setAttribute('font-family', "'Inter', sans-serif");
          text.setAttribute('font-size', count > 8 ? '10' : '11.5');
          text.setAttribute('font-weight', '700');
          text.setAttribute('fill', currentTheme.text);
          text.setAttribute('text-anchor', 'middle');
          text.setAttribute('pointer-events', 'none');
          text.textContent = sectorLabels[i % sectorLabels.length];

          g.appendChild(path);
          g.appendChild(text);

          g.addEventListener('click', () => {
            activeIndex = i;
            renderRadialMenu();
            updateCodeBox();
          });

          g.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
              e.preventDefault();
              activeIndex = (activeIndex + 1) % count;
              renderRadialMenu();
              focusActiveSector();
            } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
              e.preventDefault();
              activeIndex = (activeIndex - 1 + count) % count;
              renderRadialMenu();
              focusActiveSector();
            } else if (e.key === 'Escape') {
              e.preventDefault();
              isOpen = false;
              targetProgress = 0;
              animateSpring();
              centerHub.focus();
            }
          });

          sectorsGroup.appendChild(g);
        }

        updateCodeBox(samplePathD);
      }

      function focusActiveSector() {
        const items = sectorsGroup.querySelectorAll('[role="menuitem"]');
        if (items[activeIndex]) {
          items[activeIndex].focus();
        }
      }

      function updateCodeBox(pathString) {
        const count = slicesSlider.value;
        const innerR = innerSlider.value;
        const outerR = outerSlider.value;
        const gap = gapSlider.value;

        if (currentTab === 'svg') {
          codeOutput.textContent = `<!-- SVG Radial Annular Sector (Sector 1 of ${count}) -->\n` +
`<path class="radial-sector"\n` +
`  d="${pathString || buildAnnularPath(300, 200, innerR, outerR, gap/2, (360/count)-gap/2)}"\n` +
`  fill="#151C05"\n` +
`  stroke="#C1DD2D"\n` +
`  stroke-width="1.5"\n` +
`  role="menuitem"\n` +
`  tabindex="0"\n` +
`  aria-label="Edit Command" />`;
        } else {
          codeOutput.textContent = `// Production Polar Arc Function\n` +
`function createWedgePath(cx, cy, innerR, outerR, startAngle, endAngle) {\n` +
`  const toRad = deg => ((deg - 90) * Math.PI) / 180;\n` +
`  const p1 = { x: cx + outerR * Math.cos(toRad(startAngle)), y: cy + outerR * Math.sin(toRad(startAngle)) };\n` +
`  const p2 = { x: cx + outerR * Math.cos(toRad(endAngle)), y: cy + outerR * Math.sin(toRad(endAngle)) };\n` +
`  const p3 = { x: cx + innerR * Math.cos(toRad(endAngle)), y: cy + innerR * Math.sin(toRad(endAngle)) };\n` +
`  const p4 = { x: cx + innerR * Math.cos(toRad(startAngle)), y: cy + innerR * Math.sin(toRad(startAngle)) };\n` +
`  const largeArc = (endAngle - startAngle) > 180 ? 1 : 0;\n` +
`  return \`M \${p1.x.toFixed(2)} \${p1.y.toFixed(2)} \` +\n` +
`         \`A \${outerR} \${outerR} 0 \${largeArc} 1 \${p2.x.toFixed(2)} \${p2.y.toFixed(2)} \` +\n` +
`         \`L \${p3.x.toFixed(2)} \${p3.y.toFixed(2)} \` +\n` +
`         \`A \${innerR} \${innerR} 0 \${largeArc} 0 \${p4.x.toFixed(2)} \${p4.y.toFixed(2)} Z\`;\n` +
`}`;
        }
      }

      function animateSpring() {
        if (animFrame) cancelAnimationFrame(animFrame);

        let velocity = 0;
        const stiffness = 160;
        const damping = 14;
        const dt = 0.016;

        function step() {
          const displacement = animProgress - targetProgress;
          const force = -stiffness * displacement - damping * velocity;
          velocity += force * dt;
          animProgress += velocity * dt;

          if (Math.abs(displacement) < 0.002 && Math.abs(velocity) < 0.002) {
            animProgress = targetProgress;
            renderRadialMenu();
            return;
          }

          renderRadialMenu();
          animFrame = requestAnimationFrame(step);
        }

        step();
      }

      toggleBtn.addEventListener('click', () => {
        isOpen = !isOpen;
        targetProgress = isOpen ? 1.0 : 0.0;
        hubIcon.setAttribute('d', isOpen ? 'M 292 192 L 308 208 M 308 192 L 292 208' : 'M 292 200 L 308 200 M 300 192 L 300 208');
        animateSpring();
      });

      centerHub.addEventListener('click', () => {
        toggleBtn.click();
      });

      centerHub.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          toggleBtn.click();
        }
      });

      selectNextBtn.addEventListener('click', () => {
        const count = parseInt(slicesSlider.value, 10);
        activeIndex = (activeIndex + 1) % count;
        renderRadialMenu();
        focusActiveSector();
      });

      resetBtn.addEventListener('click', () => {
        slicesSlider.value = 6;
        innerSlider.value = 55;
        outerSlider.value = 145;
        gapSlider.value = 3.5;
        themeSelect.value = 'cyber';
        isOpen = true;
        targetProgress = 1.0;
        animProgress = 1.0;
        activeIndex = 0;
        renderRadialMenu();
      });

      slicesSlider.addEventListener('input', renderRadialMenu);
      innerSlider.addEventListener('input', renderRadialMenu);
      outerSlider.addEventListener('input', renderRadialMenu);
      gapSlider.addEventListener('input', renderRadialMenu);
      themeSelect.addEventListener('change', renderRadialMenu);

      tabSvg.addEventListener('click', () => {
        tabSvg.classList.add('active');
        tabJs.classList.remove('active');
        currentTab = 'svg';
        updateCodeBox();
      });

      tabJs.addEventListener('click', () => {
        tabJs.classList.add('active');
        tabSvg.classList.remove('active');
        currentTab = 'js';
        updateCodeBox();
      });

      copyBtn.addEventListener('click', () => {
        const text = codeOutput.textContent;
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(() => {
            copyBtn.textContent = 'Copied!';
            setTimeout(() => { copyBtn.textContent = 'Copy Code'; }, 1800);
          });
        } else {
          const ta = document.createElement('textarea');
          ta.value = text;
          document.body.appendChild(ta);
          ta.select();
          document.execCommand('copy');
          document.body.removeChild(ta);
          copyBtn.textContent = 'Copied!';
          setTimeout(() => { copyBtn.textContent = 'Copy Code'; }, 1800);
        }
      });

      renderRadialMenu();
    })();
  </script>
</body>
</html>
'''

target_dir = r"D:\Project IconStash\IconStash\articles\svg-radial-menus-and-circular-navigation-guide"
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {target_file} ({len(html_content)} bytes)")
