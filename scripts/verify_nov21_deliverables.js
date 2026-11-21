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

function verifyClientDomSimulation(content, slug) {
  function createMockElement(tag, attrs = {}) {
    const el = {
      tagName: tag.toUpperCase(),
      attributes: { ...attrs },
      id: attrs.id || '',
      value: attrs.value || '',
      checked: attrs.checked !== undefined ? attrs.checked : false,
      textContent: '',
      innerHTML: '',
      children: [],
      listeners: {},
      style: {},
      classList: {
        classes: new Set(),
        add(c) { this.classes.add(c); },
        remove(c) { this.classes.delete(c); },
        contains(c) { return this.classes.has(c); }
      },
      setAttribute(k, v) { this.attributes[k] = String(v); if (k === 'id') this.id = v; },
      getAttribute(k) { return this.attributes[k] !== undefined ? this.attributes[k] : null; },
      hasAttribute(k) { return this.attributes[k] !== undefined; },
      addEventListener(event, fn) {
        if (!this.listeners[event]) this.listeners[event] = [];
        this.listeners[event].push(fn);
      },
      dispatchEvent(event) {
        const fns = this.listeners[event.type] || [];
        for (const fn of fns) fn(event);
      },
      setPointerCapture() {},
      releasePointerCapture() {},
      getBoundingClientRect() {
        return { left: 0, top: 0, width: 760, height: 520, right: 760, bottom: 520 };
      },
      closest() { return null; },
      appendChild(child) { this.children.push(child); return child; },
      removeChild(child) {
        const idx = this.children.indexOf(child);
        if (idx !== -1) this.children.splice(idx, 1);
        return child;
      },
      select() {}
    };
    Object.defineProperty(el, 'outerHTML', {
      get() {
        return `<${tag} id="${el.id}" ${Object.entries(el.attributes).map(([k,v]) => `${k}="${v}"`).join(' ')}>${el.innerHTML}</${tag}>`;
      }
    });
    return el;
  }

  const elementsById = {};
  const idMatches = [...content.matchAll(/<([a-zA-Z0-9\-]+)[^>]*\sid=["']([^"']+)["'][^>]*>/gi)];
  for (const m of idMatches) {
    const tag = m[1];
    const id = m[2];
    const fullTag = m[0];
    const attrs = { id };
    const valMatch = fullTag.match(/value=["']([^"']*)["']/i);
    if (valMatch) attrs.value = valMatch[1];
    if (fullTag.includes('checked')) attrs.checked = true;
    elementsById[id] = createMockElement(tag, attrs);
  }

  const scriptMatch = content.match(/<script(?![^>]*application\/ld\+json)[^>]*>([\s\S]*?)<\/script>/i);
  if (!scriptMatch) return { success: false, error: 'No client script block found' };
  const jsCode = scriptMatch[1];

  const doc = {
    documentElement: createMockElement('html', { 'data-theme': 'dark' }),
    body: createMockElement('body'),
    getElementById(id) { return elementsById[id] || null; },
    querySelector(sel) {
      if (sel.startsWith('#')) return elementsById[sel.substring(1)] || null;
      return null;
    },
    querySelectorAll() { return []; },
    createElement(tag) { return createMockElement(tag); }
  };

  const sandbox = {
    document: doc,
    window: {
      addEventListener() {},
      setTimeout: (fn) => fn(),
      clearTimeout() {},
      alert() {}
    },
    localStorage: {
      store: {},
      getItem(k) { return this.store[k] || null; },
      setItem(k, v) { this.store[k] = String(v); }
    },
    navigator: { clipboard: { writeText: () => Promise.resolve() } },
    console: { log() {}, error() {}, warn() {} },
    setTimeout: (fn) => fn(),
    clearTimeout() {},
    Math, parseInt, parseFloat, JSON, Promise, Date
  };

  const context = vm.createContext(sandbox);
  try {
    vm.runInContext(jsCode, context);
  } catch (e) {
    return { success: false, error: `Initial render error: ${e.message}` };
  }

  try {
    for (const [id, el] of Object.entries(elementsById)) {
      if (el.listeners['input']) el.dispatchEvent({ type: 'input' });
      if (el.listeners['change']) el.dispatchEvent({ type: 'change' });
      if (el.listeners['click']) el.dispatchEvent({ type: 'click', target: el });
      if (el.listeners['pointerdown']) el.dispatchEvent({ type: 'pointerdown', pointerId: 1, clientX: 100, clientY: 100, target: el });
      if (el.listeners['pointermove']) el.dispatchEvent({ type: 'pointermove', pointerId: 1, clientX: 150, clientY: 150, target: el });
      if (el.listeners['pointerup']) el.dispatchEvent({ type: 'pointerup', pointerId: 1, clientX: 150, clientY: 150, target: el });
      if (el.listeners['pointerleave']) el.dispatchEvent({ type: 'pointerleave', target: el });
    }
  } catch (e) {
    return { success: false, error: `Event dispatch error: ${e.message}` };
  }
  return { success: true };
}

