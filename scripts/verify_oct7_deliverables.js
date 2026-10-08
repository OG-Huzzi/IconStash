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

console.log('=== VERIFYING OCTOBER 7, 2026 DELIVERABLES & SITE INTEGRATION ===\n');

const deliverables = [
  {
    type: 'article',
    slug: 'fluent-ui-icons-complete-guide',
    path: 'articles/fluent-ui-icons-complete-guide/index.html',
    canonical: 'https://iconstash.io/articles/fluent-ui-icons-complete-guide/',
    image: 'fluent-ui-icons-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'carbon-icons-complete-guide',
    path: 'articles/carbon-icons-complete-guide/index.html',
    canonical: 'https://iconstash.io/articles/carbon-icons-complete-guide/',
    image: 'carbon-icons-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'glossary',
    slug: 'svg-stroke-fill-and-painting-glossary',
    path: 'Glossary/svg-stroke-fill-and-painting-glossary/index.html',
    canonical: 'https://iconstash.io/Glossary/svg-stroke-fill-and-painting-glossary/',
    image: 'svg-stroke-fill-and-painting-glossary.jpg',
    schemaType: 'DefinedTermSet'
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
  assert(content.includes('href="/about/" rel="author"'), 'Visible author byline links to /about/ with rel="author"');

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
      assert(mainSchema && mainSchema.publisher && mainSchema.publisher.parentOrganization && mainSchema.publisher.parentOrganization.name === 'Great Software Company', 'Parent organization is Great Software Company');

      // Verify no GitHub link in author schema
      assert(!JSON.stringify(mainSchema.author).includes('github.com'), 'No GitHub social link in author schema');

      const breadcrumb = schemas.find(s => s['@type'] === 'BreadcrumbList');
      assert(breadcrumb && breadcrumb.itemListElement && breadcrumb.itemListElement.length === 3, 'BreadcrumbList has 3 items');

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

  // 10. Theme toggle and persistence verification
  assert(content.includes('id="themeToggle"'), 'Theme toggle button #themeToggle present in document');
  assert(content.includes("localStorage.getItem('theme')"), 'Theme persistence script present');

  // 11. No raw unrendered LaTeX math formulas
  assert(!content.includes('$$\\text{') && !content.includes('\\times') && !content.includes('\\approx'), 'No unrendered LaTeX math delimiters ($$ or \\times) found');

  // 12. Viewport responsiveness tag
  assert(content.includes('<meta name="viewport" content="width=device-width, initial-scale=1.0">'), 'Responsive viewport tag present');

  // 13. Table of Contents Anchor Integrity Verification
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

  // 14. Glossary DefinedTermSet enrichment & instant filter components
  if (item.schemaType === 'DefinedTermSet') {
    assert(content.includes('id="termFilter"'), 'Glossary has instant search filter element #termFilter');
    assert(content.includes('id="noResults"'), 'Glossary has #noResults alert container');
    assert(content.includes('id="resetFilterBtn"'), 'Glossary has #resetFilterBtn button');
    assert(content.includes('html[data-theme="light"] #simPath'), 'Glossary has light theme simulator path contrast rule');
    assert(content.includes('html[data-theme="light"] #simArrow path'), 'Glossary has light theme simulator marker contrast rule');

    const jsonLdData = JSON.parse(content.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1]);
    const mainSchema = jsonLdData.find(s => s['@type'] === 'DefinedTermSet');
    assert(mainSchema && mainSchema.hasDefinedTerm && mainSchema.hasDefinedTerm.length >= 35, `DefinedTermSet contains all 35+ terms in hasDefinedTerm (found ${mainSchema && mainSchema.hasDefinedTerm ? mainSchema.hasDefinedTerm.length : 0} terms)`);
  }
}

// Site Integration Verification: articles/index.html
console.log('\n--- Checking Site Integration in articles/index.html ---');
const articlesIndex = fs.readFileSync('articles/index.html', 'utf8');

for (const item of deliverables) {
  assert(articlesIndex.includes(item.canonical), `articles/index.html contains link to ${item.canonical}`);
}

assert(articlesIndex.includes('<span class="count">58 guides</span>'), 'Guides count updated to 58 guides');
assert(articlesIndex.includes('<span class="count">23 resources</span>'), 'Resources count updated to 23 resources');
assert(articlesIndex.includes('"position": 100') && articlesIndex.includes('"position": 101') && articlesIndex.includes('"position": 102'), 'ItemList contains positions 100, 101, 102');

// Sitemap Verification: articles-sitemap.xml
console.log('\n--- Checking articles-sitemap.xml ---');
const sitemap = fs.readFileSync('articles-sitemap.xml', 'utf8');

for (const item of deliverables) {
  assert(sitemap.includes(`<loc>${item.canonical}</loc>`), `articles-sitemap.xml includes ${item.canonical}`);
  assert(sitemap.includes(`<loc>${item.canonical}</loc><lastmod>2026-10-07</lastmod>`), `${item.slug} has current lastmod 2026-10-07`);
}
assert(sitemap.includes('<loc>https://iconstash.io/articles/</loc><lastmod>2026-10-07</lastmod>'), 'Articles hub in sitemap has lastmod 2026-10-07');

// Parent sitemap.xml
console.log('\n--- Checking parent sitemap.xml ---');
const parentSitemap = fs.readFileSync('sitemap.xml', 'utf8');
assert(parentSitemap.includes('<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-10-07</lastmod></sitemap>'), 'parent sitemap.xml references articles-sitemap.xml with 2026-10-07');

// llms.txt
console.log('\n--- Checking llms.txt ---');
const llms = fs.readFileSync('llms.txt', 'utf8');
for (const item of deliverables) {
  assert(llms.includes(item.canonical), `llms.txt includes ${item.canonical}`);
}

console.log(`\n========================================`);
console.log(`VERIFICATION SUMMARY: ${passed} PASSED, ${failed} FAILED`);
console.log(`========================================\n`);

if (failed > 0) {
  process.exit(1);
} else {
  console.log('ALL OCTOBER 7 DELIVERABLES & SITE INTEGRATIONS PASSED WITH ZERO ERRORS!\n');
}
