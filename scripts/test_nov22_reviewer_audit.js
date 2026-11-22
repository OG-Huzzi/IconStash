const fs = require('fs');
const assert = require('assert');
const vm = require('vm');

console.log('=== RUNNING DEEP SKEPTICAL REVIEWER AUDIT (NOV 22 DELIVERABLES) ===\n');

// 1. Audit Ternary Plot Greek Phase Strings & Accessible Interaction
console.log('--- Audit 1: Ternary Plot Greek Phase Strings & Accessible Interaction ---');
const terHtml = fs.readFileSync('articles/svg-ternary-plots-and-triangular-composition-diagram-guide/index.html', 'utf8');

// Assert no raw HTML entities in JS string literals
assert(!terHtml.includes("'Austenitic (&gamma;)'"), 'FAIL: Raw &gamma; HTML entity still present in JS string');
assert(terHtml.includes("'Austenitic (γ)'"), 'PASS: Proper UTF-8 unicode γ used in JS string');
assert(!terHtml.includes("'Ferritic (&alpha;)'"), 'FAIL: Raw &alpha; HTML entity still present in JS string');
assert(terHtml.includes("'Ferritic (α)'"), 'PASS: Proper UTF-8 unicode α used in JS string');

// Assert sample points have tabindex and data-sample-idx
assert(terHtml.includes('data-sample-idx="${sIdx}"'), 'PASS: Sample points have data-sample-idx attribute');
assert(terHtml.includes('class="ternary-sample" data-sample-idx='), 'PASS: Sample markup includes index binding');
assert(terHtml.includes('class="ternary-user-cursor" tabindex="0" role="slider"'), 'PASS: Draggable cursor has role="slider" and tabindex="0"');
assert(terHtml.includes("e.key === 'ArrowUp'"), 'PASS: Arrow key navigation is implemented for ternary cursor');
assert(terHtml.includes('if (!rect || !rect.width || !rect.height) return;'), 'PASS: Defensive check for zero-dimension bounding rect is present');

// 2. Audit Chord Diagram Touch Hit-testing & Standalone Export Cleanliness
console.log('\n--- Audit 2: Chord Diagram Pointer Capture Hit-testing & Export Cleanliness ---');
const chordHtml = fs.readFileSync('articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/index.html', 'utf8');

assert(chordHtml.includes('data-ribbon-idx="${idx}" tabindex="0" role="graphics-symbol"'), 'PASS: Bilateral ribbons have tabindex="0" and role="graphics-symbol"');
assert(chordHtml.includes('data-group-id="${g.id}" tabindex="0" role="region"'), 'PASS: Perimeter group arcs have tabindex="0" and role="region"');
assert(chordHtml.includes('document.elementFromPoint(e.clientX, e.clientY)'), 'PASS: document.elementFromPoint hit-testing implemented under pointer capture');
assert(chordHtml.includes("liveSvg.addEventListener('focusin'"), 'PASS: focusin event handling implemented for chord elements');
assert(chordHtml.includes('const prevGroup = activeHoveredGroup') && chordHtml.includes('activeHoveredGroup = null'), 'PASS: Standalone SVG copy resets transient hover state before exporting markup');

// 3. Audit Waterfall Chart Unit Formatting & Step Focus
console.log('\n--- Audit 3: Waterfall Chart Unit Formatting & Step Keyboard Focus ---');
const wfHtml = fs.readFileSync('articles/svg-waterfall-charts-and-financial-variance-bridge-guide/index.html', 'utf8');

assert(wfHtml.includes("unitPrefix: ''") && wfHtml.includes("unitSuffix: '%'"), 'PASS: Gross Margin Walk dataset specifies percentage units (% without $) in DATASETS');
assert(wfHtml.includes('data-step-idx="${i}" tabindex="0" role="graphics-symbol"'), 'PASS: Waterfall bars have tabindex="0" and role="graphics-symbol"');
assert(wfHtml.includes("liveSvg.addEventListener('focusin'"), 'PASS: focusin listener implemented for waterfall steps');

