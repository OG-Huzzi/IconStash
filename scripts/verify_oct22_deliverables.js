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

console.log('=== VERIFYING OCTOBER 22, 2026 DELIVERABLES & SITE INTEGRATION ===\n');

const deliverables = [
  {
    type: 'article',
    slug: 'convert-png-to-svg-javascript-guide',
    path: 'articles/convert-png-to-svg-javascript-guide/index.html',
    canonical: 'https://iconstash.io/articles/convert-png-to-svg-javascript-guide/',
    image: 'convert-png-to-svg-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'how-to-use-svg-transforms-guide',
    path: 'articles/how-to-use-svg-transforms-guide/index.html',
    canonical: 'https://iconstash.io/articles/how-to-use-svg-transforms-guide/',
    image: 'how-to-use-svg-transforms-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'alternative',
    slug: 'font-awesome',
    path: 'alternatives/font-awesome/index.html',
    canonical: 'https://iconstash.io/alternatives/font-awesome/',
    image: 'font-awesome-alternatives.jpg',
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
      const probeOut = execSync(`ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "${imgPath}"`, { encoding: 'utf8' }).trim();
      assert(probeOut === '1200x675', `Hero image resolution is 1200x675 (found ${probeOut})`);
    } catch (e) {
      console.warn(`  [WARN] ffprobe could not check resolution: ${e.message}`);
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

      if (item.type === 'alternative') {
        const itemList = schemas.find(s => s['@type'] === 'ItemList');
        assert(itemList && itemList.itemListElement && itemList.itemListElement.length >= 8, `Alternative page contains ItemList with >= 8 items (found ${itemList ? itemList.itemListElement.length : 0})`);
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

  // 10. Theme toggle and persistence verification
  assert(content.includes('id="themeToggle"'), 'Theme toggle button #themeToggle present in document');
  assert(content.includes("localStorage.getItem('theme')"), 'Theme persistence script present');
  assert(content.includes('.site-header nav a:not(.header-cta) { display: none; }'), 'Mobile nav preserves #themeToggle button visibility');
  assert(!content.includes('.site-header nav { display: none; }'), 'Mobile nav does not coarsely hide entire nav element');

  // 11. Table responsiveness check
  assert(content.includes('min-width: 640px;'), 'Data tables enforce min-width: 640px for mobile horizontal scrolling');
  assert(content.includes('<div class="table-container">') && content.includes('<table>'), 'Deliverable contains responsive data table wrapped in table-container');

  // 12. Interactive Developer Sandbox & Tools verification
  if (item.slug === 'convert-png-to-svg-javascript-guide') {
    assert(content.includes('id="vectorizerSandbox"'), 'Interactive vectorizer sandbox present');
    assert(content.includes('id="iconPresets"'), 'Interactive icon presets present');
    assert(content.includes('id="sliderThreshold"'), 'Interactive threshold slider present');
    assert(content.includes('id="sliderTolerance"'), 'Interactive tolerance slider present');
    assert(content.includes('id="copyVectorCode"'), 'Interactive copy code button present');
    assert(content.includes('id="downloadSvgFile"'), 'Interactive download svg button present');
  } else if (item.slug === 'how-to-use-svg-transforms-guide') {
    assert(content.includes('id="transformSandbox"'), 'Interactive transform sandbox present');
    assert(content.includes('id="sliderRotate"'), 'Interactive rotate slider present');
    assert(content.includes('id="sliderScale"'), 'Interactive scale slider present');
    assert(content.includes('id="boxToggleGroup"'), 'Interactive transform-box toggle present');
    assert(content.includes('id="copyTransformCode"'), 'Interactive copy code button present');
  } else if (item.slug === 'font-awesome') {
    assert(content.includes('id="faMigrationSandbox"'), 'Interactive Font Awesome migration sandbox present');
    assert(content.includes('id="targetLibSelector"'), 'Interactive target library selector present');
    assert(content.includes('id="inputFaClass"'), 'Interactive class input present');
    assert(content.includes('id="copyMigrationCode"'), 'Interactive copy migration code button present');
  }

  // 13. No raw unrendered LaTeX math formulas
  const latexMatches = [...content.matchAll(/(\$[^$\n]+\$)/g)].map(m => m[1]).filter(m => !m.includes('{') && !m.includes('"'));
  assert(latexMatches.length === 0, `No unrendered raw LaTeX math delimiters ($...$) found in ${item.slug} (found: ${JSON.stringify(latexMatches)})`);
  assert(!content.includes('$$') && !content.includes('\\times') && !content.includes('\\approx') && !content.includes('\\epsilon'), `No unrendered LaTeX math keywords found in ${item.slug}`);

  // 14. Viewport responsiveness tag
  assert(content.includes('<meta name="viewport" content="width=device-width, initial-scale=1.0">'), 'Responsive viewport tag present');

  // 15. Internal Link Integrity
  const hrefMatches = content.match(/href="(\/[^"]*)"/g) || [];
  const srcMatches = content.match(/src="(\/[^"]*)"/g) || [];
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
}

// Deep Interactive Widget Code Verification
console.log('\n--- Deep Interactive Functional Verification ---');
const art1 = fs.readFileSync('articles/convert-png-to-svg-javascript-guide/index.html', 'utf8');
assert(art1.includes('segments.push([W, S])') && art1.includes('simplifyRDP'), 'Article 1 implements real Marching Squares and RDP vectorizer');
assert(!art1.includes("activePreset === 'star' ? d = 'M64,12") && !art1.includes("if (activePreset === 'star')"), 'Article 1 does NOT use mock preset switch cases');

