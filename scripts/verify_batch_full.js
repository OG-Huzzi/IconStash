const fs = require('fs');
const path = require('path');

let passed = 0;
let failed = 0;

function assert(condition, msg) {
  if (condition) {
    passed++;
    console.log(`  [PASS] ${msg}`);
  } else {
    failed++;
    console.error(`  [FAIL] ${msg}`);
  }
}

console.log('=== FULL AUDIT OF NEW DELIVERABLES & SITE INTEGRATION ===\n');

// 1. Check articles/index.html counts
console.log('1. Checking articles/index.html section counts...');
const indexHtml = fs.readFileSync('articles/index.html', 'utf8');
const sections = indexHtml.split('<div class="section-head">');
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

// 2. Deliverables list
const deliverables = [
  {
    file: 'articles/lucide-icons-complete-guide/index.html',
    url: 'https://iconstash.io/articles/lucide-icons-complete-guide/',
    img: 'assets/articles/lucide-icons-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    file: 'articles/heroicons-complete-guide/index.html',
    url: 'https://iconstash.io/articles/heroicons-complete-guide/',
    img: 'assets/articles/heroicons-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    file: 'articles/bootstrap-icons-complete-guide/index.html',
    url: 'https://iconstash.io/articles/bootstrap-icons-complete-guide/',
    img: 'assets/articles/bootstrap-icons-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    file: 'articles/convert-svg-to-png-javascript-guide/index.html',
    url: 'https://iconstash.io/articles/convert-svg-to-png-javascript-guide/',
    img: 'assets/articles/convert-svg-to-png-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    file: 'Listicles/best-minimal-line-icon-packs/index.html',
    url: 'https://iconstash.io/Listicles/best-minimal-line-icon-packs/',
    img: 'assets/articles/best-minimal-line-icon-packs.jpg',
    schemaType: 'Article',
    isListicle: true
  },
  {
    file: 'Glossary/svg-dom-and-javascript-api-glossary/index.html',
    url: 'https://iconstash.io/Glossary/svg-dom-and-javascript-api-glossary/',
    img: 'assets/articles/svg-dom-javascript-api-glossary.jpg',
    schemaType: 'DefinedTermSet',
    isGlossary: true
  }
];

const forbidden = ['jv16', 'winfindr', 'uninstalr'];

