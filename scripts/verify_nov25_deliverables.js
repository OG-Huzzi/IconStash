import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { execSync } from 'node:child_process';

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
        return { left: 0, top: 0, width: 760, height: 440, right: 760, bottom: 440 };
      },
      closest() { return null; },
      querySelector() { return null; },
      contains() { return true; },
      focus() {},
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
        return `<${tag} id="${el.id}" ${Object.entries(el.attributes).map(([k, v]) => `${k}="${v}"`).join(' ')}>${el.innerHTML}</${tag}>`;
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
    createElement(tag) { return createMockElement(tag); },
    elementFromPoint() { return null; },
    execCommand() { return true; },
    activeElement: null
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
    Math, parseInt, parseFloat, JSON, Promise, Date, Array, Number, String, Object
  };

  const context = vm.createContext(sandbox);
  try {
    vm.runInContext(jsCode, context);
  } catch (e) {
    return { success: false, error: `Initial render error: ${e.message}` };
  }

  const liveCanvas = Object.values(elementsById).find(el => el.id.endsWith('-live-canvas'));
  if (!liveCanvas || !liveCanvas.innerHTML || liveCanvas.innerHTML.trim().length < 100) {
    return { success: false, error: 'Live SVG canvas innerHTML is empty after initial render' };
  }

  try {
    for (const [, el] of Object.entries(elementsById)) {
      if (el.listeners['input']) el.dispatchEvent({ type: 'input' });
      if (el.listeners['change']) el.dispatchEvent({ type: 'change' });
      if (el.listeners['click']) el.dispatchEvent({ type: 'click', target: el });
      if (el.listeners['focusin']) el.dispatchEvent({ type: 'focusin', target: el });
      if (el.listeners['focusout']) el.dispatchEvent({ type: 'focusout', target: el, relatedTarget: null });
      if (el.listeners['keydown']) {
        for (const key of ['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Home', 'End']) {
          el.dispatchEvent({ type: 'keydown', key, target: el, preventDefault() {} });
        }
      }
      if (el.listeners['pointerdown']) el.dispatchEvent({ type: 'pointerdown', pointerId: 1, clientX: 250, clientY: 220, target: el });
      if (el.listeners['pointermove']) el.dispatchEvent({ type: 'pointermove', pointerId: 1, clientX: 320, clientY: 210, target: el });
      if (el.listeners['pointerup']) el.dispatchEvent({ type: 'pointerup', pointerId: 1, clientX: 320, clientY: 210, target: el });
      if (el.listeners['pointercancel']) el.dispatchEvent({ type: 'pointercancel', pointerId: 1, target: el });
    }
  } catch (e) {
    return { success: false, error: `Event dispatch error: ${e.message}` };
  }

  // Validate dynamically rendered SVG XML entities & no NaN/undefined
  if (liveCanvas.innerHTML.includes('NaN') || liveCanvas.innerHTML.includes('undefined')) {
    return { success: false, error: 'NaN or undefined rendered inside dynamic SVG canvas' };
  }
  const xmlEntities = new Set(['amp', 'lt', 'gt', 'quot', 'apos']);
  const entityMatches = [...liveCanvas.innerHTML.matchAll(/&([a-zA-Z0-9]+);/g)].map(m => m[1]);
  const badDynEntities = entityMatches.filter(e => !xmlEntities.has(e));
  if (badDynEntities.length > 0) {
    return { success: false, error: `Undefined XML entities in dynamic SVG canvas: ${badDynEntities.join(', ')}` };
  }

  // Edge-case stress test: zero-dimension rect, negative/empty input values, clipboard missing
  liveCanvas.getBoundingClientRect = () => ({ left: 0, top: 0, width: 0, height: 0, right: 0, bottom: 0 });
  sandbox.navigator.clipboard = null;
  for (const [, el] of Object.entries(elementsById)) {
    if (el.id.includes('seed')) el.value = '-99';
    if (el.id.includes('slider')) el.value = '0';
    if (el.listeners['input']) el.dispatchEvent({ type: 'input' });
    if (el.listeners['change']) el.dispatchEvent({ type: 'change' });
    if (el.listeners['pointerdown']) el.dispatchEvent({ type: 'pointerdown', pointerId: 1, clientX: 9999, clientY: -50, target: el });
    if (el.listeners['pointermove']) el.dispatchEvent({ type: 'pointermove', pointerId: 1, clientX: -100, clientY: 9999, target: el });
    if (el.listeners['pointercancel']) el.dispatchEvent({ type: 'pointercancel', pointerId: 1, target: el });
  }
  if (liveCanvas.innerHTML.includes('NaN') || liveCanvas.innerHTML.includes('undefined')) {
    return { success: false, error: 'NaN or undefined rendered under boundary/zero-rect stress test' };
  }

  return { success: true, svgBytes: liveCanvas.innerHTML.length };
}

