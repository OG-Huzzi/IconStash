import os
import re

slug = "svg-network-graphs-and-force-directed-node-link-visualization-guide"
target_dir = os.path.join(r"D:\Project IconStash\IconStash\articles", slug)
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

html_content = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mastering SVG Network Graphs &amp; Force-Directed Layouts: Physics Simulation, Node-Link Geometry &amp; Drag Guide (2026) | IconStash</title>
  <meta name="description" content="Build SVG network graphs & force layouts: Coulomb repulsion, Hooke springs, Barnes-Hut quadtrees, curved edges, and interactive node drag simulation.">
  <meta name="keywords" content="svg network graph, force directed graph svg, node link diagram svg, physics simulation svg, barnes hut svg, d3 force layout svg, interactive graph dragging javascript, topological cluster visualization">
  <meta property="og:title" content="Mastering SVG Network Graphs &amp; Force-Directed Layouts: Physics Simulation, Node-Link Geometry &amp; Drag Guide (2026)">
  <meta property="og:description" content="Build SVG network graphs & force layouts: Coulomb repulsion, Hooke springs, Barnes-Hut quadtrees, curved edges, and interactive node drag simulation.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-18T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-18T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="Vector Graphics &amp; Graph Topology">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="Network Graphs">
  <meta property="article:tag" content="Force-Directed Layouts">
  <meta property="article:tag" content="Data Visualization">
  <meta property="article:tag" content="Physics Simulation">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mastering SVG Network Graphs &amp; Force-Directed Layouts: Physics Simulation, Node-Link Geometry &amp; Drag Guide (2026)">
  <meta name="twitter:description" content="Build SVG network graphs & force layouts: Coulomb repulsion, Hooke springs, Barnes-Hut quadtrees, curved edges, and interactive node drag simulation.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide/">
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
      "headline": "Mastering SVG Network Graphs & Force-Directed Layouts: Physics Simulation, Node-Link Geometry & Drag Guide (2026)",
      "description": "Build SVG network graphs & force layouts: Coulomb repulsion, Hooke springs, Barnes-Hut quadtrees, curved edges, and interactive node drag simulation.",
      "image": "https://iconstash.io/assets/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide.jpg",
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
      "mainEntityOfPage": "https://iconstash.io/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide/",
      "inLanguage": "en-US",
      "wordCount": 4920,
      "articleSection": "Vector Graphics & Graph Topology",
      "keywords": [
        "svg network graph",
        "force directed graph svg",
        "node link diagram svg",
        "physics simulation svg",
        "barnes hut svg",
        "d3 force layout svg",
        "interactive graph dragging javascript",
        "topological cluster visualization"
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
          "name": "SVG Network Graphs & Force-Directed Layouts Guide",
          "item": "https://iconstash.io/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How does Coulomb electrostatic repulsion operate in a force-directed graph simulation?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In a force-directed simulation, every node is modeled as an electrically charged particle that exerts a repulsive force on every other node in the system according to Coulomb inverse-square law: F = k_charge / distance squared. As two nodes move closer together, the repulsive force increases asymptotically, preventing node overlap and spreading interconnected clusters across the available canvas. Because computing all pairwise forces across N nodes requires O(N squared) operations per animation frame, production engines employ the Barnes-Hut quadtree algorithm to approximate distant particle clusters as single center-of-mass monopoles, reducing simulation complexity to O(N log N)."
          }
        },
        {
          "@type": "Question",
          "name": "How is Hooke law applied to simulate elastic spring tension along graph edges?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Every topological link or edge connecting node u and node v is modeled as a linear physical spring with a resting equilibrium length L_0 and stiffness constant k_spring. According to Hooke law, the restorative force is directly proportional to the displacement from equilibrium: F_spring = k_spring * (currentDistance - L_0). If the nodes are pulled farther apart than L_0, the spring exerts an attractive force pulling them together; if compressed closer than L_0, the spring pushes them apart. This elastic tension pulls topologically connected communities into tight visual clusters while repulsion forces keep separate clusters spaced apart."
          }
        },
        {
          "@type": "Question",
          "name": "How do you render curved edges and bidirectional links in native SVG?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Straight SVG line elements fail when multiple parallel edges exist between the same pair of nodes or when bidirectional relationships must be displayed, as the lines render directly on top of each other. The standard architectural solution is computing quadratic Bézier curves using SVG path elements: M x1 y1 Q cx cy x2 y2. The control point (cx, cy) is positioned at the midpoint between the two nodes and offset perpendicular to the edge direction vector by a displacement proportional to link index and edge curvature settings. For directional graphs, marker-end attributes reference reusable arrowhead markers in the SVG defs container."
          }
        },
        {
          "@type": "Question",
          "name": "How does interactive node dragging work without disrupting simulation physics?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "When a user grabs a node with pointer events, the node is pinned by assigning fixed position coordinates (fx and fy) that override standard physics velocity integration during subsequent simulation ticks. The simulation temperature or alpha parameter is immediately reheated (e.g., alphaTarget = 0.3) so surrounding connected nodes organically react and reorganize around the dragged node. In SVG, mouse coordinates must be transformed through the SVG container inverse Screen-to-Canvas Current Transformation Matrix (CTM) to ensure sub-pixel dragging accuracy across responsive viewports and high-DPI zoom levels."
          }
        },
        {
          "@type": "Question",
          "name": "What is the practical scalability limit of rendering network graphs in native SVG versus Canvas or WebGL?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Native SVG graphs excel for small-to-medium network topologies containing up to 1,500 nodes and 3,000 edges, delivering infinite resolution scalability, rich CSS styling, DOM event listeners, and full accessibility trees. However, because each node, edge, and label represents a distinct DOM element, topologies exceeding 2,500 nodes experience significant memory consumption and frame rate drops during physics simulation. For massive graphs with tens of thousands of nodes, developers should employ a hybrid architecture: rendering background physics and edges onto HTML5 Canvas or WebGL shaders, while rendering selected nodes, hover rings, and tooltips in an SVG vector overlay."
          }
        },
        {
          "@type": "Question",
          "name": "How do you ensure force-directed SVG graphs comply with WCAG 2.2 AA accessibility mandates?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A compliant SVG network graph includes role='graphics-document' on the svg container, accompanied by aria-label and descriptive title and desc elements detailing total node count, edge density, and primary topological clusters. Every individual node carries role='graphics-symbol', keyboard focusability via tabindex='0', and detailed aria-label attributes listing node identity, degree centrality, and connected neighbor IDs. Keyboard navigation handlers allow users to press Tab or arrow keys to traverse from a focused node across its connected topological links, backed by high-contrast border strokes exceeding a 4.5:1 ratio against the dark or light canvas."
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

    .preview-stage-container { background: #0D0D0D; border: 1px solid #222; border-radius: 8px; padding: 20px; display: flex; justify-content: center; align-items: center; position: relative; min-height: 520px; user-select: none; }
    .network-svg-canvas { width: 100%; max-width: 820px; height: auto; cursor: grab; }
    .network-svg-canvas:active { cursor: grabbing; }
    .network-node { cursor: pointer; transition: stroke-width 150ms ease; }
    .network-node:hover { stroke-width: 3px !important; stroke: #C1DD2D !important; }
    .network-edge { stroke-linecap: round; transition: stroke-opacity 150ms ease; }

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
      <span class="current">SVG Network Graphs &amp; Force-Directed Layouts</span>
    </nav>

    <header class="article-hero">
      <span class="tag">Graph Topology &amp; Physics</span>
      <h1>Mastering SVG Network Graphs &amp; Force-Directed Layouts: Physics Simulation, Node-Link Geometry &amp; Drag Guide</h1>
      <div class="article-meta">
        <span>By <a href="/about/">Jouni Flemming</a></span>
        <span>•</span>
        <span>Published November 18, 2026</span>
        <span>•</span>
        <span>27 min read</span>
        <span>•</span>
        <span>Computational Geometry &amp; Physics Simulation</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">

        <div class="featured-summary">
          <p><strong>Executive Architectural Overview:</strong> Network graphs and force-directed node-link visualizations solve one of the most demanding challenges in vector computer science: revealing hidden relational structures, dependency clusters, and flow hierarchies without imposing artificial grid constraints. By translating abstract topological entities into physical mechanical systems governed by Coulomb electrostatic repulsion, Hooke spring elasticity, and Barnes-Hut spatial quadtrees, developers can render organic, self-organizing graph topologies directly inside Scalable Vector Graphics viewports.</p>
          <ul>
            <li><strong>Particle Physics Mechanics:</strong> Simulating n-body electrostatic repulsion, elastic Hooke springs, and Velocity Verlet viscous drag damping.</li>
            <li><strong>Barnes-Hut Optimization:</strong> Reducing pairwise repulsion complexity from quadratic O(N^2) to logarithmic O(N log N) via hierarchical 2D quadtrees.</li>
            <li><strong>Curved Edge Geometry:</strong> Rendering bidirectional relations and parallel multi-edges via parametric quadratic Bézier offsets and dynamic SVG marker arrowheads.</li>
            <li><strong>Kinematic Dragging &amp; Pinning:</strong> Transforming pointer coordinates through inverted SVG screen-to-canvas transformation matrices to pin active nodes without destabilizing physics equilibrium.</li>
            <li><strong>Zero-Dependency Interactive Studio:</strong> Complete real-time client-side force simulator with parametric controls, draggable nodes, cluster topologies, and standalone copy-ready SVG export.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide.jpg" alt="Futuristic dark mode developer interface showing complex SVG network graph and force-directed node-link diagram with interconnected glowing nodes, physics simulation vectors, neon lime and bright cyan glowing connections, topological clusters, modern software engineering UI" width="1200" height="675" fetchpriority="high" decoding="async">
          <figcaption>Figure 1: High-performance SVG force-directed network graph visualizing microservice dependency clusters, directional communication links, and real-time physical equilibrium dynamics.</figcaption>
        </figure>

        <section id="section-graph-foundations">
          <h2>1. Graph Theory Foundations: Adjacency Matrices, Edge Lists &amp; SVG Document Object Models</h2>
          <p>At its core, a network graph is an abstract mathematical structure G = (V, E) composed of a finite set of vertices (or nodes) V and an accompanying set of edges (or links) E connecting pairs of vertices. While relational databases and in-memory analytics engines typically store graph relationships as dense two-dimensional adjacency matrices or sparse adjacency lists, translating these abstract combinatorial relations into an interactive, visually coherent SVG rendering pipeline requires transforming discrete mathematical abstractions into continuous physical coordinates.</p>
          <p>An adjacency matrix models relationships through an N x N binary or weighted table, where cell A[i][j] denotes the connection strength between node i and node j. While adjacency matrices offer O(1) edge lookup time, they consume O(N^2) memory, which becomes prohibitive when managing sparse real-world networks such as cloud microservice architectures, social follower networks, or knowledge graphs where most nodes maintain connections to fewer than 1% of total peers. For visualization rendering engines, the normalized edge-list structure represents the industry standard. An edge-list represents the graph as an array of discrete link descriptors: <code>{ source: 'auth-service', target: 'database-cluster', weight: 4.5 }</code>.</p>
          <p>When projecting this edge list onto an SVG Document Object Model, structural hierarchy is paramount. The SVG document must organize its visual elements into distinct functional groups using <code>&lt;g&gt;</code> containers. By standard convention, edges are grouped within a lower <code>&lt;g class="graph-edges"&gt;</code> element, while nodes and their associated textual labels reside in an overlying <code>&lt;g class="graph-nodes"&gt;</code> element. Because SVG enforces a painter's algorithm rendering order where elements declared earlier in the markup are painted beneath subsequent elements, this grouping guarantees that connecting lines never bisect or obscure circular node symbols or metric labels.</p>
          <p>Furthermore, each node in the SVG DOM should declare standard ARIA accessibility attributes, transforming an otherwise opaque visual diagram into a fully inspectable structural hierarchy for assistive technology. Nodes declare <code>role="graphics-symbol"</code>, <code>tabindex="0"</code> for keyboard navigability, and descriptive <code>aria-label</code> properties detailing entity identity, degree centrality, and connected neighbor counts.</p>
        
          <p>Beyond elementary connectivity, network graphs encode sophisticated topological metrics that dictate visual hierarchy. Centrality algorithms identify critical architectural bottlenecks and high-leverage entities across a distributed system. Degree centrality simply tallies the total number of incident links connected to a given node, directly informing the node circle radius in the SVG DOM. Betweenness centrality evaluates how frequently a node falls along the shortest path between all other pairs of nodes, pinpointing pivotal gateway services or bridge routers whose failure would partition the network. When rendering in SVG, high-betweenness nodes command prominent accent colors and animated pulsing stroke halos.</p>
          <p>Furthermore, real-world networks naturally exhibit community structure, where subsets of nodes form densely interconnected topological clusters with comparatively sparse inter-cluster linkages. Graph partitioning algorithms, such as the Louvain heuristic or Newman-Girvan modularity optimization, assign discrete community identifiers to each vertex. In our SVG rendering architecture, community memberships translate into harmonious categorical color palettes, while convex hull bounding polygons or alpha-shape SVG contours can be rendered beneath node clusters to visually delineate microservice functional boundaries.</p>
          <p>Adjacency representations also influence DOM serialization efficiency. While storing graph data as raw JSON objects is convenient, passing millions of node coordinates during interactive animations creates severe garbage collection pressure. High-performance vector engines serialize graph snapshots into contiguous typed arrays, such as Float32Array coordinates and Int32Array topology indices. This memory layout allows the simulation engine to iterate through thousands of spatial coordinates with maximum CPU cache locality, eliminating pointer indirection delays before updating SVG DOM attributes.</p>
</section>

        <section id="section-physics-simulation">
          <h2>2. Force-Directed Physics: Coulomb Electrostatic Repulsion &amp; Hooke's Elastic Spring Laws</h2>
          <p>The foundational insight behind force-directed graph algorithms, first pioneered by Peter Eades in 1984 and later refined by Thomas Fruchterman and Edward Reingold in 1991, is treating the graph visualization not as a static geometric layout problem, but as a dynamic particle physics simulation. Nodes are modeled as electrically charged physical bodies with mass, while edges act as mechanical springs exerting restorative tension. The simulation is initialized by scattering nodes across the canvas with random or circular coordinates, and then letting physical forces iteratively push and pull the system toward a state of minimal potential energy.</p>
          <p>The physical simulation operates via three primary interacting forces:</p>

          <div class="formula-card">
            <div class="formula-title">Coulomb Electrostatic Repulsion (N-Body Anti-Clustering)</div>
            <div class="formula-body">F_repel(u, v) = (k_charge / ||p_u - p_v||^2) * ((p_u - p_v) / ||p_u - p_v||)</div>
            <div class="formula-desc">Every node u exerts an outward repulsive force on every other node v along the unit vector separating them. The force is inversely proportional to the square of Euclidean distance ||p_u - p_v||, preventing spatial collisions and expanding dense clusters across the viewport.</div>
          </div>

          <div class="formula-card">
            <div class="formula-title">Hooke's Elastic Spring Law (Topological Edge Attraction)</div>
            <div class="formula-body">F_spring(u, v) = k_spring * (||p_u - p_v|| - L_0) * ((p_v - p_u) / ||p_u - p_v||)</div>
            <div class="formula-desc">Where L_0 represents the natural resting equilibrium length of the link, and k_spring is the stiffness coefficient. Connected nodes pulled beyond L_0 experience an attractive inward force, drawing topologically related clusters into close visual proximity.</div>
          </div>

          <div class="formula-card">
            <div class="formula-title">Centering Gravity &amp; Viscous Damping (Velocity Verlet)</div>
            <div class="formula-body">v_i(t + dt) = (v_i(t) + (F_total / m_i) * dt) * gamma_friction</div>
            <div class="formula-body">p_i(t + dt) = p_i(t) + v_i(t + dt) * dt</div>
            <div class="formula-desc">Where gamma_friction is a velocity damping factor (typically 0.85 to 0.92) that bleeds kinetic energy out of the system over successive simulation ticks, preventing perpetual oscillation and ensuring smooth mathematical convergence to visual rest.</div>
          </div>

          <p>In addition to repulsion and spring attraction, an ambient centering gravity force is applied to all nodes: <code>F_gravity(i) = -k_gravity * (p_i - p_center)</code>. Without this weak inward pull toward the viewport center, disconnected components or leaf sub-graphs would drift infinitely outward toward the boundaries of the universe driven by unconstrained Coulomb repulsion.</p>
        
          <p>The numerical integration scheme employed to solve Newton second law of motion (F = m * a) determines the physical stability and visual realism of the graph layout. Elementary simulations often employ Forward Euler integration, which computes instantaneous velocity and advances position via simple linear increments: v(t + dt) = v(t) + a(t) * dt, and p(t + dt) = p(t) + v(t) * dt. While computationally lightweight, Forward Euler is not time-reversible and tends to accumulate numerical energy over time, causing tightly connected clusters to violently oscillate or explode when stiff spring constants are introduced.</p>
          <p>To eliminate artificial energy growth and ensure unconditionally stable simulation physics, high-grade vector engines implement Velocity Verlet integration. The Velocity Verlet algorithm updates positions and velocities in staggered half-steps, evaluating forces at intermediate spatial configurations. This symplectic integration property preserves phase-space volume, ensuring that kinetic energy naturally dampens according to the prescribed friction coefficient rather than accumulating numerical drift.</p>
          <p>Simultaneously, the simulation temperature schedule governs how rapidly the system transitions from wild exploratory motion to refined micro-adjustments. Known in statistical mechanics as simulated annealing, the temperature parameter alpha begins near unity (1.0) and decays exponentially on every animation tick according to alpha(t + 1) = alpha(t) * (1 - alphaDecay). High initial alpha values allow nodes to overcome local potential energy barriers, untangling crossed edges and sorting global topological clusters. As alpha cools below 0.05, physical movements become micro-damped, settling node clusters into pristine, human-readable equilibrium layouts without sudden tremors or twitching.</p>
</section>

        <section id="section-barnes-hut-optimization">
          <h2>3. Barnes-Hut Quadtree Optimization: Reducing O(N^2) Pairwise Repulsion to O(N log N)</h2>
          <p>The principal computational bottleneck in force-directed simulation is evaluating Coulomb repulsion. In a naive implementation, calculating the repulsive forces acting upon a graph with N nodes requires evaluating every possible unordered pair (u, v). The number of pairwise interactions equals N * (N - 1) / 2. For a small graph of 50 nodes, this requires 1,225 calculations per animation frame—easily handled by modern JavaScript runtimes at 60 FPS. However, for a network of 1,000 nodes, pairwise evaluation demands nearly 500,000 distance and vector calculations per frame, causing massive CPU stalls, garbage collection thrashing, and frozen browser tabs.</p>
          <p>In 1986, astrophysicists Josh Barnes and Piet Hut published an algorithmic breakthrough for simulating gravitational n-body star cluster dynamics. Their algorithm, now universally known as the <strong>Barnes-Hut Quadtree Algorithm</strong>, reduces pairwise computation from O(N^2) to O(N log N) by recursively grouping distant clusters of particles into single equivalent virtual bodies.</p>

          <p>The algorithm executes in two distinct phases on each simulation tick:</p>
          <ol>
            <li><strong>Quadtree Construction:</strong> A two-dimensional quadtree is constructed that encompasses all nodes within the current simulation bounds. The root represents the entire bounding box. Space is recursively partitioned into four quadrants until each leaf cell contains at most one node. Each internal quadtree node computes and stores the cumulative total mass M and center of mass C = sum(m_i * p_i) / M of all bodies residing within its subtree.</li>
            <li><strong>Force Approximation Traversal:</strong> When calculating the repulsive force acting on node u, the algorithm traverses the quadtree starting from the root. For any internal cell with spatial width s and distance d from node u, the algorithm computes the quotient theta = s / d. If theta is less than a predefined accuracy threshold (typically theta = 0.8 to 0.9), the entire sub-cluster is deemed sufficiently distant that its individual internal variations are negligible. The algorithm approximates the repulsion of the entire cluster as a single interaction with the cell's center of mass C, skipping recursive traversal of all child nodes!</li>
          </ol>

          <p>By pruning entire branches of the spatial tree, Barnes-Hut reduces the average number of force evaluations per node from N to approximately log(N). For a 2,000-node graph, this optimization prunes over 95% of mathematical operations, allowing complex topological graphs to simulate smoothly at high frame rates within client-side JavaScript.</p>
        
          <p>To analyze the mathematical rigor of Barnes-Hut spatial acceleration, consider the multi-pole expansion theorem from potential theory. When a cluster of particles is viewed from a significant distance, its gravitational or electrostatic potential can be expanded as a Taylor series centered at the cluster center of mass. The leading monopole term corresponds exactly to the total accumulated charge located at the barycenter: C = sum(m_i * p_i) / M. Quadrupole and higher-order moments account for internal asymmetries within the cluster, but their influence decays rapidly with the cube and fourth power of distance.</p>
          <p>In force-directed graph visualization, approximating distant clusters using the monopole center of mass introduces an almost imperceptible angular error (typically less than 2%) when the opening angle theta is set to 0.8. However, this microscopic geometric approximation yields staggering computational dividends. While an unoptimized O(N^2) simulation stalls completely on a 1,200-node microservice mesh, the Barnes-Hut algorithm evaluates force vectors across identical topology in less than 4 milliseconds per tick, leaving abundant frame budget for smooth browser composition and user interaction.</p>
          <p>Moreover, modern quadtree implementations implement dynamic tree pooling. Rather than allocating new Quadtree cell objects on every animation frame (which creates thousands of short-lived heap allocations and triggers the JavaScript V8 scavenger garbage collector), the engine maintains a static pre-allocated array of tree nodes. On each simulation step, the tree is reset by clearing pointer indices, achieving zero-allocation spatial partitioning that runs continuously without a single GC pause.</p>
</section>

        <section id="section-edge-geometry">
          <h2>4. Edge Geometry: Directed Arrowhead Markers, Self-Loops &amp; Quadratic Bézier Bundle Curves</h2>
          <p>While straight <code>&lt;line&gt;</code> elements suffice for simple undirected graphs, real-world engineering diagrams—such as microservice call graphs, dependency trees, and transactional state machines—demand sophisticated directional and relational edge geometry. Rendering straight lines between nodes with reciprocal relationships (where service A calls service B, and service B simultaneously calls service A) causes the two visual connections to overlap perfectly, rendering the bidirectional nature of the relationship completely invisible.</p>
          <p>To elegantly separate bidirectional edges and multi-link bundles, the SVG rendering pipeline computes quadratic Bézier curves using the <code>&lt;path d="M x1 y1 Q cx cy x2 y2"&gt;</code> command. The control point (cx, cy) is calculated by finding the Euclidean midpoint between source and target nodes and displacing it along the normal unit vector perpendicular to the line of sight:</p>

          <div class="formula-card">
            <div class="formula-title">Perpendicular Normal Offset for Quadratic Bézier Edges</div>
            <div class="formula-body">dx = x2 - x1, dy = y2 - y1, L = sqrt(dx^2 + dy^2)</div>
            <div class="formula-body">nx = -dy / L, ny = dx / L (Unit Normal Vector)</div>
            <div class="formula-body">cx = (x1 + x2) / 2 + nx * curvatureOffset</div>
            <div class="formula-body">cy = (y1 + y2) / 2 + ny * curvatureOffset</div>
            <div class="formula-desc">Where curvatureOffset is positive for forward directional edges, negative for reverse edges, and dynamically scaled based on the index of parallel links sharing the same endpoints.</div>
          </div>

          <p>For directional graphs, arrowheads communicate flow polarity. SVG provides native support for directional indicators via the <code>&lt;marker&gt;</code> element declared within the document's <code>&lt;defs&gt;</code> container. Setting <code>orient="auto"</code> or <code>orient="auto-start-reverse"</code> ensures that the marker automatically rotates to match the instantaneous tangent angle of the edge path at its terminal coordinate.</p>

          <div class="warning-box">
            <div class="warning-title">Critical Marker Geometry Pitfall: Node Center vs. Perimeter Clipping</div>
            <p>If an edge path terminates at the mathematical center (cx, cy) of a target node, an arrowhead marker attached to the path will render hidden beneath the opaque circular node fill! To ensure the arrowhead lands crisply on the outer boundary of the target node, the edge path must terminate at an offset coordinate: p_end = p_target - (p_target - p_source) * (radius_target / distance). The studio engine provided in this guide calculates this exact trigonometric intersection automatically.</p>
          </div>
        
          <p>Beyond simple point-to-point connections, production engineering architectures require dedicated edge-routing strategies for reflexive self-loops and multi-graph parallel links. A self-loop occurs when an entity maintains a relationship with itself, such as a recursive microservice retry loop or an autonomous database self-healing transaction. A standard line or quadratic curve whose start and end points coincide collapses into an invisible zero-length point.</p>
          <p>In SVG, self-loops are rendered using elliptical arc commands: <code>&lt;path d="M x y A rx ry 0 1 1 (x + delta) (y + delta) Z" /&gt;</code>. By orienting the arc apex away from the centroid of connected peer nodes, the self-loop forms a neat, tear-drop shaped circular antenna that curls outwards from the node perimeter without colliding with incoming external edges.</p>
          <p>Similarly, when multiple distinct relationships connect the same two entities (such as simultaneous HTTP REST and gRPC WebSocket channels between two services), our engine assigns unique ordinal indices to each edge. The normal offset distance used in quadratic Bézier control point calculation is modulated according to offset = (linkIndex - (totalParallelLinks - 1) / 2) * bundleSpacing. This creates an elegant, symmetrically spaced bundle of nested vector curves that clearly differentiates each individual communication conduit.</p>
</section>

        <section id="section-interactive-dragging">
          <h2>5. Node Anchoring, Pinning, and Kinematic Dragging via SVG Point Matrix Inversion</h2>
          <p>The crowning feature of an exploratory network graph is tactile physical interactivity. Users intuitively desire to grab a cluster hub, pull it away from a crowded center, and pin it to a clear region of the canvas to examine its local subnet topology. However, implementing interactive dragging within a force-directed simulation requires resolving two complex technical problems: coordinate space transformation and physics equilibrium perturbation.</p>

          <h3>Inverted SVG Matrix Coordinate Transformation</h3>
          <p>When a user triggers a <code>pointerdown</code> event on a DOM element, the event payload delivers screen-space coordinates: <code>clientX</code> and <code>clientY</code>. If the SVG element has been scaled by CSS flexbox, styled with responsive percentage widths, or magnified via CSS transforms, passing raw client coordinates directly to node position attributes produces severe cursor drift, where the node lags behind or shoots wildly ahead of the pointer.</p>
          <p>To eliminate coordinate drift, the mouse coordinates must be transformed through the SVG container's Screen-to-Canvas Current Transformation Matrix (CTM):</p>

          <pre><code>// Transforming screen client coordinates to SVG canvas viewBox space
function getSvgCoordinates(svgElement, clientX, clientY) {
  const pt = svgElement.createSVGPoint();
  pt.x = clientX;
  pt.y = clientY;
  const ctm = svgElement.getScreenCTM();
  if (!ctm) return { x: clientX, y: clientY };
  const transformed = pt.matrixTransform(ctm.inverse());
  return { x: transformed.x, y: transformed.y };
}</code></pre>

          <h3>Kinematic Pinning &amp; Alpha Reheating</h3>
          <p>In standard simulation physics, a node position is updated each frame by its calculated velocity vector. During dragging, the node must transition from a free particle into a kinematically pinned body. The engine assigns fixed coordinate properties: <code>node.fx = mouseX</code> and <code>node.fy = mouseY</code>. Within the Verlet integrator loop, if <code>fx</code> and <code>fy</code> exist, standard force acceleration is bypassed and the node is clamped directly to the pinned coordinates.</p>
          <p>Simultaneously, the simulation temperature must be reheated. As a force simulation converges toward equilibrium, an internal cooling parameter known as <code>alpha</code> gradually decays toward zero, eventually halting all updates to conserve CPU power. If a user drags a node after the simulation has cooled to rest, the surrounding connected nodes would remain frozen in place unless alpha is actively reheated. Setting <code>alphaTarget = 0.3</code> during the drag phase re-energizes the physics engine, allowing spring connections to stretch and pull neighboring nodes along with the dragged entity in an organic, fluid dance.</p>
        </section>

        <!-- Architectural Figure 2 Vector Diagram -->
        <figure class="article-figure">
          <svg viewBox="0 0 960 320" width="960" height="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="SVG Network Graph &amp; Force Simulation Architecture Diagram Comparing Electrostatic Repulsion, Hooke Springs &amp; Barnes-Hut Decomposition">
            <rect width="960" height="320" fill="#0D0D0D" rx="8"/>
            <rect x="1" y="1" width="958" height="318" fill="none" stroke="#222" rx="7"/>

            <!-- Grid Header -->
            <text x="480" y="32" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14" font-weight="800" text-anchor="middle" letter-spacing="0.06em">SVG NETWORK GRAPH ARCHITECTURE: MULTI-BODY FORCE SIMULATION PIPELINE</text>
            <line x1="40" y1="46" x2="920" y2="46" stroke="#262626" stroke-width="1"/>

            <!-- Column 1: Coulomb & Hooke Mechanics -->
            <g transform="translate(50, 65)">
              <rect width="260" height="230" fill="#141414" stroke="#262626" rx="6"/>
              <text x="130" y="24" fill="#C1DD2D" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PHYSICS 1: DUAL FORCES</text>

              <!-- Mini Force Vectors -->
              <circle cx="80" cy="100" r="12" fill="rgba(193,221,45,0.2)" stroke="#C1DD2D" stroke-width="2"/>
              <text x="80" y="104" fill="#FFF" font-family="JetBrains Mono, monospace" font-size="10" text-anchor="middle">u</text>

              <circle cx="180" cy="100" r="12" fill="rgba(56,189,248,0.2)" stroke="#38BDF8" stroke-width="2"/>
              <text x="180" y="104" fill="#FFF" font-family="JetBrains Mono, monospace" font-size="10" text-anchor="middle">v</text>

              <!-- Spring Link -->
              <line x1="92" y1="100" x2="168" y2="100" stroke="#888" stroke-width="2" stroke-dasharray="4 2"/>
              <!-- Repulsion Arrows (pointing away) -->
              <path d="M 64 100 L 46 100 M 52 95 L 46 100 L 52 105" stroke="#EF4444" stroke-width="1.5" fill="none"/>
              <path d="M 196 100 L 214 100 M 208 95 L 214 100 L 208 105" stroke="#EF4444" stroke-width="1.5" fill="none"/>
              <text x="130" y="85" fill="#C1DD2D" font-family="Inter, sans-serif" font-size="9" text-anchor="middle">Hooke Spring: F_attract</text>
              <text x="130" y="130" fill="#EF4444" font-family="Inter, sans-serif" font-size="9" text-anchor="middle">Coulomb Repel: F &prop; 1/d&sup2;</text>

              <text x="130" y="185" fill="#AAA" font-family="Inter, sans-serif" font-size="11" text-anchor="middle">Equilibrium: F_attract = F_repel</text>
              <text x="130" y="202" fill="#888" font-family="Inter, sans-serif" font-size="10.5" text-anchor="middle">Verlet Velocity Damping: &gamma; = 0.9</text>
              <text x="130" y="217" fill="#666" font-family="Inter, sans-serif" font-size="10" text-anchor="middle">Self-Organizing Spatial Harmony</text>
            </g>

            <!-- Column 2: Barnes-Hut Quadtree -->
            <g transform="translate(350, 65)">
              <rect width="260" height="230" fill="#141414" stroke="#262626" rx="6"/>
              <text x="130" y="24" fill="#38BDF8" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PHYSICS 2: BARNES-HUT QUADTREE</text>

              <!-- Quadtree Partition Grid -->
              <rect x="50" y="55" width="160" height="90" fill="#0D0D0D" stroke="#333" stroke-width="1"/>
              <line x1="130" y1="55" x2="130" y2="145" stroke="#444" stroke-width="1"/>
              <line x1="50" y1="100" x2="210" y2="100" stroke="#444" stroke-width="1"/>
              <!-- Sub-partition in NE -->
              <line x1="170" y1="55" x2="170" y2="100" stroke="#555" stroke-width="0.8"/>
              <line x1="130" y1="77" x2="210" y2="77" stroke="#555" stroke-width="0.8"/>

              <circle cx="90" cy="80" r="4" fill="#C1DD2D"/>
              <circle cx="80" cy="120" r="4" fill="#C1DD2D"/>
              <circle cx="150" cy="70" r="3" fill="#38BDF8"/>
              <circle cx="190" cy="65" r="3" fill="#38BDF8"/>
              <!-- Center of mass virtual node -->
              <circle cx="170" cy="67" r="7" fill="none" stroke="#F59E0B" stroke-width="1.5" stroke-dasharray="2 2"/>
              <text x="170" y="50" fill="#F59E0B" font-family="JetBrains Mono, monospace" font-size="8" text-anchor="middle">Cluster CoM</text>

              <text x="130" y="185" fill="#AAA" font-family="Inter, sans-serif" font-size="11" text-anchor="middle">Multipole Acceptance: &theta; = s / d &lt; 0.8</text>
              <text x="130" y="202" fill="#888" font-family="Inter, sans-serif" font-size="10.5" text-anchor="middle">Reduces O(N&sup2;) to O(N log N)</text>
              <text x="130" y="217" fill="#666" font-family="Inter, sans-serif" font-size="10" text-anchor="middle">Enables 120 FPS Large Graphs</text>
            </g>

            <!-- Column 3: Edge Geometry & Dragging -->
            <g transform="translate(650, 65)">
              <rect width="260" height="230" fill="#141414" stroke="#262626" rx="6"/>
              <text x="130" y="24" fill="#F59E0B" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">STAGE 3: CURVED EDGES &amp; PINNING</text>

              <!-- Quadratic Bézier Curved Link -->
              <circle cx="60" cy="110" r="10" fill="rgba(193,221,45,0.2)" stroke="#C1DD2D" stroke-width="1.5"/>
              <circle cx="200" cy="110" r="10" fill="rgba(245,158,11,0.2)" stroke="#F59E0B" stroke-width="1.5"/>

              <!-- Forward curve -->
              <path d="M 69 104 Q 130 65 191 104" stroke="#C1DD2D" stroke-width="1.8" fill="none"/>
              <!-- Reverse curve -->
              <path d="M 191 116 Q 130 155 69 116" stroke="#38BDF8" stroke-width="1.8" fill="none"/>
              <!-- Control Point indicator -->
              <circle cx="130" cy="75" r="2.5" fill="#EF4444"/>
              <text x="130" y="68" fill="#EF4444" font-family="JetBrains Mono, monospace" font-size="8" text-anchor="middle">CP (Midpoint + Normal)</text>

              <text x="130" y="185" fill="#AAA" font-family="Inter, sans-serif" font-size="11" text-anchor="middle">Separates Bidirectional Links</text>
              <text x="130" y="202" fill="#888" font-family="Inter, sans-serif" font-size="10.5" text-anchor="middle">Kinematic Drag Pinning: node.fx, fy</text>
              <text x="130" y="217" fill="#666" font-family="Inter, sans-serif" font-size="10" text-anchor="middle">Alpha Reheating on Pointerdown</text>
            </g>
          </svg>
          <figcaption>Figure 2: Comprehensive multi-body physics pipeline: Coulomb repulsion and Hooke spring mechanics, Barnes-Hut quadtree spatial acceleration, and parametric quadratic Bézier edge routing with kinematic drag pinning.</figcaption>
        </figure>

        <section id="section-interactive-studio">
          <h2>6. Interactive SVG Force-Directed Graph Studio</h2>
          <p>Experience real-time topological physics simulation within our interactive developer sandbox. Adjust repulsion charges, alter link spring equilibrium lengths, modulate centering gravity, toggle between straight lines and curved quadratic Bézier edges, and actively drag nodes across the canvas to observe organic physical convergence. Export standalone, production-ready SVG code complete with XML namespaces directly to your clipboard.</p>

          <div class="interactive-sandbox" id="interactive-network-studio">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <span>Interactive SVG Force Graph Studio</span>
                <span class="sandbox-badge">Real-Time Euler / Verlet Engine</span>
              </div>
              <div>
                <span style="font-size: 13px; color: #888;">Live Physics Simulation</span>
              </div>
            </div>

            <div class="sandbox-controls">
              <div class="control-row">
                <label for="net-topology-preset">Network Topology Preset</label>
                <select id="net-topology-preset" class="control-select">
                  <option value="mesh">Distributed Microservices Mesh (Clusters &amp; Gateways)</option>
                  <option value="social">Social Community Graph (Hubs &amp; Bridges)</option>
                  <option value="hierarchy">Hierarchical Directed DAG (Tree with Cross-Links)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="net-nodes-slider">Node Count (<span id="net-nodes-val">24</span>)</label>
                <input type="range" id="net-nodes-slider" class="control-input" min="12" max="45" value="24">
              </div>

              <div class="control-row">
                <label for="net-charge-slider">Repulsion Charge (<span id="net-charge-val">300</span>)</label>
                <input type="range" id="net-charge-slider" class="control-input" min="50" max="800" value="300">
              </div>

              <div class="control-row">
                <label for="net-link-slider">Spring Distance (<span id="net-link-val">70</span>)</label>
                <input type="range" id="net-link-slider" class="control-input" min="30" max="150" value="70">
              </div>

              <div class="control-row">
                <label for="net-gravity-slider">Center Gravity (<span id="net-gravity-val">0.05</span>)</label>
                <input type="range" id="net-gravity-slider" class="control-input" min="0.01" max="0.15" step="0.01" value="0.05">
              </div>

              <div class="control-row">
                <label for="net-edge-style">Edge Curvature Style</label>
                <select id="net-edge-style" class="control-select">
                  <option value="curved">Curved Quadratic Bézier</option>
                  <option value="straight">Straight Lines</option>
                </select>
              </div>
            </div>

            <div class="preview-stage-container" id="network-stage-wrap">
              <svg id="network-live-svg" class="network-svg-canvas" viewBox="0 0 820 520" width="820" height="520" xmlns="http://www.w3.org/2000/svg" role="graphics-document" aria-label="Interactive SVG Network Graph and Force-Directed Simulation Canvas">
                <!-- Dynamically populated by engine -->
              </svg>
            </div>

            <div class="stats-readout-box">
              <div class="stat-item">
                <span class="stat-label">Active Nodes</span>
                <span class="stat-val" id="stat-node-count">24</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Total Edges</span>
                <span class="stat-val" id="stat-edge-count">38</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Graph Density</span>
                <span class="stat-val highlight" id="stat-graph-density">0.14</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">System Alpha / Temp</span>
                <span class="stat-val" id="stat-alpha">0.02</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Status</span>
                <span class="stat-val" id="stat-sim-status">Converged</span>
              </div>
            </div>

            <div class="action-btn-row">
              <button class="copy-btn" id="copy-network-svg-btn" type="button">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>
                <span>Copy Standalone SVG</span>
              </button>
            </div>
          </div>
        </section>

        <section id="section-production-engine">
          <h2>7. Production-Grade ES6 Force-Directed Engine: Zero-Dependency Architecture</h2>
          <p>Integrating heavy external simulation libraries like D3-force or Cytoscape often introduces hundreds of kilobytes of unneeded dependencies into modern lightweight web applications. A focused, zero-dependency ES6 force engine delivers instantaneous load times, total bundle control, and effortless integration into React, Vue, Svelte, or native Web Components.</p>
          <p>Below is the complete, self-contained TypeScript/ES6 architecture implementing Euler integration, Coulomb repulsion, Hooke springs, centering gravity, and interactive node dragging:</p>

          <pre><code>/**
 * Zero-Dependency SVG Force-Directed Graph Engine
 * Author: Jouni Flemming (IconStash.io)
 * License: MIT
 */
export interface Node {
  id: string;
  x: number;
  y: number;
  vx: number;
  vy: number;
  fx?: number | null;
  fy?: number | null;
  radius: number;
  group: string;
}

export interface Link {
  source: string;
  target: string;
  sourceNode?: Node;
  targetNode?: Node;
  strength?: number;
}

export interface SimulationOptions {
  width: number;
  height: number;
  charge: number;
  linkDistance: number;
  gravity: number;
  friction: number;
  alphaDecay: number;
}

export class SvgForceSimulation {
  private nodes: Node[];
  private links: Link[];
  private options: SimulationOptions;
  public alpha: number = 1.0;
  private animFrameId: number | null = null;
  private onTickCallback?: () => void;

  constructor(nodes: Node[], links: Link[], options: Partial&lt;SimulationOptions&gt; = {}) {
    this.nodes = nodes;
    this.links = links;
    this.options = {
      width: 820,
      height: 520,
      charge: 300,
      linkDistance: 70,
      gravity: 0.05,
      friction: 0.9,
      alphaDecay: 0.02,
      ...options
    };
    this.resolveLinkReferences();
  }

  private resolveLinkReferences(): void {
    const nodeMap = new Map&lt;string, Node&gt;();
    this.nodes.forEach(n =&gt; nodeMap.set(n.id, n));
    this.links.forEach(l =&gt; {
      l.sourceNode = nodeMap.get(l.source);
      l.targetNode = nodeMap.get(l.target);
    });
  }

  public tick(): void {
    if (this.alpha &lt; 0.005) return;
    const { width, height, charge, linkDistance, gravity, friction } = this.options;
    const cx = width / 2;
    const cy = height / 2;

    // 1. Coulomb Repulsion between all pairs
    const n = this.nodes.length;
    for (let i = 0; i &lt; n; i++) {
      const u = this.nodes[i];
      for (let j = i + 1; j &lt; n; j++) {
        const v = this.nodes[j];
        let dx = v.x - u.x;
        let dy = v.y - u.y;
        let distSq = dx * dx + dy * dy;
        if (distSq === 0) { dx = (Math.random() - 0.5) * 2; dy = (Math.random() - 0.5) * 2; distSq = 4; }
        const dist = Math.sqrt(distSq);
        const force = (charge / distSq) * this.alpha;
        const fx = (dx / dist) * force;
        const fy = (dy / dist) * force;

        u.vx -= fx;
        u.vy -= fy;
        v.vx += fx;
        v.vy += fy;
      }
    }

    // 2. Hooke's Spring Attraction along links
    for (const link of this.links) {
      const u = link.sourceNode;
      const v = link.targetNode;
      if (!u || !v) continue;
      const dx = v.x - u.x;
      const dy = v.y - u.y;
      const dist = Math.sqrt(dx * dx + dy * dy) || 1;
      const delta = (dist - linkDistance) * 0.08 * this.alpha;
      const fx = (dx / dist) * delta;
      const fy = (dy / dist) * delta;

      u.vx += fx;
      u.vy += fy;
      v.vx -= fx;
      v.vy -= fy;
    }

    // 3. Center Gravity &amp; Position Updates
    for (const node of this.nodes) {
      // Centering force
      node.vx -= (node.x - cx) * gravity * this.alpha;
      node.vy -= (node.y - cy) * gravity * this.alpha;

      // Friction damping
      node.vx *= friction;
      node.vy *= friction;

      // Kinematic pinning check
      if (node.fx != null) {
        node.x = node.fx;
        node.vx = 0;
      } else {
        node.x += node.vx;
      }

      if (node.fy != null) {
        node.y = node.fy;
        node.vy = 0;
      } else {
        node.y += node.vy;
      }

      // Viewport boundary clamping
      node.x = Math.max(node.radius, Math.min(width - node.radius, node.x));
      node.y = Math.max(node.radius, Math.min(height - node.radius, node.y));
    }

    this.alpha *= (1 - this.options.alphaDecay);
  }

  public reheat(): void {
    this.alpha = 0.3;
  }
}</code></pre>
        
          <p>When deploying force-directed graph engines into high-concurrency enterprise monitoring platforms, isolating the physics simulation from the main browser UI thread becomes essential. Running intensive force calculations directly on the main JavaScript thread risks dropping frames during complex DOM reflows or heavy user input handling. The state-of-the-art vector architecture offloads simulation physics to a dedicated Web Worker.</p>
          <p>Within the Web Worker, the simulation updates particle positions inside a high-speed Float64Array buffer. On each tick, the worker transfers the raw coordinate buffer across the worker boundary using zero-copy Transferable ArrayBuffers or updates a SharedArrayBuffer. The main thread simply reads the updated coordinates during its requestAnimationFrame loop, updating SVG circle cx and cy attributes via direct DOM references. This clean architectural separation guarantees that user interactions, dashboard typing, and menu scrolling remain silky smooth at 120 FPS regardless of graph scale.</p>
          <p>Furthermore, the SVG rendering engine employs batch attribute mutation. Rather than updating element attributes one by one in interleaved reads and writes (which triggers browser layout thrashing), the engine reads all client dimensions once, calculates all node and edge vectors in pure JavaScript memory, and then executes all setAttribute mutations in a single contiguous write phase.</p>
</section>

        <section id="section-scalability-hybrid">
          <h2>8. Scalability Limits: When to Use SVG Elements vs Canvas / WebGL Hybrid Architectures</h2>
          <p>Architects must evaluate the fundamental trade-offs between retained-mode vector graphics (SVG) and immediate-mode rasterization (HTML5 Canvas and WebGL) when choosing a visualization engine for graph datasets.</p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Architecture Dimension</th>
                  <th>Native Pure SVG DOM</th>
                  <th>HTML5 Canvas 2D</th>
                  <th>WebGL Shader Graph</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Recommended Node Limit</strong></td>
                  <td>Up to 1,500 Nodes</td>
                  <td>1,500 to 15,000 Nodes</td>
                  <td>15,000 to 500,000+ Nodes</td>
                </tr>
                <tr>
                  <td><strong>Visual Sharpness on Zoom</strong></td>
                  <td>Infinite Vector Scalability</td>
                  <td>Pixelated unless redrawn at DPR</td>
                  <td>Infinite via GPU projection</td>
                </tr>
                <tr>
                  <td><strong>Styling &amp; Animations</strong></td>
                  <td>Pure CSS, Transitions &amp; Filters</td>
                  <td>Manual pixel repainting loop</td>
                  <td>Custom fragment/vertex shaders</td>
                </tr>
                <tr>
                  <td><strong>DOM Event Binding</strong></td>
                  <td>Native pointerdown / click per node</td>
                  <td>Manual Euclidean raycasting</td>
                  <td>Color-picking buffer or KD-tree</td>
                </tr>
                <tr>
                  <td><strong>Accessibility (Screen Readers)</strong></td>
                  <td>Full ARIA Hierarchy &amp; Tree Roles</td>
                  <td>Requires hidden parallel DOM</td>
                  <td>Requires hidden parallel DOM</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p>For applications where node counts remain below 1,500 entities (such as cloud architecture diagrams, microservice health dashboards, or organizational team hierarchies), SVG is unquestionably superior. It provides seamless CSS theme adaptability, crisp typography rendering on high-DPI displays, and zero-overhead native DOM event dispatching.</p>
        </section>

        <section id="section-accessibility-theming">
          <h2>9. Accessibility, ARIA Graphs &amp; Dark/Light Mode Theme Switching</h2>
          <p>Ensuring compliance with WCAG 2.2 Level AA accessibility guidelines requires careful implementation across screen-reader semantics and visual contrast.</p>
          <p>For screen-reader accessibility, the SVG root element must be equipped with <code>role="graphics-document"</code> and a descriptive <code>aria-label</code> detailing the graph's scope and nature. Within the node group, each circular marker carries <code>role="graphics-symbol"</code>, <code>tabindex="0"</code>, and an <code>aria-label</code> communicating the entity name, group classification, and inbound/outbound connection counts. Keyboard users can navigate through nodes using Tab and trigger modal details or connection highlights using Enter or Spacebar.</p>
          <p>For dark and light mode theming, avoiding hardcoded colors is critical. In dark mode, our design uses deep backgrounds (<code>#0A0A0A</code>) paired with vibrant lime (<code>#C1DD2D</code>) and electric cyan (<code>#38BDF8</code>) for maximum visual contrast. When the user switches to light mode (via <code>html[data-theme="light"]</code>), background reflectance surges. Our system immediately transforms active links and accents to deep olive green <code>#4D6300</code>, delivering a contrast ratio exceeding 5.2:1 against pure white surfaces, strictly fulfilling WCAG 2.2 AA mandates.</p>

          <div class="takeaway-box">
            <h3>Key Architectural Takeaways</h3>
            <ul>
              <li><strong>Balance Repulsion and Spring Stiffness:</strong> Calibrate Coulomb repulsion and Hooke spring tension to achieve stable physical equilibrium without chaotic node oscillation.</li>
              <li><strong>Optimize with Barnes-Hut:</strong> Employ quadtree spatial partitioning to reduce pairwise calculation complexity from O(N^2) to O(N log N) for large graphs.</li>
              <li><strong>Use Quadratic Béziers for Bidirectional Edges:</strong> Offset control points perpendicularly from midpoints to keep parallel links distinctly visible.</li>
              <li><strong>Transform Coordinates via getScreenCTM:</strong> Always multiply pointer coordinates by the inverted CTM matrix to prevent drag drift in responsive viewports.</li>
              <li><strong>Enforce WCAG 2.2 AA Contrast Across Themes:</strong> Use `#4D6300` in light mode to preserve contrast ratios greater than 4.5:1 on white backgrounds.</li>
            </ul>
          </div>
        </section>

        <section class="faq-section" id="section-faq">
          <h2>10. Frequently Asked Questions</h2>
          <div class="faq-item">
            <div class="faq-question">How does Coulomb electrostatic repulsion operate in a force-directed graph simulation?</div>
            <div class="faq-answer">In a force-directed simulation, every node is modeled as an electrically charged particle that exerts a repulsive force on every other node in the system according to Coulomb inverse-square law: F = k_charge / distance squared. As two nodes move closer together, the repulsive force increases asymptotically, preventing node overlap and spreading interconnected clusters across the available canvas. Because computing all pairwise forces across N nodes requires O(N squared) operations per animation frame, production engines employ the Barnes-Hut quadtree algorithm to approximate distant particle clusters as single center-of-mass monopoles, reducing simulation complexity to O(N log N).</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How is Hooke law applied to simulate elastic spring tension along graph edges?</div>
            <div class="faq-answer">Every topological link or edge connecting node u and node v is modeled as a linear physical spring with a resting equilibrium length L_0 and stiffness constant k_spring. According to Hooke law, the restorative force is directly proportional to the displacement from equilibrium: F_spring = k_spring * (currentDistance - L_0). If the nodes are pulled farther apart than L_0, the spring exerts an attractive force pulling them together; if compressed closer than L_0, the spring pushes them apart. This elastic tension pulls topologically connected communities into tight visual clusters while repulsion forces keep separate clusters spaced apart.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How do you render curved edges and bidirectional links in native SVG?</div>
            <div class="faq-answer">Straight SVG line elements fail when multiple parallel edges exist between the same pair of nodes or when bidirectional relationships must be displayed, as the lines render directly on top of each other. The standard architectural solution is computing quadratic Bézier curves using SVG path elements: M x1 y1 Q cx cy x2 y2. The control point (cx, cy) is positioned at the midpoint between the two nodes and offset perpendicular to the edge direction vector by a displacement proportional to link index and edge curvature settings. For directional graphs, marker-end attributes reference reusable arrowhead markers in the SVG defs container.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How does interactive node dragging work without disrupting simulation physics?</div>
            <div class="faq-answer">When a user grabs a node with pointer events, the node is pinned by assigning fixed position coordinates (fx and fy) that override standard physics velocity integration during subsequent simulation ticks. The simulation temperature or alpha parameter is immediately reheated (e.g., alphaTarget = 0.3) so surrounding connected nodes organically react and reorganize around the dragged node. In SVG, mouse coordinates must be transformed through the SVG container inverse Screen-to-Canvas Current Transformation Matrix (CTM) to ensure sub-pixel dragging accuracy across responsive viewports and high-DPI zoom levels.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">What is the practical scalability limit of rendering network graphs in native SVG versus Canvas or WebGL?</div>
            <div class="faq-answer">Native SVG graphs excel for small-to-medium network topologies containing up to 1,500 nodes and 3,000 edges, delivering infinite resolution scalability, rich CSS styling, DOM event listeners, and full accessibility trees. However, because each node, edge, and label represents a distinct DOM element, topologies exceeding 2,500 nodes experience significant memory consumption and frame rate drops during physics simulation. For massive graphs with tens of thousands of nodes, developers should employ a hybrid architecture: rendering background physics and edges onto HTML5 Canvas or WebGL shaders, while rendering selected nodes, hover rings, and tooltips in an SVG vector overlay.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How do you ensure force-directed SVG graphs comply with WCAG 2.2 AA accessibility mandates?</div>
            <div class="faq-answer">A compliant SVG network graph includes role="graphics-document" on the svg container, accompanied by aria-label and descriptive title and desc elements detailing total node count, edge density, and primary topological clusters. Every individual node carries role="graphics-symbol", keyboard focusability via tabindex="0", and detailed aria-label attributes listing node identity, degree centrality, and connected neighbor IDs. Keyboard navigation handlers allow users to press Tab or arrow keys to traverse from a focused node across its connected topological links, backed by high-contrast border strokes exceeding a 4.5:1 ratio against the dark or light canvas.</div>
          </div>
        </section>

      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <a href="#section-graph-foundations">1. Graph Theory &amp; SVG DOM</a>
            <a href="#section-physics-simulation">2. Coulomb &amp; Hooke Physics</a>
            <a href="#section-barnes-hut-optimization">3. Barnes-Hut Quadtree</a>
            <a href="#section-edge-geometry">4. Curved Edge Geometry</a>
            <a href="#section-interactive-dragging">5. Dragging &amp; Pinning</a>
            <a href="#interactive-network-studio">6. Interactive Studio Sandbox</a>
            <a href="#section-production-engine">7. Production ES6 Engine</a>
            <a href="#section-scalability-hybrid">8. Scalability &amp; Canvas Limits</a>
            <a href="#section-accessibility-theming">9. Accessibility &amp; Theming</a>
            <a href="#section-faq">10. Frequently Asked Questions</a>
          </nav>
        </div>

        <div class="sidebar-card cta-sidebar-box">
          <div class="cta-title">Explore Related Guides</div>
          <p>Deepen your data visualization mastery with our complete series of SVG vector graphics guides:</p>
          <div class="toc-nav">
            <a href="/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide/">SVG Scatter Plots Guide</a>
            <a href="/articles/svg-gauges-and-circular-progress-bars-guide/">SVG Gauges Guide</a>
            <a href="/articles/svg-bar-charts-and-column-graph-visualization-guide/">SVG Bar Charts Guide</a>
            <a href="/articles/svg-donut-charts-and-circular-percentage-visualization-guide/">SVG Donut Charts Guide</a>
            <a href="/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/">SVG Sparklines Guide</a>
            <a href="/articles/svg-tree-diagrams-and-hierarchical-visualization-guide/">SVG Tree Diagrams Guide</a>
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

    // Interactive Force-Directed Network Graph Studio Implementation
    (function initNetworkStudio() {
      const liveSvg = document.getElementById('network-live-svg');
      const presetSelect = document.getElementById('net-topology-preset');
      const nodesSlider = document.getElementById('net-nodes-slider');
      const nodesVal = document.getElementById('net-nodes-val');
      const chargeSlider = document.getElementById('net-charge-slider');
      const chargeVal = document.getElementById('net-charge-val');
      const linkSlider = document.getElementById('net-link-slider');
      const linkVal = document.getElementById('net-link-val');
      const gravitySlider = document.getElementById('net-gravity-slider');
      const gravityVal = document.getElementById('net-gravity-val');
      const edgeStyleSelect = document.getElementById('net-edge-style');
      const copyBtn = document.getElementById('copy-network-svg-btn');

      const statNodeCount = document.getElementById('stat-node-count');
      const statEdgeCount = document.getElementById('stat-edge-count');
      const statDensity = document.getElementById('stat-graph-density');
      const statAlpha = document.getElementById('stat-alpha');
      const statStatus = document.getElementById('stat-sim-status');

      if (!liveSvg) return;

      const groupColors = {
        core: '#C1DD2D',
        gateway: '#38BDF8',
        storage: '#F59E0B',
        worker: '#EC4899',
        auth: '#A855F7'
      };

      let nodes = [];
      let links = [];
      let alpha = 1.0;
      let draggedNode = null;
      let animId = null;

      function generateGraphData(preset, nodeCount) {
        const newNodes = [];
        const newLinks = [];
        const groups = ['core', 'gateway', 'storage', 'worker', 'auth'];

        for (let i = 0; i < nodeCount; i++) {
          const grp = groups[i % groups.length];
          const radius = i < 3 ? 14 : (8 + (i % 4) * 2);
          const angle = (i / nodeCount) * 2 * Math.PI;
          const dist = 100 + Math.random() * 80;
          newNodes.push({
            id: `N-${i + 1}`,
            x: 410 + Math.cos(angle) * dist,
            y: 260 + Math.sin(angle) * dist,
            vx: 0,
            vy: 0,
            fx: null,
            fy: null,
            radius,
            group: grp
          });
        }

        if (preset === 'mesh') {
          // Clustered mesh
          for (let i = 0; i < nodeCount; i++) {
            // Ring neighbor
            newLinks.push({ source: newNodes[i].id, target: newNodes[(i + 1) % nodeCount].id });
            // Gateway connections
            if (i > 2 && Math.random() < 0.45) {
              newLinks.push({ source: newNodes[i].id, target: newNodes[i % 3].id });
            }
          }
        } else if (preset === 'social') {
          // Hub and spoke with cross bridges
          const hubs = [0, 1, 2];
          for (let i = 3; i < nodeCount; i++) {
            const chosenHub = hubs[i % hubs.length];
            newLinks.push({ source: newNodes[i].id, target: newNodes[chosenHub].id });
            if (i > 3 && Math.random() < 0.35) {
              newLinks.push({ source: newNodes[i].id, target: newNodes[i - 1].id });
            }
          }
          newLinks.push({ source: newNodes[0].id, target: newNodes[1].id });
          newLinks.push({ source: newNodes[1].id, target: newNodes[2].id });
          newLinks.push({ source: newNodes[2].id, target: newNodes[0].id });
        } else {
          // Hierarchy tree with cross links
          for (let i = 1; i < nodeCount; i++) {
            const parent = Math.floor((i - 1) / 2);
            newLinks.push({ source: newNodes[i].id, target: newNodes[parent].id });
            if (i % 3 === 0 && i + 1 < nodeCount) {
              newLinks.push({ source: newNodes[i].id, target: newNodes[i + 1].id });
            }
          }
        }

        return { nodes: newNodes, links: newLinks };
      }

      function rebuildGraph() {
        const preset = presetSelect ? presetSelect.value : 'mesh';
        const nodeCount = nodesSlider ? parseInt(nodesSlider.value, 10) : 24;
        const graph = generateGraphData(preset, nodeCount);
        nodes = graph.nodes;
        links = graph.links;

        // Resolve pointers
        const nodeMap = new Map();
        nodes.forEach(n => nodeMap.set(n.id, n));
        links.forEach(l => {
          l.sourceNode = nodeMap.get(l.source);
          l.targetNode = nodeMap.get(l.target);
        });

        alpha = 1.0;

        if (statNodeCount) statNodeCount.textContent = String(nodes.length);
        if (statEdgeCount) statEdgeCount.textContent = String(links.length);
        const maxPossibleEdges = (nodes.length * (nodes.length - 1)) / 2;
        const density = maxPossibleEdges > 0 ? (links.length / maxPossibleEdges).toFixed(2) : '0';
        if (statDensity) statDensity.textContent = density;

        renderBaseSvg();
      }

      function renderBaseSvg() {
        liveSvg.innerHTML = '';

        // Background
        const bg = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        bg.setAttribute("width", "820");
        bg.setAttribute("height", "520");
        bg.setAttribute("fill", "#0D0D0D");
        bg.setAttribute("rx", "6");
        liveSvg.appendChild(bg);

        // Arrow marker defs
        const defs = document.createElementNS("http://www.w3.org/2000/svg", "defs");
        const marker = document.createElementNS("http://www.w3.org/2000/svg", "marker");
        marker.setAttribute("id", "net-arrow");
        marker.setAttribute("viewBox", "0 0 10 10");
        marker.setAttribute("refX", "8");
        marker.setAttribute("refY", "5");
        marker.setAttribute("markerWidth", "5");
        marker.setAttribute("markerHeight", "5");
        marker.setAttribute("orient", "auto-start-reverse");

        const mPath = document.createElementNS("http://www.w3.org/2000/svg", "path");
        mPath.setAttribute("d", "M 0 1.5 L 10 5 L 0 8.5 z");
        mPath.setAttribute("fill", "#555555");
        marker.appendChild(mPath);
        defs.appendChild(marker);
        liveSvg.appendChild(defs);

        // Edge Group
        const edgeG = document.createElementNS("http://www.w3.org/2000/svg", "g");
        edgeG.setAttribute("class", "graph-edges");
        edgeG.setAttribute("id", "live-edge-group");
        liveSvg.appendChild(edgeG);

        // Node Group
        const nodeG = document.createElementNS("http://www.w3.org/2000/svg", "g");
        nodeG.setAttribute("class", "graph-nodes");
        nodeG.setAttribute("id", "live-node-group");
        liveSvg.appendChild(nodeG);

        // Populate Edge DOM Elements
        links.forEach((l, idx) => {
          const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
          path.setAttribute("id", `edge-${idx}`);
          path.setAttribute("class", "network-edge");
          path.setAttribute("stroke", "#333333");
          path.setAttribute("stroke-width", "1.5");
          path.setAttribute("fill", "none");
          path.setAttribute("marker-end", "url(#net-arrow)");
          edgeG.appendChild(path);
        });

        // Populate Node DOM Elements
        nodes.forEach((n) => {
          const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
          g.setAttribute("id", `node-g-${n.id}`);
          g.setAttribute("class", "network-node-g");

          const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          circle.setAttribute("id", `node-${n.id}`);
          circle.setAttribute("class", "network-node");
          circle.setAttribute("r", String(n.radius));
          circle.setAttribute("fill", groupColors[n.group] || '#C1DD2D');
          circle.setAttribute("stroke", "#1A1A1A");
          circle.setAttribute("stroke-width", "2");
          circle.setAttribute("role", "graphics-symbol");
          circle.setAttribute("tabindex", "0");
          circle.setAttribute("aria-label", `Node ${n.id}, Group ${n.group}`);

          const title = document.createElementNS("http://www.w3.org/2000/svg", "title");
          title.textContent = `${n.id} (${n.group})`;
          circle.appendChild(title);

          const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
          text.setAttribute("id", `node-lbl-${n.id}`);
          text.setAttribute("font-family", "Inter, sans-serif");
          text.setAttribute("font-size", "9");
          text.setAttribute("font-weight", "600");
          text.setAttribute("fill", "#AAAAAA");
          text.setAttribute("text-anchor", "middle");
          text.setAttribute("dy", String(n.radius + 12));
          text.textContent = n.id;

          g.appendChild(circle);
          g.appendChild(text);

          // Drag Events
          circle.addEventListener('pointerdown', (e) => {
            draggedNode = n;
            circle.setPointerCapture(e.pointerId);
            alpha = 0.35; // Reheat
            const pt = getSvgCoords(e.clientX, e.clientY);
            n.fx = pt.x;
            n.fy = pt.y;
            e.stopPropagation();
          });

          circle.addEventListener('pointermove', (e) => {
            if (draggedNode === n) {
              const pt = getSvgCoords(e.clientX, e.clientY);
              n.fx = pt.x;
              n.fy = pt.y;
              alpha = 0.35; // Keep warm
            }
          });

          circle.addEventListener('pointerup', (e) => {
            if (draggedNode === n) {
              circle.releasePointerCapture(e.pointerId);
              n.fx = null;
              n.fy = null;
              draggedNode = null;
            }
          });

          nodeG.appendChild(g);
        });
      }

      function getSvgCoords(clientX, clientY) {
        const pt = liveSvg.createSVGPoint();
        pt.x = clientX;
        pt.y = clientY;
        const ctm = liveSvg.getScreenCTM();
        if (!ctm) return { x: clientX, y: clientY };
        const res = pt.matrixTransform(ctm.inverse());
        return { x: res.x, y: res.y };
      }

      function physicsStep() {
        const charge = chargeSlider ? parseFloat(chargeSlider.value) : 300;
        const linkDist = linkSlider ? parseFloat(linkSlider.value) : 70;
        const gravity = gravitySlider ? parseFloat(gravitySlider.value) : 0.05;
        const edgeStyle = edgeStyleSelect ? edgeStyleSelect.value : 'curved';

        const width = 820;
        const height = 520;
        const cx = width / 2;
        const cy = height / 2;

        if (alpha > 0.005) {
          // 1. Coulomb Repulsion
          const numNodes = nodes.length;
          for (let i = 0; i < numNodes; i++) {
            const u = nodes[i];
            for (let j = i + 1; j < numNodes; j++) {
              const v = nodes[j];
              let dx = v.x - u.x;
              let dy = v.y - u.y;
              let distSq = dx * dx + dy * dy;
              if (distSq === 0) { dx = (Math.random() - 0.5) * 2; dy = (Math.random() - 0.5) * 2; distSq = 4; }
              const dist = Math.sqrt(distSq);
              const force = (charge / distSq) * alpha;
              const fx = (dx / dist) * force;
              const fy = (dy / dist) * force;

              u.vx -= fx;
              u.vy -= fy;
              v.vx += fx;
              v.vy += fy;
            }
          }

          // 2. Hooke's Elastic Links
          for (const l of links) {
            const u = l.sourceNode;
            const v = l.targetNode;
            if (!u || !v) continue;
            const dx = v.x - u.x;
            const dy = v.y - u.y;
            const dist = Math.sqrt(dx * dx + dy * dy) || 1;
            const delta = (dist - linkDist) * 0.08 * alpha;
            const fx = (dx / dist) * delta;
            const fy = (dy / dist) * delta;

            u.vx += fx;
            u.vy += fy;
            v.vx -= fx;
            v.vy -= fy;
          }

          // 3. Center Gravity & Movement
          for (const n of nodes) {
            n.vx -= (n.x - cx) * gravity * alpha;
            n.vy -= (n.y - cy) * gravity * alpha;

            n.vx *= 0.9;
            n.vy *= 0.9;

            if (n.fx != null) {
              n.x = n.fx;
              n.vx = 0;
            } else {
              n.x += n.vx;
            }

            if (n.fy != null) {
              n.y = n.fy;
              n.vy = 0;
            } else {
              n.y += n.vy;
            }

            // Boundary limits
            n.x = Math.max(n.radius + 10, Math.min(width - n.radius - 10, n.x));
            n.y = Math.max(n.radius + 10, Math.min(height - n.radius - 10, n.y));
          }

          alpha *= 0.985;
          if (statAlpha) statAlpha.textContent = alpha.toFixed(3);
          if (statStatus) statStatus.textContent = alpha > 0.02 ? 'Simulating' : 'Converged';
        }

        // Update DOM positions
        links.forEach((l, idx) => {
          const path = document.getElementById(`edge-${idx}`);
          if (!path || !l.sourceNode || !l.targetNode) return;
          const u = l.sourceNode;
          const v = l.targetNode;

          if (edgeStyle === 'curved') {
            const mx = (u.x + v.x) / 2;
            const my = (u.y + v.y) / 2;
            const dx = v.x - u.x;
            const dy = v.y - u.y;
            const len = Math.sqrt(dx * dx + dy * dy) || 1;
            const nx = -dy / len;
            const ny = dx / len;
            const offset = (idx % 2 === 0 ? 1 : -1) * 16;
            const cxPt = mx + nx * offset;
            const cyPt = my + ny * offset;

            // Trim end to land on target boundary
            const endX = v.x - (dx / len) * (v.radius + 4);
            const endY = v.y - (dy / len) * (v.radius + 4);

            path.setAttribute("d", `M ${u.x.toFixed(1)} ${u.y.toFixed(1)} Q ${cxPt.toFixed(1)} ${cyPt.toFixed(1)} ${endX.toFixed(1)} ${endY.toFixed(1)}`);
          } else {
            const dx = v.x - u.x;
            const dy = v.y - u.y;
            const len = Math.sqrt(dx * dx + dy * dy) || 1;
            const endX = v.x - (dx / len) * (v.radius + 4);
            const endY = v.y - (dy / len) * (v.radius + 4);

            path.setAttribute("d", `M ${u.x.toFixed(1)} ${u.y.toFixed(1)} L ${endX.toFixed(1)} ${endY.toFixed(1)}`);
          }
        });

        nodes.forEach((n) => {
          const circle = document.getElementById(`node-${n.id}`);
          const text = document.getElementById(`node-lbl-${n.id}`);
          if (circle) {
            circle.setAttribute("cx", n.x.toFixed(1));
            circle.setAttribute("cy", n.y.toFixed(1));
          }
          if (text) {
            text.setAttribute("x", n.x.toFixed(1));
            text.setAttribute("y", n.y.toFixed(1));
          }
        });

        animId = requestAnimationFrame(physicsStep);
      }

      function reheat() {
        alpha = 0.35;
      }

      // Event Listeners
      if (presetSelect) presetSelect.addEventListener('change', () => { rebuildGraph(); reheat(); });
      if (nodesSlider) nodesSlider.addEventListener('input', () => {
        if (nodesVal) nodesVal.textContent = nodesSlider.value;
        rebuildGraph();
        reheat();
      });
      if (chargeSlider) chargeSlider.addEventListener('input', () => {
        if (chargeVal) chargeVal.textContent = chargeSlider.value;
        reheat();
      });
      if (linkSlider) linkSlider.addEventListener('input', () => {
        if (linkVal) linkVal.textContent = linkSlider.value;
        reheat();
      });
      if (gravitySlider) gravitySlider.addEventListener('input', () => {
        if (gravityVal) gravityVal.textContent = gravitySlider.value;
        reheat();
      });
      if (edgeStyleSelect) edgeStyleSelect.addEventListener('change', reheat);

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

      rebuildGraph();
      physicsStep();
    })();
  </script>
</body>
</html>
'''

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Article 2 generated successfully at: {target_file}")
