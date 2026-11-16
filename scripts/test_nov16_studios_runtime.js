const assert = require('assert');

console.log('=== TESTING NOVEMBER 16, 2026 STUDIOS RUNTIME MATH & ACCESSIBILITY ===\n');

// ==========================================
// TEST 1: RADAR CHART STUDIO MATH & CONTRAST
// ==========================================
console.log('--- Testing Radar Chart Studio Math & Contrast ---');

function polarToCartesian(cx, cy, r, angleRad) {
  return {
    x: +(cx + r * Math.cos(angleRad - Math.PI / 2)).toFixed(2),
    y: +(cy + r * Math.sin(angleRad - Math.PI / 2)).toFixed(2)
  };
}

const pTop = polarToCartesian(250, 250, 100, 0);
assert.strictEqual(pTop.x, 250.0);
assert.strictEqual(pTop.y, 150.0);

const pRight = polarToCartesian(250, 250, 100, Math.PI / 2);
assert.strictEqual(pRight.x, 350.0);
assert.strictEqual(pRight.y, 250.0);

const pBottom = polarToCartesian(250, 250, 100, Math.PI);
assert.strictEqual(pBottom.x, 250.0);
assert.strictEqual(pBottom.y, 350.0);

const pLeft = polarToCartesian(250, 250, 100, (3 * Math.PI) / 2);
assert.strictEqual(pLeft.x, 150.0);
assert.strictEqual(pLeft.y, 250.0);
console.log('  [PASS] Polar to Cartesian 4-quadrant coordinate mapping verified');

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
assert.strictEqual(computePolygonArea(squarePoints), 100);

function getAxisAngles(axisCount) {
  const step = (2 * Math.PI) / axisCount;
  return Array.from({ length: axisCount }, (_, i) => i * step);
}
const pentagonAngles = getAxisAngles(5);
assert.strictEqual(pentagonAngles.length, 5);
assert.strictEqual(+pentagonAngles[1].toFixed(4), +(2 * Math.PI / 5).toFixed(4));
console.log('  [PASS] Equi-angular slice distribution and shoelace area verified');

function luminance(hexColor) {
  let hex = hexColor.replace('#', '');
  if (hex.length === 3) hex = hex.split('').map(c => c + c).join('');
  const r = parseInt(hex.substring(0, 2), 16) / 255;
  const g = parseInt(hex.substring(2, 4), 16) / 255;
  const b = parseInt(hex.substring(4, 6), 16) / 255;
  const a = [r, g, b].map(v => (v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4)));
  return 0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2];
}

function contrast(hex1, hex2) {
  const l1 = luminance(hex1);
  const l2 = luminance(hex2);
  return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
}

const radarLabelContrast = contrast('#27272A', '#F9FAFB');
assert(radarLabelContrast >= 4.5, `Radar axis label light contrast meets WCAG AA`);
console.log(`  [PASS] Radar axis label contrast (${radarLabelContrast.toFixed(2)}:1) meets WCAG 2.2 AA in light theme`);


// ==========================================
// TEST 2: TREEMAP SQUARIFIED STUDIO MATH & DRILL-DOWN ZOOM
// ==========================================
console.log('\n--- Testing Squarified Treemap Studio Math & Zoom Viewport ---');

function worstAspectRatio(rowAreas, length) {
  if (rowAreas.length === 0) return Infinity;
  const sum = rowAreas.reduce((a, b) => a + b, 0);
  const max = Math.max(...rowAreas);
  const min = Math.min(...rowAreas);
  const l2 = length * length;
  const s2 = sum * sum;
  return Math.max((l2 * max) / s2, s2 / (l2 * min));
}

const ratioSingle = worstAspectRatio([25], 5);
assert.strictEqual(ratioSingle, 1);

const ratioTwo = worstAspectRatio([10, 20], 10);
assert.strictEqual(+ratioTwo.toFixed(3), 2.222);
console.log('  [PASS] Bruls squarified worst aspect ratio formula verified');

function shouldAddElement(currentRow, nextElementArea, containerLength) {
  const currentRatio = worstAspectRatio(currentRow, containerLength);
  const candidateRatio = worstAspectRatio([...currentRow, nextElementArea], containerLength);
  return candidateRatio <= currentRatio;
}

assert.strictEqual(shouldAddElement([36], 1, 6), false);
console.log('  [PASS] Squarified greedy partition optimization rule verified');

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

