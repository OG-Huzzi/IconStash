const assert = require('assert');

console.log('=== TESTING NOVEMBER 16, 2026 STUDIOS RUNTIME MATH ===\n');

// ==========================================
// TEST 1: RADAR CHART STUDIO MATH
// ==========================================
console.log('--- Testing Radar Chart Studio Math ---');

// 1.1 Polar to Cartesian Coordinate Mapping
function polarToCartesian(cx, cy, r, angleRad) {
  // SVG 0 rad at 12 o'clock (subtract PI/2)
  return {
    x: +(cx + r * Math.cos(angleRad - Math.PI / 2)).toFixed(2),
    y: +(cy + r * Math.sin(angleRad - Math.PI / 2)).toFixed(2)
  };
}

const pTop = polarToCartesian(250, 250, 100, 0); // 12 o'clock
assert.strictEqual(pTop.x, 250.0);
assert.strictEqual(pTop.y, 150.0, 'Top vertex maps to cx, cy - r');

const pRight = polarToCartesian(250, 250, 100, Math.PI / 2); // 3 o'clock
assert.strictEqual(pRight.x, 350.0);
assert.strictEqual(pRight.y, 250.0, 'Right vertex maps to cx + r, cy');

const pBottom = polarToCartesian(250, 250, 100, Math.PI); // 6 o'clock
assert.strictEqual(pBottom.x, 250.0);
assert.strictEqual(pBottom.y, 350.0, 'Bottom vertex maps to cx, cy + r');

const pLeft = polarToCartesian(250, 250, 100, (3 * Math.PI) / 2); // 9 o'clock
assert.strictEqual(pLeft.x, 150.0);
assert.strictEqual(pLeft.y, 250.0, 'Left vertex maps to cx - r, cy');
console.log('  [PASS] Polar to Cartesian 4-quadrant coordinate mapping verified');

// 1.2 Shoelace Polygon Area Calculation
function computePolygonArea(points) {
  let area = 0;
  const n = points.length;
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n;
    area += points[i].x * points[j].y;
    area -= points[j].x * points[i].y;
  }
  return Math.abs(area) / 2;
}

const squarePoints = [
  { x: 0, y: 0 },
  { x: 10, y: 0 },
  { x: 10, y: 10 },
  { x: 0, y: 10 }
];
assert.strictEqual(computePolygonArea(squarePoints), 100, 'Square of 10x10 has area 100');

// 1.3 Equi-angular slice distribution
function getAxisAngles(axisCount) {
  const step = (2 * Math.PI) / axisCount;
  return Array.from({ length: axisCount }, (_, i) => i * step);
}
const pentagonAngles = getAxisAngles(5);
assert.strictEqual(pentagonAngles.length, 5);
assert.strictEqual(+pentagonAngles[1].toFixed(4), +(2 * Math.PI / 5).toFixed(4));
console.log('  [PASS] Equi-angular slice distribution and shoelace area verified');


// ==========================================
// TEST 2: TREEMAP SQUARIFIED STUDIO MATH
// ==========================================
console.log('\n--- Testing Squarified Treemap Studio Math ---');

// 2.1 Worst Aspect Ratio Calculation (Bruls et al. 2000)
function worstAspectRatio(rowAreas, length) {
  if (rowAreas.length === 0) return Infinity;
  const sum = rowAreas.reduce((a, b) => a + b, 0);
  const max = Math.max(...rowAreas);
  const min = Math.min(...rowAreas);
  const l2 = length * length;
  const s2 = sum * sum;
  return Math.max((l2 * max) / s2, s2 / (l2 * min));
}

// Case: row with single square of side 5 along container side 5 (area = 25)
const ratioSingle = worstAspectRatio([25], 5);
assert.strictEqual(ratioSingle, 1, 'Single square fitting side 5 has aspect ratio 1.0');

// Case: two rectangles of areas 10 and 20 along edge length 10
const ratioTwo = worstAspectRatio([10, 20], 10);
// sum = 30, max = 20, min = 10, l2 = 100, s2 = 900
// max(100*20 / 900, 900 / (100*10)) = max(2.222, 0.9) = 2.222
assert.strictEqual(+ratioTwo.toFixed(3), 2.222);
console.log('  [PASS] Bruls squarified worst aspect ratio formula verified');

