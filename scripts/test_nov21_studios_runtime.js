const assert = require('assert');

console.log('=== TESTING NOVEMBER 21, 2026 STUDIOS RUNTIME MATH & ACCESSIBILITY ===\n');

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
// TEST 1: SUNBURST ARC & POLAR CALCULUS
// ==========================================
console.log('--- Testing Sunburst Arc & Polar Calculus ---');

function polarToCartesian(cx, cy, r, angleRad) {
  return {
    x: +(cx + r * Math.cos(angleRad)).toFixed(2),
    y: +(cy + r * Math.sin(angleRad)).toFixed(2)
  };
}

const cx = 380;
const cy = 260;
const r0 = 60;
const r1 = 120;

// Test cardinal points (0, PI/2, PI, 3PI/2)
const p0 = polarToCartesian(cx, cy, r0, 0);
assert.strictEqual(p0.x, 440);
assert.strictEqual(p0.y, 260);

const pQuarter = polarToCartesian(cx, cy, r0, Math.PI / 2);
assert.strictEqual(pQuarter.x, 380);
assert.strictEqual(pQuarter.y, 320);

const pHalf = polarToCartesian(cx, cy, r0, Math.PI);
assert.strictEqual(pHalf.x, 320);
assert.strictEqual(pHalf.y, 260);
console.log('  [PASS] Polar-to-Cartesian cardinal projections verified');

// Test large-arc-flag logic
function computeLargeArcFlag(theta0, theta1) {
  const delta = theta1 - theta0;
  return delta > Math.PI ? 1 : 0;
}
assert.strictEqual(computeLargeArcFlag(0, Math.PI / 2), 0); // 90 deg -> 0
assert.strictEqual(computeLargeArcFlag(0, Math.PI), 0); // 180 deg -> 0
assert.strictEqual(computeLargeArcFlag(0, Math.PI * 1.2), 1); // 216 deg -> 1
console.log('  [PASS] Large-arc-flag boundary evaluation verified');

// Test Proportional Angular Partitioning
const weights = [300, 200, 500]; // Total 1000
const totalW = weights.reduce((s, w) => s + w, 0);
const spans = weights.map(w => (w / totalW) * 2 * Math.PI);
assert.strictEqual(+spans.reduce((s, a) => s + a, 0).toFixed(4), +(2 * Math.PI).toFixed(4));
assert.strictEqual(spans[0], 0.3 * 2 * Math.PI);
assert.strictEqual(spans[1], 0.2 * 2 * Math.PI);
assert.strictEqual(spans[2], 0.5 * 2 * Math.PI);
console.log('  [PASS] Conservation of angular spans across tree partitions verified');


// ==========================================
// TEST 2: VIOLIN PLOT & KDE CALCULUS
// ==========================================
console.log('\n--- Testing Violin Plot & KDE Calculus ---');

function gaussianKernel(u) {
  return (1 / Math.sqrt(2 * Math.PI)) * Math.exp(-0.5 * u * u);
}
// At u=0, K(0) = 1 / sqrt(2*PI) ~= 0.398942
assert.strictEqual(+gaussianKernel(0).toFixed(4), 0.3989);
// At u=1, K(1) = (1 / sqrt(2*PI)) * exp(-0.5) ~= 0.24197
assert.strictEqual(+gaussianKernel(1).toFixed(4), 0.2420);
// Symmetry check: K(-u) == K(u)
assert.strictEqual(gaussianKernel(-1.5), gaussianKernel(1.5));
console.log('  [PASS] Gaussian kernel evaluation and bilateral symmetry verified');

