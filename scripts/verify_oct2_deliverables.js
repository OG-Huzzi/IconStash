const fs = require('fs');
const path = require('path');

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

console.log('=== VERIFYING OCTOBER 2, 2026 DELIVERABLES & SITE INTEGRATION ===\n');

const deliverables = [
  {
    type: 'article',
    slug: 'remix-icons-complete-guide',
    path: 'articles/remix-icons-complete-guide/index.html',
    canonical: 'https://iconstash.io/articles/remix-icons-complete-guide/',
    image: 'remix-icons-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'how-to-create-animated-svg-loading-spinner-guide',
    path: 'articles/how-to-create-animated-svg-loading-spinner-guide/index.html',
    canonical: 'https://iconstash.io/articles/how-to-create-animated-svg-loading-spinner-guide/',
    image: 'svg-loading-spinner-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'glossary',
    slug: 'svg-typography-and-font-glyphs-glossary',
    path: 'Glossary/svg-typography-and-font-glyphs-glossary/index.html',
    canonical: 'https://iconstash.io/Glossary/svg-typography-and-font-glyphs-glossary/',
    image: 'svg-typography-and-font-glyphs-glossary.jpg',
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

  // 3. Canonical link
  assert(content.includes(`<link rel="canonical" href="${item.canonical}">`), `Canonical link correct: ${item.canonical}`);

  // 4. Hero image exists
  const imgPath = path.join('assets/articles', item.image);
  assert(fs.existsSync(imgPath), `Hero image exists on disk: ${imgPath}`);
  if (fs.existsSync(imgPath)) {
    const stats = fs.statSync(imgPath);
    assert(stats.size > 20000, `Hero image size (${Math.round(stats.size / 1024)} KB) > 20 KB`);
  }

  // 5. OpenGraph & Twitter tags
  assert(content.includes(`content="https://iconstash.io/assets/articles/${item.image}"`), 'OG Image points to full absolute URL');
  assert(content.includes('<meta name="twitter:card" content="summary_large_image">'), 'Twitter card is summary_large_image');

  // 6. Author attribution
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

  // 13. Glossary DefinedTermSet enrichment
  if (item.schemaType === 'DefinedTermSet') {
    const mainSchema = JSON.parse(content.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1]).find(s => s['@type'] === 'DefinedTermSet');
    assert(mainSchema && mainSchema.hasDefinedTerm && mainSchema.hasDefinedTerm.length >= 8, `DefinedTermSet contains hasDefinedTerm array (found ${mainSchema && mainSchema.hasDefinedTerm ? mainSchema.hasDefinedTerm.length : 0} terms)`);
  }
}

// 10. Site Integration Verification: articles/index.html
console.log('\n--- Checking Site Integration in articles/index.html ---');
const articlesIndex = fs.readFileSync('articles/index.html', 'utf8');

for (const item of deliverables) {
  assert(articlesIndex.includes(item.canonical), `articles/index.html contains link to ${item.canonical}`);
}

assert(articlesIndex.includes('<span class="count">54 guides</span>'), 'Guides count updated to 54 guides');
assert(articlesIndex.includes('<span class="count">21 resources</span>'), 'Resources count updated to 21 resources');
assert(articlesIndex.includes('"position": 94') && articlesIndex.includes('"position": 95') && articlesIndex.includes('"position": 96'), 'ItemList contains positions 94, 95, 96');

// 11. Sitemap Verification: articles-sitemap.xml
console.log('\n--- Checking articles-sitemap.xml ---');
const sitemap = fs.readFileSync('articles-sitemap.xml', 'utf8');

for (const item of deliverables) {
  assert(sitemap.includes(`<loc>${item.canonical}</loc>`), `articles-sitemap.xml includes ${item.canonical}`);
  assert(sitemap.includes(`<loc>${item.canonical}</loc><lastmod>2026-10-02</lastmod>`), `${item.slug} has current lastmod 2026-10-02`);
}
assert(sitemap.includes('<loc>https://iconstash.io/articles/</loc><lastmod>2026-10-02</lastmod>'), 'Articles hub in sitemap has lastmod 2026-10-02');

// 12. Parent sitemap.xml
console.log('\n--- Checking parent sitemap.xml ---');
const parentSitemap = fs.readFileSync('sitemap.xml', 'utf8');
assert(parentSitemap.includes('<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-10-02</lastmod></sitemap>'), 'parent sitemap.xml references articles-sitemap.xml with 2026-10-02');

// 13. llms.txt
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
  console.log('ALL CHECKS PASSED PERFECTLY!');
  process.exit(0);
}
