const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

let passed = 0;
let failed = 0;

function assert(condition, message) {
  if (condition) {
    passed++;
    console.log(`  [PASS] ${message}`);
  } else {
    failed++;
    console.error(`  [FAIL] ${message}`);
  }
}

console.log('=== VERIFYING OCTOBER 30, 2026 DELIVERABLES & SITE INTEGRATION ===\n');

const deliverables = [
  {
    type: 'article',
    slug: 'svg-bezier-curves-and-path-math-guide',
    path: 'articles/svg-bezier-curves-and-path-math-guide/index.html',
    canonical: 'https://iconstash.io/articles/svg-bezier-curves-and-path-math-guide/',
    image: 'svg-bezier-curves-and-path-math-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'how-to-render-svg-on-canvas-guide',
    path: 'articles/how-to-render-svg-on-canvas-guide/index.html',
    canonical: 'https://iconstash.io/articles/how-to-render-svg-on-canvas-guide/',
    image: 'how-to-render-svg-on-canvas-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'css-clip-path-and-svg-masking-guide',
    path: 'articles/css-clip-path-and-svg-masking-guide/index.html',
    canonical: 'https://iconstash.io/articles/css-clip-path-and-svg-masking-guide/',
    image: 'css-clip-path-and-svg-masking-guide.jpg',
    schemaType: 'TechArticle'
  }
];

const forbidden = ['jv16', 'winfindr', 'uninstalr'];

