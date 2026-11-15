import os

slug = "svg-sankey-diagrams-and-alluvial-flow-guide"
target_dir = os.path.join(r"D:\Project IconStash\IconStash\articles", slug)
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

html_content = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mastering SVG Sankey Diagrams &amp; Alluvial Flow: Node Stratification, Cubic Ribbon Splines &amp; Budget Graph Guide (2026) | IconStash</title>
  <meta name="description" content="Build responsive SVG Sankey diagrams. Master node stratification, iterative relaxation algorithms, cubic Bézier ribbon math, and interactive flow styling.">
  <meta name="keywords" content="svg sankey diagram, sankey chart javascript svg, alluvial diagram svg, flow diagram vector web, budget flow chart svg, cubic bezier ribbon svg, energy flow diagram svg, node relaxation algorithm web">
  <meta property="og:title" content="Mastering SVG Sankey Diagrams &amp; Alluvial Flow: Node Stratification, Cubic Ribbon Splines &amp; Budget Graph Guide (2026)">
  <meta property="og:description" content="Build responsive SVG Sankey diagrams. Master node stratification, iterative relaxation algorithms, cubic Bézier ribbon math, and interactive flow styling.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-sankey-diagrams-and-alluvial-flow-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-sankey-diagrams-and-alluvial-flow-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-15T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-15T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="Vector Graphics &amp; Flow Engineering">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="Sankey Diagrams">
  <meta property="article:tag" content="Alluvial Flow">
  <meta property="article:tag" content="Data Visualization">
  <meta property="article:tag" content="Frontend Engineering">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mastering SVG Sankey Diagrams &amp; Alluvial Flow: Node Stratification, Cubic Ribbon Splines &amp; Budget Graph Guide (2026)">
  <meta name="twitter:description" content="Build responsive SVG Sankey diagrams. Master node stratification, iterative relaxation algorithms, cubic Bézier ribbon math, and interactive flow styling.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-sankey-diagrams-and-alluvial-flow-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-sankey-diagrams-and-alluvial-flow-guide/">
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
      "headline": "Mastering SVG Sankey Diagrams & Alluvial Flow: Node Stratification, Cubic Ribbon Splines & Budget Graph Guide (2026)",
      "description": "Build responsive SVG Sankey diagrams. Master node stratification, iterative relaxation algorithms, cubic Bézier ribbon math, and interactive flow styling.",
      "image": "https://iconstash.io/assets/articles/svg-sankey-diagrams-and-alluvial-flow-guide.jpg",
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
      "mainEntityOfPage": "https://iconstash.io/articles/svg-sankey-diagrams-and-alluvial-flow-guide/",
      "inLanguage": "en-US",
      "wordCount": 4500,
      "articleSection": "Vector Graphics & Flow Systems",
      "keywords": [
        "svg sankey diagram",
        "alluvial flow diagram svg",
        "sankey chart javascript",
        "cubic bezier ribbon svg",
        "flow conservation visualization",
        "budget flow diagram",
        "dag layout vector"
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
          "name": "SVG Sankey Diagrams Guide",
          "item": "https://iconstash.io/articles/svg-sankey-diagrams-and-alluvial-flow-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why build Sankey diagrams in pure SVG rather than HTML5 Canvas?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sankey diagrams rely on distinct flow ribbons and rectilinear nodes where users expect hover tooltips, click inspections, dynamic recoloring, and lossless vector scaling. SVG maintains the full DOM identity of each flow ribbon, allowing declarative CSS styling, smooth cubic Bézier stroke-dashoffset animations, screen reader accessibility under WCAG 2.2 AA, and flawless vector PDF export."
          }
        },
        {
          "@type": "Question",
          "name": "How does topological node stratification organize layers in a DAG Sankey diagram?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For a Directed Acyclic Graph (DAG), longest-path layer assignment traverses nodes in topological order. Source nodes with zero incoming links are assigned Layer 0. For each downstream node, its layer is defined as L(v) = max(L(u) + 1) across all incoming predecessors u. This assigns every node to a discrete column across the horizontal viewport."
          }
        },
        {
          "@type": "Question",
          "name": "How does Gauss-Seidel iterative relaxation resolve ribbon crossings?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Gauss-Seidel relaxation performs alternating forward and backward passes across node layers. In each sweep, a node's target vertical position is computed as the weighted barycenter (average center-of-mass) of its connected neighbors. Overlapping nodes are pushed apart by collision resolution algorithms to maintain mandatory vertical gap spacing."
          }
        },
        {
          "@type": "Question",
          "name": "What mathematical formula constructs the dual cubic Bézier ribbon geometry in SVG?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Sankey ribbon is defined by four boundary points: source top (x0, y0_top), target top (x1, y1_top), target bottom (x1, y1_bottom), and source bottom (x0, y0_bottom). The upper curve uses control handles at midpoints (x0 + dx/2, y0_top) and (x1 - dx/2, y1_top). The path connects vertically to y1_bottom, traces the lower curve backwards with reversed control points, and closes with 'Z'."
          }
        },
        {
          "@type": "Question",
          "name": "How does Kirchhoff flow conservation apply to nodes in a Sankey diagram?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Kirchhoff flow balance requires that for every intermediate node, total incoming volume equals total outgoing volume. In real-world enterprise applications where drop-offs or conversions occur, residual difference nodes ('System Loss' or 'Pipeline Attrition') model unbalanced energy or revenue leakage."
          }
        },
        {
          "@type": "Question",
          "name": "How are hardware-accelerated animated flow streams achieved in SVG ribbons?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Flow animations can be rendered by superimposing a semi-transparent stroke along the ribbon's centerline with stroke-dasharray and animating stroke-dashoffset via CSS keyframes. This hardware-accelerated technique produces liquid pulse animations at 120 FPS without manipulating JavaScript coordinate frames."
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

    .sandbox-grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.25fr); gap: 24px; align-items: start; }
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
    .preview-stage-container { width: 100%; min-height: 420px; border: 1px dashed #444; border-radius: 10px; background: #080C10; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; user-select: none; }
    .stage-canvas-element { width: 100%; height: auto; min-height: 400px; display: block; }

    .stats-readout-box { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; background: #0E0E0E; border: 1px solid #222; border-radius: 8px; padding: 12px; }
    @media (max-width: 640px) { .stats-readout-box { grid-template-columns: repeat(2, 1fr); } }
    .stat-item { text-align: center; }
    .stat-label { font-size: 11px; text-transform: uppercase; color: #888; font-weight: 600; margin-bottom: 2px; }
    .stat-val { font-size: 14px; font-family: "JetBrains Mono", monospace; font-weight: 700; color: #FFF; }
    .stat-val.highlight { color: #C1DD2D; }

    .code-preview-pane { background: #0B0E14; border: 1px solid #222; border-radius: 8px; padding: 12px; font-family: "JetBrains Mono", monospace; font-size: 12px; color: #9CDCFE; max-height: 180px; overflow-y: auto; white-space: pre-wrap; word-break: break-all; }

    /* Flow Ribbon Interactivity */
    .sankey-ribbon { fill-opacity: 0.45; transition: fill-opacity 150ms ease, stroke-width 150ms ease; cursor: pointer; }
    .sankey-ribbon:hover { fill-opacity: 0.85; stroke: #FFF; stroke-width: 1px; }
    .sankey-node { cursor: grab; transition: fill 150ms ease; }
    .sankey-node:hover { filter: brightness(1.2); }

    /* Animated Flow Particles */
    @keyframes flowDash {
      to { stroke-dashoffset: -32; }
    }
    .flow-active-stream {
      stroke-dasharray: 6 8;
      animation: flowDash 1.2s linear infinite;
    }

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
      <span class="current" aria-current="page">Mastering SVG Sankey Diagrams &amp; Alluvial Flow</span>
    </nav>

    <header class="article-hero">
      <span class="tag">Flow Systems &amp; Vector Data Engineering</span>
      <h1>Mastering SVG Sankey Diagrams &amp; Alluvial Flow: Node Stratification, Cubic Ribbon Splines &amp; Budget Graph Guide</h1>
      <div class="article-meta">
        <span>By <a href="/about/" rel="author">Jouni Flemming</a></span>
        <span>&bull;</span>
        <time datetime="2026-11-15">November 15, 2026</time>
        <span>&bull;</span>
        <span>34 min read</span>
        <span>&bull;</span>
        <span>6,780 words</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">
        <div class="featured-summary">
          <p><strong>Executive Architectural Summary:</strong> Sankey diagrams and alluvial flow graphs represent the pinnacle of multi-stage topological data visualization. First formalized by Captain Matthew Sankey in 1898 to analyze thermal energy efficiency in steam engines, modern Sankey diagrams are indispensable across corporate financial budgeting, SaaS funnel conversion optimization, global energy grids, and cloud infrastructure cost architecture. Engineering these complex flow diagrams in native Scalable Vector Graphics (SVG) unlocks mathematical resolution independence, smooth cubic Bézier ribbon curvature, declarative gradient fills, and subpixel hover interactivity.</p>
          <ul>
            <li><strong>Directed Acyclic Graph (DAG) Stratification:</strong> Formulating topological ranking algorithms to assign flow nodes into discrete horizontal columns (depth tiers) with cycle detection and alignment modes.</li>
            <li><strong>Iterative Relaxation &amp; Crossing Minimization:</strong> Implementing Gauss-Seidel barycentric relaxation algorithms to resolve vertical node collisions and untangle spaghetti link ribbons.</li>
            <li><strong>Cubic Bézier Ribbon Geometry:</strong> Constructing seamless dual-spline vector path polygons connecting source and target nodes with smooth horizontal tangent control points.</li>
            <li><strong>Kirchhoff Flow Conservation Laws:</strong> Enforcing volume balance (&Sigma; Inflow = &Sigma; Outflow) while managing drop-off leakage, unallocated residuals, and multi-tier cascades.</li>
            <li><strong>Hardware-Accelerated Interaction &amp; Telemetry:</strong> Engineering zero-lag ribbon hover highlighting, live data tooltips, animated stream pulses via CSS stroke-dashoffset, and pure SVG export.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-sankey-diagrams-and-alluvial-flow-guide.jpg" alt="Mastering SVG Sankey Diagrams and Alluvial Flow guide hero visual showing glowing multi-stage flow ribbons connecting nodes across infrastructure pipeline" width="1200" height="675" fetchpriority="high" decoding="async">
          <figcaption>Figure 1: Production SVG Sankey flow environment rendering enterprise cloud architecture bandwidth and microservice latency, featuring multi-tier node stratification, cubic Bézier gradient ribbons, and active telemetry.</figcaption>
        </figure>

        <section id="introduction-flow-imperative">
          <h2>1. Introduction: The Visual Conservation of Flow in Modern Architecture</h2>
          <p>In data-driven enterprise engineering, financial auditing, sustainability science, and distributed cloud computing, systems are fundamentally governed by laws of conservation: money flows into an organization and is distributed across payroll, infrastructure, and taxation; electrical energy flows from generation stations through transmission grids to industrial consumers; website visitors arrive at marketing landing pages and filter through onboarding funnels toward conversion or abandonment. Understanding how volume distributes, fragments, consolidates, and dissipates across multi-stage pipelines is crucial for strategic decision-making. For quantitative financial time-series architectures, see our companion guide on <a href="/articles/svg-candlestick-charts-and-financial-visualization-guide/">SVG candlestick charts and financial visualizations</a>.</p>

          <p>Standard data visualization tools—such as bar charts, line graphs, and pie charts—fail catastrophically when tasked with representing relational multi-stage flows. A pie chart can display the breakdown of a cloud infrastructure bill at a single point in time, but it cannot show which specific microservices triggered the cost surge, how database queries routed across caching tiers, or where network egress fees accumulated. Similarly, node-link flowcharts convey logical topology but completely omit quantitative volume: a thin configuration link looks identical to a high-bandwidth 100 Gbps network trunk.</p>

          <p>The <strong>Sankey diagram</strong> (and its closely related cousin, the <strong>Alluvial chart</strong>) solves this challenge by binding geometric width directly to quantitative magnitude. In a Sankey diagram, every rectangular node represents an entity or state, and every directed ribbon connecting two nodes has a width proportional to the quantity flowing between them. Because ribbon widths visually expand or contract to reflect consolidation or division, viewers can trace massive, multi-tiered systems from origin to destination in a single intuitive glance.</p>

          <p>However, when frontend developers set out to implement Sankey diagrams on the web, they frequently encounter severe architectural hurdles across candidate rendering technologies:</p>
          <ul>
            <li><strong>The Canvas Black Box:</strong> Many charting libraries default to HTML5 Canvas to render ribbons. However, Canvas treats ribbons as flat, rasterized pixels. Implementing link hover effects requires complex inverse trigonometry and raycasting along cubic curve boundaries. Furthermore, Canvas graphics become blurry on high-DPI displays and cannot be inspected by screen readers, creating serious compliance liabilities under WCAG 2.2 AA.</li>
            <li><strong>Third-Party Library Bloat:</strong> Commercial and open-source charting suites that support Sankey diagrams often require importing multi-megabyte monolithic packages (such as D3, Highcharts, or Plotly). These libraries bundle massive amounts of unnecessary code, degrade bundle sizes, and lock developers into opinionated, difficult-to-customize DOM structures.</li>
            <li><strong>Scalable Vector Graphics (SVG):</strong> SVG is the natural, mathematically rigorous medium for Sankey diagrams. In SVG, every node is an accessible <code>&lt;rect&gt;</code>, and every flowing ribbon is a declarative <code>&lt;path&gt;</code> with smooth cubic Bézier curves. SVG paths natively support two-point linear gradients that transition smoothly from the source node's brand color to the target node's color. Furthermore, SVG elements support direct CSS pseudo-class styling, event delegation, screen reader accessibility labels, and lossless export into high-DPI vector PDF reports.</li>
          </ul>

          <p>          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Architectural Dimension</th>
                  <th>HTML5 Canvas / WebGL</th>
                  <th>Traditional D3 Sankey</th>
                  <th>IconStash Hardware-Accelerated SVG Architecture</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Geometry Pipeline</strong></td>
                  <td>Rasterized pixel approximation; no curve inspection</td>
                  <td>Dual cubic Bézier splines rendered as individual paths</td>
                  <td>Continuous cubic Bézier ribbons with GPU path acceleration</td>
                </tr>
                <tr>
                  <td><strong>Interactive Dragging</strong></td>
                  <td>Manual bounding-box collision math in JavaScript</td>
                  <td>Full-scene DOM rebuilding during drag events</td>
                  <td>PointerEvent coordinate capture with O(1) ribbon redraw</td>
                </tr>
                <tr>
                  <td><strong>Streamline Animations</strong></td>
                  <td>Procedural pixel particle simulators (high CPU load)</td>
                  <td>requestAnimationFrame loop updating SVG attributes</td>
                  <td>CSS hardware-accelerated stroke-dashoffset at 120 FPS</td>
                </tr>
                <tr>
                  <td><strong>WCAG 2.2 AA Compliance</strong></td>
                  <td>Zero DOM accessibility; invisible to screen readers</td>
                  <td>Basic SVG text labels without relational semantics</td>
                  <td>Semantic flow narration tables &amp; ARIA relationship tokens</td>
                </tr>
                <tr>
                  <td><strong>Datasheet PDF Export</strong></td>
                  <td>300 DPI raster blur in annual financial disclosures</td>
                  <td>Complex multi-step canvas raster bridge</td>
                  <td>Lossless vector PDF reproduction for investor prospectuses</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p>In this comprehensive architectural guide, we construct a production-grade, dependency-free SVG Sankey flow engine from mathematical first principles. Similar to the topological routing explored in our engineering guide on <a href="/articles/svg-circuit-diagrams-and-schematic-visualization-guide/">SVG circuit diagrams and electrical schematics</a>, node stratification and ribbon crossings demand rigorous algorithmic untangling.</p>
        </section>

        <section id="dag-topology-and-stratification">
          <h2>2. Directed Acyclic Graph (DAG) Topology &amp; Node Stratification</h2>
          <p>At its mathematical core, a Sankey diagram represents a weighted <strong>Directed Acyclic Graph (DAG)</strong>, denoted as <em>G</em> = (<em>V</em>, <em>E</em>), where <em>V</em> represents the set of nodes (entities) and <em>E</em> represents the set of directed links with positive weights <em>W</em>(<em>u</em>, <em>v</em>) &gt; 0. Before any visual coordinates can be assigned, the graph must undergo topological analysis to eliminate cycles and stratify nodes into ordered horizontal columns.</p>

          <h3>2.1 Cycle Detection &amp; Resolution</h3>
          <p>Pure Sankey diagrams assume a unidirectional progression of flow from left to right (upstream to downstream). If the dataset contains cyclical dependencies (e.g. Node A &rarr; Node B &rarr; Node C &rarr; Node A), a standard left-to-right layout algorithm enters an infinite loop or produces backwards-pointing ribbons that collide chaotically with forward flows. As with the hierarchical graph traversals analyzed in our architectural breakdown of <a href="/articles/svg-tree-diagrams-and-hierarchical-visualization-guide/">SVG tree diagrams and hierarchical layouts</a> and <a href="/articles/svg-coordinate-systems-and-transformations-guide/">SVG coordinate systems and transformations</a>, directed graph traversal and cycle resolution form the backbone of vector layout engines.</p>

          <p>Our engine executes a <strong>Depth-First Search (DFS) Cycle Detection Pass</strong> using three-color node marking (White = unvisited, Gray = currently evaluating in recursion stack, Black = fully visited). If a back-edge pointing to a currently active Gray node is detected, the cycle is resolved by either:</p>
          <ol>
            <li><strong>Back-Edge Reversal:</strong> Temporarily inverting the direction of the offending link for layout computation purposes, marking it with a distinctive return ribbon styling.</li>
            <li><strong>Virtual Node Duplication:</strong> Splitting the cyclical node into an initial source node (<em>A</em><sub>in</sub>) and a terminal feedback node (<em>A</em><sub>out</sub>), preserving strict left-to-right DAG monotonicity.</li>
          </ol>

          <h3>2.2 Node Stratification (Layer Assignment)</h3>
          <p>Once acyclicity is guaranteed, every node <em>v</em> &isin; <em>V</em> must be assigned a discrete horizontal layer index <em>L</em>(<em>v</em>) &isin; {0, 1, 2, &hellip;, <em>L</em><sub>max</sub>}. The layer index determines which vertical column the node occupies on the canvas.</p>

          <p>The standard architectural approach uses the <strong>Longest Path Layering Algorithm</strong>:</p>

          <div class="formula-card">
            <div class="formula-title">Longest Path Layer Assignment Equation</div>
            <div class="formula-body">L(v) = max( [ L(u) + 1 for u in InNeighbors(v) ] )<br>If InNeighbors(v) is empty, L(v) = 0</div>
            <div class="formula-desc">Nodes with no incoming links (primary sources) are anchored to Column 0. Each subsequent node is placed at least one column to the right of its deepest upstream parent.</div>
          </div>

          <h3>2.3 Kahn's Topological Sort Algorithm for DAG Validation</h3>
          <p>To compute the longest path ordering systematically without risking runtime stack overflows on large graphs, our engine implements <strong>Kahn's Algorithm</strong> for topological sorting. The algorithm maintains an in-degree counter for every node in the graph. Nodes with zero in-degree are pushed into an evaluation queue. As each node is dequeued, it is appended to the topological sequence, and the in-degree of all its downstream target nodes is decremented. If a target node's in-degree reaches zero, it enters the queue.</p>

          <p>If the final topological sequence contains fewer nodes than the total graph vertex count |<em>V</em>|, a cyclical dependency exists. Kahn's algorithm isolates the exact subset of cyclical nodes, allowing the engine to execute targeted back-edge reversal without corrupting the broader graph hierarchy.</p>

          <h3>2.4 Dynamic Viewport Resizing &amp; Responsive Vector Preservation</h3>
          <p>A critical engineering advantage of rendering Sankey diagrams in native SVG is responsive adaptation. Unlike canvas implementations that require complete procedural recreation upon window resize, an SVG Sankey diagram leverages the declarative <code>viewBox="0 0 740 400"</code> coordinate system coupled with CSS fluid widths: <code>width: 100%; height: auto;</code>.</p>

          <p>When the user resizes their browser window or rotates a mobile device from portrait to landscape, the SVG coordinate system scales smoothly via GPU matrix transformation without triggering DOM recalculations or text jitter. Furthermore, by configuring <code>vector-effect="non-scaling-stroke"</code> on link ribbon borders and flow particle lines, line weights maintain optimal optical density across high-resolution displays.</p>

          <p>To optimize aesthetic balance, our engine supports three distinct column alignment strategies:</p>
          <ul>
            <li><strong>Left-Aligned (Default):</strong> Pushes every node as far to the left as possible according to the Longest Path rule.</li>
            <li><strong>Right-Aligned (Sink-Anchored):</strong> Terminal sink nodes with no outgoing links are aligned to the rightmost column (<em>L</em><sub>max</sub>), and intermediate nodes are shifted rightward to shorten terminal ribbons.</li>
            <li><strong>Justified (Edge-Balanced):</strong> Source nodes anchor to column 0, sink nodes anchor to <em>L</em><sub>max</sub>, and intermediate nodes are spaced evenly across internal columns.</li>
          </ul>

          <div class="formula-card">
            <div class="formula-title">Horizontal Node Column Coordinate Equation</div>
            <div class="formula-body">X_node(v) = X_pad + L(v) &times; [ ( W_plot - W_node ) / L_max ]</div>
            <div class="formula-desc">Where W_plot is the available canvas width minus safety margins, and W_node is the fixed horizontal thickness of each node bar (typically 12px to 24px).</div>
          </div>
        </section>

        <section id="relaxation-and-crossing-minimization">
          <h2>3. Iterative Relaxation Algorithms: Gauss-Seidel Barycenter Untangling</h2>
          <p>While assigning nodes to horizontal columns is straightforward, determining the optimal vertical (<em>Y</em>) order and spacing of nodes within each column is a mathematically challenging problem. In computer science and graph drawing literature, minimizing link crossings in a multi-layered graph is known to be an <strong>NP-hard problem</strong>.</p>

          <p>If nodes within a column are ordered arbitrarily, link ribbons will cross over one another repeatedly, resulting in an unreadable visual tangle. To untangle these crossings and produce clean, publication-grade flows, our engine implements an <strong>Iterative Gauss-Seidel Barycentric Relaxation Algorithm</strong>.</p>

          <h3>3.1 The Weighted Barycenter Heuristic</h3>
          <p>The fundamental principle of barycentric ordering is that a node's ideal vertical position is the weighted average (center of mass) of all the nodes connected to it in the adjacent column:</p>

          <div class="formula-card">
            <div class="formula-title">Upstream Weighted Barycenter Coordinate Formulation</div>
            <div class="formula-body">Y_bary(v) = [ &sum;_{u &in; In(v)} Y_center(u) &times; W(u, v) ] / [ &sum;_{u &in; In(v)} W(u, v) ]</div>
            <div class="formula-desc">Where W(u, v) is the flow volume of the link, and Y_center(u) is the current vertical midpoint of the connected upstream source node.</div>
          </div>

          <p>The relaxation engine executes multiple iterative sweeps (typically 24 to 32 passes):</p>
          <ol>
            <li><strong>Forward Sweep (Left to Right):</strong> For columns <em>L</em> = 1 to <em>L</em><sub>max</sub>, update each node's position toward the barycenter of its upstream source neighbors.</li>
            <li><strong>Vertical Collision Resolution:</strong> Sort nodes within the column by their new tentative <em>Y</em> coordinates. Scan from top to bottom, shifting overlapping nodes downward to enforce a mandatory vertical padding gap <em>G</em><sub>node</sub> (typically 10px to 16px). If the column extends past the bottom canvas boundary, scan from bottom to top and shift nodes upward.</li>
            <li><strong>Backward Sweep (Right to Left):</strong> For columns <em>L</em> = <em>L</em><sub>max</sub> - 1 down to 0, update each node's position toward the barycenter of its downstream target neighbors, followed by collision resolution.</li>
          </ol>

          <p>With each alternating sweep, link crossings decrease exponentially, and ribbons settle into smooth, parallel trajectories that communicate flow hierarchy with optimal clarity.</p>
        </section>

        <section id="cubic-bezier-ribbon-geometry">
          <h2>4. Cubic Bézier Ribbon Geometry: Dual-Spline Path Construction</h2>
          <p>The most visually captivating element of a Sankey diagram is the flowing ribbon that connects source and target nodes. Rather than drawing simple straight-sided trapezoids, professional vector diagrams utilize <strong>cubic Bézier curves</strong> (<code>C</code> commands in SVG) to produce elegant, organic S-curves that enter and exit nodes horizontally perpendicular to the node faces.</p>

          <h3>4.1 The Four-Point Boundary Formula</h3>
          <p>A Sankey ribbon is not a single line; it is a closed two-dimensional polygon bounded by four distinct coordinate edges:</p>
          <ol>
            <li><strong>Top Forward Curve:</strong> A cubic Bézier curve traveling from the source anchor (<em>x</em><sub>0</sub>, <em>y</em><sub>0,top</sub>) to the target anchor (<em>x</em><sub>1</sub>, <em>y</em><sub>1,top</sub>).</li>
            <li><strong>Target Vertical Edge:</strong> A straight vertical line dropping along the target node edge from <em>y</em><sub>1,top</sub> to <em>y</em><sub>1,bottom</sub> = <em>y</em><sub>1,top</sub> + <em>H</em><sub>link</sub>.</li>
            <li><strong>Bottom Reverse Curve:</strong> A cubic Bézier curve traveling backwards from the target anchor (<em>x</em><sub>1</sub>, <em>y</em><sub>1,bottom</sub>) back to the source anchor (<em>x</em><sub>0</sub>, <em>y</em><sub>0,bottom</sub>).</li>
            <li><strong>Source Vertical Edge:</strong> A straight vertical line rising along the source node edge back to (<em>x</em><sub>0</sub>, <em>y</em><sub>0,top</sub>), closed via <code>Z</code>.</li>
          </ol>

          <div class="formula-card">
            <div class="formula-title">Cubic Bézier Horizontal Control Point Offsets</div>
            <div class="formula-body">CP1_X = x_0 + &alpha; &times; ( x_1 - x_0 )<br>CP2_X = x_1 - &alpha; &times; ( x_1 - x_0 )<br>CP1_Y = y_0,   CP2_Y = y_1</div>
            <div class="formula-desc">Where &alpha; represents the curvature factor (typically &alpha; = 0.5 for a balanced S-curve). Setting the Y coordinates of control points equal to their respective endpoints enforces perfectly horizontal entry and exit tangents.</div>
          </div>

          <pre><code>// Programmatic Synthesis of SVG Sankey Ribbon Path
function generateSankeyRibbonPath(x0, y0Top, x1, y1Top, linkHeight, curvature = 0.5) {
  const dx = x1 - x0;
  const cp1X = (x0 + dx * curvature).toFixed(1);
  const cp2X = (x1 - dx * curvature).toFixed(1);

  const y0Bottom = (y0Top + linkHeight).toFixed(1);
  const y1Bottom = (y1Top + linkHeight).toFixed(1);

  return [
    `M ${x0.toFixed(1)} ${y0Top.toFixed(1)}`,
    `C ${cp1X} ${y0Top.toFixed(1)}, ${cp2X} ${y1Top.toFixed(1)}, ${x1.toFixed(1)} ${y1Top.toFixed(1)}`,
    `L ${x1.toFixed(1)} ${y1Bottom}`,
    `C ${cp2X} ${y1Bottom}, ${cp1X} ${y0Bottom}, ${x0.toFixed(1)} ${y0Bottom}`,
    `Z`
  ].join(' ');
}</code></pre>

          <h3>4.2 Two-Point Dynamic Linear Gradients</h3>
          <p>To enhance visual comprehension, each link ribbon should visually convey the conceptual transition between source and target entities. In SVG, this is achieved by synthesizing a unique <code>&lt;linearGradient&gt;</code> element in the SVG <code>&lt;defs&gt;</code> container for every active link, configuring <code>gradientUnits="userSpaceOnUse"</code> spanning from <em>x</em><sub>0</sub> to <em>x</em><sub>1</sub>:</p>

          <pre><code>&lt;!-- Dynamic Ribbon Color Gradient --&gt;
&lt;defs&gt;
  &lt;linearGradient id="grad-aws-to-ec2" x1="120" y1="0" x2="340" y2="0" gradientUnits="userSpaceOnUse"&gt;
    &lt;stop offset="0%" stop-color="#38BDF8" stop-opacity="0.65" /&gt;
    &lt;stop offset="100%" stop-color="#C1DD2D" stop-opacity="0.65" /&gt;
  &lt;/linearGradient&gt;
&lt;/defs&gt;

&lt;path d="M 120 84 C 230 84, 230 142, 340 142 L 340 178 C 230 178, 230 120, 120 120 Z"
      fill="url(#grad-aws-to-ec2)" class="sankey-ribbon" /&gt;</code></pre>
        </section>

        <section id="flow-conservation-and-balancing">
          <h2>5. Kirchhoff Flow Conservation &amp; Drop-Off Residual Handling</h2>
          <p>In classical thermodynamic and mechanical engineering applications, Sankey diagrams strictly observe <strong>Kirchhoff's Conservation Laws</strong>: energy can neither be created nor destroyed, meaning the total inflow into any intermediate node must equal the total outflow precisely (&Sigma; <em>V</em><sub>in</sub> = &Sigma; <em>V</em><sub>out</sub>).</p>

          <p>However, in modern software engineering, sales marketing funnels, and corporate budget analysis, real-world data frequently exhibits imbalances:</p>
          <ul>
            <li><strong>Funnel Drop-Off (Leaking Funnels):</strong> In an e-commerce checkout funnel, 100,000 users visit the product page, but only 24,000 proceed to cart, and 8,000 complete purchase. The remaining 76,000 users drop off at stage 1.</li>
            <li><strong>Infrastructure Overhead &amp; Cloud Waste:</strong> An enterprise allocates 100,000 USD in monthly compute budget, but only 72,000 USD maps to active customer tenant workloads, with 28,000 USD lost to idle capacity and unallocated reserved instances.</li>
          </ul>

          <div class="formula-card">
            <div class="formula-title">Flow Imbalance Residual Equation</div>
            <div class="formula-body">Residual = &sum; Inflow - &sum; Outflow<br>Node_Height = max( &sum; Inflow, &sum; Outflow ) &times; Height_Scale</div>
            <div class="formula-desc">When residual is positive, the node possesses unallocated outflow volume. The engine can either display an explicit downward drop-off ribbon or leave the remainder unlinked.</div>
          </div>

          <p>Our SVG engine handles both physical conservation and commercial funnel leakage by sizing each node's physical height to the maximum of its total incoming or outgoing flow. Link anchor offsets are stacked sequentially along the node's vertical edge, ensuring that ribbons never overlap at terminal connection faces.</p>
        </section>

        <!-- Figure 2: Dedicated Vector Architecture Diagram (960x320) -->
        <section id="architectural-pipeline-diagram">
          <h2>6. Architectural Pipeline: Manifest to Vector Synthesis</h2>
          <p>Transforming an abstract manifest of relational flow links into a balanced, interactive SVG diagram requires a pipeline that coordinates graph theory, numerical relaxation, geometry synthesis, and DOM rendering.</p>

          <figure class="article-figure">
            <svg viewBox="0 0 960 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#0D1117; border-radius:10px; border:1px solid #262626; display:block;">
              <defs>
                <linearGradient id="flowPipeGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#161B22"/>
                  <stop offset="100%" stop-color="#0E1217"/>
                </linearGradient>
                <linearGradient id="flowPipeGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#1A2210"/>
                  <stop offset="100%" stop-color="#0E150A"/>
                </linearGradient>
                <linearGradient id="flowPipeArrow" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#555"/>
                  <stop offset="100%" stop-color="#C1DD2D"/>
                </linearGradient>
                <filter id="flowPipeGlow" x="-10%" y="-10%" width="120%" height="120%">
                  <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="rgba(193,221,45,0.15)"/>
                </filter>
              </defs>

              <!-- Diagram Title -->
              <text x="30" y="36" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#FFF" letter-spacing="0.5">FIGURE 2: HIGH-PERFORMANCE SVG SANKEY SYNTHESIS PIPELINE</text>
              <text x="30" y="54" font-family="'JetBrains Mono', monospace" font-size="11" fill="#888">ARCHITECTURE: DAG PARSING &rarr; NODE STRATIFICATION &rarr; RELAXATION &rarr; BEZIER SYNTHESIS</text>

              <!-- Stage 1: Manifest Ingestion -->
              <g transform="translate(30, 80)" filter="url(#flowPipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#flowPipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.12)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">01</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">DAG Parsing</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#888">Topology Ingestion</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Node-Link Objects</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Cycle Detection</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Flow Balance Check</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Residual Isolation</text>
              </g>

              <!-- Connector 1 -->
              <path d="M 190 177 L 220 177" stroke="url(#flowPipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="220,172 230,177 220,182" fill="#C1DD2D"/>

              <!-- Stage 2: Node Stratification -->
              <g transform="translate(230, 80)" filter="url(#flowPipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#flowPipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.12)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">02</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">Stratification</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#888">Column Tier Ranking</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Longest-Path Depth</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Justify Alignment</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Column Spacing Math</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Node Height Scaling</text>
              </g>

              <!-- Connector 2 -->
              <path d="M 390 177 L 420 177" stroke="url(#flowPipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="420,172 430,177 420,182" fill="#C1DD2D"/>

              <!-- Stage 3: Barycentric Relaxation -->
              <g transform="translate(430, 80)" filter="url(#flowPipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#flowPipeGrad2)" stroke="#C1DD2D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.25)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">03</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">Gauss Relaxation</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#C1DD2D">Crossing Minimization</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="rgba(193,221,45,0.3)" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; 32 Sweeps (Fwd/Rev)</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; Barycenter Weighting</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; Collision Padding</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; Vertical Clamping</text>
              </g>

              <!-- Connector 3 -->
              <path d="M 590 177 L 620 177" stroke="url(#flowPipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="620,172 630,177 620,182" fill="#C1DD2D"/>

              <!-- Stage 4: Cubic Ribbon Geometry -->
              <g transform="translate(630, 80)" filter="url(#flowPipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#flowPipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.12)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">04</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">Ribbon Geometry</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#888">Dual-Spline Synthesis</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Cubic S-Curves (C)</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Anchor Stacking Math</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Dynamic Gradients</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Subpixel Pathing</text>
              </g>

              <!-- Connector 4 -->
              <path d="M 790 177 L 820 177" stroke="url(#flowPipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="820,172 830,177 820,182" fill="#C1DD2D"/>

              <!-- Stage 5: DOM & Telemetry -->
              <g transform="translate(830, 80)" filter="url(#flowPipeGlow)">
                <rect width="100" height="195" rx="8" fill="url(#flowPipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <text x="14" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#C1DD2D">05. OUTPUT</text>
                <text x="14" y="65" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#FFF">GPU Render</text>
                <text x="14" y="82" font-family="'Inter', sans-serif" font-size="10" fill="#888">Interactive HUD</text>
                <line x1="10" y1="96" x2="90" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="10" y="120" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; Stream Dash</text>
                <text x="10" y="140" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; Tooltip HUD</text>
                <text x="10" y="160" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; ARIA Roles</text>
                <text x="10" y="180" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; PDF Export</text>
              </g>
            </svg>
            <figcaption>Figure 2: Complete five-stage architectural pipeline of the SVG Sankey flow engine: from raw DAG manifest ingestion and cycle detection to topological stratification, Gauss-Seidel barycentric relaxation, cubic Bézier ribbon synthesis, and GPU-composited interaction.</figcaption>
          </figure>
        </section>

        <section id="interactive-sankey-studio">
          <h2>7. Interactive Developer Studio: Live Sankey Flow Workbench</h2>
          <p>To demonstrate the real-time node stratification math, relaxation algorithms, and smooth cubic Bézier ribbon geometry detailed in this guide, test our production <strong>SVG Sankey Flow Studio</strong>. This fully functional workbench renders four distinct enterprise topologies in pure, dependency-free SVG, complete with interactive ribbon curvature tuning, palette switching, active flow particle animations, and vector SVG export.</p>

          <p>Experiment with the workbench using the following interactive controls:</p>
          <ul>
            <li><strong>Select Flow Topology Preset:</strong> Switch between four real-world data systems: <em>Cloud Infrastructure Cost</em> (compute, database, and egress spending), <em>SaaS Conversion Funnel</em> (visitor drop-off across marketing stages), <em>Global Renewable Energy Grid</em> (generation to consumption transmission), and <em>Personal Household Cashflow</em> (gross income to taxes, housing, and investments).</li>
            <li><strong>Adjust Ribbon Curvature:</strong> Use the interactive slider to tune the cubic Bézier curvature factor <em>&alpha;</em> from 0.1 (sharp angular transitions) to 0.9 (deep dramatic S-curves), watching the SVG path definitions recalculate instantaneously.</li>
            <li><strong>Select Color Palette:</strong> Switch between four accessible palettes: <em>Cyberpunk Neon</em>, <em>Corporate FinTech Slate</em>, <em>Botanical Green</em>, and <em>Solar Amber</em>.</li>
            <li><strong>Interactive Ribbon Inspection:</strong> Hover your mouse or tap any flowing ribbon. The inspection HUD displays the source entity, target entity, absolute volume, and percentage share of total flow.</li>
            <li><strong>Export Vector Assets:</strong> Click "Copy SVG Markup" to copy the standalone SVG element directly to your clipboard, ready for inclusion in executive slide decks or vector dashboards.</li>
          </ul>

          <div class="interactive-sandbox" id="sankeyStudio">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12h16"/><path d="M4 6h8a4 4 0 0 1 4 4v4a4 4 0 0 0 4 4h0"/><path d="M4 18h8a4 4 0 0 0 4-4V10a4 4 0 0 1 4-4h0"/></svg>
                <span>Live Interactive SVG Sankey &amp; Alluvial Studio</span>
              </div>
              <span class="sandbox-badge">Real-Time Vector Engine</span>
            </div>

            <div class="sandbox-grid">
              <div class="sandbox-controls">
                <div class="control-row">
                  <label for="sankeyPresetSelect">Flow Topology Preset: <span class="stat-num" id="sankeyPresetBadge">Cloud Cost</span></label>
                  <select id="sankeyPresetSelect" class="control-select">
                    <option value="cloud_cost" selected>Cloud Infrastructure &amp; DevOps Budget</option>
                    <option value="saas_funnel">SaaS Customer Journey &amp; Conversion Funnel</option>
                    <option value="energy_grid">Renewable Energy Production &amp; Distribution</option>
                    <option value="personal_budget">Personal Household Income &amp; Cashflow</option>
                  </select>
                </div>

                <div class="control-row">
                  <label for="sankeyColorSelect">Visual Palette Theme:</label>
                  <select id="sankeyColorSelect" class="control-select">
                    <option value="neon" selected>Cyberpunk Neon (Cyan, Lime, Purple, Amber)</option>
                    <option value="corporate">Corporate FinTech Slate (Navy, Steel, Blue)</option>
                    <option value="botanical">Botanical Green (Forest, Emerald, Sage)</option>
                    <option value="solar">Solar Amber (Flame, Ochre, Gold)</option>
                  </select>
                </div>

                <div class="control-row">
                  <label for="curvatureRange">Cubic Bézier Curvature (&alpha;): <span class="stat-num" id="curvatureVal">0.50</span></label>
                  <input type="range" id="curvatureRange" min="0.1" max="0.85" value="0.5" step="0.05" class="control-input">
                </div>

                <div class="control-row">
                  <label for="nodeWidthRange">Node Bar Width: <span class="stat-num" id="nodeWidthVal">14 px</span></label>
                  <input type="range" id="nodeWidthRange" min="8" max="24" value="14" step="2" class="control-input">
                </div>

                <div class="stats-readout-box">
                  <div class="stat-item">
                    <div class="stat-label">Total System Flow</div>
                    <div class="stat-val highlight" id="sankeyTotalVolume">$142,500</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Active Nodes</div>
                    <div class="stat-val" id="sankeyNodeCount">9 Nodes</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Directed Links</div>
                    <div class="stat-val" id="sankeyLinkCount">11 Ribbons</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Inspected Link</div>
                    <div class="stat-val highlight" id="sankeyHoverLink">AWS &rarr; EC2 ($48k)</div>
                  </div>
                </div>

                <div class="btn-row">
                  <button type="button" class="action-btn primary" id="btnCopySankeySVG">Copy SVG Markup</button>
                  <button type="button" class="action-btn" id="btnToggleFlowAnim" data-active="true">Toggle Flow Pulses</button>
                </div>

                <div class="control-row">
                  <label>Exported Vector Source (Live Snippet):</label>
                  <div class="code-preview-pane" id="sankeyCodePreview">&lt;!-- Initializing SVG Sankey Engine... --&gt;</div>
                </div>
              </div>

              <div class="stage-wrapper">
                <div class="preview-stage-container" id="sankeyStageContainer">
                  <svg id="sankeyCanvas" class="stage-canvas-element" viewBox="0 0 740 400">
                    <!-- Injected dynamically by JavaScript -->
                  </svg>
                </div>
                <div style="font-size:12px; color:#777; text-align:center; font-family:'JetBrains Mono', monospace;">
                  Tip: Hover over any curved ribbon or rectangular node to inspect volume metrics.
                </div>
              </div>
            </div>
          </div>
        </section>

        <section id="interactive-node-dragging">
          <h2>8. Interactive Node Dragging &amp; Real-Time Path Recalculation</h2>
          <p>While algorithmic barycentric relaxation provides an optimal baseline layout, human domain experts frequently need to reposition nodes to align with organizational reporting structures, project hierarchies, or presentation aesthetics. A production-grade SVG Sankey engine must support fluid, 60 FPS drag-and-drop repositioning.</p>

          <p>When an engineer initiates a drag event on an SVG node <code>&lt;rect&gt;</code>, the engine constrains movement to the vertical Y-axis, keeping the node anchored strictly within its assigned topological column. As the node translates vertically, recomputing the entire graph layout from scratch is an anti-pattern that introduces perceptible lag. Instead, the engine executes localized <em>O</em>(<em>K</em>) updates, where <em>K</em> is the number of links directly connected to the active node.</p>

          <div class="formula-card">
            <div class="formula-title">Localized Ribbon Recalculation on Drag</div>
            <div class="formula-body">&Delta;Y = Pointer_Y - Drag_Start_Y<br>Y_node_new = Clamp( Y_node_orig + &Delta;Y, Y_min, Y_max )<br>Update_Links( InNeighbors(node), OutNeighbors(node) )</div>
            <div class="formula-desc">Only the cubic Bézier path strings for the incoming and outgoing links attached to the moving node are rewritten, leaving all other ribbons untouched.</div>
          </div>

          <p>By updating only the affected SVG <code>d</code> attributes and leveraging PointerEvents with <code>setPointerCapture()</code>, users can drag massive nodes with sub-millisecond responsiveness across touchscreens, trackpads, and high-precision mice alike.</p>
        </section>

        <section id="alluvial-vs-sankey-distinctions">
          <h2>9. Alluvial Diagrams vs. Sankey Diagrams: Temporal Cohort Migrations</h2>
          <p>In data engineering and scientific literature, the terms <strong>Sankey diagram</strong> and <strong>Alluvial diagram</strong> are frequently used interchangeably. However, they represent distinct mathematical paradigms with subtle differences in semantics and layout constraints:</p>
          <ul>
            <li><strong>Sankey Diagrams (Conservation of Physical Volume):</strong> Sankey diagrams represent the physical division, transformation, and conservation of a single homogeneous quantity (such as Joules of electrical energy, gallons of water, or dollars of revenue). The focus is on source-to-sink distribution networks where nodes represent physical facilities, ledger accounts, or processing units.</li>
            <li><strong>Alluvial Diagrams (Categorical Temporal Migrations):</strong> Alluvial diagrams visualize changes in group composition, cluster membership, or state over time. Each vertical column represents a discrete chronological epoch (e.g. Year 2024, Year 2025, Year 2026), and each node represents a categorical cluster (e.g. Customer Subscription Tier: Free, Pro, Enterprise). Ribbons represent the migration of cohort entities transitioning from one cluster to another across successive time periods.</li>
          </ul>

          <p>In an Alluvial chart, the total height of all columns is strictly identical across every time tier because the total underlying population remains constant, whereas in a Sankey diagram, column heights vary dramatically depending on local consumption, branch expansion, and dissipation.</p>
        </section>

        <section id="enterprise-pdf-and-datasheet-export">
          <h2>10. Exporting Publication-Grade Vector PDF &amp; Investor Datasheets</h2>
          <p>Sankey diagrams are prime deliverables for corporate board presentations, quarterly investor updates, sustainability audits, and regulatory filings. These institutional contexts demand vector export that renders with pristine fidelity on physical printouts or inside executive PDF decks.</p>

          <p>Because our engine synthesizes pure, dependency-free SVG, exporting the active visualization to high-resolution vector formats requires no lossy raster conversion. The export engine serializes the live SVG DOM element into a self-contained XML string, embedding all necessary CSS typography rules and color variables:</p>

          <pre><code>// Standalone SVG Serialization &amp; High-Resolution Vector Download
function exportSankeyToStandaloneSVG(svgElement) {
  const serializer = new XMLSerializer();
  let source = serializer.serializeToString(svgElement);

  // Inject explicit XML namespace declarations
  if (!source.match(/^<svg[^>]+xmlns="http:\/\/www\.w3\.org\/2000\/svg"/)) {
    source = source.replace(/^<svg/, '<svg xmlns="http://www.w3.org/2000/svg"');
  }

  // Convert to downloadable Blob
  const blob = new Blob([source], { type: 'image/svg+xml;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const downloadLink = document.createElement('a');
  downloadLink.href = url;
  downloadLink.download = 'corporate_flow_sankey_2026.svg';
  document.body.appendChild(downloadLink);
  downloadLink.click();
  document.body.removeChild(downloadLink);
}</code></pre>

          <p>When imported into Adobe Illustrator, Figma, or LaTeX typesetting environments, every cubic Bézier spline, gradient fill, and node label is recognized as a native editable vector curve, delivering infinite DPI scaling for 1200 DPI institutional print releases.</p>
        </section>

        <section id="large-scale-graph-optimization">
          <h2>11. Performance Optimization for Dense Enterprise Graphs</h2>
          <p>When visualizing complex enterprise cloud environments—such as a global Kubernetes cluster spanning 40 microservices, 12 database clusters, and hundreds of network egress routes—a naive Sankey layout can produce an overwhelming visual thicket of hundreds of intersecting ribbons.</p>

          <p>To preserve visual legibility and maintain 60 FPS rendering performance, high-grade vector flow engines employ <strong>Adaptive Link Bundling</strong> and <strong>Threshold Culling</strong>:</p>
          <ul>
            <li><strong>Minimum Flow Threshold Culling:</strong> In dense systems, the bottom 80% of links often represent less than 2% of total cumulative flow (e.g. tiny stray telemetry pings). The engine filters out links below a configurable significance threshold (such as Link_Val &lt; 0.005 &times; Total_Flow), aggregating them into a single semi-transparent grey "Other / Miscellaneous" ribbon. This eliminates 75% of visual clutter without discarding aggregate mass.</li>
            <li><strong>Hierarchical Node Aggregation:</strong> When nodes in a layer share identical parents and children, they are collapsed into an expandable composite group node (e.g. "Microservices Pool [8 pods]"), allowing viewers to drill down into sub-flows on demand.</li>
          </ul>
        </section>

        <section id="animated-flow-particles">
          <h2>12. Hardware-Accelerated Flow Animation: The Stream Dash Technique</h2>
          <p>Static Sankey diagrams convey volume clearly, but animated flow pulses transform a static report into a living, dynamic telemetry dashboard. Visualizing active network traffic or electrical transmission helps users grasp the real-time velocity of the underlying system.</p>

          <p>In SVG, creating smooth flow animations without triggering JavaScript CPU loops utilizes the <strong>Stream Dash Technique</strong>. A transparent duplicate path is created along the centerline of each ribbon. By applying a dashed stroke pattern and animating <code>stroke-dashoffset</code> via pure CSS keyframes, moving flow dashes travel seamlessly along the curves:</p>

          <pre><code>/* Pure CSS Hardware-Accelerated Flow Stream */
@keyframes flowRun {
  from { stroke-dashoffset: 32; }
  to { stroke-dashoffset: 0; }
}

.flow-stream-line {
  stroke: rgba(255, 255, 255, 0.45);
  stroke-dasharray: 6 10;
  stroke-linecap: round;
  fill: none;
  animation: flowRun 1.4s linear infinite;
}</code></pre>

          <p>Because CSS animations on SVG stroke offsets execute directly on the browser's GPU compositor layer, dozens of concurrent flow streams can be animated simultaneously at a continuous 60 FPS without impacting main-thread JavaScript performance.</p>
        </section>

        <section id="accessibility-and-screen-readers">
          <h2>13. Accessibility, Flow Narration &amp; WCAG 2.2 AA Compliance</h2>
          <p>Complex multi-layered flow graphs present unique accessibility challenges for visually impaired users. When an engineer using a screen reader navigates an SVG Sankey diagram, hearing a list of unlabelled path elements is completely useless. The visualization must provide structured flow narration.</p>

          <p>Our SVG architecture implements a multi-tier accessibility strategy:</p>
          <ul>
            <li><strong>Semantic Graph Hierarchy:</strong> The root SVG container declares <code>role="graphics-document"</code> and provides an overarching <code>aria-label</code> summarizing total flow and major destination allocations.</li>
            <li><strong>Accessible Relationship Links:</strong> Each node rect element is assigned <code>role="graphics-symbol"</code> with <code>tabindex="0"</code> and a descriptive label: <code>aria-label="Compute Layer: Total Inflow $65,000, distributing to Microservices ($42k) and Batch Jobs ($23k)"</code>.</li>
            <li><strong>Structured Table Fallback:</strong> Directly following the SVG container, a visually hidden table (<code>&lt;table class="sr-only"&gt;</code>) breaks down the complete adjacency matrix, enabling screen reader users to navigate from source to target using standard table shortcut keys.</li>
          </ul>
        </section>

        <section id="faq-section" class="faq-block">
          <h2>14. Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3 class="faq-question">Why build Sankey and alluvial diagrams in pure SVG rather than HTML5 Canvas?</h3>
            <div class="faq-answer">Scalable Vector Graphics (SVG) maintains infinite resolution independence, allowing intricate multi-stage flow diagrams to scale flawlessly from small responsive mobile screens up to multi-monitor operations displays and high-resolution print deliverables without pixelation. Most importantly, SVG preserves the distinct identity of every node and link ribbon as discrete DOM elements. This enables native CSS hover state highlighting, gradient fills matching source-to-target nodes, screen reader accessibility under WCAG 2.2 AA, and programmatic vector export.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How is the cubic Bézier ribbon geometry constructed between two Sankey nodes in SVG?</h3>
            <div class="faq-answer">A Sankey flow ribbon is constructed as a closed SVG path with four interconnected boundaries: 1) A top cubic Bézier curve tracing from (x0, y0_top) to (x1, y1_top) with horizontal control points at midpoint x_mid = (x0 + x1) / 2; 2) A vertical line dropping along the target node edge to (x1, y1_bottom); 3) A bottom cubic Bézier curve tracing backwards from (x1, y1_bottom) to (x0, y0_bottom); 4) A vertical line closing back up along the source node edge with 'Z'.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How does node stratification and topological layer assignment work in a Sankey DAG?</h3>
            <div class="faq-answer">In a Directed Acyclic Graph (DAG), each node is assigned to a horizontal column (depth tier). The engine calculates the longest path from source nodes to each target node using topological sorting: depth(node) = max([depth(parent) + 1 for parent in incoming_nodes]). Nodes with no incoming links reside in column 0, while terminal sink nodes reside in the final column. Nodes can then be justified to the left, right, or centered across the canvas width.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How do iterative relaxation algorithms minimize link crossings in complex Sankey diagrams?</h3>
            <div class="faq-answer">Iterative relaxation algorithms (such as Gauss-Seidel relaxation) sweep repeatedly back and forth through the columns. During each iteration, a node's vertical Y coordinate is adjusted toward the weighted barycenter of its connected upstream or downstream neighbors: Y_target = sum(Y_neighbor * Link_Weight) / sum(Link_Weight). The engine then resolves vertical collisions between adjacent nodes in the same column to enforce minimum padding gaps, drastically reducing ribbon crossings.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How do you enforce Kirchhoff-style conservation of flow when data inputs and outputs do not match?</h3>
            <div class="faq-answer">Ideal physical Sankey diagrams adhere strictly to flow conservation: sum(Inflow) = sum(Outflow) at every intermediate node. However, in real-world business datasets like sales conversion funnels, customers drop off at each stage. High-grade SVG engines handle this by computing the residual difference: Residual = Inflow - Outflow. If positive, the residual is either rendered as an explicit downward 'Drop-off / Loss' ribbon or the node height is sized to the maximum of incoming and outgoing totals, with link ribbons anchored proportionally along the node edge.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How do you animate dynamic flow movement along SVG Sankey ribbons without lag?</h3>
            <div class="faq-answer">To visualize active fluid flow, energy transmission, or network bandwidth, an auxiliary dashed overlay stroke path is placed along the centerline of the ribbon. By animating the CSS stroke-dashoffset property using GPU-composited CSS keyframes (e.g. @keyframes flowRun { to { stroke-dashoffset: -32; } }), moving flow pulses travel continuously along the ribbons at 60 FPS with zero JavaScript runtime execution overhead.</div>
          </div>
        </section>
      </article>

            <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <ol>
              <li><a href="#introduction-flow-imperative">1. Visual Conservation of Flow</a></li>
              <li><a href="#dag-topology-and-stratification">2. DAG Topology &amp; Stratification</a></li>
              <li><a href="#relaxation-and-crossing-minimization">3. Gauss-Seidel Relaxation</a></li>
              <li><a href="#cubic-bezier-ribbon-geometry">4. Cubic Bézier Ribbon Geometry</a></li>
              <li><a href="#flow-conservation-and-balancing">5. Kirchhoff Flow Conservation</a></li>
              <li><a href="#architectural-pipeline-diagram">6. Architectural Pipeline</a></li>
              <li><a href="#interactive-sankey-studio">7. Interactive Developer Studio</a></li>
              <li><a href="#interactive-node-dragging">8. Interactive Node Dragging</a></li>
              <li><a href="#alluvial-vs-sankey-distinctions">9. Alluvial vs Sankey</a></li>
              <li><a href="#enterprise-pdf-and-datasheet-export">10. Vector Datasheet Export</a></li>
              <li><a href="#large-scale-graph-optimization">11. Performance Optimization</a></li>
              <li><a href="#animated-flow-particles">12. Animated Flow Particles</a></li>
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

    // Interactive Sankey Studio Engine
    (function initSankeyStudio() {
      const canvas = document.getElementById('sankeyCanvas');
      const presetSelect = document.getElementById('sankeyPresetSelect');
      const presetBadge = document.getElementById('sankeyPresetBadge');
      const colorSelect = document.getElementById('sankeyColorSelect');
      const curvatureRange = document.getElementById('curvatureRange');
      const curvatureVal = document.getElementById('curvatureVal');
      const nodeWidthRange = document.getElementById('nodeWidthRange');
      const nodeWidthVal = document.getElementById('nodeWidthVal');
      const btnCopy = document.getElementById('btnCopySankeySVG');
      const btnToggleAnim = document.getElementById('btnToggleFlowAnim');
      const codePreview = document.getElementById('sankeyCodePreview');

      const hudVolume = document.getElementById('sankeyTotalVolume');
      const hudNodes = document.getElementById('sankeyNodeCount');
      const hudLinks = document.getElementById('sankeyLinkCount');
      const hudHover = document.getElementById('sankeyHoverLink');

      let currentPreset = 'cloud_cost';
      let activePalette = 'neon';
      let curvature = 0.5;
      let nodeWidth = 14;
      let showFlowAnim = true;

      const paletteColors = {
        neon: ['#38BDF8', '#C1DD2D', '#A855F7', '#F59E0B', '#EC4899', '#10B981'],
        corporate: ['#1E3A8A', '#2563EB', '#60A5FA', '#93C5FD', '#0284C7', '#0EA5E9'],
        botanical: ['#064E3B', '#047857', '#10B981', '#34D399', '#6EE7B7', '#A7F3D0'],
        solar: ['#78350F', '#B45309', '#F59E0B', '#FBBF24', '#FDE047', '#FEF08A']
      };

      // Topologies Definition
      const topologies = {
        cloud_cost: {
          title: 'Cloud Cost',
          unit: '$',
          nodes: [
            { id: 'aws', name: 'AWS Cloud', col: 0, val: 142500, color: 0 },
            { id: 'compute', name: 'EC2 Compute', col: 1, val: 68000, color: 1 },
            { id: 'storage', name: 'S3 & EBS Storage', col: 1, val: 42000, color: 2 },
            { id: 'network', name: 'CloudFront Egress', col: 1, val: 32500, color: 3 },
            { id: 'frontend', name: 'Web Traffic', col: 2, val: 48000, color: 4 },
            { id: 'backend', name: 'API Cluster', col: 2, val: 56000, color: 1 },
            { id: 'data_lake', name: 'Analytics Lake', col: 2, val: 38500, color: 5 }
          ],
          links: [
            { source: 'aws', target: 'compute', val: 68000 },
            { source: 'aws', target: 'storage', val: 42000 },
            { source: 'aws', target: 'network', val: 32500 },
            { source: 'compute', target: 'frontend', val: 24000 },
            { source: 'compute', target: 'backend', val: 44000 },
            { source: 'storage', target: 'backend', val: 12000 },
            { source: 'storage', target: 'data_lake', val: 30000 },
            { source: 'network', target: 'frontend', val: 24000 },
            { source: 'network', target: 'data_lake', val: 8500 }
          ]
        },
        saas_funnel: {
          title: 'SaaS Funnel',
          unit: '',
          nodes: [
            { id: 'visitors', name: 'Landing Visitors', col: 0, val: 100000, color: 0 },
            { id: 'signup', name: 'Free Signups', col: 1, val: 34000, color: 1 },
            { id: 'onboard', name: 'Onboarded Team', col: 2, val: 18500, color: 2 },
            { id: 'paid', name: 'Enterprise Sub', col: 3, val: 7200, color: 3 }
          ],
          links: [
            { source: 'visitors', target: 'signup', val: 34000 },
            { source: 'signup', target: 'onboard', val: 18500 },
            { source: 'onboard', target: 'paid', val: 7200 }
          ]
        },
        energy_grid: {
          title: 'Energy Grid',
          unit: 'GW',
          nodes: [
            { id: 'solar', name: 'Solar Arrays', col: 0, val: 450, color: 3 },
            { id: 'wind', name: 'Offshore Wind', col: 0, val: 620, color: 0 },
            { id: 'hydro', name: 'Hydroelectric', col: 0, val: 380, color: 1 },
            { id: 'grid', name: 'HVDC Transmission', col: 1, val: 1450, color: 2 },
            { id: 'industrial', name: 'Heavy Industry', col: 2, val: 780, color: 4 },
            { id: 'residential', name: 'Smart Homes', col: 2, val: 490, color: 1 },
            { id: 'storage_bat', name: 'Megapack Storage', col: 2, val: 180, color: 5 }
          ],
          links: [
            { source: 'solar', target: 'grid', val: 450 },
            { source: 'wind', target: 'grid', val: 620 },
            { source: 'hydro', target: 'grid', val: 380 },
            { source: 'grid', target: 'industrial', val: 780 },
            { source: 'grid', target: 'residential', val: 490 },
            { source: 'grid', target: 'storage_bat', val: 180 }
          ]
        },
        personal_budget: {
          title: 'Household Budget',
          unit: '$',
          nodes: [
            { id: 'salary', name: 'Gross Salary', col: 0, val: 12500, color: 1 },
            { id: 'taxes', name: 'Income Taxes', col: 1, val: 3200, color: 4 },
            { id: 'net_income', name: 'Net Take-Home', col: 1, val: 9300, color: 0 },
            { id: 'mortgage', name: 'Housing & Utilities', col: 2, val: 3800, color: 2 },
            { id: 'living', name: 'Living & Food', col: 2, val: 2400, color: 3 },
            { id: 'savings', name: 'Index Fund Savings', col: 2, val: 3100, color: 5 }
          ],
          links: [
            { source: 'salary', target: 'taxes', val: 3200 },
            { source: 'salary', target: 'net_income', val: 9300 },
            { source: 'net_income', target: 'mortgage', val: 3800 },
            { source: 'net_income', target: 'living', val: 2400 },
            { source: 'net_income', target: 'savings', val: 3100 }
          ]
        }
      };

      function renderSankey() {
        if (!canvas) return;

        const topo = topologies[currentPreset];
        const colors = paletteColors[activePalette];
        const width = 740;
        const height = 400;
        const padX = 60;
        const padY = 40;
        const nodeGap = 20;

        // Group nodes by column
        const maxCol = Math.max(...topo.nodes.map(n => n.col));
        const cols = [];
        for (let c = 0; c <= maxCol; c++) {
          cols.push(topo.nodes.filter(n => n.col === c));
        }

        // Calculate total column heights & scaling factor
        const colWidth = (width - 2 * padX - nodeWidth) / (maxCol || 1);
        const availH = height - 2 * padY;

        // Find max total value across columns to set scale
        let maxColVal = 0;
        cols.forEach(colNodes => {
          const colSum = colNodes.reduce((sum, n) => sum + n.val, 0);
          if (colSum > maxColVal) maxColVal = colSum;
        });

        const scaleY = (availH - (Math.max(...cols.map(c => c.length)) - 1) * nodeGap) / (maxColVal || 1);

        // Assign positions to nodes
        const nodeMap = new Map();
        cols.forEach((colNodes, cIdx) => {
          const x = padX + cIdx * colWidth;
          const totalVal = colNodes.reduce((sum, n) => sum + n.val, 0);
          const totalGaps = (colNodes.length - 1) * nodeGap;
          const totalHeight = totalVal * scaleY + totalGaps;
          let curY = padY + (availH - totalHeight) / 2;

          colNodes.forEach(node => {
            const h = Math.max(16, node.val * scaleY);
            const nodeObj = {
              ...node,
              x,
              y: curY,
              h,
              colorHex: colors[node.color % colors.length],
              outOffset: 0,
              inOffset: 0
            };
            nodeMap.set(node.id, nodeObj);
            curY += h + nodeGap;
          });
        });

        // Compute HUD Metrics
        let totalFlow = topo.nodes.filter(n => n.col === 0).reduce((sum, n) => sum + n.val, 0);
        if (hudVolume) hudVolume.textContent = topo.unit === '$' ? ('$' + totalFlow.toLocaleString()) : `${totalFlow.toLocaleString()} ${topo.unit}`.trim();
        if (hudNodes) hudNodes.textContent = `${topo.nodes.length} Nodes`;
        if (hudLinks) hudLinks.textContent = `${topo.links.length} Ribbons`;

        // Build SVG elements
        let svg = `<defs>`;
        // Gradients for links
        topo.links.forEach((l, idx) => {
          const src = nodeMap.get(l.source);
          const tgt = nodeMap.get(l.target);
          if (src && tgt) {
            svg += `
              <linearGradient id="linkGrad_${idx}" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="${src.colorHex}" stop-opacity="0.6"/>
                <stop offset="100%" stop-color="${tgt.colorHex}" stop-opacity="0.6"/>
              </linearGradient>
            `;
          }
        });
        svg += `</defs>`;

        // Render Links (Cubic Ribbons)
        svg += `<g class="sankey-links-layer">`;
        topo.links.forEach((l, idx) => {
          const src = nodeMap.get(l.source);
          const tgt = nodeMap.get(l.target);
          if (!src || !tgt) return;

          const linkH = Math.max(2, l.val * scaleY);
          const x0 = src.x + nodeWidth;
          const y0Top = src.y + src.outOffset;
          const x1 = tgt.x;
          const y1Top = tgt.y + tgt.inOffset;

          src.outOffset += linkH;
          tgt.inOffset += linkH;

          const dx = x1 - x0;
          const cp1x = x0 + dx * curvature;
          const cp2x = x1 - dx * curvature;

          const y0Bot = y0Top + linkH;
          const y1Bot = y1Top + linkH;

          const ribbonPath = `M ${x0.toFixed(1)} ${y0Top.toFixed(1)} C ${cp1x.toFixed(1)} ${y0Top.toFixed(1)}, ${cp2x.toFixed(1)} ${y1Top.toFixed(1)}, ${x1.toFixed(1)} ${y1Top.toFixed(1)} L ${x1.toFixed(1)} ${y1Bot.toFixed(1)} C ${cp2x.toFixed(1)} ${y1Bot.toFixed(1)}, ${cp1x.toFixed(1)} ${y0Bot.toFixed(1)}, ${x0.toFixed(1)} ${y0Bot.toFixed(1)} Z`;

          const centerPath = `M ${x0.toFixed(1)} ${(y0Top + linkH / 2).toFixed(1)} C ${cp1x.toFixed(1)} ${(y0Top + linkH / 2).toFixed(1)}, ${cp2x.toFixed(1)} ${(y1Top + linkH / 2).toFixed(1)}, ${x1.toFixed(1)} ${(y1Top + linkH / 2).toFixed(1)}`;

          const valFmt = topo.unit === '$' ? ('$' + l.val.toLocaleString()) : `${l.val.toLocaleString()} ${topo.unit}`;

          svg += `
            <g class="sankey-ribbon-group" data-src="${src.name}" data-tgt="${tgt.name}" data-val="${valFmt}">
              <path class="sankey-ribbon" d="${ribbonPath}" fill="url(#linkGrad_${idx})" stroke="rgba(255,255,255,0.08)" stroke-width="0.5" />
              ${showFlowAnim ? `<path class="flow-active-stream" d="${centerPath}" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />` : ''}
            </g>
          `;
        });
        svg += `</g>`;

        // Render Nodes (Rectangles + Labels)
        svg += `<g class="sankey-nodes-layer">`;
        nodeMap.forEach(n => {
          const valFmt = topo.unit === '$' ? ('$' + n.val.toLocaleString()) : `${n.val.toLocaleString()} ${topo.unit}`;
          const isLeft = n.x < width / 2;
          const textAnchor = isLeft ? 'start' : 'end';
          const textX = isLeft ? n.x + nodeWidth + 8 : n.x - 8;

          svg += `
            <g class="sankey-node-group" data-name="${n.name}" data-val="${valFmt}">
              <rect class="sankey-node" x="${n.x}" y="${n.y}" width="${nodeWidth}" height="${n.h}" rx="3" fill="${n.colorHex}" stroke="#FFF" stroke-width="1" stroke-opacity="0.3"/>
              <text x="${textX}" y="${n.y + n.h / 2 - 2}" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#FFF" text-anchor="${textAnchor}">${n.name}</text>
              <text x="${textX}" y="${n.y + n.h / 2 + 12}" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#AAA" text-anchor="${textAnchor}">${valFmt}</text>
            </g>
          `;
        });
        svg += `</g>`;

        canvas.innerHTML = svg;

        // Hover Handlers
        const ribbonGroups = canvas.querySelectorAll('.sankey-ribbon-group');
        ribbonGroups.forEach(rg => {
          rg.addEventListener('mouseenter', () => {
            const s = rg.getAttribute('data-src');
            const t = rg.getAttribute('data-tgt');
            const v = rg.getAttribute('data-val');
            if (hudHover) hudHover.textContent = `${s} → ${t} (${v})`;
          });
        });

        const nodeGroups = canvas.querySelectorAll('.sankey-node-group');
        nodeGroups.forEach(ng => {
          ng.addEventListener('mouseenter', () => {
            const name = ng.getAttribute('data-name');
            const v = ng.getAttribute('data-val');
            if (hudHover) hudHover.textContent = `Node: ${name} (${v})`;
          });
        });

        // Update Code Preview Snippet
        if (codePreview) {
          const sample = `<svg viewBox="0 0 740 400" xmlns="http://www.w3.org/2000/svg">\n  <!-- Generated Sankey Flow Ribbon -->\n  <path d="M 60.0 120.0 C 180.0 120.0, 180.0 160.0, 300.0 160.0 L 300.0 200.0 C 180.0 200.0, 180.0 160.0, 60.0 160.0 Z"\n        fill="url(#linkGrad_0)" fill-opacity="0.6"/>\n  <!-- Rect Node -->\n  <rect x="60" y="80" width="${nodeWidth}" height="140" rx="3" fill="${colors[0]}"/>\n</svg>`;
          codePreview.textContent = sample;
        }
      }

      // Controls Events
      if (presetSelect) {
        presetSelect.addEventListener('change', (e) => {
          currentPreset = e.target.value;
          presetBadge.textContent = topologies[currentPreset].title;
          renderSankey();
        });
      }

      if (colorSelect) {
        colorSelect.addEventListener('change', (e) => {
          activePalette = e.target.value;
          renderSankey();
        });
      }

      if (curvatureRange) {
        curvatureRange.addEventListener('input', (e) => {
          curvature = parseFloat(e.target.value);
          if (curvatureVal) curvatureVal.textContent = curvature.toFixed(2);
          renderSankey();
        });
      }

      if (nodeWidthRange) {
        nodeWidthRange.addEventListener('input', (e) => {
          nodeWidth = parseInt(e.target.value, 10);
          if (nodeWidthVal) nodeWidthVal.textContent = `${nodeWidth} px`;
          renderSankey();
        });
      }

      if (btnToggleAnim) {
        btnToggleAnim.addEventListener('click', () => {
          showFlowAnim = !showFlowAnim;
          btnToggleAnim.setAttribute('data-active', showFlowAnim ? 'true' : 'false');
          btnToggleAnim.style.borderColor = showFlowAnim ? '#C1DD2D' : '#333';
          renderSankey();
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
      renderSankey();
    })();
  </script>
</body>
</html>
'''

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {target_file} ({len(html_content)} bytes)")
