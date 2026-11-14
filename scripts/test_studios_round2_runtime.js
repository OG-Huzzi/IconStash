const assert = require('assert');

console.log('=== TESTING RUNTIME STUDIOS & CODE GENERATORS (ROUND 2) ===');

// ==========================================
// TEST ARTICLE 1: TREE DIAGRAM STUDIO MATH
// ==========================================
console.log('\nTesting Article 1: Tree Diagram Studio Math...');

// Test 1: Cubic Bezier Link Generator
function generateTreeLink(source, target, orientation = 'horizontal') {
  if (orientation === 'horizontal') {
    const midX = (source.x + target.x) / 2;
    return `M ${source.x} ${source.y} C ${midX} ${source.y}, ${midX} ${target.y}, ${target.x} ${target.y}`;
  } else {
    const midY = (source.y + target.y) / 2;
    return `M ${source.x} ${source.y} C ${source.x} ${midY}, ${target.x} ${midY}, ${target.x} ${target.y}`;
  }
}

const sNode = { x: 50, y: 100 };
const tNode = { x: 250, y: 200 };
const hLink = generateTreeLink(sNode, tNode, 'horizontal');
assert.strictEqual(hLink, 'M 50 100 C 150 100, 150 200, 250 200', 'Horizontal cubic link matches');
const vLink = generateTreeLink(sNode, tNode, 'vertical');
assert.strictEqual(vLink, 'M 50 100 C 50 150, 250 150, 250 200', 'Vertical cubic link matches');
console.log('  [PASS] Cubic Bezier tree link synthesis verified');

// Test 2: Polar Radial Projection Math
function projectRadial(x, y, totalBreadth, origin = { x: 400, y: 300 }, radialScale = 60) {
  const angle = (x / totalBreadth) * 2 * Math.PI - Math.PI / 2;
  const radius = y * radialScale;
  return {
    px: origin.x + radius * Math.cos(angle),
    py: origin.y + radius * Math.sin(angle)
  };
}
const rootRad = projectRadial(0, 0, 100);
assert(Math.abs(rootRad.px - 400) < 0.001 && Math.abs(rootRad.py - 300) < 0.001, 'Root is at origin');
const childRad = projectRadial(50, 2, 100); // 180 degrees from -90 = +90 (straight down)
assert(Math.abs(childRad.px - 400) < 0.001 && Math.abs(childRad.py - 420) < 0.001, 'Child projected straight down at radius 120');
console.log('  [PASS] Polar radial projection verified');


// ==========================================
// TEST ARTICLE 2: CIRCUIT SCHEMATIC STUDIO MATH
// ==========================================
console.log('\nTesting Article 2: Circuit Schematic Studio Math...');

// Test 1: IEEE Resistor Path
function generateResistorPath(x, y, rotation = 0) {
  return `M ${x} ${y+20} L ${x+10} ${y+20} L ${x+15} ${y+10} L ${x+25} ${y+30} L ${x+35} ${y+10} L ${x+45} ${y+30} L ${x+50} ${y+20} L ${x+60} ${y+20}`;
}
const rPath = generateResistorPath(100, 50);
assert(rPath.includes('M 100 70 L 110 70 L 115 60'), 'Resistor path starts correctly');
console.log('  [PASS] IEEE Resistor symbol geometry verified');

// Test 2: Semi-circular bridge jumper arc
function generateBridgeJumper(startX, startY, endX, endY, verticalCrossings = []) {
  let pathD = `M ${startX} ${startY}`;
  const sorted = verticalCrossings.sort((a, b) => a - b);
  let curX = startX;
  for (const crossX of sorted) {
    if (crossX > curX + 8 && crossX < endX - 8) {
      pathD += ` L ${crossX - 6} ${startY}`;
      pathD += ` A 6 6 0 0 1 ${crossX + 6} ${startY}`;
      curX = crossX + 6;
    }
  }
  pathD += ` L ${endX} ${endY}`;
  return pathD;
}
const jumperD = generateBridgeJumper(0, 100, 200, 100, [100]);
assert.strictEqual(jumperD, 'M 0 100 L 94 100 A 6 6 0 0 1 106 100 L 200 100', 'Bridge jumper arc matches');
console.log('  [PASS] Bridge jumper semi-circular arc generator verified');