// 2.2 Greedy row addition decision
function shouldAddElement(currentRow, nextElementArea, containerLength) {
  const currentRatio = worstAspectRatio(currentRow, containerLength);
  const candidateRatio = worstAspectRatio([...currentRow, nextElementArea], containerLength);
  return candidateRatio <= currentRatio;
}

// Starting with item 36 on side 6: ratio is 1.0. Adding item 1 should worsen ratio to 38.027.
assert.strictEqual(shouldAddElement([36], 1, 6), false, 'Greedy partition correctly rejects element that worsens aspect ratio');
console.log('  [PASS] Squarified greedy partition optimization rule verified');

// 2.3 Total Area Scaling
function normalizeWeights(items, targetArea) {
  const total = items.reduce((sum, item) => sum + item.value, 0);
  return items.map(item => ({
    ...item,
    area: (item.value / total) * targetArea
  }));
}
const items = [{ value: 30 }, { value: 70 }];
const normalized = normalizeWeights(items, 1000);
assert.strictEqual(normalized[0].area, 300);
assert.strictEqual(normalized[1].area, 700);
console.log('  [PASS] Total area hierarchical weight normalization verified');


// ==========================================
// TEST 3: FUNNEL CHART STUDIO MATH
// ==========================================
console.log('\n--- Testing Funnel Chart Studio Math ---');

// 3.1 Width Normalization
function calculateStageWidth(value, maxValue, minWidth, maxWidth) {
  if (maxValue <= 0) return minWidth;
  const ratio = Math.max(0, Math.min(1, value / maxValue));
  return minWidth + ratio * (maxWidth - minWidth);
}

const wTop = calculateStageWidth(1000, 1000, 80, 500);
assert.strictEqual(wTop, 500, 'Max value yields maxWidth');

const wBot = calculateStageWidth(0, 1000, 80, 500);
assert.strictEqual(wBot, 80, 'Zero value yields minWidth');

const wMid = calculateStageWidth(500, 1000, 80, 500);
assert.strictEqual(wMid, 290, 'Half value yields exact midpoint width (80 + 0.5 * 420 = 290)');
console.log('  [PASS] Linear and bounded width normalization verified');

// 3.2 S-Curve Transition Bezier Points
function generateFunnelCurveSegment(cx, topY, botY, topWidth, botWidth) {
  const x0Left = cx - topWidth / 2;
  const x0Right = cx + topWidth / 2;
  const x1Left = cx - botWidth / 2;
  const x1Right = cx + botWidth / 2;
  const dy = botY - topY;
  const cpY1 = topY + dy * 0.5;
  const cpY2 = topY + dy * 0.5;

  const leftCurve = `M ${x0Left.toFixed(1)} ${topY.toFixed(1)} C ${x0Left.toFixed(1)} ${cpY1.toFixed(1)}, ${x1Left.toFixed(1)} ${cpY2.toFixed(1)}, ${x1Left.toFixed(1)} ${botY.toFixed(1)}`;
  const rightCurve = `L ${x1Right.toFixed(1)} ${botY.toFixed(1)} C ${x1Right.toFixed(1)} ${cpY2.toFixed(1)}, ${x0Right.toFixed(1)} ${cpY1.toFixed(1)}, ${x0Right.toFixed(1)} ${topY.toFixed(1)} Z`;
  return leftCurve + ' ' + rightCurve;
}

const funnelSegment = generateFunnelCurveSegment(300, 100, 200, 400, 200);
assert(funnelSegment.startsWith('M 100.0 100.0 C 100.0 150.0, 200.0 150.0, 200.0 200.0'), 'Left S-curve bezier correct');
assert(funnelSegment.includes('L 400.0 200.0 C 400.0 150.0, 500.0 150.0, 500.0 100.0 Z'), 'Right return S-curve bezier and closure correct');
console.log('  [PASS] S-curve cubic Bezier transition neck geometry verified');

// 3.3 Conversion Dropoff Rate
function computeDropoff(current, previous) {
  if (previous <= 0) return 0;
  return +(((previous - current) / previous) * 100).toFixed(1);
}
assert.strictEqual(computeDropoff(600, 1000), 40.0, '1000 to 600 represents 40% dropoff');
assert.strictEqual(computeDropoff(300, 600), 50.0, '600 to 300 represents 50% dropoff');
console.log('  [PASS] Stage-to-stage conversion dropoff percentage verified');

console.log('\n========================================');
console.log('ALL STUDIO RUNTIME MATH TESTS PASSED!');
console.log('========================================');
