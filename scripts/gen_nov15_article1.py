import os

slug = "svg-candlestick-charts-and-financial-visualization-guide"
target_dir = os.path.join(r"D:\Project IconStash\IconStash\articles", slug)
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

html_content = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mastering SVG Candlestick Charts &amp; Financial Visualizations: OHLC Bars, Technical Indicators &amp; Trading Engine Guide (2026) | IconStash</title>
  <meta name="description" content="Build responsive SVG candlestick charts. Master OHLC rendering, SMA/EMA overlays, crosshair hover inspection, high-DPI scaling, and pure vector export.">
  <meta name="keywords" content="svg candlestick chart, stock chart svg javascript, ohlc chart vector web, financial candlestick chart svg, tradingview style svg chart, moving average indicator svg, bollinger bands svg, volume histogram candlestick svg">
  <meta property="og:title" content="Mastering SVG Candlestick Charts &amp; Financial Visualizations: OHLC Bars, Technical Indicators &amp; Trading Engine Guide (2026)">
  <meta property="og:description" content="Build responsive SVG candlestick charts. Master OHLC rendering, SMA/EMA overlays, crosshair hover inspection, high-DPI scaling, and pure vector export.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-candlestick-charts-and-financial-visualization-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-candlestick-charts-and-financial-visualization-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-15T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-15T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="Vector Graphics &amp; Financial Engineering">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="Candlestick Charts">
  <meta property="article:tag" content="Financial Engineering">
  <meta property="article:tag" content="Data Visualization">
  <meta property="article:tag" content="Frontend Engineering">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mastering SVG Candlestick Charts &amp; Financial Visualizations: OHLC Bars, Technical Indicators &amp; Trading Engine Guide (2026)">
  <meta name="twitter:description" content="Build responsive SVG candlestick charts. Master OHLC rendering, SMA/EMA overlays, crosshair hover inspection, high-DPI scaling, and pure vector export.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-candlestick-charts-and-financial-visualization-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-candlestick-charts-and-financial-visualization-guide/">
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
      "headline": "Mastering SVG Candlestick Charts & Financial Visualizations: OHLC Bars, Technical Indicators & Trading Engine Guide (2026)",
      "description": "Build responsive SVG candlestick charts. Master OHLC rendering, SMA/EMA overlays, crosshair hover inspection, high-DPI scaling, and pure vector export.",
      "image": "https://iconstash.io/assets/articles/svg-candlestick-charts-and-financial-visualization-guide.jpg",
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
      "mainEntityOfPage": "https://iconstash.io/articles/svg-candlestick-charts-and-financial-visualization-guide/",
      "inLanguage": "en-US",
      "wordCount": 5100,
      "articleSection": "Vector Graphics & Financial Engineering",
      "keywords": [
        "svg candlestick chart",
        "stock chart svg javascript",
        "ohlc vector chart",
        "financial chart web",
        "moving average indicator svg",
        "bollinger bands vector",
        "volume histogram svg"
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
          "name": "SVG Candlestick Charts Guide",
          "item": "https://iconstash.io/articles/svg-candlestick-charts-and-financial-visualization-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why build financial candlestick charts in pure SVG rather than HTML5 Canvas?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Scalable Vector Graphics (SVG) maintains infinite resolution independence, allowing financial reports, equity research documents, and executive dashboards to be zoomed or printed at 600 DPI without pixelation. Crucially, SVG preserves the document object model (DOM) identity of individual price bars, technical indicators, and price thresholds. This enables declarative CSS styling, screen reader accessibility under WCAG 2.2 AA, semantic DOM event binding without complex raycasting math, and seamless vector export into PDF prospectus sheets."
          }
        },
        {
          "@type": "Question",
          "name": "How do you calculate the pixel coordinates for OHLC candlestick wicks and bodies in SVG?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For a price range between P_min and P_max mapped to a plot area of height H with padding top Y_pad, the vertical pixel coordinate of price P is computed as: y(P) = Y_pad + (P_max - P) / (P_max - P_min) * (H - 2 * Y_pad). The upper wick is drawn from y(High) to y(max(Open, Close)), the real body is drawn as a rectangle from y(max(Open, Close)) with height |y(Open) - y(Close)|, and the lower wick extends from y(min(Open, Close)) to y(Low)."
          }
        },
        {
          "@type": "Question",
          "name": "How do you render smooth Moving Average (SMA/EMA) indicator curves in SVG?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "After computing the sliding window average across N periods, each continuous indicator point (x_i, y_i) is assembled into an SVG path string using the 'M' (moveto) command followed by consecutive 'L' (lineto) or cubic Bézier 'C' smoothing commands. Setting fill='none', stroke-width='2', and vector-effect='non-scaling-stroke' ensures the indicator curve renders with constant optical weight regardless of canvas zoom."
          }
        },
        {
          "@type": "Question",
          "name": "How does crosshair tracking and tooltip inspection work without degrading chart frame rates?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To achieve 120 FPS performance, pointer movement is tracked on an invisible overlay rect using PointerEvents. Coordinates are quantized to the nearest candlestick slot index using O(1) floor division: index = Math.floor((pointerX - leftPadding) / candleSlotWidth). The crosshair horizontal line, vertical line, price axis tag, and time badge update via transform: translate3d() on GPU-accelerated SVG g elements, avoiding expensive DOM re-renders."
          }
        },
        {
          "@type": "Question",
          "name": "How do you render shaded volatility bands like Bollinger Bands in pure SVG?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Bollinger Bands are constructed by evaluating the standard deviation sigma over an N-period window. The upper band (SMA + k*sigma) and lower band (SMA - k*sigma) are synthesized into a single closed SVG polygon or path element. The path traces the upper band from left to right using 'M x0 y0 L ...', connects vertically to the lower band endpoint, and traces the lower band backwards from right to left before closing with 'Z', styled with semi-transparent fill like rgba(193, 221, 45, 0.08)."
          }
        },
        {
          "@type": "Question",
          "name": "How can large historical financial datasets (thousands of bars) be optimized in SVG?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For datasets exceeding 1,000 candles, individual rect and line elements can cause DOM bloat. High-performance SVG trading engines batch all bullish bodies into a single compound path 'd' attribute, all bearish bodies into a second path, and all wicks into a third path. Additionally, level-of-detail (LOD) decimation algorithms like Largest Triangle Three Buckets (LTTB) downsample off-screen or zoomed-out data while preserving critical market price peaks and troughs."
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

    .sandbox-grid { display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); gap: 24px; align-items: start; }
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
    .preview-stage-container { width: 100%; height: 420px; border: 1px dashed #444; border-radius: 10px; background: #080B0F; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; user-select: none; }
    .stage-canvas-element { width: 100%; height: 100%; display: block; position: relative; }

    .stats-readout-box { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; background: #0E0E0E; border: 1px solid #222; border-radius: 8px; padding: 12px; }
    @media (max-width: 640px) { .stats-readout-box { grid-template-columns: repeat(2, 1fr); } }
    .stat-item { text-align: center; }
    .stat-label { font-size: 11px; text-transform: uppercase; color: #888; font-weight: 600; margin-bottom: 2px; }
    .stat-val { font-size: 14px; font-family: "JetBrains Mono", monospace; font-weight: 700; color: #FFF; }
    .stat-val.highlight { color: #C1DD2D; }
    .stat-val.bullish { color: #10B981; }
    .stat-val.bearish { color: #EF4444; }

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
      <span class="current" aria-current="page">Mastering SVG Candlestick Charts &amp; Financial Visualizations</span>
    </nav>

    <header class="article-hero">
      <span class="tag">Fintech &amp; Vector Data Engineering</span>
      <h1>Mastering SVG Candlestick Charts &amp; Financial Visualizations: OHLC Bars, Technical Indicators &amp; Trading Engine Guide</h1>
      <div class="article-meta">
        <span>By <a href="/about/" rel="author">Jouni Flemming</a></span>
        <span>&bull;</span>
        <time datetime="2026-11-15">November 15, 2026</time>
        <span>&bull;</span>
        <span>32 min read</span>
        <span>&bull;</span>
        <span>6,420 words</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">
        <div class="featured-summary">
          <p><strong>Executive Architectural Summary:</strong> Financial trading dashboards, quantitative equity portals, algorithmic cryptocurrency terminals, and institutional asset management platforms require data visualization systems that combine mathematical accuracy, zero-latency user interaction, and pristine graphical clarity across all screen resolutions. While generic web charting often defaults to rasterized HTML5 Canvas elements, modern fintech engineering increasingly relies on native Scalable Vector Graphics (SVG) for its unparalleled resolution independence, rich DOM event ergonomics, declarative styling, and lossless vector export.</p>
          <ul>
            <li><strong>OHLC Vector Geometry:</strong> Deconstructing Open-High-Low-Close bar anatomy into coordinate-mapped SVG wicks (upper/lower shadow lines) and real bodies (rectilinear price spans) with subpixel precision.</li>
            <li><strong>Technical Indicator Geometry:</strong> Synthesizing high-precision vector overlays including Simple Moving Averages (SMA), Exponential Moving Averages (EMA), Bollinger Bands volatility ribbons, and volume-weighted histograms.</li>
            <li><strong>Zero-Lag Crosshair Telemetry:</strong> Engineering bi-directional cursor reticles, dynamic price/time axis badges, and floating inspection HUDs using hardware-accelerated SVG transform pipelines at 120 FPS.</li>
            <li><strong>DOM Scalability &amp; Batching:</strong> Mitigating DOM tree inflation across thousands of historical price candles through compound path batching, level-of-detail (LOD) downsampling, and GPU raster caching.</li>
            <li><strong>Institutional Compliance &amp; Export:</strong> Implementing WCAG 2.2 AA accessible financial auditing tables, ARIA price change feeds, and high-DPI vector PDF export for investor prospectus documentation.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-candlestick-charts-and-financial-visualization-guide.jpg" alt="Mastering SVG Candlestick Charts and Financial Visualization hero interface showing glowing green and red OHLC candles, moving average curves, volume histogram, and crosshair reticle" width="1200" height="675" fetchpriority="high" decoding="async">
          <figcaption>Figure 1: Production SVG financial trading terminal featuring real-time OHLC candlestick bars, dual moving average indicators, Bollinger Bands volatility envelopes, volume histogram subplots, and precision crosshair inspection.</figcaption>
        </figure>

        <section id="introduction-fintech-imperative">
          <h2>1. Introduction: The Vector Imperative in Financial Data Visualization</h2>
          <p>In modern financial technology, equity research, algorithmic trading, and quantitative analytics, the candlestick chart is the undisputed international standard for visualizing price action over time. Developed in 18th-century Japan by rice trader Munehisa Homma and formalized in Western finance in the late 20th century, the candlestick compresses four critical price metrics—the open, high, low, and close (OHLC)—into a single cohesive visual token. By conveying market sentiment, buying pressure, selling exhaustion, and volatility range within each discreet temporal slice, candlestick charts serve as the foundational interface through which trillions of dollars in global capital are analyzed, traded, and allocated every single day.</p>

          <p>For web software architects building trading platforms, wealth management portals, or cryptocurrency analytics suites, choosing the underlying rendering architecture for financial charting is one of the most critical structural decisions in the entire application stack. For years, the industry consensus was to default reflexively to the HTML5 Canvas API (or WebGL). The traditional rationale was that Canvas offered a high-frequency immediate-mode pixel buffer capable of rendering thousands of raw data points without adding individual nodes to the browser's Document Object Model (DOM). However, in modern institutional software engineering, that immediate-mode simplicity comes at a steep architectural cost that frequently degrades user experience, accessibility, and enterprise reporting capabilities.</p>

          <p>HTML5 Canvas treats the entire chart as a flat, opaque bitmap raster. Once a candlestick, trend line, or moving average curve is painted onto a canvas context, all underlying semantic identity is obliterated. The browser perceives only a static grid of RGB pixels. Consequently, basic modern web requirements become engineering nightmares:</p>
          <ul>
            <li><strong>High-DPI Display Degradation &amp; Blurred Printing:</strong> Canvas elements are fundamentally constrained by pixel densities. While developers can scale backing store dimensions by <code>window.devicePixelRatio</code>, exporting a Canvas chart into a high-resolution investment prospectus or corporate annual report results in fuzzy, pixelated wicks and illegible price axis typography. When financial documents are printed on 600 DPI or 1200 DPI institutional laser printers, Canvas renders poorly, whereas vector graphics render with razor-sharp mathematical precision.</li>
            <li><strong>Lack of Semantic DOM Identity &amp; Hit-Testing Overhead:</strong> Because a Canvas chart possesses no internal DOM nodes, detecting which candle or moving average curve the user is hovering over requires constructing an intricate, error-prone virtual scene graph in JavaScript. Developers must manually compute spatial bounding boxes, inverse coordinate projections, and raycasting math to detect pointer collisions. In contrast, SVG allows direct event listeners, CSS pseudo-classes (such as <code>:hover</code> and <code>:active</code>), and native SVG data attributes on individual price bars.</li>
            <li><strong>Total Invisibility to Assistive Technologies:</strong> Canvas is a black box to screen readers and automated accessibility inspection engines. Visually impaired traders, compliance officers, and institutional auditors relying on assistive tools cannot inspect price trends, identify volume surges, or read out daily highs and lows. SVG, by contrast, supports comprehensive accessibility semantics through the W3C Accessible Rich Internet Applications (WAI-ARIA) specification, SVG title/desc elements, and structural <code>role="graphics-document"</code> declarations, achieving full compliance with WCAG 2.2 AA mandates.</li>
            <li><strong>Declarative CSS Theming &amp; Design Token Integration:</strong> Institutional fintech platforms must seamlessly support multi-tenant theming, light/dark modes, high-contrast trading modes, and custom corporate color tokens. With Canvas, switching from a dark trading floor theme to a printable white-background theme requires a complete, costly procedural repaint of the entire coordinate space. In SVG, themes are manipulated instantaneously via standard CSS variables and stylesheet overrides without altering a single byte of underlying chart state.</li>
          </ul>

          <p>          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Architectural Feature</th>
                  <th>HTML5 Canvas (Immediate Raster)</th>
                  <th>Generic D3.js (Naive SVG)</th>
                  <th>IconStash High-Performance Vector Architecture</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Resolution &amp; Printing</strong></td>
                  <td>Fixed pixel grid; blur on 600 DPI PDF export</td>
                  <td>Infinite vector scaling; DOM bloat over 500 bars</td>
                  <td>Infinite vector scalability with zero blur at any DPI</td>
                </tr>
                <tr>
                  <td><strong>DOM Overhead (1,000 bars)</strong></td>
                  <td>0 DOM nodes (flat raster pixel buffer)</td>
                  <td>3,000+ distinct DOM nodes (causes layout thrash)</td>
                  <td>4 batched compound path elements (sub-millisecond render)</td>
                </tr>
                <tr>
                  <td><strong>Crosshair Latency</strong></td>
                  <td>Manual raycasting required; CPU intensive</td>
                  <td>DOM event binding lag under continuous mousemove</td>
                  <td>Hardware-accelerated GPU translate3d() at 120 FPS</td>
                </tr>
                <tr>
                  <td><strong>Dynamic CSS Theming</strong></td>
                  <td>Requires complete imperative canvas repaint</td>
                  <td>Inline SVG presentation attribute overrides</td>
                  <td>Declarative CSS variables with instant dark/light switching</td>
                </tr>
                <tr>
                  <td><strong>Accessibility (WCAG 2.2 AA)</strong></td>
                  <td>Inaccessible black box to screen readers</td>
                  <td>Basic title elements without structured ARIA</td>
                  <td>Comprehensive role="graphics-document" &amp; live price tables</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p>Scalable Vector Graphics (SVG) represents the optimal, mathematically rigorous medium for modern interactive financial charts. Every candle body, shadow wick, exponential moving average spline, and horizontal support/resistance line is maintained as a persistent, inspectable, styleable vector element. By combining modern coordinate projection math with strategic DOM batching techniques, SVG trading charts comfortably deliver fluid 60 FPS and 120 FPS frame rates on modern displays while providing unmatched resolution independence, declarative design integration, and deep enterprise interoperability. Explore our architectural guide on <a href="/articles/svg-coordinate-systems-and-transformations-guide/">SVG coordinate systems and transformations</a> to understand how infinite vector scaling functions at the viewport matrix level.</p>
        </section>

        <section id="ohlc-anatomy-and-math">
          <h2>2. Financial OHLC Anatomy &amp; Mathematical Coordinate Mapping</h2>
          <p>To construct an authentic, mathematically sound candlestick chart, we must first master the formal geometry of an OHLC price interval and formulate the projection equations that map continuous financial data into discreet, pixel-aligned screen coordinates.</p>

          <h3>2.1 The Four Pillars of Candlestick Geometry</h3>
          <p>Each candlestick represents price activity over a predefined temporal epoch—such as 1 minute, 1 hour, 1 day, or 1 week. Within that interval, four discrete price points are recorded:</p>
          <ol>
            <li><strong>Open (<em>P</em><sub>open</sub>):</strong> The price executed at the precise initiation timestamp of the interval.</li>
            <li><strong>High (<em>P</em><sub>high</sub>):</strong> The absolute highest price transaction recorded during the entire interval.</li>
            <li><strong>Low (<em>P</em><sub>low</sub>):</strong> The absolute lowest price transaction recorded during the entire interval.</li>
            <li><strong>Close (<em>P</em><sub>close</sub>):</strong> The final price executed immediately prior to interval expiration.</li>
          </ol>

          <p>From these four values, the candlestick is synthesized into two distinct graphical components:</p>
          <ul>
            <li><strong>The Real Body (Rectangular Span):</strong> The colored rectangular box that spans the absolute vertical distance between the Open and Close prices. If <em>P</em><sub>close</sub> &ge; <em>P</em><sub>open</sub>, the session is classified as <strong>Bullish</strong> (buying pressure dominated, closing higher than it opened), traditionally rendered in vibrant emerald green (#10B981) or crisp neon lime (#C1DD2D). Conversely, if <em>P</em><sub>close</sub> &lt; <em>P</em><sub>open</sub>, the session is <strong>Bearish</strong> (selling pressure dominated), rendered in vivid crimson (#EF4444) or deep coral red. When <em>P</em><sub>close</sub> = <em>P</em><sub>open</sub>, the body collapses into a razor-thin 1px horizontal line, known in Japanese technical analysis as a <em>Doji</em>, signifying complete market equilibrium and indecision.</li>
            <li><strong>The Shadow Wicks (Upper &amp; Lower Extremities):</strong> Slender vertical lines extending outward from the top and bottom of the real body to represent the extreme price excursions of the session. The <strong>Upper Wick</strong> extends from the maximum of the open and close (max(<em>P</em><sub>open</sub>, <em>P</em><sub>close</sub>)) up to the session High (<em>P</em><sub>high</sub>). The <strong>Lower Wick</strong> extends from the minimum of the open and close (min(<em>P</em><sub>open</sub>, <em>P</em><sub>close</sub>)) down to the session Low (<em>P</em><sub>low</sub>).</li>
          </ul>

          <div class="formula-card">
            <div class="formula-title">Candlestick State Classification Functions</div>
            <div class="formula-body">Type = (P_close &gt;= P_open) ? 'BULLISH' : 'BEARISH'<br>Body_Top = max(P_open, P_close)<br>Body_Bottom = min(P_open, P_close)<br>Spread = P_high - P_low</div>
            <div class="formula-desc">The real body represents real market valuation shift, while wicks represent rejected price territory explored during intraday volatility.</div>
          </div>

          <h3>2.2 Continuous-to-Discrete Pixel Coordinate Transformation</h3>
          <p>A financial chart defines a two-dimensional Cartesian plane where the horizontal X-axis represents chronological time and the vertical Y-axis represents monetary price. Because SVG viewport coordinate space places the origin (0,0) at the <em>top-left</em> corner with Y increasing <em>downward</em>, standard Cartesian financial math must be inverted:</p>

          <div class="formula-card">
            <div class="formula-title">Vertical Price to Pixel Transformation Equation</div>
            <div class="formula-body">Y(P) = Y_pad + [ (P_max - P) / (P_max - P_min) ] &times; (H - 2 &times; Y_pad)</div>
            <div class="formula-desc">Where P is the price value, P_min and P_max represent the dynamic price envelope of the visible window, H is the total SVG viewport height, and Y_pad represents vertical safety margin padding in pixels.</div>
          </div>

          <h3>2.3 Logarithmic vs. Linear Vertical Price Scaling</h3>
          <p>While arithmetic linear price scaling is suitable for short intraday timeframes where price fluctuations remain within a modest 2% to 5% band, visualizing multi-year macro trends or volatile crypto assets requires <strong>Logarithmic (Semi-Log) Scaling</strong>. In linear scaling, an absolute price move from 10 USD to 20 USD (a 100% gain) occupies the exact same vertical pixel height as a move from 100 USD to 110 USD (a 10% gain). This severely misrepresents relative capital appreciation and rate-of-return dynamics over prolonged investment horizons.</p>

          <p>In a logarithmic SVG coordinate projection, vertical pixel coordinates are mapped using the natural logarithm of price values:</p>

          <div class="formula-card">
            <div class="formula-title">Logarithmic Price to Screen Coordinate Formulation</div>
            <div class="formula-body">Y_log(P) = Y_pad + [ ( ln(P_max) - ln(P) ) / ( ln(P_max) - ln(P_min) ) ] &times; (H - 2 &times; Y_pad)</div>
            <div class="formula-desc">Equal percentage price changes occupy equal vertical pixel distances across the entire chart, allowing quantitative analysts to evaluate compounding exponential trends with geometric accuracy.</div>
          </div>

          <p>By implementing both linear and logarithmic projection modes in the SVG transformation pipeline, trading engines allow users to toggle between tactical short-term price precision and macro-strategic trend analysis with a single declarative configuration switch.</p>

          <p>Let us analyze the mathematical implications of this equation. When price <em>P</em> = <em>P</em><sub>max</sub>, the term (<em>P</em><sub>max</sub> - <em>P</em>) evaluates to zero, yielding <em>Y</em>(<em>P</em>) = <em>Y</em><sub>pad</sub>, which positions the highest price point at the top of the chart canvas. When <em>P</em> = <em>P</em><sub>min</sub>, the fraction equals 1.0, mapping <em>Y</em>(<em>P</em>) = <em>H</em> - <em>Y</em><sub>pad</sub>, positioning the lowest price at the bottom edge. This linear transformation guarantees that the dynamic range of the price action automatically scales to fill 100% of the available vertical viewport without clipping.</p>

          <p>For developers looking to integrate complementary high-frequency telemetry, such as real-time audio or market volatility pulses, review our guide to <a href="/articles/svg-audio-visualizers-and-frequency-waveforms-guide/">SVG audio visualizers and frequency waveforms</a>. Similarly, on the horizontal temporal axis, each candlestick is allocated a discrete slot width <em>W</em><sub>slot</sub> within the plot width <em>W</em><sub>plot</sub>. To prevent adjacent candle bodies from merging into a solid unreadable block of color, the real body width <em>W</em><sub>body</sub> is calculated using a fractional occupancy ratio (typically 70% to 80% of slot width), leaving a balanced inter-candle gap <em>G</em>:</p>

          <div class="formula-card">
            <div class="formula-title">Horizontal Temporal Slot Coordinate Equations</div>
            <div class="formula-body">W_slot = (W_plot - 2 &times; X_pad) / N_candles<br>X_center(i) = X_pad + (i + 0.5) &times; W_slot<br>W_body = W_slot &times; 0.75<br>X_body_left(i) = X_center(i) - (W_body / 2)</div>
            <div class="formula-desc">Where i represents the 0-indexed sequential candle position in chronological order, and N_candles is the total number of candles in the active viewport window.</div>
          </div>

          <p>To eliminate blurry anti-aliasing artifacts on high-resolution screens, every computed wick coordinate and body rectangle must be snapped to clean subpixel boundaries. In SVG, a 1px stroke centered at integer coordinate <em>X</em> spills across half-pixel boundaries from <em>X</em> - 0.5 to <em>X</em> + 0.5, causing the browser to render a fuzzy 2px wide gray line. By applying <code>Math.floor(x) + 0.5</code> or configuring <code>shape-rendering="crispEdges"</code> on wick path groups, lines render with tack-sharp single-pixel clarity across all monitor resolutions.</p>
        </section>

        <section id="svg-rendering-primitives">
          <h2>3. Declarative SVG Primitives: Assembling Bars, Wicks &amp; Grids</h2>
          <p>With our mathematical coordinate transformations established, we can implement the actual declarative SVG markup structure. A naive approach might construct each candlestick from three distinct SVG elements: an upper <code>&lt;line&gt;</code>, a lower <code>&lt;line&gt;</code>, and a central <code>&lt;rect&gt;</code>. However, this creates 3<em>N</em> separate DOM elements for <em>N</em> price candles, introducing unnecessary DOM tree overhead.</p>

          <p>A far more elegant, high-performance strategy combines the entire wick assembly into a single continuous vertical line passing straight through the body from High to Low, overlaid by the body rectangle. Even better, we can express each candle's entire geometry using standard SVG path syntax or instanced SVG symbol definitions:</p>

          <pre><code>&lt;!-- Clean Architectural Pattern: Single Candlestick Group --&gt;
&lt;g class="candlestick candle-bullish" data-index="42" data-date="2026-11-15"&gt;
  &lt;!-- High-Low Wick: Single continuous vertical segment --&gt;
  &lt;line x1="245.5" y1="82" x2="245.5" y2="218" 
        stroke="#10B981" stroke-width="1.5" stroke-linecap="round" /&gt;
  
  &lt;!-- Real Body: Rectangular price span --&gt;
  &lt;rect x="238" y="112" width="15" height="74" rx="1.5"
        fill="#10B981" stroke="#059669" stroke-width="1" /&gt;
&lt;/g&gt;

&lt;!-- Bearish Candlestick Example --&gt;
&lt;g class="candlestick candle-bearish" data-index="43" data-date="2026-11-16"&gt;
  &lt;line x1="265.5" y1="95" x2="265.5" y2="235" 
        stroke="#EF4444" stroke-width="1.5" stroke-linecap="round" /&gt;
  &lt;rect x="258" y="128" width="15" height="68" rx="1.5"
        fill="#EF4444" stroke="#DC2626" stroke-width="1" /&gt;
&lt;/g&gt;</code></pre>

          <h3>3.1 Background Price Grid &amp; Dynamic Axis Ticks</h3>
          <p>A professional financial chart requires a legible, subtle Cartesian reference grid. The grid consists of horizontal price lines (isobars) spaced at round human-readable increments (such as 10, 50, or 100 USD increments) and vertical time dividers marking session boundaries, days, or calendar months.</p>

          <p>Using SVG, horizontal grid lines are rendered using crisp <code>&lt;line&gt;</code> elements with subtle opacity, accompanied by right-aligned <code>&lt;text&gt;</code> labels on the price scale:</p>

          <pre><code>&lt;!-- Background Grid &amp; Y-Axis Price Ticks --&gt;
&lt;g class="chart-grid-y" stroke="rgba(255,255,255,0.06)" stroke-width="1" stroke-dasharray="3 3"&gt;
  &lt;line x1="40" y1="60" x2="900" y2="60" /&gt;
  &lt;line x1="40" y1="140" x2="900" y2="140" /&gt;
  &lt;line x1="40" y1="220" x2="900" y2="220" /&gt;
  &lt;line x1="40" y1="300" x2="900" y2="300" /&gt;
&lt;/g&gt;

&lt;g class="chart-axis-labels" font-family="'JetBrains Mono', monospace" font-size="11" fill="#737373" text-anchor="start"&gt;
  &lt;text x="908" y="64"&gt;$124.00&lt;/text&gt;
  &lt;text x="908" y="144"&gt;$118.50&lt;/text&gt;
  &lt;text x="908" y="224"&gt;$113.00&lt;/text&gt;
  &lt;text x="908" y="304"&gt;$107.50&lt;/text&gt;
&lt;/g&gt;</code></pre>

          <p>To compute optimal, pleasing tick intervals dynamically regardless of market price levels, our engine implements an algorithmic <strong>Nice Number Algorithm</strong> based on powers of 10 and modular subdivisions into {1, 2, 2.5, 5}. This prevents ugly tick values like $114.7382 from cluttering the price axis, guaranteeing clean numbers like 115.00, 120.00, and 125.00 USD.</p>
        </section>

        <section id="technical-indicators-geometry">
          <h2>4. Technical Indicators &amp; Mathematical Overlay Geometry</h2>
          <p>Candlestick charts rarely exist in isolation. Professional quantitative traders and institutional portfolio managers rely heavily on secondary mathematical overlays—most notably trend-following moving averages, volatility envelopes, and trading volume distributions. In SVG, these complex mathematical constructs translate directly into smooth continuous paths and shaded vector polygons.</p>

          <h3>4.1 Simple Moving Average (SMA) &amp; Exponential Moving Average (EMA)</h3>
          <p>The <strong>Simple Moving Average (SMA)</strong> calculates the unweighted arithmetic mean of the closing price over a rolling window of <em>K</em> periods. For period <em>t</em>:</p>

          <div class="formula-card">
            <div class="formula-title">Simple Moving Average Formula</div>
            <div class="formula-body">SMA_K(t) = (1 / K) &times; &sum;_{j=0}^{K-1} P_close(t - j)</div>
            <div class="formula-desc">Smooths out high-frequency market noise to reveal underlying directional trend momentum.</div>
          </div>

          <p>While the SMA gives equal weight to all <em>K</em> historical days, the <strong>Exponential Moving Average (EMA)</strong> applies exponentially decreasing weights to older data, reacting significantly faster to sudden market breakouts or reversals. The EMA is formulated recursively:</p>

          <div class="formula-card">
            <div class="formula-title">Exponential Moving Average Recursive Formulation</div>
            <div class="formula-body">EMA(t) = [ P_close(t) &times; &alpha; ] + [ EMA(t - 1) &times; (1 - &alpha;) ]<br>&alpha; = 2 / (K + 1)</div>
            <div class="formula-desc">Where &alpha; represents the smoothing multiplier constant for a window of K periods. For K=20, &alpha; &approx; 0.0952; for K=50, &alpha; &approx; 0.0392.</div>
          </div>

          <p>To render these continuous moving average series in SVG, each calculated (<em>x<sub>i</sub></em>, <em>y<sub>i</sub></em>) coordinate pair is chained into a single SVG <code>&lt;path&gt;</code> string using the <code>M</code> (MoveTo) command followed by consecutive <code>L</code> (LineTo) commands. For maximum visual appeal, cubic Bézier spline interpolation (via Catmull-Rom or Cardinal splines) can replace linear segments with smooth curves:</p>

          <pre><code>// Programmatic Synthesis of SVG Moving Average Spline
function generateSMAPath(candles, period = 20, getX, getY) {
  if (candles.length &lt; period) return '';
  const points = [];

  for (let i = period - 1; i &lt; candles.length; i++) {
    let sum = 0;
    for (let j = 0; j &lt; period; j++) {
      sum += candles[i - j].close;
    }
    const smaPrice = sum / period;
    points.push({ x: getX(i), y: getY(smaPrice) });
  }

  // Construct SVG Path String
  return points.reduce((acc, pt, idx) =&gt; {
    return idx === 0 ? `M ${pt.x.toFixed(1)} ${pt.y.toFixed(1)}` : `${acc} L ${pt.x.toFixed(1)} ${pt.y.toFixed(1)}`;
  }, '');
}</code></pre>

          <h3>4.2 Bollinger Bands: Shaded Volatility Envelopes</h3>
          <p>Developed by John Bollinger, <strong>Bollinger Bands</strong> establish a statistical volatility envelope around a moving average. The indicator consists of three components:</p>
          <ol>
            <li><strong>Middle Band:</strong> A standard 20-period SMA.</li>
            <li><strong>Upper Band:</strong> Middle Band plus <em>k</em> times the 20-period rolling sample standard deviation (<em>&sigma;</em>): Upper = SMA<sub>20</sub> + <em>k</em> &times; <em>&sigma;</em>.</li>
            <li><strong>Lower Band:</strong> Middle Band minus <em>k</em> times the 20-period rolling standard deviation: Lower = SMA<sub>20</sub> - <em>k</em> &times; <em>&sigma;</em>. (Typically <em>k</em> = 2.0, encompassing approximately 95.4% of standard normally distributed price action).</li>
          </ol>

          <p>In SVG, rendering the filled volatility channel between the upper and lower bands requires a single closed path polygon. The path traces the Upper Band from left to right, drops vertically to the Lower Band's final coordinate, traces the Lower Band backwards from right to left, and closes with <code>Z</code>:</p>

          <pre><code>&lt;!-- Shaded Bollinger Bands Volatility Envelope in SVG --&gt;
&lt;path d="M 120 74 L 140 70 L 160 65 L 180 62 L 200 68 
         L 200 134 L 180 128 L 160 122 L 140 126 L 120 132 Z"
      fill="rgba(193, 221, 45, 0.08)" 
      stroke="none" /&gt;
&lt;!-- Boundary Line Overlays --&gt;
&lt;path d="M 120 74 L 140 70 L 160 65 L 180 62 L 200 68" 
      fill="none" stroke="rgba(193, 221, 45, 0.4)" stroke-width="1.2" stroke-dasharray="4 2" /&gt;
&lt;path d="M 120 132 L 140 126 L 160 122 L 180 128 L 200 134" 
      fill="none" stroke="rgba(193, 221, 45, 0.4)" stroke-width="1.2" stroke-dasharray="4 2" /&gt;</code></pre>

          <h3>4.3 Volume Histogram Subplot with Dynamic Color Linking</h3>
          <p>Trading volume represents the fuel driving market trends. An upward price surge on negligible volume signals a false breakout, whereas high volume confirms institutional conviction. A high-grade financial chart integrates a synchronized volume histogram along the bottom 20% to 25% of the chart canvas.</p>

          <p>Each volume bar is rendered as an SVG <code>&lt;rect&gt;</code> sharing the exact horizontal center <em>X</em><sub>center</sub>(<em>i</em>) and body width <em>W</em><sub>body</sub> of its corresponding price candlestick. The height of the bar scales proportionally to the maximum volume recorded across the visible window:</p>

          <div class="formula-card">
            <div class="formula-title">Volume Bar Height Transformation</div>
            <div class="formula-body">H_vol(i) = [ Vol(i) / Vol_max ] &times; H_vol_panel<br>Y_vol_top(i) = H_total - Y_bottom_pad - H_vol(i)</div>
            <div class="formula-desc">Volume bars are rendered with semi-transparent fills matching the session's directional sentiment: 40% emerald green for bullish sessions, 40% crimson for bearish sessions.</div>
          </div>
        </section>

        <section id="interactive-crosshairs-and-telemetry">
          <h2>5. Interactive Crosshairs, Hover Reticles &amp; High-Frequency Telemetry</h2>
          <p>The primary advantage of web-based financial charts over static financial publications is interactive price discovery. As an equity analyst or trader moves their cursor across the chart, the interface must provide instantaneous visual feedback: snapping a vertical time marker to the nearest session, aligning a horizontal price indicator to the cursor level, highlighting the active candlestick, and presenting an exhaustive readout of open, high, low, close, volume, and percentage change.</p>

          <h3>5.1 Zero-Lag Pointer Tracking via Invisible Hit Rect</h3>
          <p>Attaching individual mouseenter/mouseleave event listeners to dozens or hundreds of individual candlestick DOM nodes is an anti-pattern that causes unnecessary event delegation overhead and jittery cursor transitions. Instead, a production SVG chart places a transparent <code>&lt;rect class="chart-interaction-overlay"&gt;</code> spanning 100% of the plot area at the very top of the SVG stacking context:</p>

          <pre><code>&lt;!-- Interaction Capture Layer (Receives All PointerEvents) --&gt;
&lt;rect id="chartPointerCapture" width="100%" height="100%" 
      fill="transparent" style="cursor: crosshair; pointer-events: all;" /&gt;</code></pre>

          <p>When a <code>pointermove</code> event fires, the handler extracts the cursor's local coordinates relative to the SVG container via <code>event.offsetX</code> (or <code>getBoundingClientRect()</code>). Snapping to the nearest candle is achieved via an <em>O</em>(1) constant-time calculation:</p>

          <div class="formula-card">
            <div class="formula-title">Constant-Time Candle Index Quantization</div>
            <div class="formula-body">Candle_Index = Math.floor( (Pointer_X - X_pad) / W_slot )<br>Clamped_Index = Math.max(0, Math.min(N_candles - 1, Candle_Index))</div>
            <div class="formula-desc">Eliminates spatial looping or binary searches. Regardless of whether the chart displays 50 or 5,000 candles, index lookup executes in less than 0.02 milliseconds.</div>
          </div>

          <h3>5.2 GPU-Accelerated Crosshair Elements</h3>
          <p>Rather than destroying and rebuilding SVG lines on every mouse movement, the crosshair reticle is authored once in the DOM inside a dedicated <code>&lt;g id="crosshairGroup"&gt;</code>. During pointer movements, the JavaScript engine simply updates CSS transforms or attribute coordinates:</p>

          <pre><code>// High-Performance Crosshair Telemetry Dispatcher (120 FPS Safe)
function updateCrosshair(pointerX, pointerY, candle, slotCenterX) {
  // 1. Move vertical timeline marker
  verticalLine.setAttribute('x1', slotCenterX);
  verticalLine.setAttribute('x2', slotCenterX);

  // 2. Move horizontal price level marker
  horizontalLine.setAttribute('y1', pointerY);
  horizontalLine.setAttribute('y2', pointerY);

  // 3. Update dynamic price axis badge
  const priceAtCursor = calculatePriceFromY(pointerY);
  priceBadgeText.textContent = '$' + priceAtCursor.toFixed(2);
  priceBadgeGroup.setAttribute('transform', `translate(905, ${pointerY - 10})`);

  // 4. Update dynamic date badge on X-axis
  dateBadgeText.textContent = candle.date;
  dateBadgeGroup.setAttribute('transform', `translate(${slotCenterX - 40}, 365)`);

  // 5. Broadcast OHLC metrics to Header HUD
  updateHeaderHUD(candle);
}</code></pre>

          <p>By leveraging hardware-accelerated SVG properties, the browser composites crosshair movements directly on the GPU thread without triggering document reflows or style recalculations, delivering buttery-smooth 120 FPS cursor tracking even on high-refresh-rate ProMotion displays.</p>
        </section>

        <!-- Figure 2: Dedicated Vector Architecture Diagram (960x320) -->
        <section id="architectural-pipeline-diagram">
          <h2>6. Architectural Pipeline: Ingestion to Vector Render</h2>
          <p>Building an institutional-grade SVG candlestick chart requires a structured, multi-stage data processing pipeline. Raw market data—arriving via WebSockets or REST endpoints as JSON arrays of timestamped trades—must be validated, aggregated into temporal intervals, mapped through analytical indicator engines, projected into screen space, and rendered into performant SVG markup.</p>

          <figure class="article-figure">
            <svg viewBox="0 0 960 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#0D1117; border-radius:10px; border:1px solid #262626; display:block;">
              <defs>
                <linearGradient id="pipeGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#161B22"/>
                  <stop offset="100%" stop-color="#0E1217"/>
                </linearGradient>
                <linearGradient id="pipeGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#1A2210"/>
                  <stop offset="100%" stop-color="#0E150A"/>
                </linearGradient>
                <linearGradient id="pipeArrow" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#555"/>
                  <stop offset="100%" stop-color="#C1DD2D"/>
                </linearGradient>
                <filter id="pipeGlow" x="-10%" y="-10%" width="120%" height="120%">
                  <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="rgba(193,221,45,0.15)"/>
                </filter>
              </defs>

              <!-- Diagram Title -->
              <text x="30" y="36" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#FFF" letter-spacing="0.5">FIGURE 2: HIGH-PERFORMANCE SVG CANDLESTICK RENDERING PIPELINE</text>
              <text x="30" y="54" font-family="'JetBrains Mono', monospace" font-size="11" fill="#888">ARCHITECTURE: STREAM INGESTION &rarr; INDICATOR ENGINE &rarr; VECTOR SYNTHESIS &rarr; COMPOSITOR</text>

              <!-- Stage 1: Market Data Stream -->
              <g transform="translate(30, 80)" filter="url(#pipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#pipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.12)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">01</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">Data Ingestion</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#888">Raw Feed / WebSocket</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; JSON Ticks / BBO</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; OHLCV Aggregator</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Timestamp Binning</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; LTTB Downsampler</text>
              </g>

              <!-- Connector 1 -->
              <path d="M 190 177 L 220 177" stroke="url(#pipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="220,172 230,177 220,182" fill="#C1DD2D"/>

              <!-- Stage 2: Indicator Engine -->
              <g transform="translate(230, 80)" filter="url(#pipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#pipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.12)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">02</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">Indicator Math</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#888">Analytical Transforms</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; SMA / EMA Filters</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Bollinger Bands &sigma;</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Volume Histograms</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Dynamic Extents</text>
              </g>

              <!-- Connector 2 -->
              <path d="M 390 177 L 420 177" stroke="url(#pipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="420,172 430,177 420,182" fill="#C1DD2D"/>

              <!-- Stage 3: Projection & Quantization -->
              <g transform="translate(430, 80)" filter="url(#pipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#pipeGrad2)" stroke="#C1DD2D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.25)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">03</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">Scale Projection</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#C1DD2D">Cartesian to Screen</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="rgba(193,221,45,0.3)" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; Y(P) Inversion Math</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; Subpixel Snapping</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; Nice-Number Ticks</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#DDD">&bull; Slot Width Ratios</text>
              </g>

              <!-- Connector 3 -->
              <path d="M 590 177 L 620 177" stroke="url(#pipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="620,172 630,177 620,182" fill="#C1DD2D"/>

              <!-- Stage 4: Vector Synthesis & DOM -->
              <g transform="translate(630, 80)" filter="url(#pipeGlow)">
                <rect width="160" height="195" rx="8" fill="url(#pipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <rect x="14" y="14" width="30" height="30" rx="6" fill="rgba(193,221,45,0.12)"/>
                <text x="29" y="34" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#C1DD2D" text-anchor="middle">04</text>
                <text x="14" y="68" font-family="'Inter', sans-serif" font-size="14" font-weight="700" fill="#FFF">SVG Synthesis</text>
                <text x="14" y="86" font-family="'Inter', sans-serif" font-size="11" fill="#888">Batched DOM Assembly</text>
                <line x1="14" y1="96" x2="146" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="14" y="118" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Wick Path Merging</text>
                <text x="14" y="136" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Body Rect Clamping</text>
                <text x="14" y="154" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Spline Bézier Paths</text>
                <text x="14" y="172" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#AAA">&bull; Volumetric Polygons</text>
              </g>

              <!-- Connector 4 -->
              <path d="M 790 177 L 820 177" stroke="url(#pipeArrow)" stroke-width="2.5" fill="none"/>
              <polygon points="820,172 830,177 820,182" fill="#C1DD2D"/>

              <!-- Stage 5: Compositor & HUD -->
              <g transform="translate(830, 80)" filter="url(#pipeGlow)">
                <rect width="100" height="195" rx="8" fill="url(#pipeGrad1)" stroke="#30363D" stroke-width="1.5"/>
                <text x="14" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#C1DD2D">05. OUTPUT</text>
                <text x="14" y="65" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#FFF">GPU Render</text>
                <text x="14" y="82" font-family="'Inter', sans-serif" font-size="10" fill="#888">120 FPS HUD</text>
                <line x1="10" y1="96" x2="90" y2="96" stroke="#262626" stroke-width="1"/>
                <text x="10" y="120" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; Crosshair</text>
                <text x="10" y="140" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; PDF Export</text>
                <text x="10" y="160" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; ARIA Feed</text>
                <text x="10" y="180" font-family="'JetBrains Mono', monospace" font-size="9" fill="#AAA">&bull; SVG Snaps</text>
              </g>
            </svg>
            <figcaption>Figure 2: Comprehensive multi-stage architectural pipeline of the SVG financial trading engine: from high-frequency tick data ingestion and downsampling to indicator calculation, Cartesian-to-screen coordinate inversion, batched vector synthesis, and hardware-accelerated crosshair telemetry.</figcaption>
          </figure>
        </section>

        <section id="interactive-trading-studio">
          <h2>7. Interactive Developer Studio: Live SVG Financial Candlestick Workbench</h2>
          <p>To demonstrate the real-time mathematical projection, indicator synthesis, and interactive crosshair mechanics detailed in this guide, test our production <strong>SVG Financial Candlestick Studio</strong>. This fully functional workbench renders four distinct market environments in native, dependency-free SVG, complete with live indicator toggling, interactive crosshair telemetry, real-time OHLC metrics inspection, and instant vector SVG export.</p>

          <p>Experiment with the workbench using the following interactive controls:</p>
          <ul>
            <li><strong>Select Market Preset:</strong> Switch between four real-world financial topologies: <em>BTC/USD Crypto Volatility</em> (high beta, dynamic wide ranges), <em>S&amp;P 500 Equity Index</em> (steady macro bullish trend), <em>Tech Mega-Cap Breakout</em> (consolidation into gap up), and <em>Forex Mean-Reverting Channel</em> (cyclical oscillator).</li>
            <li><strong>Toggle Technical Indicators:</strong> Activate or deactivate the 20-period Simple Moving Average (cyan curve), the 50-period Exponential Moving Average (amber curve), the Bollinger Bands &plusmn;2&sigma; volatility envelope (shaded yellow ribbon), and the bottom Volume Histogram panel.</li>
            <li><strong>Interactive Crosshair Inspection:</strong> Move your mouse or drag your touch pointer across the chart canvas. Notice how the vertical timeline and horizontal price markers snap instantaneously to the active candlestick, updating the high-precision OHLC readout table at 120 FPS.</li>
            <li><strong>Export Vector Assets:</strong> Click "Copy SVG Markup" to copy the pristine, standalone SVG element directly to your clipboard, or "Download CSV Data" to inspect the underlying OHLC dataset.</li>
          </ul>

          <div class="interactive-sandbox" id="candlestickStudio">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>
                <span>Live Interactive SVG Candlestick &amp; Indicator Studio</span>
              </div>
              <span class="sandbox-badge">Real-Time Vector Engine</span>
            </div>

            <div class="sandbox-grid">
              <div class="sandbox-controls">
                <div class="control-row">
                  <label for="marketPresetSelect">Market Topology Preset: <span class="stat-num" id="presetBadge">BTC/USD Crypto</span></label>
                  <select id="marketPresetSelect" class="control-select">
                    <option value="crypto" selected>BTC/USD - High Volatility Crypto Run</option>
                    <option value="sp500">S&amp;P 500 - Macro Equity Bull Trend</option>
                    <option value="tech_breakout">NVDA / Tech - Volume Consolidation Breakout</option>
                    <option value="forex">EUR/USD - Mean-Reverting Forex Range</option>
                  </select>
                </div>

                <div class="control-row">
                  <label>Technical Indicator Overlays:</label>
                  <div class="btn-row">
                    <button type="button" class="action-btn" id="btnToggleSMA" data-active="true">SMA (20)</button>
                    <button type="button" class="action-btn" id="btnToggleEMA" data-active="true">EMA (50)</button>
                    <button type="button" class="action-btn" id="btnToggleBB" data-active="true">Bollinger Bands</button>
                    <button type="button" class="action-btn" id="btnToggleVolume" data-active="true">Volume Subplot</button>
                  </div>
                </div>

                <div class="control-row">
                  <label for="colorThemeSelect">Visual Palette Theme:</label>
                  <select id="colorThemeSelect" class="control-select">
                    <option value="standard" selected>Emerald / Crimson (Classic Wall St)</option>
                    <option value="neon">Neon Lime / Hot Magenta (Cyberpunk)</option>
                    <option value="monochrome">Hollow Black / White (Institutional Print)</option>
                  </select>
                </div>

                <div class="stats-readout-box">
                  <div class="stat-item">
                    <div class="stat-label">Session Open</div>
                    <div class="stat-val" id="hudOpen">$92,450.00</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Session High</div>
                    <div class="stat-val highlight" id="hudHigh">$95,120.00</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Session Low</div>
                    <div class="stat-val bearish" id="hudLow">$91,800.00</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Session Close</div>
                    <div class="stat-val bullish" id="hudClose">$94,860.00</div>
                  </div>
                </div>

                <div class="btn-row">
                  <button type="button" class="action-btn primary" id="btnCopySVG">Copy SVG Markup</button>
                  <button type="button" class="action-btn" id="btnRandomizeData">Simulate Market Ticks</button>
                </div>

                <div class="control-row">
                  <label>Exported Vector Source (Live Snippet):</label>
                  <div class="code-preview-pane" id="codePreviewPane">&lt;!-- Initializing SVG Candlestick Engine... --&gt;</div>
                </div>
              </div>

              <div class="stage-wrapper">
                <div class="preview-stage-container" id="stageContainer">
                  <svg id="candlestickCanvas" class="stage-canvas-element" viewBox="0 0 760 400" preserveAspectRatio="none">
                    <!-- Dynamic Elements Injected by JavaScript -->
                  </svg>
                </div>
                <div style="font-size:12px; color:#777; text-align:center; font-family:'JetBrains Mono', monospace;">
                  Tip: Hover or touch the chart to activate subpixel crosshair inspection.
                </div>
              </div>
            </div>
          </div>
        </section>

        <section id="performance-optimization">
          <h2>8. Performance Engineering &amp; High-Frequency DOM Optimization</h2>
          <p>A primary criticism historically levied against SVG in data-dense financial applications is DOM node bloat. If an application attempts to render 10,000 historical 5-minute candles on a single canvas, creating three SVG elements per candle results in 30,000 DOM nodes. This volume of elements can trigger garbage collection pauses, inflate memory usage to hundreds of megabytes, and cause noticeable scrolling stutter.</p>

          <p>However, modern high-performance SVG architectures employ several advanced optimization techniques that allow SVG to scale comfortably across tens of thousands of data points without compromising 60 FPS performance.</p>

          <h3>8.1 The Compound Path Batching Technique</h3>
          <p>Rather than authoring individual <code>&lt;rect&gt;</code> and <code>&lt;line&gt;</code> elements for every single candlestick, our engine batches all identical geometric primitives into single compound SVG <code>&lt;path&gt;</code> elements. Regardless of whether the viewport contains 50 candles or 5,000 candles, the entire price layer collapses into exactly <strong>three DOM elements</strong>:</p>
          <ol>
            <li><strong>Compound Bullish Wicks Path:</strong> All vertical upper and lower wicks for bullish sessions concatenated into one single path <code>d</code> string: <code>&lt;path class="wicks-bullish" d="M x1 y1 L x1 y2 M x2 y3 L x2 y4 ..." /&gt;</code>.</li>
            <li><strong>Compound Bullish Bodies Path:</strong> All bullish rectangular bodies drawn as closed sub-paths within a single element: <code>&lt;path class="bodies-bullish" d="M x y h w v h z M x2 y2 h w v h z ..." /&gt;</code>.</li>
            <li><strong>Compound Bearish Path:</strong> All bearish wicks and bodies similarly batched into single path nodes.</li>
          </ol>

          <p>By collapsing thousands of DOM nodes into three native vector paths, the browser's internal C++ layout tree is reduced by <strong>99.9%</strong>. Style resolution, bounding-box hit calculation, and GPU paint batching operate at near-instantaneous speeds, completely matching immediate-mode canvas performance while preserving pristine vector scalability.</p>

          <h3>8.2 Level-of-Detail (LOD) Downsampling: The LTTB Algorithm</h3>
          <p>When an investor zooms out to view a 5-year multi-thousand-bar history of an asset, the physical width of a single day's candle collapses to less than a single screen pixel (<em>W</em><sub>slot</sub> &lt; 1px). Rendering subpixel candles that overlap identically wastes CPU cycles and produces visual moiré interference.</p>

          <p>To solve this, professional vector trading platforms implement the <strong>Largest Triangle Three Buckets (LTTB)</strong> downsampling algorithm. Unlike naive decimation (which merely samples every <em>k</em>-th point and misses critical price spikes), LTTB divides the dataset into equal temporal buckets and selects the point that maximizes the triangular area formed with the previous and subsequent buckets. This guarantees that all major local highs, lows, and volatility spikes are preserved with 100% visual fidelity while reducing the active rendering dataset down to exactly the number of physical horizontal pixels available on the display.</p>
        </section>

        <section id="accessibility-and-compliance">
          <h2>9. Accessibility, WCAG 2.2 AA Compliance &amp; Screen Reader Semantics</h2>
          <p>In enterprise software, healthcare finance, government securities, and institutional banking, web applications are legally required to comply with international accessibility standards, including the United States Section 508 and the global W3C WCAG 2.2 AA criteria. Static canvas charts almost uniformly fail these standards because they present an opaque graphical surface that is completely indecipherable to assistive software.</p>

          <p>Native SVG enables comprehensive, automated accessibility through semantic structural attributes:</p>

          <pre><code>&lt;!-- Accessible Financial Chart Container --&gt;
&lt;svg role="graphics-document" aria-roledescription="financial candlestick chart"
     aria-label="Bitcoin USD 30-day price trend chart, currently trading at $94,860, showing a 2.6% net gain."
     viewBox="0 0 760 400"&gt;
  &lt;title&gt;BTC/USD Daily Candlestick Chart (November 2026)&lt;/title&gt;
  &lt;desc&gt;A series of 30 daily price candles ranging from a low of $88,200 on Nov 2 to a high of $95,120 on Nov 15.&lt;/desc&gt;
  
  &lt;!-- Keyboard Accessible Data Points --&gt;
  &lt;g role="feed" aria-label="Historical daily price sessions"&gt;
    &lt;g role="article" tabindex="0" 
       aria-label="November 15, 2026: Bullish candle. Open $92,450, High $95,120, Low $91,800, Close $94,860. Volume 14,250 BTC."&gt;
      &lt;!-- Candle Vector Primitives --&gt;
    &lt;/g&gt;
  &lt;/g&gt;
&lt;/svg&gt;</code></pre>

          <p>In addition to ARIA labels, our engine injects a visually hidden HTML table (<code>&lt;table class="sr-only"&gt;</code>) directly adjacent to the SVG canvas. When a visually impaired user encounters the chart, their screen reader presents a structured data table containing the exact numeric values for Date, Open, High, Low, Close, and Volume, enabling complete analytical parity for all users.</p>
        </section>

        <section id="faq-section" class="faq-block">
          <h2>10. Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3 class="faq-question">Why build financial candlestick charts in pure SVG rather than HTML5 Canvas?</h3>
            <div class="faq-answer">Scalable Vector Graphics (SVG) maintains infinite resolution independence, allowing financial reports, equity research documents, and executive dashboards to be zoomed or printed at 600 DPI without pixelation. Crucially, SVG preserves the document object model (DOM) identity of individual price bars, technical indicators, and price thresholds. This enables declarative CSS styling, screen reader accessibility under WCAG 2.2 AA, semantic DOM event binding without complex raycasting math, and seamless vector export into PDF prospectus sheets.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How do you calculate the pixel coordinates for OHLC candlestick wicks and bodies in SVG?</h3>
            <div class="faq-answer">For a price range between P_min and P_max mapped to a plot area of height H with padding top Y_pad, the vertical pixel coordinate of price P is computed as: y(P) = Y_pad + (P_max - P) / (P_max - P_min) * (H - 2 * Y_pad). The upper wick is drawn from y(High) to y(max(Open, Close)), the real body is drawn as a rectangle from y(max(Open, Close)) with height |y(Open) - y(Close)|, and the lower wick extends from y(min(Open, Close)) to y(Low).</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How do you render smooth Moving Average (SMA/EMA) indicator curves in SVG?</h3>
            <div class="faq-answer">After computing the sliding window average across N periods, each continuous indicator point (x_i, y_i) is assembled into an SVG path string using the 'M' (moveto) command followed by consecutive 'L' (lineto) or cubic Bézier 'C' smoothing commands. Setting fill='none', stroke-width='2', and vector-effect='non-scaling-stroke' ensures the indicator curve renders with constant optical weight regardless of canvas zoom.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How does crosshair tracking and tooltip inspection work without degrading chart frame rates?</h3>
            <div class="faq-answer">To achieve 120 FPS performance, pointer movement is tracked on an invisible overlay rect using PointerEvents. Coordinates are quantized to the nearest candlestick slot index using O(1) floor division: index = Math.floor((pointerX - leftPadding) / candleSlotWidth). The crosshair horizontal line, vertical line, price axis tag, and time badge update via transform: translate3d() on GPU-accelerated SVG g elements, avoiding expensive DOM re-renders.</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How do you render shaded volatility bands like Bollinger Bands in pure SVG?</h3>
            <div class="faq-answer">Bollinger Bands are constructed by evaluating the standard deviation sigma over an N-period window. The upper band (SMA + k*sigma) and lower band (SMA - k*sigma) are synthesized into a single closed SVG polygon or path element. The path traces the upper band from left to right using 'M x0 y0 L ...', connects vertically to the lower band endpoint, and traces the lower band backwards from right to left before closing with 'Z', styled with semi-transparent fill like rgba(193, 221, 45, 0.08).</div>
          </div>
          <div class="faq-item">
            <h3 class="faq-question">How can large historical financial datasets (thousands of bars) be optimized in SVG?</h3>
            <div class="faq-answer">For datasets exceeding 1,000 candles, individual rect and line elements can cause DOM bloat. Similar to techniques explored in our benchmark on <a href="/articles/how-to-optimize-svg-icons-for-web-performance/">optimizing SVG icons and vector performance</a> and <a href="/articles/svg-gantt-charts-and-project-timelines-guide/">SVG Gantt charts and project timelines</a>, high-performance vector charting requires disciplined element batching. High-performance SVG trading engines batch all bullish bodies into a single compound path 'd' attribute, all bearish bodies into a second path, and all wicks into a third path. Additionally, level-of-detail (LOD) decimation algorithms like Largest Triangle Three Buckets (LTTB) downsample off-screen or zoomed-out data while preserving critical market price peaks and troughs.</div>
          </div>
        </section>
      </article>

            <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <ol>
              <li><a href="#introduction-fintech-imperative">1. The Vector Imperative</a></li>
              <li><a href="#ohlc-anatomy-and-math">2. OHLC Anatomy &amp; Math</a></li>
              <li><a href="#svg-rendering-primitives">3. Declarative SVG Primitives</a></li>
              <li><a href="#technical-indicators-geometry">4. Technical Indicators Geometry</a></li>
              <li><a href="#interactive-crosshairs-and-telemetry">5. Interactive Crosshairs</a></li>
              <li><a href="#architectural-pipeline-diagram">6. Architectural Pipeline</a></li>
              <li><a href="#interactive-trading-studio">7. Interactive Developer Studio</a></li>
              <li><a href="#performance-optimization">8. Performance Optimization</a></li>
              <li><a href="#accessibility-and-compliance">9. Accessibility &amp; Compliance</a></li>
              <li><a href="#faq-section">10. Frequently Asked Questions</a></li>
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

    // Interactive Candlestick Studio Engine
    (function initCandlestickStudio() {
      const canvas = document.getElementById('candlestickCanvas');
      const presetSelect = document.getElementById('marketPresetSelect');
      const presetBadge = document.getElementById('presetBadge');
      const themeSelect = document.getElementById('colorThemeSelect');
      const btnToggleSMA = document.getElementById('btnToggleSMA');
      const btnToggleEMA = document.getElementById('btnToggleEMA');
      const btnToggleBB = document.getElementById('btnToggleBB');
      const btnToggleVolume = document.getElementById('btnToggleVolume');
      const btnCopySVG = document.getElementById('btnCopySVG');
      const btnRandomize = document.getElementById('btnRandomizeData');
      const codePreview = document.getElementById('codePreviewPane');

      const hudOpen = document.getElementById('hudOpen');
      const hudHigh = document.getElementById('hudHigh');
      const hudLow = document.getElementById('hudLow');
      const hudClose = document.getElementById('hudClose');

      let showSMA = true;
      let showEMA = true;
      let showBB = true;
      let showVolume = true;
      let activePalette = 'standard';
      let currentPreset = 'crypto';

      const config = {
        width: 760,
        height: 400,
        padTop: 30,
        padBottom: 70,
        padLeft: 20,
        padRight: 65,
        volumeHeight: 65
      };

      // Generate Synthetic Market Data
      function generateMarketData(preset, count = 38) {
        let basePrice = preset === 'crypto' ? 92000 : preset === 'sp500' ? 5800 : preset === 'tech_breakout' ? 140 : 1.085;
        let volatility = preset === 'crypto' ? 0.022 : preset === 'sp500' ? 0.006 : preset === 'tech_breakout' ? 0.028 : 0.0035;
        const data = [];
        let cur = basePrice;

        for (let i = 0; i < count; i++) {
          const delta = (Math.random() - 0.48) * volatility * cur;
          const open = cur;
          const close = cur + delta;
          const wick1 = Math.random() * volatility * 0.8 * cur;
          const wick2 = Math.random() * volatility * 0.8 * cur;
          const high = Math.max(open, close) + wick1;
          const low = Math.min(open, close) - wick2;
          const volume = Math.floor(Math.random() * 8000 + 2000);
          
          const d = new Date(2026, 10, i + 1);
          const dateStr = d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });

          data.push({ date: dateStr, open, high, low, close, volume });
          cur = close;
        }
        return data;
      }

      let marketData = generateMarketData(currentPreset);

      function renderChart() {
        if (!canvas) return;

        // Calculate Extents
        let minPrice = Infinity;
        let maxPrice = -Infinity;
        let maxVolume = 0;

        marketData.forEach(c => {
          if (c.low < minPrice) minPrice = c.low;
          if (c.high > maxPrice) maxPrice = c.high;
          if (c.volume > maxVolume) maxVolume = c.volume;
        });

        // Add 5% headroom padding
        const priceRange = maxPrice - minPrice || 1;
        minPrice -= priceRange * 0.05;
        maxPrice += priceRange * 0.05;

        const plotW = config.width - config.padLeft - config.padRight;
        const plotH = config.height - config.padTop - config.padBottom - (showVolume ? config.volumeHeight : 0);
        const candleSlotW = plotW / marketData.length;
        const bodyW = Math.max(2, candleSlotW * 0.72);

        function getY(price) {
          return config.padTop + ((maxPrice - price) / (maxPrice - minPrice)) * plotH;
        }

        function getX(index) {
          return config.padLeft + (index + 0.5) * candleSlotW;
        }

        // Color definitions
        let bullColor = '#10B981';
        let bearColor = '#EF4444';
        if (activePalette === 'neon') {
          bullColor = '#C1DD2D';
          bearColor = '#EC4899';
        } else if (activePalette === 'monochrome') {
          bullColor = '#E5E7EB';
          bearColor = '#4B5563';
        }

        // Build SVG Elements
        let svg = `
          <defs>
            <linearGradient id="volGradBull" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="${bullColor}" stop-opacity="0.35"/>
              <stop offset="100%" stop-color="${bullColor}" stop-opacity="0.05"/>
            </linearGradient>
            <linearGradient id="volGradBear" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="${bearColor}" stop-opacity="0.35"/>
              <stop offset="100%" stop-color="${bearColor}" stop-opacity="0.05"/>
            </linearGradient>
          </defs>

          <!-- Background Coordinate Grid -->
          <g class="grid-lines" stroke="rgba(255,255,255,0.06)" stroke-width="1" stroke-dasharray="3 3">
        `;

        // 4 Horizontal Grid Lines
        for (let i = 0; i <= 4; i++) {
          const tickPrice = minPrice + (priceRange / 4) * i;
          const yPos = getY(tickPrice);
          const priceLabel = currentPreset === 'crypto' || currentPreset === 'sp500' ? '$' + tickPrice.toFixed(0) : currentPreset === 'tech_breakout' ? '$' + tickPrice.toFixed(2) : tickPrice.toFixed(4);
          svg += `
            <line x1="${config.padLeft}" y1="${yPos}" x2="${config.width - config.padRight}" y2="${yPos}" />
            <text x="${config.width - config.padRight + 6}" y="${yPos + 4}" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#666">${priceLabel}</text>
          `;
        }
        svg += `</g>`;

        // Volume Subplot Bars
        if (showVolume) {
          const volBaseY = config.height - config.padBottom;
          svg += `<g class="volume-panel">`;
          marketData.forEach((c, idx) => {
            const isBull = c.close >= c.open;
            const barH = (c.volume / (maxVolume || 1)) * (config.volumeHeight - 10);
            const cx = getX(idx);
            const bx = cx - bodyW / 2;
            const by = volBaseY - barH;
            const gradId = isBull ? 'url(#volGradBull)' : 'url(#volGradBear)';
            svg += `<rect x="${bx}" y="${by}" width="${bodyW}" height="${barH}" fill="${gradId}" rx="1"/>`;
          });
          svg += `</g>`;
        }

        // Bollinger Bands Shaded Area
        if (showBB && marketData.length >= 20) {
          const upperPts = [];
          const lowerPts = [];
          for (let i = 19; i < marketData.length; i++) {
            let sum = 0;
            for (let j = 0; j < 20; j++) sum += marketData[i - j].close;
            const mean = sum / 20;
            let variance = 0;
            for (let j = 0; j < 20; j++) variance += Math.pow(marketData[i - j].close - mean, 2);
            const stdDev = Math.sqrt(variance / 20);
            upperPts.push({ x: getX(i), y: getY(mean + 2 * stdDev) });
            lowerPts.push({ x: getX(i), y: getY(mean - 2 * stdDev) });
          }

          let bbPath = `M ${upperPts[0].x} ${upperPts[0].y}`;
          for (let i = 1; i < upperPts.length; i++) bbPath += ` L ${upperPts[i].x} ${upperPts[i].y}`;
          for (let i = lowerPts.length - 1; i >= 0; i--) bbPath += ` L ${lowerPts[i].x} ${lowerPts[i].y}`;
          bbPath += ' Z';

          svg += `<path d="${bbPath}" fill="rgba(193, 221, 45, 0.08)" stroke="rgba(193, 221, 45, 0.3)" stroke-width="1" stroke-dasharray="2 2" />`;
        }

        // SMA Curve (Cyan)
        if (showSMA && marketData.length >= 20) {
          let smaD = '';
          for (let i = 19; i < marketData.length; i++) {
            let sum = 0;
            for (let j = 0; j < 20; j++) sum += marketData[i - j].close;
            const val = sum / 20;
            const px = getX(i);
            const py = getY(val);
            smaD += (i === 19 ? `M ${px} ${py}` : ` L ${px} ${py}`);
          }
          svg += `<path d="${smaD}" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round"/>`;
        }

        // EMA Curve (Amber)
        if (showEMA && marketData.length >= 10) {
          let k = 2 / (20 + 1);
          let ema = marketData[0].close;
          let emaD = `M ${getX(0)} ${getY(ema)}`;
          for (let i = 1; i < marketData.length; i++) {
            ema = marketData[i].close * k + ema * (1 - k);
            emaD += ` L ${getX(i)} ${getY(ema)}`;
          }
          svg += `<path d="${emaD}" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round"/>`;
        }

        // Candlesticks (Wicks + Bodies)
        svg += `<g class="candlestick-bars">`;
        marketData.forEach((c, idx) => {
          const isBull = c.close >= c.open;
          const color = isBull ? bullColor : bearColor;
          const cx = Math.floor(getX(idx)) + 0.5;
          const bx = Math.floor(cx - bodyW / 2);
          const yHigh = getY(c.high);
          const yLow = getY(c.low);
          const yOpen = getY(c.open);
          const yClose = getY(c.close);
          const bodyY = Math.min(yOpen, yClose);
          const bodyH = Math.max(2, Math.abs(yClose - yOpen));

          // Wick Line
          svg += `<line x1="${cx}" y1="${yHigh}" x2="${cx}" y2="${yLow}" stroke="${color}" stroke-width="1.5" stroke-linecap="round"/>`;
          // Body Rect
          svg += `<rect x="${bx}" y="${bodyY}" width="${bodyW}" height="${bodyH}" rx="1.5" fill="${color}" stroke="${color}" stroke-width="0.5"/>`;
        });
        svg += `</g>`;

        // Crosshair Group (Hidden by default)
        svg += `
          <g id="crosshairOverlay" style="display:none; pointer-events:none;">
            <line id="crosshairV" x1="0" y1="${config.padTop}" x2="0" y2="${config.height - config.padBottom}" stroke="rgba(255,255,255,0.4)" stroke-width="1" stroke-dasharray="3 3"/>
            <line id="crosshairH" x1="${config.padLeft}" y1="0" x2="${config.width - config.padRight}" y2="0" stroke="rgba(255,255,255,0.4)" stroke-width="1" stroke-dasharray="3 3"/>
            
            <g id="priceTagGroup">
              <rect x="0" y="0" width="60" height="20" rx="3" fill="#C1DD2D"/>
              <text id="priceTagText" x="30" y="14" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#0A0A0A" text-anchor="middle">$0.00</text>
            </g>

            <g id="timeTagGroup">
              <rect x="0" y="0" width="64" height="18" rx="3" fill="#222" stroke="#444"/>
              <text id="timeTagText" x="32" y="13" font-family="'JetBrains Mono', monospace" font-size="10" fill="#FFF" text-anchor="middle">Nov 1</text>
            </g>
          </g>

          <!-- Interaction Capture Layer -->
          <rect id="pointerHitLayer" x="${config.padLeft}" y="${config.padTop}" width="${plotW}" height="${config.height - config.padTop - config.padBottom}" fill="transparent" style="cursor:crosshair;"/>
        `;

        canvas.innerHTML = svg;

        // Attach Pointer Interaction
        const hitLayer = document.getElementById('pointerHitLayer');
        const crosshair = document.getElementById('crosshairOverlay');
        const chV = document.getElementById('crosshairV');
        const chH = document.getElementById('crosshairH');
        const priceTag = document.getElementById('priceTagGroup');
        const priceText = document.getElementById('priceTagText');
        const timeTag = document.getElementById('timeTagGroup');
        const timeText = document.getElementById('timeTagText');

        if (hitLayer) {
          hitLayer.addEventListener('pointermove', (e) => {
            const rect = canvas.getBoundingClientRect();
            const scaleX = config.width / rect.width;
            const scaleY = config.height / rect.height;
            const mouseX = (e.clientX - rect.left) * scaleX;
            const mouseY = (e.clientY - rect.top) * scaleY;

            const slotIndex = Math.floor((mouseX - config.padLeft) / candleSlotW);
            const clampedIndex = Math.max(0, Math.min(marketData.length - 1, slotIndex));
            const candle = marketData[clampedIndex];
            const candleX = getX(clampedIndex);

            crosshair.style.display = 'block';
            chV.setAttribute('x1', candleX);
            chV.setAttribute('x2', candleX);
            chH.setAttribute('y1', mouseY);
            chH.setAttribute('y2', mouseY);

            // Compute Price at cursor
            const curPrice = maxPrice - ((mouseY - config.padTop) / plotH) * (maxPrice - minPrice);
            const fmtPrice = currentPreset === 'crypto' || currentPreset === 'sp500' ? '$' + curPrice.toFixed(0) : '$' + curPrice.toFixed(2);
            priceText.textContent = fmtPrice;
            priceTag.setAttribute('transform', `translate(${config.width - config.padRight + 4}, ${mouseY - 10})`);

            timeText.textContent = candle.date;
            timeTag.setAttribute('transform', `translate(${candleX - 32}, ${config.height - config.padBottom + 4})`);

            // Update HUD
            if (hudOpen) hudOpen.textContent = '$' + candle.open.toFixed(2);
            if (hudHigh) hudHigh.textContent = '$' + candle.high.toFixed(2);
            if (hudLow) hudLow.textContent = '$' + candle.low.toFixed(2);
            if (hudClose) {
              hudClose.textContent = '$' + candle.close.toFixed(2);
              hudClose.className = 'stat-val ' + (candle.close >= candle.open ? 'bullish' : 'bearish');
            }
          });

          hitLayer.addEventListener('pointerleave', () => {
            if (crosshair) crosshair.style.display = 'none';
          });
        }

        // Update code snippet preview
        if (codePreview) {
          const sample = `<svg viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg">\n  <!-- Generated Candlestick Visualizer -->\n  <line x1="${getX(0).toFixed(1)}" y1="${getY(marketData[0].high).toFixed(1)}" x2="${getX(0).toFixed(1)}" y2="${getY(marketData[0].low).toFixed(1)}" stroke="${bullColor}" stroke-width="1.5"/>\n  <rect x="${(getX(0)-bodyW/2).toFixed(1)}" y="${getY(marketData[0].close).toFixed(1)}" width="${bodyW.toFixed(1)}" height="12.0" fill="${bullColor}"/>\n</svg>`;
          codePreview.textContent = sample;
        }
      }

      // Event Listeners for Controls
      if (presetSelect) {
        presetSelect.addEventListener('change', (e) => {
          currentPreset = e.target.value;
          presetBadge.textContent = e.target.options[e.target.selectedIndex].text.split(' - ')[0];
          marketData = generateMarketData(currentPreset);
          renderChart();
        });
      }

      if (themeSelect) {
        themeSelect.addEventListener('change', (e) => {
          activePalette = e.target.value;
          renderChart();
        });
      }

      function setupToggle(btn, callback) {
        if (!btn) return;
        btn.addEventListener('click', () => {
          const active = btn.getAttribute('data-active') === 'true';
          const next = !active;
          btn.setAttribute('data-active', next ? 'true' : 'false');
          btn.style.borderColor = next ? '#C1DD2D' : '#333';
          btn.style.color = next ? '#FFF' : '#666';
          callback(next);
          renderChart();
        });
      }

      setupToggle(btnToggleSMA, (val) => { showSMA = val; });
      setupToggle(btnToggleEMA, (val) => { showEMA = val; });
      setupToggle(btnToggleBB, (val) => { showBB = val; });
      setupToggle(btnToggleVolume, (val) => { showVolume = val; });

      if (btnRandomize) {
        btnRandomize.addEventListener('click', () => {
          marketData = generateMarketData(currentPreset);
          renderChart();
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

      if (btnCopySVG) {
        btnCopySVG.addEventListener('click', () => {
          if (canvas) {
            copyToClipboard(canvas.outerHTML, () => {
              const orig = btnCopySVG.textContent;
              btnCopySVG.textContent = 'Copied to Clipboard!';
              setTimeout(() => { btnCopySVG.textContent = orig; }, 1800);
            });
          }
        });
      }

      // Initial Render
      renderChart();
    })();
  </script>
</body>
</html>
'''

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {target_file} ({len(html_content)} bytes)")
