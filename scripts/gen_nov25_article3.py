import os

html = r"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <title>Shadcn UI Icons: Lucide, Phosphor &amp; Hugeicons (2026) | IconStash</title>
  <meta name="description" content="Complete 2026 guide to shadcn/ui icons: compare Lucide, Phosphor, Hugeicons, Tabler & Remix, run npx shadcn migrate icons, and optimize Tailwind v4 SVGs.">
  <meta name="keywords" content="shadcn icons, shadcn ui icons, best icon library for shadcn, shadcn migrate icons, lucide vs phosphor vs hugeicons, custom svg icons shadcn ui, tailwind v4 button svg">
  <meta property="og:title" content="Shadcn UI Icons Complete Guide (2026): Lucide vs. Phosphor vs. Hugeicons vs. Tabler &amp; CLI Migration">
  <meta property="og:description" content="Complete 2026 guide to shadcn/ui icons: compare Lucide, Phosphor, Hugeicons, Tabler & Remix, run npx shadcn migrate icons, and optimize Tailwind v4 SVGs.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/shadcn-ui-icons-complete-guide-2026/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/shadcn-ui-icons-complete-guide-2026.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-25T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-25T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="UI Engineering &amp; Icon Systems">
  <meta property="article:tag" content="shadcn/ui">
  <meta property="article:tag" content="SVG Icons">
  <meta property="article:tag" content="Lucide">
  <meta property="article:tag" content="Phosphor Icons">
  <meta property="article:tag" content="Tailwind CSS">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Shadcn UI Icons Complete Guide (2026): Lucide vs. Phosphor vs. Hugeicons vs. Tabler &amp; CLI Migration">
  <meta name="twitter:description" content="Complete 2026 guide to shadcn/ui icons: compare Lucide, Phosphor, Hugeicons, Tabler & Remix, run npx shadcn migrate icons, and optimize Tailwind v4 SVGs.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/shadcn-ui-icons-complete-guide-2026.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/shadcn-ui-icons-complete-guide-2026/">
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
      "headline": "Shadcn UI Icons Complete Guide (2026): Lucide vs. Phosphor vs. Hugeicons vs. Tabler & CLI Migration",
      "description": "Complete 2026 guide to shadcn/ui icons: compare Lucide, Phosphor, Hugeicons, Tabler & Remix, run npx shadcn migrate icons, and optimize Tailwind v4 SVGs.",
      "image": "https://iconstash.io/assets/articles/shadcn-ui-icons-complete-guide-2026.jpg",
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
      "mainEntityOfPage": "https://iconstash.io/articles/shadcn-ui-icons-complete-guide-2026/",
      "inLanguage": "en-US",
      "wordCount": 4051,
      "articleSection": "UI Engineering & Icon Systems",
      "keywords": [
        "shadcn icons",
        "shadcn ui icons",
        "best icon library for shadcn",
        "shadcn migrate icons",
        "lucide vs phosphor vs hugeicons",
        "custom svg icons shadcn ui",
        "tailwind v4 button svg"
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
          "name": "Shadcn UI Icons Complete Guide (2026)",
          "item": "https://iconstash.io/articles/shadcn-ui-icons-complete-guide-2026/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the default icon library used by shadcn/ui in 2026?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Lucide React (lucide-react) is the default icon library for shadcn/ui across New York and Default styles, providing 1,979 uniform 2px-stroke ISC-licensed SVG icons on a 24x24 grid. Legacy projects initialized with Radix UI style presets originally used @radix-ui/react-icons on a 15x15 grid."
          }
        },
        {
          "@type": "Question",
          "name": "How do you switch icon libraries in an existing shadcn/ui codebase?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Run npx shadcn@latest migrate icons inside your project root (or pass --from lucide --to phosphor --yes). The shadcn CLI runs an AST codemod across your components/ui directory, installs the target package, rewrites icon imports and JSX components, and updates iconLibrary inside components.json."
          }
        },
        {
          "@type": "Question",
          "name": "Which icon library is the best alternative to Lucide for shadcn/ui?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Choose Phosphor Icons (9,198 icons, MIT) when your design system needs six distinct visual weights including Duotone and Fill active states; choose Tabler Icons (6,324 icons, MIT) for exhaustive enterprise coverage on a crisp 24x24 stroke grid; or choose Hugeicons (5,115 free icons, MIT) for modern rounded SaaS aesthetics."
          }
        },
        {
          "@type": "Question",
          "name": "How does shadcn/ui automatically size SVG icons inside buttons and inputs?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Modern Tailwind v4 shadcn/ui components include the arbitrary child selector [&_svg:not([class*='size-'])]:size-4 alongside [&_svg]:pointer-events-none and [&_svg]:shrink-0. Any SVG without an explicit size-* utility automatically inherits 16x16px sizing while remaining overridable with className='size-5'."
          }
        },
        {
          "@type": "Question",
          "name": "How do you use custom inline SVG icons inside shadcn/ui components?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Wrap your clean SVG paths in a React component accepting React.ComponentProps<'svg'>, apply stroke='currentColor' or fill='currentColor' instead of hardcoded hex codes, forward {...props}, and drop it directly inside Button, DropdownMenuItem, or Alert components so Tailwind child selectors size and color it automatically."
          }
        },
        {
          "@type": "Question",
          "name": "Why do Lucide or Phosphor icons slow down Next.js dev server cold starts and how do you fix it?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Importing named icons from top-level barrel exports like lucide-react or @phosphor-icons/react can cause development bundlers to parse thousands of re-exported modules. Enable experimental.optimizePackageImports in next.config.ts (or import directly from deep paths or an SVG sprite sheet) to keep HMR and cold starts instant."
          }
        },
        {
          "@type": "Question",
          "name": "How do you make icon-only shadcn/ui buttons accessible under WCAG 2.2 AA?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Always add aria-label or a visually hidden <span class='sr-only'>Action Name</span> inside icon-only Button size='icon' controls while setting aria-hidden='true' on the decorative SVG itself. Maintain at least a 3:1 contrast ratio for non-text UI graphics and avoid shrinking clickable buttons below 24x24px."
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
    .site-header .logo { display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 18px; color: #F2F2F2; flex-shrink: 0; white-space: nowrap; }
    .site-header .logo svg { width: 24px; height: 24px; color: #C1DD2D; flex-shrink: 0; }
    .site-header nav { display: flex; gap: 24px; align-items: center; }
    .site-header nav a { color: #888; font-size: 14px; font-weight: 500; }
    .site-header nav a:hover { color: #F2F2F2; }
    .header-cta { background: #C1DD2D; color: #0A0A0A !important; font-weight: 700; padding: 7px 16px; border-radius: 6px; font-size: 13px; transition: background 150ms ease; white-space: nowrap; }
    .header-cta:hover { background: #D2ED3E; }
    .theme-toggle-btn { background: #1A1A1A; border: 1px solid #2E2E2E; color: #888; width: 34px; height: 34px; border-radius: 6px; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 150ms ease; flex-shrink: 0; }
    .theme-toggle-btn:hover { color: #F2F2F2; border-color: #444; }

    .page-container { max-width: 1240px; margin: 0 auto; padding: 32px 24px 80px; }
    .breadcrumb { display: flex; align-items: center; gap: 8px; font-size: 13px; color: #666; margin-bottom: 24px; flex-wrap: wrap; }
    .breadcrumb a { color: #888; }
    .breadcrumb a:hover { color: #C1DD2D; }
    .breadcrumb .sep { color: #444; }
    .breadcrumb .current { color: #C1DD2D; font-weight: 500; }

    .article-hero { margin-bottom: 40px; border-bottom: 1px solid #1F1F1F; padding-bottom: 32px; }
    .article-hero .tag { display: inline-block; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #C1DD2D; background: rgba(193,221,45,0.08); border: 1px solid rgba(193,221,45,0.2); padding: 4px 10px; border-radius: 4px; margin-bottom: 16px; }
    .article-hero h1 { font-size: clamp(26px, 5vw, 40px); font-weight: 900; line-height: 1.2; color: #FFFFFF; letter-spacing: -0.03em; margin-bottom: 16px; max-width: 1040px; }
    .article-meta { display: flex; flex-wrap: wrap; align-items: center; gap: 16px; font-size: 14px; color: #777; }
    .article-meta a { color: #999; font-weight: 600; }
    .article-meta a:hover { color: #C1DD2D; }

    .article-layout { display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: 48px; align-items: start; }
    .article-main { min-width: 0; }
    @media (max-width: 980px) { .article-layout { grid-template-columns: 1fr; } .article-sidebar { position: static; } }
    @media (max-width: 768px) {
      .site-header { padding: 0 16px; }
      .site-header nav { gap: 10px; }
      .site-header nav a:not(.header-cta) { display: none; }
      .header-cta { padding: 6px 12px; font-size: 12.5px; }
      .page-container { padding: 20px 16px 64px; }
      .interactive-sandbox { padding: 16px; }
      .preview-stage-container { padding: 12px; min-height: 260px; }
    }

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
    .secondary-btn { background: #1E1E1E; border: 1px solid #383838; color: #F2F2F2; padding: 8px 14px; border-radius: 6px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 150ms ease; }
    .secondary-btn:hover { border-color: #C1DD2D; color: #C1DD2D; }

    .preview-stage-container { background: #0D0D0D; border: 1px solid #222; border-radius: 8px; padding: 20px; display: flex; justify-content: center; align-items: center; position: relative; min-height: 440px; user-select: none; touch-action: none; }
    .shadcn-svg-canvas { width: 100%; max-width: 760px; height: auto; touch-action: none; cursor: pointer; }

    .stats-readout-box { background: #161616; border: 1px solid #262626; border-radius: 8px; padding: 14px 18px; margin-top: 18px; display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px; }
    .stat-item { display: flex; flex-direction: column; }
    .stat-label { font-size: 11px; text-transform: uppercase; color: #888; font-weight: 600; }
    .stat-val { font-size: 15px; font-weight: 800; color: #FFF; font-family: "JetBrains Mono", monospace; }
    .stat-val.highlight { color: #C1DD2D; }

    .action-btn-row { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 12px; margin-top: 16px; }
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
    html[data-theme="light"] .secondary-btn { background: #FFFFFF; border-color: #D1D5DB; color: #18181B; }
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

  <main class="page-container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">IconStash</a>
      <span class="sep">/</span>
      <a href="/articles/">Articles</a>
      <span class="sep">/</span>
      <span class="current">Shadcn UI Icons Complete Guide</span>
    </nav>

    <header class="article-hero">
      <span class="tag">UI Engineering &amp; Icon Systems</span>
      <h1>Shadcn UI Icons Complete Guide (2026): Lucide vs. Phosphor vs. Hugeicons vs. Tabler &amp; CLI Migration</h1>
      <div class="article-meta">
        <span>Published by <a href="/about/">Jouni Flemming</a></span>
        <span>•</span>
        <span>Updated November 25, 2026</span>
        <span>•</span>
        <span>29 min read</span>
        <span>•</span>
        <span>4,051 words</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">
        <div class="featured-summary">
          <p><strong>Direct Answer:</strong> Shadcn UI defaults to <strong>Lucide React</strong> (1,979 ISC-licensed 24×24 icons) via <code>iconLibrary</code> in <code>components.json</code> and sizes SVGs automatically with Tailwind v4 child selectors like <code>[&_svg:not([class*='size-'])]:size-4</code>. You can swap cleanly to <strong>Phosphor</strong> (9,198 icons, 6 weights), <strong>Tabler</strong> (6,324 icons), <strong>Hugeicons</strong> (5,115 free icons), or <strong>Remix Icon</strong> (3,244 icons) using <code>npx shadcn@latest migrate icons</code>.</p>
          <ul>
            <li><strong>Head-to-Head Library Data:</strong> Verified IconStash benchmarks comparing icon counts, licenses, weights, grid units, and tree-shaking behavior across the five official shadcn/ui contenders.</li>
            <li><strong>Automated AST Codemods:</strong> Step-by-step guide to running <code>npx shadcn@latest migrate icons</code>, resolving unmapped glyph names, and migrating legacy 15×15 Radix projects.</li>
            <li><strong>Custom SVGs &amp; Performance:</strong> Inject brand SVGs using <code>currentColor</code> and <code>React.ComponentProps&lt;'svg'&gt;</code>, and eliminate Next.js dev cold-start slowdowns with <code>optimizePackageImports</code>.</li>
            <li><strong>Interactive Preview Studio:</strong> Preview Lucide, Phosphor, Hugeicons, Tabler, and Remix aesthetics inside live shadcn/ui Buttons, Inputs, and Navigation Cards—then copy clean SVG or <code>components.json</code> config.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/shadcn-ui-icons-complete-guide-2026.jpg"
               alt="Isometric dark UI tiles displaying crisp electric lime and white vector UI icons for shadcn/ui design systems"
               width="1200" height="675"
               fetchpriority="high" decoding="async">
          <figcaption>Figure 1: Precision 24×24 vector icon architecture powering modern shadcn/ui, Tailwind CSS v4, and React 19 component primitives.</figcaption>
        </figure>

        <section id="section-shadcn-architecture">
          <h2>1. How Shadcn UI Handles Icons Under the Hood (components.json &amp; Tailwind v4)</h2>
          <p><strong>Short Answer:</strong> Shadcn UI stores your active icon family inside the <code>iconLibrary</code> field of <code>components.json</code> and styles icons from parent components using Tailwind arbitrary variants—specifically <code>[&_svg]:pointer-events-none</code>, <code>[&_svg]:shrink-0</code>, and <code>[&_svg:not([class*='size-'])]:size-4</code>—so icons adapt cleanly without manual wrapper classes.</p>

          <p>Unlike monolithic React component packages that wrap every glyph inside a rigid proprietary wrapper, shadcn/ui copies open component source directly into your repository's <code>components/ui/</code> directory. That copy-and-own model makes icon architecture extraordinarily transparent—yet it also catches teams off guard when icons shrink unevenly inside flex buttons, fail to inherit disabled text colors, or break during Tailwind v3-to-v4 upgrades.</p>

          <h3>Inside components.json &amp; The iconLibrary Token</h3>
          <p>Whenever you run <code>npx shadcn@latest init</code> or add primitives via the registry CLI, the generator reads <code>components.json</code> at your project root. The <code>iconLibrary</code> key tells the CLI which package imports and JSX component names to emit when scaffolding <code>Select</code>, <code>Dialog</code>, <code>DropdownMenu</code>, <code>Calendar</code>, and <code>Sidebar</code>:</p>

          <pre><code>{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui"
  }
}</code></pre>

          <h3>Why Tailwind v4 Uses :not([class*='size-']) Inside Buttons</h3>
          <p>Inspect a modern 2026 shadcn/ui <code>Button</code> class string generated by <code>class-variance-authority</code> (CVA) and you will notice three specific SVG descendant selectors: <code>[&_svg]:pointer-events-none</code>, <code>[&_svg:not([class*='size-'])]:size-4</code>, and <code>[&_svg]:shrink-0</code>. Each selector solves a real production layout bug:</p>

          <ul>
            <li><strong><code>[&_svg]:pointer-events-none</code>:</strong> Prevents clicks aimed at a button's leading icon from targeting an inner SVG <code>&lt;path&gt;</code> element instead of the parent button—eliminating subtle event delegation and analytics tracking mismatches.</li>
            <li><strong><code>[&_svg]:shrink-0</code>:</strong> Stops CSS Flexbox from squashing a 16×16 icon into an oval whenever button text wraps or overflows inside narrow mobile drawers.</li>
            <li><strong><code>[&_svg:not([class*='size-'])]:size-4</code>:</strong> Applies a consistent <code>16px × 16px</code> default box to every icon inside the button <em>unless</em> you explicitly override it with <code>className="size-5"</code> or <code>size-6</code>. Older Tailwind v3 setups used <code>[&_svg]:size-4</code> without <code>:not()</code>, which caused specificity battles whenever developers passed custom icon sizes.</li>
          </ul>

          <h3>Component-by-Component Icon Sizing &amp; RTL Mirroring Rules</h3>
          <p>Different shadcn/ui primitives apply tailored icon size selectors depending on visual density. While standard <code>Button</code>, <code>DropdownMenuItem</code>, and <code>SelectTrigger</code> components default child SVGs to <code>size-4</code> (16px), compact controls like <code>Badge</code> use <code>[&>svg]:size-3</code> (12px), and <code>Alert</code> banners reserve a dedicated <code>[&>svg]:size-4</code> grid column offset by <code>translate-y-0.5</code> so the icon centers optically against the alert headline rather than floating too high.</p>
          <p>For internationalized SaaS interfaces supporting Arabic or Hebrew right-to-left (RTL) layouts, directional icons such as <code>ChevronRight</code>, <code>ArrowLeft</code>, and sidebar collapse arrows must mirror automatically. Adding Tailwind's <code>rtl:rotate-180</code> utility onto directional icons—while keeping symmetric icons like <code>Search</code>, <code>Check</code>, and <code>Clock</code> unmirrored—keeps navigation intuitive globally. See our <a href="/articles/rtl-iconography-mirroring-guide/">RTL iconography mirroring guide</a> for the complete directional taxonomy.</p>

          <h3>Tailwind v4 CSS-First Token Configuration &amp; Button Padding Offsets</h3>
          <p>Tailwind CSS v4 replaces legacy <code>tailwind.config.js</code> JavaScript themes with CSS-first <code>@theme inline</code> blocks inside <code>globals.css</code>. When pairing icons with text inside shadcn/ui <code>Button</code> variants, Tailwind v4 also exposes clean <code>has-[&gt;svg]:px-3</code> rules inside CVA definitions—automatically tightening horizontal padding whenever an icon sits adjacent to text so visual margins feel balanced on both sides of the button.</p>
        </section>

        <section id="section-library-benchmark">
          <h2>2. Head-to-Head Benchmark: Lucide vs. Phosphor vs. Hugeicons vs. Tabler vs. Remix</h2>
          <p><strong>Short Answer:</strong> Lucide (1,979 icons, ISC) remains the zero-friction shadcn/ui default; Phosphor (9,198 icons, MIT) wins for multi-weight Thin-to-Duotone UI hierarchy; Tabler (6,324 icons, MIT) leads raw enterprise coverage; Hugeicons (5,115 free icons, MIT) delivers polished rounded SaaS geometry; and Remix Icon (3,244 icons, Apache 2.0) pairs crisp line and solid toggles.</p>

          <p>Because thousands of AI-generated SaaS templates ship default Lucide icons out of the box, switching your icon family is one of the highest-leverage ways to give a shadcn/ui product a bespoke visual identity. Using verified metadata from the <a href="/stats/">IconStash 28-library open dataset</a> (134,701 total indexed SVG icons), the benchmark matrix below compares the five core libraries supported across modern shadcn workflows alongside legacy Radix Icons.</p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th scope="col">Icon Library</th>
                  <th scope="col">Indexed Count</th>
                  <th scope="col">License</th>
                  <th scope="col">Styles / Weights</th>
                  <th scope="col">Base Grid</th>
                  <th scope="col">Primary NPM Package</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Lucide Icons</strong></td>
                  <td>1,979</td>
                  <td>ISC (Zero Attribution)</td>
                  <td>1 weight (2px stroke)</td>
                  <td>24×24</td>
                  <td><code>lucide-react</code></td>
                </tr>
                <tr>
                  <td><strong>Phosphor Icons</strong></td>
                  <td>9,198</td>
                  <td>MIT (Zero Attribution)</td>
                  <td>6 weights (Thin–Duotone)</td>
                  <td>256×256 viewBox</td>
                  <td><code>@phosphor-icons/react</code></td>
                </tr>
                <tr>
                  <td><strong>Tabler Icons</strong></td>
                  <td>6,324</td>
                  <td>MIT (Zero Attribution)</td>
                  <td>Outline + Filled</td>
                  <td>24×24</td>
                  <td><code>@tabler/icons-react</code></td>
                </tr>
                <tr>
                  <td><strong>Hugeicons</strong></td>
                  <td>5,115 (free tier)</td>
                  <td>MIT (Free Core)</td>
                  <td>Stroke Rounded + Multi</td>
                  <td>24×24</td>
                  <td><code>@hugeicons/react</code></td>
                </tr>
                <tr>
                  <td><strong>Remix Icon</strong></td>
                  <td>3,244</td>
                  <td>Apache 2.0</td>
                  <td>Line &amp; Fill pairs</td>
                  <td>24×24</td>
                  <td><code>@remixicon/react</code></td>
                </tr>
                <tr>
                  <td><strong>Radix Icons (Legacy)</strong></td>
                  <td>345</td>
                  <td>MIT (Zero Attribution)</td>
                  <td>1 weight (1px crisp)</td>
                  <td>15×15</td>
                  <td><code>@radix-ui/react-icons</code></td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3>Choosing the Right Library for Your Product Aesthetic</h3>
          <p>Each of these five packages pairs differently with Tailwind CSS typography and shadcn/ui border radii. Compare how they perform in real product scenarios—and explore full deep dives in our <a href="/articles/lucide-icons-complete-guide/">Lucide guide</a>, <a href="/articles/phosphor-icons-complete-guide/">Phosphor guide</a>, <a href="/articles/tabler-icons-complete-guide/">Tabler guide</a>, and <a href="/articles/hugeicons-complete-guide/">Hugeicons guide</a>:</p>

          <ul>
            <li><strong>Lucide React — Zero-Friction Standard:</strong> Ideal when shipping fast with zero custom configuration. Every shadcn block, community registry, and documentation example compiles verbatim. Its uniform 2px rounded-cap stroke pairs naturally with Inter and Geist typography, though it lacks native filled or duotone variants for active navigation indicators.</li>
            <li><strong>Phosphor Icons — Best for State &amp; Weight Hierarchy:</strong> With six weights sharing identical geometric skeletons, Phosphor lets you render <code>weight="regular"</code> in inactive sidebar tabs and snap seamlessly to <code>weight="fill"</code> or <code>weight="duotone"</code> on active routes. Remember to configure Next.js barrel optimization or use SSR-safe imports from <code>@phosphor-icons/react/dist/ssr</code>.</li>
            <li><strong>Tabler Icons — Best for Dense Enterprise &amp; DevTools:</strong> Tabler boasts over 6,300 crisp technical glyphs covering Kubernetes pods, database schemas, financial ledgers, and hardware telemetry that smaller packs omit. You can tune stroke thickness globally via <code>stroke={1.75}</code> without breaking grid alignment.</li>
            <li><strong>Hugeicons — Best for Modern Consumer SaaS:</strong> Featuring generously curved squircle corners and friendly proportions, Hugeicons immediately differentiates dashboards from stock templates. Note that Hugeicons splits its React wrapper (<code>@hugeicons/react</code>) from its icon data package (<code>@hugeicons/core-free-icons</code>), rendering via <code>&lt;HugeiconsIcon icon={Search01Icon} /&gt;</code>.</li>
            <li><strong>Remix Icon — Best for High-Contrast Line/Fill Pairs:</strong> Every core concept in Remix ships an exact <code>-line</code> and <code>-fill</code> twin on a clean 24×24 grid under Apache 2.0, making dark-mode tab bars and mobile bottom navigation instantly legible.</li>
          </ul>

          <h3>Commercial Licensing, Attribution &amp; Open-Source Safety in Production</h3>
          <p>Before standardizing an icon package across an enterprise SaaS product or commercial UI kit, legal and procurement teams audit open-source licenses carefully. Lucide (ISC), Phosphor (MIT), Tabler (MIT), Hugeicons Core Free (MIT), and Remix Icon (Apache 2.0) all grant unrestricted commercial usage with zero attribution requirements—allowing you to ship closed-source products, sell templates, and bundle SVGs without footer credits. Across all 134,701 icons indexed on IconStash, 94.5% (127,291 icons) require zero attribution, whereas libraries like Solar Icons (CC BY 4.0) require visible attribution credits. Review our <a href="/articles/icon-licensing-explained-mit-apache-cc/">open-source icon licensing guide</a> before embedding third-party packs into redistributable client SDKs.</p>

          <h3>Zero-Dependency Direct SVG Export via IconStash</h3>
          <p>If your Next.js marketing landing page only needs twelve crisp icons—a search magnifier, three feature badges, social links, and an arrow—installing a 1,900-icon npm dependency is often unnecessary overhead. Searching IconStash lets you preview Lucide, Phosphor, Tabler, Hugeicons, and 24 additional open-source libraries side by side on the exact same concept page, customize stroke thickness and color live, and export single-click React JSX or minimal SVG paths with zero npm dependencies.</p>
        </section>

        <section id="section-cli-migration">
          <h2>3. Automated Migration with npx shadcn@latest migrate icons</h2>
          <p><strong>Short Answer:</strong> Switching an established codebase between icon libraries no longer requires manual find-and-replace across dozens of files. Execute <code>npx shadcn@latest migrate icons --from lucide --to phosphor</code> to run shadcn's AST codemod, rewrite JSX imports and tags automatically, and update <code>components.json</code>.</p>

          <p>Previously, swapping a 40-component shadcn/ui project from Lucide to Tabler or Phosphor meant hunting down every <code>ChevronDown</code>, <code>Check</code>, <code>X</code>, and <code>MoreHorizontal</code> inside <code>components/ui/</code> and guessing the target library's naming convention (for instance, Lucide's <code>X</code> maps to Tabler's <code>IconX</code> or Phosphor's <code>XIcon</code>). The official shadcn CLI migration command automates that translation using an internal symbol mapping table and TypeScript AST transforms.</p>

          <pre><code># Interactive mode (prompts for source &amp; target library)
npx shadcn@latest migrate icons

# Direct non-interactive migration from Lucide to Phosphor
npx shadcn@latest migrate icons --from lucide --to phosphor --yes

# Migrate from Lucide to Tabler Icons
npx shadcn@latest migrate icons --from lucide --to tabler --yes

# Migrate from Lucide to Hugeicons
npx shadcn@latest migrate icons --from lucide --to hugeicons --yes</code></pre>

          <h3>What the Codemod Modifies—and What Still Needs Manual Review</h3>
          <p>After the migration script finishes, always run <code>git diff</code> and <code>npx tsc --noEmit</code> before committing. Three common edge cases require a quick manual pass:</p>

          <ol>
            <li><strong>Prop Differences (<code>className</code> vs <code>size</code> vs <code>strokeWidth</code>):</strong> Lucide accepts <code>strokeWidth={1.75}</code>, whereas Phosphor expects <code>weight="bold"</code> or <code>weight="regular"</code> and Hugeicons expects <code>strokeWidth={1.5}</code> on <code>&lt;HugeiconsIcon&gt;</code>. The CLI rewrites basic imports cleanly, so verify custom wrapper props in your feature components.</li>
            <li><strong>Custom App Routes Outside <code>components/ui/</code>:</strong> Verify whether the codemod scanned custom feature folders (such as <code>src/features/billing/</code>) or only your configured UI alias directory.</li>
            <li><strong>Fallback Glyphs on Niche Icons:</strong> If your app imports a highly specialized Lucide glyph lacking a 1:1 entry in the migration map, inspect IconStash's cross-library concept search to pick the closest visual match rather than mixing two different stroke weights side by side.</li>
          </ol>

          <h3>Custom Shadcn Registry Blocks &amp; Multi-Library Design Systems</h3>
          <p>Teams publishing internal company registries via <code>shadcn build</code> often distribute shared dashboard blocks across multiple product squads. When authoring custom registry JSON manifests, avoid hardcoding one-off icon hacks inside deeply nested component files. Instead, keep icon imports isolated cleanly at the top of each UI primitive using standard named imports so downstream apps configured with <code>"iconLibrary": "phosphor"</code> or <code>"iconLibrary": "tabler"</code> can run <code>npx shadcn@latest add</code> and have the registry resolver automatically remap icons to match the host project's <code>components.json</code> preference.</p>

          <h3>Troubleshooting Common CLI Migration TypeScript Errors</h3>
          <p>Two predictable TypeScript errors occasionally surface immediately after migrating from Lucide to Hugeicons or Phosphor. First, Hugeicons renders icons via a unified wrapper component (<code>&lt;HugeiconsIcon icon={Search01Icon} /&gt;</code>) rather than standalone JSX tags, meaning type annotations typed strictly as <code>LucideIcon</code> in sidebar navigation configs should be broadened to <code>React.ReactNode</code> or a generic render callback. Second, verify that your <code>tsconfig.json</code> excludes stale build artifacts inside <code>.next/types</code> by running <code>rm -rf .next && npx tsc --noEmit</code> right after migration.</p>
        </section>

        <section id="section-architecture-pipeline">
          <h2>4. Figure 2: Shadcn UI Multi-Library Icon Resolution Pipeline</h2>
          <p>Understanding how <code>components.json</code>, AST registry transforms, React component wrappers, Tailwind v4 child selectors, and bundler tree-shaking fit together prevents bloated client bundles and broken SSR icons. Figure 2 traces the complete lifecycle from CLI scaffold to production browser paint.</p>

          <figure class="article-figure">
            <svg viewBox="0 0 960 320" width="960" height="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figure 2: Shadcn UI Icon Resolution and Tree-Shaking Pipeline">
              <rect width="960" height="320" fill="#0D0D0D" rx="8" stroke="#222222" stroke-width="1"></rect>
              <defs>
                <marker id="shArrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
                  <polygon points="0 0, 8 3, 0 6" fill="#C1DD2D"></polygon>
                </marker>
              </defs>

              <g transform="translate(24, 40)">
                <rect width="196" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="98" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="700" text-anchor="middle">STAGE 1: CONFIG</text>
                <text x="98" y="56" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">components.json</text>
                <rect x="18" y="78" width="160" height="28" fill="#1C1C1C" rx="4"></rect>
                <text x="98" y="96" fill="#A3A3A3" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">"iconLibrary": "lucide"</text>
                <text x="98" y="136" fill="#CCCCCC" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">CLI Registry Transform</text>
                <text x="98" y="156" fill="#888888" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">shadcn add / migrate</text>
                <rect x="18" y="182" width="160" height="28" fill="#1C1C1C" rx="4" stroke="#C1DD2D" stroke-width="0.6"></rect>
                <text x="98" y="200" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">AST Import Rewrite</text>
                <text x="98" y="228" fill="#666666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Zero Lock-In Ownership</text>
              </g>

              <line x1="220" y1="160" x2="250" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#shArrow)"></line>

              <g transform="translate(258, 40)">
                <rect width="196" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="98" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="700" text-anchor="middle">STAGE 2: ICON ADAPTER</text>
                <text x="98" y="56" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Library or Custom SVG</text>
                <rect x="18" y="78" width="160" height="28" fill="#1C1C1C" rx="4"></rect>
                <text x="98" y="96" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Lucide / Phosphor / Tabler</text>
                <text x="98" y="136" fill="#CCCCCC" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">currentColor Inheritance</text>
                <text x="98" y="156" fill="#888888" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">24x24 viewBox Parity</text>
                <rect x="18" y="182" width="160" height="28" fill="#1C1C1C" rx="4" stroke="#38BDF8" stroke-width="0.6"></rect>
                <text x="98" y="200" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">ComponentProps&lt;'svg'&gt;</text>
                <text x="98" y="228" fill="#666666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">IconStash Custom Export</text>
              </g>

              <line x1="454" y1="160" x2="484" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#shArrow)"></line>

              <g transform="translate(492, 40)">
                <rect width="196" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="98" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="700" text-anchor="middle">STAGE 3: TAILWIND v4</text>
                <text x="98" y="56" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">CVA Child Selectors</text>
                <rect x="18" y="78" width="160" height="28" fill="#1C1C1C" rx="4"></rect>
                <text x="98" y="96" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">not([class*='size-']):size-4</text>
                <text x="98" y="136" fill="#CCCCCC" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">[&amp;_svg]:shrink-0</text>
                <text x="98" y="156" fill="#888888" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">pointer-events-none</text>
                <rect x="18" y="182" width="160" height="28" fill="#1C1C1C" rx="4" stroke="#A855F7" stroke-width="0.6"></rect>
                <text x="98" y="200" fill="#A855F7" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">CSS Theme Tokens</text>
                <text x="98" y="228" fill="#666666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Dark / Light WCAG AA</text>
              </g>

              <line x1="688" y1="160" x2="718" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#shArrow)"></line>

              <g transform="translate(726, 40)">
                <rect width="210" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="105" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="700" text-anchor="middle">STAGE 4: BUNDLE</text>
                <text x="105" y="56" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">RSC &amp; Sprite Output</text>
                <rect x="18" y="78" width="174" height="28" fill="#1C1C1C" rx="4"></rect>
                <text x="105" y="96" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">optimizePackageImports</text>
                <text x="105" y="136" fill="#CCCCCC" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">Zero-JS Server Icons</text>
                <text x="105" y="156" fill="#888888" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">or /sprite.svg#icon Sprite</text>
                <rect x="18" y="182" width="174" height="28" fill="#1C1C1C" rx="4" stroke="#C1DD2D" stroke-width="0.6"></rect>
                <text x="105" y="200" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">ARIA + sr-only Verified</text>
                <text x="105" y="228" fill="#666666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Sub-2KB Client Payload</text>
              </g>
            </svg>
            <figcaption>Figure 2: End-to-end shadcn/ui icon resolution architecture linking components.json registry tokens, Tailwind v4 SVG selectors, and Next.js tree-shaking.</figcaption>
          </figure>
        </section>

        <section id="section-custom-svg">
          <h2>5. Custom SVG Icons, Brand Marks &amp; currentColor Inheritance in Shadcn Components</h2>
          <p><strong>Short Answer:</strong> To integrate bespoke brand logos or custom SVGs exported from IconStash into shadcn/ui components, accept <code>React.ComponentProps&lt;'svg'&gt;</code>, replace hardcoded hex colors with <code>currentColor</code>, set <code>aria-hidden="true"</code> by default, and spread <code>{...props}</code> onto the root <code>&lt;svg&gt;</code> element.</p>

          <p>Every engineering team eventually needs icons that no general UI library provides—a custom SaaS product mark, a fintech payment rail badge, or a domain-specific diagram glyph. Dropping raw Figma SVG exports directly into a shadcn/ui <code>&lt;Button&gt;</code> frequently fails in two ways: Figma hardcodes <code>width="24" height="24"</code> and <code>fill="#111827"</code>, overriding dark-mode hover states and Tailwind's automatic <code>size-4</code> scaling.</p>

          <h3>The Canonical React 19 Custom SVG Icon Pattern</h3>
          <p>Follow this TypeScript component pattern (compatible with React 19, Next.js App Router, and Tailwind v4) so custom icons behave indistinguishably from native Lucide components inside buttons, dropdown menus, and badges:</p>

          <pre><code>import * as React from "react";
import { cn } from "@/lib/utils";

export function BrandLayersIcon({
  className,
  ...props
}: React.ComponentProps&lt;"svg"&gt;) {
  return (
    &lt;svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth={2}
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      className={cn("shrink-0", className)}
      {...props}
    &gt;
      &lt;polygon points="12 2 2 7 12 12 22 7 12 2" /&gt;
      &lt;polyline points="2 17 12 22 22 17" /&gt;
      &lt;polyline points="2 12 12 17 22 12" /&gt;
    &lt;/svg&gt;
  );
}

// Usage inside shadcn/ui Button (automatically sized to size-4 unless overridden)
// &lt;Button variant="outline"&gt;&lt;BrandLayersIcon /&gt; Deploy Stack&lt;/Button&gt;
// &lt;Button size="lg"&gt;&lt;BrandLayersIcon className="size-5 text-lime-400" /&gt; Launch&lt;/Button&gt;</code></pre>

          <p>Notice why we omit fixed <code>width</code> and <code>height</code> attributes on the JSX <code>&lt;svg&gt;</code> (or rely strictly on CSS <code>size-4</code>): Tailwind v4's <code>[&_svg:not([class*='size-'])]:size-4</code> sets CSS <code>width: 1rem; height: 1rem;</code> cleanly, while <code>stroke="currentColor"</code> ensures hover, focus, and destructive button variants recolor the icon in lockstep with button text. For deeper color-token patterns, see our <a href="/articles/how-to-change-svg-color-in-css-and-react-guide/">SVG color &amp; currentColor guide</a> and <a href="/articles/how-to-use-svg-icons-in-react-nextjs-tailwind/">React, Next.js &amp; Tailwind SVG workflow guide</a>.</p>

          <h3>Automating Figma-to-Shadcn SVG Cleanup with SVGO</h3>
          <p>When designers hand off custom SVG icons from Figma or Illustrator, exported files routinely contain bloated <code>&lt;g id="Frame 42"&gt;</code> wrappers, hardcoded <code>fill="#0F172A"</code> fills, <code>clipPath</code> IDs that collide across the DOM, and redundant decimal precision. Running exports through an automated SVGO pipeline—using <code>removeDimensions: true</code> (preserving <code>viewBox</code>), <code>convertColors: { currentColor: true }</code>, and <code>prefixIds</code>—guarantees every custom icon drops straight into shadcn/ui components without dark-mode visibility failures or byte bloat. Read our <a href="/articles/figma-to-code-svg-icon-pipeline-guide/">Figma-to-Code SVG pipeline guide</a> and <a href="/articles/svgo-ci-cd-optimization-playbook/">SVGO CI/CD playbook</a> for drop-in GitHub Actions configs.</p>

          <h3>The Dynamic-Name Import Anti-Pattern &amp; Safe Registry Maps</h3>
          <p>CMS-driven navigation menus often tempt developers into writing dynamic barrel lookups such as <code>import * as Icons from 'lucide-react'; const Icon = Icons[menuItem.iconName];</code>. Importing the entire namespace object defeats Webpack and Vite static tree-shaking completely—shipping every single icon in the package (hundreds of kilobytes of JS) straight to every visitor's mobile browser! Instead, maintain an explicit whitelist map of the 15 to 40 icons your navigation schema permits (<code>const NAV_ICONS = { home: Home, billing: CreditCard, settings: Settings };</code>) or load dynamically imported chunks via <code>React.lazy</code> only for rarely opened admin drawers.</p>
        </section>

        <section id="section-treeshaking-sprites">
          <h2>6. Next.js App Router Tree-Shaking, Barrel Imports &amp; SVG Sprite Optimization</h2>
          <p><strong>Short Answer:</strong> Importing icons via barrel paths like <code>import { Search, Bell } from 'lucide-react'</code> can slow Next.js dev builds if the bundler transforms all 1,900+ icon modules. Enable <code>experimental.optimizePackageImports</code> in <code>next.config.ts</code>—and switch to an external <code>&lt;svg&gt;&lt;use&gt;</code> sprite sheet when rendering 150+ unique icons on dense data tables.</p>

          <p>Production tree-shaking in Webpack, Turbopack, and Vite strips unused icon components from final builds, keeping production JS lean. However, during local development and CI server compilation, barrel files exporting thousands of components can quietly add seconds to cold route compilation and inflate React Server Component (RSC) serialized payloads if dozens of interactive client components bundle inline path strings repeatedly.</p>

          <pre><code>// next.config.ts — Prevent barrel-file dev slowdowns across icon packages
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  experimental: {
    optimizePackageImports: [
      "lucide-react",
      "@phosphor-icons/react",
      "@tabler/icons-react",
      "@remixicon/react",
      "@hugeicons/core-free-icons",
    ],
  },
};

export default nextConfig;</code></pre>

          <h3>When SVG Sprites Beat Inline React Icon Components</h3>
          <p>Suppose your SaaS admin panel renders a 200-row table where every row displays 4 status icons (800 inline <code>&lt;svg&gt;</code> DOM subtrees containing 3,200 repeated <code>&lt;path&gt;</code> nodes). Inline JSX duplicates identical SVG path markup across all 200 rows, inflating HTML document size and DOM memory. Moving high-frequency table icons into a static <code>public/icons/sprite.svg</code> file referenced via <code>&lt;svg className="size-4"&gt;&lt;use href="/icons/sprite.svg#check" /&gt;&lt;/svg&gt;</code> eliminates repeated path strings completely while keeping full <code>currentColor</code> styling. Read our <a href="/articles/svg-sprites-vs-inline-svg-vs-components/">SVG Sprites vs. Inline SVG vs. Components benchmark</a> for exact memory and HTML byte measurements.</p>

          <div class="warning-box">
            <div class="warning-title">Watch Out for Server vs. Client Boundary Serialization in Next.js</div>
            <p>Never pass raw icon component functions (<code>icon={SearchIcon}</code>) from a React Server Component down to a <code>"use client"</code> sidebar item! Functions cannot be serialized across the Next.js RSC boundary and will throw a runtime error. Instead, pass pre-rendered JSX elements (<code>icon={&lt;SearchIcon /&gt;}</code>) or pass a string key mapped inside the client component.</p>
          </div>

          <h3>Benchmarking HTML Payload, Memory &amp; INP Across Icon Architectures</h3>
          <p>Choosing between RSC inline icons, client-side JSX icons, and external SVG sprites directly impacts Interaction to Next Paint (INP) and total HTML transfer size. Rendering 35 distinct navigation and toolbar icons in React Server Components keeps client JavaScript overhead at <code>0 KB</code> while adding roughly <code>4.2 KB</code> of gzipped HTML. Conversely, repeating 500 identical status icons inside a virtualized React client table duplicates 500 SVG subtrees in browser memory—slowing hydration and React reconciliation. Switching repeated table badges to an external SVG <code>&lt;use&gt;</code> sprite sheet cuts DOM node count by over 75% and reduces table re-render latency below 2 milliseconds.</p>
        </section>

        <section id="section-interactive-studio">
          <h2>7. Interactive Shadcn UI Icon Library &amp; Component Preview Studio</h2>
          <p>Compare how the five flagship shadcn/ui icon ecosystems transform identical UI primitives in real time. Switch between <strong>Lucide</strong>, <strong>Phosphor (Duotone)</strong>, <strong>Hugeicons</strong>, <strong>Tabler</strong>, and <strong>Remix Icon</strong>, inspect Buttons, Search Inputs, Alert Banners, or Sidebar Navigation, tune stroke weight and Tailwind <code>size-*</code> tokens, and copy either the live standalone SVG showcase or a ready-to-paste <code>components.json</code> configuration.</p>
          <p>Notice how subtle geometric parameters transform perceived brand polish across identical shadcn layouts: increasing corner radii from <code>4px</code> (Tabler/Remix) to <code>10px</code> (Hugeicons) pairs naturally with rounded stroke caps, whereas Phosphor's duotone <code>0.2</code> fill opacity creates immediate active-tab hierarchy without loud background boxes. Click any rendered component slot on the canvas—or focus it with <code>Tab</code> and cycle via <code>ArrowLeft</code> / <code>ArrowRight</code>—to inspect focus ring offsets and token bindings live.</p>

          <div class="interactive-sandbox" id="interactive-shadcn-studio">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C1DD2D" stroke-width="2">
                  <rect x="3" y="3" width="7" height="7" rx="1.5"></rect>
                  <rect x="14" y="3" width="7" height="7" rx="1.5"></rect>
                  <rect x="3" y="14" width="7" height="7" rx="1.5"></rect>
                  <rect x="14" y="14" width="7" height="7" rx="1.5"></rect>
                </svg>
                <span>Interactive Shadcn UI Icon &amp; Token Studio</span>
              </div>
              <span class="sandbox-badge">Tailwind v4 + React 19</span>
            </div>

            <div class="sandbox-controls">
              <div class="control-row">
                <label for="sh-library-select">Shadcn iconLibrary Preset</label>
                <select id="sh-library-select" class="control-select">
                  <option value="lucide" selected>Lucide (Default 2px Minimal)</option>
                  <option value="phosphor">Phosphor (Multi-Weight / Duotone)</option>
                  <option value="hugeicons">Hugeicons (Rounded Modern SaaS)</option>
                  <option value="tabler">Tabler (Dense Technical 24px)</option>
                  <option value="remixicon">Remix Icon (Bold Line &amp; Fill)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="sh-preview-select">Shadcn Component Context</label>
                <select id="sh-preview-select" class="control-select">
                  <option value="buttons-input" selected>Buttons, Search Input &amp; Badges</option>
                  <option value="sidebar-nav">Sidebar Navigation &amp; Active States</option>
                  <option value="alert-command">Command Menu &amp; Alert Banner</option>
                </select>
              </div>

              <div class="control-row">
                <label for="sh-stroke-slider">Optical Stroke (<span id="sh-stroke-val">2.0px</span>)</label>
                <input type="range" id="sh-stroke-slider" class="control-input" min="1.25" max="2.50" step="0.25" value="2.00">
              </div>

              <div class="control-row">
                <label for="sh-size-select">Tailwind Icon Size Token</label>
                <select id="sh-size-select" class="control-select">
                  <option value="14">size-3.5 (14px compact)</option>
                  <option value="16" selected>size-4 (16px shadcn default)</option>
                  <option value="20">size-5 (20px prominent)</option>
                  <option value="24">size-6 (24px hero card)</option>
                </select>
              </div>

              <div class="control-row">
                <label for="sh-accent-select">Primary Accent Token</label>
                <select id="sh-accent-select" class="control-select">
                  <option value="#C1DD2D" selected>Electric Lime (#C1DD2D)</option>
                  <option value="#38BDF8">Sky Cyan (#38BDF8)</option>
                  <option value="#F2F2F2">Monochrome Zinc (#F2F2F2)</option>
                </select>
              </div>
            </div>

            <div class="preview-stage-container">
              <svg id="sh-live-canvas" class="shadcn-svg-canvas" viewBox="0 0 760 440" width="760" height="440" xmlns="http://www.w3.org/2000/svg" role="graphics-document" aria-label="Interactive Shadcn UI Icon Library Preview Stage">
              </svg>
            </div>

            <div class="stats-readout-box" aria-live="polite">
              <div class="stat-item">
                <span class="stat-label">Icon Library</span>
                <span class="stat-val highlight" id="sh-stat-lib">lucide-react</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Indexed Icons</span>
                <span class="stat-val" id="sh-stat-count">1,979</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">License</span>
                <span class="stat-val" id="sh-stat-license">ISC</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Optical Weight</span>
                <span class="stat-val" id="sh-stat-weight">2.00px / 16px</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">Focused Slot</span>
                <span class="stat-val highlight" id="sh-stat-slot">Primary Action</span>
              </div>
            </div>

            <div class="action-btn-row">
              <button type="button" class="secondary-btn" id="sh-copy-config-btn">Copy components.json Snippet</button>
              <button type="button" class="copy-btn" id="sh-copy-code-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                  <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                <span>Copy Standalone SVG</span>
              </button>
            </div>
          </div>
        </section>

        <section id="section-radix-migration">
          <h2>8. Migrating Legacy Radix Icons &amp; Mixing Icon Sets Safely</h2>
          <p><strong>Short Answer:</strong> Never mix legacy 15×15 Radix Icons with 24×24 Lucide or Tabler icons inside the same toolbar because scaling a 15×15 viewBox up to 16px or 20px creates noticeably thicker strokes and mismatched visual balance. Standardize on a single 24×24 base grid across UI controls, and reserve distinct packs strictly for brand logos like Simple Icons.</p>

          <p>Many older shadcn/ui codebases initialized during 2023–2024 used the <code>new-york</code> style coupled with <code>@radix-ui/react-icons</code>. Radix Icons were authored specifically for a <code>15×15</code> pixel grid with crisp 1px lines. When rendered at <code>15px</code> or <code>16px</code>, they look razor-sharp—yet the moment you enlarge a Radix icon to <code>size-5</code> (20px) or <code>size-6</code> (24px) alongside a <code>24×24</code> Lucide icon, the Radix glyph looks 60% heavier than its neighbor.</p>

          <h3>Optical Weight Normalization &amp; Brand Logo Exceptions</h3>
          <p>The only valid exception to single-library governance is pairing a UI icon set (such as Lucide or Phosphor) with <strong>Simple Icons</strong> (3,714 CC0 brand logos) for OAuth buttons like GitHub, Google, and Stripe. When placing a solid filled Simple Icon logo beside a 2px-stroke Lucide chevron inside a login button, reduce the filled brand logo slightly (<code>size-3.5</code> vs <code>size-4</code>) or tone down its opacity to <code>90%</code> so the solid fill does not overpower the delicate outline chevron.</p>

          <h3>Building a Zero-Lock-In AppIcon Adapter &amp; Fixing Text Alignment</h3>
          <p>Large product teams migrating gradually from legacy Radix Icons or Font Awesome often introduce a thin <code>&lt;AppIcon name="..." /&gt;</code> adapter inside <code>components/ui/app-icon.tsx</code>. Mapping semantic names like <code>"deploy"</code>, <code>"settings"</code>, and <code>"alert"</code> in one central dictionary lets you swap underlying icon libraries, enforce uniform default <code>strokeWidth={1.75}</code>, and fix baseline alignment next to Inter or Geist typography across every button simultaneously. Remember that flex containers with <code>items-center</code> align icon bounding boxes cleanly against single-line labels, whereas multi-line checklist items should anchor icons to the first line using <code>mt-0.5 shrink-0</code>—covered thoroughly in our <a href="/articles/how-to-align-svg-icons-with-text-css-guide/">CSS SVG icon alignment guide</a>.</p>

          <h3>Converting Legacy Radix 15×15 ViewBoxes Safely During Incremental Migration</h3>
          <p>When a large monorepo cannot swap 300 legacy Radix icons in a single pull request, avoid rendering <code>15×15</code> and <code>24×24</code> icons side by side inside the same button group or dropdown menu. Migrate whole feature surfaces top-to-bottom—starting with shared <code>components/ui/</code> primitives like <code>Select</code>, <code>Dialog</code>, <code>Checkbox</code>, and <code>Calendar</code>—so every user-facing route preserves unified optical weight during the transition window.</p>
        </section>

        <section id="section-accessibility">
          <h2>9. WCAG 2.2 AA Accessibility: Decorative vs. Icon-Only Shadcn Buttons</h2>
          <p><strong>Short Answer:</strong> Every icon paired next to visible button text must carry <code>aria-hidden="true"</code> so screen readers do not announce redundant glyph descriptions, while icon-only buttons (<code>size="icon"</code>) must provide an explicit <code>aria-label</code> or <code>&lt;span className="sr-only"&gt;</code> alongside at least 3:1 contrast and 24×24px minimum target size.</p>

          <p>Even the cleanest shadcn/ui component fails accessibility audits if icons lack semantic discipline. Follow these four WCAG 2.2 AA rules across every component in your design system:</p>

          <ul>
            <li><strong>Hide Decorative Icons with Visible Labels:</strong> Inside <code>&lt;Button&gt;&lt;Trash2 aria-hidden="true" /&gt; Delete Account&lt;/Button&gt;</code>, the word "Delete Account" already conveys the action. Marking the SVG <code>aria-hidden="true"</code> stops NVDA and VoiceOver from reading confusing artifacts.</li>
            <li><strong>Name Icon-Only Controls Explicitly:</strong> Inside <code>&lt;Button variant="ghost" size="icon" aria-label="Open settings"&gt;&lt;Settings aria-hidden="true" /&gt;&lt;/Button&gt;</code>, either <code>aria-label</code> or an inner <code>&lt;span className="sr-only"&gt;Open settings&lt;/span&gt;</code> is mandatory—otherwise screen readers announce merely "Button" with zero context.</li>
            <li><strong>Enforce WCAG SC 1.4.11 (3:1 Non-Text Contrast):</strong> Meaningful UI icons (search magnifiers, warning badges, active navigation indicators) must achieve at least a <code>3:1</code> contrast ratio against their adjacent button or card surface in both light and dark themes.</li>
            <li><strong>Respect WCAG 2.2 SC 2.5.8 Target Size (Minimum 24×24px):</strong> Never render standalone icon-only close buttons or table action icons smaller than <code>24×24</code> CSS pixels without surrounding spacing; shadcn's <code>size="icon"</code> (<code>size-9</code> = 36px) and <code>size="icon-sm"</code> (<code>size-8</code> = 32px) comfortably exceed WCAG 2.2 AA requirements.</li>
            <li><strong>Verify Focus Rings &amp; Tooltip Triggers on Icon Buttons:</strong> Never wrap a disabled icon-only <code>Button</code> directly inside a Radix <code>TooltipTrigger</code> expecting keyboard hover announcements—disabled buttons drop out of tab order. Keep buttons focusable with <code>aria-disabled="true"</code> when explanatory tooltips must remain reachable via keyboard Tab navigation.</li>
          </ul>

          <h3>Automated CI Verification with Axe-Core &amp; Playwright</h3>
          <p>To prevent accessibility regressions whenever new shadcn components are added, wire <code>@axe-core/playwright</code> into your pull-request CI workflow and assert zero <code>button-name</code> or <code>svg-img-alt</code> violations across both light and dark themes. Automated contrast checks catch subtle hover-state regressions immediately before broken icon buttons ship to production.</p>

          <div class="takeaway-box">
            <h3>Shadcn UI Icon System Checklist</h3>
            <ul>
              <li>Declare your chosen <code>iconLibrary</code> inside <code>components.json</code> and migrate cleanly via <code>npx shadcn@latest migrate icons</code>.</li>
              <li>Use Tailwind v4's <code>[&_svg:not([class*='size-'])]:size-4</code> pattern so custom icon sizes never fight CVA defaults.</li>
              <li>Build custom SVG wrappers around <code>React.ComponentProps&lt;'svg'&gt;</code> with <code>stroke="currentColor"</code> and <code>aria-hidden="true"</code>.</li>
              <li>Add <code>optimizePackageImports</code> in <code>next.config.ts</code> or switch high-density table icons to a cached SVG <code>&lt;use&gt;</code> sprite.</li>
              <li>Search and preview all 28 open-source icon sets side by side on <a href="/">IconStash</a> before committing to a library.</li>
            </ul>
          </div>
        </section>

        <section id="section-faq" class="faq-section">
          <h2>10. Frequently Asked Questions</h2>

          <div class="faq-item">
            <div class="faq-question">
              <span>What is the default icon library used by shadcn/ui in 2026?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Lucide React (<code>lucide-react</code>) is the default icon library for shadcn/ui across New York and Default styles, providing 1,979 uniform 2px-stroke ISC-licensed SVG icons on a 24×24 grid. Legacy projects initialized with Radix UI style presets originally used <code>@radix-ui/react-icons</code> on a 15×15 grid.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How do you switch icon libraries in an existing shadcn/ui codebase?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Run <code>npx shadcn@latest migrate icons</code> inside your project root (or pass <code>--from lucide --to phosphor --yes</code>). The shadcn CLI runs an AST codemod across your <code>components/ui</code> directory, installs the target package, rewrites icon imports and JSX components, and updates <code>iconLibrary</code> inside <code>components.json</code>.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>Which icon library is the best alternative to Lucide for shadcn/ui?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Choose Phosphor Icons (9,198 icons, MIT) when your design system needs six distinct visual weights including Duotone and Fill active states; choose Tabler Icons (6,324 icons, MIT) for exhaustive enterprise coverage on a crisp 24×24 stroke grid; or choose Hugeicons (5,115 free icons, MIT) for modern rounded SaaS aesthetics.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How does shadcn/ui automatically size SVG icons inside buttons and inputs?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Modern Tailwind v4 shadcn/ui components include the arbitrary child selector <code>[&_svg:not([class*='size-'])]:size-4</code> alongside <code>[&_svg]:pointer-events-none</code> and <code>[&_svg]:shrink-0</code>. Any SVG without an explicit <code>size-*</code> utility automatically inherits 16×16px sizing while remaining overridable with <code>className="size-5"</code>.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How do you use custom inline SVG icons inside shadcn/ui components?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Wrap your clean SVG paths in a React component accepting <code>React.ComponentProps&lt;'svg'&gt;</code>, apply <code>stroke="currentColor"</code> or <code>fill="currentColor"</code> instead of hardcoded hex codes, forward <code>{...props}</code>, and drop it directly inside Button, DropdownMenuItem, or Alert components so Tailwind child selectors size and color it automatically.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>Why do Lucide or Phosphor icons slow down Next.js dev server cold starts and how do you fix it?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Importing named icons from top-level barrel exports like <code>lucide-react</code> or <code>@phosphor-icons/react</code> can cause development bundlers to parse thousands of re-exported modules. Enable <code>experimental.optimizePackageImports</code> in <code>next.config.ts</code> (or import via an SVG sprite sheet) to keep HMR and cold starts instant.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question">
              <span>How do you make icon-only shadcn/ui buttons accessible under WCAG 2.2 AA?</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>
            <div class="faq-answer">
              Always add <code>aria-label</code> or a visually hidden <code>&lt;span class="sr-only"&gt;Action Name&lt;/span&gt;</code> inside icon-only <code>Button size="icon"</code> controls while setting <code>aria-hidden="true"</code> on the decorative SVG itself. Maintain at least a 3:1 contrast ratio for non-text UI graphics and avoid shrinking clickable buttons below 24×24px.
            </div>
          </div>
        </section>
      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <a href="#section-shadcn-architecture">1. components.json &amp; Tailwind v4</a>
            <a href="#section-library-benchmark">2. Lucide vs. Phosphor vs. Hugeicons</a>
            <a href="#section-cli-migration">3. npx shadcn migrate icons</a>
            <a href="#section-architecture-pipeline">4. Figure 2: Resolution Pipeline</a>
            <a href="#section-custom-svg">5. Custom SVGs &amp; currentColor</a>
            <a href="#section-treeshaking-sprites">6. Tree-Shaking &amp; SVG Sprites</a>
            <a href="#section-interactive-studio">7. Interactive Shadcn Icon Studio</a>
            <a href="#section-radix-migration">8. Migrating Radix &amp; Mixing Sets</a>
            <a href="#section-accessibility">9. WCAG 2.2 AA Icon Accessibility</a>
            <a href="#section-faq">10. Frequently Asked Questions</a>
          </nav>
        </div>

        <div class="cta-sidebar-box">
          <div class="cta-title">Compare 28 Icon Libraries Live</div>
          <p>Search Lucide, Phosphor, Tabler, Hugeicons, Heroicons, and 23 more open-source sets side by side on IconStash.</p>
          <a href="/" class="header-cta" style="display:inline-block; text-align:center;">Search Icons Free</a>
        </div>
      </aside>
    </div>
  </main>

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
      try {
        const savedTheme = localStorage.getItem('iconstash-theme');
        if (savedTheme === 'light' || savedTheme === 'dark') {
          document.documentElement.setAttribute('data-theme', savedTheme);
        }
      } catch (_) {}

      const themeBtn = document.getElementById('theme-toggle');
      if (themeBtn) {
        themeBtn.addEventListener('click', () => {
          const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
          const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
          document.documentElement.setAttribute('data-theme', newTheme);
          try { localStorage.setItem('iconstash-theme', newTheme); } catch (_) {}
        });
      }

      const libSelect = document.getElementById('sh-library-select');
      const previewSelect = document.getElementById('sh-preview-select');
      const strokeSlider = document.getElementById('sh-stroke-slider');
      const strokeVal = document.getElementById('sh-stroke-val');
      const sizeSelect = document.getElementById('sh-size-select');
      const accentSelect = document.getElementById('sh-accent-select');
      const liveSvg = document.getElementById('sh-live-canvas');
      const copyBtn = document.getElementById('sh-copy-code-btn');
      const copyConfigBtn = document.getElementById('sh-copy-config-btn');

      const statLib = document.getElementById('sh-stat-lib');
      const statCount = document.getElementById('sh-stat-count');
      const statLicense = document.getElementById('sh-stat-license');
      const statWeight = document.getElementById('sh-stat-weight');
      const statSlot = document.getElementById('sh-stat-slot');

      const LIBS = {
        lucide: { pkg: 'lucide-react', count: '1,979', license: 'ISC', radius: 6, duotone: false, cap: 'round', join: 'round' },
        phosphor: { pkg: '@phosphor-icons/react', count: '9,198', license: 'MIT', radius: 8, duotone: true, cap: 'round', join: 'round' },
        hugeicons: { pkg: '@hugeicons/react', count: '5,115', license: 'MIT', radius: 10, duotone: true, cap: 'round', join: 'round' },
        tabler: { pkg: '@tabler/icons-react', count: '6,324', license: 'MIT', radius: 4, duotone: false, cap: 'round', join: 'round' },
        remixicon: { pkg: '@remixicon/react', count: '3,244', license: 'Apache 2.0', radius: 4, duotone: true, cap: 'square', join: 'miter' }
      };

      const SLOT_META_BY_VIEW = {
        'buttons-input': [
          { name: 'Primary Action', x: 72, y: 130, w: 198, h: 46 },
          { name: 'Secondary Filter', x: 290, y: 130, w: 198, h: 46 },
          { name: 'Search Input', x: 72, y: 208, w: 614, h: 48 },
          { name: 'Status Notification', x: 72, y: 286, w: 614, h: 80 }
        ],
        'sidebar-nav': [
          { name: 'Icon Registry', x: 72, y: 114, w: 280, h: 46 },
          { name: 'Concept Explorer', x: 72, y: 172, w: 280, h: 46 },
          { name: 'Theme Tokens', x: 72, y: 230, w: 280, h: 46 },
          { name: 'Audit Alerts', x: 72, y: 288, w: 280, h: 46 }
        ],
        'alert-command': [
          { name: 'Command Palette', x: 72, y: 108, w: 614, h: 180 },
          { name: 'Alert Banner', x: 72, y: 306, w: 614, h: 66 }
        ]
      };
      let activeSlot = 0;

      function getCurrentSlots() {
        const viewKey = previewSelect.value || 'buttons-input';
        return SLOT_META_BY_VIEW[viewKey] || SLOT_META_BY_VIEW['buttons-input'];
      }

      function syncSlotSelection(moveFocus = false) {
        const slots = getCurrentSlots();
        if (activeSlot >= slots.length || activeSlot < 0) activeSlot = 0;
        const meta = slots[activeSlot];
        const libKey = libSelect.value || 'lucide';
        const lib = LIBS[libKey] || LIBS.lucide;
        const accent = accentSelect.value || '#C1DD2D';
        const ringEl = liveSvg.querySelector ? liveSvg.querySelector('#sh-focus-ring') : null;
        if (ringEl && meta) {
          ringEl.setAttribute('x', String(meta.x - 3));
          ringEl.setAttribute('y', String(meta.y - 3));
          ringEl.setAttribute('width', String(meta.w + 6));
          ringEl.setAttribute('height', String(meta.h + 6));
          ringEl.setAttribute('rx', String(lib.radius + 2));
          ringEl.setAttribute('stroke', accent);
          ringEl.setAttribute('opacity', '1');
        }
        statSlot.textContent = meta ? meta.name : 'Primary Action';
        if (moveFocus && liveSvg.querySelector) {
          const targetSlot = liveSvg.querySelector(`g[data-slot-idx="${activeSlot}"]`);
          if (targetSlot && targetSlot.focus) {
            try { targetSlot.focus(); } catch (_) {}
          }
        }
      }

      function iconSvg(kind, x, y, pxSize, strokeColor, sw, libMeta) {
        const scale = pxSize / 24;
        const fillTint = libMeta.duotone ? strokeColor : 'none';
        const fillOp = libMeta.duotone ? '0.2' : '0';
        const lc = libMeta.cap;
        const lj = libMeta.join;
        let inner = '';

        if (kind === 'bolt') {
          inner = `<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" fill="${fillTint}" fill-opacity="${fillOp}" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" stroke-linejoin="${lj}" />`;
        } else if (kind === 'search') {
          inner = `<circle cx="11" cy="11" r="8" fill="${fillTint}" fill-opacity="${fillOp}" stroke="${strokeColor}" stroke-width="${sw}" /><line x1="21" y1="21" x2="16.65" y2="16.65" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" />`;
        } else if (kind === 'sliders') {
          inner = `<line x1="4" y1="21" x2="4" y2="14" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" /><line x1="4" y1="10" x2="4" y2="3" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" /><line x1="12" y1="21" x2="12" y2="12" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" /><line x1="12" y1="8" x2="12" y2="3" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" /><line x1="20" y1="21" x2="20" y2="16" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" /><line x1="20" y1="12" x2="20" y2="3" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" /><circle cx="4" cy="12" r="2" fill="${strokeColor}" /><circle cx="12" cy="10" r="2" fill="${strokeColor}" /><circle cx="20" cy="14" r="2" fill="${strokeColor}" />`;
        } else if (kind === 'bell') {
          inner = `<path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" fill="${fillTint}" fill-opacity="${fillOp}" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" stroke-linejoin="${lj}" /><path d="M13.73 21a2 2 0 0 1-3.46 0" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" />`;
        } else if (kind === 'layers') {
          inner = `<polygon points="12 2 2 7 12 12 22 7 12 2" fill="${fillTint}" fill-opacity="${fillOp}" stroke="${strokeColor}" stroke-width="${sw}" stroke-linejoin="${lj}" /><polyline points="2 17 12 22 22 17" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" stroke-linejoin="${lj}" /><polyline points="2 12 12 17 22 12" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" stroke-linejoin="${lj}" />`;
        } else if (kind === 'shield') {
          inner = `<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" fill="${fillTint}" fill-opacity="${fillOp}" stroke="${strokeColor}" stroke-width="${sw}" stroke-linejoin="${lj}" />`;
        } else if (kind === 'terminal') {
          inner = `<polyline points="4 17 10 11 4 5" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" stroke-linejoin="${lj}" /><line x1="12" y1="19" x2="20" y2="19" stroke="${strokeColor}" stroke-width="${sw}" stroke-linecap="${lc}" />`;
        }
        return `<g transform="translate(${x.toFixed(1)}, ${y.toFixed(1)}) scale(${scale.toFixed(3)})">${inner}</g>`;
      }

      function renderPreview(showFocusRing = true) {
        const libKey = libSelect.value || 'lucide';
        const lib = LIBS[libKey] || LIBS.lucide;
        const viewKey = previewSelect.value || 'buttons-input';
        const sw = parseFloat(strokeSlider.value) || 2.0;
        const pxSize = parseInt(sizeSelect.value, 10) || 16;
        const accent = accentSelect.value || '#C1DD2D';
        const r = lib.radius;
        const slots = getCurrentSlots();
        if (activeSlot >= slots.length || activeSlot < 0) activeSlot = 0;

        strokeVal.textContent = sw.toFixed(2) + 'px';

        let bodyMarkup = '';
        const actMeta = slots[activeSlot] || slots[0];
        const focusRingMarkup = (showFocusRing && actMeta)
          ? `<rect id="sh-focus-ring" x="${actMeta.x - 3}" y="${actMeta.y - 3}" width="${actMeta.w + 6}" height="${actMeta.h + 6}" rx="${r + 2}" fill="none" stroke="${accent}" stroke-width="1.5" stroke-dasharray="4,3" pointer-events="none" />`
          : '';

        if (viewKey === 'buttons-input') {
          bodyMarkup = `
            <rect x="44" y="42" width="672" height="356" rx="12" fill="#121212" stroke="#262626" />
            <text x="72" y="78" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="16" font-weight="700">Shadcn UI Component Primitives — ${lib.pkg}</text>
            <text x="72" y="100" fill="#888888" font-family="'JetBrains Mono', monospace" font-size="12">[&amp;_svg:not([class*='size-'])]:size-${pxSize === 16 ? '4' : pxSize === 20 ? '5' : pxSize === 24 ? '6' : '3.5'} | strokeWidth=${sw.toFixed(2)}</text>

            <g data-slot-idx="0" tabindex="0" role="button" aria-label="Primary Action Button" style="cursor:pointer; outline:none;">
              <rect x="72" y="130" width="198" height="46" rx="${r}" fill="${accent}" />
              ${iconSvg('bolt', 92, 153 - pxSize / 2, pxSize, '#0A0A0A', sw, lib)}
              <text x="${92 + pxSize + 10}" y="158" fill="#0A0A0A" font-family="'Inter', sans-serif" font-size="14" font-weight="700">Deploy Build</text>
            </g>

            <g data-slot-idx="1" tabindex="0" role="button" aria-label="Secondary Filter Button" style="cursor:pointer; outline:none;">
              <rect x="290" y="130" width="198" height="46" rx="${r}" fill="#1A1A1A" stroke="#333333" />
              ${iconSvg('sliders', 310, 153 - pxSize / 2, pxSize, '#F2F2F2', sw, lib)}
              <text x="${310 + pxSize + 10}" y="158" fill="#F2F2F2" font-family="'Inter', sans-serif" font-size="14" font-weight="600">Filter Tokens</text>
            </g>

            <rect x="508" y="130" width="178" height="46" rx="${r}" fill="rgba(193,221,45,0.08)" stroke="${accent}" stroke-opacity="0.35" />
            ${iconSvg('shield', 524, 153 - pxSize / 2, pxSize, accent, sw, lib)}
            <text x="${524 + pxSize + 10}" y="158" fill="${accent}" font-family="'JetBrains Mono', monospace" font-size="12.5" font-weight="700">WCAG 2.2 AA</text>

            <g data-slot-idx="2" tabindex="0" role="button" aria-label="Search Input Component" style="cursor:pointer; outline:none;">
              <rect x="72" y="208" width="614" height="48" rx="${r}" fill="#0D0D0D" stroke="#333333" />
              ${iconSvg('search', 90, 232 - pxSize / 2, pxSize, '#888888', sw, lib)}
              <text x="${90 + pxSize + 12}" y="237" fill="#777777" font-family="'Inter', sans-serif" font-size="14">Search 134,701 open-source SVG icons across 28 libraries...</text>
              <rect x="618" y="219" width="52" height="26" rx="4" fill="#1C1C1C" stroke="#2E2E2E" />
              <text x="644" y="236" fill="#999999" font-family="'JetBrains Mono', monospace" font-size="11.5" text-anchor="middle">Ctrl+K</text>
            </g>

            <g data-slot-idx="3" tabindex="0" role="button" aria-label="Status Notification Card" style="cursor:pointer; outline:none;">
              <rect x="72" y="286" width="614" height="80" rx="${r}" fill="#161616" stroke="#2A2A2A" />
              ${iconSvg('bell', 94, 326 - pxSize / 2, pxSize, accent, sw, lib)}
              <text x="${94 + pxSize + 14}" y="319" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14.5" font-weight="700">Registry Migration Complete</text>
              <text x="${94 + pxSize + 14}" y="343" fill="#999999" font-family="'JetBrains Mono', monospace" font-size="12">npx shadcn@latest migrate icons --to ${libKey} --yes</text>
            </g>
          `;
        } else if (viewKey === 'sidebar-nav') {
          const items = [
            { icon: 'layers', label: 'Icon Registry', active: true },
            { icon: 'search', label: 'Concept Explorer', active: false },
            { icon: 'sliders', label: 'Theme Tokens', active: false },
            { icon: 'bell', label: 'Audit Alerts', active: false }
          ];
          let navItems = '';
          items.forEach((it, i) => {
            const iy = 114 + i * 58;
            navItems += `
              <g data-slot-idx="${i}" tabindex="0" role="button" aria-label="${it.label}" style="cursor:pointer; outline:none;">
                <rect x="72" y="${iy}" width="280" height="46" rx="${r}" fill="${it.active ? 'rgba(193,221,45,0.12)' : '#161616'}" stroke="${it.active ? accent : '#242424'}" />
                ${iconSvg(it.icon, 90, iy + 23 - pxSize / 2, pxSize, it.active ? accent : '#A3A3A3', sw, lib)}
                <text x="${90 + pxSize + 12}" y="${iy + 28}" fill="${it.active ? '#FFFFFF' : '#BBBBBB'}" font-family="'Inter', sans-serif" font-size="14" font-weight="${it.active ? '700' : '500'}">${it.label}</text>
              </g>
            `;
          });
          bodyMarkup = `
            <rect x="44" y="42" width="672" height="356" rx="12" fill="#121212" stroke="#262626" />
            <text x="72" y="84" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="16" font-weight="700">Sidebar Primitive — Active Weight Contrast</text>
            ${navItems}
            <rect x="380" y="114" width="306" height="222" rx="${r}" fill="#0D0D0D" stroke="#262626" />
            ${iconSvg('terminal', 404, 146, Math.max(20, pxSize), accent, sw, lib)}
            <text x="440" y="162" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700">components.json</text>
            <text x="404" y="202" fill="#999999" font-family="'JetBrains Mono', monospace" font-size="12">"iconLibrary": "${libKey}"</text>
            <text x="404" y="228" fill="#888888" font-family="'JetBrains Mono', monospace" font-size="12">"package": "${lib.pkg}"</text>
            <text x="404" y="254" fill="#888888" font-family="'JetBrains Mono', monospace" font-size="12">"duotoneCapable": ${lib.duotone}</text>
            <text x="404" y="280" fill="${accent}" font-family="'JetBrains Mono', monospace" font-size="12">"license": "${lib.license}"</text>
          `;
        } else {
          bodyMarkup = `
            <rect x="44" y="42" width="672" height="356" rx="12" fill="#121212" stroke="#262626" />
            <text x="72" y="82" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="16" font-weight="700">Command Palette &amp; Alert — ${lib.pkg}</text>
            <g data-slot-idx="0" tabindex="0" role="button" aria-label="Command Palette Group" style="cursor:pointer; outline:none;">
              <rect x="72" y="108" width="614" height="180" rx="${r}" fill="#0D0D0D" stroke="#303030" />
              ${iconSvg('search', 94, 134 - pxSize / 2, pxSize, '#888888', sw, lib)}
              <text x="${94 + pxSize + 12}" y="139" fill="#AAAAAA" font-family="'Inter', sans-serif" font-size="14">Type a command or search icons...</text>
              <line x1="72" y1="162" x2="686" y2="162" stroke="#222222" />
              ${iconSvg('bolt', 94, 194 - pxSize / 2, pxSize, accent, sw, lib)}
              <text x="${94 + pxSize + 12}" y="199" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13.5" font-weight="600">Run Icon Migration Codemod</text>
              ${iconSvg('layers', 94, 242 - pxSize / 2, pxSize, '#A3A3A3', sw, lib)}
              <text x="${94 + pxSize + 12}" y="247" fill="#CCCCCC" font-family="'Inter', sans-serif" font-size="13.5">Compare 28 Open-Source Icon Libraries</text>
            </g>
            <g data-slot-idx="1" tabindex="0" role="button" aria-label="Alert Banner" style="cursor:pointer; outline:none;">
              <rect x="72" y="306" width="614" height="66" rx="${r}" fill="rgba(193,221,45,0.06)" stroke="${accent}" stroke-opacity="0.4" />
              ${iconSvg('shield', 94, 339 - pxSize / 2, pxSize, accent, sw, lib)}
              <text x="${94 + pxSize + 12}" y="334" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13.5" font-weight="700">Tree-Shaking Verified</text>
              <text x="${94 + pxSize + 12}" y="355" fill="#AAAAAA" font-family="'JetBrains Mono', monospace" font-size="11.5">optimizePackageImports enabled for ${lib.pkg}</text>
            </g>
          `;
        }

        liveSvg.innerHTML = `<rect width="760" height="440" fill="#0D0D0D" rx="8" />${bodyMarkup}${focusRingMarkup}`;

        statLib.textContent = lib.pkg;
        statCount.textContent = lib.count;
        statLicense.textContent = lib.license;
        statWeight.textContent = `${sw.toFixed(2)}px / ${pxSize}px`;
        statSlot.textContent = actMeta ? actMeta.name : 'Primary Action';
      }

      liveSvg.addEventListener('click', e => {
        const slotEl = e.target && e.target.closest ? e.target.closest('[data-slot-idx]') : null;
        if (slotEl) {
          activeSlot = parseInt(slotEl.getAttribute('data-slot-idx'), 10) || 0;
          syncSlotSelection(true);
        }
      });

      liveSvg.addEventListener('focusin', e => {
        const slotEl = e.target && e.target.closest ? e.target.closest('[data-slot-idx]') : null;
        if (slotEl) {
          activeSlot = parseInt(slotEl.getAttribute('data-slot-idx'), 10) || 0;
          syncSlotSelection(false);
        }
      });

      liveSvg.addEventListener('keydown', e => {
        const slots = getCurrentSlots();
        const count = slots.length;
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
          e.preventDefault();
          activeSlot = (activeSlot + 1) % count;
          syncSlotSelection(true);
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
          e.preventDefault();
          activeSlot = (activeSlot + count - 1) % count;
          syncSlotSelection(true);
        } else if (e.key === 'Home') {
          e.preventDefault();
          activeSlot = 0;
          syncSlotSelection(true);
        } else if (e.key === 'End') {
          e.preventDefault();
          activeSlot = count - 1;
          syncSlotSelection(true);
        }
      });

      libSelect.addEventListener('change', () => renderPreview(true));
      previewSelect.addEventListener('change', () => { activeSlot = 0; renderPreview(true); });
      strokeSlider.addEventListener('input', () => renderPreview(true));
      sizeSelect.addEventListener('change', () => renderPreview(true));
      accentSelect.addEventListener('change', () => renderPreview(true));

      function copyText(text, btn, defaultHtml) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(() => {
            btn.textContent = 'Copied to Clipboard!';
            setTimeout(() => { btn.innerHTML = defaultHtml; }, 2000);
          }).catch(() => fallbackCopy(text, btn, defaultHtml));
        } else {
          fallbackCopy(text, btn, defaultHtml);
        }
      }

      function fallbackCopy(text, btn, defaultHtml) {
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try {
          document.execCommand('copy');
          btn.textContent = 'Copied to Clipboard!';
          setTimeout(() => { btn.innerHTML = defaultHtml; }, 2000);
        } catch (e) {
          alert('Copy failed: ' + e.message);
        }
        document.body.removeChild(ta);
      }

      copyBtn.addEventListener('click', () => {
        renderPreview(false);
        let svgSource = liveSvg.outerHTML || '';
        if (!svgSource.includes('xmlns="http://www.w3.org/2000/svg"')) {
          svgSource = svgSource.replace(/<svg\b/, '<svg xmlns="http://www.w3.org/2000/svg"');
        }
        renderPreview(true);
        copyText(svgSource, copyBtn, '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> <span>Copy Standalone SVG</span>');
      });

      copyConfigBtn.addEventListener('click', () => {
        const libKey = libSelect.value || 'lucide';
        const cfg = JSON.stringify({
          "$schema": "https://ui.shadcn.com/schema.json",
          "style": "new-york",
          "rsc": true,
          "tsx": true,
          "iconLibrary": libKey
        }, null, 2);
        copyText(cfg, copyConfigBtn, 'Copy components.json Snippet');
      });

      renderPreview(true);
    })();
  </script>
</body>
</html>
"""

out_dir = os.path.join("articles", "shadcn-ui-icons-complete-guide-2026")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Generated:", out_path)