function calculateZoomViewBox(x, y, w, h, maxW = 680, maxH = 440) {
  const padX = Math.max(0, x - 10);
  const padY = Math.max(0, y - 10);
  const padW = Math.min(maxW - padX, w + 20);
  const padH = Math.min(maxH - padY, h + 20);
  return { padX, padY, padW, padH, viewBox: `${padX} ${padY} ${padW} ${padH}` };
}
const zoom1 = calculateZoomViewBox(50, 40, 200, 150);
assert(zoom1.padX >= 0 && zoom1.padY >= 0);
assert(zoom1.padW <= 680 && zoom1.padH <= 440);
console.log('  [PASS] Treemap drill-down zoom viewBox calculation verified');


// ==========================================
// TEST 3: FUNNEL CHART STUDIO MATH & LUMINANCE CONTRAST
// ==========================================
console.log('\n--- Testing Funnel Chart Studio Math & Luminance Accessibility ---');

function calculateStageWidth(value, maxValue, minWidth, maxWidth) {
  if (maxValue <= 0) return minWidth;
  const ratio = Math.max(0, Math.min(1, value / maxValue));
  return minWidth + ratio * (maxWidth - minWidth);
}

const wTop = calculateStageWidth(1000, 1000, 80, 500);
assert.strictEqual(wTop, 500);

const wBot = calculateStageWidth(0, 1000, 80, 500);
assert.strictEqual(wBot, 80);

const wMid = calculateStageWidth(500, 1000, 80, 500);
assert.strictEqual(wMid, 290);
console.log('  [PASS] Linear and bounded width normalization verified');

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
assert(funnelSegment.startsWith('M 100.0 100.0 C 100.0 150.0, 200.0 150.0, 200.0 200.0'));
assert(funnelSegment.includes('L 400.0 200.0 C 400.0 150.0, 500.0 150.0, 500.0 100.0 Z'));
console.log('  [PASS] S-curve cubic Bezier transition neck geometry verified');

function computeDropoff(current, previous) {
  if (previous <= 0) return 0;
  return +(((previous - current) / previous) * 100).toFixed(1);
}
assert.strictEqual(computeDropoff(600, 1000), 40.0);
assert.strictEqual(computeDropoff(300, 600), 50.0);
console.log('  [PASS] Stage-to-stage conversion dropoff percentage verified');

// 3.4 Dynamic Stage Label Contrast on Bright, Pastel & Saturated Stages
function getOptimalTextColor(bgHex) {
  const lum = luminance(bgHex);
  const cWhite = 1.05 / (lum + 0.05);
  const cBlack = (lum + 0.05) / 0.053;
  return cBlack >= cWhite ? '#0A0A0A' : '#FFFFFF';
}

const testColors = [
  { name: 'Lime', hex: '#C1DD2D' },
  { name: 'Lavender', hex: '#E9D5FF' },
  { name: 'Sky Blue', hex: '#7DD3FC' },
  { name: 'Light Pastel Blue', hex: '#A5B4FC' },
  { name: 'Indigo Deep', hex: '#4F46E5' },
  { name: 'Emerald Deep', hex: '#10B981' }
];

for (const tc of testColors) {
  const chosenTextColor = getOptimalTextColor(tc.hex);
  const cRatio = contrast(chosenTextColor, tc.hex);
  assert(cRatio >= 4.5, `Stage ${tc.name} (${tc.hex}) with ${chosenTextColor} has contrast ${cRatio.toFixed(2)}:1 (must be >= 4.5:1)`);
}
console.log('  [PASS] Dynamic stage text luminance contrast verified >= 4.5:1 across all light & dark stages (WCAG 2.2 AA compliant)');


// ==========================================
// TEST 4: STANDALONE SVG COPY XML NAMESPACE
// ==========================================
console.log('\n--- Testing Standalone SVG Serialization & XMLNS ---');

function serializeSVGForClipboard(svgOuterHtml) {
  let res = svgOuterHtml;
  if (!res.includes('xmlns=')) {
    res = res.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ');
  }
  return res;
}

const copiedSnippet = serializeSVGForClipboard('<svg viewBox="0 0 500 500"><circle cx="250" cy="250" r="100"/></svg>');
assert(copiedSnippet.includes('xmlns="http://www.w3.org/2000/svg"'), 'Copied SVG string contains XML namespace');
console.log('  [PASS] Standalone SVG copy XML namespace serialization verified');

console.log('\n========================================');
console.log('ALL STUDIO RUNTIME MATH & ACCESSIBILITY TESTS PASSED!');
console.log('========================================\n');
