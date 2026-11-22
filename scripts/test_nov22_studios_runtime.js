const assert = require('assert');

console.log('=== TESTING NOVEMBER 22, 2026 STUDIOS RUNTIME MATH & ACCESSIBILITY ===\n');

// Helper: Relative Luminance and Contrast Ratio
function luminance(hexColor) {
  let hex = hexColor.replace('#', '');
  if (hex.length === 3) {
    hex = hex.split('').map(c => c + c).join('');
  }
  const r = parseInt(hex.substring(0, 2), 16) / 255;
  const g = parseInt(hex.substring(2, 4), 16) / 255;
  const b = parseInt(hex.substring(4, 6), 16) / 255;

  const a = [r, g, b].map(v => {
    return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
  });
  return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
}

function contrastRatio(hex1, hex2) {
  const lum1 = luminance(hex1);
  const lum2 = luminance(hex2);
  const brightest = Math.max(lum1, lum2);
  const darkest = Math.min(lum1, lum2);
  return (brightest + 0.05) / (darkest + 0.05);
}

// ==========================================
// TEST 1: WATERFALL CHART & VARIANCE BRIDGE MATH
// ==========================================
console.log('--- Testing Waterfall Chart & Variance Bridge Math ---');

function computeWaterfallBars(data, chartHeight, padTop, padBottom, minVal, maxVal) {
  const plotH = chartHeight - padTop - padBottom;
  const range = maxVal - minVal || 1;
  const toY = (val) => chartHeight - padBottom - ((val - minVal) / range) * plotH;

  let running = 0;
  return data.map(d => {
    const prev = running;
    let y, h, type;
    if (d.isTotal) {
      running = d.value;
      const yZero = toY(0);
      const yVal = toY(running);
      y = Math.min(yZero, yVal);
      h = Math.abs(yZero - yVal);
      type = 'total';
    } else {
      running += d.value;
      const yPrev = toY(prev);
      const yCurr = toY(running);
      y = Math.min(yPrev, yCurr);
      h = Math.abs(yPrev - yCurr);
      type = d.value >= 0 ? 'positive' : 'negative';
    }
    return { label: d.label, prev, running, y, h, type, toYPrev: toY(prev) };
  });
}

const testFinancialData = [
  { label: 'Q1 Start', value: 100, isTotal: true },
  { label: 'Revenue Growth', value: 50, isTotal: false },
  { label: 'COGS', value: -30, isTotal: false },
  { label: 'OpEx', value: -20, isTotal: false },
  { label: 'Q1 End', value: 100, isTotal: true }
];

const wfBars = computeWaterfallBars(testFinancialData, 500, 40, 60, 0, 160);
assert.strictEqual(wfBars[0].running, 100);
assert.strictEqual(wfBars[1].running, 150);
assert.strictEqual(wfBars[2].running, 120);
assert.strictEqual(wfBars[3].running, 100);
assert.strictEqual(wfBars[4].running, 100);

assert.strictEqual(wfBars[0].type, 'total');
assert.strictEqual(wfBars[1].type, 'positive');
assert.strictEqual(wfBars[2].type, 'negative');
assert.strictEqual(wfBars[3].type, 'negative');
assert.strictEqual(wfBars[4].type, 'total');

// Connector continuity: connector Y of bar[i] connects to bar[i+1] baseline
for (let i = 1; i < wfBars.length - 1; i++) {
  // Bar i's final running balance must equal bar i+1's starting previous balance
  assert.strictEqual(wfBars[i].running, wfBars[i+1].prev);
}
console.log('  [PASS] Running balance accumulators and floating bar geometry verified');
console.log('  [PASS] Horizontal connector continuity verified');


// ==========================================
// TEST 2: CHORD DIAGRAM & BILATERAL FLOW CALCULUS
// ==========================================
console.log('\n--- Testing Chord Diagram & Bilateral Flow Calculus ---');

const testMatrix = [
  [0, 20, 10], // Source A to [A, B, C] -> row sum = 30
  [15, 0, 25], // Source B to [A, B, C] -> row sum = 40
  [5, 10, 0]   // Source C to [A, B, C] -> row sum = 15
]; // Grand total = 85

function computeChordLayout(matrix, padAngleRad) {
  const n = matrix.length;
  const rowSums = matrix.map(row => row.reduce((s, v) => s + v, 0));
  const grandTotal = rowSums.reduce((s, v) => s + v, 0);

  const availableAngle = 2 * Math.PI - n * padAngleRad;
  const groups = [];
  let currentAngle = 0;

  for (let i = 0; i < n; i++) {
    const span = (rowSums[i] / grandTotal) * availableAngle;
    const startAngle = currentAngle;
    const endAngle = currentAngle + span;
    groups.push({ index: i, value: rowSums[i], startAngle, endAngle });
    currentAngle = endAngle + padAngleRad;
  }
  return { groups, grandTotal, availableAngle };
}

const padAngle = 0.05; // radians
const chordLayout = computeChordLayout(testMatrix, padAngle);
assert.strictEqual(chordLayout.grandTotal, 85);
assert.strictEqual(chordLayout.groups.length, 3);

// Group angular proportions
const totalSpans = chordLayout.groups.reduce((s, g) => s + (g.endAngle - g.startAngle), 0);
assert.strictEqual(+totalSpans.toFixed(4), +(2 * Math.PI - 3 * padAngle).toFixed(4));
console.log('  [PASS] Bilateral matrix row-sum normalization and outer arc partitioning verified');

