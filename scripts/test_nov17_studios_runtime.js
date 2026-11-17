const assert = require('assert');

console.log('=== TESTING NOVEMBER 17, 2026 STUDIOS RUNTIME MATH & ACCESSIBILITY ===\n');

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
// TEST 1: DONUT CHART STUDIO MATH & TRIGONOMETRY
// ==========================================
console.log('--- Testing Donut Chart Studio Math & Geometry ---');

function polarToCartesian(cx, cy, r, angleRad) {
  return {
    x: +(cx + r * Math.cos(angleRad)).toFixed(2),
    y: +(cy + r * Math.sin(angleRad)).toFixed(2)
  };
}

// 4-quadrant check for angle offsets (standard Cartesian: 0 is right, pi/2 is down in SVG)
const pRight = polarToCartesian(200, 200, 100, 0);
assert.strictEqual(pRight.x, 300.0);
assert.strictEqual(pRight.y, 200.0);

const pBottom = polarToCartesian(200, 200, 100, Math.PI / 2);
assert.strictEqual(pBottom.x, 200.0);
assert.strictEqual(pBottom.y, 300.0);

const pLeft = polarToCartesian(200, 200, 100, Math.PI);
assert.strictEqual(pLeft.x, 100.0);
assert.strictEqual(pLeft.y, 200.0);

const pTop = polarToCartesian(200, 200, 100, (3 * Math.PI) / 2);
assert.strictEqual(pTop.x, 200.0);
assert.strictEqual(pTop.y, 100.0);
console.log('  [PASS] Polar to Cartesian 4-quadrant coordinate conversion verified');

// Circumference & Stroke-Dasharray Math
const radius = 100;
const circumference = 2 * Math.PI * radius;
assert.strictEqual(+circumference.toFixed(2), 628.32);

function calculateDasharray(percent, totalCircumference, gutterGap = 0) {
  const arcLength = (percent / 100) * totalCircumference;
  const dash = Math.max(0, arcLength - gutterGap);
  const gap = totalCircumference - dash;
  return { dash: +dash.toFixed(2), gap: +gap.toFixed(2) };
}

// 25% slice with 0 gap
const slice25 = calculateDasharray(25, circumference, 0);
assert.strictEqual(slice25.dash, +(0.25 * circumference).toFixed(2));
assert.strictEqual(slice25.gap, +(0.75 * circumference).toFixed(2));

// 50% slice with 4px gutter gap
const slice50 = calculateDasharray(50, circumference, 4);
assert.strictEqual(slice50.dash, +(0.50 * circumference - 4).toFixed(2));
assert.strictEqual(slice50.gap, +(0.50 * circumference + 4).toFixed(2));
console.log('  [PASS] Stroke-dasharray and gutter gap calculations verified');

// Annular Path Construction
function generateAnnularSlice(cx, cy, rOuter, rInner, startAngleRad, endAngleRad) {
  const p1 = polarToCartesian(cx, cy, rOuter, startAngleRad);
  const p2 = polarToCartesian(cx, cy, rOuter, endAngleRad);
  const p3 = polarToCartesian(cx, cy, rInner, endAngleRad);
  const p4 = polarToCartesian(cx, cy, rInner, startAngleRad);
  const largeArc = endAngleRad - startAngleRad > Math.PI ? 1 : 0;

  return `M ${p1.x} ${p1.y} A ${rOuter} ${rOuter} 0 ${largeArc} 1 ${p2.x} ${p2.y} L ${p3.x} ${p3.y} A ${rInner} ${rInner} 0 ${largeArc} 0 ${p4.x} ${p4.y} Z`;
}

const annularSlice = generateAnnularSlice(200, 200, 120, 80, 0, Math.PI / 2);
assert.ok(annularSlice.startsWith('M 320 200 A 120 120 0 0 1 200 320 L 200 280 A 80 80 0 0 0 280 200 Z'));
console.log('  [PASS] Annular slice SVG path construction verified');

// Slice Explosion Vector
function getExplosionOffset(midAngleRad, distance) {
  return {
    dx: +(Math.cos(midAngleRad) * distance).toFixed(2),
    dy: +(Math.sin(midAngleRad) * distance).toFixed(2)
  };
}
const expRight = getExplosionOffset(0, 15);
assert.strictEqual(expRight.dx, 15.0);
assert.strictEqual(expRight.dy, 0.0);
console.log('  [PASS] Slice explosion displacement vector verified');


// ==========================================
// TEST 2: BAR CHART STUDIO MATH & COORDINATES
// ==========================================
console.log('\n--- Testing Bar Chart Studio Math & Layouts ---');

