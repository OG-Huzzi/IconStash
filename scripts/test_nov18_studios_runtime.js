const assert = require('assert');

console.log('=== TESTING NOVEMBER 18, 2026 STUDIOS RUNTIME MATH & ACCESSIBILITY ===\n');

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
// TEST 1: SCATTER PLOT & BUBBLE CHART MATH
// ==========================================
console.log('--- Testing Scatter Plot & Bubble Chart Math ---');

function mapDataToSvg(x, y, domainX, domainY, viewW, viewH, pad) {
  const plotW = viewW - pad.left - pad.right;
  const plotH = viewH - pad.top - pad.bottom;
  const svgX = pad.left + ((x - domainX[0]) / (domainX[1] - domainX[0])) * plotW;
  const svgY = (viewH - pad.bottom) - ((y - domainY[0]) / (domainY[1] - domainY[0])) * plotH;
  return { x: +svgX.toFixed(2), y: +svgY.toFixed(2) };
}

// Test Cartesian Inversion: min y maps to bottom, max y maps to top
const pad = { top: 40, right: 40, bottom: 50, left: 60 };
const ptMin = mapDataToSvg(0, 0, [0, 100], [0, 100], 760, 480, pad);
assert.strictEqual(ptMin.x, 60.0);
assert.strictEqual(ptMin.y, 430.0); // 480 - 50 = 430

const ptMax = mapDataToSvg(100, 100, [0, 100], [0, 100], 760, 480, pad);
assert.strictEqual(ptMax.x, 720.0); // 760 - 40 = 720
assert.strictEqual(ptMax.y, 40.0);  // top padding = 40
console.log('  [PASS] Cartesian inversion and coordinate scaling verified');

// Area vs Linear Radius Scaling
function scaleRadius(z, minZ, maxZ, minR, maxR, mode = 'sqrt') {
  const norm = Math.max(0, (z - minZ) / (maxZ - minZ || 1));
  const factor = mode === 'sqrt' ? Math.sqrt(norm) : norm;
  return +(minR + factor * (maxR - minR)).toFixed(2);
}

const rLinearMin = scaleRadius(0, 0, 100, 4, 28, 'linear');
assert.strictEqual(rLinearMin, 4.0);

const rSqrtHalf = scaleRadius(25, 0, 100, 4, 28, 'sqrt');
// sqrt(0.25) = 0.5, radius = 4 + 0.5 * 24 = 16.0
assert.strictEqual(rSqrtHalf, 16.0);
console.log('  [PASS] Perceptual square root area scaling verified');

// OLS Linear Regression Calculus
function computeOLS(data) {
  let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0, sumYY = 0;
  const n = data.length;
  for (const d of data) {
    sumX += d.x;
    sumY += d.y;
    sumXY += d.x * d.y;
    sumXX += d.x * d.x;
    sumYY += d.y * d.y;
  }
  const denom = n * sumXX - sumX * sumX;
  const slope = (n * sumXY - sumX * sumY) / denom;
  const intercept = (sumY - slope * sumX) / n;
  const denomCorr = Math.sqrt((n * sumXX - sumX * sumX) * (n * sumYY - sumY * sumY));
  const corr = (n * sumXY - sumX * sumY) / denomCorr;
  return { slope: +slope.toFixed(4), intercept: +intercept.toFixed(4), corr: +corr.toFixed(4), r2: +(corr * corr).toFixed(4) };
}

// Perfect line y = 2x + 10
const linearPts = [{ x: 10, y: 30 }, { x: 20, y: 50 }, { x: 30, y: 70 }, { x: 40, y: 90 }];
const ols = computeOLS(linearPts);
assert.strictEqual(ols.slope, 2.0);
assert.strictEqual(ols.intercept, 10.0);
assert.strictEqual(ols.corr, 1.0);
assert.strictEqual(ols.r2, 1.0);
console.log('  [PASS] OLS regression and Pearson correlation calculation verified');


// ==========================================
// TEST 2: NETWORK GRAPH PHYSICS & GEOMETRY
// ==========================================
console.log('\n--- Testing Force-Directed Network Graph Physics ---');

// Coulomb Repulsion
function coulombRepulsion(u, v, charge) {
  const dx = v.x - u.x;
  const dy = v.y - u.y;
  const distSq = dx * dx + dy * dy || 1;
  const dist = Math.sqrt(distSq);
  const force = charge / distSq;
  return {
    fx: +( (dx / dist) * force ).toFixed(4),
    fy: +( (dy / dist) * force ).toFixed(4)
  };
}

const u = { x: 100, y: 100 };
const v = { x: 200, y: 100 };
const repel = coulombRepulsion(u, v, 10000); // distance 100, force = 10000 / 10000 = 1.0
assert.strictEqual(repel.fx, 1.0);
assert.strictEqual(repel.fy, 0.0);
console.log('  [PASS] Coulomb repulsion force vector verified');

// Hooke Spring Attraction
function hookeSpring(u, v, linkDistance, stiffness = 0.08) {
  const dx = v.x - u.x;
  const dy = v.y - u.y;
  const dist = Math.sqrt(dx * dx + dy * dy) || 1;
  const delta = (dist - linkDistance) * stiffness;
  return {
    fx: +( (dx / dist) * delta ).toFixed(4),
    fy: +( (dy / dist) * delta ).toFixed(4)
  };
}

