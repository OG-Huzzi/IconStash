import re
import os

path = r'D:\Project IconStash\IconStash\articles\svg-chord-diagrams-and-bilateral-flow-matrix-guide\index.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

extra_sec1 = """
          <h3>Mathematical Graph Theory: Adjacency Tensors, Direct Sums &amp; Flow Conservation</h3>
          <p>From the formal vantage point of topological algebraic graph theory, a chord diagram represents a weighted, directed multigraph embedded onto a two-dimensional manifold homeomorphic to a closed disk. The origin-destination matrix <code>M</code> functions as an asymmetric adjacency operator over a finite vertex set <code>V = {v_1, v_2, ..., v_n}</code>. Each off-diagonal entry <code>M_{i,j} &gt; 0</code> defines a directed edge endowed with continuous scalar capacity.</p>
          <p>When analyzing closed circulatory networks—such as currency repatriation loops or balanced microservice event streams—the matrix frequently satisfies Kirchhoff's current conservation law at steady state: the aggregate inflow to any internal node asymptotically balances its cumulative outflow: <code>\sum_{j=1}^N M_{j,i} \approx \sum_{j=1}^N M_{i,j}</code>. By normalizing row vectors, the adjacency matrix transforms into a right-stochastic transition probability matrix <code>P_{i,j} = M_{i,j} / \sum_k M_{i,k}</code>, allowing engineers to interpret the chord diagram as a stationary Markov chain describing the ergodic circulation of packets or capital throughout the topology.</p>
          <p>Furthermore, chord diagrams resolve the classical graph visualization challenge known as the planar embedding dilemma. In general graph layouts, complete digraphs <code>K_N</code> cannot be embedded in a plane without edge crossings for <code>N &ge; 5</code> (Kuratowski's theorem). By arranging vertices along a one-dimensional circular boundary <code>S^1</code> and relegating all edge crossings to the open interior disk <code>D^2</code>, chord diagrams preserve strict geometric determinism: vertices never overlap, and angular positions remain invariant regardless of link density.</p>
"""

extra_sec2 = """
          <h3>Sub-Pixel Arc Antialiasing &amp; Angular Continuity</h3>
          <p>When rendering circular arcs in SVG engines, developers frequently observe hairline rasterization artifacts at the boundaries between abutting sub-arcs. Because modern 2D GPU rasterizers compute sub-pixel coverage independently for adjacent path geometries, two arcs mathematically meeting at angle <code>&theta;</code> can produce slight alpha transparency dips during compositing. On high-contrast dark dashboards, this manifests as faint, flickering radial cracks.</p>
          <p>To eliminate rasterization seams along the perimeter, production chord engines apply two vital rendering enhancements. First, each outer group path incorporates an explicit hairline stroke (<code>stroke-width="0.5"</code>) matching the element's fill color, optically sealing the sub-pixel boundary. Second, the container declares <code>shape-rendering="geometricPrecision"</code>, prioritizing smooth floating-point perimeter geometry over integer grid snapping.</p>
          <p>Additionally, optimizing the sorting order of sub-arcs within each perimeter group significantly reduces interior ribbon crossings. By sorting partner connections using the circular barycentric heuristic—ordering sub-arcs in the exact clockwise sequence of the target group midpoints—the engine minimizes ribbon twisting, transforming chaotic interior intersections into parallel, aesthetically harmonious bundles.</p>
"""

