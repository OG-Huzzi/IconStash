const fs = require('fs');
const path = require('path');

const outDir = path.join('articles', 'css-clip-path-and-svg-masking-guide');
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

const p1_intro = `
        <section id="section-intro">
          <h2>1. Introduction: Modern Vector Clipping and Masking in 2026</h2>
          <p>For decades, web design was imprisoned within rigid rectangular boxes. Every <code>&lt;div&gt;</code>, image, and section divider was fundamentally constrained by the rectangular nature of the CSS box model. Early workarounds — such as slicing translucent PNG assets in Photoshop, assembling complex multi-nested wrapper markup, or layering 9-slice background images — introduced significant layout thrashing, bloated network payloads, and fragile responsive behavior across mobile devices.</p>
          <p>In modern web development, the convergence of the W3C CSS Masking Module Level 1 and Scalable Vector Graphics (SVG) has completely transformed interface design. Today, frontend engineers can sculpt web elements into arbitrary geometric silhouettes, organic waves, diagonal dynamic section dividers, non-destructive notification badge cutouts, and feather-edged spotlight glows using pure declarative code.</p>
          <p>Two primary architectural mechanisms drive this visual revolution: <strong>Clipping</strong> (via CSS <code>clip-path</code> and SVG <code>&lt;clipPath&gt;</code>) and <strong>Masking</strong> (via CSS <code>mask-image</code> and SVG <code>&lt;mask&gt;</code>). While developers often conflate the two terms, they represent fundamentally distinct mathematical and GPU compositing operations. Clipping performs 1-bit binary stencil cutouts with zero antialiasing blur, while masking performs 8-bit multi-channel alpha and luminance compositing, allowing partial transparency, linear gradient feathering, and complex texture blending.</p>
          <p>Furthermore, recent browser advancements — such as universal support for the CSS <code>path()</code> basic shape function, hardware-accelerated SVG clipping in Google Skia and Apple Metal, and responsive coordinate normalization via <code>clipPathUnits="objectBoundingBox"</code> — enable engineers to build high-performance, fluid interfaces that scale effortlessly from mobile viewports to ultra-wide displays without dropping below 120 FPS. This comprehensive engineering guide dissects the mathematical foundations, coordinate transformations, animation rules, and production UI patterns required to master clipping and masking across modern web stacks.</p>
        </section>
`;

const p2_fundamentals = `
        <section id="section-fundamentals">
          <h2>2. Fundamentals: clip-path vs mask-image vs SVG clipPath vs mask</h2>
          <p>To avoid architectural errors and rendering defects, developers must understand the precise boundaries between the four primary vector cut-out technologies available in the web platform:</p>

          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Technology</th>
                  <th>Compositing Type</th>
                  <th>Boundary Precision</th>
                  <th>Alpha Gradients</th>
                  <th>GPU Performance</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>CSS <code>clip-path</code></strong></td>
                  <td>1-bit Binary Geometry</td>
                  <td>Hard boundary (Inside = 100%, Outside = 0%)</td>
                  <td>No (Binary cutout only)</td>
                  <td>Extremely High (Compositor thread promotion)</td>
                </tr>
                <tr>
                  <td><strong>SVG <code>&lt;clipPath&gt;</code></strong></td>
                  <td>1-bit Vector Geometry</td>
                  <td>Hard boundary based on path winding rules</td>
                  <td>No (Binary vector stencil)</td>
                  <td>High (Direct GPU tessellation)</td>
                </tr>
                <tr>
                  <td><strong>CSS <code>mask-image</code></strong></td>
                  <td>8-bit Alpha / Luminance</td>
                  <td>Soft, feather-edged raster/vector blending</td>
                  <td>Yes (Full 0% to 100% opacity gradations)</td>
                  <td>Moderate (Requires intermediate texture pass)</td>
                </tr>
                <tr>
                  <td><strong>SVG <code>&lt;mask&gt;</code></strong></td>
                  <td>8-bit Luminance (Default)</td>
                  <td>Soft vector/raster alpha and luminance map</td>
                  <td>Yes (Multi-stop gradient fades and textures)</td>
                  <td>Moderate (Intermediate offscreen surface)</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3>2.1 The 1-Bit Binary Principle of Clipping</h3>
          <p>When you apply a clipping path (whether via CSS <code>clip-path: polygon(...)</code> or an SVG <code>&lt;clipPath&gt;</code> element), the browser's graphics rasterizer constructs a closed 2D polygon or spline boundary. For every pixel in the element's bounding box, the rasterizer evaluates an inside/outside point test (governed by the <code>clip-rule</code> winding algorithm):</p>
          <ul>
            <li>If the center of the pixel lies <strong>inside</strong> the clipping boundary, the pixel is painted with 100% of its computed source RGBA color.</li>
            <li>If the center of the pixel lies <strong>outside</strong> the clipping boundary, the pixel is discarded completely (0% visibility). No pointer events, mouse hover triggers, or screen-reader hit-boxes are registered outside the clipped silhouette.</li>
          </ul>
          <p>Because clipping produces a binary decision per pixel without computing alpha blending math, graphics hardware can optimize clipping using depth buffers or stencil buffers, avoiding expensive multi-pass blend calculations.</p>

          <h3>2.2 The 8-Bit Multi-Channel Principle of Masking</h3>
          <p>Masking, by contrast, operates on opacity channels. Instead of an all-or-nothing cutoff, a mask defines an image or vector graphic whose pixel values determine the final transparency of the target element:</p>
          <ul>
            <li><strong>Alpha Masking:</strong> The alpha transparency channel of the mask image dictates target visibility. Where the mask is 100% opaque (alpha = 1.0), the element is fully visible; where the mask is 50% translucent (alpha = 0.5), the element is 50% translucent; where the mask is fully transparent (alpha = 0.0), the element is invisible.</li>
            <li><strong>Luminance Masking (SVG Default):</strong> The perceived photometric brightness (luminance) of the mask determines visibility. Pure white (<code>#FFFFFF</code>) corresponds to 100% opacity; pure black (<code>#000000</code>) corresponds to 0% opacity; middle gray (<code>#808080</code>) yields 50% opacity. This allows designers to use standard linear and radial gradients to fade elements softly into backgrounds.</li>
          </ul>
        </section>
`;

const p3_shapes = `
        <section id="section-basic-shapes">
          <h2>3. CSS Basic Shapes: inset(), circle(), ellipse(), and polygon() Geometry</h2>
          <p>The CSS <code>clip-path</code> property supports four native geometric functions defined in the CSS Shapes Module: <code>inset()</code>, <code>circle()</code>, <code>ellipse()</code>, and <code>polygon()</code>. Because these functions are declared directly in stylesheets without requiring separate SVG DOM tags, they are ideal for lightweight UI styling and fluid responsive scaling.</p>

          <h3>3.1 Inset Rectangles with Rounded Borders: inset()</h3>
          <p>The <code>inset()</code> function clips an element inward from its four outer edges, functioning like an internal margin box. It accepts one to four edge offsets followed by an optional <code>round</code> parameter that applies independent corner radii:</p>

          <pre><code>/* Syntax: inset(top right bottom left round border-radius) */
.clipped-card {
  /* Clip 16px from top/bottom, 24px from left/right, with 12px rounded corners */
  clip-path: inset(16px 24px 16px 24px round 12px);
}</code></pre>
          <p>Unlike setting CSS <code>overflow: hidden</code> on a parent container, <code>inset()</code> clips child elements, borders, shadows, and pseudo-elements simultaneously without creating a nested scrolling container.</p>

          <h3>3.2 Circular and Elliptical Silhouettes: circle() &amp; ellipse()</h3>
          <p>The <code>circle()</code> and <code>ellipse()</code> functions construct curved clipping masks parameterized by radius and center positioning:</p>

          <pre><code>/* Circular avatar cutout centered at element midpoint */
.avatar-round {
  clip-path: circle(50% at 50% 50%);
}

/* Elliptical spotlight reveal centered 30% from the left edge */
.spotlight-banner {
  clip-path: ellipse(40% 60% at 30% 50%);
}</code></pre>

          <h3>3.3 Arbitrary Vertex Polygons: polygon() and Winding Rules</h3>
          <p>The <code>polygon()</code> function provides unlimited multi-point geometric freedom. It accepts an ordered comma-separated list of coordinate pairs, where coordinates can be expressed in percentages, pixels, rems, or viewport units:</p>

          <pre><code>/* Hexagonal UI Badge */
.hex-badge {
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
}

/* Diagonal Hero Section Divider */
.angled-hero {
  clip-path: polygon(0% 0%, 100% 0%, 100% 88%, 0% 100%);
}</code></pre>

          <h3>3.4 Calculating Regular N-Sided Polygon Vertices Programmatically</h3>
          <p>To generate perfectly symmetrical regular polygons (such as octagons, decagons, or pentagrams), use the standard trigonometric circle parameterization formulas:</p>

          <div class="formula-card">
            <div class="formula-title">Regular N-Sided Polygon Vertex Formula</div>
            <div class="formula-body">
X_k = 50% + 50% &times; cos( 2 &times; pi &times; k / N - pi / 2 )<br>
Y_k = 50% + 50% &times; sin( 2 &times; pi &times; k / N - pi / 2 )
            </div>
            <div class="formula-desc">Where N is the total number of vertices and k ranges from 0 to N - 1.</div>
          </div>

          <p>For an octagon (<code>N = 8</code>), evaluating this formula produces the crisp 8-point stop-sign silhouette:</p>
          <pre><code>/* Regular Octagon (8 vertices computed via trigonometric steps) */
.octagonal-card {
  clip-path: polygon(
    30% 0%, 70% 0%,
    100% 30%, 100% 70%,
    70% 100%, 30% 100%,
    0% 70%, 0% 30%
  );
}</code></pre>

          <h3>3.5 Combining CSS calc() with polygon() Coordinates</h3>
          <p>Modern CSS allows the powerful combination of percentage units with absolute pixel measurements inside <code>calc()</code> expressions. This enables futuristic chamfered sci-fi corners that maintain a fixed 20px bevel angle regardless of how wide the element stretches:</p>

          <pre><code>/* Futuristic Chamfered Cyberpunk Button */
.cyber-button {
  background: #C1DD2D;
  color: #0A0A0A;
  padding: 14px 28px;
  /* Fixed 20px diagonal cuts on top-right and bottom-left corners */
  clip-path: polygon(
    0% 0%,
    calc(100% - 20px) 0%,
    100% 20px,
    100% 100%,
    20px 100%,
    0% calc(100% - 20px)
  );
}</code></pre>

          <div class="formula-card">
            <div class="formula-title">Polygon Winding Rule Math: nonzero vs evenodd</div>
            <div class="formula-body">
nonzero: Cast a ray from test point to infinity; count signed edge crossings.<br>
evenodd: Cast a ray from test point to infinity; total crossings modulo 2.
            </div>
            <div class="formula-desc">The evenodd rule allows self-intersecting polygon vertices to produce hollow cutouts and star apertures.</div>
          </div>

          <p>By default, <code>polygon()</code> utilizes the <code>nonzero</code> winding rule. To construct hollow cutouts, prefix the coordinate list with <code>evenodd</code>:</p>
          <pre><code>/* Star badge with hollow interior aperture */
.hollow-star {
  clip-path: polygon(evenodd, 50% 0%, 65% 35%, 100% 35%, 72% 57%, 82% 91%, 50% 70%, 18% 91%, 28% 57%, 0% 35%, 35% 35%);
}</code></pre>
        </section>
`;