// ==========================================
// TEST ARTICLE 3: GANTT CHART CPM SOLVER MATH
// ==========================================
console.log('\nTesting Article 3: Gantt Chart CPM Solver Math...');

function solveCPM(tasks, dependencies) {
  const taskMap = new Map();
  const inDegree = new Map();
  const successors = new Map();
  const predecessors = new Map();

  tasks.forEach(t => {
    taskMap.set(t.id, t);
    inDegree.set(t.id, 0);
    successors.set(t.id, []);
    predecessors.set(t.id, []);
  });

  dependencies.forEach(d => {
    inDegree.set(d.to, inDegree.get(d.to) + 1);
    successors.get(d.from).push(d.to);
    predecessors.get(d.to).push(d.from);
  });

  // Kahn's TopoSort
  const queue = [];
  tasks.forEach(t => {
    if (inDegree.get(t.id) === 0) queue.push(t.id);
  });

  const topoOrder = [];
  while (queue.length > 0) {
    const u = queue.shift();
    topoOrder.push(u);
    for (const v of successors.get(u)) {
      inDegree.set(v, inDegree.get(v) - 1);
      if (inDegree.get(v) === 0) queue.push(v);
    }
  }
  assert.strictEqual(topoOrder.length, tasks.length, 'No cycles in test schedule');

  // Forward Pass
  const ES = new Map();
  const EF = new Map();
  topoOrder.forEach(id => {
    const t = taskMap.get(id);
    const preds = predecessors.get(id);
    let maxPredEF = t.startDay;
    if (preds.length > 0) {
      maxPredEF = Math.max(...preds.map(p => EF.get(p)));
    }
    const es = Math.max(t.startDay, maxPredEF);
    ES.set(id, es);
    EF.set(id, es + t.duration);
  });

  const projectDuration = Math.max(...Array.from(EF.values()), 1);

  // Backward Pass
  const LF = new Map();
  const LS = new Map();
  for (let i = topoOrder.length - 1; i >= 0; i--) {
    const id = topoOrder[i];
    const t = taskMap.get(id);
    const succs = successors.get(id);
    let minSuccLS = projectDuration;
    if (succs.length > 0) {
      minSuccLS = Math.min(...succs.map(s => LS.get(s)));
    }
    LF.set(id, minSuccLS);
    LS.set(id, minSuccLS - t.duration);
  }

  // Slack
  const criticalTasks = new Set();
  tasks.forEach(t => {
    const slack = (LS.get(t.id) || 0) - (ES.get(t.id) || 0);
    if (Math.abs(slack) < 0.001) {
      criticalTasks.add(t.id);
    }
  });

  return { ES, EF, LS, LF, projectDuration, criticalTasks };
}

const testTasks = [
  { id: 'A', startDay: 0, duration: 4 },
  { id: 'B', startDay: 4, duration: 6 },
  { id: 'C', startDay: 0, duration: 2 },
  { id: 'D', startDay: 2, duration: 3 }
];
const testDeps = [
  { from: 'A', to: 'B' },
  { from: 'C', to: 'D' }
];
const cpmRes = solveCPM(testTasks, testDeps);
assert.strictEqual(cpmRes.projectDuration, 10, 'Project duration is 10 days');
assert(cpmRes.criticalTasks.has('A') && cpmRes.criticalTasks.has('B'), 'Path A -> B is critical');
assert(!cpmRes.criticalTasks.has('C') && !cpmRes.criticalTasks.has('D'), 'Path C -> D has slack and is non-critical');
console.log('  [PASS] CPM Solver, Topological Sort, and Critical Path identification verified');

console.log('\nALL RUNTIME STUDIO TESTS PASSED SUCCESSFULLY!\n');