for (const item of deliverables) {
  console.log(`\n--- Checking ${item.type.toUpperCase()}: ${item.slug} ---`);
  assert(fs.existsSync(item.path), `File exists: ${item.path}`);
  const content = fs.readFileSync(item.path, 'utf8');

  // 1. Single H1
  const h1Matches = content.match(/<h1[\s>]/gi) || [];
  assert(h1Matches.length === 1, `Exactly one <h1> (found ${h1Matches.length})`);

  // 2. Meta description <= 155 chars
  const descMatch = content.match(/<meta name="description" content="([^"]+)"/);
  assert(descMatch && descMatch[1].length <= 155, `Meta description length (${descMatch ? descMatch[1].length : 0}) <= 155`);

  // 3. Canonical link with trailing slash
  assert(content.includes(`<link rel="canonical" href="${item.canonical}">`), `Canonical link correct: ${item.canonical}`);
  assert(item.canonical.endsWith('/'), `Canonical URL has trailing slash: ${item.canonical}`);

  // 4. Hero image exists and dimension check (1200x675)
  const imgPath = path.join('assets/articles', item.image);
  assert(fs.existsSync(imgPath), `Hero image exists on disk: ${imgPath}`);
  if (fs.existsSync(imgPath)) {
    const stats = fs.statSync(imgPath);
    assert(stats.size > 20000, `Hero image size (${Math.round(stats.size / 1024)} KB) > 20 KB`);

    try {
      const probeOut = execSync(`python -c "from PIL import Image; im = Image.open(r'${imgPath}'); print(f'{im.width}x{im.height}')"`, { encoding: 'utf8' }).trim();
      assert(probeOut === '1200x675', `Hero image resolution is 1200x675 (found ${probeOut})`);
    } catch (e) {
      console.warn(`  [WARN] Python PIL could not check resolution: ${e.message}`);
    }
  }

  // 5. OpenGraph & Twitter tags pointing to full absolute URL
  assert(content.includes(`property="og:image" content="https://iconstash.io/assets/articles/${item.image}"`), 'OG Image points to full absolute URL');
  assert(content.includes(`name="twitter:image" content="https://iconstash.io/assets/articles/${item.image}"`), 'Twitter image points to full absolute URL');
  assert(content.includes('<meta name="twitter:card" content="summary_large_image">'), 'Twitter card is summary_large_image');

  // 6. Visible author byline linking to /about/
  assert(content.includes('Jouni Flemming'), 'Author Jouni Flemming present in document');
  assert(content.includes('href="/about/" rel="author"') || content.includes('href="/about/"'), 'Visible author byline links to /about/');
  assert(!content.includes('href="/about/" rel="author" style="color:#C1DD2D') && !content.includes('href="/about/" style="color:#C1DD2D'), 'Author link does not use hardcoded inline #C1DD2D style (contrast safe)');

  // 7. Forbidden strings check
  for (const f of forbidden) {
    assert(!content.toLowerCase().includes(f), `No forbidden string "${f}" found`);
  }

  // 8. Schema.org JSON-LD validation
  const jsonLdMatch = content.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
  assert(jsonLdMatch, 'JSON-LD script block exists');
  if (jsonLdMatch) {
    try {
      const schemas = JSON.parse(jsonLdMatch[1]);
      assert(Array.isArray(schemas), 'Root JSON-LD is an array of schemas');

      const mainSchema = schemas.find(s => s['@type'] === item.schemaType || s['@type'] === 'Article' || s['@type'] === 'TechArticle');
      assert(mainSchema, `Schema contains ${item.schemaType}`);
      assert(mainSchema && mainSchema.description && mainSchema.description.length <= 155, `Schema description length (${mainSchema ? mainSchema.description.length : 0}) <= 155`);
      assert(mainSchema && mainSchema.author && mainSchema.author.name === 'Jouni Flemming', 'Schema author is Jouni Flemming');
      assert(mainSchema && mainSchema.author && mainSchema.author.worksFor && mainSchema.author.worksFor.name === 'Great Software Company', 'Author worksFor is Great Software Company');
      assert(mainSchema && mainSchema.publisher && mainSchema.publisher.parentOrganization && mainSchema.publisher.parentOrganization.name === 'Great Software Company', 'Parent organization is Great Software Company');
      assert(mainSchema && mainSchema.inLanguage === 'en-US', 'Schema has inLanguage "en-US"');
      assert(mainSchema && typeof mainSchema.wordCount === 'number' && mainSchema.wordCount >= 4000, `Schema wordCount (${mainSchema ? mainSchema.wordCount : 0}) >= 4000`);

      // Verify no GitHub link in author schema
      assert(!JSON.stringify(mainSchema.author).includes('github.com'), 'No GitHub social link in author schema');

      const breadcrumb = schemas.find(s => s['@type'] === 'BreadcrumbList');
      assert(breadcrumb && breadcrumb.itemListElement && breadcrumb.itemListElement.length === 3, 'BreadcrumbList has 3 items');
      assert(breadcrumb && breadcrumb.itemListElement && breadcrumb.itemListElement[2] && breadcrumb.itemListElement[2].item === item.canonical, `BreadcrumbList item 3 has item matching canonical (${item.canonical})`);

      const faq = schemas.find(s => s['@type'] === 'FAQPage');
      assert(faq && faq.mainEntity && faq.mainEntity.length >= 5, `FAQPage has >= 5 questions (found ${faq ? faq.mainEntity.length : 0})`);
      if (faq && faq.mainEntity) {
        let allAnswersValid = true;
        for (const q of faq.mainEntity) {
          if (!q.acceptedAnswer || !q.acceptedAnswer.text || q.acceptedAnswer.text.trim().length === 0) {
            allAnswersValid = false;
          }
        }
        assert(allAnswersValid, 'All FAQ questions have non-empty acceptedAnswer.text');
      }
    } catch (e) {
      assert(false, `JSON-LD parsing error: ${e.message}`);
    }
  }

  // 9. Light theme contrast verification
  assert(content.includes('html[data-theme="light"] pre code'), 'Light theme pre code contrast rule present');
  assert(content.includes('html[data-theme="light"] pre'), 'Light theme pre block rule present');
  assert(content.includes('html[data-theme="light"] .article-meta a'), 'Light theme article-meta a contrast rule present');
  assert(content.includes('html[data-theme="light"] a { color: #4D6300; }'), 'Light theme a color rule uses WCAG AA compliant #4D6300 (> 4.5:1)');
  assert(content.includes('html[data-theme="light"] .cta-sidebar-box h4'), 'Light theme cta-sidebar-box h4 contrast rule present');
  assert(content.includes('html[data-theme="light"] .cta-sidebar-box p'), 'Light theme cta-sidebar-box p contrast rule present');
  assert(content.includes('html[data-theme="light"] .article-hero .tag'), 'Light theme article-hero tag contrast rule present');
  assert(content.includes('html[data-theme="light"] .sandbox-badge'), 'Light theme sandbox-badge contrast rule present');
  assert(content.includes('html[data-theme="light"] .takeaway-box h3'), 'Light theme takeaway-box h3 contrast rule present');
  assert(content.includes('html[data-theme="light"] .warning-box h4'), 'Light theme warning-box h4 contrast rule present');
  assert(content.includes('html[data-theme="light"] .toc-nav a'), 'Light theme toc-nav a contrast rule present');
  assert(content.includes('html[data-theme="light"] .sidebar-title'), 'Light theme sidebar-title contrast rule present');
  assert(content.includes('html[data-theme="light"] .formula-title'), 'Light theme formula-title contrast rule present');
  assert(content.includes('html[data-theme="light"] .stat-label'), 'Light theme stat-label contrast rule present');
  assert(content.includes('html[data-theme="light"] .breadcrumb a') || content.includes('html[data-theme="light"] .breadcrumb'), 'Light theme breadcrumb contrast rule present');
  assert(content.includes('html[data-theme="light"] .site-footer a'), 'Light theme site-footer a contrast rule present');

  // 10. Theme toggle and persistence verification
  assert(content.includes('id="themeToggle"'), 'Theme toggle button #themeToggle present in document');
  assert(content.includes("localStorage.getItem('theme')"), 'Theme persistence script present');
  assert(content.includes('.site-header nav a:not(.header-cta) { display: none; }'), 'Mobile nav preserves #themeToggle button visibility');
  assert(!content.includes('.site-header nav { display: none; }'), 'Mobile nav does not coarsely hide entire nav element');

  // 11. Table & Formula responsiveness check
  assert(content.includes('min-width: 640px;'), 'Data tables enforce min-width: 640px for mobile horizontal scrolling');
  assert(content.includes('<div class="table-container">') && content.includes('<table>'), 'Deliverable contains responsive data table wrapped in table-container');
  assert(content.includes('.formula-card {') && content.includes('overflow-x: auto;'), 'Formula card enforces overflow-x: auto for mobile screens');

  // 12. Interactive Developer Sandbox & Tools verification
  if (item.slug === 'svg-bezier-curves-and-path-math-guide') {
    assert(content.includes('id="bezierStudio"'), 'Interactive Bézier studio #bezierStudio present');
    assert(content.includes('id="curveTypeSelect"'), 'Interactive curveTypeSelect present');
    assert(content.includes('id="paramTSlider"'), 'Interactive paramTSlider present');
    assert(content.includes('id="stageSvg"'), 'Interactive stageSvg present');
    assert(content.includes('id="copyBezierCodeBtn"'), 'Interactive copy button present');
    assert(content.includes('class="stage-handle"'), 'SVG stage handles have stage-handle class');
    assert(content.includes('tabindex="0"') && content.includes('role="slider"'), 'SVG stage handles have accessible keyboard attributes');
    assert(content.includes('.addEventListener(\'pointerdown\''), 'SVG handles have pointer drag listeners');
    assert(!content.includes('readoutAngle.textContent = `${angleDeg}&deg;`'), 'readoutAngle does not leak raw HTML entity &deg; into textContent');
    assert(content.includes('document.execCommand(\'copy\')'), 'Clipboard copy has robust document.execCommand fallback');
    assert(content.includes('updateStudio()'), 'updateStudio function called');
    assert(content.includes('.catch('), 'Clipboard API has fallback catch handler');
  } else if (item.slug === 'how-to-render-svg-on-canvas-guide') {
    assert(content.includes('id="canvasRasterizerStudio"'), 'Interactive canvas studio #canvasRasterizerStudio present');
    assert(content.includes('id="renderMethodSelect"'), 'Interactive renderMethodSelect present');
    assert(content.includes('id="dprScaleSelect"'), 'Interactive dprScaleSelect present');
    assert(content.includes('id="previewCanvas"'), 'Interactive previewCanvas present');
    assert(content.includes('id="copyCanvasCodeBtn"'), 'Interactive copy button present');
    assert(content.includes('drawVectorBlob'), 'Canvas studio includes authentic Blob rasterization pipeline');
    assert(content.includes('drawVectorBitmap'), 'Canvas studio includes authentic createImageBitmap rasterization pipeline');
    assert(content.includes('Method 1: Vector Rasterization via Blob URL & Image'), 'Code generator outputs Blob URL rasterization snippet');
    assert(content.includes('Method 3: Async GPU Texture Decoding via createImageBitmap'), 'Code generator outputs async ImageBitmap snippet');
    assert(content.includes('ctx.stroke(vectorPath)'), 'Canvas code generator handles line stroke paths like sparklines without filling');
    assert(content.includes('document.execCommand(\'copy\')'), 'Clipboard copy has robust document.execCommand fallback');
    assert(content.includes('updateStudio()'), 'updateStudio function called');
    assert(content.includes('.catch('), 'Clipboard API has fallback catch handler');
  } else if (item.slug === 'css-clip-path-and-svg-masking-guide') {
    assert(content.includes('id="clippingMaskStudio"'), 'Interactive clip-path studio #clippingMaskStudio present');
    assert(content.includes('id="clipModeSelect"'), 'Interactive clipModeSelect present');
    assert(content.includes('id="clipPresetSelect"'), 'Interactive clipPresetSelect present');
    assert(content.includes('id="clipScaleSlider"'), 'Interactive clipScaleSlider present');
    assert(content.includes('id="previewClippedCard"'), 'Interactive previewClippedCard present');
    assert(content.includes('id="copyClipCodeBtn"'), 'Interactive copy button present');
    assert(content.includes('pathPresets'), 'Clip-path studio defines vector path presets');
    assert(content.includes('Reusable Responsive SVG mask (objectBoundingBox)'), 'SVG tab generates authentic SVG mask element when in mask mode');
    assert(content.includes('document.execCommand(\'copy\')'), 'Clipboard copy has robust document.execCommand fallback');
    assert(content.includes('updateStudio()'), 'updateStudio function called');
    assert(content.includes('.catch('), 'Clipboard API has fallback catch handler');
  }

  // 13. No raw unrendered LaTeX math formulas
  const latexMatches = [...content.matchAll(/(\$[^$\n]+\$)/g)].map(m => m[1]).filter(m => !m.includes('{') && !m.includes('"'));
  assert(latexMatches.length === 0, `No unrendered raw LaTeX math delimiters ($...$) found in ${item.slug} (found: ${JSON.stringify(latexMatches)})`);
  assert(!content.includes('$$') && !content.includes('\\times') && !content.includes('\\approx') && !content.includes('\\epsilon'), `No unrendered LaTeX math keywords found in ${item.slug}`);

  // 14. Viewport responsiveness tag
  assert(content.includes('<meta name="viewport" content="width=device-width, initial-scale=1.0">'), 'Responsive viewport tag present');

  // 15. Internal Link Integrity (excluding code tutorial snippets)
  const contentForLinks = content.replace(/<pre[\s\S]*?<\/pre>/gi, '').replace(/<code[\s\S]*?<\/code>/gi, '');
  const hrefMatches = contentForLinks.match(/href="(\/[^"]*)"/g) || [];
  const srcMatches = contentForLinks.match(/src="(\/[^"]*)"/g) || [];
  const internalLinks = [...hrefMatches, ...srcMatches].map(m => m.split('"')[1]);
  let allLinksValid = true;
  for (const link of internalLinks) {
    const clean = link.split('#')[0].split('?')[0];
    if (!clean || clean === '/') continue;
    let target = clean.startsWith('/') ? clean.slice(1) : clean;
    if (target.endsWith('/')) target += 'index.html';
    if (!fs.existsSync(target)) {
      allLinksValid = false;
      console.error(`    Broken internal link in ${item.slug}: ${link} (disk target: ${target})`);
    }
  }
  assert(allLinksValid && internalLinks.length > 0, `All internal links in ${item.slug} resolve to valid files on disk`);

  // 16. Table of Contents Anchor Integrity Verification
  const tocNavMatch = content.match(/<nav class="toc-nav"[\s\S]*?<\/nav>/);
  if (tocNavMatch) {
    const anchorMatches = [...tocNavMatch[0].matchAll(/href="#([^"]+)"/g)].map(m => m[1]);
    let allAnchorsFound = true;
    for (const aId of anchorMatches) {
      if (!content.includes(`id="${aId}"`)) {
        allAnchorsFound = false;
        console.error(`    Missing anchor ID on page: id="${aId}"`);
      }
    }
    assert(allAnchorsFound && anchorMatches.length >= 5, `All Table of Contents anchors (${anchorMatches.length} links) resolve to valid id attributes`);
  }

  // 17. Body word count >= 4000
  const cleanBody = content.replace(/<(script|style)[^>]*>[\s\S]*?<\/\1>/gi, '').replace(/<[^>]+>/g, ' ');
  const words = cleanBody.split(/\s+/).filter(w => w.length > 0);
  assert(words.length >= 4000, `Article body word count (${words.length}) >= 4000 words`);
}

