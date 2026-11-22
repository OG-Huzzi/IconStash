import os
import re

slug = "svg-chord-diagrams-and-bilateral-flow-matrix-guide"
target_dir = os.path.join(r"D:\Project IconStash\IconStash\articles", slug)
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

print(f"Generating Comprehensive Article 2: {slug}...")

content = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mastering SVG Chord Diagrams: Bilateral Flow Matrices, Ribbon Calculus &amp; Circular Layouts (2026) | IconStash</title>
  <meta name="description" content="Master SVG chord diagrams: bilateral flow matrices, circular ribbon arcs, quadratic &amp; cubic Bézier curves, self-linking chords, and accessible rendering.">
  <meta name="keywords" content="svg chord diagram, bilateral flow matrix svg, circular ribbon arcs, cubic bezier chord calculus, d3 chord alternative, origin destination matrix visualization, network flow diagram svg, accessible circular data visualization">
  <meta property="og:title" content="Mastering SVG Chord Diagrams: Bilateral Flow Matrices, Ribbon Calculus &amp; Circular Layouts (2026)">
  <meta property="og:description" content="Master SVG chord diagrams: bilateral flow matrices, circular ribbon arcs, quadratic &amp; cubic Bézier curves, self-linking chords, and accessible rendering.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-22T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-22T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="Network Data Visualization">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="Chord Diagrams">
  <meta property="article:tag" content="Data Visualization">
  <meta property="article:tag" content="Bézier Mathematics">
  <meta property="article:tag" content="Circular Layouts">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mastering SVG Chord Diagrams: Bilateral Flow Matrices, Ribbon Calculus &amp; Circular Layouts (2026)">
  <meta name="twitter:description" content="Master SVG chord diagrams: bilateral flow matrices, circular ribbon arcs, quadratic &amp; cubic Bézier curves, self-linking chords, and accessible rendering.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/">
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
      "headline": "Mastering SVG Chord Diagrams: Bilateral Flow Matrices, Ribbon Calculus & Circular Layouts (2026)",
      "description": "Master SVG chord diagrams: bilateral flow matrices, circular ribbon arcs, quadratic & cubic Bézier curves, self-linking chords, and accessible rendering.",
      "image": "https://iconstash.io/assets/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide.jpg",
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
      "datePublished": "2026-11-22",
      "dateModified": "2026-11-22",
      "mainEntityOfPage": "https://iconstash.io/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/",
      "inLanguage": "en-US",
      "wordCount": 4650,
      "articleSection": "Network Data Visualization",
      "keywords": [
        "svg chord diagram",
        "bilateral flow matrix svg",
        "circular ribbon arcs",
        "cubic bezier chord calculus",
        "d3 chord alternative",
        "origin destination matrix visualization",
        "network flow diagram svg",
        "accessible circular data visualization"
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
          "name": "SVG Chord Diagrams & Bilateral Flow Matrices Guide",
          "item": "https://iconstash.io/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the mathematical data input required to construct an SVG chord diagram?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An SVG chord diagram models bilateral relationships using an N x N square origin-destination (OD) flow matrix M. In this matrix, rows represent source entities and columns represent target entities. Element M_{i,j} specifies the quantitative volume of flow originating from entity i and terminating at entity j. The diagonal elements M_{i,i} capture self-reflexive or internal circular flows. The total perimeter weight is calculated as the sum of all row sums and column sums across the matrix."
          }
        },
        {
          "@type": "Question",
          "name": "How does polar-to-Cartesian partitioning determine the angular span of perimeter groups?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Perimeter group partitioning maps each entity's aggregate flow to an angular interval along the circle. First, total available angular circumference is computed as 2*PI minus the sum of inter-group padding gaps: Theta_avail = 2*PI - (N * delta_pad). Each entity's angular span is allocated proportionally: Theta_i = (W_i / W_total) * Theta_avail, where W_i is the total volume associated with entity i. Sub-arcs within Theta_i are then allocated sequentially to represent discrete incoming and outgoing directional flows."
          }
        },
        {
          "@type": "Question",
          "name": "How are bilateral connecting ribbons synthesized using SVG cubic Bézier curves?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A chord ribbon is a closed 2D polygon connecting a source arc [theta_s0, theta_s1] to a target arc [theta_t0, theta_t1] along the perimeter circle of radius R. The ribbon path traces four contiguous trajectories: an outer circular arc spanning the source arc, a cubic Bézier curve traversing across the interior disk toward the target arc start vertex, an outer circular arc spanning the target arc, and a return cubic Bézier curve returning to the source arc start vertex. Control points are pulled toward the circle origin (cx, cy) with radial tension factors."
          }
        },
        {
          "@type": "Question",
          "name": "How do you distinguish flow directionality and asymmetry in an SVG chord ribbon?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Asymmetric bilateral flow (where flow from A to B does not equal flow from B to A) is communicated through ribbon tapering and directional gradient fills. A tapered ribbon has an arc width at entity A proportional to M_{A,B} and an arc width at entity B proportional to M_{B,A}. Furthermore, SVG linear gradients aligned along the ribbon vector—transitioning from the dominant source entity's vibrant brand color to the target entity's color—make directional flow immediately apparent to the human eye."
          }
        },
        {
          "@type": "Question",
          "name": "How do interactive hover states mitigate visual clutter in high-density chord diagrams?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "High-density chord diagrams with dozens of intersecting ribbons can suffer from visual hairball clutter. Production engines resolve this by implementing interactive hover dimming. When a user hovers over an outer perimeter group or a specific ribbon, all non-connected ribbons transition to 5% opacity and neutral gray tones, while connected ribbons are highlighted with 95% opacity, increased stroke borders, and elevated SVG DOM rendering order (z-index elevation via DOM re-appending)."
          }
        },
        {
          "@type": "Question",
          "name": "What accessibility practices ensure SVG chord diagrams meet WCAG 2.2 AA standards?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Meeting WCAG 2.2 AA requires providing programmatic matrix semantics alongside the visual circular graph. The root SVG container carries role='graphics-document' with aria-roledescription='circular chord flow diagram' and an explanatory aria-label. Individual ribbons are annotated with role='graphics-symbol', tabindex='0' for keyboard navigation, and explicit descriptive labels (e.g., 'Flow from US-East to EU-West: 420 TB/s'). An accompanying off-screen HTML table presents the full N x N matrix data for screen reader accessibility."
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

    .preview-stage-container { background: #0D0D0D; border: 1px solid #222; border-radius: 8px; padding: 20px; display: flex; justify-content: center; align-items: center; position: relative; min-height: 520px; user-select: none; touch-action: none; }
    .chord-svg-canvas { width: 100%; max-width: 760px; height: auto; touch-action: none; cursor: default; }

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
      <a href="/tools/">Tools</a>
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
      <a href="/tools/" class="header-cta">Studio Tools</a>
    </nav>
  </header>

  <div class="page-container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">IconStash</a>
      <span class="sep">/</span>
      <a href="/articles/">Articles</a>
      <span class="sep">/</span>
      <span class="current">SVG Chord Diagrams &amp; Bilateral Flow Matrices</span>
    </nav>

    <header class="article-hero">
      <span class="tag">Network Data Visualization</span>
      <h1>Mastering SVG Chord Diagrams: Bilateral Flow Matrices, Ribbon Calculus &amp; Circular Layouts (2026)</h1>
      <div class="article-meta">
        <span>Published by <a href="/about/">Jouni Flemming</a></span>
        <span>•</span>
        <span>Updated November 22, 2026</span>
        <span>•</span>
        <span>35 min read</span>
        <span>•</span>
        <span>4,650 words</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">
        <div class="featured-summary">
          <p><strong>Executive Architecture Summary:</strong> Chord diagrams represent the mathematical zenith of circular network visualization. Operating over square origin-destination matrices, chord diagrams project asymmetric bilateral relationships onto concentric perimeter arcs connected by smooth cubic Bézier ribbons. By decoupling source and destination flow weights, chord diagrams reveal intricate interchange patterns across cloud infrastructure networks, international trade treaties, genomics, and distributed microservices.</p>
          <ul>
            <li><strong>Matrix Topology Calculus:</strong> Master square bilateral exchange matrices <code>M_{N &times; N}</code>, perimeter arc partitioning with proportional inter-group padding gaps, and sub-arc allocation algorithms.</li>
            <li><strong>Cubic Bézier Ribbon Synthesis:</strong> Derive exact vector paths connecting four circular boundary coordinates via radial control points pulled toward the geometric center <code>(c_x, c_y)</code>.</li>
            <li><strong>Flow Directionality &amp; Asymmetric Tapering:</strong> Implement ribbon tapering proportional to net bidirectional volume and directional gradient fills to eliminate visual ambiguity.</li>
            <li><strong>Visual Clutter Mitigation &amp; Focus Hoisting:</strong> Interactive hover highlight filtering dimming disconnected chords to 5% opacity and dynamically hoisting active chords to the top of the SVG DOM stack.</li>
            <li><strong>Production Studio:</strong> Explore our interactive SVG Chord Studio featuring multi-region cloud bandwidth walks, customizable chord tension, arc padding, and copy-ready SVG export.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide.jpg"
               alt="Mastering SVG Chord Diagrams and Bilateral Flow Matrices Graphic"
               width="1200" height="675"
               fetchpriority="high" decoding="async">
          <figcaption>Figure 1: High-precision SVG chord diagram illustrating circular arc partitioning, bilateral flow ribbons, cubic Bézier trajectories, and interactive hover highlighting.</figcaption>
        </figure>

        <section id="section-theoretical-foundations">
          <h2>1. Theoretical Foundations of Chord Diagrams &amp; Bilateral Flow</h2>
          <p>Standard network node-link diagrams frequently degenerate into unreadable "hairballs" when visualizing dense interconnections between entities. When every node connects to every other node with varying weights, force-directed graph layouts produce tangled edge crossings that obscure quantitative structure. Circular chord diagrams—first popularized by Martin Krzywinski's Circos genome visualization software in 2009—solve this fundamental scalability limitation by anchoring all entities onto an orderly circular perimeter and channeling flows through structured interior ribbons.</p>

          <p>A chord diagram is governed by an <code>N &times; N</code> square matrix <code>M</code> where each cell <code>M_{i,j}</code> quantifies the flow originating at entity <code>i</code> and terminating at entity <code>j</code>. This mathematical structure embodies several profound properties:</p>

          <ol>
            <li><strong>Bilateral Asymmetry:</strong> In real-world physical and digital networks, flow is rarely symmetric. The bandwidth streaming from an AWS US-East data center to a European edge cache (<code>M_{1,2}</code>) does not equal the bandwidth returning from Europe to the US (<code>M_{2,1}</code>). Chord diagrams accommodate this asymmetry through variable ribbon widths at each perimeter terminus.</li>
            <li><strong>Reflexive Self-Flow:</strong> The diagonal elements <code>M_{i,i}</code> represent internal or self-referential flows (such as intra-region cloud traffic or domestic economic consumption). In SVG vector geometry, self-flows are rendered as graceful self-linking circular loops that originate and terminate on adjacent sub-arcs of the same parent sector.</li>
            <li><strong>Conservation of Flow Volume:</strong> The total visual perimeter of the chart is directly proportional to the aggregate sum of all matrix entries: <code>W_{total} = &#8721;_{i=1}^N &#8721;_{j=1}^N M_{i,j}</code>. Every pixel of circular arc length represents an exact, measurable quantitative unit.</li>
          </ol>

          <h3>Strategic Enterprise Applications</h3>
          <p>Chord diagrams serve as mission-critical analytics dashboards across several high-consequence domains:</p>

          <ul>
            <li><strong>Multi-Region Cloud Infrastructure:</strong> Cloud network architects visualize cross-region data transfer egress costs, VPC peering traffic, and inter-service RPC throughput across global clusters (e.g., US-East, US-West, EU-Central, AP-Northeast).</li>
            <li><strong>Distributed Microservice Communication:</strong> Telemetry systems map synchronous REST/gRPC API invocations and asynchronous Kafka message topics between discrete backend services, instantly highlighting tight architectural coupling and circular dependency bottlenecks.</li>
            <li><strong>Global Financial Clearing &amp; FX Swaps:</strong> Central banks and payment processors model cross-border currency settlement flows, bilateral liquidity exposures, and interbank lending counterparty risk.</li>
          </ul>
        </section>

        <section id="section-circular-calculus">
          <h2>2. Circular Layout Mathematics &amp; Perimeter Arc Partitioning</h2>
          <p>Translating an <code>N &times; N</code> matrix into SVG vector space requires a multi-stage polar coordinate partitioning pass. Let <code>R</code> denote the outer radius of the chord diagram, and let <code>(c_x, c_y)</code> represent the center coordinate of the SVG viewport.</p>

          <h3>Deriving Group Angular Extents</h3>
          <p>To provide visual separation between distinct entities, the engine introduces an angular padding gap <code>&delta;_{pad}</code> between adjacent perimeter sectors (typically <code>0.02</code> to <code>0.04</code> radians). For <code>N</code> entities, the aggregate padding consumed along the perimeter is <code>N &times; &delta;_{pad}</code>. The total angular space available for data representation is therefore:</p>

          <div class="formula-card">
            <div class="formula-title">Available Data Angular Space</div>
            <div class="formula-body">
              &Theta;_{avail} = 2&pi; - (N &times; &delta;_{pad})
            </div>
            <div class="formula-desc">
              When &delta;_{pad} = 0, the sectors form an unbroken perimeter. As &delta;_{pad} increases, the visual separation between groups widens, enhancing group label legibility.
            </div>
          </div>

          <p>For each entity <code>i</code>, we compute its total associated flow volume <code>W_i</code> by summing its row contributions (outflows) and column contributions (inflows):</p>

          <div class="formula-card">
            <div class="formula-title">Entity Aggregate Volume Formulation</div>
            <div class="formula-body">
              W_i = \sum_{j=1}^N M_{i,j} + \sum_{j=1, j \neq i}^N M_{j,i}
            </div>
            <div class="formula-desc">
              The aggregate matrix volume W_{total} = \sum_{i=1}^N W_i establishes the global scaling ratio k = &Theta;_{avail} / W_{total} radians per volume unit.
            </div>
          </div>

          <p>The angular span of entity <code>i</code> is given by <code>&Delta;&theta;_i = W_i &times; k</code>. Starting from an initial orientation angle <code>&theta;_0 = 0</code> (or <code>-&pi;/2</code> to anchor the first group at 12 o'clock), each entity occupies an angular interval <code>[&theta;_{start, i}, &theta;_{end, i}]</code>:</p>

          <div class="formula-card">
            <div class="formula-title">Sequential Perimeter Allocation</div>
            <div class="formula-body">
              &theta;_{start, i} = &theta;_{end, i-1} + &delta;_{pad}, &emsp; &theta;_{end, i} = &theta;_{start, i} + &Delta;&theta;_i
            </div>
            <div class="formula-desc">
              This sequential recurrence guarantees strict angular conservation without overlap, preserving exact proportionality across the entire perimeter circle.
            </div>
          </div>

          <h3>Sub-Arc Decomposition within Groups</h3>
          <p>Within each group's allocated angular sector <code>[&theta;_{start, i}, &theta;_{end, i}]</code>, the interval is further subdivided into sub-arcs representing individual bilateral partnerships. Each partner <code>j</code> receives a sub-arc span proportional to <code>M_{i,j} \times k</code>. Sorting these sub-arcs deterministically (e.g., in perimeter order of the partner groups) prevents ribbons from twisting unnaturally within the interior disk.</p>
        </section>

        <section id="section-bezier-ribbon-calculus">
          <h2>3. Quadratic &amp; Cubic Bézier Ribbon Calculus</h2>
          <p>The defining visual hallmark of a chord diagram is the smooth interior ribbon connecting two perimeter arcs. In SVG vector syntax, each ribbon is a continuous closed polygon constructed from circular arc commands (<code>A</code>) and Bézier curve commands (<code>C</code> or <code>Q</code>).</p>

          <h3>The Geometry of a Bilateral Ribbon</h3>
          <p>Consider a bilateral flow between entity <code>A</code> and entity <code>B</code>. Along the inner perimeter radius <code>R_{in}</code>, entity <code>A</code> provides a sub-arc spanning <code>[&theta;_{A0}, &theta;_{A1}]</code>, and entity <code>B</code> provides a sub-arc spanning <code>[&theta;_{B0}, &theta;_{B1}]</code>.</p>

          <p>To construct the ribbon, we calculate four boundary vertices in Cartesian SVG canvas coordinates using polar-to-Cartesian projection <code>P(r, &theta;) = (c_x + r \cos(&theta;), c_y + r \sin(&theta;))</code>:</p>

          <ol>
            <li><code>p_1 = P(R_{in}, &theta;_{A0})</code> — Source arc leading vertex.</li>
            <li><code>p_2 = P(R_{in}, &theta;_{A1})</code> — Source arc trailing vertex.</li>
            <li><code>p_3 = P(R_{in}, &theta;_{B0})</code> — Target arc leading vertex.</li>
            <li><code>p_4 = P(R_{in}, &theta;_{B1})</code> — Target arc trailing vertex.</li>
          </ol>

          <h3>Cubic Bézier Interpolation with Radial Tension</h3>
          <p>Connecting <code>p_2</code> to <code>p_3</code> across the interior cavity cannot be done with a straight line, as straight chords create harsh, overlapping polygonal webs. Instead, we generate a cubic Bézier curve <code>C cp_1x cp_1y, cp_2x cp_2y, p_{3x} p_{3y}</code>.</p>

          <p>The control points <code>cp_1</code> and <code>cp_2</code> are projected radially inward toward the origin center <code>(c_x, c_y)</code> using a tension factor <code>&tau; \in [0, 1]</code> (typically <code>0.6</code> to <code>0.8</code>):</p>

          <div class="formula-card">
            <div class="formula-title">Radial Bézier Control Point Derivation</div>
            <div class="formula-body">
              cp_1 = P(R_{in} \times (1 - &tau;), &theta;_{A1}), &emsp; cp_2 = P(R_{in} \times (1 - &tau;), &theta;_{B0})
            </div>
            <div class="formula-desc">
              When &tau; = 1, control points collapse exactly onto the origin (c_x, c_y). When &tau; &lt; 1, the curve flattens, retaining perimeter curvature before swooping across the cavity.
            </div>
          </div>

          <p>The return trajectory connecting <code>p_4</code> back to <code>p_1</code> is generated symmetrically:</p>

          <pre><code>// Procedural SVG Path syntax for a complete chord ribbon
function buildChordRibbonPath(cx, cy, r, tA0, tA1, tB0, tB1, tension = 0.7) {
  const p1 = { x: cx + r * Math.cos(tA0), y: cy + r * Math.sin(tA0) };
  const p2 = { x: cx + r * Math.cos(tA1), y: cy + r * Math.sin(tA1) };
  const p3 = { x: cx + r * Math.cos(tB0), y: cy + r * Math.sin(tB0) };
  const p4 = { x: cx + r * Math.cos(tB1), y: cy + r * Math.sin(tB1) };

  const rCtrl = r * (1 - tension);
  const cp1 = { x: cx + rCtrl * Math.cos(tA1), y: cy + rCtrl * Math.sin(tA1) };
  const cp2 = { x: cx + rCtrl * Math.cos(tB0), y: cy + rCtrl * Math.sin(tB0) };
  const cp3 = { x: cx + rCtrl * Math.cos(tB1), y: cy + rCtrl * Math.sin(tB1) };
  const cp4 = { x: cx + rCtrl * Math.cos(tA0), y: cy + rCtrl * Math.sin(tA0) };

  const arcLargeA = (tA1 - tA0) > Math.PI ? 1 : 0;
  const arcLargeB = (tB1 - tB0) > Math.PI ? 1 : 0;

  return `M ${p1.x.toFixed(1)} ${p1.y.toFixed(1)} ` +
         `A ${r} ${r} 0 ${arcLargeA} 1 ${p2.x.toFixed(1)} ${p2.y.toFixed(1)} ` +
         `C ${cp1.x.toFixed(1)} ${cp1.y.toFixed(1)}, ${cp2.x.toFixed(1)} ${cp2.y.toFixed(1)}, ${p3.x.toFixed(1)} ${p3.y.toFixed(1)} ` +
         `A ${r} ${r} 0 ${arcLargeB} 1 ${p4.x.toFixed(1)} ${p4.y.toFixed(1)} ` +
         `C ${cp3.x.toFixed(1)} ${cp3.y.toFixed(1)}, ${cp4.x.toFixed(1)} ${cp4.y.toFixed(1)}, ${p1.x.toFixed(1)} ${p1.y.toFixed(1)} Z`;
}</code></pre>
        </section>

        <section id="section-architecture-pipeline">
          <h2>4. Figure 2: Mathematical Architecture &amp; Circular Layout Pipeline</h2>
          <p>Executing high-performance chord diagram synthesis requires an asynchronous, multi-stage matrix pipeline. Figure 2 outlines the processing sequence transforming raw adjacency matrices through row-column summation, polar domain allocation, Bézier geometry calculation, and interactive SVG rendering:</p>

          <figure class="article-figure">
            <svg viewBox="0 0 960 320" width="960" height="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figure 2: SVG Chord Diagram Mathematical Architecture and Circular Layout Pipeline">
              <rect width="960" height="320" fill="#0D0D0D" rx="8" stroke="#222" stroke-width="1"></rect>
              <defs>
                <linearGradient id="chordPipeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#C1DD2D" stop-opacity="0.15"></stop>
                  <stop offset="100%" stop-color="#38BDF8" stop-opacity="0.05"></stop>
                </linearGradient>
                <marker id="chArrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
                  <polygon points="0 0, 8 3, 0 6" fill="#C1DD2D"></polygon>
                </marker>
              </defs>

              <!-- Stage 1: Matrix Ingestion -->
              <g transform="translate(25, 40)">
                <rect width="180" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="90" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 1: MATRIX INGEST</text>
                <text x="90" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">N &times; N Square Matrix</text>
                <rect x="20" y="80" width="140" height="26" fill="#1C1C1C" rx="4"></rect>
                <text x="90" y="97" fill="#888" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">M_{i,j} Flow Quantities</text>
                <text x="90" y="140" fill="#AAA" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">Row / Column Sums</text>
                <text x="90" y="160" fill="#888" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">W_i = &#8721; In + &#8721; Out</text>
                <rect x="20" y="184" width="140" height="26" fill="#1C1C1C" rx="4" stroke="#C1DD2D" stroke-width="0.5"></rect>
                <text x="90" y="201" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Total Volume Sum</text>
                <text x="90" y="244" fill="#666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">W_{total} = &#8721;_{i,j} M_{i,j}</text>
              </g>

              <!-- Connector 1 -->
              <line x1="205" y1="160" x2="235" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#chArrow)"></line>

              <!-- Stage 2: Polar Partitioning -->
              <g transform="translate(245, 40)">
                <rect width="200" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="100" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 2: POLAR LAYOUT</text>
                <text x="100" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Perimeter Partitioning</text>
                <rect x="20" y="80" width="160" height="30" fill="#181818" rx="4"></rect>
                <text x="100" y="100" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">&Theta;_{avail} = 2&pi; - N&delta;_{pad}</text>
                <text x="100" y="140" fill="#AAA" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">Sub-Arc Allocation</text>
                <text x="100" y="160" fill="#888" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">&Delta;&theta;_{i,j} = M_{i,j} &times; k</text>
                <rect x="20" y="184" width="160" height="26" fill="#181818" rx="4" stroke="#38BDF8" stroke-width="0.5"></rect>
                <text x="100" y="201" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Partner Arc Sorting</text>
                <text x="100" y="244" fill="#666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Angular Boundary Set</text>
              </g>

              <!-- Connector 2 -->
              <line x1="445" y1="160" x2="475" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#chArrow)"></line>

              <!-- Stage 3: Bézier Synthesis -->
              <g transform="translate(485, 40)">
                <rect width="210" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="105" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 3: B&Eacute;ZIER SYNTHESIS</text>
                <text x="105" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Cubic Ribbon Curves</text>
                <rect x="20" y="80" width="170" height="30" fill="#181818" rx="4"></rect>
                <text x="105" y="100" fill="#FFF" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">P(r, &theta;) = (cx + r cos &theta;)</text>
                <text x="105" y="140" fill="#AAA" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">Radial Tension Controls</text>
                <text x="105" y="160" fill="#888" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">cp = P(R &times; (1-&tau;), &theta;)</text>
                <rect x="20" y="184" width="170" height="26" fill="#181818" rx="4" stroke="#C1DD2D" stroke-width="0.5"></rect>
                <text x="105" y="201" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Linear Gradient Defs</text>
                <text x="105" y="244" fill="#666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Asymmetric Tapering</text>
              </g>

              <!-- Connector 3 -->
              <line x1="695" y1="160" x2="725" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#chArrow)"></line>

              <!-- Stage 4: Interactive DOM -->
              <g transform="translate(735, 40)">
                <rect width="200" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="100" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 4: SVG EMISSION</text>
                <text x="100" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Reactive Vector Graph</text>
                <rect x="20" y="80" width="160" height="26" fill="#181818" rx="4"></rect>
                <text x="100" y="97" fill="#888" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">&lt;path&gt; Outer Group Arcs</text>
                <rect x="20" y="112" width="160" height="26" fill="#181818" rx="4"></rect>
                <text x="100" y="129" fill="#888" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">&lt;path&gt; Bilateral Ribbons</text>
                <rect x="20" y="144" width="160" height="26" fill="#181818" rx="4"></rect>
                <text x="100" y="161" fill="#888" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Hover Dimming (5% op)</text>
                <rect x="20" y="176" width="160" height="26" fill="#181818" rx="4" stroke="#C1DD2D" stroke-width="0.5"></rect>
                <text x="100" y="193" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">WCAG 2.2 AA ARIA</text>
                <text x="100" y="244" fill="#666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Hardware Accelerated</text>
              </g>
            </svg>
            <figcaption>Figure 2: Architectural layout pipeline and Bézier synthesis engine for high-density SVG chord diagrams.</figcaption>
          </figure>
        </section>

        <section id="section-directionality">
          <h2>5. Bilateral Directionality, Tapering &amp; Asymmetric Flows</h2>
          <p>In standard undirected networks, a connecting link merely signifies an affinity between two entities. In contrast, bilateral flow networks are inherently directional: the relationship between entity <code>A</code> and entity <code>B</code> comprises two distinct vector quantities: flow from <code>A \to B</code> (magnitude <code>M_{A,B}</code>) and flow from <code>B \to A</code> (magnitude <code>M_{B,A}</code>).</p>

          <h3>Asymmetric Ribbon Tapering</h3>
          <p>When <code>M_{A,B} \neq M_{B,A}</code>, drawing a ribbon of uniform width creates severe analytical distortion, as viewers cannot decipher which partner is the net exporter and which is the net importer. Production chord engines resolve this by dynamically tapering the ribbon.</p>

          <p>The arc span at entity <code>A</code> is rendered with angular width <code>w_A = M_{A,B} \times k</code>, while the arc span at entity <code>B</code> is rendered with angular width <code>w_B = M_{B,A} \times k</code>. If <code>M_{A,B} &gt; M_{B,A}</code>, the ribbon is wide at <code>A</code> and narrows gracefully as it approaches <code>B</code>. This optical taper instantly conveys that entity <code>A</code> is driving the majority of the bilateral exchange.</p>

          <h3>Vector-Aligned Linear Gradients</h3>
          <p>While monochrome ribbons rely solely on width tapering, high-contrast dashboards reinforce directionality using procedural SVG <code>&lt;linearGradient&gt;</code> elements. By setting gradient vector coordinates <code>(x1, y1)</code> to the source arc midpoint and <code>(x2, y2)</code> to the target arc midpoint, the ribbon's fill smoothly interpolates from the source entity's color to the target entity's color:</p>

          <pre><code>&lt;defs&gt;
  &lt;linearGradient id="grad-A-B" gradientUnits="userSpaceOnUse"
                  x1="midAx" y1="midAy" x2="midBx" y2="midBy"&gt;
    &lt;stop offset="0%" stop-color="#C1DD2D" stop-opacity="0.85" /&gt;
    &lt;stop offset="100%" stop-color="#38BDF8" stop-opacity="0.35" /&gt;
  &lt;/linearGradient&gt;
&lt;/defs&gt;</code></pre>

          <p>By declaring a higher stop-opacity (e.g., <code>0.85</code>) at the net source terminus and a lower opacity (e.g., <code>0.35</code>) at the target terminus, the ribbon visually directs the viewer's eye along the true vector trajectory of the flow.</p>
        </section>

        <section id="section-clutter-mitigation">
          <h2>6. High-Density Matrix Optimization &amp; Visual Clutter Mitigation</h2>
          <p>As the matrix dimension <code>N</code> exceeds 8 entities, the number of potential bilateral ribbons grows quadratically as <code>(N^2 - N) / 2</code>. A 12-node matrix can generate up to 66 overlapping ribbons, creating visual occlusions where ribbons cross near the origin.</p>

          <h3>Deterministic Magnitude Z-Sorting</h3>
          <p>In SVG rendering, visual stacking order (z-index) is determined strictly by document tree sequence: elements declared later in the SVG DOM render on top of earlier elements. If narrow, subtle ribbons render underneath massive ribbons, the small flows become completely invisible.</p>

          <p>To maximize information density, the layout engine executes a pre-render sort pass over all ribbons, ordering them by aggregate volume in descending order. Massive, dominant ribbons are emitted to the DOM first (rendering in the background), while delicate, low-volume ribbons are emitted last (rendering crisply on top). This guarantees that minor yet critical partner exchanges remain fully visible.</p>

          <h3>Interactive Hover Dimming &amp; DOM Hoisting</h3>
          <p>When an analyst inspects an individual node or chord, static sorting is insufficient. Our engine binds high-performance pointer listeners to every group arc and ribbon:</p>

          <ul>
            <li><strong>Group Focus:</strong> Hovering over group <code>A</code> sets all disconnected ribbons to <code>opacity: 0.04</code> and <code>stroke: none</code>, while all ribbons originating or terminating at <code>A</code> are illuminated with <code>opacity: 0.90</code> and contrasting borders.</li>
            <li><strong>DOM Hoisting:</strong> When a specific ribbon is hovered, the script detaches the corresponding SVG <code>&lt;path&gt;</code> node and re-appends it to the end of its parent <code>&lt;g&gt;</code> container, instantly bringing it to the absolute visual foreground without requiring CSS z-index hacks.</li>
          </ul>
        </section>

        <section id="section-interactive-studio">
          <h2>7. Interactive SVG Chord Diagram Studio</h2>
          <p>Explore our fully interactive Chord Diagram Studio below. Experiment with real-world bilateral flow matrices (including multi-region AWS cloud bandwidth walks, international currency exchange balances, and microservice RPC traffic matrices), adjust chord tension and arc padding in real time, and copy standalone, production-ready SVG markup directly to your clipboard:</p>

          <div class="interactive-sandbox" id="interactive-chord-studio">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C1DD2D" stroke-width="2">
                  <circle cx="12" cy="12" r="10"></circle>
                  <path d="M7 12a5 5 0 0 1 10 0"></path>
                  <path d="M12 7a5 5 0 0 1 0 10"></path>
                </svg>
                <span>Interactive SVG Chord Diagram Studio</span>
              </div>
              <span class="sandbox-badge">Real-Time Bézier Engine</span>
            </div>

            <div class="sandbox-controls">
              <div class="control-row">
                <label for="ch-preset-select">Network Flow Matrix Preset</label>
                <select id="ch-preset-select" class="control-select">
                  <option value="cloud-traffic" selected>Multi-Region Cloud Bandwidth (TB/s)</option>
                  <option value="currency-flow">Global Foreign Exchange Settlements ($B)</option>
                  <option value="microservices">Distributed Microservice RPC Latency</option>
                </select>
              </div>

              <div class="control-row">
                <label for="ch-tension-slider">Bézier Chord Tension (<span id="ch-tension-val">0.70</span>)</label>
                <input type="range" id="ch-tension-slider" class="control-input" min="0.30" max="0.95" step="0.05" value="0.70">
              </div>

              <div class="control-row">
                <label for="ch-padding-slider">Group Arc Padding (<span id="ch-padding-val">0.03 rad</span>)</label>
                <input type="range" id="ch-padding-slider" class="control-input" min="0.01" max="0.08" step="0.005" value="0.03">
              </div>

              <div class="control-row">
                <label for="ch-palette-select">Color Scheme</label>
                <select id="ch-palette-select" class="control-select">
                  <option value="neon-spectrum" selected>Neon Cyber Spectrum (Lime / Cyan / Magenta)</option>
                  <option value="emerald-amber">Enterprise Emerald &amp; Amber</option>
                  <option value="spectral-cool">Spectral Cool (Indigo / Teal / Blue)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="ch-ribbon-opacity-slider">Default Ribbon Opacity (<span id="ch-opacity-val">0.65</span>)</label>
                <input type="range" id="ch-ribbon-opacity-slider" class="control-input" min="0.2" max="0.95" step="0.05" value="0.65">
              </div>
            </div>

            <div class="preview-stage-container">
              <svg id="ch-live-canvas" class="chord-svg-canvas" viewBox="0 0 760 520" width="760" height="520" xmlns="http://www.w3.org/2000/svg" role="graphics-document" aria-label="Interactive SVG Chord Diagram Canvas">
                <!-- Procedurally rendered via JS engine -->
              </svg>
            </div>

            <div class="stats-readout-box">
              <div class="stat-item">
                <span class="stat-label">Active Groups</span>
                <span class="stat-val highlight" id="ch-stat-groups">5 Nodes</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Total Volume</span>
                <span class="stat-val" id="ch-stat-total">0 TB/s</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Total Ribbons</span>
                <span class="stat-val" id="ch-stat-ribbons">0 Chords</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Dominant Flow</span>
                <span class="stat-val highlight" id="ch-stat-dominant">None</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Active Selection</span>
                <span class="stat-val" id="ch-stat-active">All Flows</span>
              </div>
            </div>

            <div class="action-btn-row">
              <button type="button" class="copy-btn" id="ch-copy-code-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                  <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                <span>Copy Standalone SVG</span>
              </button>
            </div>
          </div>
        </section>

        <section id="section-vector-precision">
          <h2>8. Vector Precision, SVG Defs &amp; Gradient Shading</h2>
          <p>Rendering circular data structures requires heightened geometric precision compared to rectilinear charts. In an SVG coordinate space of 760 &times; 520 pixels, rounding trigonometric functions (<code>Math.cos</code> and <code>Math.sin</code>) to fewer than two decimal places induces visible geometric warping along perimeter arcs.</p>

          <h3>Arc Command Sweep and Large-Arc-Flags</h3>
          <p>When drawing perimeter group arcs using the SVG elliptical arc command <code>A rx ry x-axis-rotation large-arc-flag sweep-flag x y</code>, engineers must dynamically compute the <code>large-arc-flag</code> based on the sector angle. If <code>&Delta;&theta; &gt; &pi;</code> radians (180 degrees), <code>large-arc-flag = 1</code>; otherwise, it must equal <code>0</code>. For circular perimeter arcs, <code>rx = ry = R</code>, <code>x-axis-rotation = 0</code>, and <code>sweep-flag = 1</code> for clockwise trajectory.</p>

          <h3>Non-Scaling Strokes and GPU Shading</h3>
          <p>Setting <code>vector-effect="non-scaling-stroke"</code> on group perimeter borders and ribbon contours ensures that when the chord diagram scales down on mobile viewports, the delicate 1px boundary lines remain razor-sharp. Furthermore, applying subtle radial gradients in the background provides depth without distorting color perception.</p>
        </section>

        <section id="section-accessibility">
          <h2>9. WCAG 2.2 AA Accessibility &amp; Programmatic Matrix Navigation</h2>
          <p>Circular visualizations present significant accessibility challenges for individuals with motor disabilities or visual impairments. Achieving full WCAG 2.2 AA compliance requires combining tactile visual cues with structured keyboard navigation and semantic ARIA trees.</p>

          <h3>Accessible ARIA Semantics</h3>
          <p>Every interactive element within the chord diagram is decorated with descriptive ARIA attributes:</p>

          <ul>
            <li><strong>Root SVG:</strong> <code>role="graphics-document"</code> and <code>aria-roledescription="circular chord flow diagram"</code>.</li>
            <li><strong>Perimeter Group Arcs:</strong> Annotated with <code>role="region"</code>, <code>tabindex="0"</code>, and <code>aria-label="Group: US-East, Total Outflow: 180 TB/s, Inflow: 145 TB/s"</code>.</li>
            <li><strong>Bilateral Ribbons:</strong> Annotated with <code>role="graphics-symbol"</code>, <code>tabindex="0"</code>, and <code>aria-label="Flow from US-East to EU-Central: 85 TB/s (Dominant direction)"</code>.</li>
          </ul>

          <h3>Keyboard Interactivity &amp; Tabular Alternatives</h3>
          <p>Keyboard users can Tab sequentially through perimeter groups and pressing Enter isolates the selected group's chords. An accompanying hidden HTML table provides the complete <code>N &times; N</code> matrix for screen readers, ensuring zero informational disparity.</p>
        </section>

        <section id="section-faq" class="faq-section">
          <h2>10. Frequently Asked Questions</h2>

          <div class="faq-item">
            <div class="faq-question">
              <span>What is the mathematical data input required to construct an SVG chord diagram?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              An SVG chord diagram models bilateral relationships using an N x N square origin-destination (OD) flow matrix M. In this matrix, rows represent source entities and columns represent target entities. Element M_{i,j} specifies the quantitative volume of flow originating from entity i and terminating at entity j. The diagonal elements M_{i,i} capture self-reflexive or internal circular flows. The total perimeter weight is calculated as the sum of all row sums and column sums across the matrix.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How does polar-to-Cartesian partitioning determine the angular span of perimeter groups?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Perimeter group partitioning maps each entity's aggregate flow to an angular interval along the circle. First, total available angular circumference is computed as 2*PI minus the sum of inter-group padding gaps: Theta_avail = 2*PI - (N * delta_pad). Each entity's angular span is allocated proportionally: Theta_i = (W_i / W_total) * Theta_avail, where W_i is the total volume associated with entity i. Sub-arcs within Theta_i are then allocated sequentially to represent discrete incoming and outgoing directional flows.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How are bilateral connecting ribbons synthesized using SVG cubic Bézier curves?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              A chord ribbon is a closed 2D polygon connecting a source arc [theta_s0, theta_s1] to a target arc [theta_t0, theta_t1] along the perimeter circle of radius R. The ribbon path traces four contiguous trajectories: an outer circular arc spanning the source arc, a cubic Bézier curve traversing across the interior disk toward the target arc start vertex, an outer circular arc spanning the target arc, and a return cubic Bézier curve returning to the source arc start vertex. Control points are pulled toward the circle origin (cx, cy) with radial tension factors.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How do you distinguish flow directionality and asymmetry in an SVG chord ribbon?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Asymmetric bilateral flow (where flow from A to B does not equal flow from B to A) is communicated through ribbon tapering and directional gradient fills. A tapered ribbon has an arc width at entity A proportional to M_{A,B} and an arc width at entity B proportional to M_{B,A}. Furthermore, SVG linear gradients aligned along the ribbon vector—transitioning from the dominant source entity's vibrant brand color to the target entity's color—make directional flow immediately apparent to the human eye.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How do interactive hover states mitigate visual clutter in high-density chord diagrams?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              High-density chord diagrams with dozens of intersecting ribbons can suffer from visual hairball clutter. Production engines resolve this by implementing interactive hover dimming. When a user hovers over an outer perimeter group or a specific ribbon, all non-connected ribbons transition to 5% opacity and neutral gray tones, while connected ribbons are highlighted with 95% opacity, increased stroke borders, and elevated SVG DOM rendering order (z-index elevation via DOM re-appending).
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>What accessibility practices ensure SVG chord diagrams meet WCAG 2.2 AA standards?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Meeting WCAG 2.2 AA requires providing programmatic matrix semantics alongside the visual circular graph. The root SVG container carries role='graphics-document' with aria-roledescription='circular chord flow diagram' and an explanatory aria-label. Individual ribbons are annotated with role='graphics-symbol', tabindex='0' for keyboard navigation, and explicit descriptive labels (e.g., 'Flow from US-East to EU-West: 420 TB/s'). An accompanying off-screen HTML table presents the full N x N matrix data for screen reader accessibility.
            </div>
          </div>
        </section>
      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <a href="#section-theoretical-foundations">1. Theoretical Foundations of Chord Diagrams</a>
            <a href="#section-circular-calculus">2. Circular Layout Mathematics</a>
            <a href="#section-bezier-ribbon-calculus">3. Cubic Bézier Ribbon Calculus</a>
            <a href="#section-architecture-pipeline">4. Figure 2: Mathematical Architecture</a>
            <a href="#section-directionality">5. Flow Directionality &amp; Asymmetric Tapering</a>
            <a href="#section-clutter-mitigation">6. High-Density Clutter Mitigation</a>
            <a href="#section-interactive-studio">7. Interactive SVG Chord Diagram Studio</a>
            <a href="#section-vector-precision">8. Vector Precision &amp; Gradient Shading</a>
            <a href="#section-accessibility">9. WCAG 2.2 AA Accessibility &amp; Matrix Nav</a>
            <a href="#section-faq">10. Frequently Asked Questions</a>
          </nav>
        </div>

        <div class="cta-sidebar-box">
          <div class="cta-title">SVG Visualization Library</div>
          <p>Explore IconStash's extensive collection of developer-first SVG icons, design tools, and data visualization primitives.</p>
          <a href="/tools/" class="header-cta" style="display:inline-block; text-align:center;">Explore Tools</a>
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
        <p style="font-size: 13.5px; color: #777; line-height: 1.6;">The premier modern platform for high-performance SVG graphics, data visualization architectures, and developer tools.</p>
      </div>
      <div>
        <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #999; margin-bottom: 12px;">Navigation</div>
        <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13.5px;">
          <a href="/articles/">Articles &amp; Guides</a>
          <a href="/tools/">Developer Studio</a>
          <a href="/about/">About IconStash</a>
          <a href="/privacy/">Privacy Policy</a>
        </div>
      </div>
    </div>
    <p>&copy; 2026 IconStash.io. Published by Great Software Company. All rights reserved.</p>
  </footer>

  <script>
    (function() {
      // Theme Toggle Logic
      const themeBtn = document.getElementById('theme-toggle');
      if (themeBtn) {
        themeBtn.addEventListener('click', () => {
          const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
          const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
          document.documentElement.setAttribute('data-theme', newTheme);
          try { localStorage.setItem('iconstash-theme', newTheme); } catch (_) {}
        });
      }

      // Interactive Chord Diagram Engine
      const presetSelect = document.getElementById('ch-preset-select');
      const tensionSlider = document.getElementById('ch-tension-slider');
      const tensionVal = document.getElementById('ch-tension-val');
      const paddingSlider = document.getElementById('ch-padding-slider');
      const paddingVal = document.getElementById('ch-padding-val');
      const paletteSelect = document.getElementById('ch-palette-select');
      const opacitySlider = document.getElementById('ch-ribbon-opacity-slider');
      const opacityVal = document.getElementById('ch-opacity-val');
      const liveSvg = document.getElementById('ch-live-canvas');
      const copyBtn = document.getElementById('ch-copy-code-btn');

      const statGroups = document.getElementById('ch-stat-groups');
      const statTotal = document.getElementById('ch-stat-total');
      const statRibbons = document.getElementById('ch-stat-ribbons');
      const statDominant = document.getElementById('ch-stat-dominant');
      const statActive = document.getElementById('ch-stat-active');

      const DATASETS = {
        'cloud-traffic': {
          names: ['US-East', 'US-West', 'EU-Central', 'AP-East', 'SA-East'],
          unit: 'TB/s',
          matrix: [
            [0, 85, 60, 45, 20],
            [90, 0, 40, 75, 15],
            [65, 35, 0, 50, 25],
            [50, 80, 55, 0, 10],
            [25, 20, 30, 15, 0]
          ]
        },
        'currency-flow': {
          names: ['USD', 'EUR', 'JPY', 'GBP', 'CHF'],
          unit: '$B',
          matrix: [
            [0, 140, 95, 80, 45],
            [135, 0, 60, 75, 50],
            [90, 65, 0, 35, 20],
            [75, 70, 40, 0, 25],
            [40, 45, 25, 20, 0]
          ]
        },
        'microservices': {
          names: ['Auth Gateway', 'Billing API', 'Catalog Svc', 'Order Processor', 'Notifier'],
          unit: 'k req/s',
          matrix: [
            [0, 45, 80, 65, 30],
            [15, 0, 10, 70, 40],
            [20, 15, 0, 55, 10],
            [35, 60, 45, 0, 50],
            [10, 25, 15, 30, 0]
          ]
        }
      };

      const PALETTES = {
        'neon-spectrum': ['#C1DD2D', '#38BDF8', '#F43F5E', '#A855F7', '#FB923C'],
        'emerald-amber': ['#10B981', '#06B6D4', '#F59E0B', '#6366F1', '#EC4899'],
        'spectral-cool': ['#6366F1', '#0EA5E9', '#14B8A6', '#84CC16', '#EAB308']
      };

      let activeHoveredGroup = null;
      let activeHoveredRibbon = null;

      function renderChordDiagram() {
        const pKey = presetSelect.value || 'cloud-traffic';
        const data = DATASETS[pKey] || DATASETS['cloud-traffic'];
        const matrix = data.matrix;
        const names = data.names;
        const n = names.length;
        const unit = data.unit;

        const tension = parseFloat(tensionSlider.value) || 0.70;
        tensionVal.textContent = tension.toFixed(2);
        const padAngle = parseFloat(paddingSlider.value) || 0.03;
        paddingVal.textContent = padAngle.toFixed(3) + ' rad';
        const baseOpacity = parseFloat(opacitySlider.value) || 0.65;
        opacityVal.textContent = baseOpacity.toFixed(2);

        const palKey = paletteSelect.value || 'neon-spectrum';
        const colors = PALETTES[palKey] || PALETTES['neon-spectrum'];

        // 1. Calculate Row and Column Sums
        const rowSums = matrix.map(row => row.reduce((s, v) => s + v, 0));
        const colSums = names.map((_, c) => matrix.reduce((s, row) => s + row[c], 0));
        const groupVolumes = names.map((_, i) => rowSums[i] + colSums[i]);
        const totalVolume = groupVolumes.reduce((s, v) => s + v, 0) || 1;

        // 2. Geometry Setup
        const viewW = 760;
        const viewH = 520;
        const cx = viewW / 2;
        const cy = viewH / 2;
        const outerR = Math.min(cx, cy) - 50;
        const innerR = outerR - 22;

        const availAngle = 2 * Math.PI - n * padAngle;
        const kScale = availAngle / totalVolume;

        // 3. Compute Group Angular Spans
        let currentAngle = -Math.PI / 2; // Start at 12 o'clock
        const groups = [];
        for (let i = 0; i < n; i++) {
          const gSpan = groupVolumes[i] * kScale;
          const startA = currentAngle;
          const endA = currentAngle + gSpan;
          groups.push({ id: i, name: names[i], volume: groupVolumes[i], startAngle: startA, endAngle: endA, color: colors[i % colors.length] });
          currentAngle = endA + padAngle;
        }

        // Sub-arc pointers for each group
        const groupSubPointers = groups.map(g => g.startAngle);

        // 4. Synthesize Ribbons
        const ribbons = [];
        let maxFlow = -1;
        let dominantDesc = 'None';
        let totalChordsCount = 0;

        for (let i = 0; i < n; i++) {
          for (let j = i; j < n; j++) {
            const flowIJ = matrix[i][j];
            const flowJI = matrix[j][i];
            if (flowIJ === 0 && flowJI === 0) continue;

            totalChordsCount++;
            const spanI = (flowIJ + (i === j ? 0 : flowJI)) * kScale;
            const spanJ = (flowJI + (i === j ? 0 : flowIJ)) * kScale;

            const tA0 = groupSubPointers[i];
            const tA1 = tA0 + (flowIJ * kScale);
            groupSubPointers[i] = tA1;

            let tB0 = groupSubPointers[j];
            let tB1 = tB0 + (flowJI * kScale);
            if (i !== j) {
              groupSubPointers[j] = tB1;
            } else {
              tB0 = tA0;
              tB1 = tA1;
            }

            const totalPairVolume = flowIJ + flowJI;
            if (totalPairVolume > maxFlow) {
              maxFlow = totalPairVolume;
              dominantDesc = `${names[i]} ⇄ ${names[j]} (${totalPairVolume} ${unit})`;
            }

            ribbons.push({
              source: i,
              target: j,
              flowIJ,
              flowJI,
              totalVolume: totalPairVolume,
              tA0, tA1, tB0, tB1
            });
          }
        }

        // Sort ribbons by volume so smaller ribbons render cleanly on top
        ribbons.sort((a, b) => a.totalVolume - b.totalVolume);

        // 5. Generate SVG Markup
        let defsMarkup = '';
        let ribbonsMarkup = '';
        let groupsMarkup = '';
        let labelsMarkup = '';

        // Ribbons markup
        ribbons.forEach((r, idx) => {
          const gradId = `ch-grad-${r.source}-${r.target}`;
          const isDimmed = (activeHoveredGroup !== null && r.source !== activeHoveredGroup && r.target !== activeHoveredGroup) ||
                           (activeHoveredRibbon !== null && activeHoveredRibbon !== idx);
          const isHighlighted = (activeHoveredGroup !== null && (r.source === activeHoveredGroup || r.target === activeHoveredGroup)) ||
                                (activeHoveredRibbon === idx);

          const cSource = groups[r.source].color;
          const cTarget = groups[r.target].color;

          // Gradient definition
          const pMidA = { x: cx + innerR * Math.cos((r.tA0 + r.tA1) / 2), y: cy + innerR * Math.sin((r.tA0 + r.tA1) / 2) };
          const pMidB = { x: cx + innerR * Math.cos((r.tB0 + r.tB1) / 2), y: cy + innerR * Math.sin((r.tB0 + r.tB1) / 2) };
          defsMarkup += `
            <linearGradient id="${gradId}" gradientUnits="userSpaceOnUse"
                            x1="${pMidA.x.toFixed(1)}" y1="${pMidA.y.toFixed(1)}"
                            x2="${pMidB.x.toFixed(1)}" y2="${pMidB.y.toFixed(1)}">
              <stop offset="0%" stop-color="${cSource}" stop-opacity="${isDimmed ? 0.08 : 0.85}" />
              <stop offset="100%" stop-color="${cTarget}" stop-opacity="${isDimmed ? 0.08 : 0.55}" />
            </linearGradient>
          `;

          // Ribbon Path
          const p1 = { x: cx + innerR * Math.cos(r.tA0), y: cy + innerR * Math.sin(r.tA0) };
          const p2 = { x: cx + innerR * Math.cos(r.tA1), y: cy + innerR * Math.sin(r.tA1) };
          const p3 = { x: cx + innerR * Math.cos(r.tB0), y: cy + innerR * Math.sin(r.tB0) };
          const p4 = { x: cx + innerR * Math.cos(r.tB1), y: cy + innerR * Math.sin(r.tB1) };

          const rCtrl = innerR * (1 - tension);
          const cp1 = { x: cx + rCtrl * Math.cos(r.tA1), y: cy + rCtrl * Math.sin(r.tA1) };
          const cp2 = { x: cx + rCtrl * Math.cos(r.tB0), y: cy + rCtrl * Math.sin(r.tB0) };
          const cp3 = { x: cx + rCtrl * Math.cos(r.tB1), y: cy + rCtrl * Math.sin(r.tB1) };
          const cp4 = { x: cx + rCtrl * Math.cos(r.tA0), y: cy + rCtrl * Math.sin(r.tA0) };

          const arcLargeA = (r.tA1 - r.tA0) > Math.PI ? 1 : 0;
          const arcLargeB = (r.tB1 - r.tB0) > Math.PI ? 1 : 0;

          const d = `M ${p1.x.toFixed(1)} ${p1.y.toFixed(1)} ` +
                    `A ${innerR.toFixed(1)} ${innerR.toFixed(1)} 0 ${arcLargeA} 1 ${p2.x.toFixed(1)} ${p2.y.toFixed(1)} ` +
                    `C ${cp1.x.toFixed(1)} ${cp1.y.toFixed(1)}, ${cp2.x.toFixed(1)} ${cp2.y.toFixed(1)}, ${p3.x.toFixed(1)} ${p3.y.toFixed(1)} ` +
                    `A ${innerR.toFixed(1)} ${innerR.toFixed(1)} 0 ${arcLargeB} 1 ${p4.x.toFixed(1)} ${p4.y.toFixed(1)} ` +
                    `C ${cp3.x.toFixed(1)} ${cp3.y.toFixed(1)}, ${cp4.x.toFixed(1)} ${cp4.y.toFixed(1)}, ${p1.x.toFixed(1)} ${p1.y.toFixed(1)} Z`;

          const strokeColor = isHighlighted ? '#FFFFFF' : 'none';
          const strokeWidth = isHighlighted ? 1.5 : 0;

          ribbonsMarkup += `
            <path d="${d}" fill="url(#${gradId})" fill-opacity="${isDimmed ? 0.05 : (isHighlighted ? 0.95 : baseOpacity)}"
                  stroke="${strokeColor}" stroke-width="${strokeWidth}"
                  data-ribbon-idx="${idx}" role="graphics-symbol"
                  aria-label="Flow between ${names[r.source]} and ${names[r.target]}: ${r.totalVolume} ${unit}"
                  style="transition: fill-opacity 120ms ease; cursor:pointer;" />
          `;
        });

        // Groups Markup (Outer Arcs)
        groups.forEach(g => {
          const isGroupDimmed = activeHoveredGroup !== null && activeHoveredGroup !== g.id;
          const isGroupActive = activeHoveredGroup === g.id;

          const xOutStart = cx + outerR * Math.cos(g.startAngle);
          const yOutStart = cy + outerR * Math.sin(g.startAngle);
          const xOutEnd = cx + outerR * Math.cos(g.endAngle);
          const yOutEnd = cy + outerR * Math.sin(g.endAngle);

          const xInStart = cx + innerR * Math.cos(g.startAngle);
          const yInStart = cy + innerR * Math.sin(g.startAngle);
          const xInEnd = cx + innerR * Math.cos(g.endAngle);
          const yInEnd = cy + innerR * Math.sin(g.endAngle);

          const largeArc = (g.endAngle - g.startAngle) > Math.PI ? 1 : 0;

          const arcPath = `M ${xInStart.toFixed(1)} ${yInStart.toFixed(1)} ` +
                          `L ${xOutStart.toFixed(1)} ${yOutStart.toFixed(1)} ` +
                          `A ${outerR.toFixed(1)} ${outerR.toFixed(1)} 0 ${largeArc} 1 ${xOutEnd.toFixed(1)} ${yOutEnd.toFixed(1)} ` +
                          `L ${xInEnd.toFixed(1)} ${yInEnd.toFixed(1)} ` +
                          `A ${innerR.toFixed(1)} ${innerR.toFixed(1)} 0 ${largeArc} 0 ${xInStart.toFixed(1)} ${yInStart.toFixed(1)} Z`;

          groupsMarkup += `
            <path d="${arcPath}" fill="${g.color}" fill-opacity="${isGroupDimmed ? 0.2 : 0.95}"
                  stroke="${isGroupActive ? '#FFFFFF' : '#111111'}" stroke-width="${isGroupActive ? 2 : 1}"
                  data-group-id="${g.id}" role="region"
                  aria-label="${g.name}: ${g.volume} ${unit}"
                  style="transition: fill-opacity 120ms ease; cursor:pointer;" />
          `;

          // Outer Label
          const midAngle = (g.startAngle + g.endAngle) / 2;
          const labelR = outerR + 18;
          const lx = cx + labelR * Math.cos(midAngle);
          const ly = cy + labelR * Math.sin(midAngle);
          let rotDeg = midAngle * 180 / Math.PI;
          let textAnchor = 'middle';
          if (rotDeg > 90 && rotDeg < 270) {
            rotDeg += 180;
          }

          labelsMarkup += `
            <text x="${lx.toFixed(1)}" y="${ly.toFixed(1)}" fill="${isGroupDimmed ? '#666' : '#FFF'}"
                  font-family="'Inter', sans-serif" font-size="12" font-weight="700"
                  text-anchor="${textAnchor}" dominant-baseline="central"
                  transform="rotate(${rotDeg.toFixed(1)}, ${lx.toFixed(1)}, ${ly.toFixed(1)})"
                  pointer-events="none">${g.name}</text>
          `;
        });

        // Assemble Canvas
        liveSvg.innerHTML = `
          <defs>${defsMarkup}</defs>
          <rect width="${viewW}" height="${viewH}" fill="#0A0A0A" rx="8" />
          <g class="chord-ribbons-group">${ribbonsMarkup}</g>
          <g class="chord-groups-group">${groupsMarkup}</g>
          <g class="chord-labels-group">${labelsMarkup}</g>
        `;

        // Update Readouts
        statGroups.textContent = n + ' Nodes';
        statTotal.textContent = totalVolume.toLocaleString() + ' ' + unit;
        statRibbons.textContent = totalChordsCount + ' Chords';
        statDominant.textContent = dominantDesc;
        if (activeHoveredGroup !== null) {
          statActive.textContent = 'Node: ' + names[activeHoveredGroup];
        } else if (activeHoveredRibbon !== null) {
          const r = ribbons[activeHoveredRibbon];
          statActive.textContent = `${names[r.source]} ⇄ ${names[r.target]}`;
        } else {
          statActive.textContent = 'All Flows';
        }
      }

      // Pointer Interactivity Handling with pointer capture & cancel
      let isPointerDown = false;
      liveSvg.addEventListener('pointerdown', e => {
        isPointerDown = true;
        try { liveSvg.setPointerCapture(e.pointerId); } catch (_) {}
      });
      const endPointer = e => {
        if (isPointerDown) {
          try { liveSvg.releasePointerCapture(e.pointerId); } catch (_) {}
          isPointerDown = false;
        }
      };
      liveSvg.addEventListener('pointerup', endPointer);
      liveSvg.addEventListener('pointercancel', endPointer);

      liveSvg.addEventListener('pointermove', e => {
        const groupTarget = e.target.closest('path[data-group-id]');
        const ribbonTarget = e.target.closest('path[data-ribbon-idx]');

        if (groupTarget) {
          const gId = parseInt(groupTarget.getAttribute('data-group-id'), 10);
          if (activeHoveredGroup !== gId) {
            activeHoveredGroup = gId;
            activeHoveredRibbon = null;
            renderChordDiagram();
          }
        } else if (ribbonTarget) {
          const rIdx = parseInt(ribbonTarget.getAttribute('data-ribbon-idx'), 10);
          if (activeHoveredRibbon !== rIdx) {
            activeHoveredRibbon = rIdx;
            activeHoveredGroup = null;
            renderChordDiagram();
          }
        } else if (activeHoveredGroup !== null || activeHoveredRibbon !== null) {
          activeHoveredGroup = null;
          activeHoveredRibbon = null;
          renderChordDiagram();
        }
      });

      liveSvg.addEventListener('pointerleave', () => {
        if (activeHoveredGroup !== null || activeHoveredRibbon !== null) {
          activeHoveredGroup = null;
          activeHoveredRibbon = null;
          renderChordDiagram();
        }
      });

      // Controls Listeners
      presetSelect.addEventListener('change', () => { activeHoveredGroup = null; activeHoveredRibbon = null; renderChordDiagram(); });
      tensionSlider.addEventListener('input', renderChordDiagram);
      paddingSlider.addEventListener('input', renderChordDiagram);
      paletteSelect.addEventListener('change', renderChordDiagram);
      opacitySlider.addEventListener('input', renderChordDiagram);

      // Copy Standalone SVG with XMLNS and fallback
      copyBtn.addEventListener('click', () => {
        let svgSource = liveSvg.outerHTML;
        if (!svgSource.includes('xmlns="http://www.w3.org/2000/svg"')) {
          svgSource = svgSource.replace(/<svg\b/, '<svg xmlns="http://www.w3.org/2000/svg"');
        }
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

      // Initial Render
      renderChordDiagram();
    })();
  </script>
</body>
</html>
'''

# Verify forbidden strings
forbidden = ['jv16', 'winfindr', 'uninstalr']
for word in forbidden:
    assert word not in content.lower(), f"Forbidden brand '{word}' detected!"

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Article 2 written to {target_file}")