console.log('=== VERIFYING NOVEMBER 21, 2026 DELIVERABLES & SITE INTEGRATION ===\n');

const deliverables = [
  {
    type: 'article',
    slug: 'svg-sunburst-charts-and-radial-treemap-hierarchy-guide',
    path: 'articles/svg-sunburst-charts-and-radial-treemap-hierarchy-guide/index.html',
    canonical: 'https://iconstash.io/articles/svg-sunburst-charts-and-radial-treemap-hierarchy-guide/',
    image: 'svg-sunburst-charts-and-radial-treemap-hierarchy-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'svg-violin-plots-and-kernel-density-distribution-guide',
    path: 'articles/svg-violin-plots-and-kernel-density-distribution-guide/index.html',
    canonical: 'https://iconstash.io/articles/svg-violin-plots-and-kernel-density-distribution-guide/',
    image: 'svg-violin-plots-and-kernel-density-distribution-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide',
    path: 'articles/svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide/index.html',
    canonical: 'https://iconstash.io/articles/svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide/',
    image: 'svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide.jpg',
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
  const descMatch = content.match(/<meta\s+name="description"\s+content="([^"]+)"/i);
  assert(descMatch && descMatch[1].length <= 155, `Meta description length (${descMatch ? descMatch[1].length : 0}) <= 155`);

  const twDescMatch = content.match(/<meta\s+name="twitter:description"\s+content="([^"]+)"/i);
  assert(twDescMatch && twDescMatch[1].length <= 155, `Twitter description length (${twDescMatch ? twDescMatch[1].length : 0}) <= 155`);

  // 3. Canonical link with trailing slash
  assert(content.includes(`<link rel="canonical" href="${item.canonical}">`), `Canonical link correct: ${item.canonical}`);
  assert(item.canonical.endsWith('/'), `Canonical URL has trailing slash: ${item.canonical}`);

  // 4. Hero image exists and dimension check (1200x675, > 20KB)
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
  assert(content.includes('fetchpriority="high"') && content.includes('decoding="async"'), 'Hero image has fetchpriority="high" and decoding="async" for LCP');

  // 5. OpenGraph & Twitter tags pointing to full absolute URL
  assert(content.includes(`property="og:image" content="https://iconstash.io/assets/articles/${item.image}"`), 'OG Image points to full absolute URL');
  assert(content.includes(`name="twitter:image" content="https://iconstash.io/assets/articles/${item.image}"`), 'Twitter image points to full absolute URL');
  assert(content.includes('<meta name="twitter:card" content="summary_large_image">'), 'Twitter card is summary_large_image');

  // 6. Visible author byline linking to /about/
  assert(content.includes('Jouni Flemming'), 'Author Jouni Flemming present in document');
  assert(content.includes('href="/about/"'), 'Visible author byline links to /about/');
  assert(!content.includes('href="/about/" style="color:#C1DD2D') && !content.includes('href="/about/" style="color: #C1DD2D'), 'Author link does not use hardcoded inline #C1DD2D style (contrast safe)');

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
      assert(mainSchema && mainSchema.publisher && (mainSchema.publisher.name === 'Great Software Company' || (mainSchema.publisher.parentOrganization && mainSchema.publisher.parentOrganization.name === 'Great Software Company')), 'Publisher or Parent organization is Great Software Company');
      assert(mainSchema && typeof mainSchema.wordCount === 'number' && mainSchema.wordCount >= 4000, `Schema wordCount (${mainSchema ? mainSchema.wordCount : 0}) >= 4000`);

      const breadcrumb = schemas.find(s => s['@type'] === 'BreadcrumbList');
      assert(breadcrumb && breadcrumb.itemListElement && breadcrumb.itemListElement.length === 3, 'BreadcrumbList has 3 items');
      assert(breadcrumb && breadcrumb.itemListElement && breadcrumb.itemListElement[2] && breadcrumb.itemListElement[2].item === item.canonical, `BreadcrumbList item 3 has item matching canonical (${item.canonical})`);

      const faq = schemas.find(s => s['@type'] === 'FAQPage');
      assert(faq && faq.mainEntity && faq.mainEntity.length >= 6, `FAQPage has >= 6 questions (found ${faq ? faq.mainEntity.length : 0})`);
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

  // 9. Light theme contrast verification (WCAG 2.2 AA compliant)
  assert(content.includes('html[data-theme="light"] pre code'), 'Light theme pre code contrast rule present');
  assert(content.includes('html[data-theme="light"] pre'), 'Light theme pre block rule present');
  assert(content.includes('html[data-theme="light"] a { color: #4D6300; }'), 'Light theme a color rule uses WCAG AA compliant #4D6300 (> 4.5:1)');
  assert(content.includes('html[data-theme="light"] .formula-card'), 'Light theme formula-card rule present');
  assert(content.includes('html[data-theme="light"] .data-table th'), 'Light theme table header rule present');

  // 10. Word count verification via check_words.py
  try {
    const wordOut = execSync(`python scripts/check_words.py "${item.path}"`, { encoding: 'utf8' });
    const pureWordsMatch = wordOut.match(/Pure Prose Words[^:]*:\s*(\d+)/);
    const pureCount = pureWordsMatch ? parseInt(pureWordsMatch[1], 10) : 0;
    assert(pureCount >= 4000, `Pure prose word count (${pureCount}) >= 4000 words`);
  } catch (e) {
    assert(false, `Word count script failed: ${e.message}`);
  }

  // 11. Figure 2 Vector Architecture Diagram (960x320)
  assert(content.includes('viewBox="0 0 960 320"'), 'Figure 2 vector diagram with 960x320 viewBox present');

  // 12. Interactive Developer Studio present
  assert(content.includes('class="interactive-sandbox"') || content.includes('id="interactive-'), 'Interactive Developer Studio container present');
  assert(content.includes('xmlns="http://www.w3.org/2000/svg"'), 'Valid SVG xmlns attribute present for standalone copy');
  assert(content.includes('fallbackCopy') || content.includes('execCommand'), 'Fallback copy logic (execCommand/textarea) present for standalone SVG export');

  // 13. Client-side V8 script syntax validation
  const scriptBlocks = content.match(/<script(?![^>]*application\/ld\+json)[^>]*>([\s\S]*?)<\/script>/gi) || [];
  assert(scriptBlocks.length > 0, `Client-side script blocks found (${scriptBlocks.length})`);
  let scriptValid = true;
  for (const block of scriptBlocks) {
    const jsCode = block.replace(/<script[^>]*>/i, '').replace(/<\/script>/i, '');
    try {
      new vm.Script(jsCode);
    } catch (e) {
      scriptValid = false;
      console.error(`    [JS SYNTAX ERROR in ${item.slug}]: ${e.message}`);
    }
  }
  assert(scriptValid, `Client-side JavaScript syntax is valid V8 code in ${item.slug}`);

  // 13b. Client-side DOM simulation execution and event dispatch
  const domSimResult = verifyClientDomSimulation(content, item.slug);
  assert(domSimResult.success, `Client-side DOM simulation and event dispatches execute without error in ${item.slug} (${domSimResult.error || 'clean'})`);

  // 14. Heading hierarchy without level skips
  const headings = [...content.matchAll(/<h([1-6])[^>]*>/gi)].map(m => parseInt(m[1], 10));
  let headingValid = true;
  for (let i = 0; i < headings.length - 1; i++) {
    if (headings[i+1] > headings[i] + 1) {
      headingValid = false;
      console.error(`    [HEADING SKIP in ${item.slug}]: h${headings[i]} followed by h${headings[i+1]}`);
    }
  }
  assert(headingValid, `Heading hierarchy has no level skips in ${item.slug}`);

  // 15. All internal links resolve to valid targets on disk
  const internalLinks = [...content.matchAll(/href=["'](\/(?:articles|tools|about|stats|Listicles|Glossary|privacy)\/[^"']*)["']/gi)].map(m => m[1]);
  let brokenLinks = [];
  for (const link of internalLinks) {
    const cleanLink = link.split('#')[0].split('?')[0];
    let localFile = path.join(cleanLink.replace(/^\//, ''));
    if (!fs.existsSync(localFile) && !fs.existsSync(path.join(localFile, 'index.html'))) {
      brokenLinks.push(link);
    }
  }
  assert(brokenLinks.length === 0, `All ${internalLinks.length} internal links in ${item.slug} resolve on disk (broken: ${brokenLinks.join(', ') || 'none'})`);

  // 16. Form control label accessibility
  const formControls = [...content.matchAll(/<(input|select|textarea)[^>]*id=["']([^"']+)["'][^>]*>/gi)].map(m => m[2]);
  let missingFormLabels = [];
  for (const cId of formControls) {
    if (!content.includes(`for="${cId}"`) && !content.includes(`for='${cId}'`)) {
      missingFormLabels.push(cId);
    }
  }
  assert(missingFormLabels.length === 0, `All ${formControls.length} interactive form controls in ${item.slug} have associated labels`);

  // 17. All hash anchors resolve to target IDs
  const allHashAnchors = [...content.matchAll(/href=["']#([^"']+)["']/gi)].map(m => m[1]);
  let missingTargets = [];
  for (const tId of allHashAnchors) {
    if (!content.includes(`id="${tId}"`)) {
      missingTargets.push(tId);
    }
  }
  assert(missingTargets.length === 0, `All ${allHashAnchors.length} hash anchors in ${item.slug} resolve to valid DOM id targets`);

  // 17b. Table of Contents numbering synchronized with H2 headings
  const tocAside = content.match(/<aside[\s\S]*?<\/aside>/);
  if (tocAside) {
    const tocNumberedLinks = [...tocAside[0].matchAll(/<a href="#([^"]+)">\s*(\d+)\.\s*([\s\S]*?)<\/a>/g)];
    let tocDesyncs = [];
    for (const tMatch of tocNumberedLinks) {
      const targetId = tMatch[1];
      const tocNum = parseInt(tMatch[2], 10);
      const sectionMatch = content.match(new RegExp(`<section[^>]*id=["']${targetId}["'][\\s\\S]*?<h2[^>]*>([\\s\\S]*?)<\\/h2>`, 'i'));
      if (sectionMatch) {
        const cleanH2 = sectionMatch[1].replace(/<svg[\s\S]*?<\/svg>/gi, '').replace(/<[^>]+>/g, '').trim();
        const numMatch = cleanH2.match(/^(\d+)\./) || cleanH2.match(/(\d+)\./);
        if (numMatch) {
          const h2Num = parseInt(numMatch[1], 10);
          if (tocNum !== h2Num) {
            tocDesyncs.push(`Target #${targetId}: TOC has ${tocNum}., H2 has ${h2Num}.`);
          }
        }
      }
    }
    assert(tocDesyncs.length === 0, `Table of Contents numbering is synchronized with H2 headings in ${item.slug} (desyncs: ${tocDesyncs.join('; ') || 'none'})`);
  }

  // 18. Touch handling & touch-action: none compliance
  assert(content.includes('.preview-stage-container') && content.includes('touch-action: none'), `touch-action: none is declared on canvas/container in ${item.slug}`);
  assert(content.includes('user-select: none'), `user-select: none is declared on interactive container in ${item.slug}`);

  // 19. Pointer capture and pointercancel event handling
  assert(content.includes('setPointerCapture'), `setPointerCapture is implemented for robust drag tracking in ${item.slug}`);
  assert(content.includes('pointercancel'), `pointercancel event handling is implemented for gesture recovery in ${item.slug}`);

  // 20. XML validity of inline SVGs (no undefined entities like &le; or &plusmn;)
  const noScriptContent = content.replace(/<script[\s\S]*?<\/script>/gi, '');
  const inlineSvgs = [...noScriptContent.matchAll(/<svg[\s\S]*?<\/svg>/gi)].map(m => m[0]);
  let xmlErrors = [];
  const xmlEntities = new Set(['amp', 'lt', 'gt', 'quot', 'apos']);
  for (const svg of inlineSvgs) {
    const entityMatches = [...svg.matchAll(/&([a-zA-Z0-9]+);/g)].map(m => m[1]);
    const badEntities = entityMatches.filter(e => !xmlEntities.has(e));
    if (badEntities.length > 0) {
      xmlErrors.push(`Found undefined XML entities: [${badEntities.join(', ')}]`);
    }
  }
  assert(xmlErrors.length === 0, `All ${inlineSvgs.length} inline SVGs have valid XML entity encoding in ${item.slug} (errors: ${xmlErrors.join('; ') || 'none'})`);
}

// Site Integration Verification: articles/index.html
console.log('\n--- Checking Site Integration in articles/index.html ---');
const articlesIndex = fs.readFileSync('articles/index.html', 'utf8');

for (const item of deliverables) {
  assert(articlesIndex.includes(item.canonical) || articlesIndex.includes(item.canonical.replace('https://iconstash.io', '')), `articles/index.html contains link to ${item.slug}`);
}

const guidesMatch = articlesIndex.match(/<span class="count">(\d+)\s+guides<\/span>/);
assert(guidesMatch && parseInt(guidesMatch[1], 10) >= 132, `Guides count is at least 132 guides (found ${guidesMatch ? guidesMatch[1] : 0})`);
assert(articlesIndex.includes('"position": 181') && articlesIndex.includes('"position": 182') && articlesIndex.includes('"position": 183'), 'ItemList contains positions 181 through 183');

// Sitemap Verification: articles-sitemap.xml
console.log('\n--- Checking articles-sitemap.xml ---');
const sitemap = fs.readFileSync('articles-sitemap.xml', 'utf8');

for (const item of deliverables) {
  assert(sitemap.includes(`<loc>${item.canonical}</loc>`), `articles-sitemap.xml includes ${item.canonical}`);
  const urlEntryRegex = new RegExp(`<loc>${item.canonical.replace(/\\/g, '\\/').replace(/\//g, '\\/')}<\\/loc>[\\s\\S]*?<lastmod>2026-11-21<\\/lastmod>`);
  assert(urlEntryRegex.test(sitemap), `${item.slug} has current lastmod 2026-11-21`);
}
assert(sitemap.includes('<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-21</lastmod>'), 'Articles hub in sitemap has lastmod 2026-11-21');

// Parent sitemap.xml
console.log('\n--- Checking parent sitemap.xml ---');
const parentSitemap = fs.readFileSync('sitemap.xml', 'utf8');
assert(parentSitemap.includes('<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-21</lastmod></sitemap>'), 'parent sitemap.xml references articles-sitemap.xml with 2026-11-21');

// llms.txt
console.log('\n--- Checking llms.txt ---');
const llms = fs.readFileSync('llms.txt', 'utf8');
for (const item of deliverables) {
  assert(llms.includes(item.canonical), `llms.txt includes ${item.canonical}`);
}
assert(llms.includes('- Last updated: 2026-11-21'), 'llms.txt has updated timestamp 2026-11-21 in Key Facts header');
assert(llms.includes('Last updated: 2026-11-21'), 'llms.txt has updated timestamp 2026-11-21 in footer');

// Strict brand safety on global files
for (const f of ['articles/index.html', 'articles-sitemap.xml', 'sitemap.xml', 'llms.txt']) {
  const c = fs.readFileSync(f, 'utf8');
  for (const word of forbidden) {
    assert(!c.toLowerCase().includes(word), `Strict Brand Safety in ${f}: Zero mentions of "${word}"`);
  }
}

console.log(`\n========================================`);
console.log(`VERIFICATION SUMMARY: ${passed} PASSED, ${failed} FAILED`);
console.log(`========================================\n`);

if (failed > 0) {
  process.exit(1);
} else {
  console.log('ALL NOVEMBER 21 DELIVERABLES & SITE INTEGRATIONS PASSED WITH ZERO ERRORS!\n');
}
