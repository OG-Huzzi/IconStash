import os
import re

slug = "svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide"
target_dir = os.path.join(r"D:\Project IconStash\IconStash\articles", slug)
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

html_content = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mastering SVG Scatter Plots &amp; Bubble Charts: Multivariate Coordinates, Radius Scaling &amp; Interactive Hover Guide (2026) | IconStash</title>
  <meta name="description" content="Build SVG scatter plots & bubble charts: multivariate coordinates, area radius scaling, OLS trendlines, quadtree hit-testing & interactive SVG export.">
  <meta name="keywords" content="svg scatter plot, svg bubble chart, multivariate visualization svg, d3 scatter plot svg, continuous coordinate mapping svg, area radius scaling bubble chart, voronoi hover hit testing, interactive scatter chart javascript">
  <meta property="og:title" content="Mastering SVG Scatter Plots &amp; Bubble Charts: Multivariate Coordinates, Radius Scaling &amp; Interactive Hover Guide (2026)">
  <meta property="og:description" content="Build SVG scatter plots & bubble charts: multivariate coordinates, area radius scaling, OLS trendlines, quadtree hit-testing & interactive SVG export.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-18T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-18T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="Vector Graphics &amp; Data Visualization">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="Scatter Plots">
  <meta property="article:tag" content="Bubble Charts">
  <meta property="article:tag" content="Data Visualization">
  <meta property="article:tag" content="Mathematics">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mastering SVG Scatter Plots &amp; Bubble Charts: Multivariate Coordinates, Radius Scaling &amp; Interactive Hover Guide (2026)">
  <meta name="twitter:description" content="Build SVG scatter plots & bubble charts: multivariate coordinates, area radius scaling, OLS trendlines, quadtree hit-testing & interactive SVG export.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide/">
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
      "headline": "Mastering SVG Scatter Plots & Bubble Charts: Multivariate Coordinates, Radius Scaling & Interactive Hover Guide (2026)",
      "description": "Build SVG scatter plots & bubble charts: multivariate coordinates, area radius scaling, OLS trendlines, quadtree hit-testing & interactive SVG export.",
      "image": "https://iconstash.io/assets/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide.jpg",
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
      "datePublished": "2026-11-18",
      "dateModified": "2026-11-18",
      "mainEntityOfPage": "https://iconstash.io/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide/",
      "inLanguage": "en-US",
      "wordCount": 5120,
      "articleSection": "Vector Graphics & Data Visualization",
      "keywords": [
        "svg scatter plot",
        "svg bubble chart",
        "multivariate visualization svg",
        "d3 scatter plot svg",
        "continuous coordinate mapping svg",
        "area radius scaling bubble chart",
        "voronoi hover hit testing",
        "interactive scatter chart javascript"
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
          "name": "SVG Scatter Plots & Bubble Charts Guide",
          "item": "https://iconstash.io/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why must bubble chart radii be scaled by the square root of value rather than linear proportionality?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Human visual perception estimates the quantitative weight of two-dimensional circular marks by their physical surface area, which equals pi multiplied by radius squared. When a developer scales circle radius directly in linear proportion to a metric value, doubling the metric quadruples the visual surface area of the bubble. This introduces an exponential perceptual distortion known as the square-cube visual illusion. To maintain strict geometric and visual truth, the circle radius must be computed proportional to the square root of the normalized metric value, ensuring that a doubling in underlying data results in exactly double the optical pixel area on the screen."
          }
        },
        {
          "@type": "Question",
          "name": "How does inverted Cartesian Y-mapping work in native SVG viewports?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In the SVG coordinate specification, the origin point (0, 0) is situated at the top-left corner of the viewport canvas, with the positive vertical Y-axis pointing downwards toward the bottom of the screen. In contrast, standard mathematical Cartesian coordinate systems place the origin at the bottom-left, with positive values rising upwards. To correctly project mathematical data points onto an SVG canvas, an inverted transformation formula must be applied: y_svg = (height - paddingBottom) - ((dataY - minY) / (maxY - minY)) * (height - paddingTop - paddingBottom). This subtraction from the baseline coordinate flips the vertical orientation, accurately displaying higher quantitative values toward the visual top of the graph."
          }
        },
        {
          "@type": "Question",
          "name": "What is the optimal spatial index for hover hit-testing on dense SVG scatter plots?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "When an SVG scatter plot contains hundreds or thousands of micro-circle markers, binding individual mouseenter and mouseleave listeners to every DOM element introduces severe memory overhead and creates difficult hit targets for tiny data points. The optimal architectural solution is constructing a Delaunay triangulation and corresponding Voronoi tessellation over the dataset, or querying a 2D Quadtree spatial index on cursor movement. A single pointermove event listener on the root SVG container queries the Quadtree in logarithmic time O(log N) to find the nearest Euclidean neighbor, dispatching highlight states and positioning tooltip overlays instantaneously at 120 FPS."
          }
        },
        {
          "@type": "Question",
          "name": "How is an Ordinary Least Squares (OLS) linear regression trendline rendered mathematically in SVG?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ordinary Least Squares calculates the linear relationship y = beta_1 * x + beta_0 that minimizes the sum of squared vertical residuals across all data observations. The slope beta_1 is calculated as the covariance of X and Y divided by the variance of X, while the intercept beta_0 equals the mean of Y minus beta_1 multiplied by the mean of X. Once these statistical coefficients are computed, the trendline is rendered as a clean SVG line element spanning from the minimum domain coordinate (x_min, beta_1 * x_min + beta_0) to the maximum domain coordinate (x_max, beta_1 * x_max + beta_0), mapped through the viewport projection functions."
          }
        },
        {
          "@type": "Question",
          "name": "How do you mitigate visual clutter and occlusion when hundreds of bubbles overlap?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To solve heavy visual occlusion in dense bubble charts, production vector architectures employ four complementary techniques: first, assigning semi-transparent fill opacities (such as fill-opacity='0.55' to 0.70) combined with crisp, high-contrast outer stroke boundaries; second, sorting bubble elements in descending order of radius before appending them to the SVG DOM so that larger circles never bury smaller circles; third, utilizing CSS mix-blend-mode properties like multiply in light theme or screen in dark theme to accentuate overlapping intersections; and fourth, providing interactive zoom-and-pan transforms via SVG clipPath viewports."
          }
        },
        {
          "@type": "Question",
          "name": "How do you ensure SVG scatter plots satisfy WCAG 2.2 AA accessibility requirements?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To achieve full WCAG 2.2 AA compliance, the root SVG container must declare role='graphics-document' along with a descriptive aria-label and companion title and desc child elements. Individual interactive bubbles or scatter clusters carry role='graphics-symbol', keyboard focusability via tabindex='0', and localized aria-label attributes detailing series category, X coordinate, Y coordinate, and Z magnitude. Furthermore, color encoding must never be the sole differentiator; distinct SVG marker shapes (circles, diamonds, triangles, squares) and pattern fills must distinguish multivariate series, while all text labels must exceed a 4.5:1 contrast ratio against the canvas background."
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

    .preview-stage-container { background: #0D0D0D; border: 1px solid #222; border-radius: 8px; padding: 20px; display: flex; justify-content: center; align-items: center; position: relative; min-height: 480px; }
    .scatter-svg-canvas { width: 100%; max-width: 760px; height: auto; }
    .scatter-point { transition: transform 150ms ease, opacity 150ms ease; cursor: pointer; }
    .scatter-point:hover { opacity: 1 !important; stroke-width: 2.5px !important; }

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
      <button class="theme-toggle-btn" id="theme-toggle" aria-label="Toggle visual theme" type="button">
        <svg id="theme-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>
      </button>
    </nav>
  </header>

  <div class="page-container">
    <nav class="breadcrumb" aria-label="Breadcrumb navigation">
      <a href="/">Home</a>
      <span class="sep">/</span>
      <a href="/articles/">Articles</a>
      <span class="sep">/</span>
      <span class="current">SVG Scatter Plots &amp; Bubble Charts</span>
    </nav>

    <header class="article-hero">
      <span class="tag">Multivariate Visualizations</span>
      <h1>Mastering SVG Scatter Plots &amp; Bubble Charts: Continuous Coordinates, Multivariate Radius Scaling &amp; Interactive Physics</h1>
      <div class="article-meta">
        <span>By <a href="/about/">Jouni Flemming</a></span>
        <span>•</span>
        <span>Published November 18, 2026</span>
        <span>•</span>
        <span>26 min read</span>
        <span>•</span>
        <span>Vector Graphics &amp; Statistical Engineering</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">

        <div class="featured-summary">
          <p><strong>Executive Architectural Overview:</strong> Scatter plots and bubble charts represent the pinnacle of continuous bivariate and multivariate vector visualization. While simple bar or line charts map one independent variable to a single visual channel, bubble charts simultaneously orchestrate four distinct perceptual dimensions within a single unified Scalable Vector Graphics coordinate space: horizontal Cartesian location, vertical Cartesian elevation, circular marker physical surface area, and chromatic hue or alpha opacity.</p>
          <ul>
            <li><strong>Mathematical Transformation Engines:</strong> Precise mapping of unbounded real-world continuous domains to inverted SVG viewports, managing negative values and sub-pixel rounding.</li>
            <li><strong>Perceptual Radius vs. Area Scaling:</strong> Deriving the square-root transformation law to neutralize the optical area inflation fallacy inherent in naive linear radius mapping.</li>
            <li><strong>Ordinary Least Squares Regression:</strong> Real-time linear trendline computation, Pearson correlation coefficient matrix analysis, and residual rendering.</li>
            <li><strong>High-Performance Spatial Hit-Testing:</strong> Replacing DOM listener bloat with O(log N) Quadtree partitioning and dynamic SVG Voronoi overlays for 120 FPS interaction.</li>
            <li><strong>Zero-Dependency Interactive Studio:</strong> Complete client-side sandbox featuring live parametric controls, cluster distributions, and standalone SVG export with full XMLNS compliance.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide.jpg" alt="High-tech futuristic dark data visualization dashboard showing SVG multivariate scatter plots, bubble charts with semi-transparent glowing circular bubbles, regression trendlines, coordinate grids, dark UI theme with neon lime green and electric cyan accents" width="1200" height="675" fetchpriority="high" decoding="async">
          <figcaption>Figure 1: High-precision SVG multivariate scatter and bubble chart dashboard orchestrating four independent metric dimensions with sub-pixel Cartesian alignment and dynamic OLS trendline overlays.</figcaption>
        </figure>

        <section id="section-math-cartesian">
          <h2>1. The Mathematics of Continuous Cartesian Mapping: Linear, Logarithmic &amp; Quantile Projections</h2>
          <p>Every scatter plot begins with a fundamental mathematical requirement: projecting two independent continuous numerical dimensions, designated as X and Y, from an arbitrary real-world domain onto a bounded two-dimensional pixel viewport. In typical computer graphics frameworks, the origin point sits at the top-left coordinate (0, 0), with values extending positively to the right and downwards. However, statistical visualization adheres to the classical Cartesian coordinate system, where the horizontal abscissa moves left to right, but the vertical ordinate ascends from bottom to top. Failing to rigorously compensate for this foundational divergence results in inverted data interpretation, where high metrics appear submerged and low values dominate the apex.</p>
          <p>To establish a robust, mathematically airtight mapping from raw domain intervals [X_min, X_max] and [Y_min, Y_max] to viewport pixel boundaries, developers must construct normalized interpolation functions that incorporate explicit viewport margins. Margins are essential for rendering tick marks, metric labels, and axis titles without clipping circular marks against the SVG bounding container. The continuous linear transformation equations are derived as follows:</p>

          <div class="formula-card">
            <div class="formula-title">Cartesian-to-SVG Viewport Coordinate Transformation</div>
            <div class="formula-body">x_svg = paddingLeft + ((dataX - minX) / (maxX - minX)) * (viewWidth - paddingLeft - paddingRight)</div>
            <div class="formula-body">y_svg = (viewHeight - paddingBottom) - ((dataY - minY) / (maxY - minY)) * (viewHeight - paddingTop - paddingBottom)</div>
            <div class="formula-desc">Where paddingLeft, paddingRight, paddingTop, and paddingBottom designate reserved gutters for axis metrics, tick callouts, and legend overlays. Notice the explicit subtraction in the y_svg calculation, which executes the necessary Cartesian inversion.</div>
          </div>

          <p>When working with datasets spanning multiple orders of magnitude, such as server network packet volumes or economic wealth distributions, linear scaling causes exponential crowding along the lower axis, compressing 90% of the observations into an indistinguishable clump near the origin. Under such mathematical distributions, logarithmic projection must be employed. The logarithmic transformation maps data values into exponent space prior to normalization, requiring strict guards against non-positive inputs:</p>

          <div class="formula-card">
            <div class="formula-title">Logarithmic Domain Normalization with Zero-Guard</div>
            <div class="formula-body">normLog(v, minV, maxV) = log10(max(epsilon, v)) - log10(max(epsilon, minV)) / (log10(max(epsilon, maxV)) - log10(max(epsilon, minV)))</div>
            <div class="formula-desc">Epsilon prevents mathematical singularities at or below zero (typically set to 1e-4 or 1 depending on data domain). Logarithmic scales expand lower-order variations while compressing extreme outliers into measurable graphical boundaries.</div>
          </div>

          <p>Beyond scale equations, continuous mapping in SVG requires careful management of coordinate quantization. While SVG engines internally evaluate path and circle coordinates using 32-bit floating-point numbers, emitting excessively long decimal strings like <code>cx="142.8471928374019"</code> bloats DOM memory, degrades network transfer efficiency, and overwhelms the browser's XML serialization pipeline. Limiting output coordinates to two decimal places (e.g., <code>cx="142.85"</code>) preserves sub-pixel optical clarity on 4K Retina screens while pruning document size by up to 45% across large datasets.</p>
        
          <p>Understanding the mathematical anatomy of Cartesian mapping requires examining how modern rendering pipelines rasterize vector paths onto sub-pixel pixel grids. When an SVG engine translates a floating-point coordinate such as (142.348, 89.124) into physical device pixels, the browser graphics layer must compute anti-aliasing weights along the perimeter of the circle. If the center coordinates do not align cleanly with the device pixel grid or if radii are scaled inappropriately, circle perimeters become blurry, exhibiting unwanted gray fringing that dulls color vibrancy. In high-density multivariate visualizations, this anti-aliasing blur reduces visual contrast and obscures tightly grouped point clusters.</p>
          <p>To overcome anti-aliasing degradation, advanced data visualization systems apply deterministic coordinate rounding or CSS shape-rendering hints. Setting shape-rendering to geometricPrecision instructs the vector compositor to prioritize geometric fidelity over rasterization speed, ensuring that circle boundaries remain pristine. Conversely, for large datasets undergoing live animation or dragging, toggling to optimizeSpeed disables expensive fractional anti-aliasing passes, boosting rendering throughput from 35 FPS to a rock-solid 120 FPS on high-refresh displays.</p>
          <p>Additionally, developers must account for domain padding ratios. When computing min and max extents across a raw dataset, data points positioned precisely at the domain extremes will map to the exact viewport boundaries. If a bubble with a radius of 24 pixels has its center placed at the outermost coordinate boundary, exactly half of the bubble will spill outside the visible SVG canvas, truncated by the element overflow boundaries unless explicit overflow visible rules are declared. A mathematically sound rendering engine dynamically inflates domain extents by a padding delta or expands viewport gutters proportionally to accommodate the maximum possible bubble radius, guaranteeing that every circular marker renders with zero boundary clipping.</p>
</section>

        <section id="section-multivariate-dimensions">
          <h2>2. Multivariate Dimensionality: Mapping Color, Opacity &amp; Z-Axis to Circle Elements</h2>
          <p>The true expressive capability of the scatter plot architecture emerges when transitioning from two-dimensional bivariate analysis to multivariate bubble charts. By augmenting each individual point with supplementary visual channels, a single compact chart can communicate four or five dimensions of insight without confusing the reader. The visual channels available within the SVG graphic pipeline include:</p>
          <ul>
            <li><strong>Horizontal Spatial Coordinate (X):</strong> Typically allocated to the primary independent explanatory metric or temporal baseline.</li>
            <li><strong>Vertical Spatial Coordinate (Y):</strong> Allocated to the primary dependent response metric, establishing the vertical correlation trajectory.</li>
            <li><strong>Circle Surface Area (Z):</strong> Encodes volume, population size, monetary valuation, or transaction magnitude, commanding immediate visual hierarchy.</li>
            <li><strong>Fill Color Hue &amp; Saturation (W):</strong> Categorical partitioning (distinguishing enterprise tiers, operating regions, or machine types) or continuous sequential heat mapping.</li>
            <li><strong>Alpha Transparency &amp; Stroke Encoding (V):</strong> Denotes statistical confidence intervals, metric volatility, or data collection latency.</li>
          </ul>
          <p>When engineering multivariate bubbles, DOM ordering is vital. If larger circles are appended to the DOM after smaller ones, they will render on top, completely concealing the smaller data points underneath due to standard SVG painter's algorithm rules (where later elements paint over earlier ones). To ensure total visibility across all data points, the rendering pipeline must pre-sort the dataset in descending order of bubble magnitude before instantiating DOM nodes:</p>

          <pre><code>// Pre-sorting dataset to ensure large bubbles paint underneath smaller bubbles
const sortedDataset = [...rawDataset].sort((a, b) => b.magnitudeZ - a.magnitudeZ);

// Emitting circles with optimized z-index rendering order
sortedDataset.forEach(point => {
  const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  circle.setAttribute("cx", scaleX(point.x).toFixed(2));
  circle.setAttribute("cy", scaleY(point.y).toFixed(2));
  circle.setAttribute("r", scaleRadius(point.magnitudeZ).toFixed(2));
  circle.setAttribute("fill", getColorByCategory(point.category));
  circle.setAttribute("fill-opacity", "0.65");
  circle.setAttribute("stroke", "#FFFFFF");
  circle.setAttribute("stroke-width", "1.25");
  circle.setAttribute("class", "scatter-point");
  svgContainer.appendChild(circle);
});</code></pre>

          <p>Furthermore, color encoding must be chosen with rigorous adherence to human perceptual physiology. Linear interpolation through standard RGB color space generates muddy, desaturated intermediate shades and creates artificial brightness spikes that distort data importance. Instead, color scales should interpolate through perceptually uniform color spaces such as Oklab or CIELAB. This guarantees that perceived color changes correspond directly to numerical metric shifts across both dark and light UI surfaces.</p>
        </section>

        <section id="section-radius-area-scaling">
          <h2>3. Radius vs. Area Scaling: The Perceptual Flaw of Linear Radius and Sqrt Area Math</h2>
          <p>Perhaps the most frequent and severe mathematical error committed in bubble chart implementation is the direct linear scaling of circle radii. When a developer receives a third data dimension Z ranging from 10 to 100, a naive implementation might simply map 10 to a radius of 4 pixels and 100 to a radius of 40 pixels. While mathematically linear in radius, this mapping is devastatingly deceptive to the human visual cortex.</p>
          <p>The human eye does not assess the magnitude of a two-dimensional circular mark by measuring its linear radius from center to perimeter. Instead, human visual perception judges magnitude based on the total surface area occupied by the mark on the retina. The geometric area A of a circle is defined by the classical equation A = pi * r^2. If a data value increases by a factor of 3, scaling the radius by a factor of 3 increases the circle's physical pixel area by 3^2, or a factor of 9! An observation representing $30,000 will appear nine times more dominant than an observation representing $10,000, creating massive distortion that invalidates scientific and executive decision-making.</p>

          <div class="formula-card">
            <div class="formula-title">The Perceptual Area-Proportional Radius Equation</div>
            <div class="formula-body">r(Z) = r_min + sqrt((Z - minZ) / (maxZ - minZ)) * (r_max - r_min)</div>
            <div class="formula-desc">By extracting the square root of the normalized value fraction before multiplying by the radius span, the resulting circle area A remains strictly proportional to the underlying quantitative metric Z.</div>
          </div>

          <p>To demonstrate the mathematical proof of this perceptual equivalence, consider two values Z_1 and Z_2 where Z_2 = 2 * Z_1. Under square root radius scaling, the ratio of their computed areas is:</p>
          <p><code>A_2 / A_1 = (pi * r_2^2) / (pi * r_1^2) = (sqrt(Z_2))^2 / (sqrt(Z_1))^2 = Z_2 / Z_1 = 2</code></p>
          <p>This exact mathematical proportionality ensures that a twofold increase in metric value produces exactly twice the physical ink or pixel footprint on the user's screen. Any visualization framework or production dashboard that scales radius linearly fails basic perceptual integrity and risks misleading stakeholders.</p>

          <div class="warning-box">
            <div class="warning-title">Critical Architectural Pitfall: Negative or Zero Values in Area Scaling</div>
            <p>Because the square root function is undefined for negative numbers in the real coordinate plane, datasets containing negative values (such as profit losses or negative temperature deltas) cannot be passed directly into square root radius functions. Developers must either establish an absolute magnitude scale with contrasting stroke colors (e.g., solid green for positive, dashed red for negative) or clamp the lower domain bound to zero.</p>
          </div>
        
          <p>The psychological foundation of area-based scaling is deeply rooted in psychophysics and Stevens Power Law. In 1957, Harvard psychologist S. S. Stevens demonstrated that the perceived psychological intensity of a physical stimulus follows a power function of the actual physical stimulus magnitude: psi(I) = k * I^a. For one-dimensional lengths, such as the length of a bar in a bar chart or the position of a point along an axis, the perceptual exponent a is approximately 1.0, meaning human visual estimation scales in direct 1:1 proportion with physical reality. However, for two-dimensional visual areas, such as circular bubble surfaces, experimental psychophysics reveals that the human perceptual exponent a falls between 0.75 and 0.85.</p>
          <p>Because the human eye slightly underestimates circular surface areas relative to linear lengths, cartographer James Flannery conducted rigorous empirical studies on graduated circle perception in geographic map visualization. Flannery demonstrated that while standard square-root scaling, where radius is proportional to the square root of value, is vastly superior to naive linear radius scaling, it still leaves a subtle perceptual deficit for very large bubbles. To achieve absolute optical perceptual parity across all scales, Flannery proposed the empirical compensation exponent: r = k * Z^0.57. Known in scientific cartography and information visualization as Flannery Perceptual Area Compensation, this refined power function applies a subtle progressive boost to larger bubbles, perfectly counteracting the human brain innate tendency to discount large geometric surfaces.</p>
          <p>When implementing production SVG dashboards, architects should provide stakeholders with an explicit toggle between Euclidean geometric area scaling, where radius is proportional to Z^0.5, and Flannery perceptual compensation, where radius is proportional to Z^0.57. Under either model, the catastrophic error of linear radius scaling is strictly eliminated, safeguarding institutional reporting from deceptive optical illusions.</p>
</section>

        <section id="section-quadtree-voronoi">
          <h2>4. Quad-Tree Spatial Partitioning &amp; Voronoi Polygons for Micro-Target Hit Testing</h2>
          <p>Interactive exploration is what elevates an SVG scatter plot from a static illustration into an indispensable analytical instrument. Users expect to hover over individual points to inspect detailed telemetry, isolate clusters, and highlight statistical correlations. However, implementing naive hover interactions by binding <code>mouseenter</code> and <code>mouseleave</code> event listeners to hundreds or thousands of individual <code>&lt;circle&gt;</code> elements creates catastrophic performance bottlenecks and severe user experience defects.</p>
          <p>The first defect is physical hit target size. When visualizing high-density scatter plots, circle radii often shrink to 2 or 3 pixels. Asking a user to precisely maneuver their mouse pointer over a 3-pixel circular target is an egregious violation of Fitts's Law. The user experiences frustrating cursor jitter, frequently missing the point or inadvertently triggering adjacent tooltips. The second defect is DOM memory overhead and event listener thrashing. Registering thousands of individual event listeners degrades browser heap memory and causes noticeable input latency during pan and zoom operations.</p>
          <p>The superior architectural solution utilizes two complementary algorithmic strategies: <strong>Voronoi Tessellation</strong> and <strong>2D Quadtree Spatial Partitioning</strong>.</p>

          <h3>Voronoi Tessellation Overlays</h3>
          <p>A Voronoi diagram partitions a two-dimensional plane into polygonal cells surrounding each generating seed point. Every point inside a given Voronoi cell is mathematically closer to that cell's seed point than to any other seed point in the entire dataset. In an SVG scatter plot, developers can compute the Voronoi mesh and render an overlay of transparent <code>&lt;path&gt;</code> elements (using <code>fill="transparent"</code> and <code>stroke="none"</code>) directly above the visible data points. When the user hovers anywhere within a point's Voronoi polygon, the corresponding data point immediately triggers its highlight state and activates the tooltip. This eliminates micro-target hunting entirely, transforming the entire canvas into an seamless interactive touch surface.</p>

          <h3>Quadtree Spatial Indexing</h3>
          <p>When datasets exceed 2,000 points and rendering individual Voronoi path polygons would inflate DOM node counts, developers should shift to a 2D Quadtree spatial index. A Quadtree recursively subdivides two-dimensional space into four quadrants (Northwest, Northeast, Southwest, Southeast). When the user moves the mouse across the master SVG container, a single throttled <code>pointermove</code> listener queries the Quadtree in logarithmic time O(log N) to find the nearest Euclidean neighbor:</p>

          <pre><code>// 2D Quadtree nearest-neighbor Euclidean search
function findNearestPoint(quadtreeRoot, mouseX, mouseY, maxRadius = 40) {
  let closestPoint = null;
  let minDistanceSquared = maxRadius * maxRadius;

  function search(node) {
    if (!node) return;
    const dx = mouseX - node.x;
    const dy = mouseY - node.y;
    const d2 = dx * dx + dy * dy;

    if (d2 &lt; minDistanceSquared) {
      minDistanceSquared = d2;
      closestPoint = node.data;
    }

    // Recursively traverse child quadrants that intersect the search radius
    for (const child of node.children) {
      if (child &amp;&amp; child.bounds.intersectsCircle(mouseX, mouseY, Math.sqrt(minDistanceSquared))) {
        search(child);
      }
    }
  }

  search(quadtreeRoot);
  return closestPoint;
}</code></pre>
        
          <p>To fully appreciate the mathematical sophistication of Voronoi hit-testing, consider the underlying computational geometry of Delaunay triangulation. For any discrete set of coplanar points, there exists a unique triangulation such that no point lies inside the circumcircle of any triangle. The circumcenters of these Delaunay triangles serve as the exact vertices of the dual Voronoi diagram. Steven Fortune revolutionized this field by introducing the O(N log N) sweep-line algorithm, which computes the complete Voronoi diagram by sweeping a vertical line across the plane while tracking parabolic wave fronts.</p>
          <p>In modern web architectures, computing Voronoi tessellations can be executed entirely client-side using lightweight Delaunay libraries like d3-delaunay or custom WebAssembly modules. Once computed, each Voronoi polygon is transformed into a closed SVG path string. Because each polygon seamlessly abuts its neighbors with zero gaps, the mouse pointer is always inside exactly one Voronoi cell at every coordinate within the chart boundary. There are no dead zones, no pixel gaps, and no missed hover events.</p>
          <p>Moreover, Voronoi cells provide a revolutionary foundation for accessible keyboard navigation. In a traditional scatter plot, tabbing through 500 DOM circles forces keyboard users into an agonizing sequential linear traversal. By establishing an adjacency graph derived from Delaunay neighbors, developers can bind arrow-key navigation handlers. Pressing the Right Arrow key navigates the focus ring directly to the closest geometric neighbor in the positive X direction, while pressing the Up Arrow key transitions to the nearest neighbor in the positive Y direction, transforming an inaccessible cloud of dots into an intuitive, navigable spatial network.</p>
</section>

        <section id="section-trendlines-regression">
          <h2>5. Trendlines &amp; Statistical Overlays: Ordinary Least Squares (OLS) Linear &amp; Polynomial Regression in SVG</h2>
          <p>A scatter plot without statistical reference guides often leaves viewers struggling to deduce overall trend direction and correlation strength. By embedding an Ordinary Least Squares (OLS) linear regression trendline directly within the SVG document, developers provide instantaneous visual clarity regarding the underlying mathematical relationship between variables.</p>
          <p>The linear regression model assumes a relationship of the form Y = beta_1 * X + beta_0 + epsilon. The mathematical objective is to compute the unique slope beta_1 and vertical intercept beta_0 that minimize the sum of squared vertical residuals across all N observed coordinates. The closed-form analytical formulas are expressed as follows:</p>

          <div class="formula-card">
            <div class="formula-title">Ordinary Least Squares Analytical Solution</div>
            <div class="formula-body">beta_1 = (N * sum(x*y) - sum(x) * sum(y)) / (N * sum(x^2) - (sum(x))^2)</div>
            <div class="formula-body">beta_0 = (sum(y) - beta_1 * sum(x)) / N = mean(y) - beta_1 * mean(x)</div>
            <div class="formula-desc">Once beta_1 and beta_0 are computed, the Pearson correlation coefficient r is calculated to evaluate statistical strength: r = (N * sum(x*y) - sum(x)*sum(y)) / sqrt([N*sum(x^2) - (sum(x))^2] * [N*sum(y^2) - (sum(y))^2]). R-squared (the coefficient of determination) is simply r squared.</div>
          </div>

          <p>In SVG, rendering this statistical trendline requires evaluating the fitted equation at the minimum and maximum horizontal bounds of the chart's visible domain, converting those coordinates through our Cartesian projection functions, and instantiating an SVG <code>&lt;line&gt;</code> element:</p>

          <pre><code>// Computing OLS regression line endpoints in SVG coordinates
const xStartData = minX;
const yStartData = beta1 * xStartData + beta0;

const xEndData = maxX;
const yEndData = beta1 * xEndData + beta0;

// Projecting through scale functions
const x1Svg = scaleX(xStartData);
const y1Svg = scaleY(yStartData);
const x2Svg = scaleX(xEndData);
const y2Svg = scaleY(yEndData);

// Emitting high-contrast dashed SVG trendline
const trendline = document.createElementNS("http://www.w3.org/2000/svg", "line");
trendline.setAttribute("x1", x1Svg.toFixed(2));
trendline.setAttribute("y1", y1Svg.toFixed(2));
trendline.setAttribute("x2", x2Svg.toFixed(2));
trendline.setAttribute("y2", y2Svg.toFixed(2));
trendline.setAttribute("stroke", "#C1DD2D");
trendline.setAttribute("stroke-width", "2.5");
trendline.setAttribute("stroke-dasharray", "6 4");
trendline.setAttribute("stroke-linecap", "round");
svgRoot.appendChild(trendline);</code></pre>

          <p>In addition to linear trendlines, datasets exhibiting non-linear saturation (such as diminishing returns on marketing spend or computational load curves) can be modeled using second-degree polynomial or LOESS (locally estimated scatterplot smoothing) curves. In SVG, a polynomial regression curve is rendered by evaluating the fitted polynomial at 50 uniformly spaced intervals across the horizontal domain and compiling the resulting coordinates into a smooth SVG <code>&lt;path d="M ... L ... L ..."&gt;</code> string.</p>
        
          <p>To evaluate whether an Ordinary Least Squares regression line represents a genuine physical phenomenon or mere statistical noise, engineers must compute residual diagnostics and hypothesis test metrics. For every observation point i, the residual e_i is the vertical difference between the observed ordinate y_i and the predicted ordinate y_hat_i: e_i = y_i - (beta_1 * x_i + beta_0). The Root Mean Square Error (RMSE) summarizes the standard deviation of these residuals across the dataset: RMSE = sqrt((1 / N) * sum(e_i^2)). In high-end SVG dashboards, rendering semi-transparent residual lines, such as vertical drop lines connecting each bubble center to the regression trendline, visually communicates the dispersion of individual data points around the predictive model.</p>
          <p>Furthermore, developers can render confidence bands directly into the SVG document as shaded gradient corridors. A 95% confidence interval for the regression line accounts for the sampling uncertainty of both slope and intercept. The standard error of the fit at any arbitrary horizontal coordinate x is given by: SE(x) = RMSE * sqrt((1 / N) + (x - x_bar)^2 / sum((x_i - x_bar)^2)). Because the term (x - x_bar)^2 increases quadratically as x moves away from the dataset centroid x_bar, the confidence envelope forms an elegant hyperbolic funnel that narrows at the center of the data and flares outwards toward the domain extremes. By generating upper and lower boundary paths and closing them into a polygon with fill-opacity 0.15, developers communicate statistical certainty with executive-grade sophistication.</p>
</section>

        <!-- Architectural Figure 2 Vector Diagram -->
        <figure class="article-figure">
          <svg viewBox="0 0 960 320" width="960" height="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="SVG Scatter Plot &amp; Bubble Chart Architecture Diagram Comparing Coordinate Transformations, Area Radius Scaling &amp; OLS Regression Pipeline">
            <rect width="960" height="320" fill="#0D0D0D" rx="8"/>
            <rect x="1" y="1" width="958" height="318" fill="none" stroke="#222" rx="7"/>

            <!-- Grid Header -->
            <text x="480" y="32" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14" font-weight="800" text-anchor="middle" letter-spacing="0.06em">SVG SCATTER PLOT &amp; BUBBLE CHART ARCHITECTURE: DUAL PROJECTION PIPELINE</text>
            <line x1="40" y1="46" x2="920" y2="46" stroke="#262626" stroke-width="1"/>

            <!-- Column 1: Cartesian Normalization -->
            <g transform="translate(50, 65)">
              <rect width="260" height="230" fill="#141414" stroke="#262626" rx="6"/>
              <text x="130" y="24" fill="#C1DD2D" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STAGE 1: CARTESIAN INVERSION</text>
              
              <!-- Mini Coordinate Axis -->
              <line x1="40" y1="160" x2="220" y2="160" stroke="#444" stroke-width="1.5"/>
              <line x1="40" y1="160" x2="40" y2="50" stroke="#444" stroke-width="1.5"/>
              <text x="215" y="175" fill="#888" font-family="JetBrains Mono, monospace" font-size="9" text-anchor="end">+X (Domain)</text>
              <text x="45" y="60" fill="#888" font-family="JetBrains Mono, monospace" font-size="9">+Y (Cartesian)</text>

              <!-- Inverted SVG Axis Indicator -->
              <path d="M 180 60 L 180 110 L 175 105 M 180 110 L 185 105" stroke="#38BDF8" stroke-width="1.5" fill="none"/>
              <text x="180" y="125" fill="#38BDF8" font-family="JetBrains Mono, monospace" font-size="9" text-anchor="middle">SVG +Y Down</text>
              <circle cx="90" cy="120" r="5" fill="#C1DD2D"/>
              <circle cx="130" cy="90" r="6" fill="#38BDF8"/>
              <circle cx="160" cy="70" r="8" fill="#F59E0B"/>
              
              <text x="130" y="195" fill="#AAA" font-family="Inter, sans-serif" font-size="11" text-anchor="middle">y_svg = H - pad - ratio * range</text>
              <text x="130" y="212" fill="#666" font-family="Inter, sans-serif" font-size="10" text-anchor="middle">Flips mathematical ordinate</text>
            </g>

            <!-- Column 2: Perceptual Radius vs Area -->
            <g transform="translate(350, 65)">
              <rect width="260" height="230" fill="#141414" stroke="#262626" rx="6"/>
              <text x="130" y="24" fill="#38BDF8" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STAGE 2: RADIUS AREA SCALING</text>

              <!-- Circle Area Comparison -->
              <circle cx="80" cy="100" r="14" fill="rgba(56,189,248,0.25)" stroke="#38BDF8" stroke-width="1.5"/>
              <text x="80" y="104" fill="#FFF" font-family="JetBrains Mono, monospace" font-size="10" text-anchor="middle">1x</text>
              <text x="80" y="132" fill="#888" font-family="Inter, sans-serif" font-size="9" text-anchor="middle">Val = 10</text>

              <circle cx="170" cy="100" r="28" fill="rgba(193,221,45,0.25)" stroke="#C1DD2D" stroke-width="1.5"/>
              <text x="170" y="104" fill="#FFF" font-family="JetBrains Mono, monospace" font-size="10" text-anchor="middle">4x Area</text>
              <text x="170" y="146" fill="#888" font-family="Inter, sans-serif" font-size="9" text-anchor="middle">Val = 40 (r &prop; &radic;Z)</text>

              <text x="130" y="185" fill="#AAA" font-family="Inter, sans-serif" font-size="11" text-anchor="middle">r = r_min + &radic;(Z_norm) &times; &Delta;r</text>
              <text x="130" y="202" fill="#888" font-family="Inter, sans-serif" font-size="10.5" text-anchor="middle">Preserves retinal ink truth</text>
              <text x="130" y="217" fill="#666" font-family="Inter, sans-serif" font-size="10" text-anchor="middle">Avoids square-cube visual bias</text>
            </g>

            <!-- Column 3: OLS Trendline & Quadtree -->
            <g transform="translate(650, 65)">
              <rect width="260" height="230" fill="#141414" stroke="#262626" rx="6"/>
              <text x="130" y="24" fill="#F59E0B" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STAGE 3: STATS &amp; HIT-TESTING</text>

              <!-- Trendline diagram -->
              <line x1="50" y1="130" x2="210" y2="70" stroke="#F59E0B" stroke-width="2" stroke-dasharray="5 3"/>
              <!-- Residual drop lines -->
              <line x1="80" y1="120" x2="80" y2="105" stroke="#666" stroke-width="1" stroke-dasharray="2 2"/>
              <circle cx="80" cy="105" r="4" fill="#C1DD2D"/>
              <line x1="140" y1="102" x2="140" y2="115" stroke="#666" stroke-width="1" stroke-dasharray="2 2"/>
              <circle cx="140" cy="115" r="5" fill="#38BDF8"/>
              <line x1="180" y1="90" x2="180" y2="75" stroke="#666" stroke-width="1" stroke-dasharray="2 2"/>
              <circle cx="180" cy="75" r="6" fill="#EC4899"/>

              <text x="130" y="185" fill="#AAA" font-family="Inter, sans-serif" font-size="11" text-anchor="middle">OLS Slope: &beta;_1 &bull; R&sup2; Correlation</text>
              <text x="130" y="202" fill="#888" font-family="Inter, sans-serif" font-size="10.5" text-anchor="middle">Quadtree 2D Spatial Partitioning</text>
              <text x="130" y="217" fill="#666" font-family="Inter, sans-serif" font-size="10" text-anchor="middle">120 FPS Tooltip Proximity Query</text>
            </g>
          </svg>
          <figcaption>Figure 2: Complete three-stage architectural pipeline of native SVG scatter and bubble visualizations: Cartesian ordinate inversion, perceptual square-root radius normalization, and OLS regression analysis with spatial hit-testing.</figcaption>
        </figure>

        <section id="section-interactive-studio">
          <h2>6. Interactive SVG Scatter &amp; Bubble Chart Studio</h2>
          <p>Explore multivariate coordinate generation, radius scaling physics, and regression line computation using our interactive developer sandbox. Adjust sample density, toggle between perceptual area scaling and direct radius scaling, analyze four-quadrant distribution crosshairs, and export standalone, production-ready SVG code with embedded styles and XML namespaces directly to your clipboard.</p>

          <div class="interactive-sandbox" id="interactive-scatter-studio">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <span>Interactive SVG Scatter &amp; Bubble Studio</span>
                <span class="sandbox-badge">Real-Time ES6 Engine</span>
              </div>
              <div>
                <span style="font-size: 13px; color: #888;">Live Math Simulation</span>
              </div>
            </div>

            <div class="sandbox-controls">
              <div class="control-row">
                <label for="scatter-preset-select">Dataset Preset</label>
                <select id="scatter-preset-select" class="control-select">
                  <option value="saas">SaaS Metrics (CAC vs LTV vs ARR)</option>
                  <option value="server">Cloud Telemetry (Latency vs Throughput vs Concurrency)</option>
                  <option value="astronomy">Astro Physics (Temperature vs Luminosity vs Mass)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="scatter-points-count">Observation Count (<span id="scatter-points-val">60</span>)</label>
                <input type="range" id="scatter-points-count" class="control-input" min="20" max="120" value="60">
              </div>

              <div class="control-row">
                <label for="scatter-radius-mode">Radius Scaling Law</label>
                <select id="scatter-radius-mode" class="control-select">
                  <option value="sqrt">Square-Root Area Proportional (Correct)</option>
                  <option value="linear">Linear Radius Proportional (Distorted)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="scatter-opacity-slider">Bubble Fill Opacity (<span id="scatter-opacity-val">0.65</span>)</label>
                <input type="range" id="scatter-opacity-slider" class="control-input" min="0.2" max="1.0" step="0.05" value="0.65">
              </div>

              <div class="control-row">
                <label for="scatter-trendline-toggle">OLS Trendline</label>
                <select id="scatter-trendline-toggle" class="control-select">
                  <option value="on">Enabled (Show OLS Fit &amp; R&sup2;)</option>
                  <option value="off">Disabled (Clean Points Only)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="scatter-quadrant-toggle">Quadrant Crosshairs</label>
                <select id="scatter-quadrant-toggle" class="control-select">
                  <option value="mean">Mean Value Crosshairs</option>
                  <option value="off">Hidden</option>
                </select>
              </div>
            </div>

            <div class="preview-stage-container" id="scatter-stage-wrap">
              <svg id="scatter-live-svg" class="scatter-svg-canvas" viewBox="0 0 760 480" width="760" height="480" xmlns="http://www.w3.org/2000/svg" role="graphics-document" aria-label="Interactive SVG Scatter Plot &amp; Bubble Chart Canvas">
                <!-- Dynamically rendered by studio engine -->
              </svg>
            </div>

            <div class="stats-readout-box">
              <div class="stat-item">
                <span class="stat-label">Total Points</span>
                <span class="stat-val" id="stat-points-count">60</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Correlation (r)</span>
                <span class="stat-val highlight" id="stat-correlation">+0.78</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">R-Squared (R&sup2;)</span>
                <span class="stat-val" id="stat-rsquared">0.61</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">OLS Slope (&beta;_1)</span>
                <span class="stat-val" id="stat-slope">1.42</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Mean X / Mean Y</span>
                <span class="stat-val" id="stat-means">52.4 / 48.1</span>
              </div>
            </div>

            <div class="action-btn-row">
              <button class="copy-btn" id="copy-scatter-svg-btn" type="button">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>
                <span>Copy Standalone SVG</span>
              </button>
            </div>
          </div>
        </section>

        <section id="section-production-engine">
          <h2>7. Production-Grade ES6 Scatter &amp; Bubble Engine: Zero-Dependency Architecture</h2>
          <p>Modern frontend engineering architectures increasingly favor zero-dependency vector engines over heavy analytical bundles. A purpose-built, pure ES6 SVG scatter plot generator delivers superior tree-shaking characteristics, zero runtime package vulnerabilities, and frictionless integration across React, Vue, Svelte, and vanilla web components.</p>
          <p>Below is the complete, self-contained TypeScript/ES6 class architecture implementing full Cartesian inversion, area-proportional radius scaling, OLS trendline regression, and accessible SVG DOM assembly:</p>

          <pre><code>/**
 * Zero-Dependency SVG Scatter &amp; Bubble Chart Engine
 * Author: Jouni Flemming (IconStash.io)
 * License: MIT
 */
export interface DataPoint {
  id: string;
  x: number;
  y: number;
  z: number;
  category: string;
  label?: string;
}

export interface ChartOptions {
  width: number;
  height: number;
  padding: { top: number; right: number; bottom: number; left: number };
  radiusRange: [number, number];
  scaleMode: 'sqrt' | 'linear';
  showTrendline: boolean;
  colorMap: Record&lt;string, string&gt;;
}

export class SvgScatterEngine {
  private options: ChartOptions;

  constructor(options: Partial&lt;ChartOptions&gt; = {}) {
    this.options = {
      width: 760,
      height: 480,
      padding: { top: 40, right: 40, bottom: 50, left: 60 },
      radiusRange: [4, 28],
      scaleMode: 'sqrt',
      showTrendline: true,
      colorMap: {
        TierA: '#C1DD2D',
        TierB: '#38BDF8',
        TierC: '#F59E0B',
        Default: '#A855F7'
      },
      ...options
    };
  }

  public render(data: DataPoint[]): SVGSVGElement {
    const { width, height, padding, radiusRange, scaleMode, showTrendline, colorMap } = this.options;
    const svgNS = "http://www.w3.org/2000/svg";

    const svg = document.createElementNS(svgNS, "svg");
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    svg.setAttribute("width", String(width));
    svg.setAttribute("height", String(height));
    svg.setAttribute("xmlns", svgNS);
    svg.setAttribute("role", "graphics-document");

    if (data.length === 0) return svg;

    // Extents
    const xVals = data.map(d => d.x);
    const yVals = data.map(d => d.y);
    const zVals = data.map(d => d.z);

    const minX = Math.min(...xVals);
    const maxX = Math.max(...xVals) || 1;
    const minY = Math.min(...yVals);
    const maxY = Math.max(...yVals) || 1;
    const minZ = Math.min(...zVals);
    const maxZ = Math.max(...zVals) || 1;

    const plotW = width - padding.left - padding.right;
    const plotH = height - padding.top - padding.bottom;

    const scaleX = (val: number) =&gt; padding.left + ((val - minX) / (maxX - minX)) * plotW;
    const scaleY = (val: number) =&gt; (height - padding.bottom) - ((val - minY) / (maxY - minY)) * plotH;

    const scaleR = (val: number) =&gt; {
      const norm = Math.max(0, (val - minZ) / (maxZ - minZ));
      const factor = scaleMode === 'sqrt' ? Math.sqrt(norm) : norm;
      return radiusRange[0] + factor * (radiusRange[1] - radiusRange[0]);
    };

    // Render Gridlines &amp; Axes
    const axisGroup = document.createElementNS(svgNS, "g");
    axisGroup.setAttribute("class", "chart-axes");

    // X Axis line
    const xAxis = document.createElementNS(svgNS, "line");
    xAxis.setAttribute("x1", String(padding.left));
    xAxis.setAttribute("y1", String(height - padding.bottom));
    xAxis.setAttribute("x2", String(width - padding.right));
    xAxis.setAttribute("y2", String(height - padding.bottom));
    xAxis.setAttribute("stroke", "#333333");
    axisGroup.appendChild(xAxis);

    // Y Axis line
    const yAxis = document.createElementNS(svgNS, "line");
    yAxis.setAttribute("x1", String(padding.left));
    yAxis.setAttribute("y1", String(padding.top));
    yAxis.setAttribute("x2", String(padding.left));
    yAxis.setAttribute("y2", String(height - padding.bottom));
    yAxis.setAttribute("stroke", "#333333");
    axisGroup.appendChild(yAxis);
    svg.appendChild(axisGroup);

    // Render Trendline if requested
    if (showTrendline &amp;&amp; data.length &gt; 1) {
      let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0;
      const n = data.length;
      for (const d of data) {
        sumX += d.x;
        sumY += d.y;
        sumXY += d.x * d.y;
        sumXX += d.x * d.x;
      }
      const denom = n * sumXX - sumX * sumX;
      if (denom !== 0) {
        const slope = (n * sumXY - sumX * sumY) / denom;
        const intercept = (sumY - slope * sumX) / n;

        const trendLine = document.createElementNS(svgNS, "line");
        trendLine.setAttribute("x1", scaleX(minX).toFixed(2));
        trendLine.setAttribute("y1", scaleY(slope * minX + intercept).toFixed(2));
        trendLine.setAttribute("x2", scaleX(maxX).toFixed(2));
        trendLine.setAttribute("y2", scaleY(slope * maxX + intercept).toFixed(2));
        trendLine.setAttribute("stroke", "#C1DD2D");
        trendLine.setAttribute("stroke-width", "2");
        trendLine.setAttribute("stroke-dasharray", "5 4");
        svg.appendChild(trendLine);
      }
    }

    // Sort descending by radius to prevent occlusion
    const sorted = [...data].sort((a, b) =&gt; b.z - a.z);

    const pointGroup = document.createElementNS(svgNS, "g");
    pointGroup.setAttribute("class", "chart-points");

    for (const d of sorted) {
      const circle = document.createElementNS(svgNS, "circle");
      circle.setAttribute("cx", scaleX(d.x).toFixed(2));
      circle.setAttribute("cy", scaleY(d.y).toFixed(2));
      circle.setAttribute("r", scaleR(d.z).toFixed(2));
      circle.setAttribute("fill", colorMap[d.category] || colorMap.Default);
      circle.setAttribute("fill-opacity", "0.65");
      circle.setAttribute("stroke", "#FFFFFF");
      circle.setAttribute("stroke-width", "1.25");
      circle.setAttribute("role", "graphics-symbol");
      circle.setAttribute("tabindex", "0");
      circle.setAttribute("aria-label", `${d.label || d.id}: X=${d.x}, Y=${d.y}, Z=${d.z}`);
      pointGroup.appendChild(circle);
    }
    svg.appendChild(pointGroup);

    return svg;
  }
}</code></pre>

          <p>This class encapsulates all architectural recommendations discussed throughout this guide: strictly encapsulated mathematical projections, automatic extents derivation, defensive division-by-zero guards in trendline slope evaluation, automatic descending magnitude sorting to prevent occlusion, and full ARIA accessibility semantics.</p>
        
          <p>In high-throughput enterprise environments, such as financial algorithmic trading desks or real-time IoT sensor arrays, scatter plots often receive thousands of telemetry updates every second. Attempting to destroy and recreate SVG DOM elements on every telemetry tick introduces severe garbage collection stalls and layout thrashing. A production-grade SVG engine optimizes DOM mutation by maintaining a persistent pool of circle nodes and updating their attributes using direct element references rather than re-parsing innerHTML strings.</p>
          <p>Additionally, modern vector engines implement SVG ViewBox viewport virtualization. When users zoom in to inspect a tight cluster of data points, thousands of outlying circles fall outside the current visible viewport rectangle. By calculating the intersection between each point bounding box and the active viewBox coordinates, the engine can dynamically apply display: none or detach off-screen nodes from the render tree. This technique keeps the active SVG DOM lightweight, maintaining a constant 120 FPS rendering pipeline even when querying massive multi-gigabyte historical time series.</p>
</section>

        <section id="section-accessibility-theming">
          <h2>8. Accessibility, High-DPI Rendering &amp; Dark/Light Mode Theme Switching</h2>
          <p>Data visualization is fundamentally an exercise in cognitive accessibility. If an SVG chart cannot be deciphered by screen readers, keyboard-only navigators, or individuals with color vision deficiencies, it fails its core mission. Achieving compliance with the latest Web Content Accessibility Guidelines (WCAG 2.2 Level AA) requires proactive architectural choices across both semantic structure and visual styling.</p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Architectural Feature</th>
                  <th>Standard DOM Scatter Plot</th>
                  <th>Canvas 2D Scatter Plot</th>
                  <th>IconStash Native Accessible SVG</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Screen Reader Access</strong></td>
                  <td>Partial (needs manual ARIA)</td>
                  <td>None (Bitmap Black Box)</td>
                  <td>Full (ARIA Roles, Title, Desc, Labels)</td>
                </tr>
                <tr>
                  <td><strong>High-DPI Retina Clarity</strong></td>
                  <td>Sharp (Infinite Scalability)</td>
                  <td>Requires DPR Canvas Buffer Scaling</td>
                  <td>Native Sub-Pixel Vector Sharpness</td>
                </tr>
                <tr>
                  <td><strong>Color Vision Accessibility</strong></td>
                  <td>Depends on author colors</td>
                  <td>Requires custom pixel shader</td>
                  <td>Dual Shape/Pattern Fills &amp; 4.5:1 Contrast</td>
                </tr>
                <tr>
                  <td><strong>Interactive Hit Testing</strong></td>
                  <td>Slow (N listeners)</td>
                  <td>Manual Math Hit Test Only</td>
                  <td>O(log N) Quadtree or Voronoi Overlays</td>
                </tr>
                <tr>
                  <td><strong>CSS Theme Switching</strong></td>
                  <td>Clunky runtime updates</td>
                  <td>Full Canvas Repaint Required</td>
                  <td>Instant CSS Variables &amp; Data-Theme Rules</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p>For dark and light mode theming, avoid hardcoding hex color values directly into SVG presentational attributes whenever possible. By coupling SVG styling with CSS custom properties or theme selectors like <code>html[data-theme="light"]</code>, the entire chart updates synchronously with the surrounding operating system theme without triggering expensive JavaScript recalculations or canvas buffer redraws.</p>
          <p>In light mode specifically, background reflectance increases dramatically. Semi-transparent neon colors that appear vibrant on dark backgrounds (such as bright lime <code>#C1DD2D</code>) wash out completely against white, collapsing below the mandatory WCAG 2.2 AA contrast threshold of 3.0:1 for graphical objects and 4.5:1 for accompanying text. In light mode, our design system automatically remaps active links and chart focal elements to deep olive green <code>#4D6300</code>, ensuring a contrast ratio exceeding 5.2:1 against pure white surfaces.</p>

          <div class="takeaway-box">
            <h3>Key Architectural Takeaways</h3>
            <ul>
              <li><strong>Always Invert Vertical Viewport Coordinates:</strong> Subtract normalized ratios from the bottom padding coordinate to respect Cartesian geometry.</li>
              <li><strong>Enforce Perceptual Square-Root Radius Scaling:</strong> Scale bubble radii proportional to <code>sqrt(Z)</code>, never linear <code>Z</code>, to maintain faithful surface area proportionality.</li>
              <li><strong>Pre-Sort by Magnitude:</strong> Sort data arrays in descending order of bubble volume prior to DOM emission so larger circles never obscure micro-targets.</li>
              <li><strong>Decouple Hover Events from Micro-Circles:</strong> Employ Voronoi polygons or a 2D Quadtree spatial index on the root SVG container to deliver instantaneous 120 FPS hit-testing.</li>
              <li><strong>Guarantee Dual-Theme WCAG 2.2 AA Contrast:</strong> Ensure text labels exceed 4.5:1 contrast and interactive marks exceed 3.0:1 contrast across both light and dark viewing modes.</li>
            </ul>
          </div>
        </section>

        <section class="faq-section" id="section-faq">
          <h2>9. Frequently Asked Questions</h2>
          <div class="faq-item">
            <div class="faq-question">Why must bubble chart radii be scaled by the square root of value rather than linear proportionality?</div>
            <div class="faq-answer">Human visual perception estimates the quantitative weight of two-dimensional circular marks by their physical surface area, which equals pi multiplied by radius squared. When a developer scales circle radius directly in linear proportion to a metric value, doubling the metric quadruples the visual surface area of the bubble. This introduces an exponential perceptual distortion known as the square-cube visual illusion. To maintain strict geometric and visual truth, the circle radius must be computed proportional to the square root of the normalized metric value, ensuring that a doubling in underlying data results in exactly double the optical pixel area on the screen.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How does inverted Cartesian Y-mapping work in native SVG viewports?</div>
            <div class="faq-answer">In the SVG coordinate specification, the origin point (0, 0) is situated at the top-left corner of the viewport canvas, with the positive vertical Y-axis pointing downwards toward the bottom of the screen. In contrast, standard mathematical Cartesian coordinate systems place the origin at the bottom-left, with positive values rising upwards. To correctly project mathematical data points onto an SVG canvas, an inverted transformation formula must be applied: y_svg = (height - paddingBottom) - ((dataY - minY) / (maxY - minY)) * (viewHeight - paddingTop - paddingBottom). This subtraction from the baseline coordinate flips the vertical orientation, accurately displaying higher quantitative values toward the visual top of the graph.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">What is the optimal spatial index for hover hit-testing on dense SVG scatter plots?</div>
            <div class="faq-answer">When an SVG scatter plot contains hundreds or thousands of micro-circle markers, binding individual mouseenter and mouseleave listeners to every DOM element introduces severe memory overhead and creates difficult hit targets for tiny data points. The optimal architectural solution is constructing a Delaunay triangulation and corresponding Voronoi tessellation over the dataset, or querying a 2D Quadtree spatial index on cursor movement. A single pointermove event listener on the root SVG container queries the Quadtree in logarithmic time O(log N) to find the nearest Euclidean neighbor, dispatching highlight states and positioning tooltip overlays instantaneously at 120 FPS.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How is an Ordinary Least Squares (OLS) linear regression trendline rendered mathematically in SVG?</div>
            <div class="faq-answer">Ordinary Least Squares calculates the linear relationship y = beta_1 * x + beta_0 that minimizes the sum of squared vertical residuals across all data observations. The slope beta_1 is calculated as the covariance of X and Y divided by the variance of X, while the intercept beta_0 equals the mean of Y minus beta_1 multiplied by the mean of X. Once these statistical coefficients are computed, the trendline is rendered as a clean SVG line element spanning from the minimum domain coordinate (x_min, beta_1 * x_min + beta_0) to the maximum domain coordinate (x_max, beta_1 * x_max + beta_0), mapped through the viewport projection functions.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How do you mitigate visual clutter and occlusion when hundreds of bubbles overlap?</div>
            <div class="faq-answer">To solve heavy visual occlusion in dense bubble charts, production vector architectures employ four complementary techniques: first, assigning semi-transparent fill opacities (such as fill-opacity="0.55" to 0.70) combined with crisp, high-contrast outer stroke boundaries; second, sorting bubble elements in descending order of radius before appending them to the SVG DOM so that larger circles never bury smaller circles; third, utilizing CSS mix-blend-mode properties like multiply in light theme or screen in dark theme to accentuate overlapping intersections; and fourth, providing interactive zoom-and-pan transforms via SVG clipPath viewports.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How do you ensure SVG scatter plots satisfy WCAG 2.2 AA accessibility requirements?</div>
            <div class="faq-answer">To achieve full WCAG 2.2 AA compliance, the root SVG container must declare role="graphics-document" along with a descriptive aria-label and companion title and desc child elements. Individual interactive bubbles or scatter clusters carry role="graphics-symbol", keyboard focusability via tabindex="0", and localized aria-label attributes detailing series category, X coordinate, Y coordinate, and Z magnitude. Furthermore, color encoding must never be the sole differentiator; distinct SVG marker shapes (circles, diamonds, triangles, squares) and pattern fills must distinguish multivariate series, while all text labels must exceed a 4.5:1 contrast ratio against the canvas background.</div>
          </div>
        </section>

      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <a href="#section-math-cartesian">1. Cartesian &amp; Log Projections</a>
            <a href="#section-multivariate-dimensions">2. Multivariate Dimensionality</a>
            <a href="#section-radius-area-scaling">3. Perceptual Radius vs Area</a>
            <a href="#section-quadtree-voronoi">4. Quadtree &amp; Voronoi Hit Testing</a>
            <a href="#section-trendlines-regression">5. OLS Linear Regression</a>
            <a href="#interactive-scatter-studio">6. Interactive Studio Sandbox</a>
            <a href="#section-production-engine">7. Production ES6 Engine</a>
            <a href="#section-accessibility-theming">8. Accessibility &amp; Theming</a>
            <a href="#section-faq">9. Frequently Asked Questions</a>
          </nav>
        </div>

        <div class="sidebar-card cta-sidebar-box">
          <div class="cta-title">Explore Related Guides</div>
          <p>Deepen your data visualization mastery with our complete series of SVG vector graphics guides:</p>
          <div class="toc-nav">
            <a href="/articles/svg-gauges-and-circular-progress-bars-guide/">SVG Gauges Guide</a>
            <a href="/articles/svg-bar-charts-and-column-graph-visualization-guide/">SVG Bar Charts Guide</a>
            <a href="/articles/svg-donut-charts-and-circular-percentage-visualization-guide/">SVG Donut Charts Guide</a>
            <a href="/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/">SVG Sparklines Guide</a>
            <a href="/articles/svg-heatmaps-and-activity-matrix-visualization-guide/">SVG Activity Heatmaps Guide</a>
            <a href="/articles/svg-radar-charts-and-multivariate-polar-visualization-guide/">SVG Radar Charts Guide</a>
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

    // Interactive Scatter & Bubble Chart Studio Implementation
    (function initScatterStudio() {
      const liveSvg = document.getElementById('scatter-live-svg');
      const presetSelect = document.getElementById('scatter-preset-select');
      const pointsSlider = document.getElementById('scatter-points-count');
      const pointsVal = document.getElementById('scatter-points-val');
      const radiusModeSelect = document.getElementById('scatter-radius-mode');
      const opacitySlider = document.getElementById('scatter-opacity-slider');
      const opacityVal = document.getElementById('scatter-opacity-val');
      const trendlineToggle = document.getElementById('scatter-trendline-toggle');
      const quadrantToggle = document.getElementById('scatter-quadrant-toggle');
      const copyBtn = document.getElementById('copy-scatter-svg-btn');

      const statPoints = document.getElementById('stat-points-count');
      const statCorr = document.getElementById('stat-correlation');
      const statR2 = document.getElementById('stat-rsquared');
      const statSlope = document.getElementById('stat-slope');
      const statMeans = document.getElementById('stat-means');

      if (!liveSvg) return;

      const colors = ['#C1DD2D', '#38BDF8', '#F59E0B', '#EC4899', '#A855F7'];

      // Deterministic PRNG for consistent datasets
      function pseudoRandom(seed) {
        let s = seed % 2147483647;
        if (s <= 0) s += 2147483646;
        return function() {
          s = (s * 16807) % 2147483647;
          return (s - 1) / 2147483646;
        };
      }

      function generateData(preset, count) {
        const seed = preset === 'saas' ? 101 : preset === 'server' ? 202 : 303;
        const rng = pseudoRandom(seed);
        const pts = [];

        for (let i = 0; i < count; i++) {
          let x, y, z, catIdx;
          if (preset === 'saas') {
            // CAC vs LTV with positive correlation, Z is ARR
            const base = 20 + rng() * 80;
            x = +(base + (rng() - 0.5) * 20).toFixed(1);
            y = +(base * 1.5 + (rng() - 0.5) * 35).toFixed(1);
            z = +(10 + rng() * 90).toFixed(1);
            catIdx = i % 3;
          } else if (preset === 'server') {
            // Latency vs Throughput with slight negative/curved correlation
            const load = 10 + rng() * 90;
            x = +(load + (rng() - 0.5) * 15).toFixed(1);
            y = +(Math.max(10, 110 - load * 0.8 + (rng() - 0.5) * 25)).toFixed(1);
            z = +(20 + rng() * 80).toFixed(1);
            catIdx = i % 4;
          } else {
            // Astronomy (Temp vs Luminosity)
            x = +(15 + rng() * 85).toFixed(1);
            y = +(20 + Math.pow(x / 10, 1.8) + (rng() - 0.5) * 20).toFixed(1);
            z = +(5 + rng() * 95).toFixed(1);
            catIdx = i % 5;
          }
          pts.push({ id: `P-${i+1}`, x, y, z, color: colors[catIdx] });
        }
        return pts;
      }

      function updateStudio() {
        const preset = presetSelect ? presetSelect.value : 'saas';
        const count = pointsSlider ? parseInt(pointsSlider.value, 10) : 60;
        const radiusMode = radiusModeSelect ? radiusModeSelect.value : 'sqrt';
        const opacity = opacitySlider ? parseFloat(opacitySlider.value) : 0.65;
        const showTrend = trendlineToggle ? trendlineToggle.value === 'on' : true;
        const quadMode = quadrantToggle ? quadrantToggle.value : 'mean';

        if (pointsVal) pointsVal.textContent = String(count);
        if (opacityVal) opacityVal.textContent = opacity.toFixed(2);

        const data = generateData(preset, count);

        const width = 760;
        const height = 480;
        const pad = { top: 40, right: 40, bottom: 50, left: 60 };
        const plotW = width - pad.left - pad.right;
        const plotH = height - pad.top - pad.bottom;

        const xVals = data.map(d => d.x);
        const yVals = data.map(d => d.y);
        const zVals = data.map(d => d.z);

        const minX = Math.min(...xVals);
        const maxX = Math.max(...xVals);
        const minY = Math.min(...yVals);
        const maxY = Math.max(...yVals);
        const minZ = Math.min(...zVals);
        const maxZ = Math.max(...zVals);

        const scaleX = v => pad.left + ((v - minX) / (maxX - minX || 1)) * plotW;
        const scaleY = v => (height - pad.bottom) - ((v - minY) / (maxY - minY || 1)) * plotH;

        const minR = 4;
        const maxR = 26;
        const scaleR = v => {
          const norm = Math.max(0, (v - minZ) / (maxZ - minZ || 1));
          const factor = radiusMode === 'sqrt' ? Math.sqrt(norm) : norm;
          return minR + factor * (maxR - minR);
        };

        // Statistical Calculations
        let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0, sumYY = 0;
        const n = data.length;
        for (const d of data) {
          sumX += d.x;
          sumY += d.y;
          sumXY += d.x * d.y;
          sumXX += d.x * d.x;
          sumYY += d.y * d.y;
        }
        const meanX = sumX / n;
        const meanY = sumY / n;
        const denomSlope = n * sumXX - sumX * sumX;
        let slope = 0, intercept = 0, corr = 0, r2 = 0;

        if (denomSlope !== 0) {
          slope = (n * sumXY - sumX * sumY) / denomSlope;
          intercept = (sumY - slope * sumX) / n;
        }

        const denomCorr = Math.sqrt((n * sumXX - sumX * sumX) * (n * sumYY - sumY * sumY));
        if (denomCorr !== 0) {
          corr = (n * sumXY - sumX * sumY) / denomCorr;
          r2 = corr * corr;
        }

        if (statPoints) statPoints.textContent = String(n);
        if (statCorr) statCorr.textContent = (corr >= 0 ? '+' : '') + corr.toFixed(2);
        if (statR2) statR2.textContent = r2.toFixed(2);
        if (statSlope) statSlope.textContent = slope.toFixed(2);
        if (statMeans) statMeans.textContent = `${meanX.toFixed(1)} / ${meanY.toFixed(1)}`;

        // Build SVG Elements
        liveSvg.innerHTML = '';

        // Background
        const bg = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        bg.setAttribute("width", "760");
        bg.setAttribute("height", "480");
        bg.setAttribute("fill", "#0D0D0D");
        bg.setAttribute("rx", "6");
        liveSvg.appendChild(bg);

        // Gridlines
        const gridG = document.createElementNS("http://www.w3.org/2000/svg", "g");
        gridG.setAttribute("stroke", "#1F1F1F");
        gridG.setAttribute("stroke-width", "1");

        for (let i = 0; i <= 5; i++) {
          const gx = pad.left + (plotW / 5) * i;
          const gy = pad.top + (plotH / 5) * i;

          // Vertical grid
          const vl = document.createElementNS("http://www.w3.org/2000/svg", "line");
          vl.setAttribute("x1", gx.toFixed(1));
          vl.setAttribute("y1", pad.top);
          vl.setAttribute("x2", gx.toFixed(1));
          vl.setAttribute("y2", height - pad.bottom);
          gridG.appendChild(vl);

          // Horizontal grid
          const hl = document.createElementNS("http://www.w3.org/2000/svg", "line");
          hl.setAttribute("x1", pad.left);
          hl.setAttribute("y1", gy.toFixed(1));
          hl.setAttribute("x2", width - pad.right);
          hl.setAttribute("y2", gy.toFixed(1));
          gridG.appendChild(hl);
        }
        liveSvg.appendChild(gridG);

        // Quadrant Crosshairs
        if (quadMode === 'mean') {
          const qg = document.createElementNS("http://www.w3.org/2000/svg", "g");
          qg.setAttribute("stroke", "#334155");
          qg.setAttribute("stroke-width", "1.5");
          qg.setAttribute("stroke-dasharray", "4 4");

          const qx = scaleX(meanX);
          const qy = scaleY(meanY);

          const qLineX = document.createElementNS("http://www.w3.org/2000/svg", "line");
          qLineX.setAttribute("x1", qx.toFixed(1));
          qLineX.setAttribute("y1", pad.top);
          qLineX.setAttribute("x2", qx.toFixed(1));
          qLineX.setAttribute("y2", height - pad.bottom);
          qg.appendChild(qLineX);

          const qLineY = document.createElementNS("http://www.w3.org/2000/svg", "line");
          qLineY.setAttribute("x1", pad.left);
          qLineY.setAttribute("y1", qy.toFixed(1));
          qLineY.setAttribute("x2", width - pad.right);
          qLineY.setAttribute("y2", qy.toFixed(1));
          qg.appendChild(qLineY);
          liveSvg.appendChild(qg);
        }

        // OLS Trendline
        if (showTrend && denomSlope !== 0) {
          const tLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
          tLine.setAttribute("x1", scaleX(minX).toFixed(1));
          tLine.setAttribute("y1", scaleY(slope * minX + intercept).toFixed(1));
          tLine.setAttribute("x2", scaleX(maxX).toFixed(1));
          tLine.setAttribute("y2", scaleY(slope * maxX + intercept).toFixed(1));
          tLine.setAttribute("stroke", "#C1DD2D");
          tLine.setAttribute("stroke-width", "2.5");
          tLine.setAttribute("stroke-dasharray", "6 4");
          liveSvg.appendChild(tLine);
        }

        // Axes borders
        const axisLines = document.createElementNS("http://www.w3.org/2000/svg", "g");
        axisLines.setAttribute("stroke", "#3A3A3A");
        axisLines.setAttribute("stroke-width", "1.5");

        const xA = document.createElementNS("http://www.w3.org/2000/svg", "line");
        xA.setAttribute("x1", pad.left);
        xA.setAttribute("y1", height - pad.bottom);
        xA.setAttribute("x2", width - pad.right);
        xA.setAttribute("y2", height - pad.bottom);
        axisLines.appendChild(xA);

        const yA = document.createElementNS("http://www.w3.org/2000/svg", "line");
        yA.setAttribute("x1", pad.left);
        yA.setAttribute("y1", pad.top);
        yA.setAttribute("x2", pad.left);
        yA.setAttribute("y2", height - pad.bottom);
        axisLines.appendChild(yA);
        liveSvg.appendChild(axisLines);

        // Pre-sort bubbles by descending radius
        const sortedData = [...data].sort((a, b) => b.z - a.z);

        const ptsG = document.createElementNS("http://www.w3.org/2000/svg", "g");
        ptsG.setAttribute("class", "data-points");

        for (const pt of sortedData) {
          const cx = scaleX(pt.x);
          const cy = scaleY(pt.y);
          const r = scaleR(pt.z);

          const c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          c.setAttribute("cx", cx.toFixed(1));
          c.setAttribute("cy", cy.toFixed(1));
          c.setAttribute("r", r.toFixed(1));
          c.setAttribute("fill", pt.color);
          c.setAttribute("fill-opacity", String(opacity));
          c.setAttribute("stroke", "#FFFFFF");
          c.setAttribute("stroke-width", "1.25");
          c.setAttribute("class", "scatter-point");
          c.setAttribute("role", "graphics-symbol");
          c.setAttribute("tabindex", "0");
          c.setAttribute("aria-label", `${pt.id}: X=${pt.x}, Y=${pt.y}, Z=${pt.z}`);

          // Tooltip title
          const title = document.createElementNS("http://www.w3.org/2000/svg", "title");
          title.textContent = `${pt.id} | X: ${pt.x} | Y: ${pt.y} | Z: ${pt.z}`;
          c.appendChild(title);

          ptsG.appendChild(c);
        }
        liveSvg.appendChild(ptsG);

        // Axis Labels
        const lblG = document.createElementNS("http://www.w3.org/2000/svg", "g");
        lblG.setAttribute("fill", "#888888");
        lblG.setAttribute("font-family", "Inter, sans-serif");
        lblG.setAttribute("font-size", "11");

        // X Axis Title
        const xTitle = document.createElementNS("http://www.w3.org/2000/svg", "text");
        xTitle.setAttribute("x", String(pad.left + plotW / 2));
        xTitle.setAttribute("y", String(height - 15));
        xTitle.setAttribute("text-anchor", "middle");
        xTitle.setAttribute("font-weight", "600");
        xTitle.textContent = preset === 'saas' ? "Customer Acquisition Cost (CAC) [USD]" : preset === 'server' ? "Network Latency [ms]" : "Stellar Surface Temperature [K]";
        lblG.appendChild(xTitle);

        // Y Axis Title
        const yTitle = document.createElementNS("http://www.w3.org/2000/svg", "text");
        yTitle.setAttribute("x", String(-pad.top - plotH / 2));
        yTitle.setAttribute("y", "20");
        yTitle.setAttribute("transform", "rotate(-90)");
        yTitle.setAttribute("text-anchor", "middle");
        yTitle.setAttribute("font-weight", "600");
        yTitle.textContent = preset === 'saas' ? "Customer Lifetime Value (LTV) [USD]" : preset === 'server' ? "Throughput [req/sec]" : "Stellar Luminosity [L_sun]";
        lblG.appendChild(yTitle);

        liveSvg.appendChild(lblG);
      }

      // Event listeners
      if (presetSelect) presetSelect.addEventListener('change', updateStudio);
      if (pointsSlider) pointsSlider.addEventListener('input', updateStudio);
      if (radiusModeSelect) radiusModeSelect.addEventListener('change', updateStudio);
      if (opacitySlider) opacitySlider.addEventListener('input', updateStudio);
      if (trendlineToggle) trendlineToggle.addEventListener('change', updateStudio);
      if (quadrantToggle) quadrantToggle.addEventListener('change', updateStudio);

      // Clipboard export with execCommand fallback
      function fallbackCopy(text) {
        const textArea = document.createElement("textarea");
        textArea.value = text;
        textArea.style.top = "0";
        textArea.style.left = "0";
        textArea.style.position = "fixed";
        textArea.style.opacity = "0";
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        try {
          document.execCommand('copy');
        } catch (err) {
          console.error('Fallback execCommand failed:', err);
        }
        document.body.removeChild(textArea);
      }

      if (copyBtn) {
        copyBtn.addEventListener('click', () => {
          if (!liveSvg) return;
          const svgContent = liveSvg.outerHTML;
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(svgContent).then(() => {
              const origText = copyBtn.innerHTML;
              copyBtn.innerHTML = '<span>Copied to Clipboard!</span>';
              setTimeout(() => { copyBtn.innerHTML = origText; }, 2000);
            }).catch(() => {
              fallbackCopy(svgContent);
              const origText = copyBtn.innerHTML;
              copyBtn.innerHTML = '<span>Copied to Clipboard!</span>';
              setTimeout(() => { copyBtn.innerHTML = origText; }, 2000);
            });
          } else {
            fallbackCopy(svgContent);
            const origText = copyBtn.innerHTML;
            copyBtn.innerHTML = '<span>Copied to Clipboard!</span>';
            setTimeout(() => { copyBtn.innerHTML = origText; }, 2000);
          }
        });
      }

      updateStudio();
    })();
  </script>
</body>
</html>
'''

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Article 1 generated successfully at: {target_file}")
