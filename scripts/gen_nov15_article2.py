import os

slug = "svg-heatmaps-and-activity-matrix-visualization-guide"
target_dir = os.path.join(r"D:\Project IconStash\IconStash\articles", slug)
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

html_content = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mastering SVG Heatmaps &amp; Activity Matrices: GitHub-Style Contribution Graphs, Quantile Palettes &amp; Analytics Guide (2026) | IconStash</title>
  <meta name="description" content="Build responsive SVG heatmaps and calendar activity matrices. Master GitHub-style grids, ISO week math, quantile color scales, and interactive tooltip UX.">
  <meta name="keywords" content="svg heatmap, github contribution graph svg, calendar heatmap javascript svg, activity matrix svg, svg heatmap generator, calendar activity graph web, quantile color scale svg, density matrix visualization svg">
  <meta property="og:title" content="Mastering SVG Heatmaps &amp; Activity Matrices: GitHub-Style Contribution Graphs, Quantile Palettes &amp; Analytics Guide (2026)">
  <meta property="og:description" content="Build responsive SVG heatmaps and calendar activity matrices. Master GitHub-style grids, ISO week math, quantile color scales, and interactive tooltip UX.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-heatmaps-and-activity-matrix-visualization-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-heatmaps-and-activity-matrix-visualization-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-15T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-15T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="Vector Graphics &amp; Data Engineering">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="Heatmaps">
  <meta property="article:tag" content="Activity Matrix">
  <meta property="article:tag" content="Data Visualization">
  <meta property="article:tag" content="Frontend Engineering">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mastering SVG Heatmaps &amp; Activity Matrices: GitHub-Style Contribution Graphs, Quantile Palettes &amp; Analytics Guide (2026)">
  <meta name="twitter:description" content="Build responsive SVG heatmaps and calendar activity matrices. Master GitHub-style grids, ISO week math, quantile color scales, and interactive tooltip UX.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-heatmaps-and-activity-matrix-visualization-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-heatmaps-and-activity-matrix-visualization-guide/">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/favicon.jpeg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

    <script type="application/ld+json">
  [
    {
      "@context": "https://schema.org",
      "@type": "TechArticle",
      "headline": "Mastering SVG Heatmaps & Activity Matrices: GitHub-Style Contribution Graphs, Quantile Palettes & Analytics Guide (2026)",
      "description": "Build responsive SVG heatmaps and calendar activity matrices. Master GitHub-style grids, ISO week math, quantile color scales, and interactive tooltip UX.",
      "image": "https://iconstash.io/assets/articles/svg-heatmaps-and-activity-matrix-visualization-guide.jpg",
      "author": {
        "@type": "Person",
        "name": "Jouni Flemming",
        "url": "https://iconstash.io/about/",
        "worksFor": {
          "@type": "Organization",
          "name": "Great Software Company",
          "url": "https://greatsoftwarecompany.com"
        }
      },
      "publisher": {
        "@type": "Organization",
        "name": "IconStash",
        "url": "https://iconstash.io/",
        "logo": {
          "@type": "ImageObject",
          "url": "https://iconstash.io/logo.png"
        },
        "parentOrganization": {
          "@type": "Organization",
          "name": "Great Software Company",
          "url": "https://greatsoftwarecompany.com"
        }
      },
      "datePublished": "2026-11-15",
      "dateModified": "2026-11-15",
      "mainEntityOfPage": "https://iconstash.io/articles/svg-heatmaps-and-activity-matrix-visualization-guide/",
      "inLanguage": "en-US",
      "wordCount": 5200,
      "articleSection": "Vector Graphics & Calendar Engineering",
      "keywords": [
        "svg heatmap",
        "github contribution graph svg",
        "calendar heatmap javascript",
        "activity matrix vector",
        "quantile color scale svg",
        "streak tracking engine",
        "svg data grid"
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "IconStash",
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
          "name": "SVG Heatmaps Guide",
          "item": "https://iconstash.io/articles/svg-heatmaps-and-activity-matrix-visualization-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why build calendar heatmaps in pure SVG rather than HTML tables or Canvas?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Scalable Vector Graphics (SVG) allows 365 daily cells, month headers, and day labels to be rendered inside a single responsive vector coordinate box with subpixel precision. Unlike HTML tables which bloat the DOM with complex nested tags and flexbox calculations, SVG preserves crisp vector geometry, facilitates hardware-accelerated tooltip hover reticles, supports CSS theme overrides, and prints losslessly at 600 DPI in annual PDF developer reports."
          }
        },
        {
          "@type": "Question",
          "name": "How does ISO 8601 calendar projection map 365 days into a 7x52 matrix?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In ISO 8601, weeks begin on Monday (day index 0) and end on Sunday (day index 6). For any given calendar day offset k from the start of the 52-week trailing window, the row coordinate is R = (D0_day + k) mod 7 and the column coordinate is C = floor((D0_day + k) / 7), where D0_day is the day-of-week index of the initiation date. Each cell is positioned at x = padLeft + C * (cellSize + gap) and y = padTop + R * (cellSize + gap)."
          }
        },
        {
          "@type": "Question",
          "name": "Why is non-zero quantile binning superior to linear color normalization for user activity?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Human developer and fitness activity follows a power-law distribution where inactive zero-event days dominate and rare spike days create extreme statistical outliers. A naive linear scale leaves 95% of active days in the faintest tier. Non-zero quantile binning calculates percentiles (25th, 50th, 75th) strictly among days with count greater than 0, guaranteeing balanced visual variance across light, medium, and high activity tiers."
          }
        },
        {
          "@type": "Question",
          "name": "How is continuous user activity streak calculation computed efficiently?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A chronological scan through the sorted timestamp array tracks the current running streak. When an active day is encountered, the current streak increments and the maximum streak record updates. Encountering a zero-event day resets the running streak to 0, operating in optimal O(N) time and O(1) auxiliary memory."
          }
        },
        {
          "@type": "Question",
          "name": "How do you achieve zero-lag tooltip performance across 365+ interactive SVG cells?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Instead of binding individual mouseenter and mouseleave listeners to hundreds of distinct DOM nodes, a single delegated pointermove listener on the parent SVG container extracts cell date and count attributes via event.target.closest('rect'). A single floating HUD tooltip transforms via GPU translate3d() without causing layout thrashing."
          }
        },
        {
          "@type": "Question",
          "name": "How do you ensure SVG heatmaps comply with WCAG 2.2 AA accessibility standards?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The root SVG receives role='graphics-document' with an informative aria-label summarizing total events, active days, and streaks. Each cell receives role='graphics-symbol', an accessible aria-label with the formatted date and event tally, and full keyboard tab-navigation with visible focus rings."
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

    .site-header { position: sticky; top: 0; z-index: 100; background: rgba(10,10,10,0.88); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid #1F1F1F; padding: 0 24px; height: 58px; display: flex; align-items: center; justify-content: space-between; }
    .site-header .logo { display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 18px; color: #F2F2F2; }
    .site-header .logo svg { width: 24px; height: 24px; color: #C1DD2D; }
    .site-header nav { display: flex; gap: 24px; align-items: center; }
    .site-header nav a { color: #888; font-size: 14px; font-weight: 500; }
    .site-header nav a:hover { color: #F2F2F2; }
    .header-cta { background: #C1DD2D; color: #0A0A0A; font-weight: 700; font-size: 13px; padding: 8px 18px; border-radius: 6px; border: none; cursor: pointer; transition: all 150ms ease; display: inline-block; }
    .header-cta:hover { background: #D2ED3E; transform: translateY(-1px); }
    .theme-toggle-btn { background: transparent; border: 1px solid #262626; color: #A3A3A3; width: 34px; height: 34px; border-radius: 6px; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 150ms ease; }
    .theme-toggle-btn:hover { border-color: #404040; color: #F2F2F2; }

    .page-container { max-width: 1280px; margin: 0 auto; padding: 48px 24px 80px; width: 100%; }
    .breadcrumb { display: flex; gap: 8px; font-size: 13px; color: #666; margin-bottom: 24px; align-items: center; flex-wrap: wrap; }
    .breadcrumb a { color: #888; }
    .breadcrumb a:hover { color: #C1DD2D; }
    .breadcrumb .sep { color: #444; }
    .breadcrumb .current { color: #FFF; font-weight: 500; }

    .article-hero { margin-bottom: 36px; border-bottom: 1px solid #1F1F1F; padding-bottom: 32px; }
    .article-hero .tag { display: inline-block; background: rgba(193,221,45,0.12); color: #C1DD2D; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; padding: 4px 12px; border-radius: 4px; margin-bottom: 16px; border: 1px solid rgba(193,221,45,0.25); }
    .article-hero h1 { font-size: clamp(28px, 4vw, 42px); font-weight: 900; line-height: 1.18; color: #FFF; letter-spacing: -0.03em; margin-bottom: 16px; }
    .article-meta { display: flex; gap: 20px; font-size: 13px; color: #737373; align-items: center; flex-wrap: wrap; margin-top: 12px; }
    .article-meta a { color: #C1DD2D; font-weight: 600; text-decoration: none; }

    .article-layout { display: grid; grid-template-columns: minmax(0, 1fr); gap: 48px; align-items: start; }
    @media (min-width: 1024px) {
      .article-layout { grid-template-columns: minmax(0, 1fr) 320px; }
    }

    .article-main { min-width: 0; }
    .featured-summary { background: linear-gradient(180deg, #141414 0%, #0E0E0E 100%); border: 1px solid #262626; border-left: 4px solid #C1DD2D; border-radius: 10px; padding: 24px 28px; margin-bottom: 32px; }
    .featured-summary p { font-size: 15.5px; line-height: 1.7; color: #E5E5E5; margin-bottom: 12px; font-weight: 500; }
    .featured-summary ul { margin: 0 0 0 20px; color: #D4D4D4; }
    .featured-summary li { margin-bottom: 8px; font-size: 14.5px; line-height: 1.6; }

    .article-figure { margin: 28px 0 36px; padding: 0; display: block; }
    .article-figure img { width: 100%; max-width: 100%; height: auto; border-radius: 10px; display: block; border: 1px solid #262626; }
    .article-figure figcaption { font-size: 0.85em; color: #737373; text-align: center; margin-top: 10px; font-style: italic; }

    h2 { font-size: 26px; font-weight: 800; color: #FFF; letter-spacing: -0.02em; margin: 48px 0 20px; padding-top: 24px; border-top: 1px solid #1F1F1F; }
    h3 { font-size: 20px; font-weight: 700; color: #E5E5E5; margin: 32px 0 14px; }
    h4 { font-size: 17px; font-weight: 700; color: #DDD; margin: 24px 0 10px; }
    p { margin-bottom: 22px; color: #D4D4D4; font-size: 16px; line-height: 1.8; }
    strong { color: #FFF; }
    ul, ol { margin: 0 0 24px 28px; color: #D4D4D4; }
    li { margin-bottom: 10px; line-height: 1.7; font-size: 15.5px; }

    pre { background: #121212; border: 1px solid #222; border-radius: 8px; padding: 20px; overflow-x: auto; margin: 24px 0; font-family: "JetBrains Mono", monospace; font-size: 13.5px; line-height: 1.6; color: #E5E5E5; }
    code { font-family: "JetBrains Mono", monospace; font-size: 0.9em; background: #1A1A1A; padding: 2px 6px; border-radius: 4px; color: #C1DD2D; }

    .table-container { overflow-x: auto; margin: 32px 0; border: 1px solid #222; border-radius: 12px; -webkit-overflow-scrolling: touch; }
    table { width: 100%; min-width: 640px; border-collapse: collapse; text-align: left; font-size: 14.5px; }
    th { background: #161616; color: #FFF; padding: 14px 18px; font-weight: 700; border-bottom: 1px solid #222; }
    td { padding: 14px 18px; border-bottom: 1px solid #1A1A1A; color: #CCC; }
    tr:last-child td { border-bottom: none; }
    tr:nth-child(even) { background: rgba(255,255,255,0.01); }

    .formula-card { background: #111; border: 1px solid #262626; border-left: 3px solid #C1DD2D; border-radius: 8px; padding: 16px 20px; margin: 24px 0; }
    .formula-title { font-weight: 700; font-size: 14px; color: #FFF; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
    .formula-body { font-family: "JetBrains Mono", monospace; font-size: 15px; color: #C1DD2D; margin-bottom: 6px; }
    .formula-desc { font-size: 13.5px; color: #888; line-height: 1.5; }

    /* Interactive Studio Styling */
    .interactive-sandbox { background: #121212; border: 1px solid #262626; border-radius: 12px; padding: 24px; margin: 36px 0; }
    .sandbox-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px; border-bottom: 1px solid #222; padding-bottom: 14px; }
    .sandbox-title { display: flex; align-items: center; gap: 8px; font-weight: 800; font-size: 16px; color: #FFF; }
    .sandbox-title svg { color: #C1DD2D; }
    .sandbox-badge { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; background: rgba(193,221,45,0.12); color: #C1DD2D; padding: 3px 8px; border-radius: 4px; border: 1px solid rgba(193,221,45,0.25); }

    .sandbox-grid { display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(0, 1.15fr); gap: 24px; align-items: start; }
    @media (max-width: 860px) { .sandbox-grid { grid-template-columns: 1fr; } }

    .sandbox-controls { display: flex; flex-direction: column; gap: 16px; }
    .control-row { display: flex; flex-direction: column; gap: 6px; }
    .control-row label { font-size: 13px; font-weight: 600; color: #BBB; display: flex; justify-content: space-between; }
    .control-row .stat-num { color: #C1DD2D; font-family: "JetBrains Mono", monospace; }

    .control-select, .control-input { background: #181818; border: 1px solid #333; color: #F2F2F2; padding: 8px 12px; border-radius: 6px; font-family: "Inter", sans-serif; font-size: 13.5px; width: 100%; }
    .control-select:focus, .control-input:focus { outline: none; border-color: #C1DD2D; }

    .btn-row { display: flex; gap: 10px; flex-wrap: wrap; }
    .action-btn { background: #222; border: 1px solid #333; color: #EEE; font-size: 12.5px; font-weight: 600; padding: 8px 14px; border-radius: 6px; cursor: pointer; transition: all 150ms ease; display: inline-flex; align-items: center; gap: 6px; }
    .action-btn:hover { background: #2A2A2A; border-color: #444; color: #FFF; }
    .action-btn.primary { background: #C1DD2D; color: #0A0A0A; border-color: #C1DD2D; font-weight: 700; }
    .action-btn.primary:hover { background: #D2ED3E; }

    .stage-wrapper { display: flex; flex-direction: column; gap: 14px; }
    .preview-stage-container { width: 100%; min-height: 380px; border: 1px dashed #444; border-radius: 10px; background: #0A0E14; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; overflow-x: auto; padding: 20px 10px; }
    .stage-canvas-element { width: 100%; height: auto; min-width: 680px; display: block; }

    .stats-readout-box { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; background: #0E0E0E; border: 1px solid #222; border-radius: 8px; padding: 12px; }
    @media (max-width: 640px) { .stats-readout-box { grid-template-columns: repeat(2, 1fr); } }
    .stat-item { text-align: center; }
    .stat-label { font-size: 11px; text-transform: uppercase; color: #888; font-weight: 600; margin-bottom: 2px; }
    .stat-val { font-size: 14px; font-family: "JetBrains Mono", monospace; font-weight: 700; color: #FFF; }
    .stat-val.highlight { color: #C1DD2D; }

    .code-preview-pane { background: #0B0E14; border: 1px solid #222; border-radius: 8px; padding: 12px; font-family: "JetBrains Mono", monospace; font-size: 12px; color: #9CDCFE; max-height: 180px; overflow-y: auto; white-space: pre-wrap; word-break: break-all; }

    /* FAQ Section */
    .faq-block { margin: 40px 0; }
    .faq-item { border-bottom: 1px solid #1F1F1F; padding: 20px 0; }
    .faq-question { font-size: 18px; font-weight: 700; color: #FFF; margin-bottom: 10px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
    .faq-answer { color: #B0B0B0; font-size: 15.5px; line-height: 1.7; }

    /* Sidebar / Sticky TOC */
    .article-sidebar { position: sticky; top: 80px; display: flex; flex-direction: column; gap: 24px; }
    .sidebar-card { background: #121212; border: 1px solid #222; border-radius: 12px; padding: 24px; }
    .sidebar-title { font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin-bottom: 16px; }
    .toc-nav ol { list-style: none; margin: 0; padding: 0; }
    .toc-nav li { margin-bottom: 10px; font-size: 14px; }
    .toc-nav a { color: #A3A3A3; display: block; line-height: 1.5; }
    .toc-nav a:hover { color: #C1DD2D; }

    .cta-sidebar-box { background: linear-gradient(145deg, #181E07 0%, #0F1205 100%); border: 1px solid rgba(193,221,45,0.3); border-radius: 12px; padding: 24px; text-align: center; }
    .cta-sidebar-box h4 { font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 8px; }
    .cta-sidebar-box p { font-size: 13.5px; color: #AAA; line-height: 1.5; margin-bottom: 16px; }
    .cta-sidebar-btn { display: inline-block; width: 100%; background: #C1DD2D; color: #0A0A0A; font-weight: 800; font-size: 14px; padding: 12px 18px; border-radius: 6px; transition: all 150ms ease; }
    .cta-sidebar-btn:hover { background: #D2ED3E; transform: translateY(-1px); }

    .takeaway-box { background: linear-gradient(135deg, rgba(193,221,45,0.06) 0%, rgba(193,221,45,0.02) 100%); border: 1px solid rgba(193,221,45,0.2); border-radius: 12px; padding: 28px; margin: 40px 0; }
    .takeaway-box h3 { color: #C1DD2D; font-size: 18px; font-weight: 800; margin-bottom: 16px; margin-top: 0; }
    .warning-box { background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.25); border-left: 4px solid #EF4444; border-radius: 8px; padding: 18px 22px; margin: 24px 0; }
    .warning-box h4 { color: #F87171; font-size: 15px; margin-bottom: 8px; }
    .warning-box p { color: #E5E5E5; margin-bottom: 0; font-size: 14.5px; }

    /* Light Theme Contrast Rules (WCAG 2.2 AA Compliant) */
    html[data-theme="light"] body { background: #FAFAFA; color: #171717; }
    html[data-theme="light"] .site-header { background: rgba(250,250,250,0.88); border-bottom-color: #E5E5E5; }
    html[data-theme="light"] .site-header .logo { color: #171717; }
    html[data-theme="light"] .site-header nav a { color: #525252; }
    html[data-theme="light"] .site-header nav a:hover { color: #0A0A0A; }
    html[data-theme="light"] .article-hero h1 { color: #0A0A0A; }
    html[data-theme="light"] h2 { color: #0A0A0A; border-top-color: #E5E5E5; }
    html[data-theme="light"] h3 { color: #171717; }
    html[data-theme="light"] h4 { color: #262626; }
    html[data-theme="light"] p, html[data-theme="light"] ul, html[data-theme="light"] ol { color: #383838; }
    html[data-theme="light"] strong { color: #0A0A0A; }
    html[data-theme="light"] .featured-summary { background: #F4F4F5; border-color: #E4E4E7; border-left-color: #849E00; }
    html[data-theme="light"] .featured-summary p { color: #18181B; }
    html[data-theme="light"] pre { background: #F4F4F5; border-color: #E4E4E7; color: #18181B; }
    html[data-theme="light"] pre code { background: transparent; color: #18181B; }
    html[data-theme="light"] code { background: #E4E4E7; color: #4D6300; }
    html[data-theme="light"] a { color: #4D6300; }
    html[data-theme="light"] a:hover { color: #364600; }
    html[data-theme="light"] .breadcrumb a { color: #4D6300; }
    html[data-theme="light"] .breadcrumb a:hover { color: #364600; }
    html[data-theme="light"] .breadcrumb .current { color: #171717; }
    html[data-theme="light"] .breadcrumb .sep { color: #A1A1AA; }
    html[data-theme="light"] .toc-nav a { color: #3F3F46; }
    html[data-theme="light"] .toc-nav a:hover { color: #4D6300; }
    html[data-theme="light"] .site-footer a { color: #4D6300; }
    html[data-theme="light"] .site-footer a:hover { color: #364600; }
    html[data-theme="light"] .article-hero .tag { background: #E4E4E7; color: #4D6300; border-color: #D4D4D8; }
    html[data-theme="light"] .site-footer { background: #FAFAFA; border-top-color: #E5E5E5; }
    html[data-theme="light"] .sidebar-card { background: #F4F4F5; border-color: #E4E4E7; }
    html[data-theme="light"] .cta-sidebar-box { background: #ECFDF5; border-color: #A7F3D0; }
    html[data-theme="light"] .cta-sidebar-box h4 { color: #064E3B; }
    html[data-theme="light"] .cta-sidebar-box p { color: #047857; }
    html[data-theme="light"] th { background: #F4F4F5; color: #18181B; border-bottom-color: #E4E4E7; }
    html[data-theme="light"] td { border-bottom-color: #E4E4E7; color: #3F3F46; }
    html[data-theme="light"] .table-container { border-color: #E4E4E7; }
    html[data-theme="light"] .interactive-sandbox { background: #F4F4F5; border-color: #E4E4E7; }
    html[data-theme="light"] .sandbox-header { border-bottom-color: #E4E4E7; }
    html[data-theme="light"] .sandbox-title { color: #18181B; }
    html[data-theme="light"] .control-row label { color: #4B5563; }
    html[data-theme="light"] .preview-stage-container { background: #F9FAFB; border-color: #D1D5DB; }
    html[data-theme="light"] .control-select, html[data-theme="light"] .control-input { background: #FFFFFF; border-color: #D1D5DB; color: #18181B; }
    html[data-theme="light"] .stats-readout-box { background: #F4F4F5; border-color: #E4E4E7; }
    html[data-theme="light"] .stat-val { color: #18181B; }
    html[data-theme="light"] .stat-val.highlight { color: #4D6300; }
    html[data-theme="light"] .sandbox-badge { background: #E4E4E7; color: #4D6300; border-color: #D4D4D8; }
    html[data-theme="light"] .control-row .stat-num { color: #4D6300; }
    html[data-theme="light"] .formula-card { background: #F4F4F5; border-color: #E4E4E7; border-left-color: #849E00; }
    html[data-theme="light"] .formula-title { color: #4D6300; }
    html[data-theme="light"] .formula-body { color: #18181B; }
    html[data-theme="light"] .formula-desc { color: #525252; }
    html[data-theme="light"] .takeaway-box { background: #F4F4F5; border-color: #E4E4E7; }
    html[data-theme="light"] .takeaway-box h3 { color: #4D6300; }
    html[data-theme="light"] .warning-box { background: #FEF2F2; border-color: #FCA5A5; border-left-color: #EF4444; }
    html[data-theme="light"] .warning-box h4 { color: #B91C1C; }
    html[data-theme="light"] .warning-box p { color: #450A0A; }
    html[data-theme="light"] .sidebar-title { color: #4D6300; }
    html[data-theme="light"] .stat-label { color: #525252; }
    html[data-theme="light"] .article-meta a { color: #4D6300; }
  </style>
</head>
<body>

  <header class="site-header">
    <a href="/" class="logo" aria-label="IconStash.io home">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 21 7v10l-9 5-9-5V7l9-5Z"/><path d="m8 9 4-2 4 2v6l-4 2-4-2V9Z"/></svg>
      <span>IconStash</span>
    </a>
    <nav>
      <a href="/#/">Search 134K+ Icons</a>
      <a href="/articles/">Articles &amp; Guides</a>
      <a href="/Listicles/best-free-icon-sets-2026/">Best Sets</a>
      <a href="/Glossary/icon-svg-terminology/">Glossary</a>
      <a href="/about/">About</a>
      <a href="/#/" class="header-cta">Browse Library</a>
      <button class="theme-toggle-btn" id="themeToggle" aria-label="Toggle visual theme" title="Toggle theme">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
      </button>
    </nav>
  </header>

  <main class="page-container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">IconStash</a>
      <span class="sep">/</span>
      <a href="/articles/">Articles</a>
      <span class="sep">/</span>
      <span class="current" aria-current="page">Mastering SVG Heatmaps &amp; Activity Matrices</span>
    </nav>

    <header class="article-hero">
      <span class="tag">Analytics &amp; Vector Data Engineering</span>
      <h1>Mastering SVG Heatmaps &amp; Activity Matrices: GitHub-Style Contribution Graphs, Quantile Palettes &amp; Analytics Guide</h1>
      <div class="article-meta">
        <span>By <a href="/about/" rel="author">Jouni Flemming</a></span>
        <span>&bull;</span>
        <time datetime="2026-11-15">November 15, 2026</time>
        <span>&bull;</span>
        <span>32 min read</span>
        <span>&bull;</span>
        <span>6,640 words</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">
        <div class="featured-summary">
          <p><strong>Executive Architectural Summary:</strong> The calendar activity heatmap—popularized globally by GitHub's ubiquitous developer contribution graph—has become the gold standard UI pattern for visualizing chronological intensity, habit streaks, server resource utilization, and event density across hundreds of days or thousands of hours. In modern frontend engineering, building these matrix visualizations with native Scalable Vector Graphics (SVG) delivers mathematical layout precision, sub-millisecond hover inspection, seamless dark/light mode CSS themer integration, and effortless high-DPI export.</p>
          <ul>
            <li><strong>Calendar Grid Geometry:</strong> Formulating ISO 8601 temporal math to project 365 calendar days into a 52-week horizontal matrix with 7 weekday rows, month header offsets, and leap year handling.</li>
            <li><strong>Perceptual Color Quantization:</strong> Implementing robust quantile and percentile binning distributions to overcome the long-tail distortion inherent in naive linear color interpolations.</li>
            <li><strong>Accessible DOM Architecture:</strong> Structuring SVG grids with ARIA grid semantics, roving tabindex keyboard traversal, and screen-reader status announcements conforming to WCAG 2.2 AA mandates.</li>
            <li><strong>High-Frequency Interaction &amp; Tooltip HUD:</strong> Engineering zero-lag floating inspection tooltips, active day highlighting, and multi-day streak calculation engines at 120 FPS.</li>
            <li><strong>Multi-Scale Density &amp; Export:</strong> Scaling from micro sparkline matrices to dense hourly server cluster heatmaps with batched compound paths and automated high-DPI vector SVG badge export.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-heatmaps-and-activity-matrix-visualization-guide.jpg" alt="Mastering SVG Heatmaps and Activity Matrix guide hero interface showing a glowing green developer contribution grid, calendar heatmap metrics, and telemetry dashboard" width="1200" height="675" fetchpriority="high" decoding="async">
          <figcaption>Figure 1: High-precision SVG calendar activity heatmap environment rendering 365 days of continuous developer telemetry, featuring quantile color binning, month boundary dividers, streak metrics, and interactive inspection.</figcaption>
        </figure>

        <section id="introduction-heatmap-paradigm">
          <h2>1. Introduction: The Rise of Temporal Density Visualizations in Modern UI</h2>
          <p>In modern software engineering, telemetry analysis, DevOps monitoring, and quantified self-tracking, developers and end users are inundated with immense volumes of time-series event data. A cloud infrastructure cluster generates millions of CPU load metrics every second; a modern distributed software team registers thousands of pull requests, commits, and code review comments each month; a personal productivity platform tracks habits across hundreds of consecutive days. When software architects attempt to display this data using conventional line charts or bar graphs, the interface quickly collapses into an illegible tangle of overlapping strokes or an interminable horizontal scrolling list. For high-frequency financial time-series, compare our architecture guide on <a href="/articles/svg-candlestick-charts-and-financial-visualization-guide/">SVG candlestick charts and financial visualizations</a>.</p>

          <p>The calendar heatmap—initially conceptualized in academic information visualization literature and catapulted into mainstream software culture by GitHub's iconic user profile contribution graph—solves this problem with mathematical elegance. By decomposing time into a discrete two-dimensional matrix where columns represent calendar weeks and rows represent days of the week, a full 365-day annual timeline can be compressed into a compact, beautiful widget that fits effortlessly on a standard laptop display or executive dashboard. At a single glance, users can immediately identify seasonal velocity trends, prolonged productive streaks, weekend quiet periods, sudden activity spikes, and multi-week lulls.</p>

          <p>However, when engineering a production activity heatmap for a modern web application, developers face critical architectural trade-offs across three primary rendering technologies:</p>
          <ul>
            <li><strong>HTML DOM Grid / Flexbox Implementations:</strong> Some UI component libraries attempt to construct calendar heatmaps using nested HTML elements (e.g. 52 <code>&lt;div class="week-column"&gt;</code> containers each holding 7 <code>&lt;div class="day-cell"&gt;</code> elements). This approach creates severe performance bottlenecks: 365 elements plus wrappers, borders, and flexbox styles generate a massive CSS layout tree. The browser must calculate box models, margins, padding, and layout reflows for over 400 DOM nodes. When animating multiple heatmaps across a team dashboard, frame rates plummet and mobile scrolling stutters noticeably.</li>
            <li><strong>HTML5 2D Canvas Implementations:</strong> Canvas libraries bypass DOM bloat by drawing cells onto a flat pixel buffer. While initial rendering is fast, Canvas introduces significant user experience compromises. Because Canvas obliterates the geometric identity of individual day cells, detecting mouse hover requires manual bounding-box collision detection. More critically, Canvas is completely invisible to screen readers, preventing visually impaired software engineers from reviewing their own team's contribution metrics and violating corporate accessibility mandates. Furthermore, zooming or printing a Canvas heatmap causes fuzzy, pixelated cell boundaries.</li>
            <li><strong>Scalable Vector Graphics (SVG):</strong> SVG provides the definitive, industry-standard solution. In an SVG heatmap, each day cell is rendered as a clean, hardware-accelerated <code>&lt;rect&gt;</code> element mapped to exact Cartesian coordinates within a unified <code>viewBox</code>. The browser treats the entire matrix as a single graphic, offloading rendering directly to the GPU compositor thread. Most importantly, SVG preserves full DOM inspectability: cells can be styled via CSS variables, inspected via native pointer events, focused via keyboard tab navigation, and assigned rich ARIA metadata, while remaining infinitely scalable for high-DPI retina monitors and vector print datasheets.</li>
          </ul>

          <p>In this comprehensive engineering guide, we dissect the mathematical foundations, color theory, algorithmic optimizations, and accessibility architectures required to build production-grade SVG calendar heatmaps and activity matrices from first principles. Similar to the spatial mapping principles detailed in our deep dives on <a href="/articles/svg-tree-diagrams-and-hierarchical-visualization-guide/">SVG tree diagrams and tidy hierarchies</a> and <a href="/articles/svg-gantt-charts-and-project-timelines-guide/">SVG Gantt charts and project timelines</a>, calendar matrix projection requires rigid geometric boundary math.</p>
        </section>

        <section id="calendar-grid-topology-math">
          <h2>2. Calendar Grid Topology &amp; ISO 8601 Temporal Projection Mathematics</h2>
          <p>Constructing a calendar heatmap requires mapping a continuous sequence of 365 (or 366 in leap years) chronological calendar days onto a discrete two-dimensional grid consisting of 7 vertical rows and 52 to 53 horizontal columns. While this layout appears deceptively simple on the surface, implementing the underlying date arithmetic requires rigorous handling of calendar quirks, day-of-week indexing offsets, and month boundary coordinates.</p>

          <h3>2.1 The 7&times;53 Matrix Coordinate System</h3>
          <p>Let <em>D</em><sub>0</sub> represent the anchor initiation date of the calendar heatmap (typically exactly one calendar year prior to today's date, or January 1st of the target year). For any arbitrary date <em>D<sub>k</sub></em> occurring <em>k</em> days after <em>D</em><sub>0</sub>, we must compute its exact column index <em>C</em>(<em>k</em>) and row index <em>R</em>(<em>k</em>) within the grid.</p>

          <p>In Western business and developer applications conforming to the international <strong>ISO 8601</strong> standard, the calendar week commences on <strong>Monday</strong> (<em>d</em><sub>iso</sub> = 0) and concludes on <strong>Sunday</strong> (<em>d</em><sub>iso</sub> = 6). Conversely, standard US calendar conventions treat <strong>Sunday</strong> as the initial day of the week (<em>d</em><sub>us</sub> = 0). To ensure our vector engine supports both conventions cleanly, we define a day-offset shift parameter <em>S</em><sub>start</sub> &isin; {0, 1}, where <em>S</em><sub>start</sub> = 1 denotes a Monday start and <em>S</em><sub>start</sub> = 0 denotes a Sunday start.</p>

          <div class="formula-card">
            <div class="formula-title">Day-of-Week Row Index Formulation</div>
            <div class="formula-body">R(D) = ( D.getDay() - S_start + 7 ) % 7</div>
            <div class="formula-desc">Maps JavaScript's native 0 (Sunday) through 6 (Saturday) into a normalized row index from 0 (top row) to 6 (bottom row).</div>
          </div>

          <p>Computing the horizontal column index <em>C</em>(<em>k</em>) is slightly more involved because the initial date <em>D</em><sub>0</sub> rarely falls on the very first day of a week. If <em>D</em><sub>0</sub> is a Wednesday, the first column must display empty or transparent placeholders for Monday and Tuesday, placing <em>D</em><sub>0</sub> on row 2. To preserve strict chronological alignment across all 52 weeks, the column index is formulated by accumulating the initial day offset:</p>

          <div class="formula-card">
            <div class="formula-title">Horizontal Week Column Index Equation</div>
            <div class="formula-body">C(k) = Math.floor( ( k + R(D_0) ) / 7 )</div>
            <div class="formula-desc">Where k is the integer day offset from the anchor start date D_0, and R(D_0) is the day-of-week row index of the anchor date.</div>
          </div>

          <p>Once the discrete matrix indices (<em>C</em>, <em>R</em>) are determined, they are projected into continuous SVG viewport pixel space using the cell side length <em>S</em><sub>cell</sub> (typically 10px to 14px) and inter-cell gap spacing <em>G</em><sub>cell</sub> (typically 2px to 4px):</p>

          <div class="formula-card">
            <div class="formula-title">Cell Pixel Coordinate Equations</div>
            <div class="formula-body">X_cell(C) = X_pad + C &times; ( S_cell + G_cell )<br>Y_cell(R) = Y_pad + R &times; ( S_cell + G_cell )</div>
            <div class="formula-desc">Where X_pad provides left margin space for weekday labels (Mon, Wed, Fri), and Y_pad provides top margin space for month headers (Jan, Feb, Mar...).</div>
          </div>

          <h3>2.2 Algorithmic Month Label Positioning</h3>
          <p>A frequent design flaw in poorly engineered calendar heatmaps is misaligned month labels. Some naive implementations divide the 52 columns evenly into 12 segments of 4.33 weeks, causing month names to drift arbitrarily away from the actual calendar start dates of those months. By November, the month label might sit two weeks ahead of the actual 1st of the month.</p>

          <p>A mathematically rigorous SVG heatmap engine iterates sequentially through the 365 calendar days and detects the exact column where each new month begins:</p>

          <pre><code>// Exact Algorithmic Month Label Position Generator
function computeMonthHeaderPositions(calendarDays, cellSize = 11, cellGap = 3, xPad = 32) {
  const monthLabels = [];
  let lastMonth = -1;

  calendarDays.forEach((day, index) => {
    const month = day.date.getMonth(); // 0 to 11
    if (month !== lastMonth) {
      // First day encountered for this month
      const colIndex = Math.floor((index + day.startOffset) / 7);
      const xPixel = xPad + colIndex * (cellSize + cellGap);
      
      // Enforce minimum 2-column spacing threshold to prevent label collisions
      if (monthLabels.length === 0 || colIndex - monthLabels[monthLabels.length - 1].col >= 2) {
        monthLabels.push({
          name: day.date.toLocaleDateString('en-US', { month: 'short' }),
          x: xPixel,
          col: colIndex
        });
      }
      lastMonth = month;
    }
  });

  return monthLabels;
}</code></pre>
        </section>

        <section id="color-quantization-palettes">
          <h2>3. Color Quantization &amp; Perceptual Palette Theory</h2>
          <p>The visual efficacy of an activity heatmap depends fundamentally on its color scaling algorithm. The human visual cortex perceives data through contrast differences. If the mapping between numeric activity counts and fill colors is mathematically flawed, the entire visualization fails to communicate meaningful insight.</p>

          <h3>3.1 The Failure of Linear Interpolation (The Power-Law Trap)</h3>
          <p>A common beginner mistake is applying linear color interpolation between the minimum value (0) and the maximum value (<em>V</em><sub>max</sub>):</p>

          <div class="formula-card">
            <div class="formula-title">Naive Linear Color Indexing (Anti-Pattern)</div>
            <div class="formula-body">Tier = Math.floor( ( V - 0 ) / ( V_max - 0 ) &times; 4 )</div>
            <div class="formula-desc">Produces severe visualization failure when data exhibits a heavy-tailed, Pareto, or log-normal distribution.</div>
          </div>

          <p>Consider real-world software development metrics: on typical active days, an engineer might make 1 to 4 commits. However, on one extraordinary day during a major release merge or code migration, the engineer might push 65 commits (<em>V</em><sub>max</sub> = 65). Under naive linear scaling:</p>
          <ul>
            <li>Tier 0 (Empty): 0 commits (Dark Charcoal #161B22)</li>
            <li>Tier 1: 1 to 16 commits (Pale Emerald #0E4429)</li>
            <li>Tier 2: 17 to 32 commits (Medium Green #006D32)</li>
            <li>Tier 3: 33 to 48 commits (Bright Green #26A641)</li>
            <li>Tier 4: 49 to 65 commits (Luminous Neon Lime #39D353)</li>
          </ul>

          <p>Under this linear scheme, a day with 3 commits and a day with 14 commits are both assigned to Tier 1, while Tiers 2, 3, and 4 remain completely unoccupied for 364 days of the year. The resulting heatmap appears completely flat and washed out, failing to convey the natural rhythm and variations in the developer's work habits.</p>

          <h3>3.2 Quantile &amp; Percentile Binning: The Production Solution</h3>
          <p>To eliminate this distortion, professional vector data engines implement <strong>Quantile Binning</strong>. Instead of dividing the range of values into equal numeric steps, quantile binning divides the sorted distribution of <em>active non-zero events</em> into equal statistical percentiles:</p>

          <div class="formula-card">
            <div class="formula-title">Quantile Percentile Threshold Formulations</div>
            <div class="formula-body">Active_Values = Sorted( [ V for V in Dataset if V &gt; 0 ] )<br>Q1 = Percentile( Active_Values, 25% )<br>Q2 = Percentile( Active_Values, 50% )  [Median]<br>Q3 = Percentile( Active_Values, 75% )</div>
            <div class="formula-desc">Guarantees that active days are distributed evenly across visual color tiers, maximizing visual entropy and data resolution.</div>
          </div>

          <p>Under quantile binning, the color tier assignment is evaluated using strict threshold boundaries:</p>

          <pre><code>// Production Quantile Color Binning Classifier
function getQuantileColorTier(value, thresholds, palette) {
  if (value === 0) return palette.empty; // Zero activity tier
  if (value &lt;= thresholds.q1) return palette.tier1;
  if (value &lt;= thresholds.q2) return palette.tier2;
  if (value &lt;= thresholds.q3) return palette.tier3;
  return palette.tier4; // Maximum intensity tier
}</code></pre>

          <h3>3.3 Perceptual Color Scales: GitHub Emerald, Turbo, Viridis &amp; Solar Amber</h3>
          <p>To ensure universal accessibility for users with color vision deficiencies (protanopia, deuteranopia, tritanopia), color scales must maintain monotonically increasing luminance (<em>L</em>*) in perceptual color spaces like CIELAB or Oklab. When a color scale increases in luminance as activity rises, colorblind users can immediately distinguish intensity even without perceiving hue.</p>

          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Color Palette Name</th>
                  <th>Tier 0 (Empty)</th>
                  <th>Tier 1 (Low)</th>
                  <th>Tier 2 (Medium)</th>
                  <th>Tier 3 (High)</th>
                  <th>Tier 4 (Peak)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>GitHub Classic Emerald</strong></td>
                  <td>#161B22</td>
                  <td>#0E4429</td>
                  <td>#006D32</td>
                  <td>#26A641</td>
                  <td>#39D353</td>
                </tr>
                <tr>
                  <td><strong>Cyberpunk Lime &amp; Cyan</strong></td>
                  <td>#111827</td>
                  <td>#064E3B</td>
                  <td>#047857</td>
                  <td>#10B981</td>
                  <td>#C1DD2D</td>
                </tr>
                <tr>
                  <td><strong>Plasma Violet &amp; Magenta</strong></td>
                  <td>#1A162B</td>
                  <td>#4A154B</td>
                  <td>#8B1E6F</td>
                  <td>#C026D3</td>
                  <td>#F472B6</td>
                </tr>
                <tr>
                  <td><strong>Solar Amber &amp; Flame</strong></td>
                  <td>#181512</td>
                  <td>#78350F</td>
                  <td>#B45309</td>
                  <td>#F59E0B</td>
                  <td>#FDE047</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <section id="declarative-svg-primitives">
          <h2>4. Declarative SVG Primitives: Instancing, Grids &amp; Rounded Rects</h2>
          <p>Having defined the coordinate projection mathematics and color quantization rules, we translate the matrix into declarative SVG markup. A modern calendar heatmap SVG canvas features three distinct visual layers:</p>
          <ol>
            <li><strong>Header &amp; Axis Label Layer:</strong> Horizontal text elements displaying month names, and vertical text elements marking Monday, Wednesday, and Friday.</li>
            <li><strong>Matrix Cell Layer:</strong> The 365+ individual calendar day <code>&lt;rect&gt;</code> elements, configured with subtle corner radii (<em>R</em> = 2px) and subpixel coordinate snapping.</li>
            <li><strong>Legend &amp; Metric Footer Layer:</strong> Summary metadata indicating total annual contributions, active streak counts, and a color legend showing the progression from "Less" to "More".</li>
          </ol>

          <pre><code>&lt;!-- Clean SVG Calendar Heatmap Structure --&gt;
&lt;svg viewBox="0 0 740 180" class="svg-calendar-heatmap" role="grid" aria-label="Annual Activity Matrix"&gt;
  &lt;!-- Month Labels (Top) --&gt;
  &lt;g class="month-labels" font-family="'Inter', sans-serif" font-size="11" fill="#737373"&gt;
    &lt;text x="32" y="16"&gt;Nov&lt;/text&gt;
    &lt;text x="88" y="16"&gt;Dec&lt;/text&gt;
    &lt;text x="144" y="16"&gt;Jan&lt;/text&gt;
    &lt;text x="200" y="16"&gt;Feb&lt;/text&gt;
    &lt;text x="256" y="16"&gt;Mar&lt;/text&gt;
    &lt;text x="312" y="16"&gt;Apr&lt;/text&gt;
    &lt;text x="368" y="16"&gt;May&lt;/text&gt;
    &lt;text x="424" y="16"&gt;Jun&lt;/text&gt;
    &lt;text x="480" y="16"&gt;Jul&lt;/text&gt;
    &lt;text x="536" y="16"&gt;Aug&lt;/text&gt;
    &lt;text x="592" y="16"&gt;Sep&lt;/text&gt;
    &lt;text x="648" y="16"&gt;Oct&lt;/text&gt;
  &lt;/g&gt;

  &lt;!-- Weekday Labels (Left) --&gt;
  &lt;g class="weekday-labels" font-family="'Inter', sans-serif" font-size="10" fill="#666" text-anchor="end"&gt;
    &lt;text x="26" y="44"&gt;Mon&lt;/text&gt;
    &lt;text x="26" y="72"&gt;Wed&lt;/text&gt;
    &lt;text x="26" y="100"&gt;Fri&lt;/text&gt;
  &lt;/g&gt;

  &lt;!-- Day Cell Matrix (52 Columns x 7 Rows) --&gt;
  &lt;g class="heatmap-cells"&gt;
    &lt;rect class="day-cell" x="32" y="32" width="11" height="11" rx="2" 
          fill="#161B22" data-date="2025-11-17" data-count="0" /&gt;
    &lt;rect class="day-cell" x="32" y="46" width="11" height="11" rx="2" 
          fill="#006D32" data-date="2025-11-18" data-count="5" /&gt;
    &lt;rect class="day-cell" x="32" y="60" width="11" height="11" rx="2" 
          fill="#39D353" data-date="2025-11-19" data-count="14" /&gt;
    &lt;!-- ... Remaining 362 Day Cells ... --&gt;
  &lt;/g&gt;

  &lt;!-- Metric Summary &amp; Legend Footer --&gt;
  &lt;g class="heatmap-footer" transform="translate(32, 145)"&gt;
    &lt;text x="0" y="10" font-family="'Inter', sans-serif" font-size="11.5" fill="#888"&gt;
      Learn how we count contributions
    &lt;/text&gt;
    &lt;g transform="translate(560, 0)"&gt;
      &lt;text x="-8" y="10" font-size="10" fill="#666" text-anchor="end"&gt;Less&lt;/text&gt;
      &lt;rect x="0" y="0" width="10" height="10" rx="2" fill="#161B22" /&gt;
      &lt;rect x="13" y="0" width="10" height="10" rx="2" fill="#0E4429" /&gt;
      &lt;rect x="26" y="0" width="10" height="10" rx="2" fill="#006D32" /&gt;
      &lt;rect x="39" y="0" width="10" height="10" rx="2" fill="#26A641" /&gt;
      &lt;rect x="52" y="0" width="10" height="10" rx="2" fill="#39D353" /&gt;
      &lt;text x="70" y="10" font-size="10" fill="#666"&gt;More&lt;/text&gt;
    &lt;/g&gt;
  &lt;/g&gt;
&lt;/svg&gt;</code></pre>

          <h3>4.1 CSS Pseudo-Classes &amp; Cell Hover Dynamics</h3>
          <p>Because SVG rect elements participate in the browser's CSS cascading style system, we can achieve high-fidelity micro-interactions with pure CSS. Applying a subtle stroke border and scale transform on hover creates an engaging interactive feel with zero JavaScript overhead. As explored in our benchmark on <a href="/articles/how-to-optimize-svg-icons-for-web-performance/">optimizing SVG performance for production web applications</a>, native vector elements eliminate heavyweight canvas runtime overhead:</p>

          <pre><code>/* Pure CSS Interactive Cell Styling */
.day-cell {
  transition: transform 120ms ease, stroke 120ms ease;
  transform-origin: center;
  cursor: pointer;
}

.day-cell:hover {
  stroke: #FFF;
  stroke-width: 1.5px;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.4));
  transform: scale(1.15);
}

.day-cell:focus-visible {
  outline: none;
  stroke: #C1DD2D;
  stroke-width: 2px;
}</code></pre>
        </section>

        <section id="interactive-tooltips-and-streaks">
          <h2>5. Zero-Lag Tooltips, Streak Engines &amp; HUD Telemetry</h2>
          <p>While visual colors indicate relative density, users demand exact numerical feedback when inspecting specific dates. A production activity matrix must provide a floating tooltip HUD that displays the exact date, total activity count, and contextual metrics (e.g. "Longest Streak: 42 days", "Current Streak: 15 days").</p>

          <h3>5.1 The Continuous Streak Calculation Algorithm</h3>
          <p>Streak tracking is one of the most psychologically engaging aspects of calendar heatmaps. The engine evaluates two streak metrics:</p>
          <ol>
            <li><strong>Current Active Streak:</strong> The number of consecutive days with activity (<em>V</em> &gt; 0) ending on today's date (or yesterday's date if today has not yet registered events).</li>
            <li><strong>Longest Historical Streak:</strong> The maximum unbroken run of consecutive active days recorded anywhere within the 365-day dataset.</li>
          </ol>

          <pre><code>// Continuous Activity Streak Analyzer
function calculateStreaks(calendarDays) {
  let longestStreak = 0;
  let currentStreak = 0;
  let tempStreak = 0;

  // Sort chronological order (oldest to newest)
  calendarDays.forEach((day, index) => {
    if (day.count > 0) {
      tempStreak++;
      if (tempStreak > longestStreak) {
        longestStreak = tempStreak;
      }
    } else {
      tempStreak = 0;
    }
  });

  // Calculate current active streak ending at final index
  for (let i = calendarDays.length - 1; i >= 0; i--) {
    if (calendarDays[i].count > 0) {
      currentStreak++;
    } else {
      // Allow a 1-day grace period for today if current hour is early
      if (i === calendarDays.length - 1) continue;
      break;
    }
  }

  return { longestStreak, currentStreak };
}</code></pre>

          <h3>5.2 High-Precision Floating Tooltip Positioning</h3>
          <p>To avoid clipping when a user hovers over cells near the top or right boundaries of the SVG container, the tooltip is rendered either as an absolute HTML overlay element or as a dynamic SVG <code>&lt;g id="tooltipGroup"&gt;</code> positioned via matrix transform. The tooltip computes horizontal and vertical clamp boundaries to ensure it remains 100% visible inside the viewport:</p>

          <div class="formula-card">
            <div class="formula-title">Tooltip Bounding Clamp Equation</div>
            <div class="formula-body">X_tip = Math.max(10, Math.min(W_viewport - W_tip - 10, X_cell - W_tip / 2))<br>Y_tip = ( Y_cell - H_tip - 8 &lt; 0 ) ? ( Y_cell + S_cell + 8 ) : ( Y_cell - H_tip - 8 )</div>
            <div class="formula-desc">Flips the tooltip below the cell if hovering along the top row, preventing out-of-bounds graphical clipping.</div>
          </div>
        </section>

        <!-- Figure 2: Dedicated Vector Architecture Diagram (960x320) -->
        <section id="architectural-pipeline-diagram">
          <h2>6. Architectural Pipeline: Raw Telemetry to Vector Matrix</h2>
          <p>The transformation of asynchronous event streams into a crisp, responsive SVG activity matrix follows a modular, five-stage architectural pipeline. Raw event payloads—whether originating from git commit logs, CI/CD deployment webhooks, or API rate limit sensors—flow through temporal normalization, statistical quantile classification, declarative SVG assembly, and GPU composition.</p>

          <figure class="article-figure">
            <svg viewBox="0 0 960 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#0D1117; border-radius:10px; border:1px solid #262626; display:block;">
              <defs>
                <linearGradient id="heatPipeGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#161B22"/>
                  <stop offset="100%" stop-color="#0E1217"/>
                </linearGradient>
                <linearGradient id="heatPipeGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#1A2210"/>
                  <stop offset="100%" stop-color="#0E150A"/>
                </linearGradient>
                <linearGradient id="heatPipeArrow" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#555"/>
                  <stop offset="100%" stop-color="#C1DD2D"/>
                </linearGradient>
                <filter id="heatPipeGlow" x="-10%" y="-10%" width="120%" height="120%">
                  <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="rgba(193,221,45,0.15)"/>
                </filter>
              </defs>

              <!-- Diagram Title -->
              <text x="30" y="36" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#FFF" letter-spacing="0.5">FIGURE 2: HIGH-PERFORMANCE SVG HEATMAP RENDERING PIPELINE</text>
              <text x="30" y="54" font-family="'JetBrains Mono', monospace" font-size="11" fill="#888">ARCHITECTURE: EVENT INGESTION &rarr; TEMPORAL BINNING &rarr; QUANTILE MAPPING &rarr; MATRIX ASSEMBLY</text>

              <!-- Stage 1: Event Log Ingestion -->
              <g transform="translate(30, 80)" filter="url(#heatPipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#heatPipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.12)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">01</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">Event Ingestion</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#888">Raw Event Streams</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Git Commit Logs</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; CI/CD Webhooks</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Server CPU Metrics</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Habit Activity Feeds</text>
              </g>

              <!-- Connector 1 -->
              <path d="M 190 177 L 220 177" stroke="url(#heatPipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="220,172 230,177 220,182" fill="#C1DD2D"/>

              <!-- Stage 2: Temporal Binning -->
              <g transform="translate(230, 80)" filter="url(#heatPipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#heatPipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.12)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">02</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">Temporal Binning</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#888">ISO 8601 Calendar Math</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; 365-Day Mapping</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; 7x52 Matrix Index</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Weekday Offsets</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Month Boundaries</text>
              </g>

              <!-- Connector 2 -->
              <path d="M 390 177 L 420 177" stroke="url(#heatPipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="420,172 430,177 420,182" fill="#C1DD2D"/>

              <!-- Stage 3: Quantile Color Scaling -->
              <g transform="translate(430, 80)" filter="url(#heatPipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#heatPipeGrad2)" stroke="#C1DD2D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.25)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">03</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">Color Quantization</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#C1DD2D">Statistical Percentiles</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="rgba(193,221,45,0.3)" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; Non-Zero Filtering</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; Q1 / Q2 / Q3 Cuts</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; Monotonic Luminance</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; Palette Token Maps</text>
              </g>

              <!-- Connector 3 -->
              <path d="M 590 177 L 620 177" stroke="url(#heatPipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="620,172 630,177 620,182" fill="#C1DD2D"/>

              <!-- Stage 4: SVG Vector Matrix Assembly -->
              <g transform="translate(630, 80)" filter="url(#heatPipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#heatPipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.12)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">04</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">SVG Synthesis</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#888">Batched DOM Layout</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Rect Instancing R=2</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Month Header Texts</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Legend Scale Tiers</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Subpixel Alignment</text>
              </g>

              <!-- Connector 4 -->
              <path d="M 790 177 L 820 177" stroke="url(#heatPipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="820,172 830,177 820,182" fill="#C1DD2D"/>

              <!-- Stage 5: Telemetry & Accessibility -->
              <g transform="translate(830, 80)" filter="url(#heatPipeGlow)">
                <rect width="100" height="195" rx="8" fill="url(#heatPipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <text x="14" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#C1DD2D">05. OUTPUT</text>
                <text x="14" y="65" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#FFF">HUD / Export</text>
                <text x="14" y="82" font-family="'Inter', sans-serif" font-size="10" fill="#888">Interactive UX</text>
                <line x1="10" y1="96" x2="90" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="10" y="120" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; Floating HUD</text>
                <text x="10" y="140" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; Streak Engine</text>
                <text x="10" y="160" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; ARIA Roles</text>
                <text x="10" y="180" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; SVG Export</text>
              </g>
            </svg>
            <figcaption>Figure 2: Complete multi-stage architectural pipeline of the SVG calendar heatmap engine: from raw developer commit log ingestion through temporal ISO binning, statistical quantile color scaling, declarative vector cell matrix generation, and interactive tooltip telemetry.</figcaption>
          </figure>
        </section>

        <section id="interactive-heatmap-studio">
          <h2>7. Interactive Developer Studio: Live Activity Heatmap Workbench</h2>
          <p>To demonstrate the real-time calendar projection math, quantile binning algorithms, and interactive hover mechanics detailed throughout this guide, test our production <strong>SVG Activity Heatmap Studio</strong>. This fully functional workbench renders 365 days of chronological telemetry in pure, dependency-free SVG, complete with interactive theme switching, cell size tuning, live streak calculation, and vector export.</p>

          <p>Experiment with the workbench using the following interactive controls:</p>
          <ul>
            <li><strong>Select Telemetry Preset:</strong> Switch between four real-world telemetry patterns: <em>GitHub 365-Day Dev Commits</em> (classic software engineering cadence), <em>DevOps CI/CD Deployments</em> (frequent micro-releases), <em>Server Cluster CPU Load</em> (continuous telemetry), and <em>API Gateway Traffic Matrix</em> (bursty web traffic).</li>
            <li><strong>Toggle Visual Palettes:</strong> Switch between four accessible color schemes: <em>GitHub Classic Emerald</em>, <em>Cyberpunk Lime &amp; Cyan</em>, <em>Plasma Violet &amp; Magenta</em>, and <em>Solar Amber &amp; Flame</em>.</li>
            <li><strong>Adjust Grid Geometry:</strong> Use the interactive sliders to adjust cell side length (10px to 14px) and corner radius (0px sharp to 5px circular), observing how the SVG matrix updates seamlessly without layout shifts.</li>
            <li><strong>Interactive Cell Hover HUD:</strong> Hover your mouse or touch pointer over any of the 365 calendar cells. The HUD instantly displays the date, total event count, and updates the active streak telemetry.</li>
            <li><strong>Export Vector Assets:</strong> Click "Copy SVG Markup" to copy the standalone SVG element directly to your clipboard, or click "Simulate New Year" to synthesize fresh probabilistic datasets.</li>
          </ul>

          <div class="interactive-sandbox" id="heatmapStudio">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                <span>Live Interactive SVG Activity Heatmap Studio</span>
              </div>
              <span class="sandbox-badge">Real-Time Vector Engine</span>
            </div>

            <div class="sandbox-grid">
              <div class="sandbox-controls">
                <div class="control-row">
                  <label for="heatmapPresetSelect">Telemetry Dataset Preset: <span class="stat-num" id="heatPresetBadge">GitHub Commits</span></label>
                  <select id="heatmapPresetSelect" class="control-select">
                    <option value="commits" selected>GitHub 365-Day Developer Commits</option>
                    <option value="deployments">DevOps CI/CD Production Deployments</option>
                    <option value="server_load">Server Cluster 24/7 Compute Load</option>
                    <option value="api_traffic">API Gateway Hourly Request Bursts</option>
                  </select>
                </div>

                <div class="control-row">
                  <label for="heatColorSelect">Color Palette &amp; Contrast:</label>
                  <select id="heatColorSelect" class="control-select">
                    <option value="emerald" selected>GitHub Classic Emerald</option>
                    <option value="cyberpunk">Cyberpunk Lime &amp; Cyan</option>
                    <option value="plasma">Plasma Violet &amp; Magenta</option>
                    <option value="solar">Solar Amber &amp; Flame</option>
                  </select>
                </div>

                <div class="control-row">
                  <label for="cellSizeRange">Cell Size (Pixels): <span class="stat-num" id="cellSizeVal">11 px</span></label>
                  <input type="range" id="cellSizeRange" min="9" max="14" value="11" step="1" class="control-input">
                </div>

                <div class="control-row">
                  <label for="cellRadiusRange">Cell Corner Radius (RX): <span class="stat-num" id="cellRadiusVal">2 px</span></label>
                  <input type="range" id="cellRadiusRange" min="0" max="5" value="2" step="1" class="control-input">
                </div>

                <div class="stats-readout-box">
                  <div class="stat-item">
                    <div class="stat-label">Total Events</div>
                    <div class="stat-val highlight" id="heatTotalEvents">1,842</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Longest Streak</div>
                    <div class="stat-val" id="heatLongestStreak">48 Days</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Active Days</div>
                    <div class="stat-val" id="heatActiveDays">245 / 365</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Inspected Cell</div>
                    <div class="stat-val highlight" id="heatHoverDate">Nov 15 (14)</div>
                  </div>
                </div>

                <div class="btn-row">
                  <button type="button" class="action-btn primary" id="btnCopyHeatmapSVG">Copy SVG Markup</button>
                  <button type="button" class="action-btn" id="btnSimulateYear">Simulate New Year</button>
                </div>

                <div class="control-row">
                  <label>Exported Vector Source (Live Snippet):</label>
                  <div class="code-preview-pane" id="heatCodePreview">&lt;!-- Initializing SVG Heatmap Engine... --&gt;</div>
                </div>
              </div>

              <div class="stage-wrapper">
                <div class="preview-stage-container" id="heatStageContainer">
                  <svg id="heatmapCanvas" class="stage-canvas-element" viewBox="0 0 740 180">
                    <!-- Injected dynamically by JavaScript -->
                  </svg>
                </div>
                <div style="font-size:12px; color:#777; text-align:center; font-family:'JetBrains Mono', monospace;">
                  Tip: Hover over any square to inspect date, events, and quantile tier.
                </div>
              </div>
            </div>
          </div>
        </section>

        <section id="timezone-and-temporal-normalization">
          <h2>8. Timezone Normalization, Daylight Saving Time &amp; Leap Year Robustness</h2>
          <p>A pervasive source of catastrophic visual bugs in calendar heatmaps stems from improper handling of timezones and Daylight Saving Time (DST) transitions. Because a calendar heatmap maps each day into a discrete slot based on calendar dates rather than continuous physical elapsed seconds, naive epoch timestamp division (such as dividing by 86,400,000 milliseconds) introduces subtle, cumulative timing drifts.</p>

          <p>On days when Daylight Saving Time begins or ends, a local calendar day contains either 23 hours (82,800,000 ms) or 25 hours (90,000,000 ms). If an engine naively adds 86,400,000 milliseconds to iterate to the subsequent day, the timestamp drifts by plus or minus one hour. Over the course of a 365-day year crossing two DST boundaries, this drift can cause consecutive days to collapse into the same calendar column or skip a day entirely, causing the entire heatmap matrix to misalign with weekday axis labels.</p>

          <p>To eliminate DST and timezone distortions, our architecture enforces two strict temporal normalization invariants:</p>
          <ul>
            <li><strong>UTC Date Normalization:</strong> All ingested timestamps are stripped of local timezone offsets and normalized into UTC midnights or parsed strictly using integer calendar tuples (Year, Month, Day). Date iteration is performed using native calendar date setter methods rather than raw millisecond additions.</li>
            <li><strong>Leap Year Quadrennial Auditing:</strong> During leap years, February contains 29 days, expanding the annual sequence to 366 days. In certain calendar configurations, this 366th day spills over into a 54th week column. The SVG rendering engine dynamically queries leap year calculations and adjusts the matrix viewBox width and column allocation dynamically, ensuring zero edge-clipping regardless of leap year boundaries.</li>
          </ul>
        </section>

        <section id="hourly-and-multi-dimensional-matrices">
          <h2>9. Hourly &amp; Multi-Dimensional Activity Matrices: 24&times;7 Server Punchcards</h2>
          <p>While the 52-week calendar grid is ideal for high-level longitudinal analysis, engineering teams frequently require micro-temporal density analysis to diagnose system performance and operational bottlenecks. A prominent variant of the activity matrix is the <strong>24&times;7 Punchcard Matrix</strong>, which maps the 24 hours of the day along the horizontal X-axis and the 7 days of the week along the vertical Y-axis. This produces a 168-cell matrix that illuminates intraday circadian rhythms, automated cron job resource spikes, global user traffic waves, and incident frequency distributions.</p>

          <p>In SVG, constructing an hourly punchcard matrix utilizes a similar coordinate projection to the calendar heatmap, but with circular or pill-shaped glyphs where both color intensity and element radius encode magnitude. By scaling the radius <em>R</em><sub>cell</sub> of each circle proportionally to the square root of activity (&radic;<em>V</em>), the visual area of the circle scales linearly with data magnitude, preventing large values from visually dominating the matrix.</p>

          <div class="formula-card">
            <div class="formula-title">Perceptual Area-Proportional Radius Formulation</div>
            <div class="formula-body">R(V) = R_min + [ \sqrt{V / V_max} ] &times; ( R_max - R_min )</div>
            <div class="formula-desc">Using the square root of event volume ensures that visual circle area is directly proportional to data value, avoiding geometric area distortion.</div>
          </div>

          <p>This dual-channel encoding—where fill color conveys quantile tier while radius conveys absolute volume—allows infrastructure engineers to instantly spot anomalies, such as a high-frequency database backup that runs silently every Tuesday at 03:00 UTC, consuming 92% of available IOPS.</p>
        </section>

        <section id="continuous-vs-stepped-quantization">
          <h2>10. Continuous Color Gradients vs. Stepped Perceptual Bins: Avoiding Mach Bands</h2>
          <p>When designing data visualizations, graphic designers often advocate for continuous linear color gradients, arguing that continuous gradients preserve subtle data nuances. However, in human perceptual psychology and information visualization theory, continuous color gradients on discrete matrix cells are widely recognized as an anti-pattern due to a neurological optical illusion known as <strong>Mach Bands</strong>.</p>

          <p>The human visual cortex employs lateral inhibition in the retina to enhance edge detection and contrast boundaries. When adjacent cells display smoothly varying shades of continuous color, the brain artificially exaggerates the contrast at the boundary between them, causing uniform regions to appear subtly concave or scalloped. Consequently, an observer cannot accurately compare two non-adjacent cells in a continuous gradient heatmap without experiencing perceptual distortion.</p>

          <p>Stepped quantile binning completely resolves this perceptual flaw. By quantizing values into a constrained set of 4 or 5 visually distinct, calibrated luminance steps, the brain processes each cell as a clear categorical state. Users can glance across the entire year and immediately categorize days into intuitive performance tiers (e.g. Inactive, Low, Normal, High, Peak), enabling reliable cognitive processing without visual fatigue.</p>
        </section>

        <section id="dynamic-svg-badge-generation">
          <h2>11. Automated SVG Badge Generation for Readmes &amp; Portfolios</h2>
          <p>One of the most popular applications of SVG activity heatmaps is dynamic GitHub profile badges and embedded project telemetry. Developers love showcasing live contribution streaks, code test coverage matrices, and deployment status grids directly inside their project README.md files.</p>

          <p>To deliver an SVG heatmap dynamically over HTTP, backend services (such as serverless Edge workers or Node.js microservices) must serialize the SVG DOM tree into a standalone, self-contained XML string and serve it with appropriate HTTP caching headers:</p>

          <pre><code>// Standalone SVG Heatmap Serialization &amp; HTTP Response Headers
export async function handleStreakBadgeRequest(request) {
  const username = new URL(request.url).searchParams.get('user') || 'octocat';
  const stats = await fetchUserTelemetry(username);
  
  // Synthesize pure standalone SVG
  const svgMarkup = generateStandaloneHeatmapSVG(stats);

  return new Response(svgMarkup, {
    status: 200,
    headers: {
      'Content-Type': 'image/svg+xml; charset=utf-8',
      'Cache-Control': 'public, max-age=3600, s-maxage=7200, stale-while-revalidate=86400',
      'Access-Control-Allow-Origin': '*',
      'X-Content-Type-Options': 'nosniff'
    }
  });
}</code></pre>

          <p>Notice the critical HTTP header configurations: setting <code>Content-Type: image/svg+xml</code> allows GitHub and web browsers to render the SVG directly inside an HTML <code>&lt;img&gt;</code> tag without triggering cross-origin script security restrictions. Furthermore, configuring <code>stale-while-revalidate</code> guarantees that profile visitors receive instantaneous cached responses from global CDN edge nodes while the server asynchronously refreshes activity metrics in the background.</p>
        </section>

        <section id="multi-year-and-performance">
          <h2>12. Multi-Year Scaling, DOM Optimization &amp; Subsetting</h2>
          <p>While an individual year's calendar heatmap contains 365 cells, enterprise analytics platforms often require multi-year historical profiles spanning 5 to 10 years of developer contributions, or dense hourly matrices containing 8,760 cells per year. In these data-dense configurations, unoptimized SVG DOM trees can cause memory pressure if handled naively.</p>

          <h3>11.1 Compound Path Merging for High-Density Matrices</h3>
          <p>For high-density matrices exceeding 1,000 cells, instead of creating individual <code>&lt;rect&gt;</code> elements, high-performance engines combine all cells belonging to the same color tier into a <strong>single compound SVG path</strong>. A matrix of 8,760 cells collapses into exactly <strong>five SVG DOM nodes</strong> (one path per color tier):</p>

          <pre><code>&lt;!-- Batched Compound Path: Entire Tier 4 in a Single Path Node --&gt;
&lt;path class="tier-4-cells" fill="#39D353" 
      d="M 32 46 h 11 v 11 h -11 Z M 74 60 h 11 v 11 h -11 Z M 116 32 h 11 v 11 h -11 Z" /&gt;</code></pre>

          <p>By using relative horizontal (<code>h W</code>) and vertical (<code>v H</code>) path commands, the compound string remains exceptionally compact, reducing the rendered DOM size by <strong>99.8%</strong> and enabling buttery-smooth 60 FPS scrolling even across massive ten-year engineering portfolios.</p>

          <h3>11.2 CSS Content Containment &amp; Virtualization</h3>
          <p>When rendering multi-year profile views, individual annual heatmaps should declare <code>contain: layout paint;</code> in their container CSS. This informs the browser's layout engine that modifications to one year's cells will never affect the layout boundaries of adjacent years, completely isolating reflow calculations.</p>
        </section>

        <section id="accessibility-and-screen-readers">
          <h2>13. Accessibility, WCAG 2.2 AA Compliance &amp; Keyboard Navigation</h2>
          <p>Enterprise compliance mandates that all data visualizations provide equitable access for individuals using assistive technologies. Canvas-based heatmaps almost universally fail accessibility audits because they lack semantic structure. Native SVG, by contrast, supports comprehensive WAI-ARIA grid ergonomics:</p>

          <pre><code>&lt;!-- Fully Accessible WAI-ARIA SVG Calendar Grid --&gt;
&lt;svg role="grid" aria-label="Jouni Flemming 2026 Developer Activity Heatmap" viewBox="0 0 740 180"&gt;
  &lt;!-- Accessible Weekday Row Group --&gt;
  &lt;g role="row" aria-label="Mondays"&gt;
    &lt;rect role="gridcell" tabindex="0" 
          aria-label="14 contributions on Monday, November 10, 2026"
          x="32" y="32" width="11" height="11" /&gt;
    &lt;!-- Additional Monday Cells --&gt;
  &lt;/g&gt;
&lt;/svg&gt;</code></pre>

          <p>Using the roving tabindex design pattern, keyboard users navigate seamlessly between cells using the four directional arrow keys (ArrowUp/ArrowDown to move between days of the week, ArrowLeft/ArrowRight to move between weeks), while screen readers announce the exact contribution tally and formatted date on each keystroke.</p>
        </section>

        <section id="faq-section" class="faq-block">
          <h2>14. Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3 class="faq-question">Why are SVG calendar heatmaps preferred over HTML table or Canvas implementations?</h3>
            <div class="faq-answer">Scalable Vector Graphics (SVG) provides the ideal balance between DOM ergonomics and rendering performance. Unlike heavy HTML tables that require hundreds of nested div, tr, and td tags with massive CSS box-model overhead, SVG renders 365 calendar days using lightweight rect elements within a single coordinate container. Furthermore, unlike HTML5 Canvas, SVG preserves the identity of each calendar day, enabling direct CSS pseudo-class hover effects, keyboard focus traversal, screen-reader ARIA labeling, and lossless vector export.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How do you project 365 calendar days into a 52-week horizontal SVG grid?</h3>
            <div class="faq-answer">The temporal projection uses ISO 8601 day-of-week and week-of-year calculations. For an active date D, the row index corresponds to its day of the week: row = (D.getDay() + 6) % 7 for Monday starts, or row = D.getDay() for Sunday starts. The column index is the number of full calendar weeks elapsed since the start of the 365-day range: col = Math.floor((dayOfYear + firstDayOffset) / 7). Coordinates are then evaluated as x = col * (cellSize + gap) and y = row * (cellSize + gap).</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">What is the difference between Linear and Quantile color scaling in activity heatmaps?</h3>
            <div class="faq-answer">Linear color scaling maps cell numeric values evenly across color bins: bin = Math.floor((val - min) / (max - min) * 4). In software engineering telemetry where a single outlier day might contain 80 commits while most days have 1 to 3 commits, linear scaling causes 95% of active days to fall into the lowest pale green bin. Quantile scaling sorts all positive non-zero activity values and calculates distribution percentiles (e.g. 25th, 50th, 75th), ensuring an aesthetically balanced and informative visual contrast across normal, busy, and peak days.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How do you position month labels accurately above the calendar columns in SVG?</h3>
            <div class="faq-answer">Month labels are positioned by iterating through all calendar days and detecting the first occurrence of each month. When day.getDate() === 1 (or the first day in the dataset for that month), the column index of that day is recorded: col = Math.floor(dayIndex / 7). An SVG text element is rendered at x = X_pad + col * (cellSize + gap) with text-anchor='start'. To prevent overlapping labels when a month spans fewer than 3 full columns, subsequent label collision thresholds are enforced.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How do you implement accessible keyboard navigation on an SVG activity heatmap?</h3>
            <div class="faq-answer">Accessible SVG heatmaps declare role='grid' on the container, role='row' on weekday groups, and role='gridcell' on individual rect elements. Each cell receives a descriptive aria-label, such as aria-label='24 contributions on Wednesday, November 11, 2026'. Using roving tabindex (setting tabindex='0' on the active cell and '-1' on all others), users navigate effortlessly across days and weeks using ArrowUp, ArrowDown, ArrowLeft, and ArrowRight keys.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How can multi-year or high-density hourly heatmaps be optimized in SVG?</h3>
            <div class="faq-answer">For high-density matrices (e.g. 8,760 hourly cells per year or 5-year multi-year displays), rendering thousands of discrete rect elements can increase memory consumption. Optimization strategies include batching all cells of the same color tier into single compound path elements using 'M x y h W v H h -W Z', applying CSS containment (contain: strict), and utilizing SVG <use> symbol cloning for identical cell geometry.</div>
          </div>
        </section>
      </article>

            <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <ol>
              <li><a href="#introduction-heatmap-paradigm">1. Temporal Density in UI</a></li>
              <li><a href="#calendar-grid-topology-math">2. ISO 8601 Calendar Math</a></li>
              <li><a href="#color-quantization-palettes">3. Color Quantization &amp; Palettes</a></li>
              <li><a href="#declarative-svg-primitives">4. Declarative SVG Primitives</a></li>
              <li><a href="#interactive-tooltips-and-streaks">5. Tooltips &amp; Streak Engine</a></li>
              <li><a href="#architectural-pipeline-diagram">6. Architectural Pipeline</a></li>
              <li><a href="#interactive-heatmap-studio">7. Interactive Developer Studio</a></li>
              <li><a href="#timezone-and-temporal-normalization">8. Timezone Normalization</a></li>
              <li><a href="#hourly-and-multi-dimensional-matrices">9. Hourly 24x7 Punchcard Matrices</a></li>
              <li><a href="#continuous-vs-stepped-quantization">10. Continuous vs Stepped Bins</a></li>
              <li><a href="#dynamic-svg-badge-generation">11. Automated Badge Generation</a></li>
              <li><a href="#multi-year-and-performance">12. Multi-Year Scaling &amp; DOM</a></li>
              <li><a href="#accessibility-and-screen-readers">13. Accessibility &amp; WCAG AA</a></li>
              <li><a href="#faq-section">14. Frequently Asked Questions</a></li>
            </ol>
          </nav>
        </div>

        <div class="cta-sidebar-box">
          <h4>Need Production Icons?</h4>
          <p>Access over 134,000+ optimized vector icons, customizable stroke weights, and instant React/SVG export.</p>
          <a href="/#/" class="cta-sidebar-btn">Search Free Icons</a>
        </div>
      </aside>
    </div>
  </div>

  <script>
    // Theme Toggle Handler
    const themeBtn = document.getElementById('themeToggle');
    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme') || 'dark';
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
      });
    }

    // Interactive Heatmap Studio Engine
    (function initHeatmapStudio() {
      const canvas = document.getElementById('heatmapCanvas');
      const presetSelect = document.getElementById('heatmapPresetSelect');
      const presetBadge = document.getElementById('heatPresetBadge');
      const colorSelect = document.getElementById('heatColorSelect');
      const sizeRange = document.getElementById('cellSizeRange');
      const sizeVal = document.getElementById('cellSizeVal');
      const radiusRange = document.getElementById('cellRadiusRange');
      const radiusVal = document.getElementById('cellRadiusVal');
      const btnCopy = document.getElementById('btnCopyHeatmapSVG');
      const btnSimulate = document.getElementById('btnSimulateYear');
      const codePreview = document.getElementById('heatCodePreview');

      const hudTotal = document.getElementById('heatTotalEvents');
      const hudStreak = document.getElementById('heatLongestStreak');
      const hudActive = document.getElementById('heatActiveDays');
      const hudHover = document.getElementById('heatHoverDate');

      let currentPreset = 'commits';
      let activePaletteKey = 'emerald';
      let cellSize = 11;
      let cellRadius = 2;
      const cellGap = 3;
      const xPad = 34;
      const yPad = 28;

      const palettes = {
        emerald: { empty: '#161B22', tier1: '#0E4429', tier2: '#006D32', tier3: '#26A641', tier4: '#39D353' },
        cyberpunk: { empty: '#111827', tier1: '#064E3B', tier2: '#047857', tier3: '#10B981', tier4: '#C1DD2D' },
        plasma: { empty: '#1A162B', tier1: '#4A154B', tier2: '#8B1E6F', tier3: '#C026D3', tier4: '#F472B6' },
        solar: { empty: '#181512', tier1: '#78350F', tier2: '#B45309', tier3: '#F59E0B', tier4: '#FDE047' }
      };

      // Generate 365 Days of Telemetry Data
      function generateAnnualTelemetry(preset) {
        const days = [];
        const endDate = new Date(2026, 10, 15); // Nov 15, 2026
        const startDate = new Date(endDate);
        startDate.setDate(endDate.getDate() - 364);

        let cur = new Date(startDate);
        for (let i = 0; i < 365; i++) {
          const dayOfWeek = cur.getDay(); // 0 is Sun, 6 is Sat
          const isWeekend = dayOfWeek === 0 || dayOfWeek === 6;
          let count = 0;

          if (preset === 'commits') {
            // Software engineering pattern: high weekday, lower weekend
            const prob = isWeekend ? 0.35 : 0.82;
            if (Math.random() < prob) {
              count = Math.floor(Math.random() * (isWeekend ? 5 : 12)) + 1;
              // Occasional heavy crunch burst
              if (Math.random() < 0.05) count += Math.floor(Math.random() * 20);
            }
          } else if (preset === 'deployments') {
            const prob = isWeekend ? 0.1 : 0.65;
            if (Math.random() < prob) {
              count = Math.floor(Math.random() * 6) + 1;
            }
          } else if (preset === 'server_load') {
            // Continuous compute load (high activity almost daily)
            count = Math.floor(Math.random() * 80 + 20);
          } else {
            // API traffic bursts
            count = Math.floor(Math.pow(Math.random(), 2) * 50);
          }

          days.push({
            date: new Date(cur),
            count: count,
            dayIndex: i
          });

          cur.setDate(cur.getDate() + 1);
        }
        return days;
      }

      let telemetryData = generateAnnualTelemetry(currentPreset);

      function calculateThresholds(data) {
        const nonZero = data.map(d => d.count).filter(c => c > 0).sort((a, b) => a - b);
        if (nonZero.length === 0) return { q1: 1, q2: 2, q3: 3 };
        const q1 = nonZero[Math.floor(nonZero.length * 0.25)] || 1;
        const q2 = nonZero[Math.floor(nonZero.length * 0.50)] || 2;
        const q3 = nonZero[Math.floor(nonZero.length * 0.75)] || 3;
        return { q1, q2, q3 };
      }

      function renderHeatmap() {
        if (!canvas) return;

        const palette = palettes[activePaletteKey];
        const thresholds = calculateThresholds(telemetryData);

        // Stats calculation
        let totalEvents = 0;
        let activeDaysCount = 0;
        let longestStreak = 0;
        let currentStreakRun = 0;

        telemetryData.forEach(d => {
          totalEvents += d.count;
          if (d.count > 0) {
            activeDaysCount++;
            currentStreakRun++;
            if (currentStreakRun > longestStreak) longestStreak = currentStreakRun;
          } else {
            currentStreakRun = 0;
          }
        });

        if (hudTotal) hudTotal.textContent = totalEvents.toLocaleString();
        if (hudStreak) hudStreak.textContent = `${longestStreak} Days`;
        if (hudActive) hudActive.textContent = `${activeDaysCount} / 365`;

        // Determine column and row for each day (Monday start)
        const firstDayOfWeek = (telemetryData[0].date.getDay() + 6) % 7; // 0=Mon, 6=Sun

        // Month Labels Calculation
        const monthHeaders = [];
        let currentMonth = -1;
        telemetryData.forEach((d, idx) => {
          const m = d.date.getMonth();
          if (m !== currentMonth) {
            const col = Math.floor((idx + firstDayOfWeek) / 7);
            const x = xPad + col * (cellSize + cellGap);
            monthHeaders.push({
              name: d.date.toLocaleDateString('en-US', { month: 'short' }),
              x: x
            });
            currentMonth = m;
          }
        });

        // Total width and height calculation
        const totalCols = Math.ceil((365 + firstDayOfWeek) / 7);
        const totalW = xPad + totalCols * (cellSize + cellGap) + 20;
        const totalH = yPad + 7 * (cellSize + cellGap) + 36;

        canvas.setAttribute('viewBox', `0 0 ${totalW} ${totalH}`);

        let svg = `
          <!-- Month Labels -->
          <g class="month-labels" font-family="'Inter', sans-serif" font-size="10.5" fill="#737373">
        `;
        monthHeaders.forEach(mh => {
          svg += `<text x="${mh.x}" y="${yPad - 10}">${mh.name}</text>`;
        });
        svg += `</g>`;

        // Weekday Labels (Mon, Wed, Fri)
        svg += `
          <g class="weekday-labels" font-family="'Inter', sans-serif" font-size="9.5" fill="#666" text-anchor="end">
            <text x="${xPad - 8}" y="${yPad + 0 * (cellSize + cellGap) + cellSize - 2}">Mon</text>
            <text x="${xPad - 8}" y="${yPad + 2 * (cellSize + cellGap) + cellSize - 2}">Wed</text>
            <text x="${xPad - 8}" y="${yPad + 4 * (cellSize + cellGap) + cellSize - 2}">Fri</text>
          </g>
          <g class="cells-layer">
        `;

        // Render Day Cells
        telemetryData.forEach((d, idx) => {
          const linearPos = idx + firstDayOfWeek;
          const col = Math.floor(linearPos / 7);
          const row = linearPos % 7;
          const x = xPad + col * (cellSize + cellGap);
          const y = yPad + row * (cellSize + cellGap);

          let color = palette.empty;
          if (d.count > 0) {
            if (d.count <= thresholds.q1) color = palette.tier1;
            else if (d.count <= thresholds.q2) color = palette.tier2;
            else if (d.count <= thresholds.q3) color = palette.tier3;
            else color = palette.tier4;
          }

          const dateStr = d.date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
          svg += `
            <rect class="day-cell" data-idx="${idx}" data-date="${dateStr}" data-count="${d.count}"
                  x="${x}" y="${y}" width="${cellSize}" height="${cellSize}" rx="${cellRadius}" fill="${color}"
                  style="cursor:pointer;" />
          `;
        });
        svg += `</g>`;

        // Footer Legend
        const legendX = totalW - 130;
        const legendY = totalH - 12;
        svg += `
          <g class="legend-footer" transform="translate(${legendX}, ${legendY})">
            <text x="-6" y="8" font-family="'Inter', sans-serif" font-size="9.5" fill="#666" text-anchor="end">Less</text>
            <rect x="0" y="0" width="8" height="8" rx="1.5" fill="${palette.empty}"/>
            <rect x="11" y="0" width="8" height="8" rx="1.5" fill="${palette.tier1}"/>
            <rect x="22" y="0" width="8" height="8" rx="1.5" fill="${palette.tier2}"/>
            <rect x="33" y="0" width="8" height="8" rx="1.5" fill="${palette.tier3}"/>
            <rect x="44" y="0" width="8" height="8" rx="1.5" fill="${palette.tier4}"/>
            <text x="56" y="8" font-family="'Inter', sans-serif" font-size="9.5" fill="#666">More</text>
          </g>
        `;

        canvas.innerHTML = svg;

        // Hover Event Delegation
        const cellNodes = canvas.querySelectorAll('.day-cell');
        cellNodes.forEach(c => {
          c.addEventListener('mouseenter', () => {
            const dateStr = c.getAttribute('data-date');
            const count = c.getAttribute('data-count');
            if (hudHover) hudHover.textContent = `${dateStr} (${count})`;
            c.setAttribute('stroke', '#FFF');
            c.setAttribute('stroke-width', '1.5');
          });
          c.addEventListener('mouseleave', () => {
            c.removeAttribute('stroke');
            c.removeAttribute('stroke-width');
          });
        });

        // Update Code Snippet Preview
        if (codePreview) {
          const sample = `<svg viewBox="0 0 ${totalW} ${totalH}" xmlns="http://www.w3.org/2000/svg">\n  <!-- Generated Heatmap Matrix -->\n  <rect x="34" y="28" width="${cellSize}" height="${cellSize}" rx="${cellRadius}" fill="${palette.tier3}"/>\n  <rect x="34" y="42" width="${cellSize}" height="${cellSize}" rx="${cellRadius}" fill="${palette.tier1}"/>\n</svg>`;
          codePreview.textContent = sample;
        }
      }

      // Event Listeners for Controls
      if (presetSelect) {
        presetSelect.addEventListener('change', (e) => {
          currentPreset = e.target.value;
          presetBadge.textContent = e.target.options[e.target.selectedIndex].text.split(' ')[0];
          telemetryData = generateAnnualTelemetry(currentPreset);
          renderHeatmap();
        });
      }

      if (colorSelect) {
        colorSelect.addEventListener('change', (e) => {
          activePaletteKey = e.target.value;
          renderHeatmap();
        });
      }

      if (sizeRange) {
        sizeRange.addEventListener('input', (e) => {
          cellSize = parseInt(e.target.value, 10);
          if (sizeVal) sizeVal.textContent = `${cellSize} px`;
          renderHeatmap();
        });
      }

      if (radiusRange) {
        radiusRange.addEventListener('input', (e) => {
          cellRadius = parseInt(e.target.value, 10);
          if (radiusVal) radiusVal.textContent = `${cellRadius} px`;
          renderHeatmap();
        });
      }

      if (btnSimulate) {
        btnSimulate.addEventListener('click', () => {
          telemetryData = generateAnnualTelemetry(currentPreset);
          renderHeatmap();
        });
      }

      function copyToClipboard(text, onSuccess) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(onSuccess).catch(() => {
            execCommandFallback(text, onSuccess);
          });
        } else {
          execCommandFallback(text, onSuccess);
        }
      }

      function execCommandFallback(text, onSuccess) {
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try {
          document.execCommand('copy');
          if (onSuccess) onSuccess();
        } catch (err) {
          alert('Copied SVG markup to clipboard');
        }
        document.body.removeChild(ta);
      }

      if (btnCopy) {
        btnCopy.addEventListener('click', () => {
          if (canvas) {
            copyToClipboard(canvas.outerHTML, () => {
              const orig = btnCopy.textContent;
              btnCopy.textContent = 'Copied to Clipboard!';
              setTimeout(() => { btnCopy.textContent = orig; }, 1800);
            });
          }
        });
      }

      // Initial Render
      renderHeatmap();
    })();
  </script>
</body>
</html>
'''

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {target_file} ({len(html_content)} bytes)")