// Silverman Bandwidth Test
function computeSilvermanBandwidth(arr) {
  const n = arr.length;
  const sorted = [...arr].sort((a, b) => a - b);
  const mean = arr.reduce((s, v) => s + v, 0) / n;
  const variance = arr.reduce((s, v) => s + Math.pow(v - mean, 2), 0) / (n - 1);
  const stdDev = Math.sqrt(variance);

  const q1 = sorted[Math.floor(0.25 * (n - 1))];
  const q3 = sorted[Math.floor(0.75 * (n - 1))];
  const iqr = q3 - q1;
  const normIqr = iqr > 0 ? iqr / 1.34 : stdDev;

  return 0.9 * Math.min(stdDev, normIqr) * Math.pow(n, -0.2);
}

const testSample = [10, 12, 14, 15, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 35];
const testH = computeSilvermanBandwidth(testSample);
assert(testH > 0 && testH < 15, `Silverman bandwidth (${testH}) in plausible statistical range`);
console.log('  [PASS] Silverman rule-of-thumb bandwidth calculation verified');

// KDE Summation
function evaluateKde(val, sample, h) {
  const n = sample.length;
  let sum = 0;
  for (let i = 0; i < n; i++) {
    sum += gaussianKernel((val - sample[i]) / h);
  }
  return sum / (n * h);
}
const dCenter = evaluateKde(22, testSample, testH);
const dFar = evaluateKde(150, testSample, testH);
assert(dCenter > dFar, 'Density at sample center is greater than tail density');
console.log('  [PASS] KDE continuous probability summation verified');


// ==========================================
// TEST 3: CANDLESTICK & FINANCIAL CALCULUS
// ==========================================
console.log('\n--- Testing Candlestick & Financial OHLC Calculus ---');

// Cartesian Price Projector
function mapPriceY(price, minPrice, maxPrice, viewHeight, padTop, padBottom) {
  const plotH = viewHeight - padTop - padBottom;
  const norm = (price - minPrice) / (maxPrice - minPrice || 1);
  return (viewHeight - padBottom) - norm * plotH;
}
assert.strictEqual(mapPriceY(100, 100, 200, 500, 30, 50), 450); // Min price maps to bottom: 500 - 50 = 450
assert.strictEqual(mapPriceY(200, 100, 200, 500, 30, 50), 30);  // Max price maps to top: 30
assert.strictEqual(mapPriceY(150, 100, 200, 500, 30, 50), 240); // Midpoint price maps to 30 + 420/2 = 240
console.log('  [PASS] Inverted financial price projection verified');

// Simple Moving Average (SMA)
function calculateSMA(series, period) {
  return series.map((val, i) => {
    if (i < period - 1) return null;
    let sum = 0;
    for (let j = 0; j < period; j++) sum += series[i - j];
    return sum / period;
  });
}
const prices = [10, 20, 30, 40, 50];
const sma3 = calculateSMA(prices, 3);
assert.strictEqual(sma3[0], null);
assert.strictEqual(sma3[1], null);
assert.strictEqual(sma3[2], 20); // (10+20+30)/3 = 20
assert.strictEqual(sma3[3], 30); // (20+30+40)/3 = 30
assert.strictEqual(sma3[4], 40); // (30+40+50)/3 = 40
console.log('  [PASS] Simple Moving Average (SMA) rolling window verified');

// Exponential Moving Average (EMA)
function calculateEMA(series, period) {
  const k = 2 / (period + 1);
  let prev = null;
  return series.map(val => {
    if (prev === null) { prev = val; return prev; }
    prev = val * k + prev * (1 - k);
    return prev;
  });
}
const ema3 = calculateEMA([10, 20, 30], 3);
// k = 2 / 4 = 0.5
// t=0: 10
// t=1: 20 * 0.5 + 10 * 0.5 = 15
// t=2: 30 * 0.5 + 15 * 0.5 = 22.5
assert.strictEqual(ema3[0], 10);
assert.strictEqual(ema3[1], 15);
assert.strictEqual(ema3[2], 22.5);
console.log('  [PASS] Exponential Moving Average (EMA) recursive smoothing verified');


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
console.log('ALL NOVEMBER 21 STUDIOS RUNTIME MATH TESTS PASSED!');
console.log('======================================================\n');