for (const d of deliverables) {
  console.log(`\nChecking deliverable: ${d.file}...`);
  assert(fs.existsSync(d.file), `File exists: ${d.file}`);
  const content = fs.readFileSync(d.file, 'utf8');

  // Single H1
  const h1Matches = content.match(/<h1[\s>]/gi) || [];
  assert(h1Matches.length === 1, `${d.file} has exactly one <h1> (found ${h1Matches.length})`);

  // Meta description <= 155 chars
  const descMatch = content.match(/<meta\s+name=["']description["']\s+content=["']([^"']*)["']/i);
  assert(descMatch && descMatch[1].length <= 155, `${d.file} meta description length (${descMatch ? descMatch[1].length : 0}) <= 155`);

  // Canonical tag
  assert(content.includes(`<link rel="canonical" href="${d.url}">`), `${d.file} has canonical tag pointing to ${d.url}`);

  // Visible author byline
  assert(content.includes('href="/about/"') && content.includes('Jouni Flemming'), `${d.file} has visible author byline for Jouni Flemming linking to /about/`);

  // Forbidden words
  for (const f of forbidden) {
    assert(!content.toLowerCase().includes(f), `${d.file} contains 0 mentions of ${f}`);
  }

  // Hero image exists on disk
  assert(fs.existsSync(d.img), `${d.file} hero image exists on disk at ${d.img}`);

  // JSON-LD schemas
  const jsonLdMatch = content.match(/<script\s+type=["']application\/ld\+json["']>([\s\S]*?)<\/script>/i);
  assert(!!jsonLdMatch, `${d.file} contains JSON-LD script tag`);
  if (jsonLdMatch) {
    try {
      const parsed = JSON.parse(jsonLdMatch[1]);
      const list = Array.isArray(parsed) ? parsed : (parsed['@graph'] || [parsed]);
      
      // Main entity schema
      const mainEntity = list.find(item => item['@type'] === d.schemaType);
      assert(!!mainEntity, `${d.file} has schema @type: ${d.schemaType}`);
      if (mainEntity) {
        assert(mainEntity.author && mainEntity.author.name === 'Jouni Flemming', `${d.file} schema author name is Jouni Flemming`);
        assert(mainEntity.author && mainEntity.author.url && mainEntity.author.url.includes('/about/'), `${d.file} schema author URL points to /about/`);
        assert(!JSON.stringify(mainEntity.author).toLowerCase().includes('github'), `${d.file} author schema contains no GitHub link`);
        assert(mainEntity.publisher && mainEntity.publisher.name === 'IconStash', `${d.file} schema publisher is IconStash`);
        assert(mainEntity.publisher && mainEntity.publisher.parentOrganization && mainEntity.publisher.parentOrganization.name === 'Great Software Company', `${d.file} schema parentOrganization is Great Software Company`);
        assert(mainEntity.publisher && mainEntity.publisher.parentOrganization && mainEntity.publisher.parentOrganization.url === 'https://greatsoftwarecompany.com', `${d.file} schema parentOrganization URL is https://greatsoftwarecompany.com`);
      }

      // BreadcrumbList schema
      const breadcrumb = list.find(item => item['@type'] === 'BreadcrumbList');
      assert(!!breadcrumb, `${d.file} has BreadcrumbList schema`);
      if (breadcrumb) {
        assert(breadcrumb.itemListElement && breadcrumb.itemListElement.length === 3, `${d.file} breadcrumb has 3 levels`);
      }

      // FAQPage schema
      const faq = list.find(item => item['@type'] === 'FAQPage');
      assert(!!faq, `${d.file} has FAQPage schema`);
      if (faq) {
        assert(faq.mainEntity && faq.mainEntity.length >= 3, `${d.file} has >= 3 FAQ questions`);
        for (const q of (faq.mainEntity || [])) {
          assert(!!q.name && !!q.acceptedAnswer && !!q.acceptedAnswer.text, `${d.file} FAQ "${q.name.slice(0, 30)}..." has valid question and acceptedAnswer`);
        }
      }

      // ItemList for listicle
      if (d.isListicle) {
        const itemList = list.find(item => item['@type'] === 'ItemList');
        assert(!!itemList, `${d.file} has ItemList schema`);
        if (itemList) {
          assert(itemList.numberOfItems === 15, `${d.file} ItemList specifies 15 items`);
        }
      }

      // DefinedTermSet for glossary
      if (d.isGlossary) {
        assert(mainEntity && mainEntity.hasDefinedTerm && mainEntity.hasDefinedTerm.length >= 25, `${d.file} DefinedTermSet has >= 25 defined terms`);
      }

    } catch (err) {
      assert(false, `${d.file} JSON-LD failed to parse: ${err.message}`);
    }
  }

  // Light mode pre code contrast check
  assert(content.includes('html[data-theme="light"] pre code'), `${d.file} defines html[data-theme="light"] pre code for contrast`);

  // Internal link resolution
  const aMatches = content.matchAll(/<a\s+[^>]*href=["'](\/[^"']*)["'][^>]*>/gi);
  for (const m of aMatches) {
    const rawHref = m[1];
    if (rawHref.startsWith('/#') || rawHref === '/') continue;
    const cleanPath = rawHref.split('?')[0].split('#')[0];
    if (!cleanPath || cleanPath === '/') continue;
    const relPath = cleanPath.startsWith('/') ? cleanPath.slice(1) : cleanPath;
    const directFile = path.join(__dirname, '..', relPath);
    const indexFile = path.join(__dirname, '..', relPath, 'index.html');
    assert(fs.existsSync(directFile) || fs.existsSync(indexFile), `${d.file} link ${rawHref} resolves on disk`);
  }
}

// 3. Check Sitemaps & Integration
console.log('\n3. Checking sitemaps and llms.txt integration...');
const articlesSitemap = fs.readFileSync('articles-sitemap.xml', 'utf8');
const sitemapXml = fs.readFileSync('sitemap.xml', 'utf8');
const llmsTxt = fs.readFileSync('llms.txt', 'utf8');

for (const d of deliverables) {
  assert(articlesSitemap.includes(`<loc>${d.url}</loc>`), `articles-sitemap.xml contains ${d.url}`);
  assert(indexHtml.includes(d.url.replace('https://iconstash.io', '')), `articles/index.html includes card for ${d.url}`);
  assert(llmsTxt.includes(d.url), `llms.txt includes ${d.url}`);
}

assert(/<loc>https:\/\/iconstash\.io\/articles-sitemap\.xml<\/loc><lastmod>2026-09-\d{2}<\/lastmod>/.test(sitemapXml), 'sitemap.xml has valid 2026-09 lastmod for articles-sitemap.xml');

console.log('\n========================================');
console.log(`RESULTS: ${passed} PASSED, ${failed} FAILED`);
console.log('========================================');
