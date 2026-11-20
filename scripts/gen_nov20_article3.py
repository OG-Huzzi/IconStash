import os
import re

slug = "svg-parallel-coordinates-and-multivariate-axis-visualization-guide"
target_dir = os.path.join(r"D:\Project IconStash\IconStash\articles", slug)
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

html_content = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mastering SVG Parallel Coordinates: High-Dimensional Geometry, Axis Normalization &amp; Dynamic Range Brushing (2026) | IconStash</title>
  <meta name="description" content="Master SVG parallel coordinates: dynamic axis normalization, multi-dimensional polyline projections, invertible axis scales, and interactive range brushing.">
  <meta name="keywords" content="svg parallel coordinates, multivariate visualization svg, high dimensional data visualization, parallel axis plot, d3 parallel coordinates svg, multi-dimensional filtering brush, interactive parallel coordinates javascript">
  <meta property="og:title" content="Mastering SVG Parallel Coordinates: High-Dimensional Geometry, Axis Normalization &amp; Dynamic Range Brushing (2026)">
  <meta property="og:description" content="Master SVG parallel coordinates: dynamic axis normalization, multi-dimensional polyline projections, invertible axis scales, and interactive range brushing.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-20T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-20T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="High-Dimensional Visualizations">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="Parallel Coordinates">
  <meta property="article:tag" content="Multivariate Analysis">
  <meta property="article:tag" content="Data Visualization">
  <meta property="article:tag" content="Mathematics">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mastering SVG Parallel Coordinates: High-Dimensional Geometry, Axis Normalization &amp; Dynamic Range Brushing (2026)">
  <meta name="twitter:description" content="Master SVG parallel coordinates: dynamic axis normalization, multi-dimensional polyline projections, invertible axis scales, and interactive range brushing.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/">
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
      "headline": "Mastering SVG Parallel Coordinates: High-Dimensional Geometry, Axis Normalization & Dynamic Range Brushing (2026)",
      "description": "Master SVG parallel coordinates: dynamic axis normalization, multi-dimensional polyline projections, invertible axis scales, and interactive range brushing.",
      "image": "https://iconstash.io/assets/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide.jpg",
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
      "datePublished": "2026-11-20",
      "dateModified": "2026-11-20",
      "mainEntityOfPage": "https://iconstash.io/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/",
      "inLanguage": "en-US",
      "wordCount": 4710,
      "articleSection": "High-Dimensional Visualizations",
      "keywords": [
        "svg parallel coordinates",
        "multivariate visualization svg",
        "high dimensional data visualization",
        "parallel axis plot",
        "d3 parallel coordinates svg",
        "multi-dimensional filtering brush",
        "interactive parallel coordinates javascript"
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
          "name": "SVG Parallel Coordinates Guide",
          "item": "https://iconstash.io/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is Alfred Inselberg's point-line projective duality in parallel coordinates?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Alfred Inselberg established that parallel coordinates represent a projective geometric transformation between Cartesian coordinate space and parallel axis space. In standard Cartesian 2D coordinates, an observation is represented as a point (x, y), while a linear relationship is represented as a line y = mx + b. In parallel coordinate space, this geometry is dualized: an N-dimensional data point is transformed into a continuous polygonal line (polyline) that intersects N equidistant vertical parallel axes. Conversely, a line in Cartesian space maps to a single pencil point of intersection between the two adjacent parallel axes. A negative correlation manifests as a sharp crossover intersection between axes, while a positive correlation produces parallel, non-intersecting bundles."
          }
        },
        {
          "@type": "Question",
          "name": "How does dynamic min-max normalization project heterogeneous metrics onto identical vertical pixel spans?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Because high-dimensional datasets combine metrics with wildly disparate physical units and numerical scales—such as server latency (10 to 500 ms), CPU utilization (0% to 100%), and database memory allocation (512 to 32,768 MB)—they cannot share a single vertical axis. Dynamic min-max normalization transforms each raw feature value v_k into a standardized dimensionless ratio u_k between 0.0 and 1.0: u_k = (v_k - min_k) / (max_k - min_k). In SVG coordinates, this ratio is mapped to vertical screen pixels via Cartesian inversion: y_svg = (height - paddingBottom) - u_k * (height - paddingTop - paddingBottom), ensuring that every variable occupies an identical, balanced visual span."
          }
        },
        {
          "@type": "Question",
          "name": "Why are smooth cubic Bézier splines often preferred over sharp linear polylines in dense plots?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "When visualizing hundreds or thousands of high-dimensional records, linear polylines create severe visual clutter and sharp angular intersections at every vertical axis. Human visual perception struggles to track individual trajectories through dense clusters of jagged lines. Converting polyline vertices into smooth cubic Bézier curves (or Catmull-Rom splines) softens directional changes, improves optical continuity, and aligns with the Gestalt principle of good continuation. Viewers can track individual multivariate records through dense bundles far more effectively, making structural clusters, outliers, and multivariate trajectories immediately discernible."
          }
        },
        {
          "@type": "Question",
          "name": "How does multi-axis range brushing compute conjunction filtering in real time?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Multi-axis range brushing implements a logical conjunction (AND gate) across all brushed dimensions. Each axis k can have an active selection interval [y_low_k, y_high_k]. A record is classified as active if and only if its value on every brushed axis falls strictly within that axis's active interval: Active(record) = product_{k in Brushed} (low_k <= v_k <= high_k). The engine renders active records with vibrant category colors and prominent stroke-widths (1.8px), while inactive records are dimmed to faint gray lines (opacity 0.08). This instantaneous filtering allows analysts to isolate complex multi-dimensional cohorts in sub-millisecond execution times."
          }
        },
        {
          "@type": "Question",
          "name": "How does axis ordering influence multivariate pattern recognition, and how can it be optimized?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In parallel coordinates, pairwise correlations and geometric patterns can only be visually decoded between directly adjacent parallel axes. An N-dimensional dataset features N! possible axis permutations, meaning that poorly ordered axes can hide critical relationships. To maximize pattern discovery, data engineers utilize correlation-clustering algorithms such as hierarchical clustering or maximum spanning tree (MST) Hamiltonian path traversals. By placing variables with high Pearson or Spearman correlation coefficients adjacent to one another, cross-over points and tight bundle patterns become immediately visible."
          }
        },
        {
          "@type": "Question",
          "name": "How do you achieve WCAG 2.2 AA compliance for high-dimensional SVG parallel coordinate charts?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To achieve full WCAG 2.2 AA compliance, the root SVG container must declare role='graphics-document' along with an aria-label and companion title and desc elements describing dataset scope and active filter states. Individual vertical axes declare role='graphics-axis' with accessible numerical tick labels exceeding a 4.5:1 contrast ratio against the background. Interactive brush handles carry keyboard focusability via tabindex='0' and ARIA slider attributes (aria-valuemin, aria-valuemax, aria-valuenow). Furthermore, records must never be differentiated solely by color hue; distinct dash patterns (solid, dashed, dotted) and persistent tabular inspectors must accompany all categorical cluster groupings."
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

    .preview-stage-container { background: #0D0D0D; border: 1px solid #222; border-radius: 8px; padding: 20px; display: flex; justify-content: center; align-items: center; position: relative; min-height: 480px; }
    .parallel-svg-canvas { width: 100%; max-width: 760px; height: auto; touch-action: none; }

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
    .cta-sidebar-box .cta-title, .cta-sidebar-box h4 { font-size: 15px; color: #C1DD2D; margin-bottom: 8px; font-weight: 700; }
    .cta-sidebar-box p { font-size: 13px; color: #BBB; line-height: 1.5; margin-bottom: 12px; }

    .takeaway-box { background: #121212; border: 1px solid #242424; border-radius: 8px; padding: 24px 28px; margin: 36px 0; }
    .takeaway-box h3 { color: #C1DD2D; font-size: 19px; margin-top: 0; margin-bottom: 14px; }
    .takeaway-box ul { margin-bottom: 0; }

    .warning-box { background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-left: 4px solid #EF4444; border-radius: 6px; padding: 18px 22px; margin: 28px 0; }
    .warning-box .warning-title, .warning-box h4 { color: #F87171; font-size: 15px; margin-bottom: 8px; }
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
    html[data-theme="light"] .cta-sidebar-box .cta-title, .cta-sidebar-box h4 { color: #064E3B; }
    html[data-theme="light"] .cta-sidebar-box p { color: #047857; }
    html[data-theme="light"] th { background: #F4F4F5; color: #18181B; border-bottom-color: #E4E4E7; }
    html[data-theme="light"] td { border-bottom-color: #E4E4E7; color: #3F3F46; }
    html[data-theme="light"] .table-container { border-color: #E4E4E7; }
    html[data-theme="light"] .data-table th { background: #F4F4F5; color: #18181B; border-bottom-color: #E4E4E7; }
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
    html[data-theme="light"] .formula-title { color: #4D6300; }
    html[data-theme="light"] .formula-body { color: #18181B; }
    html[data-theme="light"] .formula-desc { color: #525252; }
    html[data-theme="light"] .takeaway-box { background: #F4F4F5; border-color: #E4E4E7; }
    html[data-theme="light"] .takeaway-box h3 { color: #4D6300; }
    html[data-theme="light"] .warning-box { background: #FEF2F2; border-color: #FCA5A5; border-left-color: #EF4444; }
    html[data-theme="light"] .warning-box .warning-title, .warning-box h4 { color: #B91C1C; }
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
    <a href="/" class="logo" aria-label="IconStash Home">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
      <span>IconStash</span>
    </a>
    <nav>
      <a href="/articles/">Articles</a>
      <a href="/about/">About</a>
      <a href="/stats/">Stats</a>
      <button class="theme-toggle-btn" id="theme-toggle" aria-label="Toggle Theme">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
      </button>
      <a href="/articles/" class="header-cta">Browse 129 Guides</a>
    </nav>
  </header>

  <div class="page-container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a>
      <span class="sep">/</span>
      <a href="/articles/">Articles</a>
      <span class="sep">/</span>
      <span class="current">SVG Parallel Coordinates Guide</span>
    </nav>

    <header class="article-hero">
      <span class="tag">High-Dimensional Visualizations</span>
      <h1>Mastering SVG Parallel Coordinates: High-Dimensional Geometry, Axis Normalization &amp; Dynamic Range Brushing (2026)</h1>
      <div class="article-meta">
        <span>By <a href="/about/">Jouni Flemming</a></span>
        <span>&bull;</span>
        <span>Published November 20, 2026</span>
        <span>&bull;</span>
        <span>Reading Time: 26 min</span>
        <span>&bull;</span>
        <span>Zero-Dependency ES6 &amp; SVG</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">

        <div class="featured-summary">
          <p><strong>Executive Architectural Overview:</strong> High-dimensional data spaces—such as deep learning hyperparameter optimization manifolds, multi-sensor industrial telemetry, genomics feature spaces, and microservice infrastructure clusters—routinely exceed the 3D perceptual limits of human vision. While projection algorithms like t-SNE, UMAP, and PCA compress high-dimensional records into 2D scatter plots, they irreversibly destroy physical units, distort topological distances, and obscure multi-metric thresholds. SVG parallel coordinates solve this challenge by mapping N orthogonal mathematical dimensions onto N parallel, equidistant coordinate axes.</p>
          <ul>
            <li><strong>Inselberg Point-Line Projective Duality:</strong> Rigorous geometric transformation mapping high-dimensional observations to continuous polyline trajectories while dualizing Cartesian relationships into intersection pencils.</li>
            <li><strong>Heterogeneous Dynamic Normalization:</strong> Per-axis min-max scaling mapping disparate physical units (milliseconds, percentages, megabytes) into unified 0-to-1 vertical pixel viewports.</li>
            <li><strong>Cubic Bézier Spline Bundling:</strong> Converting jagged piecewise polylines into smooth continuous curves, softening angular clutter and revealing dense cluster bundles.</li>
            <li><strong>Sub-Millisecond Range Brushing:</strong> Real-time multi-axis logical conjunction filtering (AND gating) enabling operators to isolate complex multivariate cohorts instantaneously.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide.jpg" alt="Dark theme developer studio monitor displaying glowing neon green and cyan SVG parallel coordinate plots with multiple parallel vertical axes and brushed polyline selections" width="1200" height="675" fetchpriority="high" decoding="async">
          <figcaption>Figure 1: High-precision SVG Parallel Coordinates visualization studio rendering multivariate vertical axes, dynamic range brush filters, and glowing cluster polyline trajectories.</figcaption>
        </figure>

        <section id="section-foundations">
          <h2>1. Dimensionality Transformation: Inselberg's Point-Line Duality &amp; Geometric Foundations</h2>
          <p>The fundamental challenge of exploratory multivariate analysis is the curse of dimensionality. Standard Cartesian coordinate systems rely on mutually orthogonal axes: two dimensions are represented as perpendicular X and Y axes, while three dimensions introduce a depth Z axis. Beyond three dimensions, physical Euclidean space cannot accommodate additional mutually orthogonal axes without resorting to non-Euclidean mathematics. For decades, data analysts relied on Scatter Plot Matrices (SPLOMs), which arrange all pairwise combinations of variables into a grid of \( N \times (N - 1) / 2 \) scatter plots. However, SPLOMs fragment high-dimensional records into disconnected 2D slices, forcing analysts to manually stitch mental relationships across dozens of separate sub-plots.</p>
          <p>Introduced by mathematician Alfred Inselberg in 1985 and popularized across computational geometry and scientific visualization, parallel coordinates bypass the orthogonal constraint entirely. Rather than placing axes at right angles, parallel coordinates align \( K \) dimensions as parallel, equidistant vertical lines: \( X_0, X_1, \dots, X_{K-1} \). A single \( K \)-dimensional observation vector \( \mathbf{v} = (v_0, v_1, \dots, v_{K-1}) \) is mapped to a continuous polygonal path (polyline) that intersects each vertical axis \( X_k \) at a height proportional to its scalar value \( v_k \).</p>
          <p>Inselberg established that parallel coordinates exhibit profound projective geometric duality with Cartesian space. In Cartesian 2D coordinates, an observation is represented as a point \( (x, y) \), while a linear relationship is represented as a line \( y = mx + b \). In parallel coordinate space, this geometry is dualized: a single data point becomes a continuous line, while a linear relationship between two variables maps to a single pencil point of intersection between the two adjacent parallel axes. A strong negative correlation manifests as a dense cross-over intersection point between axes, while a strong positive correlation manifests as parallel, non-intersecting bundles of lines.</p>
          <p>Implementing parallel coordinates in native SVG provides unique engineering advantages. Because each multivariate record is declared as an individual <code>&lt;polyline&gt;</code> or <code>&lt;path&gt;</code> element, developers can apply hardware-accelerated CSS styling, dynamic opacity fading, and localized event handling. When coupled with native SVG clipPaths and interactive SVG slider components, web applications achieve high-performance interactive visual exploration of complex multivariate systems without heavy third-party charting libraries.</p>
        </section>

        <section id="section-normalization">
          <h2>2. Dynamic Axis Normalization, Scaling Schemes &amp; Invertible Axis Orientations</h2>
          <p>In real-world engineering telemetry, metrics rarely share identical physical scales. A single server telemetry record might contain CPU Utilization (0% to 100%), Memory Allocation (512 MB to 65,536 MB), Response Latency (5 ms to 2,500 ms), Disk I/O Operations (0 to 15,000 IOPS), and Error Rate (0.00% to 5.00%). Attempting to plot these raw values on a shared vertical scale would compress small-scale metrics into flat, invisible baselines while allowing large metrics to explode beyond canvas boundaries.</p>

          <div class="formula-card">
            <div class="formula-title">Dynamic Per-Axis Min-Max Normalization</div>
            <div class="formula-body">
              u_k(v) = (v - Min_k) / (Max_k - Min_k)<br>
              Y_{svg, k}(v) = (H - PadBottom) - u_k(v) * (H - PadTop - PadBottom)
            </div>
            <div class="formula-desc">Where Min_k and Max_k represent the statistical domain bounds for axis k, and H is the total SVG viewport height. Cartesian inversion guarantees that higher metric values rise toward the top margin.</div>
          </div>

          <p>Production parallel coordinate architectures support three vital scaling enhancements:</p>
          <ul>
            <li><strong>1. Logarithmic Axis Scaling:</strong> For metrics exhibiting multi-order-of-magnitude power-law distributions (such as network latency or request counts), standard linear normalization squashes 95% of data into the bottom 10% of the axis. Applying logarithmic normalization \( u_k(v) = (\ln(v) - \ln(\text{Min}_k)) / (\ln(\text{Max}_k) - \ln(\text{Min}_k)) \) reveals nuanced variance across both low-magnitude baselines and high-magnitude spikes.</li>
            <li><strong>2. Invertible Axis Orientation:</strong> By default, higher metric values ascend toward the top margin. However, in many operational workflows, metrics possess opposing optimization polarities: higher Throughput is desirable, whereas higher Latency is detrimental. Supporting clickable axis inversion allows operators to flip individual axes (mapping 0 to top and Max to bottom). Flipping an axis transforms negative correlations into positive parallel bundles, drastically improving optical readability.</li>
            <li><strong>3. Dynamic Margin Padding &amp; Axis Ticks:</strong> Each vertical axis line <code>&lt;line&gt;</code> is augmented with horizontal tick marks and high-contrast numerical labels at 0%, 25%, 50%, 75%, and 100% of its domain. These labels must display real physical units rather than normalized percentages, ensuring absolute clarity for domain specialists.</li>
          </ul>
        </section>

        <section id="section-spline-smoothing">
          <h2>3. Polyline Trajectories vs Smooth Cubic Splines: Mitigating Visual Clutter &amp; Overplotting</h2>
          <p>In naive parallel coordinate plots, every record is rendered as an angular piecewise polyline: <code>&lt;polyline points="x0,y0 x1,y1 x2,y2 ..."&gt;</code>. While computationally trivial, linear polylines suffer from severe visual overplotting when datasets exceed a few hundred records. Sharp angular turns at vertical axes create visual harshness, and overlapping lines create dense web-like clutter that obscures underlying cluster geometries.</p>

          <h3>Catmull-Rom &amp; Cubic Bézier Trajectory Smoothing</h3>
          <p>To enhance perceptual continuity, modern vector systems convert polyline vertices into smooth continuous curves using cubic Bézier splines. According to the Gestalt principle of good continuation, the human visual system tracks continuous, gentle curves through dense visual intersections far more easily than sharp, broken angles. Smoothing softens the abrupt direction changes at vertical axes, allowing analysts to follow individual records across the entire horizontal span of the visualization.</p>

          <pre><code>// Converting Parallel Coordinate Vertices to Smooth SVG Cubic Spline Path
function buildSmoothParallelPathD(coords) {
  if (coords.length &lt; 2) return '';
  let d = `M ${coords[0].x.toFixed(1)} ${coords[0].y.toFixed(1)}`;
  for (let i = 0; i &lt; coords.length - 1; i++) {
    const p1 = coords[i];
    const p2 = coords[i + 1];
    // Place control points horizontally halfway between adjacent axes
    const midX = (p1.x + p2.x) / 2;
    d += ` C ${midX.toFixed(1)} ${p1.y.toFixed(1)}, ${midX.toFixed(1)} ${p2.y.toFixed(1)}, ${p2.x.toFixed(1)} ${p2.y.toFixed(1)}`;
  }
  return d;
}</code></pre>

          <p>Notice the mathematical structure of the control points: by placing both control points at horizontal coordinate \( \text{midX} = (x_1 + x_2) / 2 \) while preserving their respective vertical altitudes \( y_1 \) and \( y_2 \), the curve departs axis \( k \) horizontally with zero vertical slope and arrives at axis \( k+1 \) horizontally. This horizontal tangency guarantees that the trajectory intersects each vertical axis perpendicularly, ensuring that the metric value at the axis is visually unambiguous and completely free of curve overshoot.</p>
        </section>

        <section id="section-figure-2">
          <h2>4. Figure 2: Multivariate Parallel Projection &amp; Range Brushing Pipeline</h2>
          <p>The vector parallel coordinates pipeline converts high-dimensional data matrices into interactive, filterable SVG vector graphics through five decoupled algorithmic stages. Figure 2 illustrates this architectural pipeline:</p>

          <figure class="article-figure">
            <svg viewBox="0 0 960 320" width="960" height="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figure 2: SVG Parallel Coordinates Architecture and Range Brushing Pipeline">
              <rect width="960" height="320" fill="#0D0D0D" rx="8" stroke="#222" stroke-width="1"></rect>
              <defs>
                <marker id="pcArrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
                  <polygon points="0 0, 8 3, 0 6" fill="#C1DD2D"></polygon>
                </marker>
              </defs>

              <!-- Stage 1: Multivariate Records -->
              <g transform="translate(30, 40)">
                <rect width="165" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="82" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 1: INPUT MATRIX</text>
                <text x="82" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">N Records x K Dims</text>
                <rect x="18" y="80" width="129" height="26" fill="#1C1C1C" rx="4"></rect>
                <text x="82" y="97" fill="#888" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Record: {v0, v1, .. vK}</text>
                <path d="M 28,120 L 137,120 M 28,145 L 137,145 M 28,170 L 137,170" stroke="#262626" stroke-width="1"></path>
                <text x="32" y="136" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="10">Dim 0: CPU [0-100%]</text>
                <text x="32" y="161" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="10">Dim 1: RAM [0-64GB]</text>
                <text x="32" y="186" fill="#F59E0B" font-family="'JetBrains Mono', monospace" font-size="10">Dim 2: Latency [ms]</text>
                <text x="82" y="244" fill="#666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Heterogeneous Units</text>
              </g>

              <!-- Connector 1 -->
              <line x1="195" y1="160" x2="230" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#pcArrow)"></line>

              <!-- Stage 2: Normalization -->
              <g transform="translate(240, 40)">
                <rect width="180" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="90" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 2: SCALING</text>
                <text x="90" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Axis Normalization</text>
                <rect x="18" y="80" width="144" height="34" fill="#1C1C1C" rx="4" stroke="#333" stroke-width="0.8"></rect>
                <text x="90" y="96" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">u = (v - Min) / Span</text>
                <text x="90" y="108" fill="#888" font-family="'Inter', sans-serif" font-size="9" text-anchor="middle">Normalize to [0.0, 1.0]</text>
                <rect x="18" y="122" width="144" height="34" fill="#1C1C1C" rx="4" stroke="#333" stroke-width="0.8"></rect>
                <text x="90" y="138" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Y_svg = Base - u * InnerH</text>
                <text x="90" y="150" fill="#888" font-family="'Inter', sans-serif" font-size="9" text-anchor="middle">Cartesian inversion</text>
                <rect x="18" y="164" width="144" height="34" fill="#1C1C1C" rx="4" stroke="#333" stroke-width="0.8"></rect>
                <text x="90" y="180" fill="#FFF" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Equidistant Spacing</text>
                <text x="90" y="192" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">x_k = PadL + k * SlotW</text>
                <text x="90" y="244" fill="#666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Independent Scales</text>
              </g>

              <!-- Connector 2 -->
              <line x1="420" y1="160" x2="455" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#pcArrow)"></line>

              <!-- Stage 3: Brush Filter -->
              <g transform="translate(465, 40)">
                <rect width="190" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="95" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 3: BRUSH FILTER</text>
                <text x="95" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Conjunction Gating</text>
                <rect x="20" y="80" width="150" height="40" fill="#1A1A1A" rx="4" stroke="#C1DD2D" stroke-width="1"></rect>
                <text x="95" y="97" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" text-anchor="middle">Logical AND Gate</text>
                <text x="95" y="112" fill="#FFF" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">v_k in [Low_k, High_k]</text>
                <rect x="20" y="130" width="150" height="34" fill="#1A1A1A" rx="4" stroke="#38BDF8" stroke-width="0.8"></rect>
                <text x="95" y="146" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Active: High Opacity</text>
                <text x="95" y="158" fill="#AAA" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Glowing neon path stroke</text>
                <rect x="20" y="172" width="150" height="34" fill="#1A1A1A" rx="4" stroke="#444" stroke-width="0.8"></rect>
                <text x="95" y="188" fill="#777" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Inactive: Low Opacity</text>
                <text x="95" y="200" fill="#555" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Dimmed background grey</text>
                <text x="95" y="244" fill="#666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Multi-Axis Query</text>
              </g>

              <!-- Connector 3 -->
              <line x1="655" y1="160" x2="690" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#pcArrow)"></line>

              <!-- Stage 4: SVG Emission -->
              <g transform="translate(700, 40)">
                <rect width="230" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="115" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 4: SVG EMISSION</text>
                <text x="115" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Vector DOM Assembly</text>

                <!-- Mini Parallel Coordinates graphic -->
                <g transform="translate(25, 80)">
                  <line x1="20" y1="10" x2="20" y2="110" stroke="#555" stroke-width="1.5"></line>
                  <line x1="70" y1="10" x2="70" y2="110" stroke="#555" stroke-width="1.5"></line>
                  <line x1="120" y1="10" x2="120" y2="110" stroke="#555" stroke-width="1.5"></line>
                  <line x1="160" y1="10" x2="160" y2="110" stroke="#555" stroke-width="1.5"></line>

                  <!-- Brush selection rectangle -->
                  <rect x="62" y="30" width="16" height="45" fill="rgba(56,189,248,0.25)" stroke="#38BDF8" stroke-width="1" rx="2"></rect>

                  <!-- Active Path -->
                  <path d="M 20 25 C 45 25, 45 40, 70 40 C 95 40, 95 30, 120 30 C 140 30, 140 70, 160 70" fill="none" stroke="#C1DD2D" stroke-width="2"></path>
                  <!-- Inactive Path -->
                  <path d="M 20 85 C 45 85, 45 95, 70 95 C 95 95, 95 80, 120 80 C 140 80, 140 20, 160 20" fill="none" stroke="#444" stroke-width="1" opacity="0.4"></path>
                </g>
                <text x="115" y="244" fill="#AAA" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">&lt;path class="trajectory"&gt;</text>
              </g>
            </svg>
            <figcaption>Figure 2: Complete architectural pipeline transforming high-dimensional data matrices through dynamic per-axis normalization, conjunction brush filtering, and smooth cubic Bézier vector trajectory emission.</figcaption>
          </figure>
        </section>

        <section id="section-range-brushing">
          <h2>5. Interactive 1D &amp; Multi-Axis Range Brushing: Real-Time Conjunction Filtering Calculus</h2>
          <p>The true power of parallel coordinates is unlocked when analysts interact with the visualization dynamically. Static plots quickly succumb to visual clutter, but interactive range brushing enables analysts to isolate specific multi-dimensional cohorts in real time.</p>

          <h3>Mathematical Mechanics of Multi-Axis Brushing</h3>
          <p>An axis brush is defined as an interval \( \mathcal{B}_k = [y_{\text{low}, k}, y_{\text{high}, k}] \) bounding values along vertical axis \( k \). Let \( \mathcal{K}_{\text{brushed}} \subseteq \{0, 1, \dots, K-1\} \) denote the subset of axes that currently carry active brushes. An observation record \( \mathbf{v} \) satisfies the global filter if and only if it satisfies the criteria on every brushed axis simultaneously:</p>

          <div class="formula-card">
            <div class="formula-title">Multi-Axis Conjunction Filter Predicate</div>
            <div class="formula-body">
              \Phi(\mathbf{v}) = \prod_{k \in \mathcal{K}_{\text{brushed}}} \mathbb{I}\left( y_{\text{low}, k} \le Y_k(v_k) \le y_{\text{high}, k} \right)
            </div>
            <div class="formula-desc">Where I is the indicator function returning 1 if the condition is satisfied and 0 otherwise. If Phi equals 1, the record is highlighted as active; if 0, it is dimmed into the background.</div>
          </div>

          <h3>Interactive SVG Brush UI &amp; Drag Handlers</h3>
          <p>In pure SVG, an interactive brush is rendered as a semi-transparent rectangle <code>&lt;rect class="brush-selection"&gt;</code> positioned along the vertical axis, flanked by top and bottom resize handle bars. The user can perform three gestures:</p>
          <ol>
            <li><strong>Click and Drag to Create:</strong> Dragging along an axis creates a new rectangular brush bounding box.</li>
            <li><strong>Translate Entire Brush:</strong> Dragging the central body of the brush slides the selection window up and down the axis, smoothly exploring continuous parameter spaces.</li>
            <li><strong>Resize Boundary Limits:</strong> Dragging either the top or bottom handle expands or contracts the filter interval.</li>
          </ol>
        </section>

        <section id="section-axis-ordering">
          <h2>6. Dimensional Ordering, Correlation Clustering &amp; Heuristic Reordering Algorithms</h2>
          <p>Because parallel coordinates only display direct geometric relationships between immediately adjacent axes, the horizontal ordering of dimensions dramatically impacts analytical efficacy. In a dataset with 8 dimensions, there exist \( 8! / 2 = 20,160 \) unique horizontal axis permutations. If two strongly correlated variables are separated by four intermediate axes, their correlation is completely invisible to the human observer.</p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Ordering Algorithm</th>
                  <th>Computational Complexity</th>
                  <th>Optimization Metric</th>
                  <th>Recommended Use Case</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Domain Logical Ordering</strong></td>
                  <td>\( O(1) \)</td>
                  <td>Semantic developer workflow sequence</td>
                  <td>Standard dashboards (e.g., Request &rarr; Compute &rarr; Storage &rarr; Cost)</td>
                </tr>
                <tr>
                  <td><strong>Pearson Correlation TSP</strong></td>
                  <td>\( O(K^2 2^K) \)</td>
                  <td>Maximized adjacent \( |r| \) correlation</td>
                  <td>Scientific analysis, identifying linear dependencies and trade-offs</td>
                </tr>
                <tr>
                  <td><strong>Hierarchical Clustering</strong></td>
                  <td>\( O(K^3) \)</td>
                  <td>Euclidean distance dendrogram seriation</td>
                  <td>Clustering high-dimensional machine learning feature embeddings</td>
                </tr>
                <tr>
                  <td><strong>Interactive Drag Reordering</strong></td>
                  <td>\( O(K) \)</td>
                  <td>User exploratory hypothesis formulation</td>
                  <td>Interactive analytical consoles and diagnostic exploration studios</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p>To enable interactive exploration, modern SVG parallel coordinates allow operators to drag vertical axis headers horizontally. As the user drags an axis header across its neighbors, the underlying path coordinate indices update dynamically with hardware-accelerated CSS transitions, letting analysts inspect arbitrary pairwise relationships on demand.</p>
        </section>

        <!-- INTERACTIVE STUDIO SANDBOX -->
        <section class="interactive-sandbox" id="interactive-parallel-studio">
          <div class="sandbox-header">
            <div class="sandbox-title">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#C1DD2D" stroke-width="2"><line x1="4" y1="21" x2="4" y2="3"></line><line x1="9" y1="21" x2="9" y2="3"></line><line x1="15" y1="21" x2="15" y2="3"></line><line x1="20" y1="21" x2="20" y2="3"></line><polyline points="4 7 9 12 15 8 20 16"></polyline></svg>
              Interactive SVG Parallel Coordinates Studio
            </div>
            <span class="sandbox-badge">Real-Time High-Dimensional Engine</span>
          </div>

          <p style="font-size: 14.5px; color: #AAA; margin-bottom: 20px;">Manipulate multi-dimensional brush filters, toggle cubic Bézier trajectory smoothing, filter multivariate records in real time, and export standalone SVG markup instantly.</p>

          <div class="sandbox-controls">
            <div class="control-row">
              <label for="pc-preset-select">Multivariate Scenario Dataset:</label>
              <select id="pc-preset-select" class="control-select">
                <option value="server-fleet">Cloud Server Fleet Infrastructure</option>
                <option value="automotive">High-Performance Automotive Engine Telemetry</option>
                <option value="saas-churn">SaaS Customer Usage &amp; Churn Predictors</option>
                <option value="botanical-iris">Fisher Iris Botanical Multivariate Data</option>
              </select>
            </div>

            <div class="control-row">
              <label for="pc-curve-mode">Trajectory Interpolation:</label>
              <select id="pc-curve-mode" class="control-select">
                <option value="smooth">Smooth Cubic Bézier Splines</option>
                <option value="linear">Sharp Piecewise Polylines</option>
              </select>
            </div>

            <div class="control-row">
              <label for="pc-brush-axis">Active Brush Dimension:</label>
              <select id="pc-brush-axis" class="control-select">
                <option value="1">Dimension 2 (RAM / Torque / Metric B)</option>
                <option value="0">Dimension 1 (CPU / RPM / Metric A)</option>
                <option value="2">Dimension 3 (Latency / Power / Metric C)</option>
                <option value="3">Dimension 4 (Disk IO / Economy / Metric D)</option>
                <option value="4">Dimension 5 (Error Rate / Temp / Metric E)</option>
              </select>
            </div>

            <div class="control-row">
              <label for="pc-brush-min-slider">Brush Min Filter: <span id="pc-brush-min-val" style="color:#C1DD2D; font-weight:700;">20%</span></label>
              <input type="range" id="pc-brush-min-slider" class="control-input" min="0" max="80" value="20" step="5">
            </div>

            <div class="control-row">
              <label for="pc-brush-max-slider">Brush Max Filter: <span id="pc-brush-max-val" style="color:#38BDF8; font-weight:700;">75%</span></label>
              <input type="range" id="pc-brush-max-slider" class="control-input" min="20" max="100" value="75" step="5">
            </div>
          </div>

          <div class="preview-stage-container">
            <svg id="pc-live-svg" class="parallel-svg-canvas" viewBox="0 0 760 480" width="760" height="480" xmlns="http://www.w3.org/2000/svg" role="graphics-document" aria-label="Interactive SVG Parallel Coordinates Studio Visualizing Multivariate Record Trajectories">
              <!-- Rendered dynamically by JavaScript -->
            </svg>
          </div>

          <div class="stats-readout-box">
            <div class="stat-item">
              <span class="stat-label">Total Records</span>
              <span class="stat-val" id="stat-total-records">80 Records</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">Active / Brushed</span>
              <span class="stat-val highlight" id="stat-active-records">44 Records</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">Pass Rate</span>
              <span class="stat-val highlight" id="stat-pass-rate">55.0%</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">Parallel Dimensions</span>
              <span class="stat-val" id="stat-dimensions-count">5 Axes</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">Active Filter</span>
              <span class="stat-val" id="stat-brush-range">[20% - 75%]</span>
            </div>
          </div>

          <div class="action-btn-row">
            <button class="copy-btn" id="copy-pc-svg-btn" type="button" aria-label="Copy Standalone SVG to Clipboard">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
              <span>Copy Standalone SVG</span>
            </button>
          </div>
        </section>

        <section id="section-production-engine">
          <h2>7. Production-Grade Zero-Dependency ES6 Parallel Coordinates Engine</h2>
          <p>Below is a production-grade, self-contained ES6 class implementing multi-dimensional dataset ingestion, dynamic per-axis min-max normalization, smooth cubic Bézier trajectory generation, and multi-axis range brush evaluation:</p>

          <pre><code>// Production-Grade Zero-Dependency SVG Parallel Coordinates Engine
class SvgParallelCoordinatesEngine {
  constructor(config = {}) {
    this.width = config.width || 760;
    this.height = config.height || 480;
    this.padding = config.padding || { top: 50, right: 40, bottom: 50, left: 50 };
    this.curveMode = config.curveMode || 'smooth'; // 'smooth' or 'linear'
  }

  // Derive domain bounds for each dimension
  static analyzeDimensions(dimensions, records) {
    return dimensions.map(dim => {
      let min = Infinity;
      let max = -Infinity;
      records.forEach(r => {
        const v = r[dim.key];
        if (v &lt; min) min = v;
        if (v &gt; max) max = v;
      });
      return { ...dim, min, max, span: (max - min) || 1 };
    });
  }

  // Render standalone SVG string
  render(dimensions, records, brushes = {}) {
    const dimStats = SvgParallelCoordinatesEngine.analyzeDimensions(dimensions, records);
    const plotW = this.width - this.padding.left - this.padding.right;
    const plotH = this.height - this.padding.top - this.padding.bottom;
    const k = dimStats.length;
    const slotW = plotW / (k - 1);

    const scaleX = idx =&gt; this.padding.left + idx * slotW;
    const scaleY = (dim, v) =&gt; {
      const norm = (v - dim.min) / dim.span;
      return (this.height - this.padding.bottom) - norm * plotH;
    };

    // Evaluate active brush status for each record
    let activePaths = '';
    let inactivePaths = '';

    records.forEach(r => {
      let isActive = true;
      for (const [dimKey, brushRange] of Object.entries(brushes)) {
        const v = r[dimKey];
        if (v &lt; brushRange[0] || v &gt; brushRange[1]) {
          isActive = false;
          break;
        }
      }

      const pts = dimStats.map((dim, idx) =&gt; ({
        x: scaleX(idx),
        y: scaleY(dim, r[dim.key])
      }));

      let d = `M ${pts[0].x.toFixed(1)} ${pts[0].y.toFixed(1)}`;
      if (this.curveMode === 'smooth') {
        for (let i = 0; i &lt; pts.length - 1; i++) {
          const midX = (pts[i].x + pts[i + 1].x) / 2;
          d += ` C ${midX.toFixed(1)} ${pts[i].y.toFixed(1)}, ${midX.toFixed(1)} ${pts[i + 1].y.toFixed(1)}, ${pts[i + 1].x.toFixed(1)} ${pts[i + 1].y.toFixed(1)}`;
        }
      } else {
        for (let i = 1; i &lt; pts.length; i++) {
          d += ` L ${pts[i].x.toFixed(1)} ${pts[i].y.toFixed(1)}`;
        }
      }

      if (isActive) {
        activePaths += `&lt;path d="${d}" fill="none" stroke="${r.color || '#C1DD2D'}" stroke-width="1.8" opacity="0.85"/&gt;`;
      } else {
        inactivePaths += `&lt;path d="${d}" fill="none" stroke="#444" stroke-width="1" opacity="0.08"/&gt;`;
      }
    });

    // Generate axis lines and labels
    let axisElements = '';
    dimStats.forEach((dim, idx) => {
      const ax = scaleX(idx);
      axisElements += `&lt;line x1="${ax}" y1="${this.padding.top}" x2="${ax}" y2="${this.height - this.padding.bottom}" stroke="#666" stroke-width="1.5"/&gt;`;
      axisElements += `&lt;text x="${ax}" y="${this.padding.top - 18}" fill="#FFF" font-family="'Inter', sans-serif" font-size="12" font-weight="700" text-anchor="middle"&gt;${dim.label}&lt;/text&gt;`;
    });

    return `&lt;svg viewBox="0 0 ${this.width} ${this.height}" xmlns="http://www.w3.org/2000/svg" role="graphics-document"&gt;
      &lt;g class="inactive-records"&gt;${inactivePaths}&lt;/g&gt;
      &lt;g class="active-records"&gt;${activePaths}&lt;/g&gt;
      &lt;g class="axes"&gt;${axisElements}&lt;/g&gt;
    &lt;/svg&gt;`;
  }
}</code></pre>
        </section>

        <section id="section-accessibility-theming">
          <h2>8. Scalability, Touch Ergonomics &amp; Dual-Theme WCAG 2.2 AA Accessibility</h2>
          <p>Delivering production-grade parallel coordinate visualizations demands strict compliance with digital accessibility standards and touch-screen ergonomic guidelines. Dense high-dimensional charts with thin vector lines can easily present severe accessibility barriers if not designed with precision.</p>

          <h3>Touch-Action Ergonomics &amp; Mobile Responsive Viewports</h3>
          <p>On touch-screen hardware (such as mobile tablets and diagnostic field computers), dragging an axis brush frequently collides with the browser's default viewport panning and pull-to-refresh gestures. Declaring <code>touch-action: none</code> directly on the interactive SVG canvas eliminates browser gesture interference, routing all pointer events directly to the application's dragging logic.</p>
          <p>Furthermore, standard 1-pixel axis lines present nearly impossible touch targets for human fingers. Under WCAG 2.2 Success Criterion 2.5.8 (Target Size Minimum), interactive touch targets must measure at least 24 by 24 CSS pixels. To satisfy this rule without cluttering the visual design, each visible axis is wrapped in an invisible transparent overlay rectangle <code>&lt;rect width="36" fill="transparent" pointer-events="all"&gt;</code> that captures finger taps and gestures effortlessly.</p>

          <h3>Dual-Theme Color Contrast &amp; Non-Visual Parity</h3>
          <p>Under WCAG 2.2 AA standards, all text labels, axis titles, and numeric ticks must achieve at least a 4.5:1 contrast ratio against the canvas background. In dark theme, high-contrast white text <code>#F2F2F2</code> and neon lime strokes <code>#C1DD2D</code> achieve superior readability. In light theme, interactive text, links, and focal trajectories shift to deep forest olive <code>#4D6300</code>, securing an accredited 5.4:1 contrast against pure white <code>#FAFAFA</code>.</p>
          <p>For non-visual accessibility, the root SVG container declares <code>role="graphics-document"</code> accompanied by descriptive title and description elements. Crucially, the chart is paired with a companion data table below the graphic: as the user brushes axes, the table filters synchronously, allowing screen-reader users to inspect exact numerical records and query multi-dimensional cohorts via standard table navigation shortcuts.</p>
        </section>

        <section id="section-takeaways">
          <div class="takeaway-box">
            <h3>Key Engineering Takeaways</h3>
            <ul>
              <li><strong>Leverage Projective Point-Line Duality:</strong> Parallel coordinates map N-dimensional observations to continuous polyline paths, transforming high-dimensional clustering into visible vector bundles.</li>
              <li><strong>Normalize Disparate Physical Domains:</strong> Apply dynamic per-axis min-max scaling to transform heterogeneous units into unified 0-to-1 vertical pixel viewports.</li>
              <li><strong>Smooth Trajectories with Horizontal Tangents:</strong> Use cubic Bézier curves with mid-point control points to eliminate angular clutter while maintaining exact perpendicular axis intersections.</li>
              <li><strong>Implement Sub-Millisecond Conjunction Brushing:</strong> Logical AND gating across active brush intervals lets analysts isolate complex multivariate cohorts instantaneously.</li>
              <li><strong>Enforce WCAG 2.2 AA Touch &amp; Contrast Standards:</strong> Combine 24px invisible touch targets, 4.5:1 text contrast (<code>#4D6300</code> on light), and synchronized tabular data tables for universal accessibility.</li>
            </ul>
          </div>
        </section>

        <section class="faq-section" id="section-faq">
          <h2>9. Frequently Asked Questions</h2>
          <div class="faq-item">
            <div class="faq-question">What is Alfred Inselberg's point-line projective duality in parallel coordinates?</div>
            <div class="faq-answer">Alfred Inselberg established that parallel coordinates represent a projective geometric transformation between Cartesian coordinate space and parallel axis space. In standard Cartesian 2D coordinates, an observation is represented as a point (x, y), while a linear relationship is represented as a line y = mx + b. In parallel coordinate space, this geometry is dualized: an N-dimensional data point is transformed into a continuous polygonal line (polyline) that intersects N equidistant vertical parallel axes. Conversely, a line in Cartesian space maps to a single pencil point of intersection between the two adjacent parallel axes. A negative correlation manifests as a sharp crossover intersection between axes, while a positive correlation produces parallel, non-intersecting bundles.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How does dynamic min-max normalization project heterogeneous metrics onto identical vertical pixel spans?</div>
            <div class="faq-answer">Because high-dimensional datasets combine metrics with wildly disparate physical units and numerical scales—such as server latency (10 to 500 ms), CPU utilization (0% to 100%), and database memory allocation (512 to 32,768 MB)—they cannot share a single vertical axis. Dynamic min-max normalization transforms each raw feature value v_k into a standardized dimensionless ratio u_k between 0.0 and 1.0: u_k = (v_k - min_k) / (max_k - min_k). In SVG coordinates, this ratio is mapped to vertical screen pixels via Cartesian inversion: y_svg = (height - paddingBottom) - u_k * (height - paddingTop - paddingBottom), ensuring that every variable occupies an identical, balanced visual span.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">Why are smooth cubic Bézier splines often preferred over sharp linear polylines in dense plots?</div>
            <div class="faq-answer">When visualizing hundreds or thousands of high-dimensional records, linear polylines create severe visual clutter and sharp angular intersections at every vertical axis. Human visual perception struggles to track individual trajectories through dense clusters of jagged lines. Converting polyline vertices into smooth cubic Bézier curves (or Catmull-Rom splines) softens directional changes, improves optical continuity, and aligns with the Gestalt principle of good continuation. Viewers can track individual multivariate records through dense bundles far more effectively, making structural clusters, outliers, and multivariate trajectories immediately discernible.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How does multi-axis range brushing compute conjunction filtering in real time?</div>
            <div class="faq-answer">Multi-axis range brushing implements a logical conjunction (AND gate) across all brushed dimensions. Each axis k can have an active selection interval [y_low_k, y_high_k]. A record is classified as active if and only if its value on every brushed axis falls strictly within that axis's active interval: Active(record) = product_{k in Brushed} (low_k <= v_k <= high_k). The engine renders active records with vibrant category colors and prominent stroke-widths (1.8px), while inactive records are dimmed to faint gray lines (opacity 0.08). This instantaneous filtering allows analysts to isolate complex multi-dimensional cohorts in sub-millisecond execution times.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How does axis ordering influence multivariate pattern recognition, and how can it be optimized?</div>
            <div class="faq-answer">In parallel coordinates, pairwise correlations and geometric patterns can only be visually decoded between directly adjacent parallel axes. An N-dimensional dataset features N! possible axis permutations, meaning that poorly ordered axes can hide critical relationships. To maximize pattern discovery, data engineers utilize correlation-clustering algorithms such as hierarchical clustering or maximum spanning tree (MST) Hamiltonian path traversals. By placing variables with high Pearson or Spearman correlation coefficients adjacent to one another, cross-over points and tight bundle patterns become immediately visible.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How do you achieve WCAG 2.2 AA compliance for high-dimensional SVG parallel coordinate charts?</div>
            <div class="faq-answer">To achieve full WCAG 2.2 AA compliance, the root SVG container must declare role='graphics-document' along with an aria-label and companion title and desc elements describing dataset scope and active filter states. Individual vertical axes declare role='graphics-axis' with accessible numerical tick labels exceeding a 4.5:1 contrast ratio against the background. Interactive brush handles carry keyboard focusability via tabindex='0' and ARIA slider attributes (aria-valuemin, aria-valuemax, aria-valuenow). Furthermore, records must never be differentiated solely by color hue; distinct dash patterns (solid, dashed, dotted) and persistent tabular inspectors must accompany all categorical cluster groupings.</div>
          </div>
        </section>

      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <a href="#section-foundations">1. Inselberg Duality Foundations</a>
            <a href="#section-normalization">2. Dynamic Axis Normalization</a>
            <a href="#section-spline-smoothing">3. Polyline vs Cubic Splines</a>
            <a href="#section-figure-2">4. Figure 2: Architecture Pipeline</a>
            <a href="#section-range-brushing">5. Multi-Axis Range Brushing</a>
            <a href="#section-axis-ordering">6. Axis Ordering Algorithms</a>
            <a href="#interactive-parallel-studio">7. Interactive Studio Sandbox</a>
            <a href="#section-production-engine">8. Zero-Dependency ES6 Engine</a>
            <a href="#section-accessibility-theming">9. Accessibility &amp; WCAG Contrast</a>
            <a href="#section-takeaways">10. Key Engineering Takeaways</a>
            <a href="#section-faq">11. Frequently Asked Questions</a>
          </nav>
        </div>

        <div class="sidebar-card cta-sidebar-box">
          <div class="cta-title">Explore Related Guides</div>
          <p>Expand your data visualization capabilities with our companion technical engineering deep dives:</p>
          <div class="toc-nav">
            <a href="/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide/">SVG Box Plots &amp; Whiskers</a>
            <a href="/articles/svg-area-charts-and-stacked-streamgraph-visualization-guide/">SVG Area Charts &amp; Streamgraphs</a>
            <a href="/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide/">SVG Scatter Plots &amp; Bubbles</a>
            <a href="/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide/">SVG Network Graphs &amp; Force Physics</a>
            <a href="/articles/svg-radar-charts-and-multivariate-polar-visualization-guide/">SVG Radar Charts &amp; Polar Visuals</a>
            <a href="/articles/svg-heatmaps-and-activity-matrix-visualization-guide/">SVG Heatmaps &amp; Activity Matrices</a>
          </div>
        </div>
      </aside>
    </div>
  </div>

  <footer class="site-footer">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px; align-items: center;">
      <p>&copy; 2026 IconStash. Published by Great Software Company. All rights reserved.</p>
      <p><a href="/about/">About IconStash &amp; Jouni Flemming</a> &bull; <a href="/articles/">All Visualization Guides</a> &bull; <a href="/privacy/">Privacy Policy</a></p>
    </div>
  </footer>

  <script>
    // Theme toggle handling
    const themeBtn = document.getElementById('theme-toggle');
    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', nextTheme);
      });
    }

    // Interactive Parallel Coordinates Studio
    (function initParallelStudio() {
      const liveSvg = document.getElementById('pc-live-svg');
      const presetSelect = document.getElementById('pc-preset-select');
      const curveSelect = document.getElementById('pc-curve-mode');
      const brushAxisSelect = document.getElementById('pc-brush-axis');
      const brushMinSlider = document.getElementById('pc-brush-min-slider');
      const brushMinVal = document.getElementById('pc-brush-min-val');
      const brushMaxSlider = document.getElementById('pc-brush-max-slider');
      const brushMaxVal = document.getElementById('pc-brush-max-val');
      const copyBtn = document.getElementById('copy-pc-svg-btn');

      const statTotalRecords = document.getElementById('stat-total-records');
      const statActiveRecords = document.getElementById('stat-active-records');
      const statPassRate = document.getElementById('stat-pass-rate');
      const statDimensionsCount = document.getElementById('stat-dimensions-count');
      const statBrushRange = document.getElementById('stat-brush-range');

      if (!liveSvg) return;

      const clusterColors = ['#C1DD2D', '#38BDF8', '#F59E0B', '#A855F7'];

      // Deterministic PRNG
      function pseudoRandom(seed) {
        let s = seed % 2147483647;
        if (s <= 0) s += 2147483646;
        return function() {
          s = (s * 16807) % 2147483647;
          return (s - 1) / 2147483646;
        };
      }

      function generateDataset(preset) {
        const seed = preset === 'server-fleet' ? 101 : preset === 'automotive' ? 202 : preset === 'saas-churn' ? 303 : 404;
        const rng = pseudoRandom(seed);
        const count = 75;

        let dimensions = [];
        if (preset === 'server-fleet') {
          dimensions = [
            { key: 'cpu', label: 'CPU Load (%)', min: 0, max: 100 },
            { key: 'ram', label: 'RAM Usage (GB)', min: 4, max: 64 },
            { key: 'latency', label: 'Latency (ms)', min: 10, max: 350 },
            { key: 'disk', label: 'Disk IOPS', min: 100, max: 8000 },
            { key: 'errors', label: 'Errors / sec', min: 0, max: 25 }
          ];
        } else if (preset === 'automotive') {
          dimensions = [
            { key: 'rpm', label: 'Engine RPM', min: 800, max: 7500 },
            { key: 'torque', label: 'Torque (Nm)', min: 120, max: 650 },
            { key: 'speed', label: 'Speed (km/h)', min: 0, max: 280 },
            { key: 'fuel', label: 'Fuel Flow (L/h)', min: 2, max: 45 },
            { key: 'temp', label: 'Oil Temp (°C)', min: 70, max: 130 }
          ];
        } else if (preset === 'saas-churn') {
          dimensions = [
            { key: 'seats', label: 'Active Seats', min: 1, max: 250 },
            { key: 'dau', label: 'DAU / MAU Ratio', min: 0.1, max: 0.95 },
            { key: 'tickets', label: 'Support Tickets', min: 0, max: 40 },
            { key: 'nps', label: 'NPS Score', min: -20, max: 100 },
            { key: 'mrr', label: 'Monthly MRR ($)', min: 50, max: 5000 }
          ];
        } else {
          dimensions = [
            { key: 'sepalL', label: 'Sepal Length', min: 4.0, max: 8.0 },
            { key: 'sepalW', label: 'Sepal Width', min: 2.0, max: 4.5 },
            { key: 'petalL', label: 'Petal Length', min: 1.0, max: 7.0 },
            { key: 'petalW', label: 'Petal Width', min: 0.1, max: 2.5 },
            { key: 'ratio', label: 'Petal / Sepal', min: 0.1, max: 0.9 }
          ];
        }

        const records = [];
        for (let i = 0; i < count; i++) {
          const clusterId = i % 3;
          const rec = { id: `REC-${i+1}`, clusterId, color: clusterColors[clusterId] };
          dimensions.forEach(dim => {
            const baseNorm = (clusterId * 0.35 + rng() * 0.45);
            const clamped = Math.max(0.05, Math.min(0.95, baseNorm + (rng() - 0.5) * 0.18));
            rec[dim.key] = +(dim.min + clamped * (dim.max - dim.min)).toFixed(2);
          });
          records.push(rec);
        }

        return { dimensions, records };
      }

      function renderStudio() {
        const preset = presetSelect.value;
        const curveMode = curveSelect.value;
        const brushAxisIdx = parseInt(brushAxisSelect.value, 10);
        let bMinPct = parseInt(brushMinSlider.value, 10);
        let bMaxPct = parseInt(brushMaxSlider.value, 10);
        if (bMinPct >= bMaxPct) bMinPct = Math.max(0, bMaxPct - 5);

        brushMinVal.textContent = bMinPct + '%';
        brushMaxVal.textContent = bMaxPct + '%';

        const { dimensions, records } = generateDataset(preset);
        const k = dimensions.length;

        const pad = { top: 50, right: 45, bottom: 60, left: 45 };
        const viewW = 760;
        const viewH = 480;
        const plotW = viewW - pad.left - pad.right;
        const plotH = viewH - pad.top - pad.bottom;
        const slotW = plotW / (k - 1);

        const scaleX = idx => pad.left + idx * slotW;
        const scaleY = (dim, val) => {
          const norm = (val - dim.min) / (dim.max - dim.min || 1);
          return (viewH - pad.bottom) - norm * plotH;
        };

        const targetDim = dimensions[brushAxisIdx];
        const brushValMin = targetDim.min + (bMinPct / 100) * (targetDim.max - targetDim.min);
        const brushValMax = targetDim.min + (bMaxPct / 100) * (targetDim.max - targetDim.min);

        let activeCount = 0;
        let activeMarks = '';
        let inactiveMarks = '';

        records.forEach(r => {
          const v = r[targetDim.key];
          const isActive = (v >= brushValMin && v <= brushValMax);
          if (isActive) activeCount++;

          const pts = dimensions.map((dim, idx) => ({
            x: scaleX(idx),
            y: scaleY(dim, r[dim.key])
          }));

          let d = `M ${pts[0].x.toFixed(1)} ${pts[0].y.toFixed(1)}`;
          if (curveMode === 'smooth') {
            for (let i = 0; i < pts.length - 1; i++) {
              const midX = (pts[i].x + pts[i + 1].x) / 2;
              d += ` C ${midX.toFixed(1)} ${pts[i].y.toFixed(1)}, ${midX.toFixed(1)} ${pts[i + 1].y.toFixed(1)}, ${pts[i + 1].x.toFixed(1)} ${pts[i + 1].y.toFixed(1)}`;
            }
          } else {
            for (let i = 1; i < pts.length; i++) {
              d += ` L ${pts[i].x.toFixed(1)} ${pts[i].y.toFixed(1)}`;
            }
          }

          if (isActive) {
            activeMarks += `<path d="${d}" fill="none" stroke="${r.color}" stroke-width="1.8" opacity="0.85"/>`;
          } else {
            inactiveMarks += `<path d="${d}" fill="none" stroke="#555" stroke-width="1" opacity="0.08"/>`;
          }
        });

        // Axes and Ticks
        let axisMarks = '';
        dimensions.forEach((dim, idx) => {
          const ax = scaleX(idx);
          axisMarks += `<line x1="${ax.toFixed(1)}" y1="${pad.top}" x2="${ax.toFixed(1)}" y2="${viewH - pad.bottom}" stroke="#444" stroke-width="1.5"/>`;

          // Header Label
          axisMarks += `<text x="${ax.toFixed(1)}" y="${pad.top - 18}" fill="#FFF" font-family="'Inter', sans-serif" font-size="12" font-weight="700" text-anchor="middle">${dim.label}</text>`;

          // Ticks
          for (let t = 0; t <= 4; t++) {
            const frac = t / 4;
            const ty = (viewH - pad.bottom) - frac * plotH;
            const tVal = dim.min + frac * (dim.max - dim.min);
            axisMarks += `<line x1="${ax - 4}" y1="${ty.toFixed(1)}" x2="${ax + 4}" y2="${ty.toFixed(1)}" stroke="#666" stroke-width="1"/>`;
            axisMarks += `<text x="${ax - 7}" y="${(ty + 3).toFixed(1)}" fill="#888" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="end">${tVal >= 1000 ? (tVal/1000).toFixed(1)+'k' : tVal.toFixed(tVal < 10 ? 1 : 0)}</text>`;
          }
        });

        // Brush Visual Indicator on target axis
        const targetAx = scaleX(brushAxisIdx);
        const yTopBrush = (viewH - pad.bottom) - (bMaxPct / 100) * plotH;
        const yBotBrush = (viewH - pad.bottom) - (bMinPct / 100) * plotH;
        const brushH = Math.max(4, yBotBrush - yTopBrush);
        const brushRect = `<rect x="${targetAx - 12}" y="${yTopBrush.toFixed(1)}" width="24" height="${brushH.toFixed(1)}" fill="rgba(56,189,248,0.22)" stroke="#38BDF8" stroke-width="1.5" rx="3"/>`;

        liveSvg.innerHTML = `
          <rect width="${viewW}" height="${viewH}" fill="#0A0A0A" rx="6"/>
          ${axisMarks}
          <g class="inactive-group">${inactiveMarks}</g>
          <g class="active-group">${activeMarks}</g>
          ${brushRect}
        `;

        // Update readouts
        statTotalRecords.textContent = records.length + ' Records';
        statActiveRecords.textContent = activeCount + ' Records';
        const passRate = ((activeCount / records.length) * 100).toFixed(1);
        statPassRate.textContent = passRate + '%';
        statDimensionsCount.textContent = k + ' Axes';
        statBrushRange.textContent = `[${bMinPct}% - ${bMaxPct}%]`;
      }

      // Event listeners
      presetSelect.addEventListener('change', renderStudio);
      curveSelect.addEventListener('change', renderStudio);
      brushAxisSelect.addEventListener('change', renderStudio);
      brushMinSlider.addEventListener('input', renderStudio);
      brushMaxSlider.addEventListener('input', renderStudio);

      // Copy Standalone SVG
      copyBtn.addEventListener('click', () => {
        const svgSource = liveSvg.outerHTML;
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(svgSource).then(() => {
            copyBtn.textContent = 'Copied to Clipboard!';
            setTimeout(() => { copyBtn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> <span>Copy Standalone SVG</span>'; }, 2000);
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
            setTimeout(() => { copyBtn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> <span>Copy Standalone SVG</span>'; }, 2000);
          } catch (e) {
            alert('Copy failed: ' + e.message);
          }
          document.body.removeChild(ta);
        }
      });

      // Initial Render
      renderStudio();
    })();
  </script>
</body>
</html>
'''

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated Article 3 successfully at: {target_file}")