// 4. Test Runtime V8 Execution of Fixed Studios
console.log('\n--- Audit 4: V8 Headless Execution of Interactive Studios ---');

function testV8Studio(slug, content) {
  const scriptMatch = content.match(/<script(?![^>]*application\/ld\+json)[^>]*>([\s\S]*?)<\/script>/i);
  assert(scriptMatch, `Script block present in ${slug}`);
  const jsCode = scriptMatch[1];

  const elements = {};
  const idMatches = [...content.matchAll(/<([a-zA-Z0-9\-]+)[^>]*\sid=["']([^"']+)["'][^>]*>/gi)];
  for (const m of idMatches) {
    const el = {
      tagName: m[1].toUpperCase(),
      id: m[2],
      attributes: { id: m[2] },
      listeners: {},
      style: {},
      innerHTML: '',
      textContent: '',
      value: '',
      addEventListener(ev, fn) {
        if (!this.listeners[ev]) this.listeners[ev] = [];
        this.listeners[ev].push(fn);
      },
      dispatchEvent(e) {
        for (const fn of this.listeners[e.type] || []) fn(e);
      },
      setPointerCapture() {},
      releasePointerCapture() {},
      getBoundingClientRect() { return { left: 0, top: 0, width: 760, height: 520 }; },
      querySelector(sel) { return null; },
      closest(sel) { return null; },
      appendChild(c) { return c; },
      removeChild(c) { return c; },
      select() {}
    };
    Object.defineProperty(el, 'outerHTML', {
      get() { return `<${m[1]} id="${m[2]}">${this.innerHTML}</${m[1]}>`; }
    });
    elements[m[2]] = el;
  }

  const sandbox = {
    document: {
      documentElement: { getAttribute: () => 'dark', setAttribute: () => {} },
      body: { appendChild: () => {}, removeChild: () => {} },
      getElementById: (id) => elements[id] || null,
      querySelector: (sel) => elements[sel.replace('#', '')] || null,
      querySelectorAll: () => [],
      createElement: () => ({ style: {}, appendChild: () => {}, removeChild: () => {}, select: () => {} }),
      elementFromPoint: () => null,
      activeElement: null
    },
    window: { addEventListener: () => {} },
    localStorage: { getItem: () => null, setItem: () => {} },
    navigator: { clipboard: { writeText: () => Promise.resolve() } },
    console: { log: () => {}, error: () => {}, warn: () => {} },
    setTimeout: (fn) => fn(),
    clearTimeout: () => {},
    Math, parseInt, parseFloat, JSON, Promise, Date
  };

  const context = vm.createContext(sandbox);
  vm.runInContext(jsCode, context);
  console.log(`  [PASS] ${slug} executed cleanly in V8 runtime`);

  // Dispatch all interactive events
  for (const [id, el] of Object.entries(elements)) {
    if (el.listeners['change']) el.dispatchEvent({ type: 'change' });
    if (el.listeners['input']) el.dispatchEvent({ type: 'input' });
    if (el.listeners['click']) el.dispatchEvent({ type: 'click', target: el });
    if (el.listeners['focusin']) el.dispatchEvent({ type: 'focusin', target: el });
    if (el.listeners['focusout']) el.dispatchEvent({ type: 'focusout', target: el, relatedTarget: null });
    if (el.listeners['keydown']) el.dispatchEvent({ type: 'keydown', key: 'ArrowUp', target: el, preventDefault: () => {} });
  }
  console.log(`  [PASS] ${slug} event dispatches (change, input, click, focusin, focusout, keydown) executed cleanly`);
}

testV8Studio('svg-waterfall-charts-and-financial-variance-bridge-guide', wfHtml);
testV8Studio('svg-chord-diagrams-and-bilateral-flow-matrix-guide', chordHtml);
testV8Studio('svg-ternary-plots-and-triangular-composition-diagram-guide', terHtml);

console.log('\n======================================================');
console.log('ALL SKEPTICAL REVIEWER AUDIT CHECKS PASSED PERFECTLY!');
console.log('======================================================\n');