console.log('=== VERIFYING NOVEMBER 25, 2026 DELIVERABLES & SITE INTEGRATION ===\n');

const deliverables = [
  {
    type: 'article',
    slug: 'svg-line-charts-and-multi-series-time-series-guide',
    path: 'articles/svg-line-charts-and-multi-series-time-series-guide/index.html',
    canonical: 'https://iconstash.io/articles/svg-line-charts-and-multi-series-time-series-guide/',
    image: 'svg-line-charts-and-multi-series-time-series-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'svg-blob-generator-and-organic-shapes-guide',
    path: 'articles/svg-blob-generator-and-organic-shapes-guide/index.html',
    canonical: 'https://iconstash.io/articles/svg-blob-generator-and-organic-shapes-guide/',
    image: 'svg-blob-generator-and-organic-shapes-guide.jpg',
    schemaType: 'TechArticle'
  },
  {
    type: 'article',
    slug: 'shadcn-ui-icons-complete-guide-2026',
    path: 'articles/shadcn-ui-icons-complete-guide-2026/index.html',
    canonical: 'https://iconstash.io/articles/shadcn-ui-icons-complete-guide-2026/',
    image: 'shadcn-ui-icons-complete-guide-2026.jpg',
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

  // 2. Meta title, description, robots
  const titleMatch = content.match(/<title>([^<]+)<\/title>/i);
  assert(titleMatch && titleMatch[1].length <= 75, `<title> length (${titleMatch ? titleMatch[1].length : 0}) concise <= 75 chars`);

  const descMatch = content.match(/<meta\s+name="description"\s+content="([^"]+)"/i);
  assert(descMatch && descMatch[1].length >= 120 && descMatch[1].length <= 155, `Meta description length (${descMatch ? descMatch[1].length : 0}) between 120 and 155 chars`);

  const twDescMatch = content.match(/<meta\s+name="twitter:description"\s+content="([^"]+)"/i);
  assert(twDescMatch && twDescMatch[1].length <= 155, `Twitter description length (${twDescMatch ? twDescMatch[1].length : 0}) <= 155`);

  assert(content.includes('<meta name="robots" content="index, follow'), 'Robots index, follow meta present');

  // 3. Canonical link with trailing slash
  assert(content.includes(`<link rel="canonical" href="${item.canonical}">`), `Canonical link correct: ${item.canonical}`);
  assert(item.canonical.endsWith('/'), `Canonical URL has trailing slash: ${item.canonical}`);

  // 4. Hero image exists and dimension check (1200x675, > 20KB)
  const imgPath = path.join('assets/articles', item.image);
  assert(fs.existsSync(imgPath), `Hero image exists on disk: ${imgPath}`);
  if (fs.existsSync(imgPath)) {
    const stats = fs.statSync(imgPath);
    assert(stats.size > 20000, `Hero image size (${Math.round(stats.size / 1024)} KB) > 20 KB`);
    const probeOut = execSync(`python -c "from PIL import Image; im = Image.open(r'${imgPath}'); print(f'{im.width}x{im.height}')"`, { encoding: 'utf8' }).trim();
    assert(probeOut === '1200x675', `Hero image resolution is 1200x675 (found ${probeOut})`);
  }
  assert(content.includes('fetchpriority="high"') && content.includes('decoding="async"'), 'Hero image has fetchpriority="high" and decoding="async"');
  assert(content.includes('width="1200" height="675"'), 'Hero image declares explicit width="1200" height="675" for zero CLS');

  // 5. OpenGraph & Twitter tags
  assert(content.includes(`property="og:image" content="https://iconstash.io/assets/articles/${item.image}"`), 'OG Image points to full absolute URL');
  assert(content.includes(`name="twitter:image" content="https://iconstash.io/assets/articles/${item.image}"`), 'Twitter image points to full absolute URL');
  assert(content.includes('<meta name="twitter:card" content="summary_large_image">'), 'Twitter card is summary_large_image');

  // 6. Author byline & Brand safety
  assert(content.includes('Jouni Flemming') && content.includes('href="/about/"'), 'Author Jouni Flemming links to /about/');
  assert(!content.includes('href="/about/" style="color:#C1DD2D'), 'Author link does not hardcode inline #C1DD2D');
  for (const f of forbidden) {
    assert(!content.toLowerCase().includes(f), `Zero forbidden string "${f}"`);
  }

  // 7. No raw LaTeX leaks
  assert(!content.includes('\\frac') && !content.includes('\\times') && !content.includes('\\sum'), 'Zero raw LaTeX escapes leaked in prose');

  // 8. Schema.org JSON-LD validation
  const jsonLdMatch = content.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
  assert(jsonLdMatch, 'JSON-LD script block exists');
  if (jsonLdMatch) {
    const schemas = JSON.parse(jsonLdMatch[1]);
    assert(Array.isArray(schemas), 'Root JSON-LD is an array');
    const mainSchema = schemas.find(s => s['@type'] === item.schemaType);
    assert(mainSchema && mainSchema.description && mainSchema.description.length <= 155, 'TechArticle schema description <= 155');
    assert(mainSchema && mainSchema.author && mainSchema.author.name === 'Jouni Flemming', 'Schema author is Jouni Flemming');
    assert(mainSchema && mainSchema.publisher && mainSchema.publisher.parentOrganization.name === 'Great Software Company', 'Parent org is Great Software Company');
    assert(mainSchema && typeof mainSchema.wordCount === 'number' && mainSchema.wordCount >= 4000, `Schema wordCount (${mainSchema ? mainSchema.wordCount : 0}) >= 4000`);
    const breadcrumb = schemas.find(s => s['@type'] === 'BreadcrumbList');
    assert(breadcrumb && breadcrumb.itemListElement.length === 3 && breadcrumb.itemListElement[2].item === item.canonical, 'BreadcrumbList valid with 3 items');
    const faq = schemas.find(s => s['@type'] === 'FAQPage');
    assert(faq && faq.mainEntity.length >= 7 && faq.mainEntity.every(q => q.acceptedAnswer && q.acceptedAnswer.text.trim().length > 20), `FAQPage has ${faq ? faq.mainEntity.length : 0} valid answers`);
  }

  // 9. Light theme contrast rules
  assert(content.includes('html[data-theme="light"] pre code') && content.includes('html[data-theme="light"] a { color: #4D6300; }') && content.includes('html[data-theme="light"] .data-table th'), 'WCAG 2.2 AA light theme CSS rules present');

  // 10. Word count >= 4000 pure prose
  const wordOut = execSync(`python scripts/check_words.py "${item.path}"`, { encoding: 'utf8' });
  const pureWordsMatch = wordOut.match(/Pure Prose Words[^:]*:\s*(\d+)/);
  const pureCount = pureWordsMatch ? parseInt(pureWordsMatch[1], 10) : 0;
  assert(pureCount >= 4000, `Pure prose word count (${pureCount}) >= 4000 words`);

  // 11. Figure 2 960x320 & Interactive Studio
  assert(content.includes('viewBox="0 0 960 320"'), 'Figure 2 960x320 vector diagram present');
  assert(content.includes('class="interactive-sandbox"') && content.includes('fallbackCopy'), 'Interactive studio + fallbackCopy present');

  // 12. JS Syntax + DOM Simulation
  const scriptBlocks = content.match(/<script(?![^>]*application\/ld\+json)[^>]*>([\s\S]*?)<\/script>/gi) || [];
  let scriptValid = true;
  for (const block of scriptBlocks) {
    const jsCode = block.replace(/<script[^>]*>/i, '').replace(/<\/script>/i, '');
    new vm.Script(jsCode);
  }
  assert(scriptValid && scriptBlocks.length > 0, 'Client JS syntax valid in V8');

  const domSim = verifyClientDomSimulation(content, item.slug);
  assert(domSim.success, `DOM simulation & event dispatch passed (${domSim.error || `rendered ${domSim.svgBytes} bytes SVG`})`);

  // 13. Headings hierarchy
  const headings = [...content.matchAll(/<h([1-6])[^>]*>/gi)].map(m => parseInt(m[1], 10));
  let headingValid = true;
  for (let i = 0; i < headings.length - 1; i++) {
    if (headings[i + 1] > headings[i] + 1) headingValid = false;
  }
  assert(headingValid, 'Heading hierarchy has zero level skips');

  // 14. Internal links resolve on disk
  const internalLinks = [...content.matchAll(/href=["'](\/(?:articles|tools|about|stats|Listicles|Glossary|privacy)\/[^"']*)["']/gi)].map(m => m[1]);
  const brokenLinks = internalLinks.filter(link => {
    const clean = link.split('#')[0].split('?')[0].replace(/^\//, '');
    return !fs.existsSync(clean) && !fs.existsSync(path.join(clean, 'index.html'));
  });
  assert(brokenLinks.length === 0, `All ${internalLinks.length} internal links resolve on disk (broken: ${brokenLinks.join(', ') || 'none'})`);

  // 15. Form labels & Hash anchors & TOC sync
  const formControls = [...content.matchAll(/<(input|select|textarea)[^>]*id=["']([^"']+)["'][^>]*>/gi)].map(m => m[2]);
  const missingLabels = formControls.filter(id => !content.includes(`for="${id}"`) && !content.includes(`for='${id}'`));
  assert(missingLabels.length === 0, `All ${formControls.length} form controls have <label for>`);

  const hashAnchors = [...content.matchAll(/href=["']#([^"']+)["']/gi)].map(m => m[1]);
  const missingTargets = hashAnchors.filter(id => !content.includes(`id="${id}"`));
  assert(missingTargets.length === 0, `All ${hashAnchors.length} #hash anchors resolve to DOM IDs`);

  const tocAside = content.match(/<aside[\s\S]*?<\/aside>/);
  let tocDesyncs = [];
  if (tocAside) {
    const tocLinks = [...tocAside[0].matchAll(/<a href="#([^"]+)">\s*(\d+)\./g)];
    for (const t of tocLinks) {
      const sec = content.match(new RegExp(`<section[^>]*id=["']${t[1]}["'][\\s\\S]*?<h2[^>]*>([\\s\\S]*?)<\\/h2>`, 'i'));
      if (sec) {
        const cleanH2 = sec[1].replace(/<[^>]+>/g, '').trim();
        const hm = cleanH2.match(/^(\d+)\./);
        if (hm && parseInt(hm[1], 10) !== parseInt(t[2], 10)) tocDesyncs.push(t[1]);
      }
    }
  }
  assert(tocDesyncs.length === 0, 'TOC numbering synchronized 1:1 with H2 headings');

  // 16. Touch & Pointer Capture
  assert(content.includes('touch-action: none') && content.includes('user-select: none') && content.includes('setPointerCapture') && content.includes('pointercancel'), 'Touch action, user-select, pointer capture & cancel present');

  // 17. XML validity of inline SVGs
  const noScript = content.replace(/<script[\s\S]*?<\/script>/gi, '');
  const svgs = [...noScript.matchAll(/<svg[\s\S]*?<\/svg>/gi)].map(m => m[0]);
  const xmlEntities = new Set(['amp', 'lt', 'gt', 'quot', 'apos']);
  let badXml = [];
  for (const svg of svgs) {
    const ents = [...svg.matchAll(/&([a-zA-Z0-9]+);/g)].map(m => m[1]).filter(e => !xmlEntities.has(e));
    if (ents.length) badXml.push(ents.join(','));
  }
  assert(badXml.length === 0, `All ${svgs.length} static inline SVGs have valid XML entities`);
}

