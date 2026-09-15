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

console.log('=== VERIFYING SEPTEMBER 15, 2026 DELIVERABLES & SITE INTEGRATION ===\n');

const deliverables = [
  {
    type: 'article',
    slug: 'how-to-make-svg-responsive-guide',
    path: 'articles/how-to-make-svg-responsive-guide/index.html',
    canonical: 'https://iconstash.io/articles/how-to-make-svg-responsive-guide/',
    image: 'responsive-svg-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'phosphor-icons-complete-guide',
    path: 'articles/phosphor-icons-complete-guide/index.html',
    canonical: 'https://iconstash.io/articles/phosphor-icons-complete-guide/',
    image: 'phosphor-icons-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'listicle',
    slug: 'best-duotone-icon-packs',
    path: 'Listicles/best-duotone-icon-packs/index.html',
    canonical: 'https://iconstash.io/Listicles/best-duotone-icon-packs/',
    image: 'best-duotone-icon-packs.jpg',
    schemaType: 'Article',
    isListicle: true
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

  // 3. Canonical tag
  assert(content.includes(`<link rel="canonical" href="${item.canonical}">`), `Canonical tag matches ${item.canonical}`);

  // 4. Visible author byline
  assert(content.includes('By <a href="/about/" rel="author">Jouni Flemming</a>'), `Visible author byline is present linking to /about/`);

  // 5. Open Graph, Twitter & Hero Figure
  const expectedImgUrl = `https://iconstash.io/assets/articles/${item.image}`;
  const assetPath = path.join('assets/articles', item.image);
  assert(fs.existsSync(assetPath), `Hero image exists on disk: ${assetPath}`);
  assert(content.includes(`property="og:image" content="${expectedImgUrl}"`), `OG image is ${item.image}`);
  assert(content.includes(`name="twitter:image" content="${expectedImgUrl}"`), `Twitter image is ${item.image}`);
  assert(content.includes('property="og:image:width" content="1200"'), `OG width is 1200`);
  assert(content.includes('property="og:image:height" content="675"'), `OG height is 675`);
  assert(content.includes(`<img src="/assets/articles/${item.image}"`), `Content includes hero figure image`);

  // 6. Zero forbidden words
  for (const f of forbidden) {
    assert(!content.toLowerCase().includes(f), `Contains zero mentions of forbidden word "${f}"`);
  }

  // 7. Rich content elements: code blocks, tables, responsive containers
  assert(content.includes('<pre><code') && content.includes('</code></pre>'), `Contains code blocks`);
  assert(!content.includes('<code><svg'), `Properly escapes &lt;svg&gt; inside code tags`);
  assert(content.includes('<table') && content.includes('</table>'), `Contains data table`);
  assert(content.includes('.table-wrap') || content.includes('overflow-x: auto'), `Table has responsive overflow container`);
  assert(content.includes('min-width: 600px'), `Table has min-width: 600px`);

  // 8. JSON-LD validation
  let data;
  const jsonMatch = content.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
  assert(!!jsonMatch, `Has JSON-LD structured data script`);
  if (jsonMatch) {
    try {
      data = JSON.parse(jsonMatch[1]);
      assert(true, `JSON-LD parses as valid JSON`);
    } catch (e) {
      assert(false, `JSON-LD parsing error: ${e.message}`);
    }

    if (data) {
      const mainSchema = data.find(d => d['@type'] === item.schemaType);
      assert(!!mainSchema, `${item.schemaType} schema present`);
      if (mainSchema) {
        assert(mainSchema.description && mainSchema.description.length <= 155, `Schema description (${mainSchema.description.length}) <= 155 chars`);
        assert(mainSchema.author && mainSchema.author.name === 'Jouni Flemming', `Schema author is Jouni Flemming`);
        assert(mainSchema.author && mainSchema.author.url === 'https://iconstash.io/about/', `Schema author URL is https://iconstash.io/about/`);
        assert(!JSON.stringify(mainSchema.author).includes('github.com'), `Schema author does not contain github.com`);
        assert(mainSchema.image === expectedImgUrl, `Schema image matches ${expectedImgUrl}`);
        assert(mainSchema.publisher && mainSchema.publisher.name === 'IconStash', `Schema publisher is IconStash`);
        assert(mainSchema.publisher && mainSchema.publisher.parentOrganization && mainSchema.publisher.parentOrganization.name === 'Great Software Company', `Schema parentOrganization is Great Software Company`);
        assert(mainSchema.publisher.parentOrganization.url === 'https://greatsoftwarecompany.com', `Schema parentOrganization URL is https://greatsoftwarecompany.com`);
        if (mainSchema.mainEntityOfPage) {
          assert(mainSchema.mainEntityOfPage === item.canonical, `mainEntityOfPage matches canonical URL`);
        }
      }

      if (item.isListicle) {
        const itemListSchema = data.find(d => d['@type'] === 'ItemList');
        assert(!!itemListSchema, `ItemList schema present for listicle`);
        if (itemListSchema) {
          assert(itemListSchema.numberOfItems === 12, `ItemList has 12 items (found ${itemListSchema.numberOfItems})`);
          assert(itemListSchema.itemListElement && itemListSchema.itemListElement.length === 12, `itemListElement has 12 entries`);
          for (const it of itemListSchema.itemListElement) {
            assert(it.position >= 1 && it.position <= 12, `Position ${it.position} in range`);
            assert(it.url && it.url.startsWith('https://iconstash.io/library/'), `Item URL points to library: ${it.url}`);
          }
        }
      }

      const faqSchema = data.find(d => d['@type'] === 'FAQPage');
      assert(!!faqSchema, `FAQPage schema present`);
      if (faqSchema) {
        assert(faqSchema.mainEntity && faqSchema.mainEntity.length >= 3, `FAQ has >= 3 questions (found ${faqSchema.mainEntity ? faqSchema.mainEntity.length : 0})`);
        for (const q of faqSchema.mainEntity) {
          assert(!!q.acceptedAnswer && !q.answer, `FAQ question "${q.name.substring(0, 30)}..." uses acceptedAnswer`);
        }
      }

      const breadcrumbSchema = data.find(d => d['@type'] === 'BreadcrumbList');
      assert(!!breadcrumbSchema, `BreadcrumbList schema present`);
      if (breadcrumbSchema) {
        assert(breadcrumbSchema.itemListElement && breadcrumbSchema.itemListElement.length === 3, `Breadcrumbs have 3 levels`);
        for (const b of breadcrumbSchema.itemListElement) {
          assert(!!b.item, `Breadcrumb position ${b.position} has full item URL: ${b.item}`);
        }
      }
    }
  }

  // 9. Responsive layout & theme support
  assert(content.includes('viewport') && content.includes('width=device-width'), `Includes mobile viewport tag`);
  assert(content.includes('@media (max-width: 768px)'), `Includes mobile media queries`);
  assert(content.includes('html[data-theme="light"]'), `Includes light theme CSS`);
  assert(content.includes('html[data-theme="light"] pre code'), `Includes light theme pre code CSS`);
  assert(content.includes('themeToggle'), `Includes theme toggle logic`);
  assert(content.includes('margin-top: 0') && content.includes('.site-footer'), `Footer has margin-top: 0 to eliminate empty space gap`);
  assert(content.includes('.header-cta') && content.includes('display: inline-block;'), `Header CTA has display: inline-block`);
  assert(content.includes('nav a:not(.header-cta)'), `Mobile header nav preserves Open App CTA button`);

  // 10. Check all internal links resolve to real files or directories
  const linkRegex = /href="(\/[^"#?]*)"/g;
  let match;
  while ((match = linkRegex.exec(content)) !== null) {
    const rawPath = match[1];
    if (rawPath === '/' || rawPath === '') continue;
    const relPath = rawPath.replace(/^\//, '');
    const directExists = fs.existsSync(relPath);
    const indexExists = fs.existsSync(path.join(relPath, 'index.html'));
    assert(directExists || indexExists, `Internal link "${rawPath}" exists on disk`);
  }
}

// 11. Site integration checks
console.log('\n--- Checking Site Integration ---');
const articlesIndex = fs.readFileSync('articles/index.html', 'utf8');
const articlesSitemap = fs.readFileSync('articles-sitemap.xml', 'utf8');
const sitemapXml = fs.readFileSync('sitemap.xml', 'utf8');
const llmsTxt = fs.readFileSync('llms.txt', 'utf8');

// Section counts check in articles/index.html
const sections = articlesIndex.split('<div class="section-head">');
sections.shift();
for (const sec of sections) {
  const titleMatch = sec.match(/<h2>(.*?)<\/h2>/);
  const countMatch = sec.match(/<span class="count">(\d+)\s+[^<]+<\/span>/);
  const title = titleMatch ? titleMatch[1] : 'Unknown';
  if (countMatch) {
    const claimed = parseInt(countMatch[1], 10);
    const gridStart = sec.indexOf('<div class="grid">');
    const gridEnd = sec.indexOf('</div>\n\n');
    const gridContent = gridStart !== -1 ? sec.slice(gridStart, gridEnd !== -1 ? gridEnd : undefined) : '';
    const actual = (gridContent.match(/<a class="card/g) || []).length;
    assert(claimed === actual, `Section "${title}" claimed count (${claimed}) matches actual cards (${actual})`);
  }
}

for (const item of deliverables) {
  if (item.type === 'article') {
    assert(articlesIndex.includes(`/articles/${item.slug}/`), `articles/index.html links to ${item.slug}`);
    assert(articlesSitemap.includes(`https://iconstash.io/articles/${item.slug}/`), `articles-sitemap.xml includes ${item.slug}`);
    assert(llmsTxt.includes(`https://iconstash.io/articles/${item.slug}/`), `llms.txt includes ${item.slug}`);
  } else {
    assert(articlesIndex.includes(`/Listicles/${item.slug}/`), `articles/index.html links to ${item.slug}`);
    assert(articlesSitemap.includes(`https://iconstash.io/Listicles/${item.slug}/`), `articles-sitemap.xml includes ${item.slug}`);
    assert(llmsTxt.includes(`https://iconstash.io/Listicles/${item.slug}/`), `llms.txt includes ${item.slug}`);
  }
}

assert(sitemapXml.includes('<loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-09-15</lastmod>'), 'sitemap.xml has lastmod 2026-09-15 for articles-sitemap.xml');
assert(articlesSitemap.includes('<loc>https://iconstash.io/articles/</loc><lastmod>2026-09-15</lastmod>'), 'articles-sitemap.xml has lastmod 2026-09-15 for articles/ index');

console.log(`\n========================================`);
console.log(`RESULTS: ${passed} PASSED, ${failed} FAILED`);
console.log(`========================================\n`);

if (failed > 0) {
  process.exit(1);
} else {
  process.exit(0);
}
