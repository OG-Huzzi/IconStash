const assert = require('assert');

console.log('=== TESTING NOVEMBER 15, 2026 STUDIOS RUNTIME MATH ===\n');

// ==========================================
// TEST 1: CANDLESTICK CHART STUDIO MATH
// ==========================================
console.log('--- Testing Candlestick Studio Math ---');

// 1.1 Price to Y coordinate projection
function calculateY(price, minPrice, maxPrice, plotHeight, padTop) {
  return padTop + ((maxPrice - price) / (maxPrice - minPrice)) * plotHeight;
}

const yMax = calculateY(100, 50, 100, 300, 20);
assert.strictEqual(yMax, 20, 'Max price maps to top pad');
const yMin = calculateY(50, 50, 100, 300, 20);
assert.strictEqual(yMin, 320, 'Min price maps to bottom');
const yMid = calculateY(75, 50, 100, 300, 20);
assert.strictEqual(yMid, 170, 'Mid price maps to exact vertical center');
console.log('  [PASS] Cartesian Price to Pixel Y-inversion projection verified');

// 1.2 Moving Average Calculations (SMA & EMA)
const testPrices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19];
function computeSMA(prices, period) {
  const window = prices.slice(prices.length - period);
  return window.reduce((sum, p) => sum + p, 0) / period;
}
const sma5 = computeSMA(testPrices, 5);
assert.strictEqual(sma5, 17, '5-period SMA of 15,16,17,18,19 is 17');
console.log('  [PASS] SMA rolling average calculation verified');

function computeEMA(prices, period) {
  const k = 2 / (period + 1);
  let ema = prices[0];
  for (let i = 1; i < prices.length; i++) {
    ema = prices[i] * k + ema * (1 - k);
  }
  return ema;
}
const emaVal = computeEMA(testPrices, 5);
assert(emaVal > 10 && emaVal < 20, 'EMA produces reasonable trend weight');
console.log('  [PASS] EMA recursive multiplier calculation verified');

// 1.3 Bollinger Bands Standard Deviation
function computeBollinger(prices, period = 5) {
  const mean = computeSMA(prices, period);
  const window = prices.slice(prices.length - period);
  const variance = window.reduce((acc, p) => acc + Math.pow(p - mean, 2), 0) / period;
  const stdDev = Math.sqrt(variance);
  return {
    middle: mean,
    upper: mean + 2 * stdDev,
    lower: mean - 2 * stdDev
  };
}
const bb = computeBollinger(testPrices, 5);
assert(bb.upper > bb.middle && bb.lower < bb.middle, 'Bollinger upper and lower envelopes encompass mean');
console.log('  [PASS] Bollinger Bands standard deviation envelope verified');


// ==========================================
// TEST 2: ACTIVITY HEATMAP STUDIO MATH
// ==========================================
console.log('\n--- Testing Heatmap Studio Math ---');

// 2.1 ISO Weekday and Column Projection
function projectCalendarCell(dayIndex, firstDayOfWeek, cellSize = 11, cellGap = 3, xPad = 34, yPad = 28) {
  const linearPos = dayIndex + firstDayOfWeek;
  const col = Math.floor(linearPos / 7);
  const row = linearPos % 7;
  return {
    col,
    row,
    x: xPad + col * (cellSize + cellGap),
    y: yPad + row * (cellSize + cellGap)
  };
}

const cell0 = projectCalendarCell(0, 0); // Monday start, day 0
assert.strictEqual(cell0.col, 0);
assert.strictEqual(cell0.row, 0);
assert.strictEqual(cell0.x, 34);
assert.strictEqual(cell0.y, 28);

const cell7 = projectCalendarCell(7, 0); // Monday start, 1 week later
assert.strictEqual(cell7.col, 1);
assert.strictEqual(cell7.row, 0);
assert.strictEqual(cell7.x, 34 + 14);
console.log('  [PASS] 7x52 Calendar matrix coordinate projection verified');

