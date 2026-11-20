const assert = require('assert');

console.log('=== TESTING NOVEMBER 20, 2026 STUDIOS RUNTIME MATH & ACCESSIBILITY ===\n');

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
// TEST 1: BOX PLOT & WHISKER CALCULUS
// ==========================================
console.log('--- Testing Box Plot & Whisker Calculus ---');

function computeQuantile(sortedArr, p) {
  if (!sortedArr.length) return 0;
  const n = sortedArr.length;
  if (p <= 0) return sortedArr[0];
  if (p >= 1) return sortedArr[n - 1];
  const idx = p * (n - 1);
  const low = Math.floor(idx);
  const high = Math.ceil(idx);
  const weight = idx - low;
  return sortedArr[low] + weight * (sortedArr[high] - sortedArr[low]);
}

const sampleData = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
const q1 = computeQuantile(sampleData, 0.25);
const med = computeQuantile(sampleData, 0.50);
const q3 = computeQuantile(sampleData, 0.75);
const iqr = q3 - q1;

// With 10 elements:
// p=0.25 -> idx = 0.25 * 9 = 2.25. sampleData[2]=30, sampleData[3]=40. 30 + 0.25 * 10 = 32.5
// p=0.50 -> idx = 0.50 * 9 = 4.50. sampleData[4]=50, sampleData[5]=60. 50 + 0.50 * 10 = 55.0
// p=0.75 -> idx = 0.75 * 9 = 6.75. sampleData[6]=70, sampleData[7]=80. 70 + 0.75 * 10 = 77.5
assert.strictEqual(q1, 32.5);
assert.strictEqual(med, 55.0);
assert.strictEqual(q3, 77.5);
assert.strictEqual(iqr, 45.0);
console.log('  [PASS] Type 7 linear interpolation quantiles verified');

// Tukey 1.5 IQR Fences
const lowerFence = q1 - 1.5 * iqr; // 32.5 - 67.5 = -35.0
const upperFence = q3 + 1.5 * iqr; // 77.5 + 67.5 = 145.0
assert.strictEqual(lowerFence, -35.0);
assert.strictEqual(upperFence, 145.0);

const testSetWithOutliers = [-50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200];
const outliers = testSetWithOutliers.filter(v => v < lowerFence || v > upperFence);
assert.deepStrictEqual(outliers, [-50, 200]);
console.log('  [PASS] Tukey 1.5 * IQR fence outlier boundary filtering verified');

// McGill Notched 95% Confidence Interval
const notchSpan = (1.57 * iqr) / Math.sqrt(sampleData.length);
// 1.57 * 45 / sqrt(10) = 70.65 / 3.162277 = 22.34
assert.strictEqual(+notchSpan.toFixed(2), 22.34);
console.log('  [PASS] McGill notched 95% confidence interval waist span verified');

// Cartesian Inverted Viewport Projector
function mapBoxY(v, minVal, maxVal, viewH, padTop, padBottom) {
  const plotH = viewH - padTop - padBottom;
  const norm = (v - minVal) / (maxVal - minVal || 1);
  return (viewH - padBottom) - norm * plotH;
}
assert.strictEqual(mapBoxY(0, 0, 100, 480, 40, 50), 430); // Min maps to 480 - 50 = 430
assert.strictEqual(mapBoxY(100, 0, 100, 480, 40, 50), 40); // Max maps to 40 (top margin)
console.log('  [PASS] Inverted Cartesian coordinate mapping verified');


// ==========================================
// TEST 2: AREA CHART & STREAMGRAPH CALCULUS
// ==========================================
console.log('\n--- Testing Area Chart & Streamgraph Calculus ---');

// Stack baseline algorithms
const seriesA = [10, 20, 30];
const seriesB = [15, 25, 35];
const totals = seriesA.map((v, i) => v + seriesB[i]); // [25, 45, 65]
assert.deepStrictEqual(totals, [25, 45, 65]);