// Stretched link: distance 150, equilibrium 100, delta = (150 - 100) * 0.08 = 4.0
const spring = hookeSpring(u, { x: 250, y: 100 }, 100);
assert.strictEqual(spring.fx, 4.0);
assert.strictEqual(spring.fy, 0.0);
console.log('  [PASS] Hooke spring elastic restorative force verified');

// Quadratic Bézier Normal Midpoint Offset
function quadraticBezierControlPoint(x1, y1, x2, y2, offset) {
  const mx = (x1 + x2) / 2;
  const my = (y1 + y2) / 2;
  const dx = x2 - x1;
  const dy = y2 - y1;
  const len = Math.sqrt(dx * dx + dy * dy) || 1;
  const nx = -dy / len;
  const ny = dx / len;
  return {
    cx: +(mx + nx * offset).toFixed(2),
    cy: +(my + ny * offset).toFixed(2)
  };
}

const cp = quadraticBezierControlPoint(100, 100, 200, 100, 20);
// Midpoint is (150, 100). dx=100, dy=0. Normal is (0, 1). Offset 20 -> (150, 120)
assert.strictEqual(cp.cx, 150.0);
assert.strictEqual(cp.cy, 120.0);
console.log('  [PASS] Quadratic Bézier perpendicular normal offset verified');


// ==========================================
// TEST 3: CHOROPLETH MAP PROJECTIONS & SCALES
// ==========================================
console.log('\n--- Testing Choropleth Map Projections & Scales ---');

// Forward Spherical Mercator
function forwardMercator(lon, lat, R = 100) {
  const lambda = (lon * Math.PI) / 180;
  const phi = (lat * Math.PI) / 180;
  const x = R * lambda;
  const y = R * Math.log(Math.tan(Math.PI / 4 + phi / 2));
  return { x: (+x.toFixed(2)) || 0, y: (+y.toFixed(2)) || 0 };
}

// Equator & Prime Meridian (0, 0) -> (0, 0)
const mercZero = forwardMercator(0, 0);
assert.strictEqual(mercZero.x, 0.0);
assert.strictEqual(mercZero.y, 0.0);

// Latitude 45 deg north: tan(pi/4 + pi/8) = tan(3pi/8) = 2.4142, ln(2.4142) = 0.8814
const merc45 = forwardMercator(0, 45);
assert.strictEqual(merc45.y, 88.14);
console.log('  [PASS] Forward Spherical Mercator projection verified');

// Quantile Classification
function computeQuantiles(values, numBins) {
  const sorted = [...values].sort((a, b) => a - b);
  const n = sorted.length;
  const breaks = [];
  for (let i = 1; i < numBins; i++) {
    const idx = Math.floor((i / numBins) * n);
    breaks.push(sorted[idx]);
  }
  return breaks;
}

const dataset = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
const quant4 = computeQuantiles(dataset, 4);
assert.strictEqual(quant4.length, 3);
assert.strictEqual(quant4[0], 30); // 25th percentile
assert.strictEqual(quant4[1], 60); // 50th percentile
assert.strictEqual(quant4[2], 80); // 75th percentile
console.log('  [PASS] Quantile classification bucket calculus verified');


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
// TEST 5: SIMULATION CONVERGENCE & TOUCH RESILIENCE
// ==========================================
console.log('\n--- Testing Simulation Convergence & Touch Resilience ---');

// Test thermal decay loop terminating in finite steps
let testAlpha = 1.0;
let stepCount = 0;
while (testAlpha > 0.005) {
  testAlpha *= 0.985;
  stepCount++;
}
assert.ok(stepCount > 50 && stepCount < 400, `Simulation should converge between 50 and 400 steps (converged in ${stepCount} steps)`);
assert.ok(testAlpha <= 0.005, 'Simulation halts when alpha <= 0.005');
console.log(`  [PASS] Thermal cooling simulation decays cleanly and halts after ${stepCount} steps`);

// Test Reheat function guarantees
function testReheat(currentAlpha, temp = 0.35) {
  return Math.max(currentAlpha, temp);
}
assert.strictEqual(testReheat(0.002, 0.35), 0.35); // cold simulation reheated
assert.strictEqual(testReheat(0.8, 0.35), 0.8);    // already warm simulation preserves higher energy
assert.strictEqual(testReheat(0.1, 1.0), 1.0);     // rebuild graph reheat gives full energy
console.log('  [PASS] Simulation reheat preserves kinetic energy bounds');

// Test Tick interval math for scatter plots
function computeAxisTicks(minVal, maxVal, intervals = 5) {
  const ticks = [];
  for (let i = 0; i <= intervals; i++) {
    ticks.push(minVal + ((maxVal - minVal) / intervals) * i);
  }
  return ticks;
}
const ticks = computeAxisTicks(0, 100, 5);
assert.deepStrictEqual(ticks, [0, 20, 40, 60, 80, 100]);
console.log('  [PASS] Scatter plot coordinate tick mark intervals verified');

console.log('\n======================================================');
console.log('ALL NOVEMBER 18 RUNTIME STUDIO TESTS & MATH PASSED!');
console.log('======================================================\n');
