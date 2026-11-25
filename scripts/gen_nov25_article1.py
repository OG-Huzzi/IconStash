import os

html = r"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <title>SVG Line Charts: Multi-Series Splines &amp; Crosshairs (2026) | IconStash</title>
  <meta name="description" content="Build zero-dependency SVG line charts with Fritsch-Carlson monotone cubic splines, nice axis ticks, crosshair bisectors, and WCAG 2.2 AA accessibility.">
  <meta name="keywords" content="svg line chart, how to create a line chart in svg, multi-series line chart svg, monotone cubic interpolation svg, interactive svg line chart javascript, svg line graph tooltip, responsive svg line chart">
  <meta property="og:title" content="Mastering SVG Line Charts &amp; Multi-Series Time-Series Graphs (2026)">
  <meta property="og:description" content="Build zero-dependency SVG line charts with Fritsch-Carlson monotone cubic splines, nice axis ticks, crosshair bisectors, and WCAG 2.2 AA accessibility.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-line-charts-and-multi-series-time-series-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-line-charts-and-multi-series-time-series-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-25T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-25T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="Data Visualization">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="SVG Line Chart">
  <meta property="article:tag" content="Time-Series Visualization">
  <meta property="article:tag" content="Monotone Cubic Spline">
  <meta property="article:tag" content="JavaScript">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mastering SVG Line Charts &amp; Multi-Series Time-Series Graphs (2026)">
  <meta name="twitter:description" content="Build zero-dependency SVG line charts with Fritsch-Carlson monotone cubic splines, nice axis ticks, crosshair bisectors, and WCAG 2.2 AA accessibility.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-line-charts-and-multi-series-time-series-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-line-charts-and-multi-series-time-series-guide/">
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
      "headline": "Mastering SVG Line Charts & Multi-Series Time-Series Graphs (2026)",
      "description": "Build zero-dependency SVG line charts with Fritsch-Carlson monotone cubic splines, nice axis ticks, crosshair bisectors, and WCAG 2.2 AA accessibility.",
      "image": "https://iconstash.io/assets/articles/svg-line-charts-and-multi-series-time-series-guide.jpg",
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
      "datePublished": "2026-11-25",
      "dateModified": "2026-11-25",
      "mainEntityOfPage": "https://iconstash.io/articles/svg-line-charts-and-multi-series-time-series-guide/",
      "inLanguage": "en-US",
      "wordCount": 4245,
      "articleSection": "Data Visualization",
      "keywords": [
        "svg line chart",
        "how to create a line chart in svg",
        "multi-series line chart svg",
        "monotone cubic interpolation svg",
        "interactive svg line chart javascript",
        "svg line graph tooltip",
        "responsive svg line chart"
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
          "name": "SVG Line Charts & Multi-Series Time-Series Guide",
          "item": "https://iconstash.io/articles/svg-line-charts-and-multi-series-time-series-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Should I use an SVG polyline or an SVG path element for a line chart?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Use an SVG path element for production line charts. While polyline works for simple straight-line segments, path supports smooth cubic Bezier curves (C), discontinuous gaps via move commands (M) for missing null data, area fill closures, and stroke-dasharray draw animations with getTotalLength()."
          }
        },
        {
          "@type": "Question",
          "name": "Why do smooth Catmull-Rom SVG line charts overshoot data peaks and how do you fix it?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Standard Catmull-Rom splines compute unconstrained tangents from neighboring points, causing curves to bulge above local maxima or dip below zero between flat and steep segments. Replacing Catmull-Rom with Fritsch-Carlson monotone cubic Hermite interpolation clamps tangent magnitudes whenever adjacent slopes differ or change sign, guaranteeing zero overshoot."
          }
        },
        {
          "@type": "Question",
          "name": "How do you build a responsive SVG line chart without distorting stroke thickness?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Define a fixed internal coordinate system via viewBox (such as 0 0 760 440) paired with CSS width: 100% and height: auto. To prevent stroke lines from shrinking below 1px on mobile viewports, add vector-effect='non-scaling-stroke' to data paths or use container-aware typography scaling."
          }
        },
        {
          "@type": "Question",
          "name": "How does a multi-series SVG crosshair bisector find the nearest data point?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Instead of attaching hover listeners to tiny individual circles, capture pointermove on the plot overlay, convert clientX into SVG user-space coordinates via getBoundingClientRect(), invert the X scale back to domain index, and perform an O(log n) binary search bisector to snap to the nearest timestamp across all active series simultaneously."
          }
        },
        {
          "@type": "Question",
          "name": "When should a developer choose SVG over HTML5 Canvas for line charts?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Choose SVG for datasets up to roughly 2,000 points per series because SVG delivers infinite Retina sharpness, native DOM accessibility, CSS variable theming, and server-side rendering without hydration flicker. Switch to HTML5 Canvas or WebGL only for high-frequency telemetry exceeding 10,000 live streaming vertices per frame."
          }
        },
        {
          "@type": "Question",
          "name": "How do you animate an SVG line chart drawing itself on page load?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Measure the exact geometric arc length of the rendered SVG path using pathElement.getTotalLength(), set stroke-dasharray and stroke-dashoffset to that length, and transition stroke-dashoffset to zero via CSS or Web Animations API while respecting prefers-reduced-motion: reduce."
          }
        },
        {
          "@type": "Question",
          "name": "How do you make a multi-series SVG line chart accessible under WCAG 2.2 AA?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Assign role='graphics-document' to the root SVG, pair series colors with distinct stroke-dasharray patterns and marker shapes so information never relies on color alone, implement keyboard ArrowLeft and ArrowRight scrubbing via a focusable slider element with an aria-live readout, and include a visually hidden sr-only HTML data table."
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
    @media (max-width: 980px) { .article-layout { grid-template-columns: 1fr; } .article-sidebar { position: static; } }

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
    table.data-table { width: 100%; border-collapse: collapse; font-size: 14.5px; text-align: left; }
    .data-table th { background: #141414; color: #FFF; font-weight: 700; padding: 14px 18px; border-bottom: 1px solid #242424; white-space: nowrap; }
    .data-table td { padding: 14px 18px; border-bottom: 1px solid #1A1A1A; color: #AAA; vertical-align: top; }
    .data-table tr:last-child td { border-bottom: none; }
    .data-table tr:hover td { background: rgba(255,255,255,0.02); }

    .interactive-sandbox { background: #121212; border: 1px solid #262626; border-radius: 10px; padding: 24px; margin: 36px 0 44px; box-shadow: 0 12px 36px rgba(0,0,0,0.3); }
    .sandbox-header { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px; border-bottom: 1px solid #242424; padding-bottom: 16px; margin-bottom: 20px; }
    .sandbox-title { font-size: 18px; font-weight: 800; color: #FFF; display: flex; align-items: center; gap: 8px; }
    .sandbox-badge { font-size: 11px; font-weight: 700; text-transform: uppercase; background: rgba(193,221,45,0.12); color: #C1DD2D; padding: 3px 8px; border-radius: 4px; border: 1px solid rgba(193,221,45,0.25); }
    .sandbox-controls { display: grid; grid-template-columns: repeat(auto-fit, minmax(195px, 1fr)); gap: 16px; margin-bottom: 20px; }
    .control-row { display: flex; flex-direction: column; gap: 6px; }
    .control-row label { font-size: 12.5px; font-weight: 600; color: #999; }
    .control-select, .control-input { background: #1A1A1A; border: 1px solid #333; border-radius: 6px; color: #FFF; padding: 8px 12px; font-size: 13.5px; outline: none; font-family: inherit; }
    .control-select:focus, .control-input:focus { border-color: #C1DD2D; }

    .preview-stage-container { background: #0D0D0D; border: 1px solid #222; border-radius: 8px; padding: 20px; display: flex; justify-content: center; align-items: center; position: relative; min-height: 440px; user-select: none; touch-action: none; }
    .line-svg-canvas { width: 100%; max-width: 760px; height: auto; touch-action: none; cursor: crosshair; outline: none; }
    .line-svg-canvas:focus-visible { outline: 2px solid #C1DD2D; outline-offset: 4px; border-radius: 6px; }

    .stats-readout-box { background: #161616; border: 1px solid #262626; border-radius: 8px; padding: 14px 18px; margin-top: 18px; display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px; }
    .stat-item { display: flex; flex-direction: column; }
    .stat-label { font-size: 11px; text-transform: uppercase; color: #888; font-weight: 600; }
    .stat-val { font-size: 15.5px; font-weight: 800; color: #FFF; font-family: "JetBrains Mono", monospace; }
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
    .cta-sidebar-box .cta-title { font-size: 15px; color: #C1DD2D; margin-bottom: 8px; font-weight: 700; }
    .cta-sidebar-box p { font-size: 13px; color: #BBB; line-height: 1.5; margin-bottom: 12px; }

    .takeaway-box { background: #121212; border: 1px solid #242424; border-radius: 8px; padding: 24px 28px; margin: 36px 0; }
    .takeaway-box h3 { color: #C1DD2D; font-size: 19px; margin-top: 0; margin-bottom: 14px; }
    .takeaway-box ul { margin-bottom: 0; }

    .warning-box { background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-left: 4px solid #EF4444; border-radius: 6px; padding: 18px 22px; margin: 28px 0; }
    .warning-box .warning-title { color: #F87171; font-size: 15px; font-weight: 700; margin-bottom: 8px; }
    .warning-box p { color: #E5E5E5; margin-bottom: 0; font-size: 14.5px; }

    .faq-section { margin-top: 56px; padding-top: 32px; border-top: 1px solid #222; }
    .faq-item { border: 1px solid #222; border-radius: 8px; margin-bottom: 14px; background: #121212; overflow: hidden; }
    .faq-question { padding: 18px 22px; font-size: 16px; font-weight: 700; color: #FFF; display: flex; justify-content: space-between; align-items: center; }
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
    html[data-theme="light"] .featured-summary li { color: #3F3F46; }
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
    html[data-theme="light"] .cta-sidebar-box .cta-title { color: #064E3B; }
    html[data-theme="light"] .cta-sidebar-box p { color: #047857; }
    html[data-theme="light"] .table-container { border-color: #E4E4E7; }
    html[data-theme="light"] .data-table th { background: #F4F4F5; color: #18181B; border-bottom-color: #E4E4E7; }
    html[data-theme="light"] .data-table td { border-bottom-color: #E4E4E7; color: #3F3F46; }
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
    html[data-theme="light"] .formula-card { background: #F4F4F5; border-color: #E4E4E7; border-left-color: #849E00; }
    html[data-theme="light"] .formula-body { color: #18181B; }
    html[data-theme="light"] .formula-title { color: #4D6300; }
    html[data-theme="light"] .formula-desc { color: #52525B; }
    html[data-theme="light"] .takeaway-box { background: #F4F4F5; border-color: #E4E4E7; }
    html[data-theme="light"] .takeaway-box h3 { color: #4D6300; }
    html[data-theme="light"] .warning-box { background: #FEF2F2; border-color: #FECACA; border-left-color: #DC2626; }
    html[data-theme="light"] .warning-box .warning-title { color: #991B1B; }
    html[data-theme="light"] .warning-box p { color: #7F1D1D; }
    html[data-theme="light"] .faq-item { background: #F4F4F5; border-color: #E4E4E7; }
    html[data-theme="light"] .faq-question { color: #18181B; }
    html[data-theme="light"] .faq-answer { color: #3F3F46; }
  </style>
</head>
<body>
  <header class="site-header">
    <a href="/" class="logo">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
        <polyline points="2 17 12 22 22 17"></polyline>
        <polyline points="2 12 12 17 22 12"></polyline>
      </svg>
      <span>IconStash</span>
    </a>
    <nav>
      <a href="/articles/">Articles</a>
      <a href="/stats/">Stats</a>
      <a href="/about/">About</a>
      <button type="button" class="theme-toggle-btn" id="theme-toggle" aria-label="Toggle visual theme">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
          <line x1="1" y1="12" x2="3" y2="12"></line>
          <line x1="21" y1="12" x2="23" y2="12"></line>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>
      </button>
      <a href="/articles/" class="header-cta">Browse 138 Guides</a>
    </nav>
  </header>

  <div class="page-container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">IconStash</a>
      <span class="sep">/</span>
      <a href="/articles/">Articles</a>
      <span class="sep">/</span>
      <span class="current">SVG Line Charts &amp; Multi-Series Time-Series</span>
    </nav>

    <header class="article-hero">
      <span class="tag">Data Visualization</span>
      <h1>Mastering SVG Line Charts &amp; Multi-Series Time-Series Graphs: Monotone Cubic Splines, Bisector Crosshairs &amp; Axis Scaling (2026)</h1>
      <div class="article-meta">
        <span>Published by <a href="/about/">Jouni Flemming</a></span>
        <span>•</span>
        <span>Updated November 25, 2026</span>
        <span>•</span>
        <span>30 min read</span>
        <span>•</span>
        <span>4,245 words</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">
        <div class="featured-summary">
          <p><strong>Direct Answer:</strong> A production-grade SVG line chart maps sorted domain tuples into an inverted SVG <code>viewBox</code> using affine scales, renders continuous curves via Fritsch-Carlson monotone cubic Bézier paths (preventing artificial spline overshoot), generates human-readable ticks with Heckbert nice-number rounding, and tracks multi-series hover states through an O(log n) binary-search crosshair bisector.</p>
          <ul>
            <li><strong>Zero-Overshoot Splines:</strong> Learn why naive Catmull-Rom curves fabricate impossible negative dips or phantom peaks, and implement Fritsch-Carlson monotone Hermite tangents in under 35 lines of Vanilla JavaScript.</li>
            <li><strong>Multi-Series Domain Unification:</strong> Compute global min/max envelopes across arbitrary series, handle null gaps cleanly with SVG <code>M</code> jumps, and snap axis ticks to clean <code>1, 2, 5 × 10ⁿ</code> intervals.</li>
            <li><strong>O(log n) Crosshair Bisector:</strong> Replace brittle per-circle mouseover listeners with pointer-captured SVG coordinate inversion and binary search scrubbing that works identically on desktop and mobile touchscreens.</li>
            <li><strong>Live Interactive Studio:</strong> Experiment with real-time SaaS, API latency, and cloud throughput datasets, switch interpolation engines, scrub the crosshair with mouse, touch, or keyboard arrows, and export clean standalone SVG markup.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-line-charts-and-multi-series-time-series-guide.jpg"
               alt="Multi-series SVG line chart with glowing lime and cyan monotone cubic splines and crosshair indicator"
               width="1200" height="675"
               fetchpriority="high" decoding="async">
          <figcaption>Figure 1: Multi-series SVG line chart architecture combining monotone cubic splines, precision coordinate grids, and synchronized crosshair bisectors.</figcaption>
        </figure>

        <section id="section-svg-vs-canvas">
          <h2>1. Why Native SVG Dominates Canvas for Interactive Line Charts</h2>
          <p><strong>Short Answer:</strong> Native SVG outperforms HTML5 Canvas for almost every product analytics, financial, and SaaS dashboard line chart under 2,000 points per series because SVG renders vector-crisp typography at any Retina DPI, integrates directly with CSS custom properties for dark/light theming, hydrates cleanly in server-side frameworks without layout shift, and exposes native DOM nodes for WCAG 2.2 AA assistive technologies.</p>

          <p>Line charts are the undisputed workhorse of quantitative user interfaces. Whenever a frontend engineer renders revenue growth, API tail latency, CPU utilization, or conversion velocity over time, the first architectural decision is whether to draw pixels onto an HTML5 Canvas bitmap or compose vector paths inside an inline <code>&lt;svg&gt;</code> element. Many teams reflexively install a 120 KB third-party charting bundle backed by Canvas, only to encounter blurry axis labels on 3x mobile displays, broken dark-mode transitions, empty server-rendered HTML shells during Core Web Vitals measurement, and inaccessible opaque rectangles that screen readers cannot inspect.</p>

          <p>Understanding when native, zero-dependency SVG is superior—and precisely where its DOM scaling ceiling begins—lets you build charts that load in microseconds, render razor-sharp curves on 6K monitors, and export directly as standalone vector assets. Compare the architectural trade-offs across browser rendering engines in the benchmark matrix below.</p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th scope="col">Architectural Dimension</th>
                  <th scope="col">Native Inline SVG</th>
                  <th scope="col">HTML5 2D Canvas</th>
                  <th scope="col">WebGL / WebGPU</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Optimal Series Scale</strong></td>
                  <td>10 to 2,500 vertices per series</td>
                  <td>2,500 to 50,000 vertices</td>
                  <td>50,000 to 5,000,000+ vertices</td>
                </tr>
                <tr>
                  <td><strong>Retina / High-DPI Crispness</strong></td>
                  <td>Infinite mathematical vector resolution</td>
                  <td>Requires manual <code>devicePixelRatio</code> scaling</td>
                  <td>Requires MSAA / shader antialiasing</td>
                </tr>
                <tr>
                  <td><strong>SSR &amp; Zero-CLS Hydration</strong></td>
                  <td>Native HTML markup streams immediately</td>
                  <td>Blank bitmap until client JS executes</td>
                  <td>Blank canvas plus shader compile delay</td>
                </tr>
                <tr>
                  <td><strong>CSS Variables &amp; Theme Switch</strong></td>
                  <td>Instant via <code>var(--token)</code> &amp; <code>currentColor</code></td>
                  <td>Requires full JS canvas repaint on toggle</td>
                  <td>Requires uniform buffer re-upload</td>
                </tr>
                <tr>
                  <td><strong>Accessibility (WCAG 2.2 AA)</strong></td>
                  <td>Native ARIA roles, focusable DOM nodes</td>
                  <td>Requires parallel shadow DOM / fallback table</td>
                  <td>Requires parallel shadow DOM / fallback table</td>
                </tr>
                <tr>
                  <td><strong>Bundle Footprint</strong></td>
                  <td>0 KB external dependencies (~3 KB helper)</td>
                  <td>Usually 40 KB–180 KB library overhead</td>
                  <td>100 KB–450 KB GPU runtime</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p>For 95% of web applications—including executive telemetry, billing dashboards, observability charts, and editorial reports—series contain between 12 and 365 daily or hourly buckets. At that cardinality, an entire multi-series SVG chart uses fewer than 80 DOM nodes and paints in under 0.4 milliseconds. Even better, pairing native SVG with the principles in our <a href="/articles/svg-charts-and-data-visualization-from-scratch-guide/">zero-dependency SVG charts architecture guide</a> removes third-party runtime vulnerabilities and keeps JavaScript main-thread blocking time near zero.</p>

          <h3>The Core Web Vitals Advantage of Declarative SVG Charts</h3>
          <p>When Googlebot and real user monitoring (RUM) pipelines measure Largest Contentful Paint (LCP) and Cumulative Layout Shift (CLS), declarative SVG line charts deliver two decisive advantages over client-mounted Canvas widgets. First, by declaring explicit <code>viewBox="0 0 760 440"</code>, <code>width="760"</code>, and <code>height="440"</code> attributes alongside <code>width: 100%; height: auto;</code> in CSS, the browser reserves the exact aspect ratio box during initial HTML parse, guaranteeing a CLS score of <code>0.000</code>. Second, because every curve is simply an ASCII path string inside <code>&lt;path d="..."&gt;</code>, Next.js React Server Components, Astro islands, and static site generators can stream the fully painted chart in the initial document payload before JavaScript hydrates interactivity.</p>
        </section>

        <section id="section-polyline-vs-path">
          <h2>2. Polyline vs. Path Architecture &amp; Coordinate Mapping</h2>
          <p><strong>Short Answer:</strong> While <code>&lt;polyline points="..."&gt;</code> works for trivial single-segment sparklines, production line charts should always use <code>&lt;path d="..."&gt;</code> because <code>&lt;path&gt;</code> natively supports cubic Bézier curves (<code>C</code>), missing-data gaps via disconnected <code>M</code> jumps, seamless area-under-curve closures, and hardware-friendly dash animations.</p>

          <p>Every SVG line chart begins with two core geometric problems: choosing the right vector primitive and transforming abstract business data—timestamps, dollar amounts, millisecond latencies—into inverted browser viewport pixels. Getting this foundation right prevents clipping bugs, distorted strokes, and fragile magic-number layouts.</p>

          <h3>Why &lt;path&gt; Beats &lt;polyline&gt; in Production Charts</h3>
          <p>At first glance, <code>&lt;polyline points="40,220 120,180 200,195"&gt;</code> looks simpler than constructing a <code>d</code> string. However, <code>&lt;polyline&gt;</code> breaks down immediately when real-world data arrives:</p>

          <ul>
            <li><strong>Missing or Null Observations:</strong> Telemetry feeds frequently drop packets or omit weekend market days. A <code>&lt;polyline&gt;</code> forces a continuous line across every vertex, misleadingly interpolating across an outage. With <code>&lt;path&gt;</code>, encountering <code>null</code> or <code>NaN</code> simply emits a new <code>M x y</code> (MoveTo) command on the next valid point, cleanly breaking the stroke without splitting the DOM element.</li>
            <li><strong>Curved Interpolation:</strong> <code>&lt;polyline&gt;</code> only connects vertices with sharp straight segments. Smooth splines require cubic (<code>C</code>) or quadratic (<code>Q</code>) Bézier commands that exist exclusively inside <code>&lt;path&gt;</code>.</li>
            <li><strong>Closed Area Fills:</strong> Combining a line chart with a subtle translucent gradient underneath requires closing the bottom edge down to the baseline (<code>L x_end y_base L x_start y_base Z</code>). A <code>&lt;polyline&gt;</code> cannot reliably separate stroke rendering from closed area geometry without duplicating coordinates.</li>
            <li><strong>Path Length Inspection:</strong> The SVGDOM method <code>SVGGeometryElement.getTotalLength()</code> and <code>getPointAtLength(distance)</code> provide exact arc-length measurements for animations and floating annotations on <code>&lt;path&gt;</code> elements across all modern engines.</li>
          </ul>

          <h3>Affine Coordinate Transformation Into Inverted SVG Space</h3>
          <p>In mathematical Cartesian space, the origin sits at the bottom-left and <code>y</code> increases upward. In SVG user space, <code>(0, 0)</code> is anchored at the top-left corner and <code>y</code> increases downward. If you fail to encapsulate this inversion inside pure scaling functions, every downstream feature—gridlines, threshold bands, tooltips, and labels—accumulates sign-flip bugs.</p>

          <p>Define an explicit margin box inside your SVG <code>viewBox</code> (for example, <code>viewBox="0 0 760 440"</code> with <code>left = 68</code>, <code>right = 28</code>, <code>top = 32</code>, <code>bottom = 52</code>). The inner plotting rectangle has width <code>W_plot = viewW - left - right</code> and height <code>H_plot = viewH - top - bottom</code>. Any sorted observation <code>(x_i, y_i)</code> maps to viewport pixels via two clean linear transformations:</p>

          <div class="formula-card">
            <div class="formula-title">Linear Domain-to-Pixel Affine Projections</div>
            <div class="formula-body">
              x_px(t) = X_left + ((t - T_min) ÷ (T_max - T_min)) × W_plot<br>
              y_px(v) = Y_top + ((Y_max - v) ÷ (Y_max - Y_min)) × H_plot
            </div>
            <div class="formula-desc">
              Note that (Y_max - v) inverts the vertical axis automatically: when v = Y_max, y_px equals Y_top (highest point on screen); when v = Y_min, y_px equals Y_top + H_plot (chart floor). Always guard against zero-span domains where Y_max === Y_min by expanding bounds symmetrically.
            </div>
          </div>

          <h3>Preserving Crisp Strokes with non-scaling-stroke</h3>
          <p>When a 760px-wide SVG scales down inside a 340px smartphone container, its internal coordinate system shrinks by roughly 55%. A <code>stroke-width="2"</code> line visually thins to <code>0.9px</code>, looking washed out against dark backgrounds. Adding <code>vector-effect="non-scaling-stroke"</code> instructs the browser rasterizer to apply the stroke width in final CSS screen pixels rather than scaled SVG user units, keeping primary data lines uniformly sharp across desktop monitors and mobile viewports alike.</p>

          <h3>Time-Proportional X-Axis Scaling, UTC Alignment &amp; Irregular Intervals</h3>
          <p>A subtle accuracy trap occurs when developers map timestamps uniformly by array index (<code>x = i × step</code>) even though the underlying telemetry contains irregular intervals—such as missing weekend trading sessions, bursty incident logs, or uneven webhook retries. Mapping by array index warps the visual slope of velocity: a five-day stagnation and a five-minute jump occupy identical horizontal width, deceiving viewers about rate of change.</p>
          <p>Instead, convert every ISO 8601 date string into numeric epoch milliseconds via <code>Date.parse(row.timestamp)</code> and project linearly between <code>T_min</code> and <code>T_max</code>. Always format tick labels in UTC or an explicit IANA zone using <code>Intl.DateTimeFormat('en-US', { timeZone: 'UTC', month: 'short', day: 'numeric' })</code> so server-rendered HTML in Virginia matches client hydration in Tokyo without off-by-one-day timezone shifts.</p>
        </section>

        <section id="section-spline-interpolation">
          <h2>3. Smooth Line Interpolation: Fritsch-Carlson Monotone Cubic vs. Catmull-Rom</h2>
          <p><strong>Short Answer:</strong> Never use unconstrained Catmull-Rom or naive midpoint Bézier smoothing for quantitative time-series charts because they create false peaks and dips between data points. Use Fritsch-Carlson monotone cubic Hermite interpolation, which guarantees mathematically that the curve never exceeds local data maxima or drops below local minima.</p>

          <p>If you search online tutorials for "smooth SVG line chart," nine out of ten code snippets compute cubic Bézier control points using a fixed tension multiplier on neighboring deltas—commonly a simplified Catmull-Rom spline. While Catmull-Rom curves look organically pleasing for abstract illustrations or <a href="/articles/svg-bezier-curves-and-path-math-guide/">generative SVG Bézier ribbons</a>, they commit a cardinal sin in data visualization: <strong>interpolation overshoot</strong>.</p>

          <p>Consider a SaaS uptime metric or conversion percentage sitting steady at <code>0%</code> for three days, jumping to <code>100%</code> on day four, and remaining at <code>100%</code> on day five. An unconstrained Catmull-Rom spline calculates a steep positive slope entering day four and dips <em>below 0%</em> between days two and three, then bulges <em>above 100%</em> between days four and five. An executive glancing at that chart sees impossible <code>-8%</code> or <code>107%</code> values that never existed in the database.</p>

          <h3>Mathematical Derivation of Fritsch-Carlson Monotone Cubic Splines</h3>
          <p>Published by F. N. Fritsch and R. E. Carlson in 1980 (<em>SIAM Journal on Numerical Analysis</em>), monotone piecewise cubic interpolation preserves monotonicity wherever the underlying data is monotonic, and enforces zero-slope horizontal tangents at local extrema. Here is the exact algorithm that D3's <code>curveMonotoneX</code> uses under the hood, implemented cleanly in zero-dependency JavaScript:</p>

          <ol>
            <li><strong>Compute Secant Slopes:</strong> For each interval <code>k</code> between point <code>P_k = (x_k, y_k)</code> and <code>P_{k+1} = (x_{k+1}, y_{k+1})</code>, calculate the segment width <code>h_k = x_{k+1} - x_k</code> and secant slope <code>m_k = (y_{k+1} - y_k) ÷ h_k</code>.</li>
            <li><strong>Initial Interior Tangents:</strong> For interior vertices <code>k = 1 … n - 2</code>, inspect the adjacent secant slopes <code>m_{k-1}</code> and <code>m_k</code>. If they have opposite signs (<code>m_{k-1} × m_k ≤ 0</code>) or either slope is zero, the vertex is a local peak, trough, or flat plateau—set its tangent <code>d_k = 0</code>. Otherwise, compute the weighted harmonic mean (Brodlie modification for non-uniform x-spacing): <code>d_k = 3 × (h_{k-1} + h_k) ÷ ((2 × h_k + h_{k-1}) ÷ m_{k-1} + (h_k + 2 × h_{k-1}) ÷ m_k)</code>.</li>
            <li><strong>Endpoint Tangents:</strong> Compute one-sided boundary derivatives <code>d_0</code> and <code>d_{n-1}</code> using a shape-preserving three-point formula clamped to the same sign as the adjacent secant slope so endpoints never curl backward.</li>
            <li><strong>Fritsch-Carlson Monotonicity Clamping:</strong> For every segment <code>k</code> where <code>m_k ≠ 0</code>, define normalized slope ratios <code>α_k = d_k ÷ m_k</code> and <code>β_k = d_{k+1} ÷ m_k</code>. A sufficient condition for strict monotonicity is <code>α_k² + β_k² ≤ 9</code>. Whenever <code>τ = √(α_k² + β_k²) &gt; 3</code>, rescale both tangents by <code>3 ÷ τ</code>: <code>d_k = (3 ÷ τ) × α_k × m_k</code> and <code>d_{k+1} = (3 ÷ τ) × β_k × m_k</code>.</li>
            <li><strong>Convert Hermite Tangents to SVG Cubic Bézier (C):</strong> Finally, convert each segment's endpoint tangents <code>d_k, d_{k+1}</code> into SVG cubic control points placed at one-third horizontal steps: <code>cp1 = (x_k + h_k ÷ 3, y_k + d_k × h_k ÷ 3)</code> and <code>cp2 = (x_{k+1} - h_k ÷ 3, y_{k+1} - d_{k+1} × h_k ÷ 3)</code>.</li>
          </ol>

          <div class="formula-card">
            <div class="formula-title">Monotone Hermite-to-SVG Cubic Bézier Conversion</div>
            <div class="formula-body">
              C (x_k + h_k/3), (y_k + d_k × h_k/3), (x_{k+1} - h_k/3), (y_{k+1} - d_{k+1} × h_k/3), x_{k+1}, y_{k+1}
            </div>
            <div class="formula-desc">
              Where h_k = x_{k+1} - x_k and tangent slopes d_k satisfy α_k² + β_k² ≤ 9. Because control point x-coordinates sit strictly at 1/3 and 2/3 of the interval, the curve is always a single-valued function of x and never loops or overshoots local data bounds.
            </div>
          </div>

          <pre><code>// Zero-dependency Fritsch-Carlson Monotone Cubic SVG Path Generator
function buildMonotoneCubicPath(pts) {
  const n = pts.length;
  if (n === 0) return '';
  if (n === 1) return `M ${pts[0].x.toFixed(2)} ${pts[0].y.toFixed(2)}`;
  if (n === 2) return `M ${pts[0].x.toFixed(2)} ${pts[0].y.toFixed(2)} L ${pts[1].x.toFixed(2)} ${pts[1].y.toFixed(2)}`;

  const h = new Array(n - 1);
  const m = new Array(n - 1);
  for (let i = 0; i &lt; n - 1; i++) {
    h[i] = Math.max(1e-6, pts[i + 1].x - pts[i].x);
    m[i] = (pts[i + 1].y - pts[i].y) / h[i];
  }

  const d = new Array(n).fill(0);
  // Brodlie weighted harmonic mean for interior tangents
  for (let i = 1; i &lt; n - 1; i++) {
    if (m[i - 1] * m[i] &gt; 0) {
      const w1 = 2 * h[i] + h[i - 1];
      const w2 = h[i] + 2 * h[i - 1];
      d[i] = (w1 + w2) / (w1 / m[i - 1] + w2 / m[i]);
    }
  }

  // Endpoint one-sided tangents
  d[0] = ((2 * h[0] + h[1]) * m[0] - h[0] * m[1]) / (h[0] + h[1]);
  if (d[0] * m[0] &lt;= 0) d[0] = 0;
  else if (Math.abs(d[0]) &gt; 3 * Math.abs(m[0])) d[0] = 3 * m[0];

  const last = n - 1;
  d[last] = ((2 * h[last - 1] + h[last - 2]) * m[last - 1] - h[last - 1] * m[last - 2]) / (h[last - 1] + h[last - 2]);
  if (d[last] * m[last - 1] &lt;= 0) d[last] = 0;
  else if (Math.abs(d[last]) &gt; 3 * Math.abs(m[last - 1])) d[last] = 3 * m[last - 1];

  // Monotonicity clamping (alpha^2 + beta^2 &lt;= 9)
  for (let i = 0; i &lt; n - 1; i++) {
    if (m[i] === 0) {
      d[i] = 0;
      d[i + 1] = 0;
      continue;
    }
    const alpha = d[i] / m[i];
    const beta = d[i + 1] / m[i];
    const mag = Math.hypot(alpha, beta);
    if (mag &gt; 3) {
      const tau = 3 / mag;
      d[i] = tau * alpha * m[i];
      d[i + 1] = tau * beta * m[i];
    }
  }

  let path = `M ${pts[0].x.toFixed(2)} ${pts[0].y.toFixed(2)}`;
  for (let i = 0; i &lt; n - 1; i++) {
    const dx = h[i] / 3;
    const cp1x = pts[i].x + dx;
    const cp1y = pts[i].y + d[i] * dx;
    const cp2x = pts[i + 1].x - dx;
    const cp2y = pts[i + 1].y - d[i + 1] * dx;
    path += ` C ${cp1x.toFixed(2)} ${cp1y.toFixed(2)}, ${cp2x.toFixed(2)} ${cp2y.toFixed(2)}, ${pts[i + 1].x.toFixed(2)} ${pts[i + 1].y.toFixed(2)}`;
  }
  return path;
}</code></pre>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th scope="col">Curve Algorithm</th>
                  <th scope="col">Peak Overshoot Risk</th>
                  <th scope="col">SVG Command</th>
                  <th scope="col">Best Production Use Case</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Linear Polyline</strong></td>
                  <td>Zero (exact piecewise linear)</td>
                  <td><code>M x y L x y</code></td>
                  <td>Financial prices, SLA error spikes, scientific telemetry</td>
                </tr>
                <tr>
                  <td><strong>Monotone Cubic (Fritsch-Carlson)</strong></td>
                  <td>Zero (strictly bounded)</td>
                  <td><code>C cp1x cp1y, cp2x cp2y, x y</code></td>
                  <td>Executive KPIs, SaaS growth curves, latency percentiles</td>
                </tr>
                <tr>
                  <td><strong>Catmull-Rom Centripetal</strong></td>
                  <td>Moderate (can bulge at step jumps)</td>
                  <td><code>C cp1x cp1y, cp2x cp2y, x y</code></td>
                  <td>Organic waveforms, ambient background visuals</td>
                </tr>
                <tr>
                  <td><strong>Step-After (Piecewise Constant)</strong></td>
                  <td>Zero (orthogonal transitions)</td>
                  <td><code>H x_{i+1} V y_{i+1}</code></td>
                  <td>Feature flag rollouts, pricing tier changes, server counts</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <section id="section-architecture-pipeline">
          <h2>4. Figure 2: Multi-Series SVG Line Chart Rendering Pipeline</h2>
          <p>Engineering a resilient multi-series line chart requires separating data normalization from SVG DOM synthesis. When datasets update via live filters or WebSocket streams, passing raw arrays through a deterministic four-stage pipeline ensures that domain unification, nice-tick generation, monotone Bézier compilation, and crosshair hit-testing stay synchronized without layout jitter.</p>

          <figure class="article-figure">
            <svg viewBox="0 0 960 320" width="960" height="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figure 2: Multi-Series SVG Line Chart Rendering Pipeline Diagram">
              <rect width="960" height="320" fill="#0D0D0D" rx="8" stroke="#222222" stroke-width="1"></rect>
              <defs>
                <marker id="lcArrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
                  <polygon points="0 0, 8 3, 0 6" fill="#C1DD2D"></polygon>
                </marker>
              </defs>

              <g transform="translate(24, 40)">
                <rect width="196" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="98" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="700" text-anchor="middle">STAGE 1: UNIFY DOMAIN</text>
                <text x="98" y="56" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Multi-Series Envelope</text>
                <rect x="18" y="78" width="160" height="28" fill="#1C1C1C" rx="4"></rect>
                <text x="98" y="96" fill="#A3A3A3" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">[S1, S2, S3] -&gt; [min, max]</text>
                <text x="98" y="136" fill="#CCCCCC" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">Heckbert Nice Ticks</text>
                <text x="98" y="156" fill="#888888" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">1, 2, 5 x 10^n intervals</text>
                <rect x="18" y="182" width="160" height="28" fill="#1C1C1C" rx="4" stroke="#C1DD2D" stroke-width="0.6"></rect>
                <text x="98" y="200" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Null Gap Partitioning</text>
                <text x="98" y="228" fill="#666666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Deterministic Scale Bounds</text>
              </g>

              <line x1="220" y1="160" x2="250" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#lcArrow)"></line>

              <g transform="translate(258, 40)">
                <rect width="196" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="98" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="700" text-anchor="middle">STAGE 2: PROJECTION</text>
                <text x="98" y="56" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Viewport Scale Matrix</text>
                <rect x="18" y="78" width="160" height="28" fill="#1C1C1C" rx="4"></rect>
                <text x="98" y="96" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">y_px = top + (max-v)*k</text>
                <text x="98" y="136" fill="#CCCCCC" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">Margin Box Clipping</text>
                <text x="98" y="156" fill="#888888" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">viewBox 760 x 440</text>
                <rect x="18" y="182" width="160" height="28" fill="#1C1C1C" rx="4" stroke="#38BDF8" stroke-width="0.6"></rect>
                <text x="98" y="200" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Grid + Axis Scaffolding</text>
                <text x="98" y="228" fill="#666666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">crispEdges Gridlines</text>
              </g>

              <line x1="454" y1="160" x2="484" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#lcArrow)"></line>

              <g transform="translate(492, 40)">
                <rect width="196" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="98" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="700" text-anchor="middle">STAGE 3: SPLINE ENGINE</text>
                <text x="98" y="56" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Path &amp; Gradient Synthesis</text>
                <rect x="18" y="78" width="160" height="28" fill="#1C1C1C" rx="4"></rect>
                <text x="98" y="96" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Fritsch-Carlson d_k</text>
                <text x="98" y="136" fill="#CCCCCC" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">a^2 + b^2 &lt;= 9 Clamp</text>
                <text x="98" y="156" fill="#888888" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">M / C / L / H Commands</text>
                <rect x="18" y="182" width="160" height="28" fill="#1C1C1C" rx="4" stroke="#A855F7" stroke-width="0.6"></rect>
                <text x="98" y="200" fill="#A855F7" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">non-scaling-stroke</text>
                <text x="98" y="228" fill="#666666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Optional Area Fill &lt;defs&gt;</text>
              </g>

              <line x1="688" y1="160" x2="718" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#lcArrow)"></line>

              <g transform="translate(726, 40)">
                <rect width="210" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="105" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="700" text-anchor="middle">STAGE 4: INTERACTION</text>
                <text x="105" y="56" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Bisector &amp; Accessibility</text>
                <rect x="18" y="78" width="174" height="28" fill="#1C1C1C" rx="4"></rect>
                <text x="105" y="96" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">O(log n) Binary Bisect</text>
                <text x="105" y="136" fill="#CCCCCC" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">Pointer Capture Scrub</text>
                <text x="105" y="156" fill="#888888" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">ArrowLeft / ArrowRight</text>
                <rect x="18" y="182" width="174" height="28" fill="#1C1C1C" rx="4" stroke="#C1DD2D" stroke-width="0.6"></rect>
                <text x="105" y="200" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">ARIA + Standalone SVG</text>
                <text x="105" y="228" fill="#666666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">WCAG 2.2 AA Verified</text>
              </g>
            </svg>
            <figcaption>Figure 2: End-to-end rendering pipeline transforming raw multi-series observations into monotone cubic SVG paths, crisp axis scaffolding, and O(log n) interactive crosshairs.</figcaption>
          </figure>
        </section>

        <section id="section-nice-ticks">
          <h2>5. Nice-Number Axis Tick Generation &amp; Multi-Series Scaling</h2>
          <p><strong>Short Answer:</strong> Dividing a raw data range by five evenly produces ugly fractional tick labels like <code>13.4</code>, <code>26.8</code>, and <code>40.2</code>. Implement Paul Heckbert's "Nice Numbers for Graph Labels" algorithm to snap tick spacing to multiples of <code>1</code>, <code>2</code>, or <code>5 × 10ⁿ</code>, then expand <code>Y_min</code> and <code>Y_max</code> outward to exact tick boundaries.</p>

          <p>Nothing distinguishes a handcrafted dashboard from an amateur script faster than Y-axis tick labeling. When raw metrics range from <code>3.7</code> to <code>94.2</code>, naive division creates unreadable decimals that slow cognitive comprehension. Conversely, rounding arbitrarily can leave the highest data peak floating awkwardly above the top gridline.</p>

          <h3>Heckbert's Nice-Number Algorithm in Practice</h3>
          <p>Paul Heckbert's classic Graphics Gems algorithm solves both problems simultaneously in under twenty lines of arithmetic. Given a raw minimum, raw maximum, and desired target tick count (typically 5 or 6 intervals), the algorithm calculates the order of magnitude of the span, chooses the cleanest rounded step size from <code>{1, 2, 5, 10}</code>, and snaps both domain endpoints outward via <code>Math.floor</code> and <code>Math.ceil</code>:</p>

          <pre><code>// Heckbert Nice-Number Tick Generator for Clean Axis Intervals
function niceNum(range, round) {
  const exponent = Math.floor(Math.log10(range));
  const fraction = range / Math.pow(10, exponent);
  let niceFraction;

  if (round) {
    if (fraction &lt; 1.5) niceFraction = 1;
    else if (fraction &lt; 3) niceFraction = 2;
    else if (fraction &lt; 7) niceFraction = 5;
    else niceFraction = 10;
  } else {
    if (fraction &lt;= 1) niceFraction = 1;
    else if (fraction &lt;= 2) niceFraction = 2;
    else if (fraction &lt;= 5) niceFraction = 5;
    else niceFraction = 10;
  }
  return niceFraction * Math.pow(10, exponent);
}

function generateNiceTicks(minVal, maxVal, maxTicks = 6) {
  const span = Math.max(1e-6, maxVal - minVal);
  const niceRange = niceNum(span, false);
  const tickSpacing = niceNum(niceRange / (maxTicks - 1), true);
  const graphMin = Math.floor(minVal / tickSpacing) * tickSpacing;
  const graphMax = Math.ceil(maxVal / tickSpacing) * tickSpacing;

  const ticks = [];
  for (let t = graphMin; t &lt;= graphMax + tickSpacing * 0.5; t += tickSpacing) {
    ticks.push(Number(t.toFixed(6)));
  }
  return { graphMin, graphMax, tickSpacing, ticks };
}</code></pre>

          <h3>Zero-Baseline Integrity vs. Zoomed Operational Ranges</h3>
          <p>A critical visual design rule governs whether your Y-axis should anchor at zero. For cumulative volume metrics—monthly recurring revenue, unit sales, or server request counts—starting the axis at <code>minVal = 0</code> preserves honest proportional comparison so a 2% increase does not visually masquerade as a 300% explosion. However, for tightly bounded physical or financial series like body temperature (<code>97°F–103°F</code>), stock prices, or conversion rates hovering between <code>98.5%</code> and <code>99.99%</code>, forcing a zero baseline flattens all variance into an unreadable horizontal sliver. Offering an explicit zero-anchor configuration flag per dataset keeps visual honesty intact without sacrificing analytical legibility.</p>

          <h3>Unified Multi-Series Envelopes &amp; Null Data Gaps</h3>
          <p>When plotting three series simultaneously—such as P50, P95, and P99 API latency—every visible series must contribute to the unified <code>[minVal, maxVal]</code> envelope before tick calculation runs. If a user toggles off P99 via legend controls, recomputing the nice ticks dynamically zooms the remaining P50 and P95 curves to fill the viewport cleanly. Similarly, when a series contains <code>null</code> or <code>undefined</code> entries, splitting the vertex list into contiguous sub-arrays ensures the spline engine emits a clean <code>M</code> jump across outages instead of hallucinating interpolated values.</p>

          <h3>Why Indexed Percentage Baselines Beat Dual Y-Axes</h3>
          <p>Product teams frequently ask how to plot two series with wildly different units—such as daily active users (120,000) and average revenue per user ($42)—on the same SVG line chart. Adding a second Y-axis on the right border introduces arbitrary visual intersections: simply changing the right-axis padding changes where the two curves cross, leading executives to infer false causal correlations. Whenever comparing relative momentum across disparate units, normalize both series to an indexed baseline of <code>100</code> at <code>t = 0</code> (<code>indexed_i = (v_i ÷ v_0) × 100</code>) or stack two vertically aligned SVG charts sharing an identical X-axis and synchronized crosshair bisector.</p>
        </section>

        <section id="section-crosshair-bisector">
          <h2>6. O(log n) Bisector Crosshairs, Pointer Capture &amp; Hover Tooltips</h2>
          <p><strong>Short Answer:</strong> Attaching hover events to individual SVG <code>&lt;circle&gt;</code> markers creates dead zones between points and sluggish DOM event storms. Instead, attach <code>pointermove</code> to a single full-plot hit layer, project <code>clientX</code> into SVG user space, and run an O(log n) binary-search bisector to snap the vertical crosshair and all series readouts simultaneously.</p>

          <p>Users interacting with a modern time-series chart expect instantaneous vertical crosshair tracking: as their mouse cursor or finger glides anywhere across the chart canvas—even in blank whitespace above or below the curves—a crisp vertical guide snaps cleanly to the nearest timestamp, highlights active rings on every plotted line, and updates a unified readout without flickering.</p>

          <h3>Screen-to-SVG Inverse Coordinate Mapping</h3>
          <p>Because responsive SVG canvases scale fluidly with CSS, a <code>clientX</code> offset of <code>320px</code> on screen might correspond to <code>495.4</code> in internal <code>viewBox</code> coordinates. Relying on raw <code>e.offsetX</code> breaks across Safari sub-pixel transforms and touch pointer capture. Using <code>getBoundingClientRect()</code> with explicit zero-dimension guards provides rock-solid coordinate inversion across mouse, pen, and touch inputs:</p>

          <pre><code>// Inverse Screen-to-SVG Mapping + O(log n) Nearest Index Bisector
function getNearestIndexFromPointer(clientX, svgEl, xCoords, viewWidth) {
  const rect = svgEl.getBoundingClientRect();
  if (!rect || !rect.width) return 0;

  // Map CSS viewport pixel to internal SVG viewBox X coordinate
  const svgX = ((clientX - rect.left) / rect.width) * viewWidth;

  // Binary search (bisector) over sorted xCoords
  let lo = 0;
  let hi = xCoords.length - 1;
  if (svgX &lt;= xCoords[0]) return 0;
  if (svgX &gt;= xCoords[hi]) return hi;

  while (lo &lt;= hi) {
    const mid = (lo + hi) &gt;&gt; 1;
    if (xCoords[mid] === svgX) return mid;
    if (xCoords[mid] &lt; svgX) lo = mid + 1;
    else hi = mid - 1;
  }

  // Compare lo (first greater) and hi (last smaller) to pick closest snap
  return (svgX - xCoords[hi]) &lt;= (xCoords[lo] - svgX) ? hi : lo;
}</code></pre>

          <h3>Mobile Touch Scrubbing with Pointer Capture &amp; touch-action: none</h3>
          <p>On iOS Safari and Android Chrome, dragging a finger horizontally across a chart triggers native browser back/forward swipe navigation or vertical scroll jitter unless explicitly prevented. Declaring <code>touch-action: none; user-select: none;</code> on the chart container hands full gesture control to your JavaScript handler. Calling <code>setPointerCapture(e.pointerId)</code> on <code>pointerdown</code>—paired with symmetrical cleanup on both <code>pointerup</code> and <code>pointercancel</code>—ensures smooth 60 FPS scrubbing even if the user's finger drifts temporarily outside the chart border.</p>
        </section>

        <section id="section-interactive-studio">
          <h2>7. Interactive SVG Multi-Series Line Chart Studio</h2>
          <p>Test our zero-dependency multi-series SVG rendering engine live below. Switch between production datasets, compare <strong>Fritsch-Carlson Monotone Cubic</strong> against <strong>Catmull-Rom</strong>, <strong>Linear</strong>, and <strong>Step-After</strong> curves, adjust stroke geometry, scrub the vertical crosshair with your mouse or finger, or focus the chart and scrub using <code>ArrowLeft</code> / <code>ArrowRight</code> keys. When satisfied, click <strong>Copy Standalone SVG</strong> to export self-contained vector markup.</p>

          <div class="interactive-sandbox" id="interactive-line-studio">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C1DD2D" stroke-width="2">
                  <path d="M3 3v18h18"></path>
                  <path d="M7 14l4-4 4 3 5-7"></path>
                </svg>
                <span>Interactive SVG Multi-Series Line Chart Studio</span>
              </div>
              <span class="sandbox-badge">Monotone Cubic Engine</span>
            </div>

            <div class="sandbox-controls">
              <div class="control-row">
                <label for="lc-preset-select">Time-Series Dataset</label>
                <select id="lc-preset-select" class="control-select">
                  <option value="saas-arr" selected>SaaS ARR vs. Net Expansion ($M)</option>
                  <option value="api-latency">API Tail Latency P50 / P95 / P99 (ms)</option>
                  <option value="cloud-traffic">Edge Requests vs. Cache Hits (k/s)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="lc-curve-select">Curve Interpolation</label>
                <select id="lc-curve-select" class="control-select">
                  <option value="monotone" selected>Monotone Cubic (Zero Overshoot)</option>
                  <option value="catmull">Catmull-Rom Spline</option>
                  <option value="linear">Linear Polyline (Exact)</option>
                  <option value="step">Step-After (Piecewise)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="lc-stroke-slider">Stroke Width (<span id="lc-stroke-val">2.5px</span>)</label>
                <input type="range" id="lc-stroke-slider" class="control-input" min="1.5" max="4.5" step="0.5" value="2.5">
              </div>

              <div class="control-row">
                <label for="lc-marker-select">Vertex Markers &amp; Area</label>
                <select id="lc-marker-select" class="control-select">
                  <option value="markers-area" selected>Markers + Area Tint</option>
                  <option value="markers-only">Markers Only (Clean Lines)</option>
                  <option value="lines-only">Lines Only (Minimal)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="lc-series-select">Visible Series Scope</label>
                <select id="lc-series-select" class="control-select">
                  <option value="all" selected>All 3 Series (Unified Scale)</option>
                  <option value="top2">Top 2 Series Only</option>
                  <option value="primary">Primary Series Only</option>
                </select>
              </div>
            </div>

            <div class="preview-stage-container">
              <svg id="lc-live-canvas" class="line-svg-canvas" viewBox="0 0 760 440" width="760" height="440" xmlns="http://www.w3.org/2000/svg" tabindex="0" role="slider" aria-label="Interactive Multi-Series SVG Line Chart Crosshair Scrubber" aria-valuemin="0" aria-valuemax="11" aria-valuenow="8">
              </svg>
            </div>

            <div class="stats-readout-box" aria-live="polite">
              <div class="stat-item">
                <span class="stat-label">Active Bucket</span>
                <span class="stat-val" id="lc-stat-label">Sep</span>
              </div>
              <div class="stat-item">
                <span class="stat-label" id="lc-stat-s1-name">Series 1</span>
                <span class="stat-val highlight" id="lc-stat-s1-val">0</span>
              </div>
              <div class="stat-item">
                <span class="stat-label" id="lc-stat-s2-name">Series 2</span>
                <span class="stat-val" style="color:#38BDF8;" id="lc-stat-s2-val">0</span>
              </div>
              <div class="stat-item">
                <span class="stat-label" id="lc-stat-s3-name">Series 3</span>
                <span class="stat-val" style="color:#A855F7;" id="lc-stat-s3-val">0</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Nice Y-Domain</span>
                <span class="stat-val" id="lc-stat-domain">[0, 100]</span>
              </div>
            </div>

            <div class="action-btn-row">
              <button type="button" class="copy-btn" id="lc-copy-code-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                  <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                <span>Copy Standalone SVG</span>
              </button>
            </div>
          </div>
        </section>

        <section id="section-production-engine">
          <h2>8. Production ES6 Line Chart Engine &amp; Stroke-Draw Animation</h2>
          <p><strong>Short Answer:</strong> To animate an SVG line chart drawing across the screen without layout thrashing, read <code>path.getTotalLength()</code> once after DOM insertion, initialize <code>stroke-dasharray</code> and <code>stroke-dashoffset</code> to that length, and animate <code>stroke-dashoffset</code> to <code>0</code> using the Web Animations API while disabling motion when <code>prefers-reduced-motion: reduce</code> matches.</p>

          <p>Shipping interactive charts in production React, Vue, or Vanilla TypeScript applications introduces subtle edge cases around animation timing, area fill gradients, and memory cleanup. Unlike bar charts—where scale transforms along the Y-axis animate easily—line charts require arc-length path reveal mechanics.</p>

          <h3>Deterministic Stroke-Draw Animation with Reduced-Motion Support</h3>
          <p>CSS keyframes cannot query a path's dynamic arc length automatically unless you normalize paths with <code>pathLength="1"</code> or calculate exact lengths in JavaScript. While <code>pathLength="1"</code> works for simple solid lines, it interferes with custom dashed secondary series (such as <code>stroke-dasharray="6 4"</code> for forecast projections). Measuring <code>getTotalLength()</code> via JavaScript preserves crisp solid-line animations while letting dashed forecast lines fade in cleanly via opacity:</p>

          <pre><code>// Accessible stroke-draw reveal respecting prefers-reduced-motion
function animateLineDraw(pathEl, durationMs = 750) {
  const prefersReduced = typeof window !== 'undefined'
    &amp;&amp; window.matchMedia
    &amp;&amp; window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (prefersReduced || typeof pathEl.getTotalLength !== 'function') {
    pathEl.style.strokeDasharray = 'none';
    pathEl.style.strokeDashoffset = '0';
    return;
  }

  const totalLen = pathEl.getTotalLength();
  pathEl.style.strokeDasharray = `${totalLen} ${totalLen}`;
  pathEl.style.strokeDashoffset = `${totalLen}`;

  if (typeof pathEl.animate === 'function') {
    pathEl.animate(
      [{ strokeDashoffset: totalLen }, { strokeDashoffset: 0 }],
      { duration: durationMs, easing: 'cubic-bezier(0.22, 1, 0.36, 1)', fill: 'forwards' }
    ).onfinish = () =&gt; {
      pathEl.style.strokeDasharray = 'none';
    };
  }
}</code></pre>

          <div class="warning-box">
            <div class="warning-title">Avoid Hardcoding Dash Lengths for Dotted Forecast Lines</div>
            <p>Never apply the <code>stroke-dashoffset</code> draw animation to a series that already uses <code>stroke-dasharray="5 5"</code> to denote projected or baseline thresholds. Overwriting <code>stroke-dasharray</code> with the full path length turns a dashed projection into a solid line during the transition. Instead, reveal dashed series using an animated SVG <code>&lt;clipPath&gt;</code> rectangle sweeping from left to right across the plot box.</p>
          </div>

          <h3>Constructing Gradient Area Fills Beneath Smooth Paths</h3>
          <p>Adding a subtle vertical linear gradient beneath the primary series visually anchors the line without cluttering overlapping curves. Rather than recomputing splines twice, append the closure straight onto the already-computed line path string: <code>const areaD = `${lineD} L ${lastX} ${baselineY} L ${firstX} ${baselineY} Z`;</code>. Always pair this with a linearGradient running from <code>stop-opacity="0.24"</code> at <code>y1="0%"</code> down to <code>stop-opacity="0"</code> at <code>y2="100%"</code> so lower gridlines remain legible.</p>

          <h3>Zero-Hydration Server Rendering in Next.js &amp; Astro</h3>
          <p>Because our spline builder, Heckbert nice-tick generator, and affine scales are pure deterministic functions over plain JavaScript numbers, the exact same module executes inside Node.js React Server Components or Astro build pipelines. You can render the complete <code>&lt;svg&gt;</code> markup on the server—delivering instant LCP painting with zero client JavaScript—and attach a tiny 1.2 KB progressive enhancement script only if the user moves a pointer or focuses the interactive crosshair scrubber. Pair that architecture with unique gradient IDs (scoped via React's <code>useId()</code>) so multiple charts on the same dashboard page never collide on <code>url(#area-grad)</code> references.</p>
        </section>

        <section id="section-accessibility">
          <h2>9. Enterprise Accessibility (WCAG 2.2 AA), Keyboard Scrubbing &amp; Testing</h2>
          <p><strong>Short Answer:</strong> Make SVG line charts WCAG 2.2 AA compliant by never encoding series identity with color alone—pair distinct colors with dash patterns and marker shapes—exposing keyboard <code>ArrowLeft</code>/<code>ArrowRight</code> scrubbing via <code>role="slider"</code> with an <code>aria-live="polite"</code> readout, and providing a screen-reader-accessible HTML table.</p>

          <p>Roughly 8% of male users and 0.5% of female users experience red-green or blue-yellow color vision deficiency. A chart displaying three thin solid lines in red, green, and orange becomes unreadable in grayscale or under deuteranopia. Enterprise design systems combine three redundant visual encodings alongside programmatic ARIA attributes:</p>

          <ul>
            <li><strong>Redundant Channel Encoding:</strong> Pair primary line color (e.g., <code>#C1DD2D</code> lime) with solid strokes and circular markers; assign secondary series (<code>#38BDF8</code> sky) subtle long dashes or diamond markers; assign tertiary series (<code>#A855F7</code> violet) crisp short dashes or square markers.</li>
            <li><strong>Focus-Visible Keyboard Scrubbing:</strong> Decorate the interactive plot region with <code>tabindex="0"</code> and <code>role="slider"</code>, updating <code>aria-valuenow</code>, <code>aria-valuetext</code>, and an accompanying <code>aria-live="polite"</code> stats panel whenever the user presses <code>ArrowLeft</code>, <code>ArrowRight</code>, <code>Home</code>, or <code>End</code>.</li>
            <li><strong>High-Contrast Theme Tokens:</strong> When toggling between dark obsidian (<code>#0A0A0A</code>) and light paper themes, adjust gridline opacity, axis label contrast (at least <code>4.5:1</code> per WCAG SC 1.4.3), and graphic stroke contrast (at least <code>3:1</code> per WCAG SC 1.4.11). Read our <a href="/articles/designing-accessible-svg-icons/">accessible SVG architecture guide</a> and <a href="/articles/how-to-change-svg-color-in-css-and-react-guide/">SVG theming guide</a> for full contrast token tables.</li>
            <li><strong>Visually Hidden Tabular Mirror:</strong> Render an off-screen <code>&lt;table class="sr-only"&gt;</code> synchronized with the chart dataset so screen-reader users can jump directly across rows and columns using native table navigation shortcuts.</li>
          </ul>

          <div class="takeaway-box">
            <h3>Production Engineering Checklist for SVG Line Charts</h3>
            <ul>
              <li>Always compute Y-axis bounds across <strong>all active series</strong> simultaneously and round ticks using Heckbert's nice-number spacing.</li>
              <li>Use <strong>Fritsch-Carlson monotone cubic</strong> paths instead of naive Catmull-Rom whenever curve smoothness must preserve exact data bounds.</li>
              <li>Split curves at <code>null</code> values using SVG <code>M</code> commands so missing telemetry never draws misleading bridge lines.</li>
              <li>Use <code>vector-effect="non-scaling-stroke"</code> and <code>shape-rendering="crispEdges"</code> on axis grids for razor-sharp rendering across viewports.</li>
              <li>Strip transient hover crosshairs before exporting standalone SVG markup via <code>outerHTML</code>.</li>
            </ul>
          </div>
        </section>

        <section id="section-faq" class="faq-section">
          <h2>10. Frequently Asked Questions</h2>

          <div class="faq-item">
            <div class="faq-question">
              <span>Should I use an SVG polyline or an SVG path element for a line chart?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Use an SVG <code>&lt;path&gt;</code> element for production line charts. While <code>&lt;polyline&gt;</code> works for simple straight-line segments, <code>&lt;path&gt;</code> supports smooth cubic Bézier curves (<code>C</code>), discontinuous gaps via move commands (<code>M</code>) for missing null data, area fill closures, and stroke-dasharray draw animations with <code>getTotalLength()</code>.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>Why do smooth Catmull-Rom SVG line charts overshoot data peaks and how do you fix it?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Standard Catmull-Rom splines compute unconstrained tangents from neighboring points, causing curves to bulge above local maxima or dip below zero between flat and steep segments. Replacing Catmull-Rom with Fritsch-Carlson monotone cubic Hermite interpolation clamps tangent magnitudes whenever adjacent slopes differ or change sign, guaranteeing zero overshoot.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How do you build a responsive SVG line chart without distorting stroke thickness?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Define a fixed internal coordinate system via <code>viewBox</code> (such as <code>0 0 760 440</code>) paired with CSS <code>width: 100%</code> and <code>height: auto</code>. To prevent stroke lines from shrinking below 1px on mobile viewports, add <code>vector-effect="non-scaling-stroke"</code> to data paths or scale typography proportionately.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How does a multi-series SVG crosshair bisector find the nearest data point?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Instead of attaching hover listeners to tiny individual circles, capture <code>pointermove</code> on the plot overlay, convert <code>clientX</code> into SVG user-space coordinates via <code>getBoundingClientRect()</code>, and perform an O(log n) binary search bisector over sorted X coordinates to snap to the nearest timestamp across all active series simultaneously.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>When should a developer choose SVG over HTML5 Canvas for line charts?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Choose SVG for datasets up to roughly 2,000 points per series because SVG delivers infinite Retina sharpness, native DOM accessibility, CSS variable theming, and server-side rendering without hydration flicker. Switch to HTML5 Canvas or WebGL only for high-frequency telemetry exceeding 10,000 live streaming vertices per frame.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How do you animate an SVG line chart drawing itself on page load?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Measure the exact geometric arc length of the rendered SVG path using <code>pathElement.getTotalLength()</code>, set <code>stroke-dasharray</code> and <code>stroke-dashoffset</code> to that length, and transition <code>stroke-dashoffset</code> to zero via CSS or Web Animations API while respecting <code>prefers-reduced-motion: reduce</code>.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How do you make a multi-series SVG line chart accessible under WCAG 2.2 AA?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Assign <code>role="graphics-document"</code> to the root SVG, pair series colors with distinct dash patterns and marker shapes so information never relies on color alone, implement keyboard <code>ArrowLeft</code> and <code>ArrowRight</code> scrubbing via a focusable slider element with an <code>aria-live</code> readout, and include a visually hidden <code>sr-only</code> HTML data table.
            </div>
          </div>
        </section>
      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <a href="#section-svg-vs-canvas">1. Why SVG Dominates Canvas</a>
            <a href="#section-polyline-vs-path">2. Polyline vs. Path &amp; Scaling</a>
            <a href="#section-spline-interpolation">3. Monotone Cubic vs. Catmull-Rom</a>
            <a href="#section-architecture-pipeline">4. Figure 2: Rendering Pipeline</a>
            <a href="#section-nice-ticks">5. Nice-Number Axis Ticks</a>
            <a href="#section-crosshair-bisector">6. O(log n) Crosshair Bisector</a>
            <a href="#section-interactive-studio">7. Interactive Line Chart Studio</a>
            <a href="#section-production-engine">8. ES6 Engine &amp; Animations</a>
            <a href="#section-accessibility">9. WCAG 2.2 AA Accessibility</a>
            <a href="#section-faq">10. Frequently Asked Questions</a>
          </nav>
        </div>

        <div class="cta-sidebar-box">
          <div class="cta-title">Explore 134,701 Free SVG Icons</div>
          <p>Search 28 open-source icon libraries side by side and export clean SVG, PNG, or React JSX in one click.</p>
          <a href="/" class="header-cta" style="display:inline-block; text-align:center;">Open IconStash</a>
        </div>
      </aside>
    </div>
  </div>

  <footer class="site-footer">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 24px; text-align: left; margin-bottom: 32px;">
      <div style="flex: 1 1 260px;">
        <div style="font-weight: 800; font-size: 16px; color: #FFF; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C1DD2D" stroke-width="2.5"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
          IconStash
        </div>
        <p style="font-size: 13.5px; color: #777; line-height: 1.6;">Open-source SVG icon search engine and developer graphics engineering resource covering 28 libraries and 134,701 vector icons.</p>
      </div>
      <div>
        <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #999; margin-bottom: 12px;">Navigation</div>
        <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13.5px;">
          <a href="/articles/">Articles &amp; Guides</a>
          <a href="/stats/">Icon Statistics</a>
          <a href="/about/">About IconStash</a>
          <a href="/privacy/">Privacy Policy</a>
        </div>
      </div>
    </div>
    <p>&copy; 2026 IconStash.io. Published by Great Software Company. All rights reserved.</p>
  </footer>

  <script>
    (function() {
      const themeBtn = document.getElementById('theme-toggle');
      if (themeBtn) {
        themeBtn.addEventListener('click', () => {
          const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
          const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
          document.documentElement.setAttribute('data-theme', newTheme);
          try { localStorage.setItem('iconstash-theme', newTheme); } catch (_) {}
        });
      }

      const presetSelect = document.getElementById('lc-preset-select');
      const curveSelect = document.getElementById('lc-curve-select');
      const strokeSlider = document.getElementById('lc-stroke-slider');
      const strokeVal = document.getElementById('lc-stroke-val');
      const markerSelect = document.getElementById('lc-marker-select');
      const seriesSelect = document.getElementById('lc-series-select');
      const liveSvg = document.getElementById('lc-live-canvas');
      const copyBtn = document.getElementById('lc-copy-code-btn');

      const statLabel = document.getElementById('lc-stat-label');
      const statS1Name = document.getElementById('lc-stat-s1-name');
      const statS1Val = document.getElementById('lc-stat-s1-val');
      const statS2Name = document.getElementById('lc-stat-s2-name');
      const statS2Val = document.getElementById('lc-stat-s2-val');
      const statS3Name = document.getElementById('lc-stat-s3-name');
      const statS3Val = document.getElementById('lc-stat-s3-val');
      const statDomain = document.getElementById('lc-stat-domain');

      const DATASETS = {
        'saas-arr': {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
          unitPre: '$',
          unitSuf: 'M',
          zeroAnchor: true,
          series: [
            { name: 'Total ARR', color: '#C1DD2D', dash: '', values: [14.2, 15.8, 17.1, 19.6, 21.0, 24.4, 26.8, 28.1, 31.5, 34.2, 37.8, 41.4] },
            { name: 'Enterprise', color: '#38BDF8', dash: '7,4', values: [8.4, 9.1, 10.2, 12.0, 12.9, 15.3, 17.0, 18.2, 20.6, 22.8, 25.4, 28.2] },
            { name: 'Self-Serve', color: '#A855F7', dash: '3,3', values: [5.8, 6.7, 6.9, 7.6, 8.1, 9.1, 9.8, 9.9, 10.9, 11.4, 12.4, 13.2] }
          ]
        },
        'api-latency': {
          labels: ['00:00', '02:00', '04:00', '06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'],
          unitPre: '',
          unitSuf: 'ms',
          zeroAnchor: true,
          series: [
            { name: 'P99 Tail', color: '#C1DD2D', dash: '', values: [88, 74, 68, 92, 148, 214, 196, 242, 228, 174, 132, 98] },
            { name: 'P95 Latency', color: '#38BDF8', dash: '7,4', values: [52, 46, 42, 58, 96, 134, 122, 149, 138, 108, 82, 61] },
            { name: 'P50 Median', color: '#A855F7', dash: '3,3', values: [21, 19, 18, 24, 38, 49, 46, 54, 51, 41, 32, 25] }
          ]
        },
        'cloud-traffic': {
          labels: ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11', 'W12'],
          unitPre: '',
          unitSuf: 'k/s',
          zeroAnchor: true,
          series: [
            { name: 'Edge Req', color: '#C1DD2D', dash: '', values: [120, 145, 145, 210, 265, 250, 290, 340, 340, 395, 420, 468] },
            { name: 'Cache Hits', color: '#38BDF8', dash: '7,4', values: [98, 121, 122, 182, 232, 219, 256, 304, 305, 358, 382, 429] },
            { name: 'Origin Pass', color: '#A855F7', dash: '3,3', values: [22, 24, 23, 28, 33, 31, 34, 36, 35, 37, 38, 39] }
          ]
        }
      };

      function niceNum(range, round) {
        const exp = Math.floor(Math.log10(range));
        const frac = range / Math.pow(10, exp);
        let nf;
        if (round) {
          if (frac < 1.5) nf = 1;
          else if (frac < 3) nf = 2;
          else if (frac < 7) nf = 5;
          else nf = 10;
        } else {
          if (frac <= 1) nf = 1;
          else if (frac <= 2) nf = 2;
          else if (frac <= 5) nf = 5;
          else nf = 10;
        }
        return nf * Math.pow(10, exp);
      }

      function computeNiceScale(minVal, maxVal, maxTicks = 6) {
        const span = Math.max(1e-4, maxVal - minVal);
        const niceRange = niceNum(span, false);
        const step = niceNum(niceRange / (maxTicks - 1), true);
        const gMin = Math.floor(minVal / step) * step;
        const gMax = Math.ceil(maxVal / step) * step;
        const ticks = [];
        for (let t = gMin; t <= gMax + step * 0.5; t += step) {
          ticks.push(Number(t.toFixed(6)));
        }
        return { gMin, gMax, step, ticks };
      }

      function buildMonotonePath(pts) {
        const n = pts.length;
        if (n === 0) return '';
        if (n === 1) return `M ${pts[0].x.toFixed(2)} ${pts[0].y.toFixed(2)}`;
        if (n === 2) return `M ${pts[0].x.toFixed(2)} ${pts[0].y.toFixed(2)} L ${pts[1].x.toFixed(2)} ${pts[1].y.toFixed(2)}`;
        const h = new Array(n - 1);
        const m = new Array(n - 1);
        for (let i = 0; i < n - 1; i++) {
          h[i] = Math.max(1e-6, pts[i + 1].x - pts[i].x);
          m[i] = (pts[i + 1].y - pts[i].y) / h[i];
        }
        const d = new Array(n).fill(0);
        for (let i = 1; i < n - 1; i++) {
          if (m[i - 1] * m[i] > 0) {
            const w1 = 2 * h[i] + h[i - 1];
            const w2 = h[i] + 2 * h[i - 1];
            d[i] = (w1 + w2) / (w1 / m[i - 1] + w2 / m[i]);
          }
        }
        d[0] = ((2 * h[0] + h[1]) * m[0] - h[0] * m[1]) / (h[0] + h[1]);
        if (d[0] * m[0] <= 0) d[0] = 0;
        else if (Math.abs(d[0]) > 3 * Math.abs(m[0])) d[0] = 3 * m[0];

        const last = n - 1;
        d[last] = ((2 * h[last - 1] + h[last - 2]) * m[last - 1] - h[last - 1] * m[last - 2]) / (h[last - 1] + h[last - 2]);
        if (d[last] * m[last - 1] <= 0) d[last] = 0;
        else if (Math.abs(d[last]) > 3 * Math.abs(m[last - 1])) d[last] = 3 * m[last - 1];

        for (let i = 0; i < n - 1; i++) {
          if (m[i] === 0) {
            d[i] = 0;
            d[i + 1] = 0;
            continue;
          }
          const alpha = d[i] / m[i];
          const beta = d[i + 1] / m[i];
          const mag = Math.hypot(alpha, beta);
          if (mag > 3) {
            const tau = 3 / mag;
            d[i] = tau * alpha * m[i];
            d[i + 1] = tau * beta * m[i];
          }
        }

        let path = `M ${pts[0].x.toFixed(2)} ${pts[0].y.toFixed(2)}`;
        for (let i = 0; i < n - 1; i++) {
          const dx = h[i] / 3;
          const cp1x = pts[i].x + dx;
          const cp1y = pts[i].y + d[i] * dx;
          const cp2x = pts[i + 1].x - dx;
          const cp2y = pts[i + 1].y - d[i + 1] * dx;
          path += ` C ${cp1x.toFixed(2)} ${cp1y.toFixed(2)}, ${cp2x.toFixed(2)} ${cp2y.toFixed(2)}, ${pts[i + 1].x.toFixed(2)} ${pts[i + 1].y.toFixed(2)}`;
        }
        return path;
      }

      function buildCatmullPath(pts) {
        const n = pts.length;
        if (n < 2) return '';
        let path = `M ${pts[0].x.toFixed(2)} ${pts[0].y.toFixed(2)}`;
        for (let i = 0; i < n - 1; i++) {
          const p0 = pts[Math.max(0, i - 1)];
          const p1 = pts[i];
          const p2 = pts[i + 1];
          const p3 = pts[Math.min(n - 1, i + 2)];
          const cp1x = p1.x + (p2.x - p0.x) / 6;
          const cp1y = p1.y + (p2.y - p0.y) / 6;
          const cp2x = p2.x - (p3.x - p1.x) / 6;
          const cp2y = p2.y - (p3.y - p1.y) / 6;
          path += ` C ${cp1x.toFixed(2)} ${cp1y.toFixed(2)}, ${cp2x.toFixed(2)} ${cp2y.toFixed(2)}, ${p2.x.toFixed(2)} ${p2.y.toFixed(2)}`;
        }
        return path;
      }

      function buildLinearPath(pts) {
        return pts.map((p, i) => `${i === 0 ? 'M' : 'L'} ${p.x.toFixed(2)} ${p.y.toFixed(2)}`).join(' ');
      }

      function buildStepPath(pts) {
        let d = `M ${pts[0].x.toFixed(2)} ${pts[0].y.toFixed(2)}`;
        for (let i = 1; i < pts.length; i++) {
          d += ` H ${pts[i].x.toFixed(2)} V ${pts[i].y.toFixed(2)}`;
        }
        return d;
      }

      let activeIdx = 8;
      let cachedXCoords = [];
      let cachedLen = 12;

      function renderChart(showCrosshair = true) {
        const dsKey = presetSelect.value || 'saas-arr';
        const ds = DATASETS[dsKey] || DATASETS['saas-arr'];
        const curveMode = curveSelect.value || 'monotone';
        const sw = parseFloat(strokeSlider.value) || 2.5;
        strokeVal.textContent = sw.toFixed(1) + 'px';
        const markerMode = markerSelect.value || 'markers-area';
        const scope = seriesSelect.value || 'all';

        let activeSeries = ds.series;
        if (scope === 'top2') activeSeries = ds.series.slice(0, 2);
        else if (scope === 'primary') activeSeries = ds.series.slice(0, 1);

        cachedLen = ds.labels.length;
        if (activeIdx >= cachedLen) activeIdx = cachedLen - 1;
        if (activeIdx < 0) activeIdx = 0;

        let rawMin = ds.zeroAnchor ? 0 : Infinity;
        let rawMax = -Infinity;
        activeSeries.forEach(s => {
          s.values.forEach(v => {
            if (v < rawMin) rawMin = v;
            if (v > rawMax) rawMax = v;
          });
        });

        const { gMin, gMax, ticks } = computeNiceScale(rawMin, rawMax * 1.05, 6);

        const viewW = 760;
        const viewH = 440;
        const padLeft = 66;
        const padRight = 28;
        const padTop = 36;
        const padBottom = 56;
        const plotW = viewW - padLeft - padRight;
        const plotH = viewH - padTop - padBottom;

        const scaleX = (idx) => padLeft + (idx / Math.max(1, cachedLen - 1)) * plotW;
        const scaleY = (v) => padTop + ((gMax - v) / Math.max(1e-6, gMax - gMin)) * plotH;

        cachedXCoords = ds.labels.map((_, i) => scaleX(i));

        let gridSvg = '';
        ticks.forEach(t => {
          const gy = scaleY(t);
          const isZero = Math.abs(t) < 1e-6;
          gridSvg += `
            <line x1="${padLeft}" y1="${gy.toFixed(1)}" x2="${viewW - padRight}" y2="${gy.toFixed(1)}"
                  stroke="${isZero ? '#444444' : '#1E1E1E'}" stroke-width="${isZero ? '1.5' : '1'}" shape-rendering="crispEdges" />
            <text x="${padLeft - 10}" y="${(gy + 4).toFixed(1)}" fill="#888888"
                  font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="end">${ds.unitPre}${t}${ds.unitSuf}</text>
          `;
        });

        let xAxisSvg = '';
        ds.labels.forEach((lbl, i) => {
          const gx = cachedXCoords[i];
          xAxisSvg += `
            <line x1="${gx.toFixed(1)}" y1="${padTop}" x2="${gx.toFixed(1)}" y2="${viewH - padBottom}"
                  stroke="#161616" stroke-width="1" />
            <text x="${gx.toFixed(1)}" y="${viewH - padBottom + 22}" fill="${i === activeIdx && showCrosshair ? '#C1DD2D' : '#888888'}"
                  font-family="'JetBrains Mono', monospace" font-size="11" font-weight="${i === activeIdx && showCrosshair ? '700' : '400'}"
                  text-anchor="middle">${lbl}</text>
          `;
        });

        let defsSvg = '<defs>';
        let areasSvg = '';
        let linesSvg = '';
        let markersSvg = '';
        let legendSvg = '';

        activeSeries.forEach((s, sIdx) => {
          const pts = s.values.map((v, i) => ({ x: cachedXCoords[i], y: scaleY(v), v }));
          let pathD = '';
          if (curveMode === 'monotone') pathD = buildMonotonePath(pts);
          else if (curveMode === 'catmull') pathD = buildCatmullPath(pts);
          else if (curveMode === 'step') pathD = buildStepPath(pts);
          else pathD = buildLinearPath(pts);

          const gradId = `lc-area-grad-${sIdx}`;
          defsSvg += `
            <linearGradient id="${gradId}" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="${s.color}" stop-opacity="${sIdx === 0 ? '0.22' : '0.09'}" />
              <stop offset="100%" stop-color="${s.color}" stop-opacity="0" />
            </linearGradient>
          `;

          if (markerMode === 'markers-area') {
            const baseY = scaleY(gMin);
            const areaD = `${pathD} L ${pts[pts.length - 1].x.toFixed(2)} ${baseY.toFixed(2)} L ${pts[0].x.toFixed(2)} ${baseY.toFixed(2)} Z`;
            areasSvg += `<path d="${areaD}" fill="url(#${gradId})" pointer-events="none" />`;
          }

          linesSvg += `
            <path d="${pathD}" fill="none" stroke="${s.color}" stroke-width="${sw}"
                  stroke-linecap="round" stroke-linejoin="round"
                  ${s.dash ? `stroke-dasharray="${s.dash}"` : ''}
                  vector-effect="non-scaling-stroke" />
          `;

          if (markerMode !== 'lines-only') {
            pts.forEach((p, idx) => {
              const isAct = showCrosshair && idx === activeIdx;
              markersSvg += `
                <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="${isAct ? '5.5' : '3.2'}"
                        fill="${isAct ? s.color : '#0D0D0D'}" stroke="${s.color}" stroke-width="${isAct ? '2.5' : '2'}"
                        pointer-events="none" />
              `;
            });
          } else if (showCrosshair) {
            const p = pts[activeIdx];
            markersSvg += `
              <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="5"
                      fill="${s.color}" stroke="#0D0D0D" stroke-width="2" pointer-events="none" />
            `;
          }

          const legX = padLeft + sIdx * 165;
          legendSvg += `
            <g transform="translate(${legX}, 14)">
              <line x1="0" y1="5" x2="18" y2="5" stroke="${s.color}" stroke-width="2.5" ${s.dash ? `stroke-dasharray="${s.dash}"` : ''} />
              <text x="24" y="9" fill="#D4D4D4" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600">${s.name}</text>
            </g>
          `;
        });
        defsSvg += '</defs>';

        let crosshairSvg = '';
        if (showCrosshair) {
          const cx = cachedXCoords[activeIdx];
          crosshairSvg = `
            <line x1="${cx.toFixed(1)}" y1="${padTop}" x2="${cx.toFixed(1)}" y2="${viewH - padBottom}"
                  stroke="#C1DD2D" stroke-width="1.2" stroke-dasharray="4,3" stroke-opacity="0.75" pointer-events="none" />
          `;
        }

        liveSvg.innerHTML = `
          <rect width="${viewW}" height="${viewH}" fill="#0D0D0D" rx="8" />
          ${defsSvg}
          <g class="lc-grid">${gridSvg}${xAxisSvg}</g>
          <g class="lc-areas">${areasSvg}</g>
          <g class="lc-crosshair">${crosshairSvg}</g>
          <g class="lc-lines">${linesSvg}</g>
          <g class="lc-markers">${markersSvg}</g>
          <g class="lc-legend">${legendSvg}</g>
        `;

        liveSvg.setAttribute('aria-valuemax', String(cachedLen - 1));
        liveSvg.setAttribute('aria-valuenow', String(activeIdx));
        liveSvg.setAttribute('aria-valuetext', `${ds.labels[activeIdx]}: ${activeSeries.map(s => `${s.name} ${ds.unitPre}${s.values[activeIdx]}${ds.unitSuf}`).join(', ')}`);

        statLabel.textContent = ds.labels[activeIdx];
        const s1 = ds.series[0];
        const s2 = ds.series[1];
        const s3 = ds.series[2];

        statS1Name.textContent = s1.name;
        statS1Val.textContent = `${ds.unitPre}${s1.values[activeIdx]}${ds.unitSuf}`;

        statS2Name.textContent = s2.name;
        statS2Val.textContent = scope === 'primary' ? 'Hidden' : `${ds.unitPre}${s2.values[activeIdx]}${ds.unitSuf}`;

        statS3Name.textContent = s3.name;
        statS3Val.textContent = scope === 'all' ? `${ds.unitPre}${s3.values[activeIdx]}${ds.unitSuf}` : 'Hidden';

        statDomain.textContent = `[${ds.unitPre}${gMin}${ds.unitSuf}, ${ds.unitPre}${gMax}${ds.unitSuf}]`;
      }

      function updateFromClientX(clientX) {
        if (!cachedXCoords.length) return;
        const rect = liveSvg.getBoundingClientRect();
        if (!rect || !rect.width) return;
        const svgX = ((clientX - rect.left) / rect.width) * 760;
        let lo = 0;
        let hi = cachedXCoords.length - 1;
        if (svgX <= cachedXCoords[0]) activeIdx = 0;
        else if (svgX >= cachedXCoords[hi]) activeIdx = hi;
        else {
          while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (cachedXCoords[mid] === svgX) { lo = mid; hi = mid; break; }
            if (cachedXCoords[mid] < svgX) lo = mid + 1;
            else hi = mid - 1;
          }
          activeIdx = (svgX - cachedXCoords[hi]) <= (cachedXCoords[lo] - svgX) ? hi : lo;
        }
        renderChart(true);
      }

      let isDragging = false;
      liveSvg.addEventListener('pointerdown', e => {
        isDragging = true;
        try { liveSvg.setPointerCapture(e.pointerId); } catch (_) {}
        updateFromClientX(e.clientX);
      });
      liveSvg.addEventListener('pointermove', e => {
        updateFromClientX(e.clientX);
      });
      const endPointer = e => {
        if (isDragging) {
          try { liveSvg.releasePointerCapture(e.pointerId); } catch (_) {}
          isDragging = false;
        }
      };
      liveSvg.addEventListener('pointerup', endPointer);
      liveSvg.addEventListener('pointercancel', endPointer);

      liveSvg.addEventListener('keydown', e => {
        if (e.key === 'ArrowLeft') {
          e.preventDefault();
          activeIdx = Math.max(0, activeIdx - 1);
          renderChart(true);
        } else if (e.key === 'ArrowRight') {
          e.preventDefault();
          activeIdx = Math.min(cachedLen - 1, activeIdx + 1);
          renderChart(true);
        } else if (e.key === 'Home') {
          e.preventDefault();
          activeIdx = 0;
          renderChart(true);
        } else if (e.key === 'End') {
          e.preventDefault();
          activeIdx = cachedLen - 1;
          renderChart(true);
        }
      });

      presetSelect.addEventListener('change', () => renderChart(true));
      curveSelect.addEventListener('change', () => renderChart(true));
      strokeSlider.addEventListener('input', () => renderChart(true));
      markerSelect.addEventListener('change', () => renderChart(true));
      seriesSelect.addEventListener('change', () => renderChart(true));

      copyBtn.addEventListener('click', () => {
        renderChart(false);
        let svgSource = liveSvg.outerHTML || '';
        if (!svgSource.includes('xmlns="http://www.w3.org/2000/svg"')) {
          svgSource = svgSource.replace(/<svg\b/, '<svg xmlns="http://www.w3.org/2000/svg"');
        }
        renderChart(true);

        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(svgSource).then(() => {
            copyBtn.textContent = 'Copied to Clipboard!';
            setTimeout(() => {
              copyBtn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> <span>Copy Standalone SVG</span>';
            }, 2000);
          }).catch(fallbackCopy);
        } else {
          fallbackCopy();
        }

        function fallbackCopy() {
          const ta = document.createElement('textarea');
          ta.value = svgSource;
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.select();
          try {
            document.execCommand('copy');
            copyBtn.textContent = 'Copied to Clipboard!';
            setTimeout(() => {
              copyBtn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> <span>Copy Standalone SVG</span>';
            }, 2000);
          } catch (e) {
            alert('Copy failed: ' + e.message);
          }
          document.body.removeChild(ta);
        }
      });

      renderChart(true);
    })();
  </script>
</body>
</html>
"""

out_dir = os.path.join("articles", "svg-line-charts-and-multi-series-time-series-guide")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Generated:", out_path)