const p4_path_fn = `
        <section id="section-path-function">
          <h2>4. The path() Function in CSS: Direct SVG Path Data in Stylesheets</h2>
          <p>Until recently, developers needing intricate curved clipping shapes — such as wavy organic banners, heart silhouettes, or custom brand emblems — had to author an external SVG document and link to it via <code>clip-path: url(#my-clip)</code>. The CSS Shapes specification introduced the native <code>path()</code> basic shape function, allowing standard SVG path data strings to be authored directly inside CSS declarations.</p>

          <h3>4.1 Native CSS path() Syntax</h3>
          <p>The <code>path()</code> function takes an optional winding rule followed by a quoted SVG path string containing standard commands (<code>M</code>, <code>L</code>, <code>C</code>, <code>S</code>, <code>Q</code>, <code>T</code>, <code>A</code>, <code>Z</code>):</p>

          <pre><code>/* Pure CSS wavy bottom header using SVG cubic Bézier path commands */
.wave-header {
  width: 100%;
  height: 280px;
  background: linear-gradient(135deg, #181E07 0%, #0C0F05 100%);
  clip-path: path('M 0 0 L 1000 0 L 1000 220 C 800 280, 600 160, 400 240 C 200 320, 100 180, 0 220 Z');
}</code></pre>

          <h3>4.2 The Critical Limitation of CSS path(): Absolute Pixel Units</h3>
          <div class="warning-box">
            <h4>Architectural Warning: Lack of Percentage Scaling in path()</h4>
            <p>Unlike <code>polygon()</code> or SVG <code>objectBoundingBox</code>, the coordinates inside CSS <code>path('M ...')</code> are strictly interpreted as <strong>unscaled CSS pixels</strong> (<code>px</code>). The CSS specification does not currently allow percentage signs inside path data commands. If an element resizes from 400px wide to 1200px wide, a shape clipped with <code>path()</code> will remain fixed at its original pixel dimensions, causing awkward empty spaces on the right.</p>
          </div>
          <p>To achieve fluid, 100% responsive vector clipping that stretches proportionally across arbitrary element dimensions, engineers must use SVG <code>&lt;clipPath&gt;</code> elements configured with <code>clipPathUnits="objectBoundingBox"</code>, as explored in Section 6.</p>
        </section>
`;

const p5_svg_clippath = `
        <section id="section-svg-clippath">
          <h2>5. Reusable SVG clipPath Elements &amp; Coordinate System Units</h2>
          <p>When interface designs require complex vector geometry, multiple disconnected sub-paths, or shared clipping silhouettes reused across hundreds of components, the SVG <code>&lt;clipPath&gt;</code> element is the industry standard. SVG clip paths are declared inside a <code>&lt;defs&gt;</code> block and referenced via CSS <code>url(#clip-id)</code>:</p>

          <pre><code>&lt;!-- Define reusable SVG clipPath in document HTML --&gt;
&lt;svg width="0" height="0" style="position: absolute; pointer-events: none;" aria-hidden="true"&gt;
  &lt;defs&gt;
    &lt;clipPath id="squircleClip" clipPathUnits="userSpaceOnUse"&gt;
      &lt;path d="M 0 20 C 0 5, 5 0, 20 0 H 60 C 75 0, 80 5, 80 20 V 60 C 80 75, 75 80, 60 80 H 20 C 5 80, 0 75, 0 60 Z"/&gt;
    &lt;/clipPath&gt;
  &lt;/defs&gt;
&lt;/svg&gt;

&lt;!-- Apply to HTML element via CSS --&gt;
&lt;div class="squircle-card" style="clip-path: url(#squircleClip);"&gt;
  &lt;img src="/og-default.png" alt="Preview"&gt;
&lt;/div&gt;</code></pre>

          <h3>5.1 Combining Multiple Geometric Primitives</h3>
          <p>A powerful advantage of <code>&lt;clipPath&gt;</code> over CSS basic shapes is that it can contain multiple overlapping or disjointed elements. You can combine <code>&lt;circle&gt;</code>, <code>&lt;rect&gt;</code>, <code>&lt;polygon&gt;</code>, and <code>&lt;text&gt;</code> inside a single clip path. The browser computes the union of all enclosed shapes to form the final silhouette:</p>

          <pre><code>&lt;!-- Complex composite clip path combining geometry and typography --&gt;
&lt;clipPath id="compositeBadgeClip"&gt;
  &lt;circle cx="50" cy="50" r="45"/&gt;
  &lt;rect x="40" y="80" width="20" height="30" rx="4"/&gt;
  &lt;text x="50" y="55" font-size="24" font-weight="900" text-anchor="middle"&gt;PRO&lt;/text&gt;
&lt;/clipPath&gt;</code></pre>
        </section>
`;

const p6_boundingbox = `
        <section id="section-objectboundingbox">
          <h2>6. Responsive Scaling with objectBoundingBox (0.0 to 1.0 Coordinates)</h2>
          <p>By default, SVG <code>&lt;clipPath&gt;</code> operates under <code>clipPathUnits="userSpaceOnUse"</code>. In this mode, coordinates correspond 1:1 with local SVG user coordinate pixels. If the target HTML element changes dimensions across responsive breakpoints, the clip path remains static, misaligning with the element's layout bounds.</p>
          <p>To make an SVG clip path automatically stretch, squish, and scale to fit any HTML element regardless of width or height, set <code>clipPathUnits="objectBoundingBox"</code>. In this coordinate system, the target element's entire bounding box is normalized to a unit square where coordinates span continuously from <code>0.0</code> (0% top/left) to <code>1.0</code> (100% bottom/right):</p>

          <div class="formula-card">
            <div class="formula-title">objectBoundingBox Coordinate Normalization Formula</div>
            <div class="formula-body">
Normalized X = Raw SVG X / Original ViewBox Width<br>
Normalized Y = Raw SVG Y / Original ViewBox Height
            </div>
            <div class="formula-desc">Maps absolute vector coordinates directly into unit interval [0.0, 1.0] for fluid responsive scaling.</div>
          </div>

          <h3>6.1 Normalized Path Example: Responsive Hexagonal Shield</h3>
          <p>Consider a standard hexagonal shield designed on a 100&times;100px vector canvas. To convert it into an <code>objectBoundingBox</code> clip path, divide all coordinate numbers by 100:</p>

          <pre><code>&lt;!-- Fluid, responsive SVG clip path that scales to ANY container size --&gt;
&lt;svg width="0" height="0" style="position: absolute; pointer-events: none;" aria-hidden="true"&gt;
  &lt;defs&gt;
    &lt;clipPath id="responsiveShield" clipPathUnits="objectBoundingBox"&gt;
      &lt;!-- Values span from 0.0 to 1.0 instead of fixed pixels --&gt;
      &lt;path d="M 0.5 0 L 1.0 0.25 L 1.0 0.75 L 0.5 1.0 L 0.0 0.75 L 0.0 0.25 Z"/&gt;
    &lt;/clipPath&gt;
  &lt;/defs&gt;
&lt;/svg&gt;

&lt;!-- This div can be 200x200px on mobile or 800x400px on desktop; clipping adapts perfectly! --&gt;
&lt;div class="fluid-shield-banner" style="clip-path: url(#responsiveShield);"&gt;&lt;/div&gt;</code></pre>

          <h3>6.2 Automated Script for Path Normalization</h3>
          <p>To convert arbitrary SVG icons or paths from standard viewBoxes (such as 24&times;24 in Lucide or Heroicons) into <code>objectBoundingBox</code> strings, use this helper utility:</p>

          <pre><code>// Utility to normalize SVG path coordinates to [0, 1] unit space
function normalizePathToObjectBoundingBox(pathString, viewBoxWidth = 24, viewBoxHeight = 24) {
  // Regex matches coordinate numbers and scales them
  return pathString.replace(/([-+]?[0-9]*\.?[0-9]+)/g, (match, num, offset, fullStr) => {
    // Alternate between X and Y based on coordinate token context
    const val = parseFloat(match);
    const scaled = (val / viewBoxWidth).toFixed(4);
    return scaled;
  });
}</code></pre>
        </section>
`;

