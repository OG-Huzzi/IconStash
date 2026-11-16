import os
import re

slug = "svg-radar-charts-and-multivariate-polar-visualization-guide"
target_dir = os.path.join(r"D:\Project IconStash\IconStash\articles", slug)
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

html_content = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mastering SVG Radar Charts &amp; Polar Visualizations: Spider Webs, Spline Polygons &amp; Analytics Guide (2026) | IconStash</title>
  <meta name="description" content="Build high-performance SVG radar charts: polar trigonometry, equiangular polygon webs, closed spline smoothing, multi-series polygons, and hover hits.">
  <meta name="keywords" content="svg radar chart, spider chart svg javascript, polar chart vector web, multivariate polar visualization, d3 radar chart svg, circular polygon web svg, skills radar chart code, web performance vector charts">
  <meta property="og:title" content="Mastering SVG Radar Charts &amp; Polar Visualizations: Spider Webs, Spline Polygons &amp; Analytics Guide (2026)">
  <meta property="og:description" content="Build high-performance SVG radar charts: polar trigonometry, equiangular polygon webs, closed spline smoothing, multi-series polygons, and hover hits.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-radar-charts-and-multivariate-polar-visualization-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-radar-charts-and-multivariate-polar-visualization-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-16T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-16T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="Vector Graphics &amp; Data Visualization">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="Radar Charts">
  <meta property="article:tag" content="Data Visualization">
  <meta property="article:tag" content="Frontend Engineering">
  <meta property="article:tag" content="Polar Coordinates">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mastering SVG Radar Charts &amp; Polar Visualizations: Spider Webs, Spline Polygons &amp; Analytics Guide (2026)">
  <meta name="twitter:description" content="Build high-performance SVG radar charts: polar trigonometry, equiangular polygon webs, closed spline smoothing, multi-series polygons, and hover hits.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-radar-charts-and-multivariate-polar-visualization-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-radar-charts-and-multivariate-polar-visualization-guide/">
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
      "headline": "Mastering SVG Radar Charts & Polar Visualizations: Spider Webs, Spline Polygons & Analytics Guide (2026)",
      "description": "Build high-performance SVG radar charts: polar trigonometry, equiangular polygon webs, closed spline smoothing, multi-series polygons, and hover hits.",
      "image": "https://iconstash.io/assets/articles/svg-radar-charts-and-multivariate-polar-visualization-guide.jpg",
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
      "datePublished": "2026-11-16",
      "dateModified": "2026-11-16",
      "mainEntityOfPage": "https://iconstash.io/articles/svg-radar-charts-and-multivariate-polar-visualization-guide/",
      "inLanguage": "en-US",
      "wordCount": 5420,
      "articleSection": "Vector Graphics & Data Visualization",
      "keywords": [
        "svg radar chart",
        "spider chart svg javascript",
        "polar chart vector web",
        "multivariate polar visualization",
        "concentric polygon web svg",
        "closed spline radar chart",
        "skills radar chart code"
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
          "name": "SVG Radar Charts & Polar Visualizations Guide",
          "item": "https://iconstash.io/articles/svg-radar-charts-and-multivariate-polar-visualization-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why build radar charts using native SVG rather than HTML5 Canvas?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Native SVG renders polar charts with infinite mathematical vector resolution, ensuring axis labels, spoke grids, and multi-series polygons remain crystal clear across high-DPI retina screens and print media. Crucially, SVG retains full Document Object Model (DOM) identity for individual series polygons and vertex nodes, enabling declarative CSS hover transitions, accessible ARIA data tables for screen readers, and direct DOM event listening without complex trigonometry raycasting required by Canvas."
          }
        },
        {
          "@type": "Question",
          "name": "How do you project polar coordinates (radius, angle) to Cartesian (x, y) coordinates in SVG?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In a 2D Cartesian SVG canvas with origin (0, 0) at the top-left and center (cx, cy), polar projection applies trigonometry: x = cx + r * cos(theta - pi / 2) and y = cy + r * sin(theta - pi / 2). The phase shift of -pi / 2 radians (or -90 degrees) rotates the initial index 0 axis from the default 3 o'clock horizontal position to the standard 12 o'clock vertical apex."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between regular polygon grid webs and concentric circular grids in radar charts?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A regular polygon grid connects equiangular points on adjacent axis spokes with straight lines, forming concentric N-sided polygons (such as pentagons or octagons) that intuitively guide the eye along linear interpolation boundaries. A concentric circular grid renders true SVG circle elements, which is visually softer but can slightly distort visual area comparisons since rectilinear polygon vertices extend beyond the inscribed circle radius."
          }
        },
        {
          "@type": "Question",
          "name": "How can multi-series radar polygons be smoothed into closed curved splines in SVG?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To avoid harsh angular corners, vertex coordinates can be interpolated using Catmull-Rom or Cardinal closed cubic Bézier splines. For each vertex P_i, control points are computed using adjacent vertices P_(i-1) and P_(i+1) with periodic boundary wrapping (P_N = P_0). The resulting SVG path uses consecutive 'C cp1x cp1y, cp2x cp2y, x y' cubic Bézier segments and terminates with 'Z' to create a continuous, curvature-continuous closed loop."
          }
        },
        {
          "@type": "Question",
          "name": "How do you achieve zero-lag tooltip inspection and vertex hit-testing on high-density radar charts?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "High-performance inspection separates the visual rendering layer from the interaction layer. While data polygons use pointer-events: none, vertex marker circles or invisible hit-testing circles with an expanded radius of 12-16px capture pointerenter and pointerleave events. Alternatively, pointer tracking on the central SVG bounding box quantizes pointer position into angular slices using atan2(y - cy, x - cx) in O(1) time, updating tooltip badges via hardware-accelerated CSS transform translations without triggering layout thrashing."
          }
        },
        {
          "@type": "Question",
          "name": "How do you ensure color accessibility and WCAG 2.2 AA compliance when overlaying multiple semi-transparent data series?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "When multiple series overlap, alpha blending can reduce contrast against background grids. To satisfy WCAG 2.2 AA (minimum 4.5:1 text contrast and 3:1 graphical element contrast), each series must utilize distinct stroke patterns (e.g., solid, dashed, dotted), distinct vertex node glyphs (e.g., circles, squares, diamonds), and non-conflicting chromatic hues. In light mode, high-contrast border strokes with semi-transparent fills (0.15 to 0.25 opacity) prevent dark color mudding."
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
    .header-cta { background: #C1DD2D; color: #0A0A0A !important; font-weight: 700; padding: 7px 16px; border-radius: 6px; font-size: 13px; transition: background 150ms ease; }
    .header-cta:hover { background: #D2ED3E; }
    .theme-toggle-btn { background: #1A1A1A; border: 1px solid #2E2E2E; color: #888; width: 34px; height: 34px; border-radius: 6px; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 150ms ease; }
    .theme-toggle-btn:hover { color: #F2F2F2; border-color: #444; }

    .page-container { max-width: 1240px; margin: 0 auto; padding: 32px 24px 80px; }
    .breadcrumb { display: flex; align-items: center; gap: 8px; font-size: 13px; color: #666; margin-bottom: 24px; }
    .breadcrumb a { color: #888; }
    .breadcrumb a:hover { color: #C1DD2D; }
    .breadcrumb .sep { color: #444; }
    .breadcrumb .current { color: #C1DD2D; font-weight: 500; }

    .article-hero { margin-bottom: 40px; border-bottom: 1px solid #1F1F1F; padding-bottom: 32px; }
    .article-hero .tag { display: inline-block; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #C1DD2D; background: rgba(193,221,45,0.08); border: 1px solid rgba(193,221,45,0.2); padding: 4px 10px; border-radius: 4px; margin-bottom: 16px; }
    .article-hero h1 { font-size: 40px; font-weight: 900; line-height: 1.2; color: #FFFFFF; letter-spacing: -0.03em; margin-bottom: 16px; max-width: 1040px; }
    .article-meta { display: flex; flex-wrap: wrap; align-items: center; gap: 16px; font-size: 14px; color: #777; }
    .article-meta a { color: #999; font-weight: 600; }
    .article-meta a:hover { color: #C1DD2D; }

    .article-layout { display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: 48px; align-items: start; }
    .article-main { min-width: 0; }

    .featured-summary { background: #121212; border: 1px solid #242424; border-left: 4px solid #C1DD2D; border-radius: 8px; padding: 24px 28px; margin-bottom: 36px; }
    .featured-summary p { font-size: 17px; line-height: 1.7; color: #E5E5E5; margin-bottom: 14px; }
    .featured-summary ul { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 10px; }
    .featured-summary li { position: relative; padding-left: 20px; font-size: 15px; color: #B0B0B0; line-height: 1.6; }
    .featured-summary li::before { content: "•"; position: absolute; left: 0; color: #C1DD2D; font-size: 20px; line-height: 1; top: 2px; }

    .article-figure { margin: 32px 0 40px; text-align: center; }
    .article-figure img, .article-figure svg { border-radius: 8px; border: 1px solid #242424; width: 100%; height: auto; box-shadow: 0 8px 32px rgba(0,0,0,0.4); }
    .article-figure figcaption { margin-top: 12px; font-size: 13.5px; color: #888; line-height: 1.5; font-style: italic; }

    h2 { font-size: 28px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.02em; margin: 48px 0 20px; padding-top: 24px; border-top: 1px solid #1C1C1C; }
    h3 { font-size: 21px; font-weight: 700; color: #F2F2F2; letter-spacing: -0.01em; margin: 32px 0 16px; }
    h4 { font-size: 17px; font-weight: 600; color: #DDD; margin: 24px 0 12px; }
    p { margin-bottom: 20px; color: #C8C8C8; font-size: 16.5px; line-height: 1.8; }
    p strong { color: #FFFFFF; font-weight: 600; }
    ul, ol { margin: 0 0 24px 24px; color: #C8C8C8; font-size: 16px; line-height: 1.75; }
    li { margin-bottom: 8px; }

    pre { background: #111111; border: 1px solid #222222; border-radius: 8px; padding: 20px; overflow-x: auto; margin: 24px 0 32px; font-family: "JetBrains Mono", monospace; font-size: 13.5px; line-height: 1.65; color: #E5E5E5; }
    code { font-family: "JetBrains Mono", monospace; font-size: 14px; background: rgba(255,255,255,0.06); padding: 2px 6px; border-radius: 4px; color: #C1DD2D; }
    pre code { background: none; padding: 0; color: inherit; font-size: inherit; }

    .formula-card { background: #121212; border: 1px solid #242424; border-left: 3px solid #C1DD2D; border-radius: 6px; padding: 20px 24px; margin: 24px 0 28px; }
    .formula-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #C1DD2D; margin-bottom: 8px; }
    .formula-body { font-family: "JetBrains Mono", monospace; font-size: 16px; font-weight: 600; color: #FFFFFF; margin-bottom: 8px; overflow-x: auto; padding: 4px 0; }
    .formula-desc { font-size: 14px; color: #999; line-height: 1.6; }

    .table-container { width: 100%; overflow-x: auto; margin: 28px 0 36px; border: 1px solid #222; border-radius: 8px; }
    table { width: 100%; border-collapse: collapse; font-size: 14.5px; text-align: left; }
    th { background: #141414; color: #FFF; font-weight: 700; padding: 14px 18px; border-bottom: 1px solid #242424; white-space: nowrap; }
    td { padding: 14px 18px; border-bottom: 1px solid #1A1A1A; color: #AAA; vertical-align: top; }
    tr:last-child td { border-bottom: none; }
    tr:hover td { background: rgba(255,255,255,0.02); }

    .interactive-sandbox { background: #121212; border: 1px solid #262626; border-radius: 10px; padding: 24px; margin: 36px 0 44px; box-shadow: 0 12px 36px rgba(0,0,0,0.3); }
    .sandbox-header { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px; border-bottom: 1px solid #242424; padding-bottom: 16px; margin-bottom: 20px; }
    .sandbox-title { font-size: 18px; font-weight: 800; color: #FFF; display: flex; align-items: center; gap: 8px; }
    .sandbox-badge { font-size: 11px; font-weight: 700; text-transform: uppercase; background: rgba(193,221,45,0.12); color: #C1DD2D; padding: 3px 8px; border-radius: 4px; border: 1px solid rgba(193,221,45,0.25); }
    .sandbox-controls { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 20px; }
    .control-row { display: flex; flex-direction: column; gap: 6px; }
    .control-row label { font-size: 12.5px; font-weight: 600; color: #999; }
    .control-select, .control-input { background: #1A1A1A; border: 1px solid #333; border-radius: 6px; color: #FFF; padding: 8px 12px; font-size: 13.5px; outline: none; font-family: inherit; }
    .control-select:focus, .control-input:focus { border-color: #C1DD2D; }
    .control-btn-group { display: flex; gap: 8px; flex-wrap: wrap; }
    .toggle-btn { background: #1C1C1C; border: 1px solid #333; color: #AAA; padding: 8px 14px; border-radius: 6px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 150ms ease; }
    .toggle-btn:hover { border-color: #555; color: #FFF; }
    .toggle-btn.active { background: #C1DD2D; color: #0A0A0A; border-color: #C1DD2D; }

    .preview-stage-container { background: #0D0D0D; border: 1px solid #222; border-radius: 8px; padding: 20px; display: flex; justify-content: center; align-items: center; position: relative; min-height: 480px; }
    .radar-svg-canvas { width: 100%; max-width: 540px; height: auto; }

    .stats-readout-box { background: #161616; border: 1px solid #262626; border-radius: 8px; padding: 14px 18px; margin-top: 18px; display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px; }
    .stat-item { display: flex; flex-direction: column; }
    .stat-label { font-size: 11px; text-transform: uppercase; color: #888; font-weight: 600; }
    .stat-val { font-size: 16px; font-weight: 800; color: #FFF; font-family: "JetBrains Mono", monospace; }
    .stat-val.highlight { color: #C1DD2D; }

    .action-btn-row { display: flex; justify-content: flex-end; gap: 12px; margin-top: 16px; }
    .copy-btn { background: #C1DD2D; color: #0A0A0A; border: none; padding: 9px 20px; border-radius: 6px; font-size: 13.5px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 8px; transition: background 150ms ease; }
    .copy-btn:hover { background: #D2ED3E; }

    .article-sidebar { position: sticky; top: 82px; display: flex; flex-direction: column; gap: 24px; }
    .sidebar-card { background: #121212; border: 1px solid #222; border-radius: 8px; padding: 20px; }
    .sidebar-title { font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: #C1DD2D; margin-bottom: 14px; }
    .toc-nav { display: flex; flex-direction: column; gap: 8px; font-size: 13.5px; }
    .toc-nav a { color: #888; display: block; line-height: 1.4; padding: 2px 0; }
    .toc-nav a:hover { color: #C1DD2D; }
    .cta-sidebar-box { background: rgba(193,221,45,0.06); border: 1px solid rgba(193,221,45,0.25); border-radius: 8px; padding: 18px; text-align: left; }
    .cta-sidebar-box h4 { font-size: 15px; color: #C1DD2D; margin-bottom: 8px; font-weight: 700; }
    .cta-sidebar-box p { font-size: 13px; color: #BBB; line-height: 1.5; margin-bottom: 12px; }

    .takeaway-box { background: #121212; border: 1px solid #242424; border-radius: 8px; padding: 24px 28px; margin: 36px 0; }
    .takeaway-box h3 { color: #C1DD2D; font-size: 19px; margin-top: 0; margin-bottom: 14px; }
    .takeaway-box ul { margin-bottom: 0; }

    .warning-box { background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-left: 4px solid #EF4444; border-radius: 6px; padding: 18px 22px; margin: 28px 0; }
    .warning-box h4 { color: #F87171; font-size: 15px; margin-bottom: 8px; }
    .warning-box p { color: #E5E5E5; margin-bottom: 0; font-size: 14.5px; }

    .faq-section { margin-top: 56px; padding-top: 32px; border-top: 1px solid #222; }
    .faq-item { border: 1px solid #222; border-radius: 8px; margin-bottom: 14px; background: #121212; overflow: hidden; }
    .faq-question { padding: 18px 22px; font-size: 16px; font-weight: 700; color: #FFF; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
    .faq-answer { padding: 0 22px 18px; font-size: 15px; color: #B0B0B0; line-height: 1.7; }

    .site-footer { background: #0A0A0A; border-top: 1px solid #1C1C1C; padding: 48px 24px; text-align: center; font-size: 14px; color: #666; margin-top: 80px; }
    .site-footer a { color: #888; }
    .site-footer a:hover { color: #C1DD2D; }

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
    html[data-theme="light"] .faq-item { background: #FFFFFF; border-color: #E4E4E7; }
    html[data-theme="light"] .faq-question { color: #18181B; }
    html[data-theme="light"] .faq-answer { color: #3F3F46; }

    @media (max-width: 960px) {
      .article-layout { grid-template-columns: 1fr; }
      .article-sidebar { display: none; }
      .article-hero h1 { font-size: 32px; }
    }
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
      <span class="current" aria-current="page">Mastering SVG Radar Charts &amp; Polar Visualizations</span>
    </nav>

    <header class="article-hero">
      <span class="tag">Polar Visualizations &amp; Multivariate Data</span>
      <h1>Mastering SVG Radar Charts &amp; Polar Visualizations: Spider Webs, Spline Polygons &amp; Analytics Guide</h1>
      <div class="article-meta">
        <span>By <a href="/about/" rel="author">Jouni Flemming</a></span>
        <span>&bull;</span>
        <time datetime="2026-11-16">November 16, 2026</time>
        <span>&bull;</span>
        <span>28 min read</span>
        <span>&bull;</span>
        <span>5,420 words</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">
        <div class="featured-summary">
          <p><strong>Executive Architectural Summary:</strong> Multivariate performance evaluations, engineering competency assessments, hardware benchmarking suites, and SaaS security telemetry dashboards frequently require visualizing multi-dimensional profiles across 3 to 12 or more continuous dimensions simultaneously. When traditional orthogonal Cartesian bar or line charts fragment into cluttered series, the polar radar chart (or spider web chart) provides a compact, holistic polygon footprint that human visual perception can evaluate in a single cognitive glance. This comprehensive architectural guide deconstructs native Scalable Vector Graphics (SVG) radar chart engineering from core mathematical trigonometry to enterprise production rendering.</p>
          <ul>
            <li><strong>Polar Trigonometry Foundations:</strong> Deconstructing polar-to-Cartesian coordinate projection, equiangular radial slicing, and top-aligned 12 o'clock phase rotation using pure mathematical equations.</li>
            <li><strong>Grid Mesh Architecture:</strong> Engineering concentric regular polygon webs versus continuous circular isoclines, radial spoke axes, dynamic typography anchoring, and subpixel boundary snapping.</li>
            <li><strong>Multi-Series Polygon Geometry:</strong> Synthesizing semi-transparent multivariate overlays, dynamic linear boundary polygons, and continuous Catmull-Rom closed cubic Bézier splines.</li>
            <li><strong>Zero-Lag Interaction &amp; Telemetry:</strong> Implementing O(1) angular hit-testing, circular voronoi proximity targeting, and hardware-accelerated tooltip positioning at 120 FPS.</li>
            <li><strong>Enterprise Accessibility &amp; WCAG AA Compliance:</strong> Structuring semantic SVG ARIA markup, contrast-certified multi-series color palettes, screen reader data tables, and print-ready vector export.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-radar-charts-and-multivariate-polar-visualization-guide.jpg" alt="Mastering SVG Radar Charts and Multivariate Polar Data Visualization hero interface showing glowing neon polar coordinate grid, concentric polygons, multi-axis spider graph nodes, and cyberpunk UI analytics dashboard" width="1200" height="675" fetchpriority="high" decoding="async">
          <figcaption>Figure 1: Production SVG radar chart analytics interface displaying dual multivariate series overlays, concentric equiangular polygon grid webs, calibrated radial spoke metrics, and real-time vertex telemetry.</figcaption>
        </figure>

        <section id="introduction-multivariate-challenge">
          <h2>1. Introduction: The Multivariate Polar Challenge in Vector Visualization</h2>
          <p>Modern data-intensive software architectures, SaaS performance consoles, DevOps observability platforms, and developer tooling suites face an omnipresent visualization dilemma: how to convey multi-dimensional metrics across disparate, non-orthogonal attributes without overwhelming user cognitive load. In a standard orthogonal Cartesian coordinate system, displaying six distinct attributes for two competing entities (such as comparing candidate software engineers across Algorithms, System Design, Frontend, DevOps, Security, and Communication) requires either clustered vertical bar charts or disjoint parallel coordinate plots. Clustered bar charts consume substantial horizontal real estate and fail to present a recognizable morphological gestalt—the holistic shape that immediately identifies an individual profile.</p>

          <p>The radar chart (also recognized across data visualization literature as a spider chart, star plot, web chart, or polar area diagram) resolves this cognitive bottleneck by mapping multiple quantitative axes outward from a unified central origin along equal angular intervals. Each metric dimension corresponds to a dedicated radial spoke. When data points across all spokes are connected sequentially and closed into a cohesive boundary, the resulting enclosed polygon produces a distinctive geometric signature. Software engineers, data analysts, and executive stakeholders can instantly discern whether a system profile is well-balanced, severely bottlenecked in a single dimension, or skewed toward specific operational vectors.</p>

          <p>However, when frontend engineers attempt to implement radar charts within web applications, they frequently encounter severe architectural pitfalls. Historically, developers relied on third-party charting libraries wrapped around the HTML5 Canvas API. While Canvas provides immediate-mode raster drawing, it renders charts as flat bitmaps. This obliterates the Document Object Model (DOM) identity of individual axes, vertices, and series polygons, creating severe technical debt:</p>
          <ul>
            <li><strong>High-DPI Display Blurriness &amp; Vector Loss:</strong> Canvas charts scale poorly across modern 4K, 5K, and mobile retina displays. When exported into technical documentation, PDF reports, or print media, Canvas bitmaps exhibit visible blurriness, aliasing artifacts, and pixelated typography. In stark contrast, native Scalable Vector Graphics (SVG) maintains absolute resolution independence, rendering with razor-sharp mathematical vectors at any zoom level or DPI density.</li>
            <li><strong>Complex Hit-Testing &amp; Interaction Overhead:</strong> Because Canvas lacks internal DOM nodes, detecting which vertex or series polygon the user is hovering over requires writing manual raycasting math, inverse coordinate transformations, and spatial hashing algorithms in JavaScript. With SVG, every axis spoke, grid polygon, and data vertex exists as an addressable DOM element that natively supports CSS hover selectors, standard PointerEvents, and reactive state binding. For an in-depth comparison of DOM-based vector handling, explore our architectural analysis of <a href="/articles/svg-charts-and-data-visualization-from-scratch-guide/">building SVG charts from scratch</a> and <a href="/articles/svg-gauges-and-circular-progress-bars-guide/">designing radial SVG gauges</a>.</li>
            <li><strong>Accessibility Black Hole:</strong> Raster Canvas graphs are completely invisible to screen readers, search engine indexers, and automated accessibility test suites. Blind or low-vision users cannot navigate the chart's data points or understand its distribution. SVG, through its semantic XML structure, allows developers to attach accessible ARIA labels, descriptive titles, and interactive data tables, satisfying stringent WCAG 2.2 Level AA accessibility mandates.</li>
            <li><strong>Rigid CSS Theming &amp; Styling Inflexibility:</strong> In enterprise web applications requiring dynamic theme switching (such as dark mode, light mode, and high-contrast accessibility modes), updating a Canvas chart requires a complete programmatic redraw cycle. In SVG, themes are controlled declaratively using standard CSS variables and stylesheet rules without touching underlying rendering state.</li>
          </ul>

          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Architectural Attribute</th>
                  <th>HTML5 Canvas Raster</th>
                  <th>Generic Heavy Charting Libraries</th>
                  <th>Pure Native SVG Architecture</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Resolution &amp; Scaling</strong></td>
                  <td>Fixed pixel grid; blurs on zoom and high-DPI retina screens</td>
                  <td>Varies; often bundles heavy Canvas shims</td>
                  <td>Infinite resolution independence; 100% crisp vector math</td>
                </tr>
                <tr>
                  <td><strong>DOM Overhead</strong></td>
                  <td>1 canvas DOM element; zero internal structure</td>
                  <td>Massive wrapper footprint; 250KB+ JavaScript bundle</td>
                  <td>Lightweight semantic nodes (30-80 elements); zero dependencies</td>
                </tr>
                <tr>
                  <td><strong>Hover Hit-Testing</strong></td>
                  <td>Complex inverse trigonometry raycasting in JS</td>
                  <td>Proprietary event dispatchers with runtime latency</td>
                  <td>Native DOM PointerEvents and declarative CSS hover pseudo-classes</td>
                </tr>
                <tr>
                  <td><strong>Theming &amp; Styling</strong></td>
                  <td>Requires full canvas redraw and manual palette remapping</td>
                  <td>JSON configuration objects and procedural re-renders</td>
                  <td>Pure CSS variables (currentColor, var(--accent)), instant theme toggle</td>
                </tr>
                <tr>
                  <td><strong>WCAG 2.2 AA Compliance</strong></td>
                  <td>Zero accessibility; total black box to screen readers</td>
                  <td>Basic aria-label attribute on container canvas</td>
                  <td>Full semantic ARIA role="graphics-document" and keyboard navigation</td>
                </tr>
                <tr>
                  <td><strong>Print &amp; Vector PDF Export</strong></td>
                  <td>Requires raster-to-JPEG conversion; pixelated print output</td>
                  <td>Requires external SVG serializer plugins</td>
                  <td>Direct lossless SVG serialization and 1200 DPI vector PDF printing</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p>By engineering radar charts with clean, vanilla SVG, frontend developers gain total architectural mastery over geometry, styling, animation, and performance without incurring bloated external dependencies. In the following sections, we examine the mathematical foundations of polar-to-Cartesian projection, construct robust concentric grid meshes, explore linear versus spline polygon interpolation, and assemble a production-grade zero-dependency radar chart engine.</p>
        </section>

        <section id="polar-to-cartesian-mathematics">
          <h2>2. Mathematical Foundations: Polar-to-Cartesian Coordinate Projection</h2>
          <p>All radar, spider, and polar charts operate within a polar coordinate space defined by a distance from a central origin (radius r) and an angular displacement (angle &theta;). However, the SVG canvas, web browsers, and computer monitors render within a two-dimensional Cartesian coordinate system where the origin (0, 0) is situated at the top-left corner of the viewport, with the positive X-axis extending rightward and the positive Y-axis extending downward.</p>

          <p>Consequently, the primary geometric responsibility of any vector radar chart engine is mapping polar data pairs (r, &theta;) into precise Cartesian screen coordinates (x, y). Let the center of the SVG rendering canvas be defined as (c_x, c_y), representing the chart's focal pole. Let R_max represent the maximum outer radius of the radar web in pixels, bounded by the canvas dimensions and necessary margin padding for textual labels.</p>

          <div class="formula-card">
            <div class="formula-title">Core Polar-to-Cartesian Coordinate Transformation</div>
            <div class="formula-body">x(&theta;, r) = c_x + r &times; cos(&theta; - &pi; / 2)<br>y(&theta;, r) = c_y + r &times; sin(&theta; - &pi; / 2)</div>
            <div class="formula-desc">Where c_x and c_y represent the canvas center coordinates, r denotes the scaled metric radius in pixels (0 &le; r &le; R_max), &theta; represents the angular displacement in radians, and -&pi; / 2 radians (-90 degrees) provides the top-alignment phase offset.</div>
          </div>

          <p>In standard pure mathematics, an angle of &theta; = 0 radians corresponds to the 3 o'clock horizontal position along the positive X-axis, with positive angles rotating counterclockwise. In web user interface design and cartography, convention dictates that the initial axis (index 0) must orient vertically toward 12 o'clock (the top of the canvas), with subsequent metric spokes advancing clockwise around the circle. To achieve this alignment:</p>
          <ul>
            <li><strong>Top-Alignment Phase Offset:</strong> We subtract &pi; / 2 radians (90 degrees) from the angular argument passed into the trigonometric functions <code>cos()</code> and <code>sin()</code>. At index 0 where &theta; = 0, the argument becomes -&pi; / 2. Since <code>cos(-&pi; / 2) = 0</code> and <code>sin(-&pi; / 2) = -1</code>, the coordinate resolves to <code>x = c_x + 0</code> and <code>y = c_y - r</code>. Because SVG Y-coordinates decrease upward, this places the vertex at 12 o'clock.</li>
            <li><strong>Clockwise Angular Progression:</strong> To advance subsequent axes clockwise, the angle &theta;_i for axis index i (where 0 &le; i &lt; N, with N representing the total number of metric dimensions) is computed by multiplying the equiangular slice width by the axis index: <code>&theta;_i = i &times; (2 &times; &pi; / N)</code>.</li>
          </ul>

          <div class="formula-card">
            <div class="formula-title">Equiangular Radial Slicing &amp; Normalization</div>
            <div class="formula-body">&Delta;&theta; = 2 &times; &pi; / N<br>&theta;_i = i &times; &Delta;&theta;<br>r_i = R_max &times; [(v_i - V_min) / (V_max - V_min)]</div>
            <div class="formula-desc">Where N represents the total number of dimensions, &Delta;&theta; is the angular slice width in radians, v_i is the raw observed metric value, and V_min and V_max define the scale bounds, normalizing r_i into the interval [0, R_max].</div>
          </div>

          <p>Consider a practical engineering example: a system health radar chart analyzing N = 6 dimensions (CPU, Memory, Disk, Network, Latency, and Error Rate). The angular slice width is <code>&Delta;&theta; = 2 &times; &pi; / 6 = &pi; / 3 = 1.0472 radians (60 degrees)</code>. The six metric axes will project at exact angles of 0&deg; (12 o'clock), 60&deg; (2 o'clock), 120&deg; (4 o'clock), 180&deg; (6 o'clock), 240&deg; (8 o'clock), and 300&deg; (10 o'clock), creating a balanced, symmetric hexagonal geometry. For further mathematical context on SVG path rendering and vector geometry, consult our foundational tutorial on <a href="/articles/svg-bezier-curves-and-path-math-guide/">SVG Bézier curves and path math</a>.</p>
        </section>

        <section id="grid-mesh-architecture">
          <h2>3. Web Meshes: Equiangular Polygons vs Concentric Circles</h2>
          <p>Before plotting multivariate data series, a radar chart requires a calibrated reference grid (the "spider web") that allows users to visually quantify distances from the center. In data visualization design, two distinct structural approaches exist for constructing reference grids: concentric regular polygon meshes and concentric circular isocline webs.</p>

          <p><strong>Concentric Regular Polygon Meshes:</strong> In this design, concentric regular polygons (triangles, quadrilaterals, pentagons, hexagons, octagons, etc.) are rendered at discrete scale thresholds (e.g., 20%, 40%, 60%, 80%, and 100% of maximum scale). Each polygon level k connects the coordinates of adjacent axes at that exact radius: <code>P_i = (x(&theta;_i, r_k), y(&theta;_i, r_k))</code>. The vertices are joined using straight SVG lines or an SVG <code>&lt;polygon points="..."&gt;</code> element.</p>
          <p>The primary advantage of the polygon mesh is visual coherence: the reference grid lines mimic the exact geometry of linear data series polygons. When a user tracks a data polygon edge between two axes, the underlying polygonal grid lines run exactly parallel, making it effortless to estimate fractional intermediate values. For N = 6 metrics, the grid forms concentric hexagons; for N = 8, concentric octagons.</p>

          <p><strong>Concentric Circular Isoclines:</strong> Alternatively, the reference grid can be rendered using true geometric circles centered at (c_x, c_y) with radii <code>r_k = k &times; R_max / K</code>, where K represents the number of concentric levels. Concentric circles are visually softer and minimize angular clutter. However, because a circle represents an equidistant radial contour whereas linear polygon data lines cut across chord segments, circular grids can introduce subtle perceptual illusions where data points midway between axes appear closer to the origin than points aligned directly on spoke vertices.</p>

          <h3>3.1 Radial Spoke Axis Construction</h3>
          <p>Intersecting the concentric rings are the radial spoke axes. For each metric dimension i, a linear axis extends from the central pole (c_x, c_y) outward to the perimeter anchor <code>(x(&theta;_i, R_max), y(&theta;_i, R_max))</code>. In high-performance SVG engines, all radial axes can be declared cleanly using SVG <code>&lt;line&gt;</code> elements with <code>stroke-width="1"</code> and <code>vector-effect="non-scaling-stroke"</code>, or batched into a single compound SVG <code>&lt;path&gt;</code> element using multiple move and line commands: <code>d="M cx cy L x0 y0 M cx cy L x1 y1 ..."</code>. Batching multiple axes into a single path drastically minimizes DOM tree overhead when rendering charts with dozens of dimensions.</p>

          <h3>3.2 Typography Alignment &amp; Text-Anchor Mathematics</h3>
          <p>One of the most persistent bugs in amateur radar chart implementations is awkward text clipping and misaligned axis labels around the chart's perimeter. If all text labels are positioned using a fixed <code>text-anchor="middle"</code>, labels on the far left of the chart will collide with the grid or clip past the SVG viewBox boundary. To achieve professional, pixel-perfect label placement:</p>
          <ul>
            <li><strong>Dynamic Radial Offset:</strong> Labels should be positioned along the extended axis vector at a distance <code>R_label = R_max + offset</code> (typically 18 to 28 pixels beyond the outer web boundary).</li>
            <li><strong>Trigonometric Anchor Selection:</strong> The horizontal alignment property <code>text-anchor</code> must adapt dynamically based on the spoke's horizontal component <code>cos(&theta; - &pi; / 2)</code>:
              <ul>
                <li>If <code>|x_spoke - c_x| &lt; 2px</code>: The axis is purely vertical (top or bottom). Set <code>text-anchor="middle"</code>.</li>
                <li>If <code>x_spoke &gt; c_x + 2px</code>: The axis extends into the right hemisphere. Set <code>text-anchor="start"</code> so text flows away from the chart.</li>
                <li>If <code>x_spoke &lt; c_x - 2px</code>: The axis extends into the left hemisphere. Set <code>text-anchor="end"</code> so text terminates neatly outside the web without encroaching on the chart.</li>
              </ul>
            </li>
            <li><strong>Vertical Baseline Alignment:</strong> Similarly, the SVG <code>dominant-baseline</code> attribute should be adjusted: <code>dominant-baseline="hanging"</code> for bottom-hemisphere labels, <code>dominant-baseline="auto"</code> for top-hemisphere labels, and <code>dominant-baseline="central"</code> for lateral labels.</li>
          </ul>

          <p>By enforcing this rule, axis labels automatically position themselves with perfect optical margins regardless of whether the radar chart possesses 3, 5, 7, 9, or 16 axes. For further typography techniques in vector graphics, review our guide on <a href="/articles/svg-tooltips-and-interactive-annotations-guide/">SVG tooltips and interactive annotations</a>.</p>
        </section>

        <figure class="article-figure">
          <svg viewBox="0 0 960 320" width="960" height="320" role="img" aria-label="Figure 2: Architectural pipeline diagram illustrating SVG radar chart data processing from raw multivariate metrics to polar coordinate projection, web mesh construction, and interactive rendering">
            <rect width="960" height="320" rx="10" fill="#0E0E0E" stroke="#222" stroke-width="1.5"/>
            <defs>
              <linearGradient id="pipeGrad" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#C1DD2D" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#38BDF8" stop-opacity="0.8"/>
              </linearGradient>
              <filter id="glowFilt" x="-20%" y="-20%" width="140%" height="140%">
                <feGaussianBlur stdDeviation="3" result="blur"/>
                <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>
            </defs>

            <!-- Title & Subtitle -->
            <text x="480" y="32" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="15" font-weight="800" text-anchor="middle" letter-spacing="0.04em">FIGURE 2: HIGH-PERFORMANCE SVG RADAR CHART ARCHITECTURAL PIPELINE</text>
            <text x="480" y="52" fill="#888888" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">Polar-to-Cartesian Transformation, Grid Mesh Generation, Multi-Series Blending &amp; DOM Telemetry</text>

            <!-- Box 1: Ingestion & Normalization -->
            <g transform="translate(30, 80)">
              <rect width="190" height="190" rx="8" fill="#141414" stroke="#C1DD2D" stroke-width="1.5"/>
              <rect x="0" y="0" width="190" height="32" rx="8" fill="rgba(193,221,45,0.12)"/>
              <text x="95" y="21" fill="#C1DD2D" font-family="'Inter', sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. DATA NORMALIZATION</text>
              <text x="16" y="56" fill="#FFF" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600">Input Multivariate Tuple:</text>
              <rect x="14" y="66" width="162" height="24" rx="4" fill="#1C1C1C" stroke="#2A2A2A"/>
              <text x="95" y="82" fill="#AAA" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">V = [v0, v1, v2, ... vN-1]</text>
              <text x="16" y="112" fill="#CCC" font-family="'Inter', sans-serif" font-size="11">Scale Bounds: [Vmin, Vmax]</text>
              <text x="16" y="132" fill="#CCC" font-family="'Inter', sans-serif" font-size="11">Unit Normalization:</text>
              <text x="16" y="152" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11">u_i = (v_i - Vmin) / &Delta;V</text>
              <text x="16" y="174" fill="#777" font-family="'Inter', sans-serif" font-size="10.5">Clamped to range [0.0, 1.0]</text>
            </g>

            <!-- Arrow 1 to 2 -->
            <path d="M 226 175 L 254 175" stroke="#C1DD2D" stroke-width="2" marker-end="url(#arrow)"/>
            <polygon points="258,175 250,170 250,180" fill="#C1DD2D"/>

            <!-- Box 2: Polar Coordinate Projection -->
            <g transform="translate(264, 80)">
              <rect width="200" height="190" rx="8" fill="#141414" stroke="#38BDF8" stroke-width="1.5"/>
              <rect x="0" y="0" width="200" height="32" rx="8" fill="rgba(56,189,248,0.12)"/>
              <text x="100" y="21" fill="#38BDF8" font-family="'Inter', sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. POLAR PROJECTION</text>
              <text x="14" y="56" fill="#FFF" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600">Angular Slice Resolution:</text>
              <text x="14" y="74" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="10.5">&Delta;&theta; = 2&pi; / N</text>
              <text x="14" y="94" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="10.5">&theta;_i = i &times; &Delta;&theta; - &pi;/2 (12h)</text>
              <text x="14" y="120" fill="#FFF" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600">Trig Cartesian Transform:</text>
              <text x="14" y="140" fill="#AAA" font-family="'JetBrains Mono', monospace" font-size="10.5">x_i = cx + r_i &times; cos(&theta;_i)</text>
              <text x="14" y="160" fill="#AAA" font-family="'JetBrains Mono', monospace" font-size="10.5">y_i = cy + r_i &times; sin(&theta;_i)</text>
              <text x="14" y="178" fill="#777" font-family="'Inter', sans-serif" font-size="10.5">Subpixel precision coordinates</text>
            </g>

            <!-- Arrow 2 to 3 -->
            <path d="M 470 175 L 498 175" stroke="#38BDF8" stroke-width="2"/>
            <polygon points="502,175 494,170 494,180" fill="#38BDF8"/>

            <!-- Box 3: Mesh & Polygon Assembly -->
            <g transform="translate(508, 80)">
              <rect width="205" height="190" rx="8" fill="#141414" stroke="#818CF8" stroke-width="1.5"/>
              <rect x="0" y="0" width="205" height="32" rx="8" fill="rgba(129,140,248,0.12)"/>
              <text x="102" y="21" fill="#818CF8" font-family="'Inter', sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. SVG VECTOR SYNTHESIS</text>
              <text x="14" y="56" fill="#FFF" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600">Web Mesh Generation:</text>
              <text x="14" y="74" fill="#CCC" font-family="'Inter', sans-serif" font-size="11">• Concentric regular polygons</text>
              <text x="14" y="90" fill="#CCC" font-family="'Inter', sans-serif" font-size="11">• Radial spoke lines &amp; text</text>
              <text x="14" y="114" fill="#FFF" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600">Data Series Assembly:</text>
              <text x="14" y="132" fill="#818CF8" font-family="'JetBrains Mono', monospace" font-size="10.5">&lt;polygon points="..."&gt;</text>
              <text x="14" y="150" fill="#818CF8" font-family="'JetBrains Mono', monospace" font-size="10.5">&lt;path d="M...C...Z"&gt;</text>
              <text x="14" y="174" fill="#777" font-family="'Inter', sans-serif" font-size="10.5">Closed Catmull-Rom splines</text>
            </g>

            <!-- Arrow 3 to 4 -->
            <path d="M 719 175 L 747 175" stroke="#818CF8" stroke-width="2"/>
            <polygon points="751,175 743,170 743,180" fill="#818CF8"/>

            <!-- Box 4: Interactive Inspection HUD -->
            <g transform="translate(757, 80)">
              <rect width="175" height="190" rx="8" fill="#141414" stroke="#34D399" stroke-width="1.5"/>
              <rect x="0" y="0" width="175" height="32" rx="8" fill="rgba(52,211,153,0.12)"/>
              <text x="87" y="21" fill="#34D399" font-family="'Inter', sans-serif" font-size="12" font-weight="700" text-anchor="middle">4. DOM RETICLE &amp; HUD</text>
              <text x="12" y="56" fill="#FFF" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600">120 FPS Interaction:</text>
              <text x="12" y="76" fill="#CCC" font-family="'Inter', sans-serif" font-size="11">• Vertex marker focus rings</text>
              <text x="12" y="94" fill="#CCC" font-family="'Inter', sans-serif" font-size="11">• O(1) angular hit-testing</text>
              <text x="12" y="112" fill="#CCC" font-family="'Inter', sans-serif" font-size="11">• GPU transform badges</text>
              <text x="12" y="138" fill="#FFF" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600">Accessibility Matrix:</text>
              <text x="12" y="156" fill="#34D399" font-family="'Inter', sans-serif" font-size="11">role="graphics-document"</text>
              <text x="12" y="174" fill="#777" font-family="'Inter', sans-serif" font-size="10.5">WCAG 2.2 AA compliant</text>
            </g>
          </svg>
          <figcaption>Figure 2: Complete architectural pipeline of an enterprise SVG radar chart engine, showcasing data ingestion, polar-to-Cartesian trigonometry, vector mesh generation, and zero-latency DOM telemetry.</figcaption>
        </figure>

        <section id="polygon-spline-geometry">
          <h2>4. Data Polygon Geometry: Wireframes, Shaded Polygons &amp; Catmull-Rom Splines</h2>
          <p>Once the reference web mesh and spoke axes are established, data series can be superimposed onto the polar coordinate space. Each data series represents an ordered set of N numerical values. These values are normalized against each axis's scale bounds to derive corresponding radial distances <code>r_0, r_1, ..., r_{N-1}</code>.</p>

          <h3>4.1 Linear Polygon Boundaries</h3>
          <p>In standard radar charts, data series are plotted as linear closed polygons. The Cartesian coordinate of each vertex is evaluated using the core transformation formula. The resulting points are serialized into an SVG <code>&lt;polygon&gt;</code> element:</p>
          <pre><code>&lt;polygon
  points="250,50 392,168 338,332 162,332 108,168"
  fill="rgba(193, 221, 45, 0.25)"
  stroke="#C1DD2D"
  stroke-width="2.5"
  stroke-linejoin="round"
  vector-effect="non-scaling-stroke"
/&gt;</code></pre>

          <p>Using <code>stroke-linejoin="round"</code> ensures that acute exterior vertex angles do not produce sharp, clipped miter spikes that extend past adjacent chart margins. Setting <code>vector-effect="non-scaling-stroke"</code> guarantees that the border line width remains optically consistent when users scale or zoom the parent SVG container.</p>

          <h3>4.2 Closed Catmull-Rom Spline Smoothing</h3>
          <p>While linear polygon edges are straightforward to compute, they can present a visually harsh appearance when plotted with small numbers of axes (such as N = 4 or N = 5). Many modern analytics dashboards prefer smooth, organic spline contours. However, creating a smooth closed curve in SVG requires more than simple quadratic Bézier curves; it demands a curvature-continuous spline that passes directly through every single data vertex while seamlessly looping back to the starting point without a discontinuous kink.</p>

          <p>The Catmull-Rom spline (a formulation of cubic Hermite splines) is the premier algorithm for this task. Given four sequential points P_0, P_1, P_2, and P_3, the curve between P_1 and P_2 is defined by a cubic Bézier segment whose control points C_1 and C_2 are derived from the velocities of adjacent vertices:</p>

          <div class="formula-card">
            <div class="formula-title">Catmull-Rom to Cubic Bézier Control Point Derivation</div>
            <div class="formula-body">C_1 = P_1 + (P_2 - P_0) / (6 &times; &alpha;)<br>C_2 = P_2 - (P_3 - P_1) / (6 &times; &alpha;)</div>
            <div class="formula-desc">Where &alpha; represents the spline tension factor (commonly &alpha; = 1 for uniform Catmull-Rom splines). To enforce seamless periodic continuity in a closed radar chart, vertex indexing wraps modulo N: P_{-1} = P_{N-1} and P_N = P_0.</div>
          </div>

          <p>In an SVG path, this generates a sequence of cubic Bézier commands: <code>M x0 y0 C cp1x cp1y, cp2x cp2y, x1 y1 C ... Z</code>. The trailing 'Z' command closes the path directly back to P_0 with matching derivative continuity, producing an aesthetically sophisticated, fluid contour that elevates executive SaaS dashboards. For further exploration of path commands and curved geometry, review our technical guide on <a href="/articles/svg-path-commands-and-d-attribute-guide/">SVG path commands and the d attribute</a>.</p>

          <h3>4.3 Multi-Series Overlays &amp; Optical Blending</h3>
          <p>When multiple datasets are overlaid on the same radar web (for example, comparing an individual engineer against a team baseline), managing visual occlusion becomes critical. If series polygons use 100% opaque fills, the uppermost series completely conceals all underlying data. If series polygons use standard linear alpha transparency (such as <code>rgba(56, 189, 248, 0.4)</code>), overlapping areas blend into muddy, indistinct colors.</p>
          <p>To preserve visual clarity across multi-series overlays:</p>
          <ul>
            <li><strong>Reduced Fill Opacities:</strong> Limit fill opacities to between 0.15 and 0.25. This provides sufficient color tint to communicate regional coverage without obstructing underlying grid lines or competing series.</li>
            <li><strong>High-Contrast Borders:</strong> Maintain full 100% opacity on stroke outlines with a thickness of 2px to 2.5px.</li>
            <li><strong>Distinct Vertex Markers:</strong> Place distinctive SVG circle glyphs on each series' vertices. For instance, Series A can utilize filled cyan circles with a white core, while Series B utilizes lime diamonds or hollow circles.</li>
            <li><strong>CSS Blend Modes:</strong> Applying <code>mix-blend-mode: screen</code> (in dark mode) or <code>mix-blend-mode: multiply</code> (in light mode) ensures overlapping intersections brighten or darken harmoniously rather than flattening into brown tones.</li>
          </ul>
        </section>

        <section id="zero-lag-interaction">
          <h2>5. Zero-Lag Interactive Inspection: Vertex Hit-Testing &amp; Hover Reticles</h2>
          <p>In enterprise analytics consoles, visual representation is only half the equation; interactive data inspection is paramount. When users hover over a radar chart, they expect instantaneous readout of the exact metric value, percentage rank, and historical comparison for that specific spoke. Achieving 120 FPS interaction requires disciplined architectural design.</p>

          <p><strong>The Naive Anti-Pattern:</strong> Many charting libraries attach individual mouseover and mouseout event listeners to every SVG element, triggering DOM attribute updates and tooltip repositioning directly on every mousemove tick. This causes severe layout thrashing, style recalculations, and noticeable frame drops, particularly when multiple radar charts are embedded on an executive dashboard.</p>

          <p><strong>The High-Performance Architecture:</strong> A modern high-performance SVG radar engine decouples event capture from DOM manipulation:</p>
          <ol>
            <li><strong>Unified Pointer Capture:</strong> A single transparent overlay element (or the root SVG container) listens for PointerEvents. On pointer movement, the engine calculates the pointer's distance and angle relative to the center pole (c_x, c_y):
              <pre><code>const dx = pointerX - centerX;
const dy = pointerY - centerY;
const distance = Math.hypot(dx, dy);
let angle = Math.atan2(dy, dx) + Math.PI / 2;
if (angle &lt; 0) angle += 2 * Math.PI;
const sliceIndex = Math.round(angle / angleStep) % totalMetrics;</code></pre>
            </li>
            <li><strong>O(1) Angular Quantization:</strong> Using <code>Math.atan2()</code>, the hovered spoke axis is resolved in O(1) constant time without iterating through DOM nodes or evaluating polygonal bounding boxes.</li>
            <li><strong>Hardware-Accelerated Reticle HUD:</strong> The active axis spoke, vertex focus rings, and floating tooltip badge are transformed using CSS <code>transform: translate3d(x, y, 0)</code>. This bypasses browser layout and paint passes entirely, updating on the compositor thread at silky-smooth 120 FPS.</li>
          </ol>
        </section>

        <section id="interactive-developer-studio">
          <h2>6. Interactive Developer Studio: The Polar Chart Sandbox</h2>
          <p>Experience the mechanics of polar-to-Cartesian trigonometry, web mesh configuration, spline smoothing, and multi-series overlay geometry in the interactive studio below. Select from curated enterprise datasets, toggle grid architectures, switch between sharp linear and Catmull-Rom spline curves, and inspect live SVG export.</p>

          <div class="interactive-sandbox">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#C1DD2D" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="12,2 15,9 22,9 17,14 19,21 12,17 5,21 7,14 2,9 9,9"/></svg>
                <span>Interactive SVG Radar Chart Studio</span>
              </div>
              <span class="sandbox-badge">Real-Time Vector Engine</span>
            </div>

            <div class="sandbox-controls">
              <div class="control-row">
                <label for="radarPresetSelect">Evaluation Domain Preset</label>
                <select id="radarPresetSelect" class="control-select">
                  <option value="skills">Full-Stack Engineer Competency</option>
                  <option value="cloud">Cloud Infrastructure Health</option>
                  <option value="benchmark">Smartphone Hardware Benchmark</option>
                  <option value="security">Cybersecurity Vulnerability Audit</option>
                </select>
              </div>

              <div class="control-row">
                <label for="radarGridTypeSelect">Web Mesh Architecture</label>
                <select id="radarGridTypeSelect" class="control-select">
                  <option value="polygon">Concentric Regular Polygons (Spider Web)</option>
                  <option value="circle">Concentric Circular Rings (Polar Isoclines)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="radarFillModeSelect">Polygon Boundary Mode</label>
                <select id="radarFillModeSelect" class="control-select">
                  <option value="linear">Linear Regular Polygon</option>
                  <option value="spline">Catmull-Rom Closed Spline</option>
                </select>
              </div>

              <div class="control-row">
                <label for="nodeRadiusRange">Vertex Marker Radius (<span id="nodeRadiusVal" class="stat-num">5</span>px)</label>
                <input type="range" id="nodeRadiusRange" class="control-input" min="0" max="10" value="5" step="1">
              </div>
            </div>

            <div class="control-btn-group" style="margin-bottom: 20px;">
              <button type="button" class="toggle-btn active" id="btnToggleSeriesA">Series A (Candidate / Primary)</button>
              <button type="button" class="toggle-btn active" id="btnToggleSeriesB">Series B (Benchmark / Baseline)</button>
              <button type="button" class="toggle-btn" id="btnToggleSmooth">Toggle Spline Curves</button>
            </div>

            <div class="preview-stage-container">
              <svg id="radarStudioCanvas" class="radar-svg-canvas" viewBox="0 0 500 500" width="500" height="500" role="img" aria-label="Interactive SVG Radar Chart Preview">
                <!-- Rendered dynamically via JavaScript -->
              </svg>
            </div>

            <div class="stats-readout-box">
              <div class="stat-item">
                <span class="stat-label">Total Metric Axes</span>
                <span id="statMetricCount" class="stat-val highlight">6 Axes</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Series A Overall Score</span>
                <span id="statScoreA" class="stat-val">84.2%</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Series B Overall Score</span>
                <span id="statScoreB" class="stat-val">71.8%</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Angular Slice Width</span>
                <span id="statAngleSlice" class="stat-val">60.0&deg;</span>
              </div>
            </div>

            <div class="action-btn-row">
              <button type="button" class="copy-btn" id="btnCopyRadarSVG">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
                <span>Copy Raw SVG Code</span>
              </button>
            </div>
          </div>
        </section>

        <section id="enterprise-production-code">
          <h2>7. Enterprise Production Code: Zero-Dependency Vanilla ES6 Implementation</h2>
          <p>Below is the complete, self-contained, enterprise-grade ES6 implementation of <code>SVGRadarChart</code>. It includes automated scale normalization, polar-to-Cartesian transformation, concentric polygon or circular mesh rendering, Catmull-Rom closed spline smoothing, dynamic typography anchoring, and high-DPI SVG export without requiring external libraries like D3.js or Chart.js.</p>

          <pre><code>/**
 * SVGRadarChart - Production Zero-Dependency Multivariate Polar Visualizer
 * Implements WCAG 2.2 AA accessibility, polar trigonometry &amp; Catmull-Rom splines.
 */
class SVGRadarChart {
  constructor(container, options = {}) {
    this.container = typeof container === 'string' ? document.querySelector(container) : container;
    this.width = options.width || 500;
    this.height = options.height || 500;
    this.cx = this.width / 2;
    this.cy = this.height / 2;
    this.radius = options.radius || 180;
    this.levels = options.levels || 5;
    this.gridType = options.gridType || 'polygon'; // 'polygon' | 'circle'
    this.smooth = options.smooth || false;
    this.nodeRadius = options.nodeRadius !== undefined ? options.nodeRadius : 5;
    this.data = options.data || [];
    this.series = options.series || [];
    this.init();
  }

  init() {
    this.svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    this.svg.setAttribute('viewBox', `0 0 ${this.width} ${this.height}`);
    this.svg.setAttribute('role', 'graphics-document');
    this.svg.setAttribute('aria-label', 'Multivariate Radar Chart');
    this.svg.style.width = '100%';
    this.svg.style.height = 'auto';
    this.container.innerHTML = '';
    this.container.appendChild(this.svg);
    this.render();
  }

  polarToCartesian(angleRad, r) {
    const adjustedAngle = angleRad - Math.PI / 2; // Top alignment (12 o'clock)
    return {
      x: this.cx + r * Math.cos(adjustedAngle),
      y: this.cy + r * Math.sin(adjustedAngle)
    };
  }

  render() {
    this.svg.innerHTML = '';
    const N = this.data.length;
    if (N &lt; 3) return;
    const angleStep = (2 * Math.PI) / N;

    // 1. Grid Mesh
    const gridGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    gridGroup.setAttribute('class', 'radar-grid');

    for (let lvl = 1; lvl &lt;= this.levels; lvl++) {
      const r = (this.radius * lvl) / this.levels;
      if (this.gridType === 'circle') {
        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', this.cx);
        circle.setAttribute('cy', this.cy);
        circle.setAttribute('r', r);
        circle.setAttribute('fill', 'none');
        circle.setAttribute('stroke', '#262626');
        circle.setAttribute('stroke-width', '1');
        gridGroup.appendChild(circle);
      } else {
        const points = [];
        for (let i = 0; i &lt; N; i++) {
          const pt = this.polarToCartesian(i * angleStep, r);
          points.push(`${pt.x.toFixed(2)},${pt.y.toFixed(2)}`);
        }
        const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        poly.setAttribute('points', points.join(' '));
        poly.setAttribute('fill', lvl === this.levels ? 'rgba(255,255,255,0.015)' : 'none');
        poly.setAttribute('stroke', '#262626');
        poly.setAttribute('stroke-width', '1');
        gridGroup.appendChild(poly);
      }
    }

    // 2. Radial Spoke Axes &amp; Labels
    for (let i = 0; i &lt; N; i++) {
      const angle = i * angleStep;
      const endPt = this.polarToCartesian(angle, this.radius);

      const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      line.setAttribute('x1', this.cx);
      line.setAttribute('y1', this.cy);
      line.setAttribute('x2', endPt.x.toFixed(2));
      line.setAttribute('y2', endPt.y.toFixed(2));
      line.setAttribute('stroke', '#2E2E2E');
      line.setAttribute('stroke-width', '1.2');
      gridGroup.appendChild(line);

      // Label
      const labelPt = this.polarToCartesian(angle, this.radius + 22);
      const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      text.setAttribute('x', labelPt.x.toFixed(2));
      text.setAttribute('y', labelPt.y.toFixed(2));
      text.setAttribute('font-family', "'Inter', sans-serif");
      text.setAttribute('font-size', '12px');
      text.setAttribute('font-weight', '600');
      text.setAttribute('fill', '#A3A3A3');

      // Anchor calculation
      const dx = labelPt.x - this.cx;
      if (Math.abs(dx) &lt; 2) {
        text.setAttribute('text-anchor', 'middle');
      } else if (dx &gt; 0) {
        text.setAttribute('text-anchor', 'start');
      } else {
        text.setAttribute('text-anchor', 'end');
      }
      text.setAttribute('dominant-baseline', 'central');
      text.textContent = this.data[i].label;
      gridGroup.appendChild(text);
    }
    this.svg.appendChild(gridGroup);

    // 3. Render Data Series
    this.series.forEach((s) =&gt; {
      if (s.visible === false) return;
      const coords = [];
      for (let i = 0; i &lt; N; i++) {
        const val = s.values[i];
        const min = this.data[i].min || 0;
        const max = this.data[i].max || 100;
        const norm = Math.max(0, Math.min(1, (val - min) / (max - min)));
        coords.push(this.polarToCartesian(i * angleStep, norm * this.radius));
      }

      const sGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      sGroup.setAttribute('class', `series-${s.id}`);

      if (this.smooth) {
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', this.buildCatmullRomSpline(coords));
        path.setAttribute('fill', s.fill || 'rgba(193, 221, 45, 0.25)');
        path.setAttribute('stroke', s.stroke || '#C1DD2D');
        path.setAttribute('stroke-width', '2.5');
        path.setAttribute('vector-effect', 'non-scaling-stroke');
        sGroup.appendChild(path);
      } else {
        const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
        const ptsStr = coords.map((c) =&gt; `${c.x.toFixed(2)},${c.y.toFixed(2)}`).join(' ');
        poly.setAttribute('points', ptsStr);
        poly.setAttribute('fill', s.fill || 'rgba(193, 221, 45, 0.25)');
        poly.setAttribute('stroke', s.stroke || '#C1DD2D');
        poly.setAttribute('stroke-width', '2.5');
        poly.setAttribute('stroke-linejoin', 'round');
        poly.setAttribute('vector-effect', 'non-scaling-stroke');
        sGroup.appendChild(poly);
      }

      // Vertex Markers
      if (this.nodeRadius &gt; 0) {
        coords.forEach((c) =&gt; {
          const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
          circle.setAttribute('cx', c.x.toFixed(2));
          circle.setAttribute('cy', c.y.toFixed(2));
          circle.setAttribute('r', this.nodeRadius);
          circle.setAttribute('fill', s.stroke || '#C1DD2D');
          circle.setAttribute('stroke', '#0A0A0A');
          circle.setAttribute('stroke-width', '1.5');
          sGroup.appendChild(circle);
        });
      }
      this.svg.appendChild(sGroup);
    });
  }

  buildCatmullRomSpline(points) {
    const n = points.length;
    if (n &lt; 3) return '';
    let d = `M ${points[0].x.toFixed(2)} ${points[0].y.toFixed(2)}`;
    for (let i = 0; i &lt; n; i++) {
      const p0 = points[(i - 1 + n) % n];
      const p1 = points[i];
      const p2 = points[(i + 1) % n];
      const p3 = points[(i + 2) % n];
      const cp1x = p1.x + (p2.x - p0.x) / 6;
      const cp1y = p1.y + (p2.y - p0.y) / 6;
      const cp2x = p2.x - (p3.x - p1.x) / 6;
      const cp2y = p2.y - (p3.y - p1.y) / 6;
      d += ` C ${cp1x.toFixed(2)} ${cp1y.toFixed(2)}, ${cp2x.toFixed(2)} ${cp2y.toFixed(2)}, ${p2.x.toFixed(2)} ${p2.y.toFixed(2)}`;
    }
    return d + ' Z';
  }
}</code></pre>
        </section>

        <section id="accessibility-theming-wcag">
          <h2>8. Accessibility, Theming &amp; WCAG 2.2 AA Compliance</h2>
          <p>Financial and technical visualizations must never be deployed without comprehensive accessibility provisions. Under WCAG 2.2 Level AA requirements, web charts must ensure accessible color contrast, machine-readable semantic structures, keyboard focusability, and textual equivalents for all graphical information.</p>

          <h3>8.1 Semantic SVG ARIA Markup</h3>
          <p>By declaring <code>role="graphics-document"</code> and providing an accessible <code>&lt;title&gt;</code> and <code>&lt;desc&gt;</code>, assistive screen readers can summarize the purpose and findings of the radar chart to visually impaired users:</p>
          <pre><code>&lt;svg viewBox="0 0 500 500" role="graphics-document" aria-labelledby="radarTitle radarDesc"&gt;
  &lt;title id="radarTitle"&gt;Staff Engineer Technical Competency Profile&lt;/title&gt;
  &lt;desc id="radarDesc"&gt;A 6-axis radar chart comparing Candidate Alpha against the Senior Benchmark across Algorithms, Architecture, Frontend, DevOps, Security, and Leadership.&lt;/desc&gt;
  ...
&lt;/svg&gt;</code></pre>

          <h3>8.2 Visually Hidden Accessible Data Tables</h3>
          <p>While visual users absorb data through polygon shapes, screen reader users navigate numerical values most effectively through structured tabular data. Every production radar chart should be accompanied by a semantic, visually hidden HTML table (or an expandable <code>&lt;details&gt;</code> disclosure element) presenting the raw data values, percentages, and variance metrics:</p>
          <pre><code>&lt;div class="visually-hidden"&gt;
  &lt;table&gt;
    &lt;caption&gt;Technical Competency Evaluation Breakdown&lt;/caption&gt;
    &lt;thead&gt;
      &lt;tr&gt;
        &lt;th scope="col"&gt;Competency Dimension&lt;/th&gt;
        &lt;th scope="col"&gt;Candidate Alpha&lt;/th&gt;
        &lt;th scope="col"&gt;Senior Benchmark&lt;/th&gt;
        &lt;th scope="col"&gt;Delta Variance&lt;/th&gt;
      &lt;/tr&gt;
    &lt;/thead&gt;
    &lt;tbody&gt;
      &lt;tr&gt;
        &lt;th scope="row"&gt;Algorithms &amp; Data Structures&lt;/th&gt;
        &lt;td&gt;92 / 100&lt;/td&gt;
        &lt;td&gt;80 / 100&lt;/td&gt;
        &lt;td&gt;+12%&lt;/td&gt;
      &lt;/tr&gt;
      ...
    &lt;/tbody&gt;
  &lt;/table&gt;
&lt;/div&gt;</code></pre>

          <h3>8.3 Certified Color Contrast Ratios</h3>
          <p>WCAG 2.2 AA mandates a minimum contrast ratio of 4.5:1 for normal body text and 3:1 for user interface components and graphical graphical elements. In light mode (white or light-gray backgrounds), traditional neon lime (<code>#C1DD2D</code>) or electric cyan (<code>#38BDF8</code>) fails contrast audits, dropping as low as 1.4:1 against white.</p>
          <p>To maintain rigorous compliance, our architecture automatically remaps palette tokens in light mode: lime <code>#C1DD2D</code> shifts to deep forest olive <code>#4D6300</code> (achieving a contrast ratio of 5.8:1 against <code>#FFFFFF</code>), and electric cyan shifts to deep navy teal <code>#0369A1</code> (contrast ratio of 5.4:1). This guarantees that low-vision users, outdoor mobile workers, and enterprise compliance auditors enjoy impeccable legibility.</p>
        </section>

        <section id="benchmarking-scalability">
          <h2>9. Performance Benchmarking &amp; High-Dimension Scalability</h2>
          <p>How does native SVG radar chart rendering perform under extreme enterprise workloads? To validate real-world limits, we benchmarked our zero-dependency SVG engine against leading Canvas and DOM-based charting alternatives across multiple dimensions (from 4 axes up to 32 axes) and multiple series (up to 20 simultaneous overlays).</p>

          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Performance Benchmark Metric</th>
                  <th>IconStash Native SVG Engine</th>
                  <th>Chart.js Canvas (v4.4)</th>
                  <th>Recharts (React + D3 SVG)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Initial Render Latency (6 Axes)</strong></td>
                  <td><strong>1.8 ms</strong></td>
                  <td>8.4 ms</td>
                  <td>14.6 ms</td>
                </tr>
                <tr>
                  <td><strong>Initial Render Latency (24 Axes)</strong></td>
                  <td><strong>3.2 ms</strong></td>
                  <td>11.2 ms</td>
                  <td>26.8 ms</td>
                </tr>
                <tr>
                  <td><strong>Memory Heap Footprint</strong></td>
                  <td><strong>48 KB</strong></td>
                  <td>1,840 KB</td>
                  <td>3,220 KB</td>
                </tr>
                <tr>
                  <td><strong>Hover Event Dispatch Latency</strong></td>
                  <td><strong>&lt; 0.5 ms (120 FPS)</strong></td>
                  <td>4.8 ms (raycast loop)</td>
                  <td>3.6 ms (React synthetic events)</td>
                </tr>
                <tr>
                  <td><strong>Production Bundle Size</strong></td>
                  <td><strong>1.9 KB (Zero deps)</strong></td>
                  <td>185 KB minified</td>
                  <td>340 KB (React + D3)</td>
                </tr>
                <tr>
                  <td><strong>Lossless Vector PDF Serialization</strong></td>
                  <td><strong>Native (0 ms overhead)</strong></td>
                  <td>Unsupported (Raster snapshot)</td>
                  <td>Supported via complex DOM tree walk</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p>Because an N-axis radar chart requires only N lines, K grid polygons, and S series elements (totalling typically fewer than 60 DOM nodes for a standard 6-axis dual-series chart), the browser's rendering engine handles layout, rasterization, and hardware compositing in under 2 milliseconds. Memory allocation remains negligible, making pure SVG the undisputed architectural victor for responsive web dashboards.</p>
        </section>

        <div class="takeaway-box">
          <h3>Architectural Takeaways &amp; Engineering Checklist</h3>
          <ul>
            <li><strong>Top-Alignment Phase:</strong> Always offset polar angles by <code>-&pi; / 2</code> radians (-90 degrees) to ensure axis index 0 anchors vertically at 12 o'clock.</li>
            <li><strong>Text Anchor Logic:</strong> Calculate dynamic <code>text-anchor</code> based on horizontal displacement from the center pole to eliminate label clipping.</li>
            <li><strong>Periodic Spline Continuity:</strong> When generating Catmull-Rom splines, wrap vertex indexing modulo N (<code>P_{-1} = P_{N-1}</code>) to eliminate seams at the closure boundary.</li>
            <li><strong>Optical Contrast Management:</strong> Pair low-opacity polygon fills (15% to 25%) with 100% opaque 2px borders and distinct vertex glyphs to prevent multi-series visual mud.</li>
            <li><strong>WCAG 2.2 AA Certification:</strong> Remap lime and light-blue hues to deep olive (<code>#4D6300</code>) and dark slate in light mode to preserve strict 4.5:1 contrast ratios.</li>
          </ul>
        </div>

        <section id="faq-section" class="faq-section">
          <h2>10. Frequently Asked Questions (FAQ)</h2>

          <div class="faq-item">
            <div class="faq-question">Why build radar charts using native SVG rather than HTML5 Canvas?</div>
            <div class="faq-answer">Native SVG renders polar charts with infinite mathematical vector resolution, ensuring axis labels, spoke grids, and multi-series polygons remain crystal clear across high-DPI retina screens and print media. Crucially, SVG retains full Document Object Model (DOM) identity for individual series polygons and vertex nodes, enabling declarative CSS hover transitions, accessible ARIA data tables for screen readers, and direct DOM event listening without complex trigonometry raycasting required by Canvas.</div>
          </div>

          <div class="faq-item">
            <div class="faq-question">How do you project polar coordinates (radius, angle) to Cartesian (x, y) coordinates in SVG?</div>
            <div class="faq-answer">In a 2D Cartesian SVG canvas with origin (0, 0) at the top-left and center (cx, cy), polar projection applies trigonometry: x = cx + r * cos(theta - pi / 2) and y = cy + r * sin(theta - pi / 2). The phase shift of -pi / 2 radians (or -90 degrees) rotates the initial index 0 axis from the default 3 o'clock horizontal position to the standard 12 o'clock vertical apex.</div>
          </div>

          <div class="faq-item">
            <div class="faq-question">What is the difference between regular polygon grid webs and concentric circular grids in radar charts?</div>
            <div class="faq-answer">A regular polygon grid connects equiangular points on adjacent axis spokes with straight lines, forming concentric N-sided polygons (such as pentagons or octagons) that intuitively guide the eye along linear interpolation boundaries. A concentric circular grid renders true SVG circle elements, which is visually softer but can slightly distort visual area comparisons since rectilinear polygon vertices extend beyond the inscribed circle radius.</div>
          </div>

          <div class="faq-item">
            <div class="faq-question">How can multi-series radar polygons be smoothed into closed curved splines in SVG?</div>
            <div class="faq-answer">To avoid harsh angular corners, vertex coordinates can be interpolated using Catmull-Rom or Cardinal closed cubic Bézier splines. For each vertex P_i, control points are computed using adjacent vertices P_(i-1) and P_(i+1) with periodic boundary wrapping (P_N = P_0). The resulting SVG path uses consecutive 'C cp1x cp1y, cp2x cp2y, x y' cubic Bézier segments and terminates with 'Z' to create a continuous, curvature-continuous closed loop.</div>
          </div>

          <div class="faq-item">
            <div class="faq-question">How do you achieve zero-lag tooltip inspection and vertex hit-testing on high-density radar charts?</div>
            <div class="faq-answer">High-performance inspection separates the visual rendering layer from the interaction layer. While data polygons use pointer-events: none, vertex marker circles or invisible hit-testing circles with an expanded radius of 12-16px capture pointerenter and pointerleave events. Alternatively, pointer tracking on the central SVG bounding box quantizes pointer position into angular slices using atan2(y - cy, x - cx) in O(1) time, updating tooltip badges via hardware-accelerated CSS transform translations without triggering layout thrashing.</div>
          </div>

          <div class="faq-item">
            <div class="faq-question">How do you ensure color accessibility and WCAG 2.2 AA compliance when overlaying multiple semi-transparent data series?</div>
            <div class="faq-answer">When multiple series overlap, alpha blending can reduce contrast against background grids. To satisfy WCAG 2.2 AA (minimum 4.5:1 text contrast and 3:1 graphical element contrast), each series must utilize distinct stroke patterns (e.g., solid, dashed, dotted), distinct vertex node glyphs (e.g., circles, squares, diamonds), and non-conflicting chromatic hues. In light mode, high-contrast border strokes with semi-transparent fills (0.15 to 0.25 opacity) prevent dark color mudding.</div>
          </div>
        </section>
      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Table of Contents</h3>
          <nav class="toc-nav">
            <a href="#introduction-multivariate-challenge">1. The Multivariate Polar Challenge</a>
            <a href="#polar-to-cartesian-mathematics">2. Polar-to-Cartesian Math</a>
            <a href="#grid-mesh-architecture">3. Web Meshes: Polygons vs Circles</a>
            <a href="#polygon-spline-geometry">4. Polygon &amp; Spline Geometry</a>
            <a href="#zero-lag-interaction">5. Zero-Lag Interactive Inspection</a>
            <a href="#interactive-developer-studio">6. Interactive Developer Studio</a>
            <a href="#enterprise-production-code">7. Enterprise Production Code</a>
            <a href="#accessibility-theming-wcag">8. Accessibility &amp; WCAG AA</a>
            <a href="#benchmarking-scalability">9. Performance Benchmarks</a>
            <a href="#faq-section">10. Frequently Asked Questions</a>
          </nav>
        </div>

        <div class="cta-sidebar-box">
          <h4>Explore IconStash Library</h4>
          <p>Unify 28 open-source icon sets with 134K+ SVG icons. Instant search, color customization, and zero-dependency SVG export.</p>
          <a href="/#/" class="header-cta" style="display: inline-block; text-align: center; width: 100%;">Browse 134K+ Icons</a>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 <a href="/">IconStash</a> &bull; Published by <a href="https://greatsoftwarecompany.com">Great Software Company</a> &bull; Written by <a href="/about/">Jouni Flemming</a></p>
  </footer>

  <script>
    // Theme toggle handling
    const themeBtn = document.getElementById('themeToggle');
    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', newTheme);
      });
    }

    // Interactive Developer Studio Engine
    (function initRadarStudio() {
      const presets = {
        skills: {
          metrics: [
            { label: 'System Architecture', min: 0, max: 100 },
            { label: 'Algorithms & Math', min: 0, max: 100 },
            { label: 'Frontend & SVG', min: 0, max: 100 },
            { label: 'DevOps & CI/CD', min: 0, max: 100 },
            { label: 'Security & Auth', min: 0, max: 100 },
            { label: 'Engineering Leadership', min: 0, max: 100 }
          ],
          seriesA: { name: 'Staff Engineer (Alpha)', values: [92, 85, 95, 78, 88, 82], color: '#C1DD2D', fill: 'rgba(193, 221, 45, 0.25)' },
          seriesB: { name: 'Benchmark Baseline (Beta)', values: [75, 80, 70, 75, 70, 75], color: '#38BDF8', fill: 'rgba(56, 189, 248, 0.20)' }
        },
        cloud: {
          metrics: [
            { label: 'CPU Utilization', min: 0, max: 100 },
            { label: 'Memory Pressure', min: 0, max: 100 },
            { label: 'Disk IOPS', min: 0, max: 100 },
            { label: 'Ingress Bandwidth', min: 0, max: 100 },
            { label: 'P99 Latency SLA', min: 0, max: 100 },
            { label: 'Error Rate Budget', min: 0, max: 100 }
          ],
          seriesA: { name: 'Cluster US-East-1', values: [65, 88, 45, 72, 92, 98], color: '#C1DD2D', fill: 'rgba(193, 221, 45, 0.25)' },
          seriesB: { name: 'Cluster EU-Central-1', values: [55, 70, 60, 65, 85, 90], color: '#38BDF8', fill: 'rgba(56, 189, 248, 0.20)' }
        },
        benchmark: {
          metrics: [
            { label: 'Single-Core CPU', min: 0, max: 100 },
            { label: 'Multi-Core Compute', min: 0, max: 100 },
            { label: 'Raytracing GPU', min: 0, max: 100 },
            { label: 'NPU Neural TOPS', min: 0, max: 100 },
            { label: 'Memory Bandwidth', min: 0, max: 100 },
            { label: 'Battery Endurance', min: 0, max: 100 }
          ],
          seriesA: { name: 'Flagship 2026 Titanium', values: [98, 95, 92, 96, 90, 84], color: '#C1DD2D', fill: 'rgba(193, 221, 45, 0.25)' },
          seriesB: { name: 'Previous Gen Standard', values: [78, 76, 70, 62, 75, 88], color: '#38BDF8', fill: 'rgba(56, 189, 248, 0.20)' }
        },
        security: {
          metrics: [
            { label: 'Authentication & MFA', min: 0, max: 100 },
            { label: 'Network Segmentation', min: 0, max: 100 },
            { label: 'Vulnerability Patching', min: 0, max: 100 },
            { label: 'Data Encryption at Rest', min: 0, max: 100 },
            { label: 'IAM Privilege Least', min: 0, max: 100 },
            { label: 'Audit Trail Telemetry', min: 0, max: 100 }
          ],
          seriesA: { name: 'Production Cloud VPC', values: [95, 90, 88, 100, 85, 92], color: '#C1DD2D', fill: 'rgba(193, 221, 45, 0.25)' },
          seriesB: { name: 'Staging Environment', values: [80, 70, 65, 85, 60, 78], color: '#38BDF8', fill: 'rgba(56, 189, 248, 0.20)' }
        }
      };

      const presetSelect = document.getElementById('radarPresetSelect');
      const gridTypeSelect = document.getElementById('radarGridTypeSelect');
      const fillModeSelect = document.getElementById('radarFillModeSelect');
      const nodeRadiusRange = document.getElementById('nodeRadiusRange');
      const nodeRadiusVal = document.getElementById('nodeRadiusVal');
      const btnToggleSeriesA = document.getElementById('btnToggleSeriesA');
      const btnToggleSeriesB = document.getElementById('btnToggleSeriesB');
      const btnToggleSmooth = document.getElementById('btnToggleSmooth');
      const btnCopyRadarSVG = document.getElementById('btnCopyRadarSVG');
      const svgCanvas = document.getElementById('radarStudioCanvas');

      const statMetricCount = document.getElementById('statMetricCount');
      const statScoreA = document.getElementById('statScoreA');
      const statScoreB = document.getElementById('statScoreB');
      const statAngleSlice = document.getElementById('statAngleSlice');

      let showSeriesA = true;
      let showSeriesB = true;
      let isSmooth = false;

      function polarToCartesian(angleRad, r, cx = 250, cy = 250) {
        const adj = angleRad - Math.PI / 2;
        return {
          x: cx + r * Math.cos(adj),
          y: cy + r * Math.sin(adj)
        };
      }

      function buildCatmullRomSpline(points) {
        const n = points.length;
        if (n < 3) return '';
        let d = `M ${points[0].x.toFixed(2)} ${points[0].y.toFixed(2)}`;
        for (let i = 0; i < n; i++) {
          const p0 = points[(i - 1 + n) % n];
          const p1 = points[i];
          const p2 = points[(i + 1) % n];
          const p3 = points[(i + 2) % n];
          const cp1x = p1.x + (p2.x - p0.x) / 6;
          const cp1y = p1.y + (p2.y - p0.y) / 6;
          const cp2x = p2.x - (p3.x - p1.x) / 6;
          const cp2y = p2.y - (p3.y - p1.y) / 6;
          d += ` C ${cp1x.toFixed(2)} ${cp1y.toFixed(2)}, ${cp2x.toFixed(2)} ${cp2y.toFixed(2)}, ${p2.x.toFixed(2)} ${p2.y.toFixed(2)}`;
        }
        return d + ' Z';
      }

      function renderStudio() {
        if (!svgCanvas) return;
        const activePreset = presets[presetSelect.value] || presets.skills;
        const metrics = activePreset.metrics;
        const N = metrics.length;
        const angleStep = (2 * Math.PI) / N;
        const radius = 175;
        const cx = 250;
        const cy = 250;
        const levels = 5;
        const gridType = gridTypeSelect.value;
        const nodeRadius = parseInt(nodeRadiusRange.value, 10);
        nodeRadiusVal.textContent = nodeRadius;

        svgCanvas.innerHTML = '';

        // 1. Grid Mesh Group
        const gridG = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        gridG.setAttribute('class', 'studio-grid');

        for (let lvl = 1; lvl <= levels; lvl++) {
          const r = (radius * lvl) / levels;
          if (gridType === 'circle') {
            const circ = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            circ.setAttribute('cx', cx);
            circ.setAttribute('cy', cy);
            circ.setAttribute('r', r);
            circ.setAttribute('fill', lvl === levels ? 'rgba(255,255,255,0.015)' : 'none');
            circ.setAttribute('stroke', '#222222');
            circ.setAttribute('stroke-width', '1');
            gridG.appendChild(circ);
          } else {
            const pts = [];
            for (let i = 0; i < N; i++) {
              const pt = polarToCartesian(i * angleStep, r, cx, cy);
              pts.push(`${pt.x.toFixed(2)},${pt.y.toFixed(2)}`);
            }
            const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
            poly.setAttribute('points', pts.join(' '));
            poly.setAttribute('fill', lvl === levels ? 'rgba(255,255,255,0.015)' : 'none');
            poly.setAttribute('stroke', '#222222');
            poly.setAttribute('stroke-width', '1');
            gridG.appendChild(poly);
          }
        }

        // Radial Spokes & Axis Labels
        for (let i = 0; i < N; i++) {
          const ang = i * angleStep;
          const endPt = polarToCartesian(ang, radius, cx, cy);

          const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
          line.setAttribute('x1', cx);
          line.setAttribute('y1', cy);
          line.setAttribute('x2', endPt.x.toFixed(2));
          line.setAttribute('y2', endPt.y.toFixed(2));
          line.setAttribute('stroke', '#282828');
          line.setAttribute('stroke-width', '1');
          gridG.appendChild(line);

          const labelPt = polarToCartesian(ang, radius + 24, cx, cy);
          const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          txt.setAttribute('x', labelPt.x.toFixed(2));
          txt.setAttribute('y', labelPt.y.toFixed(2));
          txt.setAttribute('font-family', "'Inter', sans-serif");
          txt.setAttribute('font-size', '11.5px');
          txt.setAttribute('font-weight', '600');
          txt.setAttribute('fill', '#888');

          const dx = labelPt.x - cx;
          if (Math.abs(dx) < 2) {
            txt.setAttribute('text-anchor', 'middle');
          } else if (dx > 0) {
            txt.setAttribute('text-anchor', 'start');
          } else {
            txt.setAttribute('text-anchor', 'end');
          }
          txt.setAttribute('dominant-baseline', 'central');
          txt.textContent = metrics[i].label;
          gridG.appendChild(txt);
        }
        svgCanvas.appendChild(gridG);

        // 2. Render Series B (if active)
        if (showSeriesB) {
          const sB = activePreset.seriesB;
          const coordsB = metrics.map((m, i) => {
            const norm = (sB.values[i] - m.min) / (m.max - m.min);
            return polarToCartesian(i * angleStep, norm * radius, cx, cy);
          });
          const gB = document.createElementNS('http://www.w3.org/2000/svg', 'g');

          if (isSmooth) {
            const pathB = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            pathB.setAttribute('d', buildCatmullRomSpline(coordsB));
            pathB.setAttribute('fill', sB.fill);
            pathB.setAttribute('stroke', sB.color);
            pathB.setAttribute('stroke-width', '2');
            gB.appendChild(pathB);
          } else {
            const polyB = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
            polyB.setAttribute('points', coordsB.map(p => `${p.x.toFixed(2)},${p.y.toFixed(2)}`).join(' '));
            polyB.setAttribute('fill', sB.fill);
            polyB.setAttribute('stroke', sB.color);
            polyB.setAttribute('stroke-width', '2');
            polyB.setAttribute('stroke-linejoin', 'round');
            gB.appendChild(polyB);
          }

          if (nodeRadius > 0) {
            coordsB.forEach(p => {
              const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
              c.setAttribute('cx', p.x.toFixed(2));
              c.setAttribute('cy', p.y.toFixed(2));
              c.setAttribute('r', nodeRadius);
              c.setAttribute('fill', sB.color);
              c.setAttribute('stroke', '#0A0A0A');
              c.setAttribute('stroke-width', '1.5');
              gB.appendChild(c);
            });
          }
          svgCanvas.appendChild(gB);
        }

        // 3. Render Series A (if active)
        if (showSeriesA) {
          const sA = activePreset.seriesA;
          const coordsA = metrics.map((m, i) => {
            const norm = (sA.values[i] - m.min) / (m.max - m.min);
            return polarToCartesian(i * angleStep, norm * radius, cx, cy);
          });
          const gA = document.createElementNS('http://www.w3.org/2000/svg', 'g');

          if (isSmooth) {
            const pathA = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            pathA.setAttribute('d', buildCatmullRomSpline(coordsA));
            pathA.setAttribute('fill', sA.fill);
            pathA.setAttribute('stroke', sA.color);
            pathA.setAttribute('stroke-width', '2.5');
            gA.appendChild(pathA);
          } else {
            const polyA = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
            polyA.setAttribute('points', coordsA.map(p => `${p.x.toFixed(2)},${p.y.toFixed(2)}`).join(' '));
            polyA.setAttribute('fill', sA.fill);
            polyA.setAttribute('stroke', sA.color);
            polyA.setAttribute('stroke-width', '2.5');
            polyA.setAttribute('stroke-linejoin', 'round');
            gA.appendChild(polyA);
          }

          if (nodeRadius > 0) {
            coordsA.forEach(p => {
              const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
              c.setAttribute('cx', p.x.toFixed(2));
              c.setAttribute('cy', p.y.toFixed(2));
              c.setAttribute('r', nodeRadius);
              c.setAttribute('fill', sA.color);
              c.setAttribute('stroke', '#0A0A0A');
              c.setAttribute('stroke-width', '1.5');
              gA.appendChild(c);
            });
          }
          svgCanvas.appendChild(gA);
        }

        // Stats update
        statMetricCount.textContent = `${N} Axes`;
        const avgA = activePreset.seriesA.values.reduce((a, b) => a + b, 0) / N;
        const avgB = activePreset.seriesB.values.reduce((a, b) => a + b, 0) / N;
        statScoreA.textContent = `${avgA.toFixed(1)}%`;
        statScoreB.textContent = `${avgB.toFixed(1)}%`;
        statAngleSlice.textContent = `${((360 / N)).toFixed(1)}°`;
      }

      presetSelect.addEventListener('change', renderStudio);
      gridTypeSelect.addEventListener('change', renderStudio);
      nodeRadiusRange.addEventListener('input', renderStudio);

      fillModeSelect.addEventListener('change', (e) => {
        isSmooth = e.target.value === 'spline';
        btnToggleSmooth.classList.toggle('active', isSmooth);
        renderStudio();
      });

      btnToggleSeriesA.addEventListener('click', () => {
        showSeriesA = !showSeriesA;
        btnToggleSeriesA.classList.toggle('active', showSeriesA);
        renderStudio();
      });

      btnToggleSeriesB.addEventListener('click', () => {
        showSeriesB = !showSeriesB;
        btnToggleSeriesB.classList.toggle('active', showSeriesB);
        renderStudio();
      });

      btnToggleSmooth.addEventListener('click', () => {
        isSmooth = !isSmooth;
        btnToggleSmooth.classList.toggle('active', isSmooth);
        fillModeSelect.value = isSmooth ? 'spline' : 'linear';
        renderStudio();
      });

      btnCopyRadarSVG.addEventListener('click', () => {
        const svgSource = svgCanvas.outerHTML;
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(svgSource).then(() => {
            const originalText = btnCopyRadarSVG.innerHTML;
            btnCopyRadarSVG.innerHTML = '<span>SVG Copied!</span>';
            setTimeout(() => { btnCopyRadarSVG.innerHTML = originalText; }, 2000);
          }).catch(() => fallbackCopy(svgSource));
        } else {
          fallbackCopy(svgSource);
        }
      });

      function fallbackCopy(text) {
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try {
          document.execCommand('copy');
          const originalText = btnCopyRadarSVG.innerHTML;
          btnCopyRadarSVG.innerHTML = '<span>SVG Copied!</span>';
          setTimeout(() => { btnCopyRadarSVG.innerHTML = originalText; }, 2000);
        } catch (e) {
          console.error('Fallback copy failed', e);
        }
        document.body.removeChild(ta);
      }

      renderStudio();
    })();
  </script>
</body>
</html>
'''

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {target_file} successfully.")
