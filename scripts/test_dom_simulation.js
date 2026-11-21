const fs = require('fs');
const vm = require('vm');

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
    closest(selector) {
      return null;
    },
    appendChild(child) {
      this.children.push(child);
      return child;
    },
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

function runDomTestForArticle(file) {
  console.log(`\n--- Simulating DOM for ${file} ---`);
  const content = fs.readFileSync(file, 'utf8');

  // Extract all elements with IDs
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
  if (!scriptMatch) throw new Error('No client script found');
  const jsCode = scriptMatch[1];

  const doc = {
    documentElement: createMockElement('html', { 'data-theme': 'dark' }),
    body: createMockElement('body'),
    getElementById(id) {
      return elementsById[id] || null;
    },
    querySelector(sel) {
      if (sel.startsWith('#')) return elementsById[sel.substring(1)] || null;
      return null;
    },
    querySelectorAll(sel) {
      return [];
    },
    createElement(tag) {
      return createMockElement(tag);
    }
  };

  const sandbox = {
    document: doc,
    window: {
      addEventListener() {},
      setTimeout: (fn) => fn(),
      clearTimeout() {},
      alert(msg) { console.log('Alert:', msg); }
    },
    localStorage: {
      store: {},
      getItem(k) { return this.store[k] || null; },
      setItem(k, v) { this.store[k] = String(v); }
    },
    navigator: {
      clipboard: {
        writeText: (t) => Promise.resolve()
      }
    },
    console: {
      log: () => {},
      error: console.error,
      warn: console.warn
    },
    setTimeout: (fn) => fn(),
    clearTimeout: () => {},
    Math,
    parseInt,
    parseFloat,
    JSON,
    Promise,
    Date
  };

  const context = vm.createContext(sandbox);

  try {
    vm.runInContext(jsCode, context);
    console.log('  [PASS] Initial execution / render completed without error');
  } catch (e) {
    console.error(`  [FAIL] Initial execution threw error: ${e.message}`);
    console.error(e.stack);
    return false;
  }

  // Trigger events on all controls
  try {
    for (const [id, el] of Object.entries(elementsById)) {
      if (el.listeners['input']) {
        el.dispatchEvent({ type: 'input' });
      }
      if (el.listeners['change']) {
        el.dispatchEvent({ type: 'change' });
      }
      if (el.listeners['click']) {
        el.dispatchEvent({ type: 'click', target: el });
      }
      if (el.listeners['pointerdown']) {
        el.dispatchEvent({ type: 'pointerdown', pointerId: 1, clientX: 100, clientY: 100, target: el });
      }
      if (el.listeners['pointermove']) {
        el.dispatchEvent({ type: 'pointermove', pointerId: 1, clientX: 150, clientY: 150, target: el });
      }
      if (el.listeners['pointerup']) {
        el.dispatchEvent({ type: 'pointerup', pointerId: 1, clientX: 150, clientY: 150, target: el });
      }
      if (el.listeners['pointerleave']) {
        el.dispatchEvent({ type: 'pointerleave', target: el });
      }
    }
    console.log('  [PASS] All UI event dispatches (input, change, click, pointer) executed without error');
    return true;
  } catch (e) {
    console.error(`  [FAIL] Event dispatch threw error: ${e.message}`);
    console.error(e.stack);
    return false;
  }
}

const articles = [
  'articles/svg-sunburst-charts-and-radial-treemap-hierarchy-guide/index.html',
  'articles/svg-violin-plots-and-kernel-density-distribution-guide/index.html',
  'articles/svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide/index.html'
];

let allPassed = true;
for (const a of articles) {
  const ok = runDomTestForArticle(a);
  if (!ok) allPassed = false;
}

if (!allPassed) {
  console.log('\nDOM SIMULATION FAILED!');
  process.exit(1);
} else {
  console.log('\nALL DOM SIMULATIONS PASSED!');
}