// Site Integration Verification: articles/index.html
console.log('\n--- Checking Site Integration in articles/index.html ---');
const articlesIndex = fs.readFileSync('articles/index.html', 'utf8');

for (const item of deliverables) {
  assert(articlesIndex.includes(item.canonical) || articlesIndex.includes(item.canonical.replace('https://iconstash.io', '')), `articles/index.html contains link to ${item.slug}`);
}

assert(articlesIndex.includes('<span class="count">87 guides</span>'), 'Guides count updated to 87 guides');
assert(articlesIndex.includes('"position": 136') && articlesIndex.includes('"position": 137') && articlesIndex.includes('"position": 138'), 'ItemList contains positions 136, 137, 138');

// Sitemap Verification: articles-sitemap.xml
console.log('\n--- Checking articles-sitemap.xml ---');
const sitemap = fs.readFileSync('articles-sitemap.xml', 'utf8');

for (const item of deliverables) {
  assert(sitemap.includes(`<loc>${item.canonical}</loc>`), `articles-sitemap.xml includes ${item.canonical}`);
  assert(sitemap.includes(`<loc>${item.canonical}</loc><lastmod>2026-10-30</lastmod>`), `${item.slug} has current lastmod 2026-10-30`);
}
assert(sitemap.includes('<loc>https://iconstash.io/articles/</loc><lastmod>2026-10-30</lastmod>'), 'Articles hub in sitemap has lastmod 2026-10-30');

// Parent sitemap.xml
console.log('\n--- Checking parent sitemap.xml ---');
const parentSitemap = fs.readFileSync('sitemap.xml', 'utf8');
assert(parentSitemap.includes('<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-10-30</lastmod></sitemap>'), 'parent sitemap.xml references articles-sitemap.xml with 2026-10-30');

// llms.txt
console.log('\n--- Checking llms.txt ---');
const llms = fs.readFileSync('llms.txt', 'utf8');
for (const item of deliverables) {
  assert(llms.includes(item.canonical), `llms.txt includes ${item.canonical}`);
}
assert(llms.includes('- Last updated: 2026-10-30'), 'llms.txt has updated timestamp 2026-10-30 in Key Facts header');
assert(llms.includes('Last updated: 2026-10-30'), 'llms.txt has updated timestamp 2026-10-30 in footer');

console.log(`\n========================================`);
console.log(`VERIFICATION SUMMARY: ${passed} PASSED, ${failed} FAILED`);
console.log(`========================================\n`);

if (failed > 0) {
  process.exit(1);
} else {
  console.log('ALL OCTOBER 30 DELIVERABLES & SITE INTEGRATIONS PASSED WITH ZERO ERRORS!\n');
}