console.log('\n--- Checking Site Integration ---');
const articlesIndex = fs.readFileSync('articles/index.html', 'utf8');
for (const item of deliverables) {
  assert(articlesIndex.includes(item.canonical) && articlesIndex.includes(`/articles/${item.slug}/`), `articles/index.html links to ${item.slug}`);
}
assert(articlesIndex.includes('<span class="count">138 guides</span>'), 'articles/index.html displays 138 guides');
assert(articlesIndex.includes('"position": 187') && articlesIndex.includes('"position": 188') && articlesIndex.includes('"position": 189'), 'ItemList includes positions 187, 188, 189');
const idxLdMatch = articlesIndex.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
let idxLdValid = false;
if (idxLdMatch) {
  const idxSchemas = JSON.parse(idxLdMatch[1]);
  const itemList = idxSchemas.find(s => s['@type'] === 'ItemList');
  idxLdValid = Boolean(itemList && itemList.itemListElement && itemList.itemListElement.length === 189);
}
assert(idxLdValid, 'articles/index.html JSON-LD parses cleanly with 189 sequential ItemList items');

const sitemap = fs.readFileSync('articles-sitemap.xml', 'utf8');
for (const item of deliverables) {
  assert(sitemap.includes(`<loc>${item.canonical}</loc>`), `articles-sitemap.xml includes ${item.slug}`);
}
assert(sitemap.includes('<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-25</lastmod>'), 'articles-sitemap.xml hub lastmod is 2026-11-25');