// Cartesian Inverted Y-Mapping
function mapValueToY(val, maxVal, height, padding) {
  const drawableH = height - 2 * padding;
  const ratio = Math.max(0, Math.min(1, val / maxVal));
  const barH = ratio * drawableH;
  const y = padding + (1 - ratio) * drawableH;
  return { y: +y.toFixed(2), height: +barH.toFixed(2) };
}

// Total height 300, padding 30, drawable 240, maxVal 100
const barZero = mapValueToY(0, 100, 300, 30);
assert.strictEqual(barZero.y, 270.0);
assert.strictEqual(barZero.height, 0.0);

const barHalf = mapValueToY(50, 100, 300, 30);
assert.strictEqual(barHalf.y, 150.0);
assert.strictEqual(barHalf.height, 120.0);

const barFull = mapValueToY(100, 100, 300, 30);
assert.strictEqual(barFull.y, 30.0);
assert.strictEqual(barFull.height, 240.0);
console.log('  [PASS] Inverted Cartesian Y-mapping and bar heights verified');

// Grouped Series Sub-Slot Mapping
function computeGroupedBars(categories, seriesCount, width, padding, groupGapRatio) {
  const numCats = categories.length;
  const drawableW = width - 2 * padding;
  const slotWidth = drawableW / numCats;
  const usableSlotW = slotWidth * (1 - groupGapRatio);
  const barWidth = usableSlotW / seriesCount;

  const results = [];
  for (let c = 0; c < numCats; c++) {
    const slotX = padding + c * slotWidth + (slotWidth * groupGapRatio) / 2;
    for (let s = 0; s < seriesCount; s++) {
      const barX = slotX + s * barWidth;
      results.push({ category: c, series: s, x: +barX.toFixed(2), width: +barWidth.toFixed(2) });
    }
  }
  return results;
}

const grouped = computeGroupedBars(['Q1', 'Q2', 'Q3', 'Q4'], 3, 500, 20, 0.2);
assert.strictEqual(grouped.length, 12);
// Slot width is (500 - 40) / 4 = 115. Gap is 23, usable is 92. Bar width = 92 / 3 = 30.67
assert.strictEqual(grouped[0].width, 30.67);
assert.strictEqual(grouped[0].x, +(20 + 11.5).toFixed(2));
console.log('  [PASS] Grouped series sub-slot distribution verified');

// Stacked Bar Height Accumulation
function computeStackedBars(segments, maxTotalVal, height, padding) {
  const drawableH = height - 2 * padding;
  let currentY = height - padding;
  return segments.map(val => {
    const segH = (val / maxTotalVal) * drawableH;
    currentY -= segH;
    return { y: +currentY.toFixed(2), height: +segH.toFixed(2) };
  });
}

const stacked = computeStackedBars([30, 50, 20], 100, 300, 30);
assert.strictEqual(stacked.length, 3);
assert.strictEqual(stacked[0].height, +(0.3 * 240).toFixed(2)); // 72
assert.strictEqual(stacked[1].height, +(0.5 * 240).toFixed(2)); // 120
assert.strictEqual(stacked[2].height, +(0.2 * 240).toFixed(2)); // 48
assert.strictEqual(stacked[2].y, 30.0); // Top of the stack reaches y = 30 (100% of height)
console.log('  [PASS] Stacked bar cumulative height accumulation verified');


// ==========================================
// TEST 3: SPARKLINES & MICRO-CHARTS MATH
// ==========================================
console.log('\n--- Testing Sparklines & Micro-Charts Studio Math ---');

// Normalization with Flatline Guard
function normalizePoints(values, width, height, padding, forceZero = false) {
  const n = values.length;
  const minVal = forceZero ? Math.min(0, ...values) : Math.min(...values);
  const maxVal = Math.max(...values);
  const range = (maxVal - minVal) || 1;

  return values.map((val, i) => {
    const x = padding + (n > 1 ? (i / (n - 1)) * (width - 2 * padding) : (width / 2));
    const y = padding + (1 - (val - minVal) / range) * (height - 2 * padding);
    return { x: +x.toFixed(2), y: +y.toFixed(2), val };
  });
}

const ptsNorm = normalizePoints([10, 30, 20, 50], 300, 100, 10);
assert.strictEqual(ptsNorm.length, 4);
assert.strictEqual(ptsNorm[0].x, 10.0);
assert.strictEqual(ptsNorm[0].y, 90.0); // minVal 10 maps to bottom: 10 + (1 - 0) * 80 = 90
assert.strictEqual(ptsNorm[3].x, 290.0);
assert.strictEqual(ptsNorm[3].y, 10.0); // maxVal 50 maps to top: 10 + (1 - 1) * 80 = 10

