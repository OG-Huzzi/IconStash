import os
import re

slug = "svg-box-plots-and-whisker-charts-statistical-distribution-guide"
target_dir = os.path.join(r"D:\Project IconStash\IconStash\articles", slug)
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

# Constructing Article 1: Box Plots & Whisker Charts
html_content = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mastering SVG Box Plots &amp; Whisker Charts: Five-Number Summaries, Quartile Calculus &amp; Distribution Visualizations (2026) | IconStash</title>
  <meta name="description" content="Master SVG box plots: Tukey five-number summaries, IQR outlier filtering, notched confidence intervals, and jittered raw data points in vector graphics.">
  <meta name="keywords" content="svg box plot, svg box and whisker chart, statistical data visualization svg, five number summary svg, quartile calculation box plot, outlier detection svg, notched box plot d3 react, interactive box plot javascript">
  <meta property="og:title" content="Mastering SVG Box Plots &amp; Whisker Charts: Five-Number Summaries, Quartile Calculus &amp; Distribution Visualizations (2026)">
  <meta property="og:description" content="Master SVG box plots: Tukey five-number summaries, IQR outlier filtering, notched confidence intervals, and jittered raw data points in vector graphics.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-11-20T00:00:00Z">
  <meta property="article:modified_time" content="2026-11-20T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="Statistical Data Visualization">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="Box Plots">
  <meta property="article:tag" content="Data Visualization">
  <meta property="article:tag" content="Statistics">
  <meta property="article:tag" content="Mathematics">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mastering SVG Box Plots &amp; Whisker Charts: Five-Number Summaries, Quartile Calculus &amp; Distribution Visualizations (2026)">
  <meta name="twitter:description" content="Master SVG box plots: Tukey five-number summaries, IQR outlier filtering, notched confidence intervals, and jittered raw data points in vector graphics.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide/">
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
      "headline": "Mastering SVG Box Plots & Whisker Charts: Five-Number Summaries, Quartile Calculus & Distribution Visualizations (2026)",
      "description": "Master SVG box plots: Tukey five-number summaries, IQR outlier filtering, notched confidence intervals, and jittered raw data points in vector graphics.",
      "image": "https://iconstash.io/assets/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide.jpg",
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
      "mainEntityOfPage": "https://iconstash.io/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide/",
      "inLanguage": "en-US",
      "wordCount": 4650,
      "articleSection": "Statistical Data Visualization",
      "keywords": [
        "svg box plot",
        "svg box and whisker chart",
        "statistical data visualization svg",
        "five number summary svg",
        "quartile calculation box plot",
        "outlier detection svg",
        "notched box plot d3 react",
        "interactive box plot javascript"
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
          "name": "SVG Box Plots & Whisker Charts Guide",
          "item": "https://iconstash.io/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why is the median preferred over the arithmetic mean in box and whisker plots?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The median represents the non-parametric fiftieth percentile of an ordered dataset, dividing observations into two equal halves. Unlike the arithmetic mean, the median is highly resistant to extreme skewness, heavy tails, and anomalous outliers. In real-world engineering telemetry such as API response latencies, a small handful of catastrophic timeout events can drag the arithmetic mean upward by hundreds of milliseconds, giving a false impression of degraded baseline performance. The median accurately conveys the typical user experience, while the surrounding interquartile range (IQR) and whisker bounds isolate anomalous outliers without corrupting central tendency indicators."
          }
        },
        {
          "@type": "Question",
          "name": "How does John Tukey's 1.5 IQR multiplier establish outlier fence thresholds?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "John Tukey established the 1.5 multiplier for interquartile range (IQR) outlier fences as a pragmatic heuristic grounded in Gaussian distribution theory. For a perfectly normal Gaussian distribution, the interquartile range spans approximately 1.349 standard deviations. Adding and subtracting 1.5 times the IQR from the third and first quartiles respectively yields boundary fences situated at approximately plus or minus 2.698 standard deviations from the distribution mean. In a standard normal distribution, this threshold captures approximately 99.3 percent of all valid observations, classifying only 0.7 percent of extreme observations as potential outliers, balancing sensitivity with noise resistance."
          }
        },
        {
          "@type": "Question",
          "name": "How do notched box plots evaluate statistical significance between comparison groups?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Notches in an SVG box plot visually represent an approximate 95 percent confidence interval for the true population median. The notch boundaries extend above and below the calculated median by a factor of 1.57 multiplied by the interquartile range divided by the square root of the sample size N. When comparing two or more adjacent box plots on identical scale axes, if the notches of two distributions do not overlap vertically, an observer can conclude with approximately 95 percent confidence that their true population medians are statistically significantly different, providing immediate hypothesis testing without formal p-value calculation."
          }
        },
        {
          "@type": "Question",
          "name": "How do you map continuous statistical values into an inverted SVG viewport canvas?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Because SVG canvas viewports place the origin point (0, 0) at the top-left corner with the positive Y-axis descending downward, direct mapping of higher statistical values would incorrectly place higher metrics toward the bottom of the screen. To establish an intuitive Cartesian coordinate system where higher values ascend upward, developers apply an inverted linear transformation: y_svg = (totalHeight - paddingBottom) - ((dataValue - domainMin) / (domainMax - domainMin)) * (totalHeight - paddingTop - paddingBottom). This subtraction from the baseline coordinate guarantees that the minimum domain boundary anchors at the bottom axis and maximum metrics rise toward the top margin."
          }
        },
        {
          "@type": "Question",
          "name": "What is the purpose of overlaying jittered strip chart points on an SVG box plot?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "While a box plot efficiently condenses hundreds or thousands of observations into five summary metrics, it inherently masks multi-modality, bi-modal distributions, gaps, and sample density clustering. Overlaying semi-transparent jittered dots—displacing each raw observation along the perpendicular categorical axis by a deterministic pseudo-random offset—reveals the true underlying distribution morphology. Observers can simultaneously inspect the macroscopic summary quartiles of the Tukey box alongside the microscopic density clustering and sample size weight of raw data points."
          }
        },
        {
          "@type": "Question",
          "name": "How do you guarantee WCAG 2.2 AA accessibility for complex interactive SVG box plots?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Full WCAG 2.2 AA accessibility requires marking the root SVG container with role='graphics-document' alongside aria-label and companion title and desc elements detailing dataset purpose and sample size. Individual box plot glyphs and outlier points must receive role='graphics-symbol', keyboard focusability via tabindex='0', and programmatic ARIA labels detailing median, Q1, Q3, whisker bounds, and outlier values. Furthermore, color encoding must never be the sole information channel; distinct fill patterns or stroke styles must differentiate categories, and all text labels must achieve at least 4.5:1 contrast against both light and dark backgrounds."
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
    .box-svg-canvas { width: 100%; max-width: 760px; height: auto; }

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
      <span class="current">SVG Box Plots &amp; Whisker Charts Guide</span>
    </nav>

    <header class="article-hero">
      <span class="tag">Statistical Data Visualization</span>
      <h1>Mastering SVG Box Plots &amp; Whisker Charts: Five-Number Summaries, Quartile Calculus &amp; Distribution Visualizations (2026)</h1>
      <div class="article-meta">
        <span>By <a href="/about/">Jouni Flemming</a></span>
        <span>&bull;</span>
        <span>Published November 20, 2026</span>
        <span>&bull;</span>
        <span>Reading Time: 24 min</span>
        <span>&bull;</span>
        <span>Zero-Dependency ES6 &amp; SVG</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">

        <div class="featured-summary">
          <p><strong>Executive Architectural Overview:</strong> Box and whisker plots represent one of the most mathematically rigorous and perceptually robust tools in exploratory data analysis. Unlike standard bar charts that reduce high-dimensional continuous distributions to a single fragile metric like the arithmetic mean, SVG box plots visualize the complete non-parametric five-number summary: sample minimum, lower quartile (Q1), median (Q2), upper quartile (Q3), and sample maximum, augmented with Tukey outlier fences.</p>
          <ul>
            <li><strong>Non-Parametric Robustness:</strong> Resilient to heavy distributional skewness and extreme tail outliers that fundamentally corrupt arithmetic means and standard deviation metrics.</li>
            <li><strong>Tukey Interquartile Range (IQR) Fences:</strong> Algorithmic separation of expected distribution variance from statistical outliers via 1.5 &times; IQR boundary thresholds.</li>
            <li><strong>Notched 95% Confidence Intervals:</strong> Visual hypothesis testing across categorical groups where non-overlapping notch waists confirm statistically significant median divergence.</li>
            <li><strong>Zero-Dependency Vector Precision:</strong> Direct generation of scalable, responsive SVG markup utilizing native rect, line, path, and circle primitives without bloated third-party charting libraries.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide.jpg" alt="Dark theme developer studio monitor displaying high precision glowing neon SVG box plots, quartile boundaries, whisker fences, and outlier annotations" width="1200" height="675" fetchpriority="high" decoding="async">
          <figcaption>Figure 1: High-precision SVG Box and Whisker distribution dashboard rendering statistical quartiles, Tukey fences, notched confidence waists, and jittered raw observation scatter overlays.</figcaption>
        </figure>

        <section id="section-foundations">
          <h2>1. Architectural Foundations of Statistical Box and Whisker Visualizations</h2>
          <p>In modern software engineering, web performance monitoring, machine learning telemetry, and financial analytics, developers routinely encounter large numerical datasets that defy simplistic summarization. When evaluating metrics such as API response latencies, server garbage collection pauses, microservice database transaction times, or neural network inference jitter, calculating the arithmetic mean is notoriously misleading. A single network timeout event of 15,000 milliseconds will dramatically inflate the mean of one thousand 20-millisecond queries, creating the false diagnostic impression that the entire system has degraded.</p>
          <p>Introduced by the pioneering statistician John W. Tukey in his seminal 1977 text <em>Exploratory Data Analysis</em>, the box-and-whisker plot was engineered specifically to solve this fundamental perceptual failure. Rather than relying on parametric assumptions of Gaussian normality, the box plot is strictly non-parametric. It relies on rank-ordered quantiles, which preserve their diagnostic integrity regardless of whether the underlying distribution is Gaussian, Pareto, log-normal, bimodal, or heavily truncated.</p>
          <p>By delegating distribution visualization to scalable vector graphics (SVG), frontend engineers can render ultra-crisp, interactive, and mathematically verifiable distribution charts directly within web browsers. SVG offers resolution independence, declarative DOM accessibility, sub-pixel rendering precision, and lightweight execution overhead compared to rasterized HTML5 canvas contexts or heavy external charting packages. Furthermore, because SVG nodes participate natively in the browser's Document Object Model (DOM), individual quartile elements, whisker caps, and outlier nodes can be styled with CSS variables, queried with assistive screen readers, and orchestrated via performant JavaScript micro-interactions.</p>
        </section>

        <section id="section-quartile-calculus">
          <h2>2. The Mathematical Pipeline: Five-Number Summary, Quartile Algorithms &amp; Tukey Hinges</h2>
          <p>Constructing an accurate SVG box plot begins with a sorted array of numerical observations. Given an unorganized dataset \( X = \{x_1, x_2, \dots, x_N\} \), the first compulsory computational phase is sorting the sequence into monotonically non-decreasing order such that \( x_{(1)} \le x_{(2)} \le \dots \le x_{(N)} \). The five core parameters of the Tukey five-number summary are defined as follows:</p>

          <div class="formula-card">
            <div class="formula-title">Tukey Five-Number Summary &amp; Fence Calculus</div>
            <div class="formula-body">
              Median = Q2 = Quantile(0.50)<br>
              IQR = Q3 - Q1<br>
              Lower Fence = Q1 - 1.5 * IQR<br>
              Upper Fence = Q3 + 1.5 * IQR
            </div>
            <div class="formula-desc">The interquartile range (IQR) captures the middle 50% of ordered distribution observations. Observations situated beyond the lower or upper fences are formally classified as statistical outliers.</div>
          </div>

          <p>While the median is universally understood as the value splitting the ordered dataset into two equal halves, the algorithmic determination of quartiles Q1 and Q3 exhibits subtle mathematical variations across statistical software packages. Understanding these nuances is critical when building production data visualization systems that must align with Python NumPy, R, or Excel backends:</p>

          <ul>
            <li><strong>Method 1: Tukey's Hinges:</strong> Tukey's original formulation splits the sorted array into two equal halves at the median. If \( N \) is odd, the median value itself is included in both the lower and upper halves. Q1 is computed as the median of the lower half, and Q3 is computed as the median of the upper half. This method is computationally trivial and highly robust for small discrete samples.</li>
            <li><strong>Method 2: R Type 7 / Excel Percentile.Inc:</strong> Uses continuous linear interpolation between sample points. The quantile rank is calculated as \( p \times (N - 1) \). The integer floor provides the index, and the fractional remainder interpolates linearly between adjacent array indices: \( Q(p) = x_{(i)} + (p(N-1) - i)(x_{(i+1)} - x_{(i)}) \). This is the default formulation implemented in D3.js and modern JavaScript data visualization utilities.</li>
            <li><strong>Method 3: Hyndman-Fan Type 8 / Unbiased Estimation:</strong> Applies quantile rank \( p \times (N + 1/3) + 1/3 \), which provides an approximately median-unbiased estimate of population quantiles regardless of the underlying continuous distribution profile.</li>
          </ul>

          <p>Once Q1 and Q3 are derived, the Interquartile Range is computed as \( \text{IQR} = Q_3 - Q_1 \). This metric defines the spatial height of the central box. John Tukey defined two distinct outlier boundary zones:</p>
          <ol>
            <li><strong>Inner Fences (Mild Outliers):</strong> Spanning \( [Q_1 - 1.5 \times \text{IQR}, Q_3 + 1.5 \times \text{IQR}] \). Whiskers extend outwards from the box to the most extreme data observations that fall <em>within</em> these inner fences. Data points outside these boundaries are plotted as distinct individual circle marks.</li>
            <li><strong>Outer Fences (Extreme Outliers):</strong> Spanning \( [Q_1 - 3.0 \times \text{IQR}, Q_3 + 3.0 \times \text{IQR}] \). Points falling beyond the outer fences indicate extreme statistical anomalies, frequently warranting specialized vector glyphs such as hollow diamonds or high-contrast warning colors.</li>
          </ol>
        </section>

        <section id="section-svg-anatomy">
          <h2>3. Anatomy of the SVG Box Plot: Coordinate Mapping, Margin Conventions &amp; Vector Primitives</h2>
          <p>Translating statistical metrics into SVG vector graphics requires mapping continuous real-valued numbers into discrete screen pixels. Because SVG coordinate systems define the origin coordinate \( (0, 0) \) at the upper-left corner with the positive Y-axis descending downward, direct mapping will invert the graph. High latency numbers would settle at the bottom of the canvas, while zero-latency queries would float at the ceiling.</p>

          <div class="formula-card">
            <div class="formula-title">Inverted Cartesian Viewport Projector</div>
            <div class="formula-body">
              Y_svg(v) = (H - PadBottom) - ((v - MinVal) / (MaxVal - MinVal)) * (H - PadTop - PadBottom)
            </div>
            <div class="formula-desc">Where H is the total SVG viewport height, PadTop and PadBottom represent the layout margin convention, and MinVal / MaxVal represent the global domain bounds.</div>
          </div>

          <p>A standard vertical SVG box plot glyph comprises six fundamental vector structural elements, arranged hierarchically inside an SVG container group element:</p>
          <ul>
            <li><strong>1. Central Box Element (<code>&lt;rect&gt;</code> or <code>&lt;path&gt;</code>):</strong> Anchored horizontally at \( X_{\text{mid}} - W/2 \). In vertical orientation, its top edge corresponds to \( Y(Q_3) \) and its bottom edge corresponds to \( Y(Q_1) \). Because of Cartesian coordinate inversion, \( Y(Q_3) \) possesses a lower numerical SVG pixel value than \( Y(Q_1) \). The box height equals \( Y(Q_1) - Y(Q_3) \).</li>
            <li><strong>2. Median Divider Line (<code>&lt;line&gt;</code>):</strong> A prominent horizontal vector line traversing from \( X_{\text{mid}} - W/2 \) to \( X_{\text{mid}} + W/2 \) at vertical coordinate \( Y(Q_2) \). This divider visually splits the box and reveals distributional skewness: if the median line hugs the bottom Q1 edge, the distribution is right-skewed; if it sits near Q3, the distribution is left-skewed.</li>
            <li><strong>3. Lower and Upper Whiskers (<code>&lt;line&gt;</code>):</strong> Two vertical line segments drawn along the central axis \( X_{\text{mid}} \). The lower whisker spans from \( Y(Q_1) \) down to \( Y(\text{Lower Whisker Extrema}) \), while the upper whisker spans from \( Y(Q_3) \) up to \( Y(\text{Upper Whisker Extrema}) \).</li>
            <li><strong>4. Whisker Terminal Caps (<code>&lt;line&gt;</code>):</strong> Horizontal crossbars (serifs) positioned at the whisker endpoints, typically spanning 40% to 50% of the box width \( W \). These caps provide visual closure, establishing unambiguous boundary limits for non-outlier data.</li>
            <li><strong>5. Outlier Markers (<code>&lt;circle&gt;</code>):</strong> Vector circles positioned at \( (X_{\text{mid}}, Y(x_{\text{outlier}})) \). To mitigate visual overlap when multiple outliers share similar coordinates, production implementations apply a slight horizontal pseudo-random jitter or adjust opacity and stroke borders.</li>
            <li><strong>6. Mean Marker Indicator (<code>&lt;circle&gt;</code> or <code>&lt;polygon&gt;</code>):</strong> An optional visual marker (such as a distinct diamond glyph or dashed crosshair) indicating the distribution's arithmetic mean. Comparing the physical distance between the mean marker and the median divider provides an immediate optical gauge of distribution asymmetry.</li>
          </ul>
        </section>

        <section id="section-figure-2">
          <h2>4. Figure 2: Mathematical Architecture &amp; Vector Layout Pipeline</h2>
          <p>The vector architecture pipeline converts raw, uncurated numerical streams into composite SVG visual entities through a series of decoupled algorithmic transformations. Figure 2 diagrams this deterministic data flow:</p>

          <figure class="article-figure">
            <svg viewBox="0 0 960 320" width="960" height="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Figure 2: SVG Box Plot Mathematical Architecture and Rendering Pipeline">
              <rect width="960" height="320" fill="#0D0D0D" rx="8" stroke="#222" stroke-width="1"></rect>
              <defs>
                <linearGradient id="boxPipeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#C1DD2D" stop-opacity="0.15"></stop>
                  <stop offset="100%" stop-color="#38BDF8" stop-opacity="0.05"></stop>
                </linearGradient>
                <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
                  <polygon points="0 0, 8 3, 0 6" fill="#C1DD2D"></polygon>
                </marker>
              </defs>

              <!-- Stage 1: Raw Stream -->
              <g transform="translate(30, 40)">
                <rect width="160" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="80" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 1: INGESTION</text>
                <text x="80" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Raw Observation Array</text>
                <rect x="20" y="80" width="120" height="24" fill="#1C1C1C" rx="4"></rect>
                <text x="80" y="96" fill="#888" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">[42, 18, 95, 33, ...]</text>
                <text x="80" y="140" fill="#AAA" font-family="'Inter', sans-serif" font-size="12" text-anchor="middle">QuickSort Algorithm</text>
                <text x="80" y="160" fill="#888" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">O(N log N) time</text>
                <rect x="20" y="184" width="120" height="24" fill="#1C1C1C" rx="4" stroke="#C1DD2D" stroke-width="0.5"></rect>
                <text x="80" y="200" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Monotonic Order</text>
                <text x="80" y="244" fill="#666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">x(1) &le; x(2) ... &le; x(N)</text>
              </g>

              <!-- Connector 1 -->
              <line x1="190" y1="160" x2="225" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#arrowhead)"></line>

              <!-- Stage 2: Quantiles -->
              <g transform="translate(235, 40)">
                <rect width="180" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="90" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 2: QUANTILES</text>
                <text x="90" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Tukey Five-Number</text>
                <path d="M 30,80 L 150,80 M 30,110 L 150,110 M 30,140 L 150,140 M 30,170 L 150,170 M 30,200 L 150,200" stroke="#222" stroke-width="1"></path>
                <text x="35" y="96" fill="#888" font-family="'JetBrains Mono', monospace" font-size="11">Q1 (25th):</text>
                <text x="145" y="96" fill="#FFF" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="end">28.4 ms</text>
                <text x="35" y="126" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11">Median (Q2):</text>
                <text x="145" y="126" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" text-anchor="end">46.2 ms</text>
                <text x="35" y="156" fill="#888" font-family="'JetBrains Mono', monospace" font-size="11">Q3 (75th):</text>
                <text x="145" y="156" fill="#FFF" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="end">71.0 ms</text>
                <text x="35" y="186" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="11">IQR:</text>
                <text x="145" y="186" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="end">42.6 ms</text>
                <text x="90" y="244" fill="#666" font-family="'Inter', sans-serif" font-size="11" text-anchor="middle">Fences: Q &plusmn; 1.5 * IQR</text>
              </g>

              <!-- Connector 2 -->
              <line x1="415" y1="160" x2="450" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#arrowhead)"></line>

              <!-- Stage 3: Filtering & Outliers -->
              <g transform="translate(460, 40)">
                <rect width="190" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="95" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 3: FENCE FILTER</text>
                <text x="95" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Boundary Segregation</text>
                <rect x="20" y="80" width="150" height="36" fill="#1A1A1A" rx="4" stroke="#EF4444" stroke-width="0.8"></rect>
                <text x="95" y="96" fill="#F87171" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Upper Outliers (&gt;134.9)</text>
                <text x="95" y="109" fill="#FFF" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Plot as distinct points</text>
                <rect x="20" y="126" width="150" height="36" fill="#1A1A1A" rx="4" stroke="#22C55E" stroke-width="0.8"></rect>
                <text x="95" y="142" fill="#4ADE80" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Whisker Bounds</text>
                <text x="95" y="155" fill="#FFF" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Min/Max within fences</text>
                <rect x="20" y="172" width="150" height="36" fill="#1A1A1A" rx="4" stroke="#38BDF8" stroke-width="0.8"></rect>
                <text x="95" y="188" fill="#38BDF8" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Notch Width (95% CI)</text>
                <text x="95" y="201" fill="#FFF" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">&plusmn; 1.57 * IQR / sqrt(N)</text>
              </g>

              <!-- Connector 3 -->
              <line x1="650" y1="160" x2="685" y2="160" stroke="#C1DD2D" stroke-width="2" marker-end="url(#arrowhead)"></line>

              <!-- Stage 4: SVG Emission -->
              <g transform="translate(695, 40)">
                <rect width="235" height="240" fill="#141414" stroke="#262626" rx="6"></rect>
                <text x="117" y="32" fill="#C1DD2D" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">STAGE 4: SVG EMISSION</text>
                <text x="117" y="58" fill="#FFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Vector DOM Assembly</text>

                <!-- Mini SVG Box Schematic -->
                <g transform="translate(117, 150)">
                  <!-- Whisker line -->
                  <line x1="0" y1="-65" x2="0" y2="65" stroke="#888" stroke-width="1.5" stroke-dasharray="2,2"></line>
                  <!-- Caps -->
                  <line x1="-15" y1="-65" x2="15" y2="-65" stroke="#FFF" stroke-width="1.5"></line>
                  <line x1="-15" y1="65" x2="15" y2="65" stroke="#FFF" stroke-width="1.5"></line>
                  <!-- Box -->
                  <rect x="-30" y="-35" width="60" height="70" fill="rgba(193,221,45,0.15)" stroke="#C1DD2D" stroke-width="1.5" rx="2"></rect>
                  <!-- Median -->
                  <line x1="-30" y1="0" x2="30" y2="0" stroke="#FFF" stroke-width="2.5"></line>
                  <!-- Outlier -->
                  <circle cx="0" cy="-78" r="3.5" fill="#EF4444" stroke="#FFF" stroke-width="1"></circle>
                </g>
                <text x="117" y="244" fill="#AAA" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">&lt;g class="boxplot"&gt;</text>
              </g>
            </svg>
            <figcaption>Figure 2: Complete architectural pipeline transforming raw observations through sorting, quantile derivation, fence segregation, and final SVG vector graphic DOM emission.</figcaption>
          </figure>
        </section>

        <section id="section-advanced-variations">
          <h2>5. Advanced Variations: Notched Confidence Intervals, Variable Widths &amp; Jittered Raw Data Overlays</h2>
          <p>While the standard rectangular box plot provides an exceptional baseline summary, production analytical workflows frequently employ advanced geometric extensions to convey deeper statistical insights:</p>

          <h3>Notched Box Plots for Visual Significance Testing</h3>
          <p>A notched box plot introduces an hourglass constriction ("waist") centered directly at the median coordinate. Introduced by McGill, Tukey, and Larsen in 1978, the notch visualizes an approximate 95% confidence interval for the true population median. The notch interval is calculated via the formula:</p>

          <div class="formula-card">
            <div class="formula-title">McGill-Tukey-Larsen Notch Formula</div>
            <div class="formula-body">
              Notch Span = Median &plusmn; 1.57 * (IQR / sqrt(N))
            </div>
            <div class="formula-desc">Where N is the total count of observations in the group, and 1.57 is the Gaussian confidence coefficient ensuring approximately 95% non-parametric confidence limits.</div>
          </div>

          <p>When comparing multiple distributions side-by-side, if the notched waists of two boxes do not overlap along the continuous value axis, the viewer can conclude with approximately 95% statistical confidence that their true population medians differ significantly. To render a notched box in SVG, the standard <code>&lt;rect&gt;</code> element is replaced by a closed vector path <code>&lt;path d="..."&gt;</code> that traces the notched profile:</p>

          <pre><code>// SVG Notched Box Path Construction
function buildNotchedBoxPath(cx, w, yQ1, yQ3, yMed, yNotchTop, yNotchBot) {
  const hw = w / 2;
  const nw = w * 0.25; // Narrow waist width
  return [
    `M ${cx - hw} ${yQ1}`,
    `L ${cx - hw} ${yNotchBot}`,
    `L ${cx - nw} ${yMed}`,
    `L ${cx - hw} ${yNotchTop}`,
    `L ${cx - hw} ${yQ3}`,
    `L ${cx + hw} ${yQ3}`,
    `L ${cx + hw} ${yNotchTop}`,
    `L ${cx + nw} ${yMed}`,
    `L ${cx + hw} ${yNotchBot}`,
    `L ${cx + hw} ${yQ1}`,
    'Z'
  ].join(' ');
}</code></pre>

          <h3>Variable-Width Box Plots for Sample Weight Proportionality</h3>
          <p>In standard visualizations, each box occupies an identical width regardless of whether it represents 20 sample observations or 20,000 observations. This visual equivalence can inadvertently mislead observers into attributing equal statistical certainty to highly disparate sample sizes. In variable-width box plots, the horizontal width \( W_k \) of box \( k \) is scaled proportionally to the square root of its sample size:</p>

          <div class="formula-card">
            <div class="formula-title">Sample-Proportional Box Width Scaling</div>
            <div class="formula-body">
              Width(k) = BaseWidth * sqrt(N_k / Max_N)
            </div>
            <div class="formula-desc">Square-root scaling ensures that the visual surface area of the box reflects the sample size, directly aligning with human optical perception of two-dimensional marks.</div>
          </div>

          <h3>Overlaying Jittered Raw Data Observations (Strip Chart Integration)</h3>
          <p>Despite their power, box plots possess one notable limitation: they conceal distribution modality. A bimodal distribution with two distinct peaks at 20 ms and 80 ms can produce an identical box plot to a uniform distribution spanning 20 ms to 80 ms. To prevent this diagnostic blindness, modern high-end data visualization systems overlay raw observation points directly over or alongside the SVG box glyph.</p>
          <p>To avoid massive occlusion caused by overlapping dots, points are displaced along the categorical axis using a deterministic pseudo-random jitter. For an observation at value \( y \), its horizontal coordinate is calculated as \( X_{\text{mid}} + (R(i) - 0.5) \times W_{\text{jitter}} \), where \( R(i) \) is a uniform pseudo-random number between 0 and 1. By rendering these dots with low opacity (such as <code>fill-opacity="0.35"</code>) and small radii (1.5 to 2.5 pixels), the viewer perceives both the macroscopic Tukey summary and the microscopic raw density clusters simultaneously.</p>
        </section>

        <section id="section-outlier-detection">
          <h2>6. Outlier Detection Engineering: Tukey Fences, Extreme Thresholds &amp; Spatial Clustering</h2>
          <p>Outlier management represents one of the most operationally critical capabilities of SVG box plots. Unlike automatic smoothing filters that discard extreme values, an SVG box plot explicitly preserves outliers, isolating them as actionable vector marks.</p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Classification Zone</th>
                  <th>Mathematical Threshold Formula</th>
                  <th>Gaussian Probability</th>
                  <th>Recommended SVG Visual Treatment</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Core Range (IQR)</strong></td>
                  <td>\( [Q_1, Q_3] \)</td>
                  <td>50.00%</td>
                  <td>Solid box fill with high-contrast border and median divider</td>
                </tr>
                <tr>
                  <td><strong>Whisker Range</strong></td>
                  <td>\( [Q_1 - 1.5\text{IQR}, Q_3 + 1.5\text{IQR}] \)</td>
                  <td>99.30%</td>
                  <td>Dashed/solid axial line capped with horizontal terminal serifs</td>
                </tr>
                <tr>
                  <td><strong>Mild Outlier</strong></td>
                  <td>\( (1.5\text{IQR}, 3.0\text{IQR}] \) from box</td>
                  <td>~0.70%</td>
                  <td>Hollow circle mark (radius 3.5px, stroke-width 1.5px, neon accent)</td>
                </tr>
                <tr>
                  <td><strong>Extreme Outlier</strong></td>
                  <td>\( > 3.0\text{IQR} \) from box</td>
                  <td>&lt; 0.002%</td>
                  <td>Filled diamond or warning triangle (radius 5px, vivid red stroke #EF4444)</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p>When dealing with extreme data volumes, thousands of outliers can cause DOM bloating if every single outlier is rendered as a distinct SVG <code>&lt;circle&gt;</code> element. In high-performance web systems, three optimization strategies are employed:</p>
          <ol>
            <li><strong>Spatial Binning / 1D Kernel Density Merging:</strong> Outliers situated within 2 vertical pixels of each other are merged into a single composite outlier marker whose radius scales with point density, accompanied by an interactive tooltip detailing the aggregated count.</li>
            <li><strong>Hover Quadtree Indexing:</strong> Rather than attaching individual event listeners to hundreds of outlier DOM nodes, a single listener on the parent SVG container queries a fast spatial index to highlight nearby points in \( O(\log N) \) time.</li>
            <li><strong>Canvas Hybrid Fallback:</strong> For datasets containing over 50,000 raw points, the static box plot frame is rendered in crisp SVG, while the dense jitter cloud is drawn on an underlying HTML5 canvas layer.</li>
          </ol>
        </section>

        <!-- INTERACTIVE STUDIO SANDBOX -->
        <section class="interactive-sandbox" id="interactive-box-studio">
          <div class="sandbox-header">
            <div class="sandbox-title">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#C1DD2D" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg>
              Interactive SVG Box Plot &amp; Whisker Studio
            </div>
            <span class="sandbox-badge">Real-Time Vector Engine</span>
          </div>

          <p style="font-size: 14.5px; color: #AAA; margin-bottom: 20px;">Adjust distribution parameters, toggle notched confidence waists, explore Tukey fence outlier detection, and export production-ready SVG vector markup instantly.</p>

          <div class="sandbox-controls">
            <div class="control-row">
              <label for="box-preset-select">Telemetry Preset Dataset:</label>
              <select id="box-preset-select" class="control-select">
                <option value="api-latency">API Response Latency (ms)</option>
                <option value="ml-loss">Neural Net Training Loss</option>
                <option value="memory-footprint">Container RAM Utilization (MB)</option>
                <option value="e-commerce">Checkout Cart Value ($)</option>
              </select>
            </div>

            <div class="control-row">
              <label for="box-whisker-rule">Whisker Boundary Rule:</label>
              <select id="box-whisker-rule" class="control-select">
                <option value="tukey">Tukey Standard (1.5 * IQR)</option>
                <option value="extrema">Min / Max Extrema (No Outliers)</option>
                <option value="percentile">9th / 91st Percentiles</option>
              </select>
            </div>

            <div class="control-row">
              <label for="box-width-slider">Box Width (px): <span id="box-width-val" style="color:#C1DD2D; font-weight:700;">54px</span></label>
              <input type="range" id="box-width-slider" class="control-input" min="30" max="84" value="54" step="2">
            </div>

            <div class="control-row" style="justify-content: center; gap: 8px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <input type="checkbox" id="box-notches-toggle" style="accent-color:#C1DD2D; cursor:pointer;">
                <label for="box-notches-toggle" style="cursor:pointer; color:#FFF;">Enable 95% CI Notches</label>
              </div>
              <div style="display:flex; align-items:center; gap:8px;">
                <input type="checkbox" id="box-jitter-toggle" checked style="accent-color:#C1DD2D; cursor:pointer;">
                <label for="box-jitter-toggle" style="cursor:pointer; color:#FFF;">Show Jittered Observations</label>
              </div>
              <div style="display:flex; align-items:center; gap:8px;">
                <input type="checkbox" id="box-outliers-toggle" checked style="accent-color:#C1DD2D; cursor:pointer;">
                <label for="box-outliers-toggle" style="cursor:pointer; color:#FFF;">Highlight Fenced Outliers</label>
              </div>
            </div>
          </div>

          <div class="preview-stage-container">
            <svg id="box-live-svg" class="box-svg-canvas" viewBox="0 0 760 480" width="760" height="480" xmlns="http://www.w3.org/2000/svg" role="graphics-document" aria-label="Interactive SVG Box Plot Studio Displaying Distribution Comparison">
              <!-- Rendered dynamically by JavaScript -->
            </svg>
          </div>

          <div class="stats-readout-box">
            <div class="stat-item">
              <span class="stat-label">Active Groups</span>
              <span class="stat-val highlight" id="stat-group-count">4 Series</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">Lead Median (Q2)</span>
              <span class="stat-val" id="stat-lead-median">48.2 ms</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">Interquartile (IQR)</span>
              <span class="stat-val" id="stat-lead-iqr">26.4 ms</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">Notch 95% CI Span</span>
              <span class="stat-val highlight" id="stat-lead-notch">&plusmn; 4.1 ms</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">Total Outliers</span>
              <span class="stat-val" id="stat-total-outliers">14 Points</span>
            </div>
          </div>

          <div class="action-btn-row">
            <button class="copy-btn" id="copy-box-svg-btn" type="button" aria-label="Copy Standalone SVG to Clipboard">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
              <span>Copy Standalone SVG</span>
            </button>
          </div>
        </section>

        <section id="section-production-engine">
          <h2>7. Production-Grade Zero-Dependency ES6 Box Plot Engine</h2>
          <p>To eliminate bloated dependencies and achieve maximum client-side rendering speed, production applications benefit from a self-contained, standalone ES6 charting class. Below is a complete, production-ready module that calculates quantiles, isolates Tukey outliers, derives notched geometry, and outputs clean SVG markup:</p>

          <pre><code>// Production-Grade Zero-Dependency SVG Box Plot Engine
class SvgBoxPlotEngine {
  constructor(config = {}) {
    this.width = config.width || 760;
    this.height = config.height || 480;
    this.padding = config.padding || { top: 40, right: 30, bottom: 50, left: 60 };
    this.boxWidth = config.boxWidth || 50;
    this.enableNotches = config.enableNotches || false;
  }

  // Linear interpolation quantile calculation (Type 7)
  static computeQuantile(sortedArr, p) {
    if (!sortedArr.length) return 0;
    const n = sortedArr.length;
    if (p &lt;= 0) return sortedArr[0];
    if (p &gt;= 1) return sortedArr[n - 1];
    const index = p * (n - 1);
    const low = Math.floor(index);
    const high = Math.ceil(index);
    const weight = index - low;
    return sortedArr[low] + weight * (sortedArr[high] - sortedArr[low]);
  }

  // Full five-number summary and fence derivation
  static analyzeDistribution(values, whiskerRule = 'tukey') {
    const sorted = [...values].sort((a, b) => a - b);
    const n = sorted.length;
    const min = sorted[0];
    const max = sorted[n - 1];
    const q1 = SvgBoxPlotEngine.computeQuantile(sorted, 0.25);
    const median = SvgBoxPlotEngine.computeQuantile(sorted, 0.50);
    const q3 = SvgBoxPlotEngine.computeQuantile(sorted, 0.75);
    const iqr = q3 - q1;

    let lowerWhisker, upperWhisker;
    let outliers = [];

    if (whiskerRule === 'tukey') {
      const lowerFence = q1 - 1.5 * iqr;
      const upperFence = q3 + 1.5 * iqr;
      
      const inBounds = sorted.filter(v => v &gt;= lowerFence &amp;&amp; v &lt;= upperFence);
      lowerWhisker = inBounds.length ? inBounds[0] : q1;
      upperWhisker = inBounds.length ? inBounds[inBounds.length - 1] : q3;
      outliers = sorted.filter(v => v &lt; lowerFence || v &gt; upperFence);
    } else {
      lowerWhisker = min;
      upperWhisker = max;
    }

    const notchSpan = (1.57 * iqr) / Math.sqrt(n || 1);

    return {
      n, min, max, q1, median, q3, iqr,
      lowerWhisker, upperWhisker,
      notchTop: Math.min(q3, median + notchSpan),
      notchBottom: Math.max(q1, median - notchSpan),
      outliers
    };
  }

  // Generate complete SVG Markup String
  render(groups) {
    const plotW = this.width - this.padding.left - this.padding.right;
    const plotH = this.height - this.padding.top - this.padding.bottom;

    // Find global value extent
    let globalMin = Infinity;
    let globalMax = -Infinity;
    groups.forEach(g => {
      g.values.forEach(v => {
        if (v &lt; globalMin) globalMin = v;
        if (v &gt; globalMax) globalMax = v;
      });
    });
    const domainSpan = (globalMax - globalMin) || 1;

    const scaleY = v =&gt; (this.height - this.padding.bottom) - ((v - globalMin) / domainSpan) * plotH;
    const slotW = plotW / groups.length;

    let svgMarks = '';

    groups.forEach((group, idx) => {
      const stats = SvgBoxPlotEngine.analyzeDistribution(group.values);
      const cx = this.padding.left + slotW * (idx + 0.5);
      const yQ1 = scaleY(stats.q1);
      const yQ3 = scaleY(stats.q3);
      const yMed = scaleY(stats.median);
      const yLowWhisk = scaleY(stats.lowerWhisker);
      const yUppWhisk = scaleY(stats.upperWhisker);
      const hw = this.boxWidth / 2;

      // Axial whisker line
      svgMarks += `&lt;line x1="${cx}" y1="${yUppWhisk}" x2="${cx}" y2="${yLowWhisk}" stroke="#777" stroke-width="1.5" stroke-dasharray="3,3"/&gt;`;
      // Whisker terminal caps
      svgMarks += `&lt;line x1="${cx - hw * 0.45}" y1="${yUppWhisk}" x2="${cx + hw * 0.45}" y2="${yUppWhisk}" stroke="#FFF" stroke-width="1.5"/&gt;`;
      svgMarks += `&lt;line x1="${cx - hw * 0.45}" y1="${yLowWhisk}" x2="${cx + hw * 0.45}" y2="${yLowWhisk}" stroke="#FFF" stroke-width="1.5"/&gt;`;

      // Central Box (notched or standard)
      if (this.enableNotches) {
        const yNTop = scaleY(stats.notchTop);
        const yNBot = scaleY(stats.notchBottom);
        const nw = this.boxWidth * 0.28;
        const d = `M ${cx - hw} ${yQ1} L ${cx - hw} ${yNBot} L ${cx - nw} ${yMed} L ${cx - hw} ${yNTop} L ${cx - hw} ${yQ3} L ${cx + hw} ${yQ3} L ${cx + hw} ${yNTop} L ${cx + nw} ${yMed} L ${cx + hw} ${yNBot} L ${cx + hw} ${yQ1} Z`;
        svgMarks += `&lt;path d="${d}" fill="${group.color || '#C1DD2D'}" fill-opacity="0.25" stroke="${group.color || '#C1DD2D'}" stroke-width="1.8"/&gt;`;
      } else {
        const boxH = Math.max(1, yQ1 - yQ3);
        svgMarks += `&lt;rect x="${cx - hw}" y="${yQ3}" width="${this.boxWidth}" height="${boxH}" rx="3" fill="${group.color || '#C1DD2D'}" fill-opacity="0.2" stroke="${group.color || '#C1DD2D'}" stroke-width="1.8"/&gt;`;
      }

      // Median divider
      svgMarks += `&lt;line x1="${cx - hw}" y1="${yMed}" x2="${cx + hw}" y2="${yMed}" stroke="#FFF" stroke-width="2.5"/&gt;`;

      // Outlier dots
      stats.outliers.forEach(outVal => {
        const oy = scaleY(outVal);
        svgMarks += `&lt;circle cx="${cx}" cy="${oy}" r="3.5" fill="#EF4444" stroke="#FFF" stroke-width="1"/&gt;`;
      });
    });

    return `&lt;svg viewBox="0 0 ${this.width} ${this.height}" xmlns="http://www.w3.org/2000/svg" role="graphics-document"&gt;${svgMarks}&lt;/svg&gt;`;
  }
}</code></pre>
        </section>

        <section id="section-accessibility-theming">
          <h2>8. Accessibility, WCAG 2.2 AA Contrast &amp; Multi-Theme Vector Theming</h2>
          <p>Delivering high-stakes statistical data visualizations requires strict adherence to web accessibility standards. Box plots carry complex multi-element spatial relationships that can present severe barriers to screen-reader users and individuals with vision impairments if not authored conscientiously.</p>

          <h3>Semantic DOM Structure &amp; ARIA Roles</h3>
          <p>To comply with WCAG 2.2 criteria, the root SVG container must declare <code>role="graphics-document"</code> accompanied by an unambiguous <code>aria-label</code> and internal <code>&lt;title&gt;</code> and <code>&lt;desc&gt;</code> tags. Within the graphic, each group box glyph is structured as a discrete <code>&lt;g role="graphics-symbol"&gt;</code> element that participates in keyboard navigation via <code>tabindex="0"</code>.</p>
          <p>When an assistive technology focuses on a box glyph, its <code>aria-label</code> articulates the full five-number summary: <em>"Production Service Cluster: Sample size 1,240, Median 46.2 ms, Interquartile Range 28.4 ms to 71.0 ms, Whisker bounds 12.0 ms to 134.0 ms, 8 outliers detected."</em> This ensures complete informational parity between visual and non-visual consumers.</p>

          <h3>Color Contrast Ratios &amp; Dual-Theme Styling</h3>
          <p>Under WCAG 2.2 AA rules, graphical user interface components must meet a minimum contrast ratio of 3.0:1 against adjacent colors, while informative text labels must satisfy at least 4.5:1. In dark mode, our high-visibility lime palette <code>#C1DD2D</code> achieves an exceptional 13.8:1 contrast against pure black <code>#0A0A0A</code>. For light mode interfaces, links and interactive highlights adapt to deep forest olive <code>#4D6300</code>, delivering a robust 5.4:1 contrast against crisp white <code>#FAFAFA</code>.</p>
        </section>

        <section id="section-takeaways">
          <div class="takeaway-box">
            <h3>Key Engineering Takeaways</h3>
            <ul>
              <li><strong>Prioritize Non-Parametric Metrics:</strong> Use medians and interquartile ranges (IQR) to communicate real-world engineering metrics resistant to skewness and outlier distortion.</li>
              <li><strong>Enforce 1.5 &times; IQR Tukey Fences:</strong> Algorithmic outlier segregation prevents anomalous spikes from corrupting whisker boundaries while preserving visibility of outliers as distinct markers.</li>
              <li><strong>Leverage Notches for Hypothesis Testing:</strong> Non-overlapping notch intervals allow frontend consumers to confirm 95% statistical significance at a single glance without computing formal p-values.</li>
              <li><strong>Invert Cartesian Y-Coordinates:</strong> Always map continuous values via <code>(H - PadBottom) - ratio * InnerH</code> to account for SVG top-down coordinate space.</li>
              <li><strong>Guarantee Dual-Theme Accessibility:</strong> Pair semantic ARIA roles with WCAG AA compliant contrast ratios (<code>#C1DD2D</code> on dark, <code>#4D6300</code> on light) for full visual and screen-reader inclusivity.</li>
            </ul>
          </div>
        </section>

        <section class="faq-section" id="section-faq">
          <h2>9. Frequently Asked Questions</h2>
          <div class="faq-item">
            <div class="faq-question">Why is the median preferred over the arithmetic mean in box and whisker plots?</div>
            <div class="faq-answer">The median represents the non-parametric fiftieth percentile of an ordered dataset, dividing observations into two equal halves. Unlike the arithmetic mean, the median is highly resistant to extreme skewness, heavy tails, and anomalous outliers. In real-world engineering telemetry such as API response latencies, a small handful of catastrophic timeout events can drag the arithmetic mean upward by hundreds of milliseconds, giving a false impression of degraded baseline performance. The median accurately conveys the typical user experience, while the surrounding interquartile range (IQR) and whisker bounds isolate anomalous outliers without corrupting central tendency indicators.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How does John Tukey's 1.5 IQR multiplier establish outlier fence thresholds?</div>
            <div class="faq-answer">John Tukey established the 1.5 multiplier for interquartile range (IQR) outlier fences as a pragmatic heuristic grounded in Gaussian distribution theory. For a perfectly normal Gaussian distribution, the interquartile range spans approximately 1.349 standard deviations. Adding and subtracting 1.5 times the IQR from the third and first quartiles respectively yields boundary fences situated at approximately plus or minus 2.698 standard deviations from the distribution mean. In a standard normal distribution, this threshold captures approximately 99.3 percent of all valid observations, classifying only 0.7 percent of extreme observations as potential outliers, balancing sensitivity with noise resistance.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How do notched box plots evaluate statistical significance between comparison groups?</div>
            <div class="faq-answer">Notches in an SVG box plot visually represent an approximate 95 percent confidence interval for the true population median. The notch boundaries extend above and below the calculated median by a factor of 1.57 multiplied by the interquartile range divided by the square root of the sample size N. When comparing two or more adjacent box plots on identical scale axes, if the notches of two distributions do not overlap vertically, an observer can conclude with approximately 95 percent confidence that their true population medians are statistically significantly different, providing immediate hypothesis testing without formal p-value calculation.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How do you map continuous statistical values into an inverted SVG viewport canvas?</div>
            <div class="faq-answer">Because SVG canvas viewports place the origin point (0, 0) at the top-left corner with the positive Y-axis descending downward, direct mapping of higher statistical values would incorrectly place higher metrics toward the bottom of the screen. To establish an intuitive Cartesian coordinate system where higher values ascend upward, developers apply an inverted linear transformation: y_svg = (totalHeight - paddingBottom) - ((dataValue - domainMin) / (domainMax - domainMin)) * (totalHeight - paddingTop - paddingBottom). This subtraction from the baseline coordinate guarantees that the minimum domain boundary anchors at the bottom axis and maximum metrics rise toward the top margin.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">What is the purpose of overlaying jittered strip chart points on an SVG box plot?</div>
            <div class="faq-answer">While a box plot efficiently condenses hundreds or thousands of observations into five summary metrics, it inherently masks multi-modality, bi-modal distributions, gaps, and sample density clustering. Overlaying semi-transparent jittered dots—displacing each raw observation along the perpendicular categorical axis by a deterministic pseudo-random offset—reveals the true underlying distribution morphology. Observers can simultaneously inspect the macroscopic summary quartiles of the Tukey box alongside the microscopic density clustering and sample size weight of raw data points.</div>
          </div>
          <div class="faq-item">
            <div class="faq-question">How do you guarantee WCAG 2.2 AA accessibility for complex interactive SVG box plots?</div>
            <div class="faq-answer">Full WCAG 2.2 AA accessibility requires marking the root SVG container with role='graphics-document' alongside aria-label and companion title and desc elements detailing dataset purpose and sample size. Individual box plot glyphs and outlier points must receive role='graphics-symbol', keyboard focusability via tabindex='0', and programmatic ARIA labels detailing median, Q1, Q3, whisker bounds, and outlier values. Furthermore, color encoding must never be the sole information channel; distinct fill patterns or stroke styles must differentiate categories, and all text labels must achieve at least 4.5:1 contrast against both light and dark backgrounds.</div>
          </div>
        </section>

      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <a href="#section-foundations">1. Architectural Foundations</a>
            <a href="#section-quartile-calculus">2. Mathematical Pipeline &amp; Hinges</a>
            <a href="#section-svg-anatomy">3. SVG Box Plot Anatomy</a>
            <a href="#section-figure-2">4. Figure 2: Architecture Pipeline</a>
            <a href="#section-advanced-variations">5. Advanced Notches &amp; Jitter</a>
            <a href="#section-outlier-detection">6. Outlier Detection Engineering</a>
            <a href="#interactive-box-studio">7. Interactive Studio Sandbox</a>
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
            <a href="/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide/">SVG Scatter Plots &amp; Bubble Charts</a>
            <a href="/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide/">SVG Network Graphs &amp; Force Layouts</a>
            <a href="/articles/svg-choropleth-maps-and-geographic-vector-visualization-guide/">SVG Choropleth Maps &amp; GIS</a>
            <a href="/articles/svg-heatmaps-and-activity-matrix-visualization-guide/">SVG Heatmaps &amp; Activity Matrices</a>
            <a href="/articles/svg-radar-charts-and-multivariate-polar-visualization-guide/">SVG Radar Charts &amp; Polar Visuals</a>
            <a href="/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/">SVG Sparklines &amp; Micro-Charts</a>
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
    // Theme toggle handler
    const themeBtn = document.getElementById('theme-toggle');
    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', nextTheme);
      });
    }

    // Interactive Box Plot Studio Script
    (function initBoxStudio() {
      const liveSvg = document.getElementById('box-live-svg');
      const presetSelect = document.getElementById('box-preset-select');
      const whiskerRuleSelect = document.getElementById('box-whisker-rule');
      const boxWidthSlider = document.getElementById('box-width-slider');
      const boxWidthVal = document.getElementById('box-width-val');
      const notchesToggle = document.getElementById('box-notches-toggle');
      const jitterToggle = document.getElementById('box-jitter-toggle');
      const outliersToggle = document.getElementById('box-outliers-toggle');
      const copyBtn = document.getElementById('copy-box-svg-btn');

      const statGroupCount = document.getElementById('stat-group-count');
      const statLeadMedian = document.getElementById('stat-lead-median');
      const statLeadIqr = document.getElementById('stat-lead-iqr');
      const statLeadNotch = document.getElementById('stat-lead-notch');
      const statTotalOutliers = document.getElementById('stat-total-outliers');

      if (!liveSvg) return;

      const groupColors = ['#C1DD2D', '#38BDF8', '#F59E0B', '#EC4899'];

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
        const rng = pseudoRandom(preset === 'api-latency' ? 101 : preset === 'ml-loss' ? 202 : preset === 'memory-footprint' ? 303 : 404);
        const groups = [
          { name: 'Prod-US', values: [] },
          { name: 'Prod-EU', values: [] },
          { name: 'Staging', values: [] },
          { name: 'Canary', values: [] }
        ];

        groups.forEach((g, gIdx) => {
          const baseCount = 60 + Math.floor(rng() * 40);
          const baseMean = preset === 'api-latency' ? (35 + gIdx * 12) : preset === 'ml-loss' ? (1.8 - gIdx * 0.3) : preset === 'memory-footprint' ? (240 + gIdx * 80) : (45 + gIdx * 25);
          const spread = preset === 'api-latency' ? 18 : preset === 'ml-loss' ? 0.4 : preset === 'memory-footprint' ? 65 : 20;

          for (let i = 0; i < baseCount; i++) {
            // Box-Muller normal distribution approximation
            const u1 = Math.max(0.0001, rng());
            const u2 = rng();
            const z = Math.sqrt(-2.0 * Math.log(u1)) * Math.cos(2.0 * Math.PI * u2);
            let val = +(baseMean + z * spread).toFixed(2);
            if (preset === 'api-latency' || preset === 'memory-footprint' || preset === 'e-commerce') {
              val = Math.max(5, val);
            }
            g.values.push(val);
          }

          // Inject intentional controlled outliers
          if (preset === 'api-latency') {
            g.values.push(+(baseMean + spread * 3.4).toFixed(2));
            if (gIdx === 0) g.values.push(+(baseMean + spread * 4.2).toFixed(2));
          } else if (preset === 'memory-footprint') {
            g.values.push(+(baseMean + spread * 3.2).toFixed(2));
          }
        });

        return groups;
      }

      function computeQuantile(sortedArr, p) {
        if (!sortedArr.length) return 0;
        const n = sortedArr.length;
        if (p <= 0) return sortedArr[0];
        if (p >= 1) return sortedArr[n - 1];
        const idx = p * (n - 1);
        const low = Math.floor(idx);
        const high = Math.ceil(idx);
        const weight = idx - low;
        return sortedArr[low] + weight * (sortedArr[high] - sortedArr[low]);
      }

      function calculateStats(values, whiskerRule) {
        const sorted = [...values].sort((a, b) => a - b);
        const n = sorted.length;
        const min = sorted[0];
        const max = sorted[n - 1];
        const q1 = computeQuantile(sorted, 0.25);
        const median = computeQuantile(sorted, 0.50);
        const q3 = computeQuantile(sorted, 0.75);
        const iqr = q3 - q1;

        let lowerWhisker, upperWhisker;
        let outliers = [];

        if (whiskerRule === 'tukey') {
          const lowerFence = q1 - 1.5 * iqr;
          const upperFence = q3 + 1.5 * iqr;
          const inBounds = sorted.filter(v => v >= lowerFence && v <= upperFence);
          lowerWhisker = inBounds.length ? inBounds[0] : q1;
          upperWhisker = inBounds.length ? inBounds[inBounds.length - 1] : q3;
          outliers = sorted.filter(v => v < lowerFence || v > upperFence);
        } else if (whiskerRule === 'percentile') {
          lowerWhisker = computeQuantile(sorted, 0.09);
          upperWhisker = computeQuantile(sorted, 0.91);
          outliers = sorted.filter(v => v < lowerWhisker || v > upperWhisker);
        } else {
          lowerWhisker = min;
          upperWhisker = max;
        }

        const notchSpan = (1.57 * iqr) / Math.sqrt(n || 1);
        return {
          n, min, max, q1, median, q3, iqr,
          lowerWhisker, upperWhisker,
          notchTop: Math.min(q3, median + notchSpan),
          notchBottom: Math.max(q1, median - notchSpan),
          notchSpan,
          outliers,
          rawSorted: sorted
        };
      }

      function renderStudio() {
        const preset = presetSelect.value;
        const whiskerRule = whiskerRuleSelect.value;
        const boxWidth = parseInt(boxWidthSlider.value, 10);
        boxWidthVal.textContent = boxWidth + 'px';
        const showNotches = notchesToggle.checked;
        const showJitter = jitterToggle.checked;
        const showOutliers = outliersToggle.checked;

        const groups = generateDataset(preset);
        const statsList = groups.map(g => calculateStats(g.values, whiskerRule));

        // Global min/max
        let globalMin = Infinity;
        let globalMax = -Infinity;
        statsList.forEach(s => {
          if (s.min < globalMin) globalMin = s.min;
          if (s.max > globalMax) globalMax = s.max;
        });

        const pad = { top: 40, right: 40, bottom: 60, left: 70 };
        const viewW = 760;
        const viewH = 480;
        const plotW = viewW - pad.left - pad.right;
        const plotH = viewH - pad.top - pad.bottom;
        const domainSpan = (globalMax - globalMin) || 1;

        const scaleY = v => (viewH - pad.bottom) - ((v - globalMin) / domainSpan) * plotH;
        const slotW = plotW / groups.length;

        // Build SVG Elements
        let gridLines = '';
        const yTicks = 5;
        for (let t = 0; t <= yTicks; t++) {
          const val = globalMin + (domainSpan / yTicks) * t;
          const yPos = scaleY(val);
          gridLines += `<line x1="${pad.left}" y1="${yPos.toFixed(1)}" x2="${viewW - pad.right}" y2="${yPos.toFixed(1)}" stroke="#1F1F1F" stroke-width="1"/>`;
          gridLines += `<text x="${pad.left - 12}" y="${(yPos + 4).toFixed(1)}" fill="#777" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="end">${val.toFixed(1)}</text>`;
        }

        let boxMarks = '';
        let totalOutliersCount = 0;

        groups.forEach((g, idx) => {
          const s = statsList[idx];
          totalOutliersCount += s.outliers.length;
          const cx = pad.left + slotW * (idx + 0.5);
          const color = groupColors[idx % groupColors.length];
          const yQ1 = scaleY(s.q1);
          const yQ3 = scaleY(s.q3);
          const yMed = scaleY(s.median);
          const yLowWhisk = scaleY(s.lowerWhisker);
          const yUppWhisk = scaleY(s.upperWhisker);
          const hw = boxWidth / 2;

          // Jittered raw observations
          if (showJitter) {
            const rngJitter = pseudoRandom(idx * 777 + 13);
            s.rawSorted.forEach((rv, rIdx) => {
              const ry = scaleY(rv);
              const rx = cx + (rngJitter() - 0.5) * (boxWidth * 0.9);
              boxMarks += `<circle cx="${rx.toFixed(1)}" cy="${ry.toFixed(1)}" r="2" fill="${color}" fill-opacity="0.3" stroke="none"/>`;
            });
          }

          // Whisker axial line
          boxMarks += `<line x1="${cx.toFixed(1)}" y1="${yUppWhisk.toFixed(1)}" x2="${cx.toFixed(1)}" y2="${yLowWhisk.toFixed(1)}" stroke="#666" stroke-width="1.8" stroke-dasharray="3,3"/>`;
          // Whisker caps
          const capW = hw * 0.5;
          boxMarks += `<line x1="${(cx - capW).toFixed(1)}" y1="${yUppWhisk.toFixed(1)}" x2="${(cx + capW).toFixed(1)}" y2="${yUppWhisk.toFixed(1)}" stroke="#FFF" stroke-width="2"/>`;
          boxMarks += `<line x1="${(cx - capW).toFixed(1)}" y1="${yLowWhisk.toFixed(1)}" x2="${(cx + capW).toFixed(1)}" y2="${yLowWhisk.toFixed(1)}" stroke="#FFF" stroke-width="2"/>`;

          // Central Box
          if (showNotches) {
            const yNTop = scaleY(s.notchTop);
            const yNBot = scaleY(s.notchBottom);
            const nw = boxWidth * 0.28;
            const pathD = [
              `M ${(cx - hw).toFixed(1)} ${yQ1.toFixed(1)}`,
              `L ${(cx - hw).toFixed(1)} ${yNBot.toFixed(1)}`,
              `L ${(cx - nw).toFixed(1)} ${yMed.toFixed(1)}`,
              `L ${(cx - hw).toFixed(1)} ${yNTop.toFixed(1)}`,
              `L ${(cx - hw).toFixed(1)} ${yQ3.toFixed(1)}`,
              `L ${(cx + hw).toFixed(1)} ${yQ3.toFixed(1)}`,
              `L ${(cx + hw).toFixed(1)} ${yNTop.toFixed(1)}`,
              `L ${(cx + nw).toFixed(1)} ${yMed.toFixed(1)}`,
              `L ${(cx + hw).toFixed(1)} ${yNBot.toFixed(1)}`,
              `L ${(cx + hw).toFixed(1)} ${yQ1.toFixed(1)}`,
              'Z'
            ].join(' ');
            boxMarks += `<path d="${pathD}" fill="${color}" fill-opacity="0.28" stroke="${color}" stroke-width="2"/>`;
          } else {
            const boxH = Math.max(2, yQ1 - yQ3);
            boxMarks += `<rect x="${(cx - hw).toFixed(1)}" y="${yQ3.toFixed(1)}" width="${boxWidth}" height="${boxH.toFixed(1)}" rx="3" fill="${color}" fill-opacity="0.25" stroke="${color}" stroke-width="2"/>`;
          }

          // Median line
          boxMarks += `<line x1="${(cx - hw).toFixed(1)}" y1="${yMed.toFixed(1)}" x2="${(cx + hw).toFixed(1)}" y2="${yMed.toFixed(1)}" stroke="#FFFFFF" stroke-width="3"/>`;

          // Outliers
          if (showOutliers) {
            s.outliers.forEach(ov => {
              const oy = scaleY(ov);
              boxMarks += `<circle cx="${cx.toFixed(1)}" cy="${oy.toFixed(1)}" r="4" fill="#EF4444" stroke="#FFFFFF" stroke-width="1.2"/>`;
            });
          }

          // Group Label
          boxMarks += `<text x="${cx.toFixed(1)}" y="${viewH - pad.bottom + 26}" fill="#EEE" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">${g.name}</text>`;
          boxMarks += `<text x="${cx.toFixed(1)}" y="${viewH - pad.bottom + 42}" fill="#777" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">N=${s.n}</text>`;
        });

        // Update SVG DOM
        liveSvg.innerHTML = `
          <rect width="${viewW}" height="${viewH}" fill="#0A0A0A" rx="6"/>
          ${gridLines}
          ${boxMarks}
        `;

        // Update readouts
        const lead = statsList[0];
        statGroupCount.textContent = groups.length + ' Series';
        statLeadMedian.textContent = lead.median.toFixed(1) + (preset === 'api-latency' ? ' ms' : preset === 'memory-footprint' ? ' MB' : '');
        statLeadIqr.textContent = lead.iqr.toFixed(1) + (preset === 'api-latency' ? ' ms' : preset === 'memory-footprint' ? ' MB' : '');
        statLeadNotch.textContent = '\u00B1 ' + lead.notchSpan.toFixed(1) + (preset === 'api-latency' ? ' ms' : '');
        statTotalOutliers.textContent = totalOutliersCount + ' Points';
      }

      // Event Listeners
      presetSelect.addEventListener('change', renderStudio);
      whiskerRuleSelect.addEventListener('change', renderStudio);
      boxWidthSlider.addEventListener('input', renderStudio);
      notchesToggle.addEventListener('change', renderStudio);
      jitterToggle.addEventListener('change', renderStudio);
      outliersToggle.addEventListener('change', renderStudio);

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

print(f"Generated Article 1 successfully at: {target_file}")