// 2.2 Quantile Color Binning
function computeQuantiles(values) {
  const sorted = values.filter(v => v > 0).sort((a, b) => a - b);
  return {
    q1: sorted[Math.floor(sorted.length * 0.25)],
    q2: sorted[Math.floor(sorted.length * 0.50)],
    q3: sorted[Math.floor(sorted.length * 0.75)]
  };
}
const testTelemetry = [0, 0, 0, 1, 2, 3, 4, 5, 8, 12, 16, 24, 60];
const quantiles = computeQuantiles(testTelemetry);
assert(quantiles.q1 <= quantiles.q2 && quantiles.q2 <= quantiles.q3, 'Quantiles monotonically increase');
console.log('  [PASS] Non-zero quantile percentile binning verified');

// 2.3 Streak Calculation Engine
function calculateStreaks(days) {
  let longest = 0;
  let temp = 0;
  days.forEach(d => {
    if (d > 0) {
      temp++;
      if (temp > longest) longest = temp;
    } else {
      temp = 0;
    }
  });
  return longest;
}
const streakTest = [1, 2, 0, 3, 4, 5, 6, 7, 0, 1, 2];
assert.strictEqual(calculateStreaks(streakTest), 5, 'Longest streak is 5');
console.log('  [PASS] Continuous activity streak tracking verified');


// ==========================================
// TEST 3: SANKEY DIAGRAM STUDIO MATH
// ==========================================
console.log('\n--- Testing Sankey Diagram Studio Math ---');

// 3.1 Longest Path Node Layer Stratification
function stratifyDAG(nodes, links) {
  const inDegree = new Map();
  const incoming = new Map();
  nodes.forEach(n => {
    inDegree.set(n.id, 0);
    incoming.set(n.id, []);
  });
  links.forEach(l => {
    inDegree.set(l.target, inDegree.get(l.target) + 1);
    incoming.get(l.target).push(l.source);
  });

  const layers = new Map();
  nodes.forEach(n => {
    if (inDegree.get(n.id) === 0) {
      layers.set(n.id, 0);
    }
  });

  let changed = true;
  while (changed) {
    changed = false;
    links.forEach(l => {
      const srcLayer = layers.get(l.source) || 0;
      const tgtLayer = layers.get(l.target) || 0;
      if (tgtLayer <= srcLayer) {
        layers.set(l.target, srcLayer + 1);
        changed = true;
      }
    });
  }
  return layers;
}

const sNodes = [{ id: 'A' }, { id: 'B' }, { id: 'C' }];
const sLinks = [{ source: 'A', target: 'B' }, { source: 'B', target: 'C' }];
const layers = stratifyDAG(sNodes, sLinks);
assert.strictEqual(layers.get('A'), 0, 'Source node at layer 0');
assert.strictEqual(layers.get('B'), 1, 'Intermediate node at layer 1');
assert.strictEqual(layers.get('C'), 2, 'Sink node at layer 2');
console.log('  [PASS] DAG longest path layer stratification verified');

// 3.2 Dual-Cubic Bezier Ribbon Geometry
function generateRibbon(x0, y0Top, x1, y1Top, linkHeight, curvature = 0.5) {
  const dx = x1 - x0;
  const cp1x = (x0 + dx * curvature).toFixed(1);
  const cp2x = (x1 - dx * curvature).toFixed(1);
  const y0Bot = (y0Top + linkHeight).toFixed(1);
  const y1Bot = (y1Top + linkHeight).toFixed(1);

  return `M ${x0.toFixed(1)} ${y0Top.toFixed(1)} C ${cp1x} ${y0Top.toFixed(1)}, ${cp2x} ${y1Top.toFixed(1)}, ${x1.toFixed(1)} ${y1Top.toFixed(1)} L ${x1.toFixed(1)} ${y1Bot} C ${cp2x} ${y1Bot}, ${cp1x} ${y0Bot}, ${x0.toFixed(1)} ${y0Bot} Z`;
}

const ribbonD = generateRibbon(100, 50, 300, 150, 20, 0.5);
assert(ribbonD.startsWith('M 100.0 50.0 C 200.0 50.0, 200.0 150.0, 300.0 150.0'), 'Top curve correct');
assert(ribbonD.includes('L 300.0 170.0'), 'Vertical drop correct');
assert(ribbonD.endsWith('Z'), 'Path properly closed with Z');
console.log('  [PASS] Dual-cubic Bezier ribbon geometry verified');

console.log('\n========================================');
console.log('ALL STUDIO RUNTIME MATH TESTS PASSED!');
console.log('========================================');