// Silhouette Baseline (-0.5 * Total)
const silhouetteY0 = totals.map(tot => -0.5 * tot);
assert.deepStrictEqual(silhouetteY0, [-12.5, -22.5, -32.5]);
console.log('  [PASS] Silhouette baseline centering verified');

// Catmull-Rom to Cubic Bézier conversion
function catmullRomToCubicBezier(p0, p1, p2, p3, tension = 0.65) {
  const cp1x = p1.x + (p2.x - p0.x) / (6 * tension);
  const cp1y = p1.y + (p2.y - p0.y) / (6 * tension);
  const cp2x = p2.x - (p3.x - p1.x) / (6 * tension);
  const cp2y = p2.y - (p3.y - p1.y) / (6 * tension);
  return {
    cp1x: +cp1x.toFixed(2),
    cp1y: +cp1y.toFixed(2),
    cp2x: +cp2x.toFixed(2),
    cp2y: +cp2y.toFixed(2)
  };
}

const pts = [
  { x: 0, y: 100 },
  { x: 100, y: 150 },
  { x: 200, y: 120 },
  { x: 300, y: 180 }
];
const bezierCP = catmullRomToCubicBezier(pts[0], pts[1], pts[2], pts[3], 1.0);
// p1=(100, 150), p2=(200, 120), p0=(0, 100), p3=(300, 180)
// cp1 = (100 + (200 - 0)/6, 150 + (120 - 100)/6) = (133.33, 153.33)
// cp2 = (200 - (300 - 100)/6, 120 - (180 - 150)/6) = (166.67, 115.00)
assert.strictEqual(bezierCP.cp1x, 133.33);
assert.strictEqual(bezierCP.cp1y, 153.33);
assert.strictEqual(bezierCP.cp2x, 166.67);
assert.strictEqual(bezierCP.cp2y, 115.0);
console.log('  [PASS] Catmull-Rom to cubic Bézier control point conversion verified');

// 100% Normalized Area Layer Calculus
function normalizeAreaValues(valuesAtStep, totalAtStep) {
  return valuesAtStep.map(v => +( (v / totalAtStep) * 100 ).toFixed(2));
}
const normSlice = normalizeAreaValues([10, 30, 60], 100);
assert.deepStrictEqual(normSlice, [10.0, 30.0, 60.0]);
assert.strictEqual(normSlice.reduce((a, b) => a + b, 0), 100.0);
console.log('  [PASS] 100% normalized proportional area layer calculus verified');


// ==========================================
// TEST 3: PARALLEL COORDINATES PROJECTIVE DUALITY
// ==========================================
console.log('\n--- Testing Parallel Coordinates Projective Duality ---');

// Alfred Inselberg Point-Line Duality
// Line y = mx + b in Cartesian space maps to point (d / (1 - m), b / (1 - m)) in parallel coordinate space
function inselbergDualPoint(m, b, d = 100) {
  const xParallel = d / (1 - m);
  const yParallel = b / (1 - m);
  return {
    x: +xParallel.toFixed(2),
    y: +yParallel.toFixed(2)
  };
}

// Negative correlation: slope m = -1, intercept b = 50. d = 100
// Dual point = (100 / (1 - (-1)), 50 / (1 - (-1))) = (100 / 2, 50 / 2) = (50, 25)
// Exactly halfway between the two parallel axes!
const dualNeg = inselbergDualPoint(-1, 50, 100);
assert.strictEqual(dualNeg.x, 50.0);
assert.strictEqual(dualNeg.y, 25.0);
console.log('  [PASS] Inselberg point-line projective duality internal intersection verified');

// Multi-Axis Conjunction Filter (Logical AND gate)
function evaluateConjunctionFilter(record, brushes) {
  for (const [key, range] of Object.entries(brushes)) {
    const val = record[key];
    if (val < range[0] || val > range[1]) return false;
  }
  return true;
}

