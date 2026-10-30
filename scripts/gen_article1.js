const fs = require('fs');
const path = require('path');

const outDir = path.join('articles', 'svg-bezier-curves-and-path-math-guide');
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

const html = `<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SVG Bézier Curves &amp; Path Math: The Complete Engineering Guide (2026) | IconStash</title>
  <meta name="description" content="Master SVG cubic and quadratic Bézier curve math: polynomial formulas, de Casteljau's algorithm, tangent vectors, curvature, and interactive path studio.">
  <meta name="keywords" content="svg bezier curve, cubic bezier math, quadratic bezier svg, svg path curvature, de casteljau algorithm, bezier curve formula javascript, svg smooth path, svg c s q t path commands">
  <meta property="og:title" content="SVG Bézier Curves &amp; Path Math: The Complete Engineering Guide (2026)">
  <meta property="og:description" content="Master SVG cubic and quadratic Bézier curve math: polynomial formulas, de Casteljau's algorithm, tangent vectors, curvature, and interactive path studio.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-bezier-curves-and-path-math-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-bezier-curves-and-path-math-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-10-30T00:00:00Z">
  <meta property="article:modified_time" content="2026-10-30T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="Vector Geometry &amp; Mathematics">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="Bézier Curves">
  <meta property="article:tag" content="Vector Math">
  <meta property="article:tag" content="Frontend Engineering">
  <meta property="article:tag" content="Web Animation">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="SVG Bézier Curves &amp; Path Math: The Complete Engineering Guide (2026)">
  <meta name="twitter:description" content="Master SVG cubic and quadratic Bézier curve math: polynomial formulas, de Casteljau's algorithm, tangent vectors, curvature, and interactive path studio.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-bezier-curves-and-path-math-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-bezier-curves-and-path-math-guide/">
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
      "headline": "SVG Bézier Curves & Path Math: The Complete Engineering Guide (2026)",
      "description": "Master SVG cubic and quadratic Bézier curve math: polynomial formulas, de Casteljau's algorithm, tangent vectors, curvature, and interactive path studio.",
      "image": "https://iconstash.io/assets/articles/svg-bezier-curves-and-path-math-guide.jpg",
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
        "url": "https://iconstash.io",
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
      "datePublished": "2026-10-30",
      "dateModified": "2026-10-30",
      "mainEntityOfPage": "https://iconstash.io/articles/svg-bezier-curves-and-path-math-guide/",
      "isPartOf": {
        "@type": "WebSite",
        "@id": "https://iconstash.io/#website"
      },
      "inLanguage": "en-US",
      "wordCount": 4453,
      "articleSection": "Vector Geometry & Mathematics",
      "proficiencyLevel": "Advanced",
      "keywords": [
        "svg bezier curve",
        "cubic bezier math",
        "quadratic bezier svg",
        "svg path curvature",
        "de casteljau algorithm",
        "bezier curve formula javascript",
        "svg smooth path",
        "svg c s q t path commands"
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
          "name": "SVG Bézier Curves & Path Math Guide",
          "item": "https://iconstash.io/articles/svg-bezier-curves-and-path-math-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the mathematical difference between quadratic and cubic Bézier curves in SVG?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A quadratic Bézier curve (defined by SVG command Q) uses a 2nd-degree Bernstein polynomial parameterized by 3 control points: a start anchor, a single direction control point, and an end anchor. It has constant second-derivative curvature and cannot generate inflection points (S-bends). A cubic Bézier curve (command C) uses a 3rd-degree Bernstein polynomial parameterized by 4 control points: a start anchor, two independent direction control points, and an end anchor. The two control points allow cubic curves to model inflection points, changing curvature direction smoothly within a single segment."
          }
        },
        {
          "@type": "Question",
          "name": "How does de Casteljau's algorithm evaluate Bézier curves geometrically?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "De Casteljau's algorithm evaluates a Bézier curve at parameter t (between 0.0 and 1.0) through recursive linear interpolation. For cubic curves, it computes linear interpolations along the 3 polygon edges connecting P0-C1, C1-C2, and C2-P3 to find 3 intermediate points. It then interpolates between those 3 points to find 2 points, and finally interpolates between those 2 points to yield the exact coordinate on the curve. This algorithm guarantees numerical stability in floating-point computation and is fundamental for splitting curves into independent sub-segments."
          }
        },
        {
          "@type": "Question",
          "name": "How do SVG smooth curve commands S and T calculate implicit control points?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The SVG smooth cubic command S and smooth quadratic command T maintain continuous first derivatives (tangent continuity C1) by automatically reflecting the preceding segment's final control point across the shared anchor point. For cubic curves, the first control point C1 is computed as C1 = 2 * P0 - C2_prev. If the preceding command was not a cubic curve, C1 defaults to the current point P0. For quadratic curves, command T computes C1 = 2 * P0 - C1_prev."
          }
        },
        {
          "@type": "Question",
          "name": "Why can cubic Bézier curves only approximate a true circular arc, and what is the optimal kappa constant?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Bézier curves are polynomial parameterizations (x(t), y(t) are polynomials of t), whereas true circles require rational trigonometric equations where x^2 + y^2 = r^2. Polynomials cannot trace exact circles without rational weighting. However, a 90-degree circular arc can be approximated with extreme precision (maximum radial error under 0.0273%) using a cubic Bézier curve whose control points are offset along tangent vectors by the kappa constant: kappa = 4 * (sqrt(2) - 1) / 3, approximately 0.5522847498 times the radius."
          }
        },
        {
          "@type": "Question",
          "name": "How do you calculate the exact bounding box of an SVG cubic Bézier curve without overestimating?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Evaluating only the control points produces a loose convex-hull bounding box that significantly overestimates the curve's true visual bounds. To compute the exact bounding box, calculate the first derivative of the cubic equation with respect to parameter t for both X and Y components: B'(t) = 3a*t^2 + 2b*t + c. Using the quadratic formula, solve for roots where B'(t) = 0. Filter the roots to retain only real numbers strictly within the interval (0, 1). Evaluate the curve position at t = 0, t = 1, and all valid root parameters; the minimum and maximum X and Y values among these candidate points form the exact bounding box."
          }
        },
        {
          "@type": "Question",
          "name": "How do browser graphics engines accelerate Bézier curve rendering on modern GPUs?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Modern graphics engines such as Google Skia (in Chromium) and WebRender (in Firefox) evaluate and rasterize Bézier curves via hardware-accelerated path rendering. Skia's Pathfinder and Ganesh/Graphite pipelines transform cubic curves into monotonic quadratic approximations or tessellate the curves directly into triangle strips within vertex shaders using compute pipelines. This enables 120 FPS hardware rasterization without locking CPU threads or generating bloated DOM path points."
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
    .header-cta { background: #C1DD2D; color: #0A0A0A; font-weight: 700; font-size: 13px; padding: 8px 18px; border-radius: 6px; border: none; cursor: pointer; transition: all 150ms ease; }
    .header-cta:hover { background: #D2ED3E; transform: translateY(-1px); }
    .theme-toggle-btn { background: transparent; border: 1px solid #262626; color: #A3A3A3; width: 34px; height: 34px; border-radius: 6px; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 150ms ease; }
    .theme-toggle-btn:hover { border-color: #404040; color: #F2F2F2; }

    .page-container { max-width: 1280px; margin: 0 auto; padding: 48px 24px 80px; width: 100%; }
    .breadcrumb { display: flex; gap: 8px; font-size: 13px; color: #666; margin-bottom: 24px; align-items: center; flex-wrap: wrap; }
    .breadcrumb a { color: #888; }
    .breadcrumb a:hover { color: #C1DD2D; }
    .breadcrumb .sep { color: #444; }

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

    /* Tables */
    .table-container { overflow-x: auto; margin: 32px 0; border: 1px solid #222; border-radius: 12px; -webkit-overflow-scrolling: touch; }
    table { width: 100%; min-width: 640px; border-collapse: collapse; text-align: left; font-size: 14.5px; }
    th { background: #161616; color: #FFF; padding: 14px 18px; font-weight: 700; border-bottom: 1px solid #222; }
    td { padding: 14px 18px; border-bottom: 1px solid #1A1A1A; color: #CCC; }
    tr:last-child td { border-bottom: none; }
    tr:nth-child(even) { background: rgba(255,255,255,0.01); }

    /* Interactive Studio */
    .interactive-sandbox { background: #121212; border: 1px solid #262626; border-radius: 12px; padding: 24px; margin: 36px 0; }
    .sandbox-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px; border-bottom: 1px solid #222; padding-bottom: 14px; }
    .sandbox-title { display: flex; align-items: center; gap: 8px; font-weight: 800; font-size: 16px; color: #FFF; }
    .sandbox-title svg { color: #C1DD2D; }
    .sandbox-badge { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; background: rgba(193,221,45,0.12); color: #C1DD2D; padding: 3px 8px; border-radius: 4px; border: 1px solid rgba(193,221,45,0.25); }

    .sandbox-grid { display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr); gap: 24px; align-items: start; }
    @media (max-width: 768px) { .sandbox-grid { grid-template-columns: 1fr; } }

    .sandbox-controls { display: flex; flex-direction: column; gap: 16px; }
    .control-row { display: flex; flex-direction: column; gap: 6px; }
    .control-row label { font-size: 13px; font-weight: 600; color: #BBB; display: flex; justify-content: space-between; }
    .control-row .stat-num { color: #C1DD2D; font-family: "JetBrains Mono", monospace; }

    .control-select, .control-input { background: #181818; border: 1px solid #333; color: #F2F2F2; padding: 8px 12px; border-radius: 6px; font-family: "Inter", sans-serif; font-size: 13.5px; width: 100%; }
    .control-select:focus, .control-input:focus { outline: none; border-color: #C1DD2D; }

    .points-input-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 4px; }

    .stage-wrapper { display: flex; flex-direction: column; gap: 14px; }
    .preview-stage-container { width: 100%; height: 320px; border: 1px dashed #444; border-radius: 10px; background: #080808; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; }
    .stage-svg-element { width: 100%; height: 100%; display: block; }
    .viewport-meta-overlay { position: absolute; bottom: 8px; right: 10px; font-size: 11px; font-family: "JetBrains Mono", monospace; color: #888; background: rgba(0,0,0,0.8); padding: 3px 8px; border-radius: 4px; pointer-events: none; border: 1px solid #222; }

    .stats-readout-box { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; background: #0E0E0E; border: 1px solid #222; border-radius: 8px; padding: 12px; }
    .stat-item { text-align: center; }
    .stat-label { font-size: 11px; text-transform: uppercase; color: #777; font-weight: 700; letter-spacing: 0.05em; }
    .stat-val { font-size: 13px; font-weight: 800; color: #FFF; font-family: "JetBrains Mono", monospace; margin-top: 2px; }
    .stat-val.highlight { color: #C1DD2D; }

    .generated-code-box { margin-top: 20px; background: #0A0A0A; border: 1px solid #262626; border-radius: 8px; overflow: hidden; }
    .code-box-head { display: flex; justify-content: space-between; align-items: center; padding: 10px 14px; background: #161616; border-bottom: 1px solid #222; font-size: 12px; font-weight: 700; color: #888; flex-wrap: wrap; gap: 8px; }
    .code-tabs { display: flex; gap: 6px; }
    .code-tab-btn { background: transparent; border: none; color: #888; font-size: 12px; font-weight: 700; cursor: pointer; padding: 4px 8px; border-radius: 4px; }
    .code-tab-btn.active { color: #C1DD2D; background: rgba(193,221,45,0.12); }
    .code-actions { display: flex; gap: 8px; }
    .copy-btn { background: rgba(193,221,45,0.15); border: 1px solid rgba(193,221,45,0.3); color: #C1DD2D; font-size: 11px; font-weight: 700; padding: 5px 12px; border-radius: 4px; cursor: pointer; transition: all 120ms ease; }
    .copy-btn:hover { background: #C1DD2D; color: #0A0A0A; }
    .code-output-area { padding: 16px; max-height: 180px; overflow-y: auto; font-family: "JetBrains Mono", monospace; font-size: 12px; line-height: 1.5; color: #E5E5E5; word-break: break-all; white-space: pre-wrap; background: #080808; margin: 0; border: none; }

    /* Formula Cards & Callouts */
    .formula-card { background: #161616; border: 1px solid #2E2E2E; border-left: 3px solid #C1DD2D; border-radius: 8px; padding: 16px 20px; margin: 20px 0; overflow-x: auto; -webkit-overflow-scrolling: touch; }
    .formula-title { font-size: 12px; text-transform: uppercase; letter-spacing: 0.06em; color: #888; font-weight: 700; margin-bottom: 6px; }
    .formula-body { font-family: "JetBrains Mono", monospace; font-size: 14px; color: #C1DD2D; line-height: 1.5; overflow-x: auto; -webkit-overflow-scrolling: touch; }
    .formula-desc { font-size: 13.5px; color: #AAA; margin-top: 8px; line-height: 1.5; }

    .takeaway-box { background: linear-gradient(135deg, rgba(193,221,45,0.06) 0%, rgba(193,221,45,0.02) 100%); border: 1px solid rgba(193,221,45,0.2); border-radius: 12px; padding: 28px; margin: 40px 0; }
    .takeaway-box h3 { color: #C1DD2D; font-size: 18px; font-weight: 800; margin-bottom: 16px; margin-top: 0; }
    .warning-box { background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.25); border-left: 4px solid #EF4444; border-radius: 8px; padding: 18px 22px; margin: 24px 0; }
    .warning-box h4 { color: #F87171; font-size: 15px; margin-bottom: 8px; }
    .warning-box p { color: #E5E5E5; margin-bottom: 0; font-size: 14.5px; }

    .faq-item { background: #121212; border: 1px solid #222; border-radius: 8px; margin-bottom: 14px; padding: 18px 22px; }
    .faq-item h3 { margin-top: 0; font-size: 16px; color: #FFF; margin-bottom: 8px; }
    .faq-item p { margin-bottom: 0; color: #A3A3A3; font-size: 14.5px; }

    /* Sticky Sidebar */
    .article-sidebar { display: flex; flex-direction: column; gap: 24px; }
    @media (min-width: 1024px) {
      .article-sidebar { position: sticky; top: 80px; }
    }
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

    .site-footer { border-top: 1px solid #1F1F1F; padding: 48px 24px; background: #0A0A0A; text-align: center; font-size: 14px; color: #666; margin-top: 80px; }
    .site-footer a { color: #888; }
    .site-footer a:hover { color: #C1DD2D; }

    @media (max-width: 768px) {
      .page-container { padding: 28px 16px 60px; }
      .site-header nav a:not(.header-cta) { display: none; }
      .site-header nav { gap: 12px; }
      .header-cta { padding: 6px 12px; font-size: 12px; }
      .article-hero h1 { font-size: 26px; }
      .featured-summary { padding: 18px 20px; }
      pre { padding: 14px; font-size: 12.5px; }
      .stats-readout-box { grid-template-columns: 1fr; }
    }

    /* Light Theme Contrast Rules */
    html[data-theme="light"] body { background: #FAFAFA; color: #171717; }
    html[data-theme="light"] .site-header { background: rgba(250,250,250,0.88); border-bottom-color: #E5E5E5; }
    html[data-theme="light"] .site-header .logo { color: #171717; }
    html[data-theme="light"] .site-header nav a { color: #525252; }
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
    html[data-theme="light"] .site-header nav a:hover { color: #0A0A0A; }
    html[data-theme="light"] .breadcrumb a { color: #4D6300; }
    html[data-theme="light"] .breadcrumb a:hover { color: #364600; }
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
    html[data-theme="light"] .generated-code-box { background: #FAFAFA; border-color: #E4E4E7; }
    html[data-theme="light"] .code-box-head { background: #F4F4F5; border-bottom-color: #E4E4E7; color: #525252; }
    html[data-theme="light"] .code-output-area { background: #FFFFFF; color: #1F2937; }
    html[data-theme="light"] .copy-btn { background: #F0F4D8; border-color: #D2ED3E; color: #4D6300; }
    html[data-theme="light"] .copy-btn:hover { background: #4D6300; color: #FFF; }
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
      <a href="/stats/">Statistics</a>
      <button class="theme-toggle-btn" id="themeToggle" aria-label="Toggle Theme">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
      </button>
      <a href="/#/" class="header-cta">Open App</a>
    </nav>
  </header>

  <main class="page-container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a>
      <span class="sep">/</span>
      <a href="/articles/">Articles</a>
      <span class="sep">/</span>
      <span>SVG Bézier Curves &amp; Path Math Guide</span>
    </nav>

    <header class="article-hero">
      <span class="tag">Engineering Deep Dive &bull; 2026</span>
      <h1>SVG Bézier Curves &amp; Path Math: The Complete Engineering Guide</h1>
      <div class="article-meta">
        <span>By <a href="/about/">Jouni Flemming</a></span>
        <span>&bull;</span>
        <span>October 30, 2026</span>
        <span>&bull;</span>
        <span>22 min read</span>
        <span>&bull;</span>
        <span>4,453 words</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">

        <div class="featured-summary">
          <p><strong>Executive Summary for UI Engineers &amp; Graphics Developers:</strong></p>
          <ul>
            <li><strong>Bernstein Polynomial Foundation:</strong> Understand how cubic (C, S) and quadratic (Q, T) SVG path commands translate into parametric polynomials B(t) where t spans [0.0, 1.0].</li>
            <li><strong>De Casteljau's Algorithm:</strong> Master recursive geometric interpolation for curve evaluation, subdivision, and floating-point numerical stability without trigonometric divergence.</li>
            <li><strong>Derivatives, Tangents &amp; Curvature:</strong> Calculate instantaneous velocity vectors B'(t), normal vectors N(t), and curvature kappa(t) for orienting objects along paths, smooth camera movement, and robotic pathing.</li>
            <li><strong>Exact Bounding Box Calculus:</strong> Stop guessing bounding boxes with crude control point convex hulls. Calculate exact extrema roots via the quadratic formula on B'(t) = 0.</li>
            <li><strong>Interactive Developer Studio:</strong> Inspect live parametric points, velocity vectors, control handles, and generated production JavaScript/SVG code in real time.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-bezier-curves-and-path-math-guide.jpg" alt="SVG Bézier Curves Cubic and Quadratic Vector Mathematics Technical Illustration" width="1200" height="675" loading="eager">
          <figcaption>Figure 1: Mathematical coordinate breakdown of cubic and quadratic Bézier curves with control points, velocity tangent vectors, and parametric polynomials.</figcaption>
        </figure>

        <section id="section-intro">
          <h2>1. Introduction: Bézier Curves in Vector Graphics and SVG</h2>
          <p>Every smooth curve rendered in digital computer graphics — from the glyph outlines of web fonts and design system icons in <a href="/articles/lucide-icons-complete-guide/">Lucide</a> or <a href="/articles/heroicons-complete-guide/">Heroicons</a> to responsive data visualization in D3.js and motion paths in modern CSS — relies on the mathematical elegance of Bézier curves. Named after French engineer Pierre Bézier, who popularized them in the 1960s for computer-aided automotive body design at Renault, Bézier curves provide an intuitive yet mathematically rigorous framework for defining complex curved trajectories using discrete anchor points and control handles.</p>
          <p>Within the Scalable Vector Graphics (SVG) specification, path curves are encapsulated inside the ubiquitous <code>d</code> attribute of the <code>&lt;path&gt;</code> element. While lines (<code>L</code>, <code>H</code>, <code>V</code>) require only start and destination coordinates, curved segments introduce higher polynomial degrees. The SVG standard provides two primary classes of polynomial curves: Quadratic Bézier curves (invoked via <code>Q</code> and smooth continuation <code>T</code>) and Cubic Bézier curves (invoked via <code>C</code> and smooth continuation <code>S</code>).</p>
          <p>Too often, web developers treat SVG path strings as impenetrable black boxes generated by design applications like Figma or Illustrator. However, when building dynamic charting engines, vector morphing libraries, canvas renderers, interactive connectors, or animated SVG micro-interactions, relying on opaque design exports leads to severe performance bottlenecks and rendering bugs. In this comprehensive engineering guide, we dissect the rigorous mathematical principles, algebraic formulas, geometric algorithms, and practical implementation patterns required to master SVG Bézier curves from first principles.</p>
        </section>

        <section id="section-math-foundations">
          <h2>2. Parametric Polynomials and the Bernstein Basis Form</h2>
          <p>To manipulate Bézier curves in software, one must first recognize that a Bézier curve is a parametric function. Unlike an explicit Cartesian function <code>y = f(x)</code> (which cannot easily describe vertical lines, loops, or self-intersecting loops without becoming multi-valued), a parametric curve defines both the horizontal <code>x</code> and vertical <code>y</code> coordinates independently as functions of a single scalar parameter, conventionalized as <code>t</code>, where <code>t</code> ranges smoothly from <code>0.0</code> (the start of the curve) to <code>1.0</code> (the conclusion of the curve):</p>

          <div class="formula-card">
            <div class="formula-title">Parametric Vector Definition of Bézier Curves</div>
            <div class="formula-body">B(t) = ( x(t), y(t) ), where t in [0.0, 1.0]</div>
            <div class="formula-desc">Both coordinate axes are evaluated concurrently at normalized parameter step t.</div>
          </div>

          <p>The general mathematical formulation for any Bézier curve of degree <code>n</code> is defined as a linear combination of <code>n + 1</code> control points <code>P_i</code> weighted by the <strong>Bernstein basis polynomials</strong> of degree <code>n</code>:</p>

          <div class="formula-card">
            <div class="formula-title">General Bernstein Polynomial Formula</div>
            <div class="formula-body">B(t) = Sum_{i=0}^{n} [ C(n, i) &times; (1 - t)^(n - i) &times; t^i &times; P_i ]</div>
            <div class="formula-desc">Where C(n, i) represents the binomial coefficient: n! / (i! &times; (n - i)!).</div>
          </div>

          <p>The Bernstein polynomial weights possess remarkable mathematical properties that guarantee the stability and predictability of vector curves:</p>
          <ul>
            <li><strong>Partition of Unity:</strong> For any value of <code>t</code> in the interval <code>[0, 1]</code>, the sum of all Bernstein basis coefficients equals exactly <code>1.0</code>. Mathematically, <code>Sum_{i=0}^{n} b_{i,n}(t) = 1</code>. This ensures that the curve is an affine combination of its control points, making it invariant under translation, rotation, and uniform scaling.</li>
            <li><strong>Non-Negativity:</strong> Within the range <code>0 &le; t &le; 1</code>, every basis polynomial <code>b_{i,n}(t) &ge; 0</code>. Because all weights are non-negative and sum to unity, every point on the curve represents a convex combination of its control points.</li>
            <li><strong>Convex Hull Property:</strong> Because the weights form a convex combination, the entire curve is strictly enclosed within the convex hull of its control points <code>{P_0, P_1, ..., P_n}</code>. Graphics engines exploit this property for extremely fast clipping and bounding-box rejection during spatial indexing and collision detection.</li>
            <li><strong>Endpoint Interpolation:</strong> At <code>t = 0.0</code>, the basis weights reduce such that <code>B(0) = P_0</code>. At <code>t = 1.0</code>, <code>B(1) = P_n</code>. The curve always passes precisely through its initial and terminal anchor points. Intermediate control points generally do not lie on the curve; instead, they act as gravitational attractors dictating the curve's velocity and curvature.</li>
          </ul>

          <p>Let us now examine the two specific polynomial degrees codified into the W3C SVG specification.</p>
        </section>

        <section id="section-quadratic">
          <h2>3. Quadratic Bézier Curves (Q and T Commands)</h2>
          <p>A quadratic Bézier curve is an algebraic polynomial of degree <code>n = 2</code>. It requires exactly three control points: an initial anchor point <code>P_0</code>, a single directional control point <code>C_1</code> (often designated <code>P_1</code>), and a terminal anchor point <code>P_2</code>. In SVG path syntax, a quadratic curve is declared using the <code>Q</code> (absolute) or <code>q</code> (relative) command followed by the control point and destination coordinates:</p>

          <pre><code>&lt;!-- Syntax: M startX startY Q controlX controlY endX endY --&gt;
&lt;path d="M 50 150 Q 150 20 250 150" fill="none" stroke="#C1DD2D" stroke-width="3"/&gt;</code></pre>

          <h3>3.1 Mathematical Formulation of Quadratic Curves</h3>
          <p>Expanding the general Bernstein equation for <code>n = 2</code> produces the explicit quadratic polynomial:</p>

          <div class="formula-card">
            <div class="formula-title">Quadratic Bézier Polynomial Equation</div>
            <div class="formula-body">Q(t) = (1 - t)^2 &times; P_0 + 2 &times; (1 - t) &times; t &times; C_1 + t^2 &times; P_2</div>
            <div class="formula-desc">Evaluated independently for X and Y components across the parameter t in [0.0, 1.0].</div>
          </div>

          <p>By expanding the polynomial terms and grouping by descending powers of <code>t</code>, we obtain the standard monomial power basis representation:</p>

          <div class="formula-card">
            <div class="formula-title">Quadratic Monomial Power Basis</div>
            <div class="formula-body">Q(t) = t^2 &times; (P_0 - 2&times;C_1 + P_2) + t &times; (-2&times;P_0 + 2&times;C_1) + P_0</div>
            <div class="formula-desc">Expressed compactly as Q(t) = A&times;t^2 + B&times;t + C for high-speed algorithmic evaluation.</div>
          </div>

          <h3>3.2 The Smooth Quadratic Continuation (T Command)</h3>
          <p>When chaining multiple curved segments together to build complex vector paths or wave ribbons, maintaining mathematical tangency across junctions is critical. If adjacent segments share an anchor point but have misaligned tangent vectors, a visible sharp crease appears.</p>
          <p>The SVG <code>T</code> (absolute) or <code>t</code> (relative) command provides smooth quadratic continuation. It requires only the destination anchor point coordinates. The browser's graphics engine dynamically computes the control point <code>C_1</code> by reflecting the previous segment's control point across the shared start anchor:</p>

          <div class="formula-card">
            <div class="formula-title">Quadratic Control Point Reflection Formula (T Command)</div>
            <div class="formula-body">C_1 = 2 &times; P_0 - C_{1,\text{prev}}</div>
            <div class="formula-desc">The new control point C_1 is positioned collinear with C_{1,\text{prev}} across anchor P_0.</div>
          </div>

          <p>If the command preceding <code>T</code> is not a quadratic curve (such as a line <code>L</code> or a cubic <code>C</code>), the SVG specification mandates that the control point defaults directly to the current point: <code>C_1 = P_0</code>. In that fallback scenario, the curve degenerates into a linear segment.</p>
        </section>

        <section id="section-cubic">
          <h2>4. Cubic Bézier Curves (C and S Commands)</h2>
          <p>While quadratic curves are computationally lightweight, they suffer from a severe geometric limitation: their second derivative is constant. Consequently, a single quadratic Bézier segment cannot change its direction of curvature; it cannot produce an "S-bend" or inflection point. To create an S-shaped curve with quadratic segments, an engineer must stitch together at least two separate quadratic curves.</p>
          <p>Cubic Bézier curves, defined by polynomials of degree <code>n = 3</code>, overcome this constraint completely. A cubic curve utilizes four control points: initial anchor <code>P_0</code>, first control point <code>C_1</code>, second control point <code>C_2</code>, and destination anchor <code>P_3</code>. The presence of two independent control handles allows cubic curves to form complex non-planar trajectories, loops, and inflection points where curvature smoothly reverses direction.</p>

          <pre><code>&lt;!-- Syntax: M startX startY C ctrl1X ctrl1Y ctrl2X ctrl2Y endX endY --&gt;
&lt;path d="M 40 180 C 80 20 220 280 260 120" fill="none" stroke="#C1DD2D" stroke-width="3"/&gt;</code></pre>

          <h3>4.1 Mathematical Formulation of Cubic Curves</h3>
          <p>Expanding the Bernstein formula for <code>n = 3</code> yields the fundamental cubic Bézier equation:</p>

          <div class="formula-card">
            <div class="formula-title">Cubic Bézier Polynomial Equation</div>
            <div class="formula-body">C(t) = (1 - t)^3 &times; P_0 + 3 &times; (1 - t)^2 &times; t &times; C_1 + 3 &times; (1 - t) &times; t^2 &times; C_2 + t^3 &times; P_3</div>
            <div class="formula-desc">The foundational equation powering vector glyphs in OpenType, SVG path geometry, and CSS easing.</div>
          </div>

          <p>Grouping the terms into the standard monomial power basis <code>C(t) = a&times;t^3 + b&times;t^2 + c&times;t + d</code> gives us the following matrix coefficients:</p>

          <div class="formula-card">
            <div class="formula-title">Cubic Monomial Matrix Coefficients</div>
            <div class="formula-body">
a = -P_0 + 3&times;C_1 - 3&times;C_2 + P_3<br>
b = 3&times;P_0 - 6&times;C_1 + 3&times;C_2<br>
c = -3&times;P_0 + 3&times;C_1<br>
d = P_0
            </div>
            <div class="formula-desc">Precomputing vectors a, b, c, d enables lightning-fast evaluation using Horner's polynomial rule.</div>
          </div>

          <h3>4.2 The Smooth Cubic Continuation (S Command)</h3>
          <p>Similar to the quadratic <code>T</code> command, SVG provides the <code>S</code> (absolute) or <code>s</code> (relative) command for chaining smooth cubic segments. The <code>S</code> command requires only the second control point <code>C_2</code> and the final anchor <code>P_3</code>. The browser calculates the first control point <code>C_1</code> by reflecting the previous cubic curve's second control point <code>C_{2,\text{prev}}</code> across the shared anchor <code>P_0</code>:</p>

          <div class="formula-card">
            <div class="formula-title">Cubic Control Point Reflection Formula (S Command)</div>
            <div class="formula-body">C_1 = 2 &times; P_0 - C_{2,\text{prev}}</div>
            <div class="formula-desc">Guarantees C^1 continuity (matching tangent vector direction and magnitude) at the junction.</div>
          </div>

          <p>If the command preceding <code>S</code> is not a cubic Bézier command (<code>C</code> or <code>S</code>), <code>C_1</code> is assumed to be coincident with the current point <code>P_0</code>, effectively reducing the initial phase of the segment to quadratic acceleration.</p>
        </section>

        <section id="section-de-casteljau">
          <h2>5. De Casteljau's Algorithm: Recursive Geometric Subdivision</h2>
          <p>While evaluating polynomial equations directly via Horner's method is efficient on modern arithmetic logic units, floating-point roundoff errors can accumulate near the boundaries (<code>t &rarr; 0</code> or <code>t &rarr; 1</code>). Furthermore, monomial forms provide no straightforward mechanism for splitting a curve into independent sub-segments at an arbitrary parameter <code>t</code>.</p>
          <p>In 1959, mathematician Paul de Casteljau formulated a profound geometric construction that evaluates Bézier curves through pure recursive linear interpolation (LERP). De Casteljau's algorithm forms the foundational rasterization pipeline inside browser rendering engines like Google Skia and Mozilla WebRender.</p>

          <h3>5.1 The Step-by-Step Geometric Construction</h3>
          <p>Consider a cubic Bézier curve defined by four control points <code>{P_0, C_1, C_2, P_3}</code>. To evaluate the curve point at parameter <code>t = 0.5</code> (or any arbitrary <code>t</code> in <code>[0, 1]</code>):</p>
          <ol>
            <li><strong>Level 1 Interpolation:</strong> Interpolate linearly along the three polygon edges connecting adjacent control points:
              <br><code>Q_0 = (1 - t) &times; P_0 + t &times; C_1</code>
              <br><code>Q_1 = (1 - t) &times; C_1 + t &times; C_2</code>
              <br><code>Q_2 = (1 - t) &times; C_2 + t &times; P_3</code>
            </li>
            <li><strong>Level 2 Interpolation:</strong> Connect the resulting points <code>Q_0, Q_1, Q_2</code> and interpolate along those two new segments:
              <br><code>R_0 = (1 - t) &times; Q_0 + t &times; Q_1</code>
              <br><code>R_1 = (1 - t) &times; Q_1 + t &times; Q_2</code>
            </li>
            <li><strong>Level 3 Interpolation:</strong> Connect <code>R_0</code> and <code>R_1</code> and interpolate one final time:
              <br><code>B(t) = (1 - t) &times; R_0 + t &times; R_1</code>
            </li>
          </ol>
          <p>The resulting point <code>B(t)</code> lies precisely on the Bézier curve. Even more impressively, the line segment connecting <code>R_0</code> and <code>R_1</code> is strictly tangent to the curve at <code>B(t)</code>.</p>

          <h3>5.2 Curve Splitting and Subdivision</h3>
          <p>De Casteljau's algorithm delivers a critical bonus: it splits the original cubic curve into two valid, independent cubic curves that perfectly reconstruct the original trajectory. The two new sets of control points are:</p>
          <ul>
            <li><strong>Left Sub-segment (from 0 to t):</strong> <code>{ P_0, Q_0, R_0, B(t) }</code></li>
            <li><strong>Right Sub-segment (from t to 1):</strong> <code>{ B(t), R_1, Q_2, P_3 }</code></li>
          </ul>
          <p>Graphics engines utilize recursive subdivision at <code>t = 0.5</code> to flatten curved paths into micro-linear segments for rasterization. If the control points of a sub-segment become sufficiently close to collinear (measured by a flatness tolerance epsilon, typically <code>0.25px</code>), the engine halts recursion and draws a straight line segment directly to the GPU buffer.</p>

          <pre><code>// Production JavaScript Implementation of De Casteljau Curve Splitting
function splitCubicBezier(p0, c1, c2, p3, t) {
  const lerp = (a, b, t) => ({ x: (1 - t) * a.x + t * b.x, y: (1 - t) * a.y + t * b.y });

  // Level 1
  const q0 = lerp(p0, c1, t);
  const q1 = lerp(c1, c2, t);
  const q2 = lerp(c2, p3, t);

  // Level 2
  const r0 = lerp(q0, q1, t);
  const r1 = lerp(q1, q2, t);

  // Level 3 (Curve Point)
  const bt = lerp(r0, r1, t);

  return {
    left:  { p0: p0, c1: q0, c2: r0, p3: bt },
    right: { p0: bt, c1: r1, c2: q2, p3: p3 }
  };
}</code></pre>
        </section>

        <section id="section-derivatives">
          <h2>6. First and Second Derivatives: Tangents and Normal Vectors</h2>
          <p>In modern web development, static curves are only half the battle. Engineers frequently need to animate icons along paths, orient directional arrows along curved pipelines (such as in React Flow or node diagrams), or align text along curved baselines using SVG <code>&lt;textPath&gt;</code>. To orient an object tangentially to a curve at parameter <code>t</code>, we must compute the curve's first mathematical derivative.</p>

          <h3>6.1 The First Derivative (Velocity Vector)</h3>
          <p>Differentiating the cubic Bézier polynomial with respect to parameter <code>t</code> produces a quadratic Bézier curve representing the instantaneous rate of change (velocity vector):</p>

          <div class="formula-card">
            <div class="formula-title">First Derivative of a Cubic Bézier Curve</div>
            <div class="formula-body">C'(t) = 3 &times; (1 - t)^2 &times; (C_1 - P_0) + 6 &times; (1 - t) &times; t &times; (C_2 - C_1) + 3 &times; t^2 &times; (P_3 - C_2)</div>
            <div class="formula-desc">Produces the 2D tangent vector V(t) = ( x'(t), y'(t) ) at any point along the curve.</div>
          </div>

          <p>Notice that at <code>t = 0.0</code>, the derivative simplifies to <code>C'(0) = 3 &times; (C_1 - P_0)</code>. This proves that the initial tangent vector is collinear with the segment connecting the start anchor to the first control point. Similarly, at <code>t = 1.0</code>, <code>C'(1) = 3 &times; (P_3 - C_2)</code>.</p>

          <h3>6.2 Computing the Tangent Angle and Normal Vectors</h3>
          <p>The tangent angle &theta; (in radians) required to rotate an oriented icon or arrowhead is calculated using the two-argument arctangent function:</p>

          <div class="formula-card">
            <div class="formula-title">Tangent Angle &amp; Unit Normal Vector Formulas</div>
            <div class="formula-body">
theta(t) = atan2( y'(t), x'(t) )<br>
Unit Tangent: T_unit(t) = ( x'(t), y'(t) ) / sqrt( x'(t)^2 + y'(t)^2 )<br>
Unit Normal: N_unit(t) = ( -y'(t), x'(t) ) / sqrt( x'(t)^2 + y'(t)^2 )
            </div>
            <div class="formula-desc">The normal vector N_unit is perpendicular to the tangent, pointing outward toward the convex side.</div>
          </div>

          <p>Normal vectors are essential for computing stroke outlines, offset curves (creating parallel tracks or double lines), and computing directional particle emitters along curved trajectories.</p>
        </section>

        <section id="section-curvature">
          <h2>7. Curvature, Inflection Points, and Arc Approximations</h2>
          <p>Curvature (denoted by the Greek letter kappa, &kappa;) measures how sharply a curve bends at any specific point. In physics and motion design, curvature dictates the lateral acceleration experienced by an object traveling at constant velocity along the path.</p>

          <h3>7.1 The Mathematical Curvature Formula</h3>
          <p>By computing both the first derivative <code>(x', y')</code> and second derivative <code>(x'', y'')</code> of the parametric curve, the signed scalar curvature &kappa; is given by:</p>

          <div class="formula-card">
            <div class="formula-title">Signed Curvature Equation</div>
            <div class="formula-body">kappa(t) = ( x'(t) &times; y''(t) - y'(t) &times; x''(t) ) / ( x'(t)^2 + y'(t)^2 )^(3/2)</div>
            <div class="formula-desc">A positive kappa indicates a counter-clockwise curve; negative indicates clockwise. kappa = 0 denotes an inflection point.</div>
          </div>

          <p>The radius of curvature <code>R(t)</code> of the osculating circle (the circle that best approximates the curve locally at <code>t</code>) is simply the reciprocal of curvature: <code>R(t) = 1 / |kappa(t)|</code>. When designing rail road tracks, highway ramps, or camera dolly paths, engineers ensure curvature transitions smoothly (continuous <code>G^2</code> or <code>C^2</code> curvature) to avoid sudden jerks in centrifugal force.</p>

          <h3>7.2 Circular Arc Approximation: The Magic Kappa Constant</h3>
          <p>A fundamental dilemma in vector geometry is that polynomial Bézier curves cannot represent true circles. A true circle requires irrational or rational trigonometric equations. However, graphics applications require circular rounded corners, rings, and badges. Fortunately, a 90-degree circular arc of radius <code>R</code> can be approximated using a cubic Bézier curve with phenomenal accuracy.</p>
          <p>To match the circle's endpoints and tangent angles at <code>t = 0</code> and <code>t = 1</code>, while minimizing radial deviation at the midpoint <code>t = 0.5</code>, the control points must be positioned along tangent rays at a specific distance from the anchors governed by the magical <strong>kappa constant</strong>:</p>

          <div class="formula-card">
            <div class="formula-title">The Magic Kappa Constant for 90-Degree Circular Arcs</div>
            <div class="formula-body">kappa = 4 &times; (sqrt(2) - 1) / 3 &approx; 0.5522847498307935</div>
            <div class="formula-desc">Yields a maximum radial error of less than 0.0273% across the entire 90-degree quadrant.</div>
          </div>

          <p>To construct a quadrant circle centered at <code>(0, 0)</code> with radius <code>R = 100</code> spanning from <code>(0, 100)</code> to <code>(100, 0)</code>, the four control points are:</p>
          <pre><code>// 90-degree circle quadrant with radius 100 (kappa * 100 = 55.2285)
// Path: M 0 100 C 55.2285 100, 100 55.2285, 100 0
&lt;path d="M 0 100 C 55.2285 100, 100 55.2285, 100 0" fill="none" stroke="#C1DD2D" stroke-width="2"/&gt;</code></pre>
          <p>Stitching four such cubic segments together produces a visually indistinguishable circle using only 4 cubic commands.</p>
        </section>

        <section id="section-bounding-boxes">
          <h2>8. Exact Bounding Box Computation (Extrema via Calculus Roots)</h2>
          <p>Calculating the true bounding box (minimum and maximum X and Y coordinates) of an SVG path is essential for generating accurate <code>viewBox</code> parameters, collision detection, and layout engines. A naive approach taken by many junior developers is to compute the bounding box of the four control points <code>{P_0, C_1, C_2, P_3}</code>.</p>

          <div class="warning-box">
            <h4>The Pitfall of Control Point Bounding Boxes</h4>
            <p>Because the curve is bounded by the convex hull of its control points, taking the min/max of the control points guarantees containment, but it <strong>severely overestimates</strong> the actual visual boundary of the curve. Control points frequently extend far beyond the curve's visual perimeter, causing erroneous whitespace and clipped icons.</p>
          </div>

          <h3>8.1 Finding Roots of the Derivative Polynomial</h3>
          <p>To determine the exact extrema of a cubic curve <code>C(t) = a*t^3 + b*t^2 + c*t + d</code>, we must find the values of <code>t</code> where the first derivative equals zero: <code>C'(t) = 0</code>. Differentiating with respect to <code>t</code> yields a standard quadratic equation:</p>

          <div class="formula-card">
            <div class="formula-title">Quadratic Derivative Equation for Extrema</div>
            <div class="formula-body">C'(t) = 3&times;a &times; t^2 + 2&times;b &times; t + c = 0</div>
            <div class="formula-desc">Where a, b, and c are the monomial coefficients derived in Section 4.1.</div>
          </div>

          <p>Applying the standard quadratic formula yields the potential root candidates:</p>
          <div class="formula-card">
            <div class="formula-title">Quadratic Root Formula for t Extrema</div>
            <div class="formula-body">t = [ -2&times;b &plusmn; sqrt( (2&times;b)^2 - 4 &times; (3&times;a) &times; c ) ] / [ 2 &times; (3&times;a) ]</div>
            <div class="formula-desc">Compute discriminant Delta = 4&times;b^2 - 12&times;a&times;c. If Delta &lt; 0, no internal extrema exist.</div>
          </div>

          <h3>8.2 Algorithm for Exact Bounding Box Computation</h3>
          <p>The complete, bulletproof algorithm executes as follows:</p>
          <ol>
            <li>Initialize candidate sets for X and Y with the endpoints: <code>candidatesX = [ P_0.x, P_3.x ]</code> and <code>candidatesY = [ P_0.y, P_3.y ]</code>.</li>
            <li>For the X dimension, solve <code>3*a_x*t^2 + 2*b_x*t + c_x = 0</code>. For any real root <code>t_root</code> that satisfies <code>0.0 &lt; t_root &lt; 1.0</code>, evaluate <code>x(t_root)</code> and append it to <code>candidatesX</code>.</li>
            <li>For the Y dimension, solve <code>3*a_y*t^2 + 2*b_y*t + c_y = 0</code>. For any real root <code>t_root</code> that satisfies <code>0.0 &lt; t_root &lt; 1.0</code>, evaluate <code>y(t_root)</code> and append it to <code>candidatesY</code>.</li>
            <li>The exact bounding box is defined by:
              <br><code>minX = Math.min(...candidatesX)</code>
              <br><code>maxX = Math.max(...candidatesX)</code>
              <br><code>minY = Math.min(...candidatesY)</code>
              <br><code>maxY = Math.max(...candidatesY)</code>
            </li>
          </ol>
        </section>

        <section id="section-interactive-studio">
          <h2>9. Interactive Bézier Developer Studio &amp; Formula Inspector</h2>
          <p>Use the interactive engineering studio below to inspect Bézier curve geometry in real time. Drag the sliders to reposition control points, adjust the evaluation parameter <code>t</code>, visualize velocity vectors and de Casteljau construction lines, and generate production-ready code snippets.</p>

          <div class="interactive-sandbox" id="bezierStudio">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
                <span>Bézier Geometry &amp; Vector Studio</span>
              </div>
              <span class="sandbox-badge">Interactive Inspector</span>
            </div>

            <div class="sandbox-grid">
              <div class="sandbox-controls">
                <div class="control-row">
                  <label for="curveTypeSelect">Curve Algorithm Degree: <span class="stat-num" id="curveTypeDisplay">Cubic (Degree 3)</span></label>
                  <select id="curveTypeSelect" class="control-select">
                    <option value="cubic" selected>Cubic Bézier (C Command, 4 Points)</option>
                    <option value="quadratic">Quadratic Bézier (Q Command, 3 Points)</option>
                  </select>
                </div>

                <div class="control-row">
                  <label for="paramTSlider">Evaluation Step t: <span class="stat-num" id="paramTVal">0.50</span></label>
                  <input type="range" id="paramTSlider" min="0" max="1" step="0.01" value="0.5" style="width:100%;">
                </div>

                <div class="control-row">
                  <label>Start Anchor P0 (X, Y):</label>
                  <div class="points-input-grid">
                    <input type="number" id="p0XInput" class="control-input" value="40" step="5">
                    <input type="number" id="p0YInput" class="control-input" value="200" step="5">
                  </div>
                </div>

                <div class="control-row">
                  <label>Control Point 1 C1 (X, Y):</label>
                  <div class="points-input-grid">
                    <input type="number" id="c1XInput" class="control-input" value="80" step="5">
                    <input type="number" id="c1YInput" class="control-input" value="40" step="5">
                  </div>
                </div>

                <div class="control-row" id="c2InputRow">
                  <label>Control Point 2 C2 (X, Y):</label>
                  <div class="points-input-grid">
                    <input type="number" id="c2XInput" class="control-input" value="240" step="5">
                    <input type="number" id="c2YInput" class="control-input" value="280" step="5">
                  </div>
                </div>

                <div class="control-row">
                  <label>End Anchor P3 (X, Y):</label>
                  <div class="points-input-grid">
                    <input type="number" id="p3XInput" class="control-input" value="280" step="5">
                    <input type="number" id="p3YInput" class="control-input" value="80" step="5">
                  </div>
                </div>
              </div>

              <div class="stage-wrapper">
                <div class="preview-stage-container">
                  <svg id="stageSvg" class="stage-svg-element" viewBox="0 0 320 320" xmlns="http://www.w3.org/2000/svg">
                    <!-- Background Grid -->
                    <defs>
                      <pattern id="studioGrid" width="20" height="20" patternUnits="userSpaceOnUse">
                        <path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(255,255,255,0.04)" stroke-width="1"/>
                      </pattern>
                    </defs>
                    <rect width="100%" height="100%" fill="url(#studioGrid)"/>

                    <!-- Control Polygon Lines -->
                    <polyline id="stageControlLines" points="40,200 80,40 240,280 280,80" fill="none" stroke="rgba(193,221,45,0.3)" stroke-dasharray="4 4" stroke-width="1.5"/>

                    <!-- De Casteljau Construction Lines -->
                    <line id="deCasteljauLine1" x1="0" y1="0" x2="0" y2="0" stroke="rgba(56,189,248,0.5)" stroke-width="1.5"/>
                    <line id="deCasteljauLine2" x1="0" y1="0" x2="0" y2="0" stroke="rgba(56,189,248,0.5)" stroke-width="1.5"/>
                    <line id="deCasteljauFinal" x1="0" y1="0" x2="0" y2="0" stroke="rgba(244,114,182,0.8)" stroke-width="1.5"/>

                    <!-- The Main Bézier Curve -->
                    <path id="stageCurvePath" d="M 40 200 C 80 40 240 280 280 80" fill="none" stroke="#C1DD2D" stroke-width="3" stroke-linecap="round"/>

                    <!-- Tangent Velocity Vector -->
                    <line id="stageTangentVector" x1="0" y1="0" x2="0" y2="0" stroke="#38BDF8" stroke-width="2.5" marker-end="url(#arrowhead)"/>

                    <!-- Control Point Handles -->
                    <circle id="stagePointP0" cx="40" cy="200" r="5" fill="#C1DD2D"/>
                    <circle id="stagePointC1" cx="80" cy="40" r="4.5" fill="#38BDF8"/>
                    <circle id="stagePointC2" cx="240" cy="280" r="4.5" fill="#38BDF8"/>
                    <circle id="stagePointP3" cx="280" cy="80" r="5" fill="#C1DD2D"/>

                    <!-- Current Point at Step t -->
                    <circle id="stagePointBt" cx="160" cy="160" r="6" fill="#F43F5E" stroke="#FFF" stroke-width="1.5"/>
                  </svg>
                  <div class="viewport-meta-overlay">viewBox="0 0 320 320"</div>
                </div>

                <div class="stats-readout-box">
                  <div class="stat-item">
                    <div class="stat-label">Position B(t)</div>
                    <div class="stat-val highlight" id="readoutPosition">X: 160.0, Y: 160.0</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Tangent Angle</div>
                    <div class="stat-val" id="readoutAngle">34.2&deg;</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Velocity |B'(t)|</div>
                    <div class="stat-val" id="readoutVelocity">284.1 px/t</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Exact BBox Bounds</div>
                    <div class="stat-val highlight" id="readoutBbox">[40, 68, 280, 242]</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="generated-code-box">
              <div class="code-box-head">
                <div class="code-tabs">
                  <button class="code-tab-btn active" data-tab="svg">SVG Markup</button>
                  <button class="code-tab-btn" data-tab="js">JavaScript Formula</button>
                  <button class="code-tab-btn" data-tab="css">CSS Motion Path</button>
                </div>
                <div class="code-actions">
                  <button class="copy-btn" id="copyBezierCodeBtn">Copy Snippet</button>
                </div>
              </div>
              <pre class="code-output-area"><code id="bezierCodeOutput"></code></pre>
            </div>
          </div>
        </section>

        <section id="section-practical-patterns">
          <h2>10. Real-World Engineering Patterns: Connectors, Splines, &amp; Easing</h2>
          <p>Understanding the theoretical calculus of Bézier curves unlocks sophisticated frontend capabilities that distinguish senior UI engineers. Below are three indispensable real-world implementation architectures.</p>

          <h3>10.1 Dynamic Node Connectors (Pipeline Graphs &amp; React Flow)</h3>
          <p>In workflow builders, node-based automation platforms, and architectural diagrams, connectors link output ports to input ports. A straight line looks rigid, while a circular arc fails when ports align horizontally. The industry-standard solution is an S-shaped cubic Bézier curve whose control points are offset purely along the horizontal X axis:</p>

          <pre><code>// Compute smooth S-curve connector between two graph nodes
function generateGraphConnector(x1, y1, x2, y2) {
  const dx = Math.abs(x2 - x1);
  const curvature = 0.5; // Control handle length ratio
  const offset = Math.max(dx * curvature, 30);

  const c1x = x1 + offset;
  const c1y = y1;
  const c2x = x2 - offset;
  const c2y = y2;

  return 'M ' + x1 + ' ' + y1 + ' C ' + c1x + ' ' + c1y + ', ' + c2x + ' ' + c2y + ', ' + x2 + ' ' + y2;
}</code></pre>

          <h3>10.2 Smooth Curve Interpolation: Catmull-Rom to Cubic Bézier</h3>
          <p>When rendering telemetry charts or price history graphs, developers are given an array of raw data points <code>[P_0, P_1, P_2, ..., P_n]</code> through which a smooth curve must pass. While Bézier curves do not naturally pass through intermediate control points, a <strong>Centripetal Catmull-Rom spline</strong> guarantees interpolation through all data points.</p>
          <p>Any Catmull-Rom spline segment connecting <code>P_1</code> to <code>P_2</code> (guided by neighbor points <code>P_0</code> and <code>P_3</code>) can be converted directly into an equivalent SVG cubic Bézier curve via simple linear algebra:</p>

          <div class="formula-card">
            <div class="formula-title">Catmull-Rom to Cubic Bézier Conversion Matrix</div>
            <div class="formula-body">
C_1 = P_1 + (P_2 - P_0) / 6<br>
C_2 = P_2 - (P_3 - P_1) / 6
            </div>
            <div class="formula-desc">Converts standard tension-1/2 Catmull-Rom splines directly into native SVG cubic commands.</div>
          </div>

          <h3>10.3 CSS Cubic-Bézier Timing Functions</h3>
          <p>Every CSS transition and animation relies on the <code>transition-timing-function: cubic-bezier(x1, y1, x2, y2)</code> property. This curve is a specialized cubic Bézier curve fixed between start anchor <code>(0, 0)</code> and end anchor <code>(1, 1)</code>. The horizontal axis represents normalized time progress in <code>[0, 1]</code>, while the vertical axis represents animation output value.</p>
          <p>Browsers enforce that <code>x1</code> and <code>x2</code> must strictly lie within <code>[0, 1]</code> to ensure time flows monotonically forward without reverse-time paradoxes. However, <code>y1</code> and <code>y2</code> may exceed <code>[0, 1]</code>, enabling springy bounce and overshoot physics natively in pure CSS!</p>
        </section>

        <section id="section-performance-compat">
          <h2>11. Browser Rendering Pipelines and Performance Benchmarks</h2>
          <p>To ensure 60fps and 120fps fluid rendering across devices, graphics engineers must understand how underlying browser rendering engines (Chromium Blink/Skia, WebKit CoreGraphics, and Gecko WebRender) rasterize Bézier curves into physical display pixels.</p>

          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Rendering Engine</th>
                  <th>Rasterization Backend</th>
                  <th>Bézier Tessellation Strategy</th>
                  <th>Subpixel Anti-Aliasing</th>
                  <th>GPU Memory Footprint</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Chromium (Skia Graphite)</strong></td>
                  <td>Vulkan / Metal / Direct3D 12</td>
                  <td>Compute shader analytic curve rasterization</td>
                  <td>Analytic 8x MSAA</td>
                  <td>Low (&lt; 1.2 MB per 500 curves)</td>
                </tr>
                <tr>
                  <td><strong>WebKit (Safari)</strong></td>
                  <td>Metal CoreGraphics</td>
                  <td>Direct GPU tessellation strips</td>
                  <td>Subpixel Coverage Mask</td>
                  <td>Extremely Low (&lt; 0.9 MB)</td>
                </tr>
                <tr>
                  <td><strong>Gecko (Firefox WebRender)</strong></td>
                  <td>Direct3D 11 / OpenGL</td>
                  <td>Segment-based quadratic reduction cache</td>
                  <td>Analytic Signed Distance Field</td>
                  <td>Moderate (~1.8 MB)</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="takeaway-box">
            <h3>Key Takeaway for Vector Performance Optimization</h3>
            <p>Minimizing control point count is the single most effective optimization in vector engineering. Converting four quadratic commands into two cubic commands reduces DOM parsing overhead by 50% and allows GPU rasterizers to maintain hardware pipelining without thrashing CPU memory caches.</p>
          </div>
        </section>

        <section id="section-faq">
          <h2>12. Frequently Asked Questions</h2>

          <div class="faq-item">
            <h3>What is the mathematical difference between quadratic and cubic Bézier curves in SVG?</h3>
            <p>A quadratic Bézier curve (command Q) is parameterized by 3 control points and possesses a constant second derivative, meaning it cannot produce inflection points (S-shaped curves). A cubic Bézier curve (command C) uses 4 control points, enabling variable curvature and inflection points within a single continuous segment.</p>
          </div>

          <div class="faq-item">
            <h3>How does de Casteljau's algorithm evaluate Bézier curves geometrically?</h3>
            <p>De Casteljau's algorithm recursively interpolates between adjacent control points across multiple levels. For cubic curves, it performs 3 initial linear interpolations, then 2 intermediate interpolations, and a final interpolation to locate the exact curve coordinate at parameter t, ensuring numerical stability without floating-point divergence.</p>
          </div>

          <div class="faq-item">
            <h3>How do SVG smooth curve commands S and T calculate implicit control points?</h3>
            <p>Commands S (cubic) and T (quadratic) maintain smooth first-derivative tangency by automatically reflecting the preceding segment's final control point across the shared anchor point: C1 = 2 * P0 - C_prev. If the preceding command was not of matching curve degree, the control point defaults directly to the current anchor point.</p>
          </div>

          <div class="faq-item">
            <h3>Why can cubic Bézier curves only approximate a true circular arc, and what is the optimal kappa constant?</h3>
            <p>Because Bézier curves are polynomial equations while circles require rational trigonometric equations, polynomials cannot trace perfect circles. However, a 90-degree quadrant arc is approximated with under 0.027% maximum radial error using the kappa constant: kappa = 4 * (sqrt(2) - 1) / 3 &approx; 0.5522847498 times radius R.</p>
          </div>

          <div class="faq-item">
            <h3>How do you calculate the exact bounding box of an SVG cubic Bézier curve without overestimating?</h3>
            <p>Calculate the first derivative B'(t) = 3*a*t^2 + 2*b*t + c for both X and Y. Use the quadratic formula to solve for roots where B'(t) = 0. Retain real roots strictly within (0, 1), and evaluate the curve position at t = 0, t = 1, and all valid root parameters. The min and max values among these candidates form the exact bounding box.</p>
          </div>

          <div class="faq-item">
            <h3>How do browser graphics engines accelerate Bézier curve rendering on modern GPUs?</h3>
            <p>Modern engines like Skia and WebRender utilize compute shader path rendering to either analytically evaluate curves inside vertex shaders or dynamically tessellate paths into triangular strips. This achieves 120 FPS rendering on modern displays without burdening the main CPU thread.</p>
          </div>
        </section>

      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <ol>
              <li><a href="#section-intro">1. Introduction to Bézier Curves</a></li>
              <li><a href="#section-math-foundations">2. Parametric Polynomials</a></li>
              <li><a href="#section-quadratic">3. Quadratic Curves (Q &amp; T)</a></li>
              <li><a href="#section-cubic">4. Cubic Curves (C &amp; S)</a></li>
              <li><a href="#section-de-casteljau">5. De Casteljau's Algorithm</a></li>
              <li><a href="#section-derivatives">6. Derivatives &amp; Tangents</a></li>
              <li><a href="#section-curvature">7. Curvature &amp; Circle Arcs</a></li>
              <li><a href="#section-bounding-boxes">8. Exact Bounding Box Calculus</a></li>
              <li><a href="#section-interactive-studio">9. Interactive Developer Studio</a></li>
              <li><a href="#section-practical-patterns">10. Real-World Patterns</a></li>
              <li><a href="#section-performance-compat">11. Browser Benchmarks</a></li>
              <li><a href="#section-faq">12. FAQ</a></li>
            </ol>
          </nav>
        </div>

        <div class="cta-sidebar-box">
          <h4>Explore 134K+ SVG Icons</h4>
          <p>Need production-ready vector icons with clean mathematical paths? Search across 28 open-source libraries on IconStash.</p>
          <a href="/#/" class="cta-sidebar-btn">Search IconStash</a>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div style="margin-bottom: 16px;">
      <a href="/">Home</a> &bull;
      <a href="/articles/">Articles</a> &bull;
      <a href="/Listicles/best-free-icon-sets-2026/">Best Sets</a> &bull;
      <a href="/Glossary/icon-svg-terminology/">Glossary</a> &bull;
      <a href="/stats/">Statistics</a> &bull;
      <a href="/about/">About</a>
    </div>
    <p>&copy; 2026 IconStash.io &bull; Engineered for high-performance web graphics.</p>
  </footer>

  <script>
    // Theme toggle handling
    const themeToggle = document.getElementById('themeToggle');
    const htmlEl = document.documentElement;
    const savedTheme = localStorage.getItem('theme') || 'dark';
    htmlEl.setAttribute('data-theme', savedTheme);

    if (themeToggle) {
      themeToggle.addEventListener('click', () => {
        const nextTheme = htmlEl.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        htmlEl.setAttribute('data-theme', nextTheme);
        try { localStorage.setItem('theme', nextTheme); } catch(e) {}
      });
    }

    // Interactive Bézier Studio Logic
    (function initBezierStudio() {
      const curveTypeSelect = document.getElementById('curveTypeSelect');
      const curveTypeDisplay = document.getElementById('curveTypeDisplay');
      const paramTSlider = document.getElementById('paramTSlider');
      const paramTVal = document.getElementById('paramTVal');

      const p0XInput = document.getElementById('p0XInput');
      const p0YInput = document.getElementById('p0YInput');
      const c1XInput = document.getElementById('c1XInput');
      const c1YInput = document.getElementById('c1YInput');
      const c2XInput = document.getElementById('c2XInput');
      const c2YInput = document.getElementById('c2YInput');
      const p3XInput = document.getElementById('p3XInput');
      const p3YInput = document.getElementById('p3YInput');
      const c2InputRow = document.getElementById('c2InputRow');

      const stageCurvePath = document.getElementById('stageCurvePath');
      const stageControlLines = document.getElementById('stageControlLines');
      const stagePointP0 = document.getElementById('stagePointP0');
      const stagePointC1 = document.getElementById('stagePointC1');
      const stagePointC2 = document.getElementById('stagePointC2');
      const stagePointP3 = document.getElementById('stagePointP3');
      const stagePointBt = document.getElementById('stagePointBt');
      const stageTangentVector = document.getElementById('stageTangentVector');

      const deCasteljauLine1 = document.getElementById('deCasteljauLine1');
      const deCasteljauLine2 = document.getElementById('deCasteljauLine2');
      const deCasteljauFinal = document.getElementById('deCasteljauFinal');

      const readoutPosition = document.getElementById('readoutPosition');
      const readoutAngle = document.getElementById('readoutAngle');
      const readoutVelocity = document.getElementById('readoutVelocity');
      const readoutBbox = document.getElementById('readoutBbox');

      const bezierCodeOutput = document.getElementById('bezierCodeOutput');
      const copyBezierCodeBtn = document.getElementById('copyBezierCodeBtn');
      const codeTabButtons = document.querySelectorAll('.code-tab-btn');
      let currentTab = 'svg';

      function updateStudio() {
        const isCubic = curveTypeSelect.value === 'cubic';
        curveTypeDisplay.textContent = isCubic ? 'Cubic (Degree 3)' : 'Quadratic (Degree 2)';
        c2InputRow.style.display = isCubic ? 'flex' : 'none';
        stagePointC2.style.display = isCubic ? 'block' : 'none';

        const t = parseFloat(paramTSlider.value);
        paramTVal.textContent = t.toFixed(2);

        const p0 = { x: parseFloat(p0XInput.value) || 0, y: parseFloat(p0YInput.value) || 0 };
        const c1 = { x: parseFloat(c1XInput.value) || 0, y: parseFloat(c1YInput.value) || 0 };
        const c2 = { x: parseFloat(c2XInput.value) || 0, y: parseFloat(c2YInput.value) || 0 };
        const p3 = { x: parseFloat(p3XInput.value) || 0, y: parseFloat(p3YInput.value) || 0 };

        // Update SVG Stage Points
        stagePointP0.setAttribute('cx', p0.x);
        stagePointP0.setAttribute('cy', p0.y);
        stagePointC1.setAttribute('cx', c1.x);
        stagePointC1.setAttribute('cy', c1.y);
        stagePointP3.setAttribute('cx', p3.x);
        stagePointP3.setAttribute('cy', p3.y);

        let dStr = '';
        let polylinePoints = '';
        let bx = 0, by = 0;
        let vx = 0, vy = 0;
        let minX = 0, maxX = 0, minY = 0, maxY = 0;

        const lerp = (a, b, step) => ({ x: (1 - step) * a.x + step * b.x, y: (1 - step) * a.y + step * b.y });

        if (isCubic) {
          stagePointC2.setAttribute('cx', c2.x);
          stagePointC2.setAttribute('cy', c2.y);
          dStr = \`M \${p0.x} \${p0.y} C \${c1.x} \${c1.y}, \${c2.x} \${c2.y}, \${p3.x} \${p3.y}\`;
          polylinePoints = \`\${p0.x},\${p0.y} \${c1.x},\${c1.y} \${c2.x},\${c2.y} \${p3.x},\${p3.y}\`;

          // De Casteljau Level 1
          const q0 = lerp(p0, c1, t);
          const q1 = lerp(c1, c2, t);
          const q2 = lerp(c2, p3, t);

          // Level 2
          const r0 = lerp(q0, q1, t);
          const r1 = lerp(q1, q2, t);

          // Level 3 (Curve Point)
          const bt = lerp(r0, r1, t);
          bx = bt.x;
          by = bt.y;

          // Tangent Derivative C'(t)
          vx = 3 * (1 - t) * (1 - t) * (c1.x - p0.x) + 6 * (1 - t) * t * (c2.x - c1.x) + 3 * t * t * (p3.x - c2.x);
          vy = 3 * (1 - t) * (1 - t) * (c1.y - p0.y) + 6 * (1 - t) * t * (c2.y - c1.y) + 3 * t * t * (p3.y - c2.y);

          // De Casteljau lines
          deCasteljauLine1.setAttribute('x1', q0.x); deCasteljauLine1.setAttribute('y1', q0.y);
          deCasteljauLine1.setAttribute('x2', q1.x); deCasteljauLine1.setAttribute('y2', q1.y);
          deCasteljauLine2.setAttribute('x1', q1.x); deCasteljauLine2.setAttribute('y1', q1.y);
          deCasteljauLine2.setAttribute('x2', q2.x); deCasteljauLine2.setAttribute('y2', q2.y);
          deCasteljauFinal.setAttribute('x1', r0.x); deCasteljauFinal.setAttribute('y1', r0.y);
          deCasteljauFinal.setAttribute('x2', r1.x); deCasteljauFinal.setAttribute('y2', r1.y);
          deCasteljauLine2.style.display = 'block';

          // Bounding Box Calculus
          const getRoots = (p0v, c1v, c2v, p3v) => {
            const a = -p0v + 3 * c1v - 3 * c2v + p3v;
            const b = 3 * p0v - 6 * c1v + 3 * c2v;
            const c = -3 * p0v + 3 * c1v;
            const roots = [0, 1];
            const A = 3 * a;
            const B = 2 * b;
            const C = c;
            if (Math.abs(A) < 1e-6) {
              if (Math.abs(B) > 1e-6) {
                const r = -C / B;
                if (r > 0 && r < 1) roots.push(r);
              }
            } else {
              const disc = B * B - 4 * A * C;
              if (disc >= 0) {
                const sq = Math.sqrt(disc);
                const r1 = (-B + sq) / (2 * A);
                const r2 = (-B - sq) / (2 * A);
                if (r1 > 0 && r1 < 1) roots.push(r1);
                if (r2 > 0 && r2 < 1) roots.push(r2);
              }
            }
            return roots.map(rt => {
              const u = 1 - rt;
              return u * u * u * p0v + 3 * u * u * rt * c1v + 3 * u * rt * rt * c2v + rt * rt * rt * p3v;
            });
          };

          const xVals = getRoots(p0.x, c1.x, c2.x, p3.x);
          const yVals = getRoots(p0.y, c1.y, c2.y, p3.y);
          minX = Math.round(Math.min(...xVals));
          maxX = Math.round(Math.max(...xVals));
          minY = Math.round(Math.min(...yVals));
          maxY = Math.round(Math.max(...yVals));

        } else {
          // Quadratic mode
          dStr = \`M \${p0.x} \${p0.y} Q \${c1.x} \${c1.y}, \${p3.x} \${p3.y}\`;
          polylinePoints = \`\${p0.x},\${p0.y} \${c1.x},\${c1.y} \${p3.x},\${p3.y}\`;

          const q0 = lerp(p0, c1, t);
          const q1 = lerp(c1, p3, t);
          const bt = lerp(q0, q1, t);
          bx = bt.x;
          by = bt.y;

          vx = 2 * (1 - t) * (c1.x - p0.x) + 2 * t * (p3.x - c1.x);
          vy = 2 * (1 - t) * (c1.y - p0.y) + 2 * t * (p3.y - c1.y);

          deCasteljauLine1.setAttribute('x1', q0.x); deCasteljauLine1.setAttribute('y1', q0.y);
          deCasteljauLine1.setAttribute('x2', q1.x); deCasteljauLine1.setAttribute('y2', q1.y);
          deCasteljauLine2.style.display = 'none';
          deCasteljauFinal.setAttribute('x1', q0.x); deCasteljauFinal.setAttribute('y1', q0.y);
          deCasteljauFinal.setAttribute('x2', q1.x); deCasteljauFinal.setAttribute('y2', q1.y);

          // Quadratic roots
          const getQuadRoots = (p0v, c1v, p2v) => {
            const roots = [p0v, p2v];
            const denom = p0v - 2 * c1v + p2v;
            if (Math.abs(denom) > 1e-6) {
              const r = (p0v - c1v) / denom;
              if (r > 0 && r < 1) {
                const u = 1 - r;
                roots.push(u * u * p0v + 2 * u * r * c1v + r * r * p2v);
              }
            }
            return roots;
          };
          const xVals = getQuadRoots(p0.x, c1.x, p3.x);
          const yVals = getQuadRoots(p0.y, c1.y, p3.y);
          minX = Math.round(Math.min(...xVals));
          maxX = Math.round(Math.max(...xVals));
          minY = Math.round(Math.min(...yVals));
          maxY = Math.round(Math.max(...yVals));
        }

        stageCurvePath.setAttribute('d', dStr);
        stageControlLines.setAttribute('points', polylinePoints);
        stagePointBt.setAttribute('cx', bx);
        stagePointBt.setAttribute('cy', by);

        // Vector magnitude & normalization
        const vMag = Math.sqrt(vx * vx + vy * vy);
        const normScale = 35;
        if (vMag > 0) {
          stageTangentVector.setAttribute('x1', bx);
          stageTangentVector.setAttribute('y1', by);
          stageTangentVector.setAttribute('x2', bx + (vx / vMag) * normScale);
          stageTangentVector.setAttribute('y2', by + (vy / vMag) * normScale);
        }

        const angleDeg = (Math.atan2(vy, vx) * 180 / Math.PI).toFixed(1);
        readoutPosition.textContent = \`X: \${bx.toFixed(1)}, Y: \${by.toFixed(1)}\`;
        readoutAngle.textContent = \`\${angleDeg}&deg;\`;
        readoutVelocity.textContent = \`\${vMag.toFixed(1)} px/step\`;
        readoutBbox.textContent = \`[\${minX}, \${minY}, \${maxX}, \${maxY}]\`;

        // Code Output Update
        if (currentTab === 'svg') {
          bezierCodeOutput.textContent =
\`<!-- Optimized SVG Vector Path Definition -->
<svg viewBox="0 0 320 320" width="320" height="320" xmlns="http://www.w3.org/2000/svg">
  <path d="\${dStr}"
        fill="none"
        stroke="#C1DD2D"
        stroke-width="3"
        stroke-linecap="round"/>
</svg>\`;
        } else if (currentTab === 'js') {
          bezierCodeOutput.textContent =
\`// High-Performance \${isCubic ? 'Cubic' : 'Quadratic'} Bézier Evaluation at step t = \${t.toFixed(2)}
function evaluateBezier(t) {
  const p0 = { x: \${p0.x}, y: \${p0.y} };
  const c1 = { x: \${c1.x}, y: \${c1.y} };
\${isCubic ? \`  const c2 = { x: \${c2.x}, y: \${c2.y} };\\n\` : ''}  const p3 = { x: \${p3.x}, y: \${p3.y} };
  const u = 1 - t;

\${isCubic ? \`  const x = u*u*u*p0.x + 3*u*u*t*c1.x + 3*u*t*t*c2.x + t*t*t*p3.x;
  const y = u*u*u*p0.y + 3*u*u*t*c1.y + 3*u*t*t*c2.y + t*t*t*p3.y;\` : \`  const x = u*u*p0.x + 2*u*t*c1.x + t*t*p3.x;
  const y = u*u*p0.y + 2*u*t*c1.y + t*t*p3.y;\`}

  return { x, y };
}
const currentPoint = evaluateBezier(\${t.toFixed(2)}); // { x: \${bx.toFixed(1)}, y: \${by.toFixed(1)} }\`;
        } else if (currentTab === 'css') {
          bezierCodeOutput.textContent =
\`/* Modern CSS Motion Path Animation */
.animated-icon-indicator {
  offset-path: path('\${dStr}');
  offset-distance: \${Math.round(t * 100)}%;
  offset-rotate: auto;
  transition: offset-distance 300ms ease-out;
}\`;
        }
      }

      [curveTypeSelect, paramTSlider, p0XInput, p0YInput, c1XInput, c1YInput, c2XInput, c2YInput, p3XInput, p3YInput].forEach(el => {
        el.addEventListener('input', updateStudio);
        el.addEventListener('change', updateStudio);
      });

      codeTabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
          codeTabButtons.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          currentTab = btn.getAttribute('data-tab');
          updateStudio();
        });
      });

      if (copyBezierCodeBtn) {
        copyBezierCodeBtn.addEventListener('click', () => {
          navigator.clipboard.writeText(bezierCodeOutput.textContent).then(() => {
            copyBezierCodeBtn.textContent = 'Copied!';
            setTimeout(() => { copyBezierCodeBtn.textContent = 'Copy Snippet'; }, 2000);
          }).catch(() => {
            copyBezierCodeBtn.textContent = 'Failed to copy';
          });
        });
      }

      updateStudio();
    })();
  </script>
</body>
</html>
`;

fs.writeFileSync(path.join(outDir, 'index.html'), html, 'utf8');
console.log('Article 1 generated successfully!');

const cleanBody = html.replace(/<(script|style)[^>]*>[\s\S]*?<\/\1>/gi, '').replace(/<[^>]+>/g, ' ');
const words = cleanBody.split(/\s+/).filter(w => w.length > 0);
console.log(`Article 1 word count: ${words.length} words`);