// Flatline dataset test
const flatline = normalizePoints([42, 42, 42, 42], 300, 100, 10);
assert.strictEqual(flatline[0].y, 90.0); // With range fallback to 1, val - min is 0, maps safely without NaN
console.log('  [PASS] Sparkline range normalization & flatline guard verified');

// Catmull-Rom Spline Control Point Derivation
function computeCatmullRomControlPoints(p0, p1, p2, p3) {
  return {
    cp1x: +(p1.x + (p2.x - p0.x) / 6).toFixed(2),
    cp1y: +(p1.y + (p2.y - p0.y) / 6).toFixed(2),
    cp2x: +(p2.x - (p3.x - p1.x) / 6).toFixed(2),
    cp2y: +(p2.y - (p3.y - p1.y) / 6).toFixed(2)
  };
}

const p0 = { x: 0, y: 100 };
const p1 = { x: 50, y: 50 };
const p2 = { x: 100, y: 60 };
const p3 = { x: 150, y: 20 };
const cp = computeCatmullRomControlPoints(p0, p1, p2, p3);

assert.strictEqual(cp.cp1x, +(50 + (100 - 0) / 6).toFixed(2));
assert.strictEqual(cp.cp1y, +(50 + (60 - 100) / 6).toFixed(2));
assert.strictEqual(cp.cp2x, +(100 - (150 - 50) / 6).toFixed(2));
assert.strictEqual(cp.cp2y, +(60 - (20 - 50) / 6).toFixed(2));
console.log('  [PASS] Catmull-Rom C1 continuous control point calculus verified');

// Closed Area Path Generation
function getAreaClosedPath(pts, width, height, padding) {
  const firstX = pts[0].x;
  const lastX = pts[pts.length - 1].x;
  const baseH = height - padding;
  let lineCommands = pts.map((p, i) => `${i === 0 ? 'M' : 'L'} ${p.x} ${p.y}`).join(' ');
  return `M ${firstX} ${baseH} L ${firstX} ${pts[0].y} ${lineCommands.substring(lineCommands.indexOf(' '))} L ${lastX} ${baseH} Z`;
}

const closedArea = getAreaClosedPath(ptsNorm, 300, 100, 10);
assert.ok(closedArea.startsWith('M 10 90 L 10 90'));
assert.ok(closedArea.endsWith('L 290 90 Z'));
console.log('  [PASS] Airtight area gradient polygon closure verified');


// ==========================================
// TEST 4: ACCESSIBILITY & CONTRAST (WCAG 2.2 AA)
// ==========================================
console.log('\n--- Testing Color Contrast Ratios (WCAG 2.2 AA Requirement >= 4.5:1) ---');

const bgDark = '#090A0F';
const bgLight = '#FFFFFF';
const primaryDark = '#C1DD2D'; // Brand lime on dark
const primaryLight = '#4D6300'; // Olive green on light
const accentCyan = '#38BDF8';
const textLight = '#F3F4F6';
const textDark = '#0F172A';

const contrastPrimaryDark = contrastRatio(primaryDark, bgDark);
const contrastPrimaryLight = contrastRatio(primaryLight, bgLight);
const contrastAccentDark = contrastRatio(accentCyan, bgDark);
const contrastTextDark = contrastRatio(textLight, bgDark);
const contrastTextLight = contrastRatio(textDark, bgLight);

console.log(`  Dark Mode Primary (#C1DD2D on #090A0F): ${contrastPrimaryDark.toFixed(2)}:1`);
assert.ok(contrastPrimaryDark >= 4.5, 'Primary color must meet 4.5:1 on dark');

console.log(`  Light Mode Link (#4D6300 on #FFFFFF): ${contrastPrimaryLight.toFixed(2)}:1`);
assert.ok(contrastPrimaryLight >= 4.5, 'Light mode link must meet 4.5:1 on white');

console.log(`  Accent Cyan (#38BDF8 on #090A0F): ${contrastAccentDark.toFixed(2)}:1`);
assert.ok(contrastAccentDark >= 4.5, 'Accent color must meet 4.5:1 on dark');

console.log(`  Light Text on Dark (#F3F4F6 on #090A0F): ${contrastTextDark.toFixed(2)}:1`);
assert.ok(contrastTextDark >= 7.0, 'Body text should meet AAA level (>= 7:1) on dark');

console.log(`  Dark Text on Light (#0F172A on #FFFFFF): ${contrastTextLight.toFixed(2)}:1`);
assert.ok(contrastTextLight >= 7.0, 'Body text should meet AAA level (>= 7:1) on light');

console.log('  [PASS] All color contrast ratios strictly satisfy WCAG 2.2 AA standards');

console.log('\n======================================================');
console.log('ALL RUNTIME STUDIO TESTS & ACCESSIBILITY AUDITS PASSED!');
console.log('======================================================\n');