const parentSitemap = fs.readFileSync('sitemap.xml', 'utf8');
assert(parentSitemap.includes('<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-25</lastmod></sitemap>'), 'sitemap.xml lastmod is 2026-11-25');

// XML parse test on sitemaps
execSync('python -c "import xml.etree.ElementTree as ET; ET.parse(\'sitemap.xml\'); ET.parse(\'articles-sitemap.xml\'); print(\'XML OK\')"', { encoding: 'utf8' });
assert(true, 'Both sitemap.xml and articles-sitemap.xml parse as valid XML');

const llms = fs.readFileSync('llms.txt', 'utf8');
for (const item of deliverables) {
  assert(llms.includes(item.canonical), `llms.txt includes ${item.slug}`);
}
assert(llms.includes('- Last updated: 2026-11-25') && llms.includes('\nLast updated: 2026-11-25'), 'llms.txt timestamps updated to 2026-11-25');

for (const f of ['articles/index.html', 'articles-sitemap.xml', 'sitemap.xml', 'llms.txt']) {
  const c = fs.readFileSync(f, 'utf8');
  for (const word of forbidden) {
    assert(!c.toLowerCase().includes(word), `Brand safety in ${f}: zero "${word}"`);
  }
}

console.log(`\n========================================`);
console.log(`VERIFICATION SUMMARY: ${passed} PASSED, ${failed} FAILED`);
console.log(`========================================\n`);

if (failed > 0) process.exit(1);