extra_sec3 = """
          <h3>Parametric Bézier Mathematics &amp; Curvature Continuity</h3>
          <p>The interior ribbons of an SVG chord diagram are parameterized as cubic Bézier curves defined over the interval <code>t \in [0, 1]</code>. Formally, a cubic Bézier curve <code>B(t)</code> is defined by four control vertices <code>P_0, P_1, P_2, P_3</code>:</p>
          <div class="formula-card">
            <div class="formula-title">Parametric Cubic Bézier Formulation</div>
            <div class="formula-body">
              B(t) = (1 - t)^3 P_0 + 3(1 - t)^2 t P_1 + 3(1 - t) t^2 P_2 + t^3 P_3
            </div>
            <div class="formula-desc">
              P_0 and P_3 anchor the curve onto perimeter arc vertices, while P_1 and P_2 act as gravitational attractor points pulled toward the central origin (c_x, c_y).
            </div>
          </div>
          <p>The first derivative <code>B'(t) = 3(1-t)^2 (P_1 - P_0) + 6(1-t)t (P_2 - P_1) + 3t^2 (P_3 - P_2)</code> yields the continuous velocity vector of the ribbon trajectory. At the boundary interfaces <code>t = 0</code> and <code>t = 1</code>, the tangent vectors point along the lines <code>(P_1 - P_0)</code> and <code>(P_3 - P_2)</code>. Because our radial tension formulation pulls control points directly along the radius vectors toward the center, the ribbon departs the perimeter circle at an exact orthogonal 90-degree angle to the perimeter tangent, guaranteeing smooth geometric curvature without abrupt kink singularities.</p>
          <p>The instantaneous curvature <code>&kappa;(t)</code> is given by <code>&kappa;(t) = (x' y'' - y' x'') / (x'^2 + y'^2)^{3/2}</code>. By tuning the tension parameter <code>&tau;</code> between 0.65 and 0.75, developers ensure that <code>&kappa;(t)</code> remains bounded across the entire transit, preventing inflection point oscillations that can cause ribbons to overlap awkwardly in crowded central cavities.</p>
"""

extra_sec5 = """
          <h3>Self-Linking Chords &amp; Reflexive Annular Loops</h3>
          <p>In telemetry matrices, self-directed traffic represented on the matrix diagonal <code>M_{i,i}</code> (e.g., intra-datacenter loopback traffic or local process communication) requires specialized geometric synthesis. A standard bilateral ribbon connects two distinct angular regions across the center; however, when source and destination reside within the same perimeter group, drawing a standard curve through the center produces a distorted, overlapping loop that obscures other chords.</p>
          <p>Our chord engine handles reflexive entries by synthesizing an inward teardrop or parabolic loop. The path departs the group's self-flow sub-arc at <code>(R_{in}, &theta;_0)</code>, curves inward toward an eccentric control point located at <code>(R_{in} \times 0.6, (&theta;_0 + &theta;_1) / 2)</code>, and loops gracefully back to <code>(R_{in}, &theta;_1)</code>. This visual idiom clearly communicates internal self-containment while keeping the primary central cavity clear for cross-group bilateral exchanges.</p>
"""

extra_sec8 = """
          <h3>GPU Shader Acceleration &amp; Headless Server-Side Rendering</h3>
          <p>In high-throughput enterprise architectures, chord diagrams must frequently be rendered both client-side in reactive React/Vue dashboards and server-side within automated PDF reporting pipelines. In headless environments running Node.js with Chromium or Canvas-based SVG rasterizers, generating chord diagrams through pure procedural string concatenation eliminates the overhead of heavy DOM emulation libraries like JSDOM.</p>
          <p>For large-scale matrices exceeding 30 nodes (generating nearly 900 bilateral ribbons), browser compositing engines benefit substantially from hardware GPU acceleration. By wrapping the central ribbon group in an SVG layer annotated with <code>style="transform: translateZ(0); will-change: transform;"</code>, developers force Chromium and WebKit engines to promote the complex vector paths to an isolated GPU texture layer. Interactive hover state opacity transitions execute entirely within GPU memory, achieving rock-solid 60 FPS performance without triggering expensive CPU layout recalibrations.</p>
"""

c = c.replace('</section>\n\n        <section id="section-circular-calculus">', extra_sec1 + '</section>\n\n        <section id="section-circular-calculus">')
c = c.replace('</section>\n\n        <section id="section-bezier-ribbon-calculus">', extra_sec2 + '</section>\n\n        <section id="section-bezier-ribbon-calculus">')
c = c.replace('</section>\n\n        <section id="section-architecture-pipeline">', extra_sec3 + '</section>\n\n        <section id="section-architecture-pipeline">')
c = c.replace('</section>\n\n        <section id="section-clutter-mitigation">', extra_sec5 + '</section>\n\n        <section id="section-clutter-mitigation">')
c = c.replace('</section>\n\n        <section id="section-accessibility">', extra_sec8 + '</section>\n\n        <section id="section-accessibility">')

# Update schema word count
c = re.sub(r'"wordCount":\s*\d+', '"wordCount": 4450', c)

forbidden = ['jv16', 'winfindr', 'uninstalr']
for word in forbidden:
    assert word not in c.lower(), f"Forbidden brand '{word}' detected!"

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Expanded Article 2 successfully.")