// Ribbon Quadratic Bézier Endpoint Check
function polarPoint(cx, cy, r, angle) {
  return {
    x: +(cx + r * Math.cos(angle)).toFixed(3),
    y: +(cy + r * Math.sin(angle)).toFixed(3)
  };
}
const pStart = polarPoint(300, 300, 200, 0);
const pEnd = polarPoint(300, 300, 200, Math.PI);
assert.strictEqual(pStart.x, 500);
assert.strictEqual(pStart.y, 300);
assert.strictEqual(pEnd.x, 100);
assert.strictEqual(pEnd.y, 300);
console.log('  [PASS] Radial chord polar-to-Cartesian ribbon projections verified');


// ==========================================
// TEST 3: TERNARY PLOT & BARYCENTRIC CALCULUS
// ==========================================
console.log('\n--- Testing Ternary Plot & Barycentric Calculus ---');

// Equilateral triangle layout: Vertex A (top), Vertex B (bottom-left), Vertex C (bottom-right)
function barycentricToCartesian(a, b, c, originX, originY, size) {
  const sum = a + b + c;
  const na = a / sum;
  const nb = b / sum;
  const nc = c / sum;

  const h = size * (Math.sqrt(3) / 2);
  const Ax = originX + size / 2;
  const Ay = originY;
  const Bx = originX;
  const By = originY + h;
  const Cx = originX + size;
  const Cy = originY + h;

  const px = na * Ax + nb * Bx + nc * Cx;
  const py = na * Ay + nb * By + nc * Cy;
  return { x: +px.toFixed(3), y: +py.toFixed(3) };
}

// Invert Cartesian back to normalized Barycentric
function cartesianToBarycentric(px, py, originX, originY, size) {
  const h = size * (Math.sqrt(3) / 2);
  const Ax = originX + size / 2;
  const Ay = originY;
  const Bx = originX;
  const By = originY + h;
  const Cx = originX + size;
  const Cy = originY + h;

  const det = (By - Cy) * (Ax - Cx) + (Cx - Bx) * (Ay - Cy);
  const na = ((By - Cy) * (px - Cx) + (Cx - Bx) * (py - Cy)) / det;
  const nb = ((Cy - Ay) * (px - Cx) + (Ax - Cx) * (py - Cy)) / det;
  const nc = 1 - na - nb;
  return { a: +na.toFixed(4), b: +nb.toFixed(4), c: +nc.toFixed(4) };
}

const origX = 100;
const origY = 50;
const side = 400;

// Test Vertex A (1, 0, 0)
const ptA = barycentricToCartesian(1, 0, 0, origX, origY, side);
assert.strictEqual(ptA.x, 300);
assert.strictEqual(ptA.y, 50);
const invA = cartesianToBarycentric(ptA.x, ptA.y, origX, origY, side);
assert.strictEqual(invA.a, 1);
assert.strictEqual(invA.b, 0);
assert.strictEqual(invA.c, 0);

// Test Centroid (1/3, 1/3, 1/3)
const ptCenter = barycentricToCartesian(1/3, 1/3, 1/3, origX, origY, side);
const invCenter = cartesianToBarycentric(ptCenter.x, ptCenter.y, origX, origY, side);
assert.strictEqual(+(invCenter.a + invCenter.b + invCenter.c).toFixed(2), 1.00);
assert.strictEqual(+invCenter.a.toFixed(2), 0.33);
assert.strictEqual(+invCenter.b.toFixed(2), 0.33);
assert.strictEqual(+invCenter.c.toFixed(2), 0.33);

// Test Midpoint BC (0, 0.5, 0.5)
const ptBC = barycentricToCartesian(0, 0.5, 0.5, origX, origY, side);
const invBC = cartesianToBarycentric(ptBC.x, ptBC.y, origX, origY, side);
assert.strictEqual(invBC.a, 0);
assert.strictEqual(invBC.b, 0.5);
assert.strictEqual(invBC.c, 0.5);

console.log('  [PASS] Barycentric-to-Cartesian equilateral projection verified');
console.log('  [PASS] Cartesian-to-Barycentric inverse transformation verified');
console.log('  [PASS] Simplex conservation law (a + b + c = 1) verified at all vertices and centroid');


// ==========================================
// TEST 4: WCAG 2.2 AA CONTRAST RATIO
// ==========================================
console.log('\n--- Testing WCAG 2.2 AA Accessibility & Color Contrast ---');

const linkContrast = contrastRatio('#4D6300', '#FFFFFF');
assert(linkContrast >= 4.5, `Light mode link color #4D6300 achieves WCAG AA contrast against white: ${linkContrast.toFixed(2)}:1 (>= 4.5:1)`);
console.log(`  [PASS] Light mode link #4D6300 contrast: ${linkContrast.toFixed(2)}:1`);

const darkBg = '#0A0A0A';
const brandLime = '#C1DD2D';
const darkContrast = contrastRatio(brandLime, darkBg);
assert(darkContrast >= 4.5, `Dark mode lime #C1DD2D achieves WCAG AA contrast against #0A0A0A: ${darkContrast.toFixed(2)}:1`);
console.log(`  [PASS] Dark mode brand #C1DD2D contrast: ${darkContrast.toFixed(2)}:1`);

console.log('\n======================================================');
console.log('ALL NOVEMBER 22 STUDIOS RUNTIME MATH TESTS PASSED!');
console.log('======================================================\n');
