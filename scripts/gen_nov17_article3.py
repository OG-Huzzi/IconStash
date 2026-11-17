import os
import re

slug = "svg-sparklines-and-micro-charts-dashboard-visualization-guide"
target_dir = os.path.join(r"D:\Project IconStash\IconStash\articles", slug)
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

html_content = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mastering SVG Sparklines &amp; Micro-Charts: Inline Trendlines, Area Gradients &amp; Dashboard Metrics Guide (2026) | IconStash</title>
  <meta name="description" content="Build high-performance SVG sparklines: inline trendlines, Catmull-Rom splines, area gradients, min-max dots, and zero-dependency micro-chart metrics in HTML.">
  <meta name="keywords" content="svg sparkline, inline svg trendline, micro chart svg javascript, dashboard sparkline web, catmull rom spline sparkline, area gradient sparkline svg, tufte sparkline web, minimal data visualization svg">
  <meta property="og:title" content="Mastering SVG Sparklines &amp; Micro-Charts: Inline Trendlines, Area Gradients &amp; Dashboard Metrics Guide (2026)">
  <meta property="og:description" content="Build high-performance SVG sparklines: inline trendlines, Catmull-Rom splines, area gradients, min-max dots, and zero-dependency micro-chart metrics in HTML.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-17T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-17T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="Vector Graphics &amp; Micro-Visualization Engineering">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="Sparklines">
  <meta property="article:tag" content="Data Visualization">
  <meta property="article:tag" content="Frontend Engineering">
  <meta property="article:tag" content="Tufte Principles">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mastering SVG Sparklines &amp; Micro-Charts: Inline Trendlines, Area Gradients &amp; Dashboard Metrics Guide (2026)">
  <meta name="twitter:description" content="Build high-performance SVG sparklines: inline trendlines, Catmull-Rom splines, area gradients, min-max dots, and zero-dependency micro-chart metrics in HTML.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/">
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
      "headline": "Mastering SVG Sparklines & Micro-Charts: Inline Trendlines, Area Gradients & Dashboard Metrics Guide (2026)",
      "description": "Build high-performance SVG sparklines: inline trendlines, Catmull-Rom splines, area gradients, min-max dots, and zero-dependency micro-chart metrics in HTML.",
      "image": "https://iconstash.io/assets/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide.jpg",
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
      "datePublished": "2026-11-17",
      "dateModified": "2026-11-17",
      "mainEntityOfPage": "https://iconstash.io/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/",
      "inLanguage": "en-US",
      "wordCount": 5080,
      "articleSection": "Vector Graphics & Data Visualization",
      "keywords": [
        "svg sparkline",
        "inline svg trendline",
        "micro chart svg javascript",
        "dashboard sparkline web",
        "catmull rom spline sparkline",
        "area gradient sparkline svg",
        "tufte sparkline web",
        "minimal data visualization svg"
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
          "name": "SVG Sparklines & Micro-Charts Guide",
          "item": "https://iconstash.io/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is an SVG sparkline and how does it differ from a standard full-size line chart?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Coined by statistician Edward Tufte, a sparkline is a small, high-density, word-sized data graphic designed to be embedded directly inline with prose, metrics cards, or dense tabular rows. Unlike full-size line charts that feature elaborate Y-axis labels, tick grids, and legends, a sparkline eliminates all peripheral chart junk to maximize the data-ink ratio, communicating historical trend, volatility, and direction at a glance."
          }
        },
        {
          "@type": "Question",
          "name": "How do you project arbitrary data points into a compact SVG sparkline viewBox?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For N chronological values [y_0, y_1, ..., y_(N-1)] mapped into a viewport of width W and height H with vertical padding p, the X-coordinate scales uniformly as x_i = (i / (N - 1)) * W. The Y-coordinate maps inversely to handle SVG top-left origin: y_i = p + (1 - (v_i - min) / (max - min || 1)) * (H - 2 * p). If all values are identical, min equals max and the line centers vertically at H / 2."
          }
        },
        {
          "@type": "Question",
          "name": "What is the mathematical difference between polyline sparklines and Catmull-Rom spline sparklines?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An SVG polyline connects adjacent points with straight linear segments (L x y), producing sharp angular peaks that can feel mechanical at small scales. A Catmull-Rom spline calculates cubic Bézier control points (C cp1x cp1y, cp2x cp2y, x y) using neighboring data points, guaranteeing first-order derivative continuity (C1 smoothness) so the curve passes through every data point without overshoot."
          }
        },
        {
          "@type": "Question",
          "name": "How do you construct a closed area gradient fill under an SVG sparkline?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An area fill is created by starting at the bottom-left baseline (M x_0 H), drawing straight up to the first data point (L x_0 y_0), tracing the sparkline path to the final point (x_(N-1), y_(N-1)), dropping straight down to the bottom-right baseline (L x_(N-1) H), and closing the path (Z) back to the start. The closed path is filled with a vertical linearGradient transitioning from a semi-transparent accent to fully transparent at the baseline."
          }
        },
        {
          "@type": "Question",
          "name": "How do you render high-impact endpoint dots and min/max peak markers without visual clipping?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tufte sparkline conventions emphasize marking the latest endpoint value with a colored dot and highlighting historical min/max extremes. To prevent circular markers from clipping against the SVG viewport edges, the chart includes vertical and horizontal padding p >= markerRadius + strokeWidth. In CSS, setting overflow: visible on the SVG container ensures marker circles extend gracefully into surrounding margin space without truncation."
          }
        },
        {
          "@type": "Question",
          "name": "How do you ensure thousands of inline SVG sparklines in dense data tables do not degrade DOM performance?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In large enterprise tables displaying hundreds of rows with sparklines, embedding full SVG trees can bloat DOM memory. Production systems optimize performance by using virtualized scrolling (only mounting visible rows), sharing a single SVG defs linearGradient across all instances via id reference, generating compact path strings without extra wrapper groups, and applying content-visibility: auto to off-screen table rows."
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
    .sandbox-controls { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 20px; }
    .control-row { display: flex; flex-direction: column; gap: 6px; }
    .control-row label { font-size: 12.5px; font-weight: 600; color: #999; }
    .control-select, .control-input { background: #1A1A1A; border: 1px solid #333; border-radius: 6px; color: #FFF; padding: 8px 12px; font-size: 13.5px; outline: none; font-family: inherit; }
    .control-select:focus, .control-input:focus { border-color: #C1DD2D; }
    .control-btn-group { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px; }
    .toggle-btn { background: #1C1C1C; border: 1px solid #333; color: #AAA; padding: 8px 14px; border-radius: 6px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 150ms ease; }
    .toggle-btn:hover { border-color: #555; color: #FFF; }
    .toggle-btn.active { background: #C1DD2D; color: #0A0A0A; border-color: #C1DD2D; }

    .preview-stage-container { background: #0D0D0D; border: 1px solid #222; border-radius: 8px; padding: 24px; display: flex; flex-direction: column; justify-content: center; align-items: center; position: relative; min-height: 240px; }
    .spark-card-wrapper { background: #141414; border: 1px solid #262626; border-radius: 8px; padding: 20px 24px; width: 100%; max-width: 440px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
    .spark-card-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px; }
    .spark-metric-title { font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: #888; font-weight: 600; }
    .spark-metric-val { font-size: 26px; font-weight: 900; color: #FFF; font-family: "JetBrains Mono", monospace; }
    .spark-delta-badge { font-size: 12px; font-weight: 700; padding: 2px 6px; border-radius: 4px; display: inline-flex; align-items: center; gap: 4px; }
    .spark-delta-badge.positive { background: rgba(193,221,45,0.12); color: #C1DD2D; }
    .spark-delta-badge.negative { background: rgba(239,68,68,0.12); color: #EF4444; }
    .spark-svg-canvas { width: 100%; height: 72px; overflow: visible; }
    .spark-line-path { fill: none; stroke-linecap: round; stroke-linejoin: round; }
    .spark-dot { transition: transform 150ms ease; }
    .spark-dot:hover { transform: scale(1.4); }

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
    html[data-theme="light"] .spark-card-wrapper { background: #FFFFFF; border-color: #E4E4E7; box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
    html[data-theme="light"] .spark-metric-val { color: #18181B; }
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
      <span class="current" aria-current="page">Mastering SVG Sparklines &amp; Micro-Charts</span>
    </nav>

    <header class="article-hero">
      <span class="tag">Micro-Visualizations &amp; Trendline Vectors</span>
      <h1>Mastering SVG Sparklines &amp; Micro-Charts: Inline Trendlines, Area Gradients &amp; Dashboard Metrics Guide</h1>
      <div class="article-meta">
        <span>By <a href="/about/" rel="author">Jouni Flemming</a></span>
        <span>&bull;</span>
        <time datetime="2026-11-17">November 17, 2026</time>
        <span>&bull;</span>
        <span>27 min read</span>
        <span>&bull;</span>
        <span>5,080 words</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">
        <div class="featured-summary">
          <p><strong>Executive Architectural Summary:</strong> Sparklines and inline micro-charts represent the pinnacle of data density in modern user interface design. Coined by information design pioneer Edward Tufte, a sparkline is a small, intense, word-sized graphic intended to be embedded directly within sentences, metric cards, and dense financial tables. Instead of burdening production applications with massive charting frameworks, native SVG provides the ultimate runtime engine for high-frequency, responsive micro-visualizations.</p>
          <ul>
            <li><strong>Edward Tufte's Data-Ink Theory:</strong> Eliminate axis ticks, decorative border frames, and chart junk to maximize the data-ink ratio, delivering instantaneous trend comprehension within sub-100px viewports.</li>
            <li><strong>Mathematical Normalization &amp; Aspect Ratios:</strong> Formulate coordinate compression pipelines that scale arbitrary time-series arrays into compact bounding boxes while preserving truthful rate-of-change perception.</li>
            <li><strong>Continuous Spline Smoothing:</strong> Contrast piecewise linear polylines against Catmull-Rom cubic Bézier splines, guaranteeing smooth curve continuity without artificial mathematical overshoot.</li>
            <li><strong>High-Throughput Table Virtualization:</strong> Deploy memory-efficient SVG symbol instancing, CSS gradient sharing, and off-screen virtualization to render thousands of active sparklines at 120 FPS.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide.jpg" alt="Mastering SVG Sparklines and Micro Charts Hero Visualization Guide" width="1200" height="675" fetchpriority="high" decoding="async">
          <figcaption>Figure 1: Production-grade dark mode executive telemetry console featuring inline SVG sparklines, gradient area micro-charts, and high-impact min/max endpoint anchors.</figcaption>
        </figure>

        <section id="tufte-data-ink-theory">
          <h2>1. Executive Summary &amp; Edward Tufte's Data-Ink Theory for Micro-Visualizations</h2>
          <p>In his seminal work <em>The Visual Display of Quantitative Information</em>, statistician Edward Tufte established the foundational principle that governs all effective visual information design: the <strong>data-ink ratio</strong>. Tufte defined data-ink as the non-erasable core of a graphic &mdash; the non-redundant ink arranged in space to communicate authentic data variation. Every single drop of ink that does not directly represent data variation (such as decorative drop-shadow frames, heavy gridlines, saturated background fills, and redundant numerical callouts) represents \"chart junk\" that diminishes visual clarity and slows human cognitive processing.</p>

          <p>Sparklines represent the ultimate realization of Tufte's data-ink optimization doctrine. A sparkline is a data graphic stripped down to its irreducible mathematical essence: a single continuous trendline, an optional translucent area gradient, and a pair of endpoint anchors. By shedding heavy Cartesian axes, tick marks, and legends, a sparkline achieves intense information density. It occupies no more visual real estate than a single word or short phrase, allowing it to be embedded directly inline within running text, financial data tables, and compact summary metric cards.</p>

          <p>However, when frontend engineering teams attempt to integrate sparklines into modern enterprise applications, they frequently make the catastrophic mistake of deploying heavy third-party charting libraries. Bundling packages such as Chart.js, Recharts, or ApexCharts just to render a 120px by 30px sparkline injects hundreds of kilobytes of unused JavaScript, registers hundreds of global window event listeners, and severely degrades dashboard initial load times. Even worse, attempting to render hundreds of sparklines in a financial data grid using HTML5 <code>&lt;canvas&gt;</code> introduces severe memory bloating and leaves screen readers completely blind to data trends.</p>

          <p>Native Scalable Vector Graphics represents the quintessential runtime technology for sparklines. An inline SVG sparkline requires less than 300 bytes of lightweight XML markup. It renders with infinite mathematical vector crispness on retina and mobile displays, binds effortlessly to CSS variables for instant dark and light mode theming, and natively integrates with accessibility trees via WAI-ARIA graphics module roles. To explore how native SVG powers diverse visualization archetypes across enterprise consoles, examine our architectural guides on <a href="/articles/svg-charts-and-data-visualization-from-scratch-guide/">building SVG charts from scratch</a>, <a href="/articles/svg-donut-charts-and-circular-percentage-visualization-guide/">circular donut charts</a>, and <a href="/articles/svg-bar-charts-and-column-graph-visualization-guide/">Cartesian bar graphs</a>.</p>

          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Architecture Dimension</th>
                  <th>Canvas Micro-Renders</th>
                  <th>Monolithic Library Bundle</th>
                  <th>Pure Vanilla SVG Sparkline</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Markup Footprint</strong></td>
                  <td>1 canvas tag per chart (high memory)</td>
                  <td>Massive wrapper DOM trees (300KB+ JS)</td>
                  <td>Under 300 bytes of inline vector XML</td>
                </tr>
                <tr>
                  <td><strong>Vector Crispness on Retina</strong></td>
                  <td>Blurs unless manually rescaled by DPR</td>
                  <td>Varies; heavy raster shims</td>
                  <td>100% infinite vector precision</td>
                </tr>
                <tr>
                  <td><strong>DOM Overhead in 500-Row Tables</strong></td>
                  <td>500 canvas backing stores (GPU memory crash)</td>
                  <td>Thousands of detached listener closures</td>
                  <td>Lightweight inline paths (zero GC pressure)</td>
                </tr>
                <tr>
                  <td><strong>CSS Theming Integration</strong></td>
                  <td>Requires manual JS redraw loop</td>
                  <td>JSON configuration overrides</td>
                  <td>Pure CSS variables (stroke: var(--accent))</td>
                </tr>
                <tr>
                  <td><strong>Accessibility (WCAG 2.2 AA)</strong></td>
                  <td>Completely opaque black box</td>
                  <td>Basic outer container aria-label</td>
                  <td>Full semantic ARIA role='graphics-symbol'</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <section id="normalization-mathematics">
          <h2>2. Normalization Mathematics: Range Compression &amp; Aspect Ratio Optimization</h2>
          <p>The mathematical heart of an SVG sparkline engine is the coordinate transformation pipeline that converts an arbitrary time-series array of raw floating-point numbers into a normalized SVG viewport. Let an input dataset be an ordered sequence of <code>N</code> values: <code>V = [v<sub>0</sub>, v<sub>1</sub>, ..., v<sub>N-1</sub>]</code>. The target SVG canvas is defined by its coordinate bounding box width <code>W</code> and height <code>H</code>, along with a protective vertical margin padding <code>p</code>.</p>

          <p>To preserve visual truthfulness, the engine first determines the empirical data bounds: the minimum value <code>v<sub>min</sub> = min(V)</code> and the maximum value <code>v<sub>max</sub> = max(V)</code>. The total numeric domain span is &Delta;v = v<sub>max</sub> - v<sub>min</sub>. A classic mathematical edge case occurs when all values in the time-series are identical (&Delta;v = 0, indicating a flat trendline). In this scenario, division by zero must be guarded, centering the line vertically at <code>y = H / 2</code>.</p>

          <p>The horizontal X-coordinate maps uniformly across the time dimension:</p>

          <div class="formula-card">
            <div class="formula-title">Horizontal Time-Axis Normalization</div>
            <div class="formula-body">x<sub>i</sub> = (i / (N - 1)) &times; W</div>
            <div class="formula-desc">Maps category index i (from 0 to N-1) linearly across the entire available canvas width W.</div>
          </div>

          <p>The vertical Y-coordinate requires inversion to account for the SVG top-left origin, mapping <code>v<sub>max</sub></code> to the top margin <code>p</code> and <code>v<sub>min</sub></code> to the bottom baseline <code>H - p</code>:</p>

          <div class="formula-card">
            <div class="formula-title">Inverted Vertical Range Projection</div>
            <div class="formula-body">y<sub>i</sub> = p + (1 - (v<sub>i</sub> - v<sub>min</sub>) / &Delta;v) &times; (H - 2 &times; p)</div>
            <div class="formula-desc">Guarantees that maximum values touch the top padding boundary and minimum values align with the bottom baseline.</div>
          </div>

          <h3>2.1 Aspect Ratio &amp; Banking to 45 Degrees</h3>
          <p>A crucial perceptual principle established by William Cleveland is <strong>banking to 45 degrees</strong>. If a sparkline's aspect ratio is too tall and narrow, minor fluctuations appear as catastrophic spikes; conversely, if the sparkline is too flat and wide, dramatic volatility appears deceptively dormant. Cleveland proved that human visual perception estimates rates of change with maximum accuracy when the absolute slope of the line segments averages approximately 45 degrees. For dashboard sparklines, an aspect ratio between 3:1 and 5:1 (such as 120px &times; 30px or 320px &times; 80px) achieves optimal optical banking for typical business metrics.</p>
        </section>

        <!-- Architectural Figure 2 Vector Diagram -->
        <figure class="article-figure">
          <svg viewBox="0 0 960 320" width="960" height="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Edward Tufte's Data-Ink Optimization Pipeline Diagram">
            <rect width="960" height="320" fill="#0D0D0D" rx="8"/>
            <rect x="1" y="1" width="958" height="318" fill="none" stroke="#222" rx="7"/>

            <!-- Header -->
            <text x="480" y="32" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14" font-weight="800" text-anchor="middle" letter-spacing="0.06em">EDWARD TUFTE'S DATA-INK OPTIMIZATION PIPELINE FOR SVG SPARKLINES</text>
            <line x1="40" y1="46" x2="920" y2="46" stroke="#262626" stroke-width="1"/>

            <!-- Step 1: Raw Data Array -->
            <g transform="translate(60, 65)">
              <rect width="180" height="230" fill="#141414" stroke="#262626" rx="6"/>
              <text x="90" y="24" fill="#888" font-family="Inter, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. RAW DATA ARRAY</text>
              <rect x="25" y="50" width="130" height="28" fill="#1A1A1A" rx="4"/>
              <text x="90" y="68" fill="#FFF" font-family="JetBrains Mono, monospace" font-size="11" text-anchor="middle">[42, 58, 35, 74, ...]</text>
              <text x="90" y="110" fill="#AAA" font-family="Inter, sans-serif" font-size="10.5" text-anchor="middle">Extract Min / Max</text>
              <text x="90" y="128" fill="#C1DD2D" font-family="JetBrains Mono, monospace" font-size="11" text-anchor="middle">vMin: 35 &bull; vMax: 94</text>
              <text x="90" y="170" fill="#888" font-family="Inter, sans-serif" font-size="10" text-anchor="middle">&Delta;v = vMax - vMin</text>
              <text x="90" y="205" fill="#666" font-family="Inter, sans-serif" font-size="9.5" text-anchor="middle">Domain Range Bounds</text>
            </g>

            <!-- Arrow 1 -->
            <path d="M 250,180 L 280,180" stroke="#444" stroke-width="2" marker-end="url(#arrow)"/>

            <!-- Step 2: Coordinate Normalization -->
            <g transform="translate(290, 65)">
              <rect width="180" height="230" fill="#141414" stroke="#262626" rx="6"/>
              <text x="90" y="24" fill="#38BDF8" font-family="Inter, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. Y-INVERSION MATH</text>
              <line x1="20" y1="160" x2="160" y2="160" stroke="#333" stroke-width="1"/>
              <!-- Scaled Polyline -->
              <polyline points="30,140 60,110 90,150 120,80 150,95" fill="none" stroke="#38BDF8" stroke-width="2"/>
              <circle cx="150" cy="95" r="3" fill="#38BDF8"/>
              <text x="90" y="185" fill="#AAA" font-family="Inter, sans-serif" font-size="10" text-anchor="middle">y = p + (1 - norm) &times; H</text>
              <text x="90" y="205" fill="#666" font-family="Inter, sans-serif" font-size="9.5" text-anchor="middle">Cartesian Sub-Pixel Fit</text>
            </g>

            <!-- Arrow 2 -->
            <path d="M 480,180 L 510,180" stroke="#444" stroke-width="2"/>

            <!-- Step 3: Spline vs Polyline -->
            <g transform="translate(520, 65)">
              <rect width="180" height="230" fill="#141414" stroke="#262626" rx="6"/>
              <text x="90" y="24" fill="#A855F7" font-family="Inter, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. CATMULL-ROM SPLINE</text>
              <path d="M 30,140 C 45,125 45,110 60,110 C 75,110 75,150 90,150 C 105,150 105,80 120,80 C 135,80 135,95 150,95" fill="none" stroke="#A855F7" stroke-width="2"/>
              <circle cx="30" cy="140" r="2.5" fill="#FFF"/>
              <circle cx="150" cy="95" r="3" fill="#A855F7"/>
              <text x="90" y="185" fill="#AAA" font-family="Inter, sans-serif" font-size="10" text-anchor="middle">C1 Continuity Cubic</text>
              <text x="90" y="205" fill="#666" font-family="Inter, sans-serif" font-size="9.5" text-anchor="middle">Zero Sharp Elbows</text>
            </g>

            <!-- Arrow 3 -->
            <path d="M 710,180 L 740,180" stroke="#444" stroke-width="2"/>

            <!-- Step 4: Gradient Area & Anchors -->
            <g transform="translate(750, 65)">
              <rect width="150" height="230" fill="#141414" stroke="#262626" rx="6"/>
              <text x="75" y="24" fill="#C1DD2D" font-family="Inter, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. AREA GRADIENT</text>
              <defs>
                <linearGradient id="fig2Grad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#C1DD2D" stop-opacity="0.35"/>
                  <stop offset="100%" stop-color="#C1DD2D" stop-opacity="0"/>
                </linearGradient>
              </defs>
              <path d="M 20,130 C 40,115 50,140 70,100 C 90,80 110,110 130,70 L 130,150 L 20,150 Z" fill="url(#fig2Grad)"/>
              <path d="M 20,130 C 40,115 50,140 70,100 C 90,80 110,110 130,70" fill="none" stroke="#C1DD2D" stroke-width="2"/>
              <circle cx="130" cy="70" r="3.5" fill="#C1DD2D"/>
              <text x="75" y="185" fill="#AAA" font-family="Inter, sans-serif" font-size="10" text-anchor="middle">L xN H L x0 H Z</text>
              <text x="75" y="205" fill="#666" font-family="Inter, sans-serif" font-size="9.5" text-anchor="middle">Closed Luminous Base</text>
            </g>
          </svg>
          <figcaption>Figure 2: Edward Tufte's data-ink optimization pipeline illustrating data array normalization, Cartesian Y-inversion, Catmull-Rom spline interpolation, and translucent gradient area fill closure.</figcaption>
        </figure>

        <section id="polyline-vs-spline">
          <h2>3. Polyline vs. Catmull-Rom Spline Smoothing for Sub-100px Viewports</h2>
          <p>Once data points are projected into Cartesian coordinates, the frontend engineer must select the path interpolation geometry. In vanilla SVG, two primary rendering primitives dominate: linear <code>&lt;polyline&gt;</code> elements versus smoothed cubic Bézier <code>&lt;path&gt;</code> splines.</p>

          <h3>3.1 The Mechanical Simplicity of Polyline</h3>
          <p>The <code>&lt;polyline&gt;</code> element is the most straightforward representation: it connects sequential points with direct straight line segments using a simple whitespace-delimited coordinate string:</p>
          <pre><code>&lt;polyline
  points="0,65 40,42 80,78 120,25 160,34 200,12"
  fill="none"
  stroke="#C1DD2D"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
/&gt;</code></pre>
          <p>While polylines are computationally lightweight, they suffer from harsh angular inflection points at sharp directional peaks. At high zoom levels or in refined financial consoles, straight-line zigzag segments can appear unrefined and jarring.</p>

          <h3>3.2 Catmull-Rom Spline Interpolation</h3>
          <p>To eliminate harsh angles while ensuring that the curve passes through every single data point without artificial overshoot, production charting engines deploy <strong>Catmull-Rom centripetal cubic splines</strong>. Unlike uniform B-splines which approximate control points without actually touching the data vertices, a Catmull-Rom spline guarantees interpolation: every vertex P<sub>i</sub> lies directly on the curve.</p>

          <p>For each segment between P<sub>i</sub> and P<sub>i+1</sub>, cubic Bézier control points CP<sub>1</sub> and CP<sub>2</sub> are derived from the adjacent vertices P<sub>i-1</sub> and P<sub>i+2</sub>:</p>

          <div class="formula-card">
            <div class="formula-title">Catmull-Rom Cubic Bézier Control Points</div>
            <div class="formula-body">CP<sub>1</sub> = P<sub>i</sub> + (P<sub>i+1</sub> - P<sub>i-1</sub>) / 6, &nbsp; CP<sub>2</sub> = P<sub>i+1</sub> - (P<sub>i+2</sub> - P<sub>i</sub>) / 6</div>
            <div class="formula-desc">Generates C1 continuous cubic Bézier segments that transition smoothly across all interior vertices.</div>
          </div>

          <p>For the initial segment (where P<sub>i-1</sub> does not exist) and the terminating segment (where P<sub>i+2</sub> does not exist), phantom control points are mirrored across the endpoints, ensuring continuous curvature across the entire span.</p>
        </section>

        <section id="gradient-area-fills">
          <h2>4. Gradient Area Fills &amp; Baseline Zero Anchoring</h2>
          <p>A bare 1.5px stroke trendline, while minimalist, can sometimes lack visual presence within a busy data dashboard. To anchor the metric and provide a sense of volumetric weight, modern UI design conventions combine the trendline with a translucent vertical linear gradient area fill.</p>

          <p>Constructing an area fill requires closing the open line path into a complete two-dimensional polygon. The path begins at the bottom-left baseline coordinate <code>(x<sub>0</sub>, H)</code>, draws a straight line up to the first data point <code>(x<sub>0</sub>, y<sub>0</sub>)</code>, traces along the entire upper sparkline contour (whether polyline or spline), drops vertically to the bottom-right baseline coordinate <code>(x<sub>N-1</sub>, H)</code>, and terminates with <code>Z</code> to close back to <code>(x<sub>0</sub>, H)</code>:</p>

          <div class="formula-card">
            <div class="formula-title">Closed Area Polygon Geometry</div>
            <div class="formula-body">M x<sub>0</sub> H L x<sub>0</sub> y<sub>0</sub> [Sparkline Path] L x<sub>N-1</sub> H Z</div>
            <div class="formula-desc">Forms an airtight closed contour bounded by the sparkline above and the chart baseline below.</div>
          </div>

          <p>The area path is filled with a vertical SVG <code>&lt;linearGradient&gt;</code> defined in the <code>&lt;defs&gt;</code> block with <code>x1="0" y1="0" x2="0" y2="1"</code>. The top color stop is set to the primary metric accent (such as <code>#C1DD2D</code>) with an opacity of 0.25 to 0.35, while the bottom color stop transitions smoothly to <code>opacity="0"</code> at the baseline. This creates a luminous, soft glow beneath the trendline that guides the viewer's eye without obscuring background dashboard cards.</p>
        </section>

        <section id="endpoint-anchoring">
          <h2>5. Endpoint Anchoring: Highlighting First, Last, Min, and Max Points</h2>
          <p>In accordance with Edward Tufte's data-ink optimization principles, a sparkline should not rely on external axis callouts to communicate key inflection points. Instead, key points are highlighted directly on the vector path via miniature circular anchors and direct value text:</p>

          <ul>
            <li><strong>Latest Value Dot (Terminal Anchor):</strong> Placed on the final point <code>(x<sub>N-1</sub>, y<sub>N-1</sub>)</code> with radius r=3.5px. It signals the current real-time state of the metric and is typically rendered with a bright accent fill and a 1.5px background-colored border.</li>
            <li><strong>Historical Peak (Max Marker):</strong> Placed on the absolute highest point <code>(x<sub>max</sub>, y<sub>max</sub>)</code> in the series. In financial trading or latency dashboards, identifying the peak resistance level provides instant risk context.</li>
            <li><strong>Historical Trough (Min Marker):</strong> Placed on the absolute lowest point <code>(x<sub>min</sub>, y<sub>min</sub>)</code>. Often rendered in red or amber to indicate drawdown severity.</li>
            <li><strong>Reference Baseline Band:</strong> In high-frequency operational monitoring, a subtle gray horizontal band spanning from the target minimum to target maximum threshold illustrates whether the current metric is operating within acceptable service level agreements (SLAs).</li>
          </ul>

          <p>To prevent circular markers from clipping against the edges of the SVG canvas, the SVG container should always specify <code>overflow="visible"</code> in its CSS styling, and coordinate calculations must enforce a protective padding margin <code>p &ge; 4px</code>.</p>
        </section>

        <!-- Interactive Developer Studio -->
        <section id="interactive-sparkline-studio">
          <h2>6. Interactive SVG Sparkline &amp; Micro-Chart Studio</h2>
          <p>Explore real-time micro-visualization in the studio below. Switch between live enterprise metric presets, toggle between linear polyline, Catmull-Rom spline, gradient area, and discrete micro-bar rendering modes, adjust stroke thickness, toggle endpoint anchors, and export clean, production-ready standalone SVG source code.</p>

          <div class="interactive-sandbox">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                <span>Interactive SVG Sparkline &amp; Micro-Chart Studio</span>
              </div>
              <span class="sandbox-badge">Real-Time Micro Engine</span>
            </div>

            <div class="sandbox-controls">
              <div class="control-row">
                <label for="sparkPresetSelect">Telemetry Metric Preset</label>
                <select id="sparkPresetSelect" class="control-select">
                  <option value="volatility">Cryptocurrency Volatility (BTC/USD)</option>
                  <option value="signups">SaaS Free Trial Signups (Hourly)</option>
                  <option value="memory">Server RAM Pressure (Kubernetes Pod)</option>
                  <option value="latency">API Edge Latency (Milliseconds)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="sparkRenderModeSelect">Rendering Mode Architecture</label>
                <select id="sparkRenderModeSelect" class="control-select">
                  <option value="spline">Catmull-Rom Spline + Gradient Area</option>
                  <option value="linear">Piecewise Linear Polyline + Area</option>
                  <option value="lineOnly">Pure Minimalist Stroke (No Fill)</option>
                  <option value="microbar">Discrete Micro-Bar Column Matrix</option>
                </select>
              </div>

              <div class="control-row">
                <label for="sparkStrokeWidthRange">Stroke Thickness (<span id="sparkStrokeVal" class="stat-num">2.0</span>px)</label>
                <input type="range" id="sparkStrokeWidthRange" class="control-input" min="1" max="4" value="2" step="0.5">
              </div>
            </div>

            <div class="control-btn-group">
              <button type="button" class="toggle-btn active" id="btnToggleDots">Show Min/Max &amp; End Dots</button>
              <button type="button" class="toggle-btn active" id="btnToggleGradient">Translucent Gradient Area</button>
            </div>

            <div class="preview-stage-container">
              <div class="spark-card-wrapper">
                <div class="spark-card-header">
                  <div>
                    <div id="sparkCardTitle" class="spark-metric-title">Bitcoin / USD (1H)</div>
                    <div id="sparkCardValue" class="spark-metric-val">$94,250</div>
                  </div>
                  <div id="sparkCardDelta" class="spark-delta-badge positive">+8.4% &uarr;</div>
                </div>

                <svg id="sparkStudioCanvas" class="spark-svg-canvas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 80" width="320" height="80" role="img" aria-label="Interactive SVG Sparkline Preview">
                  <!-- Rendered dynamically via JS -->
                </svg>
              </div>
            </div>

            <div class="stats-readout-box">
              <div class="stat-item">
                <span class="stat-label">Period Data Points</span>
                <span id="statSparkPoints" class="stat-val highlight">16 Samples</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Period Peak (High)</span>
                <span id="statSparkHigh" class="stat-val">$96,800</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Period Trough (Low)</span>
                <span id="statSparkLow" class="stat-val">$88,400</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">DOM Element Count</span>
                <span id="statDOMCount" class="stat-val highlight">3 Nodes</span>
              </div>
            </div>

            <div class="action-btn-row">
              <button type="button" class="copy-btn" id="btnCopySparkSVG">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
                <span>Copy Standalone SVG</span>
              </button>
            </div>
          </div>
        </section>

        <section id="production-es6-engine">
          <h2>7. Production-Grade ES6 Sparkline Component: Zero-Dependency Architecture</h2>
          <p>Below is the complete, self-contained, enterprise-grade ES6 implementation of <code>SVGSparkline</code>. It supports linear polyline, Catmull-Rom splines, translucent area gradient fills, endpoint dot anchoring, and standalone SVG export without third-party charting libraries.</p>

          <pre><code>/**
 * SVGSparkline - Production Zero-Dependency Micro-Chart Visualizer
 * Fully WCAG 2.2 AA compliant with Catmull-Rom splines &amp; gradient area fills.
 */
class SVGSparkline {
  constructor(container, options = {}) {
    this.container = typeof container === 'string' ? document.querySelector(container) : container;
    this.width = options.width || 320;
    this.height = options.height || 80;
    this.padding = options.padding !== undefined ? options.padding : 6;
    this.strokeWidth = options.strokeWidth || 2;
    this.color = options.color || '#C1DD2D';
    this.smooth = options.smooth !== undefined ? options.smooth : true;
    this.showArea = options.showArea !== undefined ? options.showArea : true;
    this.showDots = options.showDots !== undefined ? options.showDots : true;
    this.data = options.data || [];
    this.init();
  }

  init() {
    this.svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    this.svg.setAttribute('viewBox', `0 0 ${this.width} ${this.height}`);
    this.svg.setAttribute('role', 'graphics-symbol');
    this.svg.setAttribute('aria-label', 'Metric Trendline Sparkline');
    this.svg.style.width = '100%';
    this.svg.style.height = 'auto';
    this.svg.style.overflow = 'visible';
    this.container.innerHTML = '';
    this.container.appendChild(this.svg);
    this.render();
  }

  render() {
    this.svg.innerHTML = '';
    const N = this.data.length;
    if (N &lt; 2) return;

    const min = Math.min(...this.data);
    const max = Math.max(...this.data);
    const range = (max - min) || 1;
    const plotH = this.height - 2 * this.padding;

    // Map coordinates
    const points = this.data.map((v, i) =&gt; ({
      x: (i / (N - 1)) * this.width,
      y: this.padding + (1 - (v - min) / range) * plotH
    }));

    // Defs for Linear Gradient
    const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
    const gradId = 'sparkGrad_' + Math.random().toString(36).substr(2, 6);
    const grad = document.createElementNS('http://www.w3.org/2000/svg', 'linearGradient');
    grad.setAttribute('id', gradId);
    grad.setAttribute('x1', '0');
    grad.setAttribute('y1', '0');
    grad.setAttribute('x2', '0');
    grad.setAttribute('y2', '1');

    const stop1 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
    stop1.setAttribute('offset', '0%');
    stop1.setAttribute('stop-color', this.color);
    stop1.setAttribute('stop-opacity', '0.35');

    const stop2 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
    stop2.setAttribute('offset', '100%');
    stop2.setAttribute('stop-color', this.color);
    stop2.setAttribute('stop-opacity', '0.0');

    grad.appendChild(stop1);
    grad.appendChild(stop2);
    defs.appendChild(grad);
    this.svg.appendChild(defs);

    // Build Path
    let pathD = '';
    if (this.smooth) {
      pathD = this.buildCatmullRom(points);
    } else {
      pathD = points.map((p, i) =&gt; (i === 0 ? `M ${p.x.toFixed(1)} ${p.y.toFixed(1)}` : `L ${p.x.toFixed(1)} ${p.y.toFixed(1)}`)).join(' ');
    }

    // Render Area Fill
    if (this.showArea) {
      const areaD = `${pathD} L ${this.width} ${this.height} L 0 ${this.height} Z`;
      const areaPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      areaPath.setAttribute('d', areaD);
      areaPath.setAttribute('fill', `url(#${gradId})`);
      this.svg.appendChild(areaPath);
    }

    // Render Line Stroke
    const linePath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    linePath.setAttribute('d', pathD);
    linePath.setAttribute('fill', 'none');
    linePath.setAttribute('stroke', this.color);
    linePath.setAttribute('stroke-width', this.strokeWidth);
    linePath.setAttribute('stroke-linecap', 'round');
    linePath.setAttribute('stroke-linejoin', 'round');
    this.svg.appendChild(linePath);

    // Render Terminal Anchor Dot
    if (this.showDots) {
      const lastP = points[points.length - 1];
      const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      dot.setAttribute('cx', lastP.x.toFixed(1));
      dot.setAttribute('cy', lastP.y.toFixed(1));
      dot.setAttribute('r', '3.5');
      dot.setAttribute('fill', this.color);
      dot.setAttribute('stroke', '#0A0A0A');
      dot.setAttribute('stroke-width', '1.5');
      this.svg.appendChild(dot);
    }
  }

  buildCatmullRom(pts) {
    let d = `M ${pts[0].x.toFixed(1)} ${pts[0].y.toFixed(1)}`;
    for (let i = 0; i &lt; pts.length - 1; i++) {
      const p0 = pts[i === 0 ? 0 : i - 1];
      const p1 = pts[i];
      const p2 = pts[i + 1];
      const p3 = pts[i + 2 &gt;= pts.length ? i + 1 : i + 2];

      const cp1x = p1.x + (p2.x - p0.x) / 6;
      const cp1y = p1.y + (p2.y - p0.y) / 6;
      const cp2x = p2.x - (p3.x - p1.x) / 6;
      const cp2y = p2.y - (p3.y - p1.y) / 6;

      d += ` C ${cp1x.toFixed(1)} ${cp1y.toFixed(1)}, ${cp2x.toFixed(1)} ${cp2y.toFixed(1)}, ${p2.x.toFixed(1)} ${p2.y.toFixed(1)}`;
    }
    return d;
  }
}</code></pre>
        </section>

        <section id="virtual-scrolling-and-performance">
          <h2>8. Virtual Scrolling, DOM Overhead &amp; High-Frequency Streaming Optimization</h2>
          <p>The primary technical hurdle encountered when deploying sparklines in real-world applications is scale. In a financial securities trading terminal or microservice mesh monitoring console, a single page may render a table with 500 rows, each row hosting three sparklines (CPU, Memory, Network I/O). In total, this represents 1,500 active charts.</p>

          <p>If implemented with traditional heavy charting tools or individual canvas elements, allocating 1,500 canvas backing stores consumes several gigabytes of GPU memory, resulting in browser crashes. In contrast, 1,500 SVG sparklines represent merely 4,500 lightweight DOM nodes. However, even with SVG, rendering 4,500 nodes simultaneously in a single unvirtualized document causes scroll jank. To achieve silky 120 FPS performance, production engineering teams implement three key architectural patterns:</p>

          <ul>
            <li><strong>DOM Virtualization:</strong> By coupling sparklines with a virtualized list container (such as TanStack Virtual or react-window), only the rows currently visible within the viewport are mounted into the DOM. As the user scrolls, exiting sparkline paths are unmounted and entering paths are instantiated.</li>
            <li><strong>Shared Gradient Defs:</strong> Instead of embedding a distinct <code>&lt;defs&gt;</code> container with gradient definitions inside every single sparkline instance, a single global gradient container is mounted in the root page markup, and all sparklines reference it via <code>fill="url(#globalSparkGrad)"</code>. This trims DOM memory by up to 40%.</li>
            <li><strong>CSS content-visibility:</strong> Applying <code>content-visibility: auto</code> and <code>contain-intrinsic-size: 320px 80px</code> instructs the browser rendering engine to skip layout and painting for off-screen sparklines entirely until they approach the viewport boundary.</li>
          </ul>

          <p>For cross-paradigm comparisons with alternative analytical layouts, explore our guides on <a href="/articles/svg-donut-charts-and-circular-percentage-visualization-guide/">SVG donut and circular percentage charts</a>, <a href="/articles/svg-bar-charts-and-column-graph-visualization-guide/">Cartesian bar and column graphs</a>, and <a href="/articles/svg-funnel-charts-and-conversion-pipeline-visualization-guide/">conversion funnel pipeline charts</a>.</p>

          <div class="takeaway-box">
            <h3>Key Architectural Takeaways</h3>
            <ul>
              <li><strong>Tufte Data-Ink Rule:</strong> Omit axes, tick marks, and decorative frames to maximize the data-ink ratio in sub-100px viewports.</li>
              <li><strong>Catmull-Rom Splines:</strong> Deploy C1 continuous cubic Bézier splines to smooth trendlines without artificial peak overshoot.</li>
              <li><strong>Translucent Area Fills:</strong> Close path contours against the bottom baseline (<code>L W H L 0 H Z</code>) to provide volumetric weight without obscuring background content.</li>
              <li><strong>Zero Dependencies:</strong> A vanilla ES6 sparkline engine requires under 8KB of code, delivers 120 FPS rendering, and satisfies all WCAG 2.2 AA accessibility mandates.</li>
            </ul>
          </div>
        </section>

        <section id="frequently-asked-questions" class="faq-section">
          <h2>9. Frequently Asked Questions</h2>
          <div class="faq-item">
            <div class="faq-question">What is an SVG sparkline and how does it differ from a standard full-size line chart?</div>
            <div class="faq-answer">Coined by statistician Edward Tufte, a sparkline is a small, high-density, word-sized data graphic designed to be embedded directly inline with prose, metrics cards, or dense tabular rows. Unlike full-size line charts that feature elaborate Y-axis labels, tick grids, and legends, a sparkline eliminates all peripheral chart junk to maximize the data-ink ratio, communicating historical trend, volatility, and direction at a glance.</div>
          </div>

          <div class="faq-item">
            <div class="faq-question">How do you project arbitrary data points into a compact SVG sparkline viewBox?</div>
            <div class="faq-answer">For N chronological values [y_0, y_1, ..., y_(N-1)] mapped into a viewport of width W and height H with vertical padding p, the X-coordinate scales uniformly as x_i = (i / (N - 1)) * W. The Y-coordinate maps inversely to handle SVG top-left origin: y_i = p + (1 - (v_i - min) / (max - min || 1)) * (H - 2 * p). If all values are identical, min equals max and the line centers vertically at H / 2.</div>
          </div>

          <div class="faq-item">
            <div class="faq-question">What is the mathematical difference between polyline sparklines and Catmull-Rom spline sparklines?</div>
            <div class="faq-answer">An SVG polyline connects adjacent points with straight linear segments (L x y), producing sharp angular peaks that can feel mechanical at small scales. A Catmull-Rom spline calculates cubic Bézier control points (C cp1x cp1y, cp2x cp2y, x y) using neighboring data points, guaranteeing first-order derivative continuity (C1 smoothness) so the curve passes through every data point without overshoot.</div>
          </div>

          <div class="faq-item">
            <div class="faq-question">How do you construct a closed area gradient fill under an SVG sparkline?</div>
            <div class="faq-answer">An area fill is created by starting at the bottom-left baseline (M x_0 H), drawing straight up to the first data point (L x_0 y_0), tracing the sparkline path to the final point (x_(N-1), y_(N-1)), dropping straight down to the bottom-right baseline (L x_(N-1) H), and closing the path (Z) back to the start. The closed path is filled with a vertical linearGradient transitioning from a semi-transparent accent to fully transparent at the baseline.</div>
          </div>

          <div class="faq-item">
            <div class="faq-question">How do you render high-impact endpoint dots and min/max peak markers without visual clipping?</div>
            <div class="faq-answer">Tufte sparkline conventions emphasize marking the latest endpoint value with a colored dot and highlighting historical min/max extremes. To prevent circular markers from clipping against the SVG viewport edges, the chart includes vertical and horizontal padding p &ge; markerRadius + strokeWidth. In CSS, setting overflow: visible on the SVG container ensures marker circles extend gracefully into surrounding margin space without truncation.</div>
          </div>

          <div class="faq-item">
            <div class="faq-question">How do you ensure thousands of inline SVG sparklines in dense data tables do not degrade DOM performance?</div>
            <div class="faq-answer">In large enterprise tables displaying hundreds of rows with sparklines, embedding full SVG trees can bloat DOM memory. Production systems optimize performance by using virtualized scrolling (only mounting visible rows), sharing a single SVG defs linearGradient across all instances via id reference, generating compact path strings without extra wrapper groups, and applying content-visibility: auto to off-screen table rows.</div>
          </div>
        </section>
      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <a href="#tufte-data-ink-theory">1. Tufte's Data-Ink Theory</a>
            <a href="#normalization-mathematics">2. Normalization Mathematics</a>
            <a href="#polyline-vs-spline">3. Polyline vs. Catmull-Rom Spline</a>
            <a href="#gradient-area-fills">4. Gradient Area Fills &amp; Baselines</a>
            <a href="#endpoint-anchoring">5. Endpoint Anchoring &amp; Dots</a>
            <a href="#interactive-sparkline-studio">6. Interactive Sparkline Studio</a>
            <a href="#production-es6-engine">7. Production ES6 Engine</a>
            <a href="#virtual-scrolling-and-performance">8. Virtual Scrolling &amp; Scale</a>
            <a href="#frequently-asked-questions">9. Frequently Asked Questions</a>
          </nav>
        </div>

        <div class="cta-sidebar-box">
          <h4>Explore 134K+ Free SVG Icons</h4>
          <p>Looking for micro-icons to accompany your dashboard trendline metrics? Browse IconStash's comprehensive open-source icon repository.</p>
          <a href="/#/" class="header-cta" style="display:inline-block; text-align:center;">Browse Free Icons</a>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 IconStash.io &bull; Precision Vector Graphics &amp; Developer Resources.</p>
    <p style="margin-top: 8px;"><a href="/">Home</a> &bull; <a href="/articles/">Articles</a> &bull; <a href="/about/">About</a> &bull; <a href="/privacy/">Privacy</a></p>
  </footer>

  <script>
    (function() {
      // Theme toggle functionality
      const themeToggle = document.getElementById('themeToggle');
      if (themeToggle) {
        themeToggle.addEventListener('click', function() {
          const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
          const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
          document.documentElement.setAttribute('data-theme', nextTheme);
        });
      }

      // Studio Datasets
      const presets = {
        volatility: {
          title: 'Bitcoin / USD (1H)',
          currentVal: '$94,250',
          delta: '+8.4% ↑',
          isPositive: true,
          color: '#C1DD2D',
          values: [88400, 89100, 88900, 90200, 91400, 90800, 92100, 93400, 92800, 94100, 93600, 95200, 96800, 95900, 94800, 94250]
        },
        signups: {
          title: 'SaaS Free Trial Signups',
          currentVal: '1,420 /hr',
          delta: '+14.2% ↑',
          isPositive: true,
          color: '#38BDF8',
          values: [920, 960, 1020, 1080, 1140, 1100, 1220, 1280, 1240, 1310, 1360, 1420, 1480, 1450, 1390, 1420]
        },
        memory: {
          title: 'Server RAM Pressure',
          currentVal: '84.6%',
          delta: '+2.8% ↑',
          isPositive: false,
          color: '#F59E0B',
          values: [62, 64, 63, 68, 71, 69, 74, 76, 75, 78, 81, 82, 86, 85, 83, 84.6]
        },
        latency: {
          title: 'API Edge Latency (p99)',
          currentVal: '14.2 ms',
          delta: '-18.5% ↓',
          isPositive: true,
          color: '#10B981',
          values: [28, 26, 24, 25, 22, 21, 19, 18, 17, 16, 15, 16, 14, 15, 14.5, 14.2]
        }
      };

      // Controls
      const presetSelect = document.getElementById('sparkPresetSelect');
      const renderModeSelect = document.getElementById('sparkRenderModeSelect');
      const strokeWidthRange = document.getElementById('sparkStrokeWidthRange');
      const strokeValSpan = document.getElementById('sparkStrokeVal');
      const btnToggleDots = document.getElementById('btnToggleDots');
      const btnToggleGradient = document.getElementById('btnToggleGradient');
      const btnCopySparkSVG = document.getElementById('btnCopySparkSVG');
      const svgCanvas = document.getElementById('sparkStudioCanvas');

      // Card Header Readouts
      const cardTitle = document.getElementById('sparkCardTitle');
      const cardValue = document.getElementById('sparkCardValue');
      const cardDelta = document.getElementById('sparkCardDelta');

      // Stats
      const statSparkPoints = document.getElementById('statSparkPoints');
      const statSparkHigh = document.getElementById('statSparkHigh');
      const statSparkLow = document.getElementById('statSparkLow');
      const statDOMCount = document.getElementById('statDOMCount');

      let showDots = true;
      let showGradient = true;
      let activePresetKey = 'volatility';

      function renderStudio() {
        const preset = presets[activePresetKey];
        const mode = renderModeSelect.value;
        const strokeW = parseFloat(strokeWidthRange.value);
        strokeValSpan.textContent = strokeWidthRange.value;

        cardTitle.textContent = preset.title;
        cardValue.textContent = preset.currentVal;
        cardDelta.textContent = preset.delta;
        cardDelta.className = 'spark-delta-badge ' + (preset.isPositive ? 'positive' : 'negative');

        const W = 320;
        const H = 80;
        const padding = 8;
        const plotH = H - 2 * padding;

        svgCanvas.innerHTML = '';

        const min = Math.min(...preset.values);
        const max = Math.max(...preset.values);
        const range = (max - min) || 1;
        const N = preset.values.length;

        // Map coordinates
        const points = preset.values.map((v, i) => ({
          x: (i / (N - 1)) * W,
          y: padding + (1 - (v - min) / range) * plotH
        }));

        let nodeCount = 0;

        if (mode === 'microbar') {
          const barW = (W / N) * 0.7;
          const stepW = W / N;

          preset.values.forEach((v, i) => {
            const h = ((v - min) / range) * plotH + 4;
            const x = i * stepW + (stepW - barW) / 2;
            const y = H - h;

            const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            rect.setAttribute('x', x.toFixed(1));
            rect.setAttribute('y', y.toFixed(1));
            rect.setAttribute('width', barW.toFixed(1));
            rect.setAttribute('height', h.toFixed(1));
            rect.setAttribute('fill', i === N - 1 ? preset.color : '#444444');
            rect.setAttribute('rx', '1.5');
            svgCanvas.appendChild(rect);
            nodeCount++;
          });
        } else {
          // Defs for gradient
          const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
          const gradId = 'studioSparkGrad';
          const grad = document.createElementNS('http://www.w3.org/2000/svg', 'linearGradient');
          grad.setAttribute('id', gradId);
          grad.setAttribute('x1', '0');
          grad.setAttribute('y1', '0');
          grad.setAttribute('x2', '0');
          grad.setAttribute('y2', '1');

          const s1 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
          s1.setAttribute('offset', '0%');
          s1.setAttribute('stop-color', preset.color);
          s1.setAttribute('stop-opacity', '0.35');

          const s2 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
          s2.setAttribute('offset', '100%');
          s2.setAttribute('stop-color', preset.color);
          s2.setAttribute('stop-opacity', '0.0');

          grad.appendChild(s1);
          grad.appendChild(s2);
          defs.appendChild(grad);
          svgCanvas.appendChild(defs);

          let pathD = '';
          if (mode === 'spline') {
            pathD = buildCatmullRom(points);
          } else {
            pathD = points.map((p, i) => (i === 0 ? `M ${p.x.toFixed(1)} ${p.y.toFixed(1)}` : `L ${p.x.toFixed(1)} ${p.y.toFixed(1)}`)).join(' ');
          }

          // Area Fill
          if (showGradient && mode !== 'lineOnly') {
            const areaD = `${pathD} L ${W} ${H} L 0 ${H} Z`;
            const areaPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            areaPath.setAttribute('d', areaD);
            areaPath.setAttribute('fill', `url(#${gradId})`);
            svgCanvas.appendChild(areaPath);
            nodeCount++;
          }

          // Stroke Path
          const linePath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
          linePath.setAttribute('d', pathD);
          linePath.setAttribute('fill', 'none');
          linePath.setAttribute('stroke', preset.color);
          linePath.setAttribute('stroke-width', strokeW);
          linePath.setAttribute('stroke-linecap', 'round');
          linePath.setAttribute('stroke-linejoin', 'round');
          svgCanvas.appendChild(linePath);
          nodeCount++;

          // Anchor Dots
          if (showDots) {
            // Min dot
            const minIdx = preset.values.indexOf(min);
            const minP = points[minIdx];
            const dotMin = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            dotMin.setAttribute('cx', minP.x.toFixed(1));
            dotMin.setAttribute('cy', minP.y.toFixed(1));
            dotMin.setAttribute('r', '3');
            dotMin.setAttribute('fill', '#EF4444');
            dotMin.setAttribute('stroke', '#0A0A0A');
            dotMin.setAttribute('stroke-width', '1.5');
            svgCanvas.appendChild(dotMin);
            nodeCount++;

            // Max dot
            const maxIdx = preset.values.indexOf(max);
            const maxP = points[maxIdx];
            const dotMax = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            dotMax.setAttribute('cx', maxP.x.toFixed(1));
            dotMax.setAttribute('cy', maxP.y.toFixed(1));
            dotMax.setAttribute('r', '3');
            dotMax.setAttribute('fill', '#10B981');
            dotMax.setAttribute('stroke', '#0A0A0A');
            dotMax.setAttribute('stroke-width', '1.5');
            svgCanvas.appendChild(dotMax);
            nodeCount++;

            // Endpoint dot
            const endP = points[points.length - 1];
            const dotEnd = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            dotEnd.setAttribute('cx', endP.x.toFixed(1));
            dotEnd.setAttribute('cy', endP.y.toFixed(1));
            dotEnd.setAttribute('r', '3.5');
            dotEnd.setAttribute('fill', preset.color);
            dotEnd.setAttribute('stroke', '#0A0A0A');
            dotEnd.setAttribute('stroke-width', '1.5');
            svgCanvas.appendChild(dotEnd);
            nodeCount++;
          }
        }

        // Update Stats
        statSparkPoints.textContent = `${N} Samples`;
        statSparkHigh.textContent = typeof max === 'number' && max > 1000 ? `$${max.toLocaleString()}` : `${max}`;
        statSparkLow.textContent = typeof min === 'number' && min > 1000 ? `$${min.toLocaleString()}` : `${min}`;
        statDOMCount.textContent = `${nodeCount} Nodes`;
      }

      function buildCatmullRom(pts) {
        let d = `M ${pts[0].x.toFixed(1)} ${pts[0].y.toFixed(1)}`;
        for (let i = 0; i < pts.length - 1; i++) {
          const p0 = pts[i === 0 ? 0 : i - 1];
          const p1 = pts[i];
          const p2 = pts[i + 1];
          const p3 = pts[i + 2 >= pts.length ? i + 1 : i + 2];

          const cp1x = p1.x + (p2.x - p0.x) / 6;
          const cp1y = p1.y + (p2.y - p0.y) / 6;
          const cp2x = p2.x - (p3.x - p1.x) / 6;
          const cp2y = p2.y - (p3.y - p1.y) / 6;

          d += ` C ${cp1x.toFixed(1)} ${cp1y.toFixed(1)}, ${cp2x.toFixed(1)} ${cp2y.toFixed(1)}, ${p2.x.toFixed(1)} ${p2.y.toFixed(1)}`;
        }
        return d;
      }

      presetSelect.addEventListener('change', (e) => {
        activePresetKey = e.target.value;
        renderStudio();
      });

      renderModeSelect.addEventListener('change', renderStudio);
      strokeWidthRange.addEventListener('input', renderStudio);

      btnToggleDots.addEventListener('click', () => {
        showDots = !showDots;
        btnToggleDots.classList.toggle('active', showDots);
        renderStudio();
      });

      btnToggleGradient.addEventListener('click', () => {
        showGradient = !showGradient;
        btnToggleGradient.classList.toggle('active', showGradient);
        renderStudio();
      });

      btnCopySparkSVG.addEventListener('click', () => {
        let svgSource = svgCanvas.outerHTML;
        if (!svgSource.includes('xmlns=')) {
          svgSource = svgSource.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ');
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(svgSource).then(() => {
            const originalText = btnCopySparkSVG.innerHTML;
            btnCopySparkSVG.innerHTML = '<span>SVG Copied!</span>';
            setTimeout(() => { btnCopySparkSVG.innerHTML = originalText; }, 2000);
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
          const originalText = btnCopySparkSVG.innerHTML;
          btnCopySparkSVG.innerHTML = '<span>SVG Copied!</span>';
          setTimeout(() => { btnCopySparkSVG.innerHTML = originalText; }, 2000);
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