const rec1 = { cpu: 45, ram: 16, latency: 40 };
const rec2 = { cpu: 85, ram: 32, latency: 120 };
const brushes = { cpu: [20, 60], ram: [8, 24] };

assert.strictEqual(evaluateConjunctionFilter(rec1, brushes), true);
assert.strictEqual(evaluateConjunctionFilter(rec2, brushes), false);
console.log('  [PASS] Multi-axis conjunction range brush filtering verified');

// Horizontal Tangency Cubic Spline Control Points
function computeHorizontalTangencyControl(x1, y1, x2, y2) {
  const midX = (x1 + x2) / 2;
  return {
    cp1: { x: +midX.toFixed(2), y: +y1.toFixed(2) },
    cp2: { x: +midX.toFixed(2), y: +y2.toFixed(2) }
  };
}
const ht = computeHorizontalTangencyControl(100, 200, 300, 400);
assert.strictEqual(ht.cp1.x, 200.0);
assert.strictEqual(ht.cp1.y, 200.0);
assert.strictEqual(ht.cp2.x, 200.0);
assert.strictEqual(ht.cp2.y, 400.0);
console.log('  [PASS] Parallel coordinate horizontal tangency control points verified');


// ==========================================
// TEST 4: ACCESSIBILITY & CONTRAST (WCAG 2.2 AA)
// ==========================================
console.log('\n--- Testing Color Contrast Ratios (WCAG 2.2 AA Requirement >= 4.5:1) ---');

const bgDark = '#0A0A0A';
const bgLight = '#FAFAFA';
const primaryDark = '#C1DD2D';
const primaryLight = '#4D6300';
const accentCyan = '#38BDF8';
const textLight = '#F2F2F2';
const textDark = '#171717';

const contrastPrimaryDark = contrastRatio(primaryDark, bgDark);
const contrastPrimaryLight = contrastRatio(primaryLight, bgLight);
const contrastAccentDark = contrastRatio(accentCyan, bgDark);
const contrastTextDark = contrastRatio(textLight, bgDark);
const contrastTextLight = contrastRatio(textDark, bgLight);

console.log(`  Dark Mode Primary (#C1DD2D on #0A0A0A): ${contrastPrimaryDark.toFixed(2)}:1`);
assert.ok(contrastPrimaryDark >= 4.5, 'Primary color must meet 4.5:1 on dark');

console.log(`  Light Mode Link (#4D6300 on #FAFAFA): ${contrastPrimaryLight.toFixed(2)}:1`);
assert.ok(contrastPrimaryLight >= 4.5, 'Light mode link must meet 4.5:1 on light');

console.log(`  Accent Cyan (#38BDF8 on #0A0A0A): ${contrastAccentDark.toFixed(2)}:1`);
assert.ok(contrastAccentDark >= 4.5, 'Accent cyan must meet 4.5:1 on dark');

console.log(`  Body Text Dark (#F2F2F2 on #0A0A0A): ${contrastTextDark.toFixed(2)}:1`);
assert.ok(contrastTextDark >= 7.0, 'Body text should satisfy AAA level on dark');

console.log(`  Body Text Light (#171717 on #FAFAFA): ${contrastTextLight.toFixed(2)}:1`);
assert.ok(contrastTextLight >= 7.0, 'Body text should satisfy AAA level on light');

console.log('  [PASS] All color contrast ratios strictly satisfy WCAG 2.2 AA standards');

// ==========================================
// TEST 5: STATISTICAL EDGE CASES & RESILIENCE
// ==========================================
console.log('\n--- Testing Statistical Edge Cases & Resilience ---');