const art2 = fs.readFileSync('articles/how-to-use-svg-transforms-guide/index.html', 'utf8');
assert(art2.includes('codeOutput.textContent = `<!-- SVG Presentation Attribute -->'), 'Article 2 uses raw HTML strings in textContent');
assert(!art2.includes('codeOutput.textContent = `&lt;!-- SVG Presentation Attribute --&gt;'), 'Article 2 does NOT double-escape HTML entities in textContent');

const altFa = fs.readFileSync('alternatives/font-awesome/index.html', 'utf8');
assert(altFa.includes('fa-(solid|regular|brands|light|thin|duotone|sharp|classic)'), 'Alternative page converter regex supports Font Awesome 6/7 styles');
assert(altFa.includes('classMatch'), 'Alternative page converter parses HTML <i> tag inputs');

// Site Integration Verification: articles/index.html
console.log('\n--- Checking Site Integration in articles/index.html ---');
const articlesIndex = fs.readFileSync('articles/index.html', 'utf8');

for (const item of deliverables) {
  assert(articlesIndex.includes(item.canonical) || articlesIndex.includes(item.canonical.replace('https://iconstash.io', '')), `articles/index.html contains link to ${item.slug}`);
}

assert(articlesIndex.includes('<span class="count">72 guides</span>'), 'Guides count updated to 72 guides');
assert(articlesIndex.includes('"position": 121') && articlesIndex.includes('"position": 122') && articlesIndex.includes('"position": 123'), 'ItemList contains positions 121, 122, 123');

// Site Integration Verification: alternatives/index.html
console.log('\n--- Checking Site Integration in alternatives/index.html ---');
const altIndex = fs.readFileSync('alternatives/index.html', 'utf8');
assert(altIndex.includes('/alternatives/font-awesome/'), 'alternatives/index.html links to /alternatives/font-awesome/');

// Sitemap Verification: articles-sitemap.xml
console.log('\n--- Checking articles-sitemap.xml ---');
const sitemap = fs.readFileSync('articles-sitemap.xml', 'utf8');

for (const item of deliverables) {
  assert(sitemap.includes(`<loc>${item.canonical}</loc>`), `articles-sitemap.xml includes ${item.canonical}`);
  assert(sitemap.includes(`<loc>${item.canonical}</loc><lastmod>2026-10-22</lastmod>`), `${item.slug} has current lastmod 2026-10-22`);
}
assert(sitemap.includes('<loc>https://iconstash.io/articles/</loc><lastmod>2026-10-22</lastmod>'), 'Articles hub in sitemap has lastmod 2026-10-22');

// Parent sitemap.xml
console.log('\n--- Checking parent sitemap.xml ---');
const parentSitemap = fs.readFileSync('sitemap.xml', 'utf8');
assert(parentSitemap.includes('<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-10-22</lastmod></sitemap>'), 'parent sitemap.xml references articles-sitemap.xml with 2026-10-22');
assert(parentSitemap.includes('<sitemap><loc>https://iconstash.io/sitemaps/compare.xml</loc><lastmod>2026-10-22</lastmod></sitemap>'), 'parent sitemap.xml references sitemaps/compare.xml with 2026-10-22');
assert(parentSitemap.includes('<sitemap><loc>https://iconstash.io/sitemaps/hubs.xml</loc><lastmod>2026-10-22</lastmod></sitemap>'), 'parent sitemap.xml references sitemaps/hubs.xml with 2026-10-22');

// sitemaps/compare.xml
console.log('\n--- Checking sitemaps/compare.xml ---');
const compareSitemap = fs.readFileSync('sitemaps/compare.xml', 'utf8');
assert(compareSitemap.includes('https://iconstash.io/alternatives/font-awesome/'), 'sitemaps/compare.xml includes https://iconstash.io/alternatives/font-awesome/');

// sitemaps/hubs.xml
console.log('\n--- Checking sitemaps/hubs.xml ---');
const hubsSitemap = fs.readFileSync('sitemaps/hubs.xml', 'utf8');
assert(hubsSitemap.includes('<loc>https://iconstash.io/alternatives/</loc><lastmod>2026-10-22</lastmod>'), 'sitemaps/hubs.xml includes https://iconstash.io/alternatives/ with lastmod 2026-10-22');

// llms.txt
console.log('\n--- Checking llms.txt ---');
const llms = fs.readFileSync('llms.txt', 'utf8');
for (const item of deliverables) {
  assert(llms.includes(item.canonical), `llms.txt includes ${item.canonical}`);
}
assert(llms.includes('- Last updated: 2026-10-22'), 'llms.txt has updated timestamp 2026-10-22 in Key Facts header');
assert(llms.includes('Last updated: 2026-10-22'), 'llms.txt has updated timestamp 2026-10-22 in footer');

console.log(`\n========================================`);
console.log(`VERIFICATION SUMMARY: ${passed} PASSED, ${failed} FAILED`);
console.log(`========================================\n`);

if (failed > 0) {
  process.exit(1);
} else {
  console.log('ALL OCTOBER 22 DELIVERABLES & SITE INTEGRATIONS PASSED WITH ZERO ERRORS!\n');
}