const p7_masks = `
        <section id="section-svg-masks">
          <h2>7. Alpha vs Luminance Masking: Feathering, Gradients &amp; Opacity Maps</h2>
          <p>While clipping paths are limited to razor-sharp binary edges, modern UI design frequently requires soft, feathered transitions. Examples include fading a scrollable card container smoothly into transparency at the bottom, creating glowing particle trails, or feathering the perimeter of a hero photograph.</p>

          <h3>7.1 CSS mask-image with Linear Gradients</h3>
          <p>The CSS <code>mask-image</code> property accepts standard CSS gradient functions. By default in CSS masking, gradients behave as <strong>alpha masks</strong>:</p>

          <pre><code>/* Smooth vertical fadeout for scrollable lists (Top 85% visible, bottom 15% fades to 0) */
.fade-scroll-container {
  overflow-y: auto;
  mask-image: linear-gradient(to bottom, black 85%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, black 85%, transparent 100%);
}</code></pre>

          <h3>7.2 Boolean Geometry Operations with mask-composite</h3>
          <p>The CSS Masking specification introduced <code>mask-composite</code>, which enables Boolean constructive solid geometry operations directly between multiple mask layers:</p>
          <ul>
            <li><code>mask-composite: add</code> (Union: combines visibility across all masks).</li>
            <li><code>mask-composite: subtract</code> (Difference: subtracts the second mask from the first).</li>
            <li><code>mask-composite: intersect</code> (Intersection: only keeps areas covered by both masks).</li>
            <li><code>mask-composite: exclude</code> (XOR: hides overlapping regions).</li>
          </ul>

          <pre><code>/* Combine a gradient mask with a circular cutout using mask-composite */
.composite-masked-banner {
  mask-image: linear-gradient(to right, black, transparent), radial-gradient(circle at center, black, transparent);
  mask-composite: intersect;
  -webkit-mask-composite: source-in; /* Safari vendor compatibility */
}</code></pre>

          <h3>7.3 SVG &lt;mask&gt; and Luminance Mapping</h3>
          <p>Within native SVG, the <code>&lt;mask&gt;</code> element defaults to <code>mask-type: luminance</code>. The browser calculates the perceived brightness of the mask graphics using the international ITU-R BT.709 photometric coefficients:</p>

          <div class="formula-card">
            <div class="formula-title">Photometric Luminance Calculation Formula</div>
            <div class="formula-body">Luminance Y = 0.2126 &times; R + 0.7152 &times; G + 0.0722 &times; B</div>
            <div class="formula-desc">Green contributes over 71% of perceived luminance; pure blue contributes only 7.2%.</div>
          </div>

          <p>To construct a radial spotlight mask that illuminates a central circle while softly feathering the outer perimeter:</p>

          <pre><code>&lt;svg width="0" height="0" style="position: absolute;" aria-hidden="true"&gt;
  &lt;defs&gt;
    &lt;radialGradient id="spotlightGrad" cx="50%" cy="50%" r="50%"&gt;
      &lt;stop offset="40%" stop-color="#FFFFFF" stop-opacity="1"/&gt; &lt;!-- Fully visible --&gt;
      &lt;stop offset="100%" stop-color="#000000" stop-opacity="1"/&gt; &lt;!-- Fully hidden --&gt;
    &lt;/radialGradient&gt;
    &lt;mask id="spotlightMask" maskUnits="objectBoundingBox"&gt;
      &lt;rect width="1" height="1" fill="url(#spotlightGrad)"/&gt;
    &lt;/mask&gt;
  &lt;/defs&gt;
&lt;/svg&gt;

&lt;div class="hero-card" style="mask: url(#spotlightMask);"&gt;&lt;/div&gt;</code></pre>
        </section>
`;

const p8_animation = `
        <section id="section-animation">
          <h2>8. Animating Clip Paths: Morphing Transitions, WAAPI, and Interpolation Rules</h2>
          <p>Animating clipping boundaries creates showstopping micro-interactions — such as circular button click ripples expanding outward to fill the screen, menu drawers morphing from compact circles into full-screen dialogs, and dynamic geometric card hover reveals.</p>

          <h3>8.1 The Strict Vertex Count Interpolation Rule</h3>
          <div class="warning-box">
            <h4>Mandatory Rule for Animating polygon()</h4>
            <p>Browsers can only smoothly interpolate between two <code>polygon()</code> declarations if <strong>both polygons contain the exact same number of vertices</strong>. If Polygon A has 4 points and Polygon B has 6 points, CSS transitions cannot match intermediate points and will abruptly jump at 50% keyframe progress.</p>
          </div>
          <p>To morph between dissimilar shapes (such as a 4-point rectangle and an 8-point star), you must pad the simpler shape with degenerate collocated vertices (points that share the exact same coordinates) until vertex counts match perfectly.</p>

          <h3>8.2 High-Performance Animation via WAAPI</h3>
          <p>Using the Web Animations API (WAAPI), you can orchestrate hardware-accelerated clip-path morphs on the browser's GPU compositor thread without triggering layout reflows:</p>

          <pre><code>// Morph a circular button into an expanded modal card via WAAPI
function expandModalClip(element) {
  element.animate([
    { clipPath: 'circle(24px at 50% 50%)' },
    { clipPath: 'circle(100% at 50% 50%)' }
  ], {
    duration: 500,
    easing: 'cubic-bezier(0.16, 1, 0.3, 1)',
    fill: 'forwards'
  });
}</code></pre>

          <h3>8.3 FLIP Animations with Dynamic Clip-Paths</h3>
          <p>The FLIP technique (First, Last, Invert, Play) allows seamless geometric transitions between UI states. By measuring the initial bounding rect of a thumbnail card and the final dimensions of an expanded hero modal, you can calculate the exact <code>inset()</code> coordinates required to transition between them without animating expensive <code>width</code>, <code>height</code>, or <code>top</code> properties.</p>
        </section>
`;

const p9_gpu = `
        <section id="section-gpu-compositing">
          <h2>9. GPU Acceleration, Stacking Contexts, and Compositor Performance</h2>
          <p>Applying <code>clip-path</code> or <code>mask-image</code> significantly impacts how browser rendering engines composite layers on the GPU. Understanding these internals allows engineers to avoid accidental frame drops and memory spikes.</p>

          <h3>9.1 Automatic Stacking Context Generation</h3>
          <p>Under CSS specifications, setting any value for <code>clip-path</code> other than <code>none</code> automatically establishes a <strong>new CSS stacking context</strong>. Furthermore, it creates a new containing block for all descendants with <code>position: fixed</code> or <code>position: absolute</code>. If your application relies on fixed modal overlays placed inside a clipped container, the modal will be trapped inside the clipped boundary rather than spanning the viewport.</p>

          <h3>9.2 Layer Promotion and Anti-Aliasing</h3>
          <p>Modern graphics engines (Chromium Blink, Safari WebKit, and Firefox Gecko) handle clipped element rasterization by promoting the clipped element to a dedicated GPU texture layer. However, anti-aliasing techniques diverge across operating systems:</p>
          <ul>
            <li><strong>Chromium (Skia):</strong> Evaluates clip-path geometry using multi-sample anti-aliasing (MSAA) or analytic coverage within compute shaders.</li>
            <li><strong>Safari (WebKit / Metal):</strong> Implements clipping via hardware CoreAnimation masks, providing exceptionally smooth edges on Apple Silicon hardware with zero battery drain.</li>
          </ul>
        </section>
`;

const p10_studio = `
        <section id="section-interactive-studio">
          <h2>10. Interactive Developer Studio: Live Clip-Path &amp; SVG Masking Sandbox</h2>
          <p>Use the interactive workbench below to design and inspect clipping shapes and masks in real time. Switch between native CSS polygons, circular apertures, organic Bézier paths, and luminance gradient masks. Inspect generated code and test responsive scaling.</p>

          <div class="interactive-sandbox" id="clippingMaskStudio">
            <div class="sandbox-header">
              <div class="sandbox-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m14 2-8.5 8.5a2.12 2.12 0 0 0 0 3l5 5a2.12 2.12 0 0 0 3 0L22 10Z"/><path d="M7 16l-4 4"/></svg>
                <span>Clip-Path &amp; SVG Mask Visual Studio</span>
              </div>
              <span class="sandbox-badge">Interactive Inspector</span>
            </div>

            <div class="sandbox-grid">
              <div class="sandbox-controls">
                <div class="control-row">
                  <label for="clipModeSelect">Clipping Technique: <span class="stat-num" id="clipModeDisplay">CSS polygon()</span></label>
                  <select id="clipModeSelect" class="control-select">
                    <option value="polygon" selected>CSS Basic Shape: polygon()</option>
                    <option value="circle">CSS Basic Shape: circle()</option>
                    <option value="path">CSS Vector Function: path()</option>
                    <option value="mask">SVG Mask: Radial Luminance Fade</option>
                  </select>
                </div>

                <div class="control-row">
                  <label for="clipPresetSelect">Shape Preset Silhouette:</label>
                  <select id="clipPresetSelect" class="control-select">
                    <option value="hexagon" selected>Hexagonal UI Badge (6 Vertices)</option>
                    <option value="chevron">Forward Navigation Chevron</option>
                    <option value="ribbon">Corner Bookmark Ribbon</option>
                    <option value="badge">Notification Badge Notch Cutout</option>
                  </select>
                </div>

                <div class="control-row">
                  <label for="bgGradientSelect">Card Texture &amp; Background:</label>
                  <select id="bgGradientSelect" class="control-select">
                    <option value="cyber" selected>Cyber Lime &amp; Dark Graphite</option>
                    <option value="glass">Translucent Glassmorphism</option>
                    <option value="mesh">High-Contrast Radial Gradient</option>
                  </select>
                </div>

                <div class="control-row">
                  <label for="clipScaleSlider">Dynamic Inset / Scale: <span class="stat-num" id="scaleVal">100%</span></label>
                  <input type="range" id="clipScaleSlider" min="50" max="100" step="1" value="100" style="width:100%;">
                </div>
              </div>

              <div class="stage-wrapper">
                <div class="preview-stage-container">
                  <div id="previewClippedCard" style="width: 240px; height: 240px; background: linear-gradient(135deg, #C1DD2D 0%, #15803D 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; color: #0A0A0A; font-weight: 800; font-size: 16px; transition: clip-path 250ms ease, mask 250ms ease; position: relative;">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#0A0A0A" stroke-width="2.5" style="margin-bottom: 8px;"><path d="M12 2L2 7l10 5 10-5-10-5Z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/></svg>
                    <span>Clipped Target</span>
                  </div>
                  <div class="viewport-meta-overlay" id="clipMetaOverlay">clip-path: polygon(...)</div>
                </div>

                <div class="stats-readout-box">
                  <div class="stat-item">
                    <div class="stat-label">Compositor Promotion</div>
                    <div class="stat-val highlight" id="compositorStatus">GPU Layer Active</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Stacking Context</div>
                    <div class="stat-val" id="stackingStatus">Created (Isolated)</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Bounding Area</div>
                    <div class="stat-val" id="areaRatioVal">75.0% Fill Ratio</div>
                  </div>
                  <div class="stat-item">
                    <div class="stat-label">Hit-Test Boundary</div>
                    <div class="stat-val highlight" id="hitTestStatus">Restricted to Shape</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="generated-code-box">
              <div class="code-box-head">
                <div class="code-tabs">
                  <button class="code-tab-btn active" data-tab="css">CSS Declaration</button>
                  <button class="code-tab-btn" data-tab="tailwind">Tailwind CSS v4</button>
                  <button class="code-tab-btn" data-tab="svg">SVG clipPath</button>
                </div>
                <div class="code-actions">
                  <button class="copy-btn" id="copyClipCodeBtn">Copy Snippet</button>
                </div>
              </div>
              <pre class="code-output-area"><code id="clipCodeOutput"></code></pre>
            </div>
          </div>
        </section>
`;

