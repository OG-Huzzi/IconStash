const fs = require('fs');
const path = require('path');
const vm = require('vm');
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

console.log('=== VERIFYING NOVEMBER 14, 2026 ROUND 2 DELIVERABLES & SITE INTEGRATION ===\n');

const deliverables = [
  {
    type: 'article',
    slug: 'svg-tree-diagrams-and-hierarchical-visualization-guide',
    path: 'articles/svg-tree-diagrams-and-hierarchical-visualization-guide/index.html',
    canonical: 'https://iconstash.io/articles/svg-tree-diagrams-and-hierarchical-visualization-guide/',
    image: 'svg-tree-diagrams-and-hierarchical-visualization-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'svg-circuit-diagrams-and-schematic-visualization-guide',
    path: 'articles/svg-circuit-diagrams-and-schematic-visualization-guide/index.html',
    canonical: 'https://iconstash.io/articles/svg-circuit-diagrams-and-schematic-visualization-guide/',
    image: 'svg-circuit-diagrams-and-schematic-visualization-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'svg-gantt-charts-and-project-timelines-guide',
    path: 'articles/svg-gantt-charts-and-project-timelines-guide/index.html',
    canonical: 'https://iconstash.io/articles/svg-gantt-charts-and-project-timelines-guide/',
    image: 'svg-gantt-charts-and-project-timelines-guide.jpg',
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
  const descMatch = content.match(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i);
  assert(descMatch && descMatch[1].length > 0 && descMatch[1].length <= 155,
    `Meta description valid length (${descMatch ? descMatch[1].length : 0} chars, <= 155): "${descMatch ? descMatch[1] : ''}"`);

  // 3. Canonical URL
  const canonMatch = content.match(/<link\s+rel=["']canonical["']\s+href=["'](.*?)["']/i);
  assert(canonMatch && canonMatch[1] === item.canonical,
    `Canonical matches exactly (${canonMatch ? canonMatch[1] : 'none'})`);

  // 4. Hero image check
  const imgPath = path.join('assets/articles', item.image);
  assert(fs.existsSync(imgPath), `Hero image file exists: ${imgPath}`);
  if (fs.existsSync(imgPath)) {
    const stats = fs.statSync(imgPath);
    assert(stats.size > 20000, `Hero image size > 20KB (${Math.round(stats.size / 1024)} KB)`);
  }

  // 5. Schema checks: TechArticle, BreadcrumbList, FAQPage
  const schemas = content.match(/<script\s+type=["']application\/ld\+json["']>([\s\S]*?)<\/script>/gi) || [];
  let foundTechArticle = false;
  let foundBreadcrumb = false;
  let foundFAQ = false;

  schemas.forEach(sTag => {
    const rawJson = sTag.replace(/<script[^>]*>|<\/script>/gi, '').trim();
    try {
      const parsed = JSON.parse(rawJson);
      if (parsed['@type'] === 'TechArticle') {
        foundTechArticle = true;
        assert(parsed.headline && parsed.description && parsed.author, 'TechArticle has headline, description, author');
      }
      if (parsed['@type'] === 'BreadcrumbList') {
        foundBreadcrumb = true;
        assert(Array.isArray(parsed.itemListElement) && parsed.itemListElement.length >= 3, 'BreadcrumbList has valid items');
      }
      if (parsed['@type'] === 'FAQPage') {
        foundFAQ = true;
        assert(Array.isArray(parsed.mainEntity) && parsed.mainEntity.length >= 5, `FAQPage has ${parsed.mainEntity ? parsed.mainEntity.length : 0} items (>= 5)`);
      }
    } catch (e) {
      assert(false, `Malformed JSON-LD schema: ${e.message}`);
    }
  });

  assert(foundTechArticle, 'Found valid TechArticle schema');
  assert(foundBreadcrumb, 'Found valid BreadcrumbList schema');
  assert(foundFAQ, 'Found valid FAQPage schema');

  // 6. Author byline & Publisher
  assert(content.includes('Jouni Flemming') && content.includes('/about/'), 'Author byline mentions Jouni Flemming with link to /about/');
  assert(content.includes('Great Software Company') && content.includes('https://greatsoftwarecompany.com'), 'Publisher mentions Great Software Company');

  // 7. Word count check (Pure prose > 4000)
  const cleanBody = content.replace(/<(script|style)[^>]*>[\s\S]*?<\/\1>/gi, '').replace(/<[^>]+>/g, ' ');
  const totalWords = cleanBody.split(/\s+/).filter(Boolean).length;
  assert(totalWords > 4500, `Total word count > 4500 (found ${totalWords})`);

  const artMatch = content.match(/<article[^>]*class=["'][^"']*article-main[^"']*["'][\s\S]*?<\/article>/i);
  if (artMatch) {
    const pureProse = artMatch[0].replace(/<(script|style|svg|pre)[^>]*>[\s\S]*?<\/\1>/gi, ' ').replace(/<[^>]+>/g, ' ');
    const pureWords = pureProse.split(/\s+/).filter(Boolean).length;
    assert(pureWords >= 4000, `Pure prose word count >= 4000 (found ${pureWords})`);
  } else {
    assert(false, 'Could not find <article class="article-main"> for prose word count');
  }

  // 8. Strict Brand Safety: zero forbidden words
  forbidden.forEach(word => {
    const regex = new RegExp(`\\b${word}\\b`, 'i');
    assert(!regex.test(content), `Strict Brand Safety: Zero mentions of "${word}"`);
  });

  // 9. Figure 2 Vector Architectural Diagram
  assert(content.includes('viewBox="0 0 960 320"') || content.includes('viewBox="0 0 960 360"'), 'Figure 2 dedicated 960px vector architecture diagram present');

  // 10. Check that client-side JS evaluates without syntax errors
  const clientScripts = content.match(/<script>(?![\s\S]*application\/ld\+json)([\s\S]*?)<\/script>/gi) || [];
  clientScripts.forEach((sc, idx) => {
    const code = sc.replace(/<script>|<\/script>/gi, '');
    try {
      new vm.Script(code);
      assert(true, `Client-side script #${idx + 1} syntax is valid (no parse errors)`);
    } catch (e) {
      assert(false, `Client-side script #${idx + 1} has syntax error: ${e.message}`);
    }
  });
}

// Global Site Integration Checks
console.log('\n--- Checking Global Site Integration ---');

// 1. articles/index.html
const indexContent = fs.readFileSync('articles/index.html', 'utf8');
assert(indexContent.includes('114 guides'), 'articles/index.html counter updated to 114 guides');
deliverables.forEach(d => {
  assert(indexContent.includes(`/articles/${d.slug}/`), `articles/index.html links to /articles/${d.slug}/`);
  assert(indexContent.includes(d.canonical), `articles/index.html ItemList schema includes ${d.canonical}`);
});

// 2. articles-sitemap.xml
const sitemapContent = fs.readFileSync('articles-sitemap.xml', 'utf8');
deliverables.forEach(d => {
  assert(sitemapContent.includes(`<loc>${d.canonical}</loc>`), `articles-sitemap.xml includes ${d.canonical}`);
});
assert(sitemapContent.includes('<lastmod>2026-11-14</lastmod>'), 'articles-sitemap.xml lastmod is 2026-11-14');

// 3. sitemap.xml
const rootSitemap = fs.readFileSync('sitemap.xml', 'utf8');
assert(rootSitemap.includes('<loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-14</lastmod>'), 'sitemap.xml points to articles-sitemap.xml with lastmod 2026-11-14');

// 4. llms.txt
const llmsContent = fs.readFileSync('llms.txt', 'utf8');
deliverables.forEach(d => {
  assert(llmsContent.includes(d.canonical), `llms.txt includes ${d.canonical}`);
});
assert(llmsContent.includes('Last updated: 2026-11-14'), 'llms.txt timestamp is 2026-11-14');

console.log(`\n========================================`);
console.log(`VERIFICATION SUMMARY: ${passed} PASSED, ${failed} FAILED`);
console.log(`========================================`);

if (failed > 0) {
  process.exit(1);
}