// 1. Box plot zero-variance invariant distribution
const invariantData = [50, 50, 50, 50, 50];
const invQ1 = computeQuantile(invariantData, 0.25);
const invMed = computeQuantile(invariantData, 0.50);
const invQ3 = computeQuantile(invariantData, 0.75);
const invIqr = invQ3 - invQ1;
assert.strictEqual(invIqr, 0);
assert.strictEqual(invMed, 50);
const invNotchSpan = (1.57 * invIqr) / Math.sqrt(invariantData.length || 1);
assert.strictEqual(invNotchSpan, 0);
const invNotchTop = Math.min(invQ3, invMed + invNotchSpan);
const invNotchBot = Math.max(invQ1, invMed - invNotchSpan);
assert.strictEqual(invNotchTop, 50);
assert.strictEqual(invNotchBot, 50);
console.log('  [PASS] Box plot zero-variance invariant distribution handled cleanly');

// 2. Box plot small sample size N=4 with notch span exceeding IQR
const smallSet = [10, 20, 80, 90];
const smallQ1 = computeQuantile(smallSet, 0.25); // 17.5
const smallMed = computeQuantile(smallSet, 0.50); // 50
const smallQ3 = computeQuantile(smallSet, 0.75); // 82.5
const smallIqr = smallQ3 - smallQ1; // 65
const smallNotchSpan = (1.57 * smallIqr) / Math.sqrt(4); // 1.57 * 65 / 2 = 51.025
// median + notchSpan = 101.025 which exceeds Q3 (82.5)
const clampedTop = Math.min(smallQ3, smallMed + smallNotchSpan);
const clampedBot = Math.max(smallQ1, smallMed - smallNotchSpan);
assert.strictEqual(clampedTop, smallQ3, 'Notch top clamped cleanly to Q3 hinge');
assert.strictEqual(clampedBot, smallQ1, 'Notch bottom clamped cleanly to Q1 hinge');
console.log('  [PASS] McGill notched waist clamping on small sample sizes (N=4) verified');

// 3. Catmull-Rom zero-tension division-by-zero protection
function safeCubicControls(p0, p1, p2, p3, tension) {
  const safeT = Math.max(0.05, tension || 0.65);
  const cp1x = p1.x + (p2.x - p0.x) / (6 * safeT);
  const cp1y = p1.y + (p2.y - p0.y) / (6 * safeT);
  return { cp1x: isFinite(cp1x), cp1y: isFinite(cp1y) };
}
const zeroTensionRes = safeCubicControls({x: 0, y: 0}, {x: 10, y: 10}, {x: 20, y: 20}, {x: 30, y: 30}, 0);
assert.ok(zeroTensionRes.cp1x && zeroTensionRes.cp1y, 'Safe tension avoids Infinity/NaN');
console.log('  [PASS] Catmull-Rom zero-tension division-by-zero guard verified');

// 4. Parallel coordinates invariant axis (min === max)
function scaleParallelY(dim, val, viewH = 480, padBottom = 60, plotH = 370) {
  const norm = (val - dim.min) / ((dim.max - dim.min) || 1);
  return (viewH - padBottom) - norm * plotH;
}
const invDim = { min: 100, max: 100 };
const invY = scaleParallelY(invDim, 100);
assert.strictEqual(invY, 420); // Finite baseline, no NaN or Infinity
assert.ok(!isNaN(invY) && isFinite(invY), 'Invariant axis produces finite coordinate');
console.log('  [PASS] Parallel coordinates zero-variance axis (min === max) verified');

// 5. Slider synchronization logic
function syncSliders(minVal, maxVal) {
  let bMin = minVal;
  let bMax = maxVal;
  if (bMin > bMax - 5) {
    bMax = Math.min(100, bMin + 5);
  }
  return { bMin, bMax, gap: bMax - bMin };
}
const synced = syncSliders(80, 70);
assert.ok(synced.gap >= 5, 'Slider sync maintains >= 5% positive brush interval');
assert.strictEqual(synced.bMax, 85);
console.log('  [PASS] Dual-range brush slider synchronization verified');

console.log('\n======================================================');
console.log('ALL NOVEMBER 20 RUNTIME STUDIO TESTS & MATH PASSED!');
console.log('======================================================\n');