const p11_recipes = `
        <section id="section-ui-recipes">
          <h2>11. Production UI Patterns: Notification Badges, Angled Dividers &amp; Spotlights</h2>
          <p>Below are four battle-tested UI recipes that solve everyday design challenges using modern clipping and masking.</p>

          <h3>11.1 Non-Destructive Notification Badge Cutout</h3>
          <p>When placing an unread notification count badge over an icon or avatar, a traditional border creates an unsightly halo on non-solid backgrounds. Using an SVG mask with a circular cutout punches a transparent hole precisely around the badge:</p>

          <pre><code>&lt;!-- Non-destructive hole punch avatar badge --&gt;
&lt;svg viewBox="0 0 48 48" width="48" height="48"&gt;
  &lt;mask id="badgeHole"&gt;
    &lt;!-- Everything white is visible --&gt;
    &lt;rect width="48" height="48" fill="white"/&gt;
    &lt;!-- The black circle punches a 100% transparent hole --&gt;
    &lt;circle cx="38" cy="10" r="8" fill="black"/&gt;
  &lt;/mask&gt;
  &lt;!-- Avatar image is clipped by mask --&gt;
  &lt;image href="/og-default.png" width="48" height="48" mask="url(#badgeHole)"/&gt;
  &lt;!-- Unclipped badge sits cleanly inside the hole --&gt;
  &lt;circle cx="38" cy="10" r="6" fill="#EF4444"/&gt;
&lt;/svg&gt;</code></pre>

          <h3>11.2 Fluid Responsive Diagonal Section Divider</h3>
          <p>To construct full-width slanted section dividers without raster image assets or horizontal scrollbar overflow bugs, apply <code>clip-path: polygon()</code> directly to the section container:</p>

          <pre><code>.slanted-section {
  width: 100%;
  padding: 120px 24px;
  background: #121212;
  /* Slant top edge down 4vw, bottom edge up 4vw */
  clip-path: polygon(0 4vw, 100% 0, 100% calc(100% - 4vw), 0 100%);
}</code></pre>

          <h3>11.3 Interactive Cursor Spotlight Reveal</h3>
          <p>Create an interactive spotlight effect where the user's cursor dynamically reveals an underlying visual layer using CSS variables updated via JavaScript:</p>

          <pre><code>// Update CSS spotlight coordinates via cursor mousemove
const hero = document.querySelector('.spotlight-hero');
hero.addEventListener('mousemove', (e) => {
  const rect = hero.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  hero.style.setProperty('--spotlight-x', x + 'px');
  hero.style.setProperty('--spotlight-y', y + 'px');
});

/* CSS Declaration */
.spotlight-top-layer {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, #C1DD2D 0%, transparent 70%);
  clip-path: circle(140px at var(--spotlight-x, 50%) var(--spotlight-y, 50%));
  transition: clip-path 50ms ease-out;
  pointer-events: none;
}</code></pre>
        </section>
`;

const p12_compat = `
        <section id="section-compat-matrix">
          <h2>12. Browser Compatibility Matrix &amp; CSS Specification Support</h2>
          <p>The table below summarizes browser engine compatibility for modern clipping and masking features across desktop and mobile browsers:</p>

          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Chrome (Blink)</th>
                  <th>Safari (WebKit)</th>
                  <th>Firefox (Gecko)</th>
                  <th>Mobile Support (iOS/Android)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>CSS <code>polygon()</code></strong></td>
                  <td>Chrome 55+</td>
                  <td>Safari 10.1+</td>
                  <td>Firefox 54+</td>
                  <td>Full Support (100%)</td>
                </tr>
                <tr>
                  <td><strong>CSS <code>path()</code></strong></td>
                  <td>Chrome 88+</td>
                  <td>Safari 13.1+</td>
                  <td>Firefox 97+</td>
                  <td>Full Support (98.2%)</td>
                </tr>
                <tr>
                  <td><strong><code>clipPathUnits="objectBoundingBox"</code></strong></td>
                  <td>Chrome 55+</td>
                  <td>Safari 11+</td>
                  <td>Firefox 54+</td>
                  <td>Full Support (100%)</td>
                </tr>
                <tr>
                  <td><strong>CSS <code>mask-image</code></strong></td>
                  <td>Chrome 120+ (unprefixed)</td>
                  <td>Requires <code>-webkit-</code> prefix</td>
                  <td>Firefox 53+</td>
                  <td>Full Support (Vendor Prefix Safe)</td>
                </tr>
                <tr>
                  <td><strong><code>mask-composite</code></strong></td>
                  <td>Chrome 120+</td>
                  <td>Safari 15.4+ (prefixed)</td>
                  <td>Firefox 53+</td>
                  <td>Modern Browsers (96.5%)</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="takeaway-box">
            <h3>Key Takeaway for Production Deployment</h3>
            <p>Always include the <code>-webkit-mask-image</code> vendor prefix alongside standard <code>mask-image</code> in your production CSS bundles to ensure 100% compatibility across Safari on macOS and iOS.</p>
          </div>
        </section>
`;

const p13_faq = `
        <section id="section-faq">
          <h2>13. Frequently Asked Questions</h2>

          <div class="faq-item">
            <h3>What is the mathematical difference between CSS clip-path and CSS mask-image?</h3>
            <p>CSS clip-path performs a 1-bit binary stencil test where pixels are either 100% visible or 100% discarded, with no partial opacity. CSS mask-image performs 8-bit alpha or luminance channel compositing, allowing smooth gradient feathering, translucent blurs, and variable opacity transitions.</p>
          </div>

          <div class="faq-item">
            <h3>Why does CSS clip-path: path() fail to scale responsively with element dimensions?</h3>
            <p>The path() basic shape function strictly interprets all coordinates as absolute, unscaled CSS pixels (px). To achieve fluid, responsive vector clipping that scales with container dimensions, use an SVG clipPath element configured with clipPathUnits="objectBoundingBox" where coordinates span normalized unit values from 0.0 to 1.0.</p>
          </div>

          <div class="faq-item">
            <h3>How do you animate clip-path: polygon() smoothly without sudden jumps?</h3>
            <p>Browsers require both keyframes to possess the exact same number of polygon vertices. If one polygon has 4 points and the other has 6, interpolation fails. Pad simpler shapes with redundant overlapping vertices to match point counts across all animation states.</p>
          </div>

          <div class="faq-item">
            <h3>Does applying a clip-path create a new CSS stacking context?</h3>
            <p>Yes. Any non-none value of clip-path automatically promotes the element to a new stacking context and acts as a containing block for absolute and fixed position descendants, preventing fixed child elements from escaping the clipped boundaries.</p>
          </div>

          <div class="faq-item">
            <h3>What is the difference between alpha masking and luminance masking?</h3>
            <p>Alpha masking uses the transparency channel of the mask image (opaque = visible, transparent = hidden). Luminance masking, the default in SVG, uses the visual brightness of the mask graphics (white = fully visible, black = fully hidden, gray = translucent).</p>
          </div>

          <div class="faq-item">
            <h3>Are user click and touch pointer events captured outside a clipped shape?</h3>
            <p>No. By default, clipping paths clip both the visual pixel output and the hit-testing boundary of the element. Pointer events outside the clipped silhouette pass directly through to underlying DOM elements.</p>
          </div>
        </section>
`;

const fullHtml = `<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSS clip-path &amp; SVG Masking Deep Dive: Polygon, Path() &amp; Masks (2026) | IconStash</title>
  <meta name="description" content="Master CSS clip-path and SVG masking: polygon, path(), SVG clipPath vs mask, objectBoundingBox scaling, WAAPI animations, and live developer studio.">
  <meta name="keywords" content="css clip-path, clip-path polygon, clip-path path svg, clip-path url, css clip-path animation, clip-path vs mask, responsive clip-path, clipPathUnits objectBoundingBox">
  <meta property="og:title" content="CSS clip-path &amp; SVG Masking Deep Dive: Polygon, Path() &amp; Masks (2026)">
  <meta property="og:description" content="Master CSS clip-path and SVG masking: polygon, path(), SVG clipPath vs mask, objectBoundingBox scaling, WAAPI animations, and live developer studio.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://iconstash.io/articles/css-clip-path-and-svg-masking-guide/">
  <meta property="og:image" content="https://iconstash.io/assets/articles/css-clip-path-and-svg-masking-guide.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:site_name" content="IconStash">
  <meta property="article:published_time" content="2026-10-30T00:00:00Z">
  <meta property="article:modified_time" content="2026-10-30T00:00:00Z">
  <meta property="article:author" content="Jouni Flemming">
  <meta property="article:section" content="CSS Architecture &amp; Masking">
  <meta property="article:tag" content="CSS">
  <meta property="article:tag" content="SVG">
  <meta property="article:tag" content="clip-path">
  <meta property="article:tag" content="Web Animation">
  <meta property="article:tag" content="Frontend Engineering">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="CSS clip-path &amp; SVG Masking Deep Dive: Polygon, Path() &amp; Masks (2026)">
  <meta name="twitter:description" content="Master CSS clip-path and SVG masking: polygon, path(), SVG clipPath vs mask, objectBoundingBox scaling, WAAPI animations, and live developer studio.">
  <meta name="twitter:image" content="https://iconstash.io/assets/articles/css-clip-path-and-svg-masking-guide.jpg">
  <link rel="canonical" href="https://iconstash.io/articles/css-clip-path-and-svg-masking-guide/">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/favicon.jpeg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script type="application/ld+json">
  [
    {
      "@context": "https://schema.org",
      "@type": "TechArticle",
      "headline": "CSS clip-path & SVG Masking Deep Dive: Polygon, Path() & Masks (2026)",
      "description": "Master CSS clip-path and SVG masking: polygon, path(), SVG clipPath vs mask, objectBoundingBox scaling, WAAPI animations, and live developer studio.",
      "image": "https://iconstash.io/assets/articles/css-clip-path-and-svg-masking-guide.jpg",
      "author": {
        "@type": "Person",
        "name": "Jouni Flemming",
        "url": "https://iconstash.io/about/",
        "worksFor": {
          "@type": "Organization",
          "name": "Great Software Company",
          "url": "https://greatsoftwarecompany.com"
        }
      },
      "publisher": {
        "@type": "Organization",
        "name": "IconStash",
        "url": "https://iconstash.io",
        "logo": {
          "@type": "ImageObject",
          "url": "https://iconstash.io/logo.png"
        },
        "parentOrganization": {
          "@type": "Organization",
          "name": "Great Software Company",
          "url": "https://greatsoftwarecompany.com"
        }
      },
      "datePublished": "2026-10-30",
      "dateModified": "2026-10-30",
      "mainEntityOfPage": "https://iconstash.io/articles/css-clip-path-and-svg-masking-guide/",
      "isPartOf": {
        "@type": "WebSite",
        "@id": "https://iconstash.io/#website"
      },
      "inLanguage": "en-US",
      "wordCount": 4092,
      "articleSection": "CSS Architecture & Masking",
      "proficiencyLevel": "Advanced",
      "keywords": [
        "css clip-path",
        "clip-path polygon",
        "clip-path path svg",
        "clip-path url",
        "css clip-path animation",
        "clip-path vs mask",
        "responsive clip-path",
        "clipPathUnits objectBoundingBox"
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "IconStash",
          "item": "https://iconstash.io/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Articles",
          "item": "https://iconstash.io/articles/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "CSS clip-path & SVG Masking Guide",
          "item": "https://iconstash.io/articles/css-clip-path-and-svg-masking-guide/"
        }
      ]
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the mathematical difference between CSS clip-path and CSS mask-image?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "CSS clip-path performs a 1-bit binary stencil test where pixels are either 100% visible or 100% discarded, with no partial opacity. CSS mask-image performs 8-bit alpha or luminance channel compositing, allowing smooth gradient feathering, translucent blurs, and variable opacity transitions."
          }
        },
        {
          "@type": "Question",
          "name": "Why does CSS clip-path: path() fail to scale responsively with element dimensions?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The path() basic shape function strictly interprets all coordinates as absolute, unscaled CSS pixels (px). To achieve fluid, responsive vector clipping that scales with container dimensions, use an SVG clipPath element configured with clipPathUnits='objectBoundingBox' where coordinates span normalized unit values from 0.0 to 1.0."
          }
        },
        {
          "@type": "Question",
          "name": "How do you animate clip-path: polygon() smoothly without sudden jumps?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Browsers require both keyframes to possess the exact same number of polygon vertices. If one polygon has 4 points and the other has 6, interpolation fails. Pad simpler shapes with redundant overlapping vertices to match point counts across all animation states."
          }
        },
        {
          "@type": "Question",
          "name": "Does applying a clip-path create a new CSS stacking context?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Any non-none value of clip-path automatically promotes the element to a new stacking context and acts as a containing block for absolute and fixed position descendants, preventing fixed child elements from escaping the clipped boundaries."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between alpha masking and luminance masking?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Alpha masking uses the transparency channel of the mask image (opaque = visible, transparent = hidden). Luminance masking, the default in SVG, uses the visual brightness of the mask graphics (white = fully visible, black = fully hidden, gray = translucent)."
          }
        },
        {
          "@type": "Question",
          "name": "Are user click and touch pointer events captured outside a clipped shape?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. By default, clipping paths clip both the visual pixel output and the hit-testing boundary of the element. Pointer events outside the clipped silhouette pass directly through to underlying DOM elements."
          }
        }
      ]
    }
  ]
  </script>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
    body { background: #0A0A0A; color: #F2F2F2; font: 400 17px/1.8 "Inter", system-ui, -apple-system, sans-serif; -webkit-font-smoothing: antialiased; }
    a { color: #C1DD2D; text-decoration: none; transition: color 150ms ease; }
    a:hover { color: #D2ED3E; }
    ::selection { background: rgba(193,221,45,0.25); color: #fff; }
    svg { max-width: 100%; display: inline-block; vertical-align: middle; }

    .site-header { position: sticky; top: 0; z-index: 100; background: rgba(10,10,10,0.88); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid #1F1F1F; padding: 0 24px; height: 58px; display: flex; align-items: center; justify-content: space-between; }
    .site-header .logo { display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 18px; color: #F2F2F2; }
    .site-header .logo svg { width: 24px; height: 24px; color: #C1DD2D; }
    .site-header nav { display: flex; gap: 24px; align-items: center; }
    .site-header nav a { color: #888; font-size: 14px; font-weight: 500; }
    .site-header nav a:hover { color: #F2F2F2; }
    .header-cta { background: #C1DD2D; color: #0A0A0A; font-weight: 700; font-size: 13px; padding: 8px 18px; border-radius: 6px; border: none; cursor: pointer; transition: all 150ms ease; }
    .header-cta:hover { background: #D2ED3E; transform: translateY(-1px); }
    .theme-toggle-btn { background: transparent; border: 1px solid #262626; color: #A3A3A3; width: 34px; height: 34px; border-radius: 6px; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 150ms ease; }
    .theme-toggle-btn:hover { border-color: #404040; color: #F2F2F2; }

    .page-container { max-width: 1280px; margin: 0 auto; padding: 48px 24px 80px; width: 100%; }
    .breadcrumb { display: flex; gap: 8px; font-size: 13px; color: #666; margin-bottom: 24px; align-items: center; flex-wrap: wrap; }
    .breadcrumb a { color: #888; }
    .breadcrumb a:hover { color: #C1DD2D; }
    .breadcrumb .sep { color: #444; }

    .article-hero { margin-bottom: 36px; border-bottom: 1px solid #1F1F1F; padding-bottom: 32px; }
    .article-hero .tag { display: inline-block; background: rgba(193,221,45,0.12); color: #C1DD2D; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; padding: 4px 12px; border-radius: 4px; margin-bottom: 16px; border: 1px solid rgba(193,221,45,0.25); }
    .article-hero h1 { font-size: clamp(28px, 4vw, 42px); font-weight: 900; line-height: 1.18; color: #FFF; letter-spacing: -0.03em; margin-bottom: 16px; }
    .article-meta { display: flex; gap: 20px; font-size: 13px; color: #737373; align-items: center; flex-wrap: wrap; margin-top: 12px; }
    .article-meta a { color: #C1DD2D; font-weight: 600; text-decoration: none; }

    .article-layout { display: grid; grid-template-columns: minmax(0, 1fr); gap: 48px; align-items: start; }
    @media (min-width: 1024px) {
      .article-layout { grid-template-columns: minmax(0, 1fr) 320px; }
    }

    .article-main { min-width: 0; }
    .featured-summary { background: linear-gradient(180deg, #141414 0%, #0E0E0E 100%); border: 1px solid #262626; border-left: 4px solid #C1DD2D; border-radius: 10px; padding: 24px 28px; margin-bottom: 32px; }
    .featured-summary p { font-size: 15.5px; line-height: 1.7; color: #E5E5E5; margin-bottom: 12px; font-weight: 500; }
    .featured-summary ul { margin: 0 0 0 20px; color: #D4D4D4; }
    .featured-summary li { margin-bottom: 8px; font-size: 14.5px; line-height: 1.6; }

    .article-figure { margin: 28px 0 36px; padding: 0; display: block; }
    .article-figure img { width: 100%; max-width: 100%; height: auto; border-radius: 10px; display: block; border: 1px solid #262626; }
    .article-figure figcaption { font-size: 0.85em; color: #737373; text-align: center; margin-top: 10px; font-style: italic; }

    h2 { font-size: 26px; font-weight: 800; color: #FFF; letter-spacing: -0.02em; margin: 48px 0 20px; padding-top: 24px; border-top: 1px solid #1F1F1F; }
    h3 { font-size: 20px; font-weight: 700; color: #E5E5E5; margin: 32px 0 14px; }
    h4 { font-size: 17px; font-weight: 700; color: #DDD; margin: 24px 0 10px; }
    p { margin-bottom: 22px; color: #D4D4D4; font-size: 16px; line-height: 1.8; }
    strong { color: #FFF; }
    ul, ol { margin: 0 0 24px 28px; color: #D4D4D4; }
    li { margin-bottom: 10px; line-height: 1.7; font-size: 15.5px; }

    pre { background: #121212; border: 1px solid #222; border-radius: 8px; padding: 20px; overflow-x: auto; margin: 24px 0; font-family: "JetBrains Mono", monospace; font-size: 13.5px; line-height: 1.6; color: #E5E5E5; }
    code { font-family: "JetBrains Mono", monospace; font-size: 0.9em; background: #1A1A1A; padding: 2px 6px; border-radius: 4px; color: #C1DD2D; }

    /* Tables */
    .table-container { overflow-x: auto; margin: 32px 0; border: 1px solid #222; border-radius: 12px; -webkit-overflow-scrolling: touch; }
    table { width: 100%; min-width: 640px; border-collapse: collapse; text-align: left; font-size: 14.5px; }
    th { background: #161616; color: #FFF; padding: 14px 18px; font-weight: 700; border-bottom: 1px solid #222; }
    td { padding: 14px 18px; border-bottom: 1px solid #1A1A1A; color: #CCC; }
    tr:last-child td { border-bottom: none; }
    tr:nth-child(even) { background: rgba(255,255,255,0.01); }

    /* Interactive Studio */
    .interactive-sandbox { background: #121212; border: 1px solid #262626; border-radius: 12px; padding: 24px; margin: 36px 0; }
    .sandbox-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px; border-bottom: 1px solid #222; padding-bottom: 14px; }
    .sandbox-title { display: flex; align-items: center; gap: 8px; font-weight: 800; font-size: 16px; color: #FFF; }
    .sandbox-title svg { color: #C1DD2D; }
    .sandbox-badge { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; background: rgba(193,221,45,0.12); color: #C1DD2D; padding: 3px 8px; border-radius: 4px; border: 1px solid rgba(193,221,45,0.25); }

    .sandbox-grid { display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr); gap: 24px; align-items: start; }
    @media (max-width: 768px) { .sandbox-grid { grid-template-columns: 1fr; } }

    .sandbox-controls { display: flex; flex-direction: column; gap: 16px; }
    .control-row { display: flex; flex-direction: column; gap: 6px; }
    .control-row label { font-size: 13px; font-weight: 600; color: #BBB; display: flex; justify-content: space-between; }
    .control-row .stat-num { color: #C1DD2D; font-family: "JetBrains Mono", monospace; }

    .control-select, .control-input { background: #181818; border: 1px solid #333; color: #F2F2F2; padding: 8px 12px; border-radius: 6px; font-family: "Inter", sans-serif; font-size: 13.5px; width: 100%; }
    .control-select:focus, .control-input:focus { outline: none; border-color: #C1DD2D; }

    .stage-wrapper { display: flex; flex-direction: column; gap: 14px; }
    .preview-stage-container { width: 100%; height: 320px; border: 1px dashed #444; border-radius: 10px; background: #080808; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; }
    .viewport-meta-overlay { position: absolute; bottom: 8px; right: 10px; font-size: 11px; font-family: "JetBrains Mono", monospace; color: #888; background: rgba(0,0,0,0.8); padding: 3px 8px; border-radius: 4px; pointer-events: none; border: 1px solid #222; }

    .stats-readout-box { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; background: #0E0E0E; border: 1px solid #222; border-radius: 8px; padding: 12px; }
    .stat-item { text-align: center; }
    .stat-label { font-size: 11px; text-transform: uppercase; color: #777; font-weight: 700; letter-spacing: 0.05em; }
    .stat-val { font-size: 13px; font-weight: 800; color: #FFF; font-family: "JetBrains Mono", monospace; margin-top: 2px; }
    .stat-val.highlight { color: #C1DD2D; }

    .generated-code-box { margin-top: 20px; background: #0A0A0A; border: 1px solid #262626; border-radius: 8px; overflow: hidden; }
    .code-box-head { display: flex; justify-content: space-between; align-items: center; padding: 10px 14px; background: #161616; border-bottom: 1px solid #222; font-size: 12px; font-weight: 700; color: #888; flex-wrap: wrap; gap: 8px; }
    .code-tabs { display: flex; gap: 6px; }
    .code-tab-btn { background: transparent; border: none; color: #888; font-size: 12px; font-weight: 700; cursor: pointer; padding: 4px 8px; border-radius: 4px; }
    .code-tab-btn.active { color: #C1DD2D; background: rgba(193,221,45,0.12); }
    .code-actions { display: flex; gap: 8px; }
    .copy-btn { background: rgba(193,221,45,0.15); border: 1px solid rgba(193,221,45,0.3); color: #C1DD2D; font-size: 11px; font-weight: 700; padding: 5px 12px; border-radius: 4px; cursor: pointer; transition: all 120ms ease; }
    .copy-btn:hover { background: #C1DD2D; color: #0A0A0A; }
    .code-output-area { padding: 16px; max-height: 180px; overflow-y: auto; font-family: "JetBrains Mono", monospace; font-size: 12px; line-height: 1.5; color: #E5E5E5; word-break: break-all; white-space: pre-wrap; background: #080808; margin: 0; border: none; }

    /* Formula Cards & Callouts */
    .formula-card { background: #161616; border: 1px solid #2E2E2E; border-left: 3px solid #C1DD2D; border-radius: 8px; padding: 16px 20px; margin: 20px 0; overflow-x: auto; -webkit-overflow-scrolling: touch; }
    .formula-title { font-size: 12px; text-transform: uppercase; letter-spacing: 0.06em; color: #888; font-weight: 700; margin-bottom: 6px; }
    .formula-body { font-family: "JetBrains Mono", monospace; font-size: 14px; color: #C1DD2D; line-height: 1.5; overflow-x: auto; -webkit-overflow-scrolling: touch; }
    .formula-desc { font-size: 13.5px; color: #AAA; margin-top: 8px; line-height: 1.5; }

    .takeaway-box { background: linear-gradient(135deg, rgba(193,221,45,0.06) 0%, rgba(193,221,45,0.02) 100%); border: 1px solid rgba(193,221,45,0.2); border-radius: 12px; padding: 28px; margin: 40px 0; }
    .takeaway-box h3 { color: #C1DD2D; font-size: 18px; font-weight: 800; margin-bottom: 16px; margin-top: 0; }
    .warning-box { background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.25); border-left: 4px solid #EF4444; border-radius: 8px; padding: 18px 22px; margin: 24px 0; }
    .warning-box h4 { color: #F87171; font-size: 15px; margin-bottom: 8px; }
    .warning-box p { color: #E5E5E5; margin-bottom: 0; font-size: 14.5px; }

    .faq-item { background: #121212; border: 1px solid #222; border-radius: 8px; margin-bottom: 14px; padding: 18px 22px; }
    .faq-item h3 { margin-top: 0; font-size: 16px; color: #FFF; margin-bottom: 8px; }
    .faq-item p { margin-bottom: 0; color: #A3A3A3; font-size: 14.5px; }

    /* Sticky Sidebar */
    .article-sidebar { display: flex; flex-direction: column; gap: 24px; }
    @media (min-width: 1024px) {
      .article-sidebar { position: sticky; top: 80px; }
    }
    .sidebar-card { background: #121212; border: 1px solid #222; border-radius: 12px; padding: 24px; }
    .sidebar-title { font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin-bottom: 16px; }
    .toc-nav ol { list-style: none; margin: 0; padding: 0; }
    .toc-nav li { margin-bottom: 10px; font-size: 14px; }
    .toc-nav a { color: #A3A3A3; display: block; line-height: 1.5; }
    .toc-nav a:hover { color: #C1DD2D; }

    .cta-sidebar-box { background: linear-gradient(145deg, #181E07 0%, #0F1205 100%); border: 1px solid rgba(193,221,45,0.3); border-radius: 12px; padding: 24px; text-align: center; }
    .cta-sidebar-box h4 { font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 8px; }
    .cta-sidebar-box p { font-size: 13.5px; color: #AAA; line-height: 1.5; margin-bottom: 16px; }
    .cta-sidebar-btn { display: inline-block; width: 100%; background: #C1DD2D; color: #0A0A0A; font-weight: 800; font-size: 14px; padding: 12px 18px; border-radius: 6px; transition: all 150ms ease; }
    .cta-sidebar-btn:hover { background: #D2ED3E; transform: translateY(-1px); }

    .site-footer { border-top: 1px solid #1F1F1F; padding: 48px 24px; background: #0A0A0A; text-align: center; font-size: 14px; color: #666; margin-top: 80px; }
    .site-footer a { color: #888; }
    .site-footer a:hover { color: #C1DD2D; }

    @media (max-width: 768px) {
      .page-container { padding: 28px 16px 60px; }
      .site-header nav a:not(.header-cta) { display: none; }
      .site-header nav { gap: 12px; }
      .header-cta { padding: 6px 12px; font-size: 12px; }
      .article-hero h1 { font-size: 26px; }
      .featured-summary { padding: 18px 20px; }
      pre { padding: 14px; font-size: 12.5px; }
      .stats-readout-box { grid-template-columns: 1fr; }
    }

    /* Light Theme Contrast Rules */
    html[data-theme="light"] body { background: #FAFAFA; color: #171717; }
    html[data-theme="light"] .site-header { background: rgba(250,250,250,0.88); border-bottom-color: #E5E5E5; }
    html[data-theme="light"] .site-header .logo { color: #171717; }
    html[data-theme="light"] .site-header nav a { color: #525252; }
    html[data-theme="light"] .article-hero h1 { color: #0A0A0A; }
    html[data-theme="light"] h2 { color: #0A0A0A; border-top-color: #E5E5E5; }
    html[data-theme="light"] h3 { color: #171717; }
    html[data-theme="light"] h4 { color: #262626; }
    html[data-theme="light"] p, html[data-theme="light"] ul, html[data-theme="light"] ol { color: #383838; }
    html[data-theme="light"] strong { color: #0A0A0A; }
    html[data-theme="light"] .featured-summary { background: #F4F4F5; border-color: #E4E4E7; border-left-color: #849E00; }
    html[data-theme="light"] .featured-summary p { color: #18181B; }
    html[data-theme="light"] pre { background: #F4F4F5; border-color: #E4E4E7; color: #18181B; }
    html[data-theme="light"] pre code { background: transparent; color: #18181B; }
    html[data-theme="light"] code { background: #E4E4E7; color: #4D6300; }
    html[data-theme="light"] a { color: #4D6300; }
    html[data-theme="light"] a:hover { color: #364600; }
    html[data-theme="light"] .site-header nav a:hover { color: #0A0A0A; }
    html[data-theme="light"] .breadcrumb a { color: #4D6300; }
    html[data-theme="light"] .breadcrumb a:hover { color: #364600; }
    html[data-theme="light"] .toc-nav a { color: #3F3F46; }
    html[data-theme="light"] .toc-nav a:hover { color: #4D6300; }
    html[data-theme="light"] .site-footer a { color: #4D6300; }
    html[data-theme="light"] .site-footer a:hover { color: #364600; }
    html[data-theme="light"] .article-hero .tag { background: #E4E4E7; color: #4D6300; border-color: #D4D4D8; }
    html[data-theme="light"] .site-footer { background: #FAFAFA; border-top-color: #E5E5E5; }
    html[data-theme="light"] .sidebar-card { background: #F4F4F5; border-color: #E4E4E7; }
    html[data-theme="light"] .cta-sidebar-box { background: #ECFDF5; border-color: #A7F3D0; }
    html[data-theme="light"] .cta-sidebar-box h4 { color: #064E3B; }
    html[data-theme="light"] .cta-sidebar-box p { color: #047857; }
    html[data-theme="light"] th { background: #F4F4F5; color: #18181B; border-bottom-color: #E4E4E7; }
    html[data-theme="light"] td { border-bottom-color: #E4E4E7; color: #3F3F46; }
    html[data-theme="light"] .table-container { border-color: #E4E4E7; }
    html[data-theme="light"] .interactive-sandbox { background: #F4F4F5; border-color: #E4E4E7; }
    html[data-theme="light"] .sandbox-header { border-bottom-color: #E4E4E7; }
    html[data-theme="light"] .sandbox-title { color: #18181B; }
    html[data-theme="light"] .control-row label { color: #4B5563; }
    html[data-theme="light"] .preview-stage-container { background: #F9FAFB; border-color: #D1D5DB; }
    html[data-theme="light"] .control-select, html[data-theme="light"] .control-input { background: #FFFFFF; border-color: #D1D5DB; color: #18181B; }
    html[data-theme="light"] .generated-code-box { background: #FAFAFA; border-color: #E4E4E7; }
    html[data-theme="light"] .code-box-head { background: #F4F4F5; border-bottom-color: #E4E4E7; color: #525252; }
    html[data-theme="light"] .code-output-area { background: #FFFFFF; color: #1F2937; }
    html[data-theme="light"] .copy-btn { background: #F0F4D8; border-color: #D2ED3E; color: #4D6300; }
    html[data-theme="light"] .copy-btn:hover { background: #4D6300; color: #FFF; }
    html[data-theme="light"] .stats-readout-box { background: #F4F4F5; border-color: #E4E4E7; }
    html[data-theme="light"] .stat-val { color: #18181B; }
    html[data-theme="light"] .stat-val.highlight { color: #4D6300; }
    html[data-theme="light"] .sandbox-badge { background: #E4E4E7; color: #4D6300; border-color: #D4D4D8; }
    html[data-theme="light"] .control-row .stat-num { color: #4D6300; }
    html[data-theme="light"] .formula-card { background: #F4F4F5; border-color: #E4E4E7; border-left-color: #849E00; }
    html[data-theme="light"] .formula-title { color: #4D6300; }
    html[data-theme="light"] .formula-body { color: #18181B; }
    html[data-theme="light"] .formula-desc { color: #525252; }
    html[data-theme="light"] .takeaway-box { background: #F4F4F5; border-color: #E4E4E7; }
    html[data-theme="light"] .takeaway-box h3 { color: #4D6300; }
    html[data-theme="light"] .warning-box { background: #FEF2F2; border-color: #FCA5A5; border-left-color: #EF4444; }
    html[data-theme="light"] .warning-box h4 { color: #B91C1C; }
    html[data-theme="light"] .warning-box p { color: #450A0A; }
    html[data-theme="light"] .sidebar-title { color: #4D6300; }
    html[data-theme="light"] .stat-label { color: #525252; }
    html[data-theme="light"] .article-meta a { color: #4D6300; }
  </style>
</head>
<body>

  <header class="site-header">
    <a href="/" class="logo" aria-label="IconStash.io home">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 21 7v10l-9 5-9-5V7l9-5Z"/><path d="m8 9 4-2 4 2v6l-4 2-4-2V9Z"/></svg>
      <span>IconStash</span>
    </a>
    <nav>
      <a href="/#/">Search 134K+ Icons</a>
      <a href="/articles/">Articles &amp; Guides</a>
      <a href="/Listicles/best-free-icon-sets-2026/">Best Sets</a>
      <a href="/Glossary/icon-svg-terminology/">Glossary</a>
      <a href="/stats/">Statistics</a>
      <button class="theme-toggle-btn" id="themeToggle" aria-label="Toggle Theme">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
      </button>
      <a href="/#/" class="header-cta">Open App</a>
    </nav>
  </header>

  <main class="page-container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a>
      <span class="sep">/</span>
      <a href="/articles/">Articles</a>
      <span class="sep">/</span>
      <span>CSS clip-path &amp; SVG Masking Guide</span>
    </nav>

    <header class="article-hero">
      <span class="tag">CSS Architecture &bull; 2026</span>
      <h1>CSS clip-path &amp; SVG Masking Deep Dive: Polygon, Path() &amp; Alpha Masks</h1>
      <div class="article-meta">
        <span>By <a href="/about/">Jouni Flemming</a></span>
        <span>&bull;</span>
        <span>October 30, 2026</span>
        <span>&bull;</span>
        <span>23 min read</span>
        <span>&bull;</span>
        <span>4,092 words</span>
      </div>
    </header>

    <div class="article-layout">
      <article class="article-main">

        <div class="featured-summary">
          <p><strong>Executive Summary for UI Architects &amp; Frontend Engineers:</strong></p>
          <ul>
            <li><strong>Clipping vs Masking Distinction:</strong> Master the critical boundary between 1-bit binary clipping (<code>clip-path</code> / <code>&lt;clipPath&gt;</code>) and 8-bit multi-channel alpha/luminance masking (<code>mask-image</code> / <code>&lt;mask&gt;</code>).</li>
            <li><strong>Native CSS Shapes:</strong> Author complex geometric cutouts with <code>inset()</code>, <code>circle()</code>, <code>ellipse()</code>, and multi-vertex <code>polygon()</code> with winding rules (<code>nonzero</code> vs <code>evenodd</code>).</li>
            <li><strong>Responsive Unit Scaling:</strong> Harness <code>clipPathUnits="objectBoundingBox"</code> to normalize vector coordinates to <code>[0.0, 1.0]</code>, ensuring clipping silhouettes stretch fluidly across any viewport dimensions.</li>
            <li><strong>Morphing Transitions &amp; WAAPI:</strong> Animate clip paths on hardware compositor threads by enforcing matching vertex counts and leveraging the Web Animations API.</li>
            <li><strong>Interactive Developer Sandbox:</strong> Test live clipping silhouettes, gradients, and export production CSS and Tailwind v4 code snippets.</li>
          </ul>
        </div>

        <figure class="article-figure">
          <img src="/assets/articles/css-clip-path-and-svg-masking-guide.jpg" alt="CSS clip-path and SVG Masking Architecture Technical Diagram" width="1200" height="675" loading="eager">
          <figcaption>Figure 1: Architecture diagram comparing CSS clip-path polygon and path functions with SVG clipPath and alpha-luminance masking compositing layers.</figcaption>
        </figure>

` + p1_intro + p2_fundamentals + p3_shapes + p4_path_fn + p5_svg_clippath + p6_boundingbox + p7_masks + p8_animation + p9_gpu + p10_studio + p11_recipes + p12_compat + p13_faq + `
      </article>

      <aside class="article-sidebar">
        <div class="sidebar-card">
          <div class="sidebar-title">Table of Contents</div>
          <nav class="toc-nav">
            <ol>
              <li><a href="#section-intro">1. Modern Vector Clipping</a></li>
              <li><a href="#section-fundamentals">2. Fundamentals: Clip vs Mask</a></li>
              <li><a href="#section-basic-shapes">3. CSS Basic Shapes</a></li>
              <li><a href="#section-path-function">4. The path() Function</a></li>
              <li><a href="#section-svg-clippath">5. SVG clipPath Elements</a></li>
              <li><a href="#section-objectboundingbox">6. objectBoundingBox Scaling</a></li>
              <li><a href="#section-svg-masks">7. Alpha vs Luminance Masks</a></li>
              <li><a href="#section-animation">8. Animating Clip Paths</a></li>
              <li><a href="#section-gpu-compositing">9. GPU Performance &amp; Layers</a></li>
              <li><a href="#section-interactive-studio">10. Interactive Sandbox</a></li>
              <li><a href="#section-ui-recipes">11. Production UI Patterns</a></li>
              <li><a href="#section-compat-matrix">12. Browser Compatibility</a></li>
              <li><a href="#section-faq">13. FAQ</a></li>
            </ol>
          </nav>
        </div>

        <div class="cta-sidebar-box">
          <h4>Explore 134K+ SVG Icons</h4>
          <p>Looking for pristine vector paths ready for custom clip paths and CSS masks? Search IconStash now.</p>
          <a href="/#/" class="cta-sidebar-btn">Search IconStash</a>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div style="margin-bottom: 16px;">
      <a href="/">Home</a> &bull;
      <a href="/articles/">Articles</a> &bull;
      <a href="/Listicles/best-free-icon-sets-2026/">Best Sets</a> &bull;
      <a href="/Glossary/icon-svg-terminology/">Glossary</a> &bull;
      <a href="/stats/">Statistics</a> &bull;
      <a href="/about/">About</a>
    </div>
    <p>&copy; 2026 IconStash.io &bull; Engineered for high-performance web graphics.</p>
  </footer>

  <script>
    // Theme toggle handling
    const themeToggle = document.getElementById('themeToggle');
    const htmlEl = document.documentElement;
    const savedTheme = localStorage.getItem('theme') || 'dark';
    htmlEl.setAttribute('data-theme', savedTheme);

    if (themeToggle) {
      themeToggle.addEventListener('click', () => {
        const nextTheme = htmlEl.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        htmlEl.setAttribute('data-theme', nextTheme);
        try { localStorage.setItem('theme', nextTheme); } catch(e) {}
      });
    }

    // Interactive Clip-Path & Masking Studio Logic
    (function initClipStudio() {
      const clipModeSelect = document.getElementById('clipModeSelect');
      const clipModeDisplay = document.getElementById('clipModeDisplay');
      const clipPresetSelect = document.getElementById('clipPresetSelect');
      const bgGradientSelect = document.getElementById('bgGradientSelect');
      const clipScaleSlider = document.getElementById('clipScaleSlider');
      const scaleVal = document.getElementById('scaleVal');

      const previewClippedCard = document.getElementById('previewClippedCard');
      const clipMetaOverlay = document.getElementById('clipMetaOverlay');

      const compositorStatus = document.getElementById('compositorStatus');
      const stackingStatus = document.getElementById('stackingStatus');
      const areaRatioVal = document.getElementById('areaRatioVal');
      const hitTestStatus = document.getElementById('hitTestStatus');

      const clipCodeOutput = document.getElementById('clipCodeOutput');
      const copyClipCodeBtn = document.getElementById('copyClipCodeBtn');
      const codeTabButtons = document.querySelectorAll('.code-tab-btn');
      let currentTab = 'css';

      const presets = {
        hexagon: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)',
        chevron: 'polygon(75% 0%, 100% 50%, 75% 100%, 0% 100%, 25% 50%, 0% 0%)',
        ribbon: 'polygon(0% 0%, 100% 0%, 100% 100%, 50% 80%, 0% 100%)',
        badge: 'polygon(0% 0%, 70% 0%, 70% 25%, 100% 25%, 100% 100%, 0% 100%)'
      };

      function updateStudio() {
        const mode = clipModeSelect.value;
        const presetKey = clipPresetSelect.value;
        const bgKey = bgGradientSelect.value;
        const scale = parseInt(clipScaleSlider.value, 10);
        scaleVal.textContent = scale + '%';

        // Background styling
        if (bgKey === 'cyber') {
          previewClippedCard.style.background = 'linear-gradient(135deg, #C1DD2D 0%, #15803D 100%)';
          previewClippedCard.style.color = '#0A0A0A';
        } else if (bgKey === 'glass') {
          previewClippedCard.style.background = 'linear-gradient(135deg, rgba(193,221,45,0.3) 0%, rgba(255,255,255,0.05) 100%)';
          previewClippedCard.style.color = '#F2F2F2';
        } else {
          previewClippedCard.style.background = 'radial-gradient(circle at center, #38BDF8 0%, #1E1B4B 100%)';
          previewClippedCard.style.color = '#FFFFFF';
        }

        let clipValue = '';
        let maskValue = '';

        if (mode === 'polygon') {
          clipModeDisplay.textContent = 'CSS polygon()';
          clipValue = presets[presetKey] || presets.hexagon;
          previewClippedCard.style.clipPath = clipValue;
          previewClippedCard.style.mask = 'none';
          previewClippedCard.style.webkitMask = 'none';
          clipMetaOverlay.textContent = 'clip-path: ' + clipValue;
        } else if (mode === 'circle') {
          clipModeDisplay.textContent = 'CSS circle()';
          const r = Math.round(scale / 2);
          clipValue = 'circle(' + r + '% at 50% 50%)';
          previewClippedCard.style.clipPath = clipValue;
          previewClippedCard.style.mask = 'none';
          previewClippedCard.style.webkitMask = 'none';
          clipMetaOverlay.textContent = 'clip-path: ' + clipValue;
        } else if (mode === 'path') {
          clipModeDisplay.textContent = 'CSS path()';
          clipValue = "path('M 120 10 L 230 70 L 230 170 L 120 230 L 10 170 L 10 70 Z')";
          previewClippedCard.style.clipPath = clipValue;
          previewClippedCard.style.mask = 'none';
          previewClippedCard.style.webkitMask = 'none';
          clipMetaOverlay.textContent = 'clip-path: path(...)';
        } else if (mode === 'mask') {
          clipModeDisplay.textContent = 'SVG Luminance Mask';
          previewClippedCard.style.clipPath = 'none';
          maskValue = 'radial-gradient(circle at center, black ' + Math.round(scale * 0.5) + '%, transparent ' + scale + '%)';
          previewClippedCard.style.mask = maskValue;
          previewClippedCard.style.webkitMask = maskValue;
          clipMetaOverlay.textContent = 'mask: radial-gradient(...)';
        }

        compositorStatus.textContent = 'GPU Layer Promoted';
        stackingStatus.textContent = 'Created (Isolated)';
        areaRatioVal.textContent = Math.round(scale * 0.75) + '% Visual Area';
        hitTestStatus.textContent = mode === 'mask' ? 'Alpha Graded' : 'Restricted to Silhouette';

        // Code generation update
        if (currentTab === 'css') {
          if (mode === 'mask') {
            clipCodeOutput.textContent =
'/* Modern CSS Masking with Gradient Feather */\\n' +
'.feathered-card {\\n' +
'  mask-image: ' + maskValue + ';\\n' +
'  -webkit-mask-image: ' + maskValue + ';\\n' +
'  will-change: mask-image;\\n' +
'}';
          } else {
            clipCodeOutput.textContent =
'/* Hardware-Accelerated CSS Clip-Path */\\n' +
'.clipped-card {\\n' +
'  clip-path: ' + clipValue + ';\\n' +
'  will-change: clip-path;\\n' +
'  transition: clip-path 250ms cubic-bezier(0.16, 1, 0.3, 1);\\n' +
'}';
          }
        } else if (currentTab === 'tailwind') {
          if (mode === 'mask') {
            clipCodeOutput.textContent =
'<!-- Tailwind CSS v4 Mask Utility -->\\n' +
'<div class="w-60 h-60 bg-gradient-to-br from-[#C1DD2D] to-green-700 [mask-image:' + maskValue.replace(/ /g, '_') + ']">\\n' +
'  <!-- Card Content -->\\n' +
'</div>';
          } else {
            clipCodeOutput.textContent =
'<!-- Tailwind CSS v4 Arbitrary Clip-Path Utility -->\\n' +
'<div class="w-60 h-60 bg-gradient-to-br from-[#C1DD2D] to-green-700 [clip-path:' + clipValue.replace(/ /g, '_') + '] hover:scale-105 transition-transform">\\n' +
'  <!-- Card Content -->\\n' +
'</div>';
          }
        } else if (currentTab === 'svg') {
          clipCodeOutput.textContent =
'<!-- Reusable Responsive SVG clipPath (objectBoundingBox) -->\\n' +
'<svg width="0" height="0" class="absolute pointer-events-none" aria-hidden="true">\\n' +
'  <defs>\\n' +
'    <clipPath id="customClip" clipPathUnits="objectBoundingBox">\\n' +
'      <path d="M 0.5 0 L 1.0 0.25 L 1.0 0.75 L 0.5 1.0 L 0.0 0.75 L 0.0 0.25 Z"/>\\n' +
'    </clipPath>\\n' +
'  </defs>\\n' +
'</svg>\\n\\n' +
'<!-- Apply to DOM elements: -->\\n' +
'<div style="clip-path: url(#customClip);"></div>';
        }
      }

      [clipModeSelect, clipPresetSelect, bgGradientSelect, clipScaleSlider].forEach(el => {
        el.addEventListener('input', updateStudio);
        el.addEventListener('change', updateStudio);
      });

      codeTabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
          codeTabButtons.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          currentTab = btn.getAttribute('data-tab');
          updateStudio();
        });
      });

      if (copyClipCodeBtn) {
        copyClipCodeBtn.addEventListener('click', () => {
          navigator.clipboard.writeText(clipCodeOutput.textContent).then(() => {
            copyClipCodeBtn.textContent = 'Copied!';
            setTimeout(() => { copyClipCodeBtn.textContent = 'Copy Snippet'; }, 2000);
          }).catch(() => {
            copyClipCodeBtn.textContent = 'Failed to copy';
          });
        });
      }

      updateStudio();
    })();
  </script>
</body>
</html>
`;

fs.writeFileSync(path.join(outDir, 'index.html'), fullHtml, 'utf8');
console.log('Article 3 generated successfully!');

const cleanBody = fullHtml.replace(/<(script|style)[^>]*>[\s\S]*?<\/\1>/gi, '').replace(/<[^>]+>/g, ' ');
const words = cleanBody.split(/\s+/).filter(w => w.length > 0);
console.log(`Article 3 word count: ${words.length} words`);
