with open(r"D:\Project IconStash\IconStash\scripts\gen_nov21_article3.py", "r", encoding="utf-8") as f:
    code = f.read()

target = r'''        <section id="section-streaming-telemetry">
          <h2>9. Streaming Real-Time Telemetry &amp; WebSocket DOM Virtualization</h2>
          <p>In production algorithmic environments, trading dashboards ingest continuous market tick events streamed over low-latency WebSockets. If every incoming price update triggers complete SVG DOM reconstruction, garbage collection overhead will quickly degrade rendering performance. High-frequency SVG architectures implement three critical real-time optimizations:</p>

          <ul>
            <li><strong>Sliding Buffer Ring:</strong> Maintain a fixed-length circular buffer of visible candles (e.g., 60 bars). When a new candle completes, evict the oldest candle from the left margin, slide existing elements horizontally, and append the new candle to the right.</li>
            <li><strong>Direct DOM Mutation for Live Bar:</strong> The currently open candle (the active time bucket) fluctuates continuously on every matched tick. Rather than re-rendering the entire chart, the WebSocket message handler targets only the single active candle's <code>&lt;rect&gt;</code> and <code>&lt;line&gt;</code> DOM nodes, updating their <code>height</code>, <code>y</code>, and <code>y2</code> attributes directly in memory.</li>
            <li><strong>Throttled Price Scale Recalibration:</strong> Recalibrating the vertical price scale Y-axis on every tick causes the chart to jiggle vertically. Production systems recalculate the price domain only when a new tick exceeds the current visible high or low boundary, maintaining smooth visual continuity.</li>
          </ul>
        </section>'''

replacement = r'''        <section id="section-streaming-telemetry">
          <h2>9. Streaming Real-Time Telemetry &amp; WebSocket DOM Virtualization</h2>
          <p>In production algorithmic environments, trading dashboards ingest continuous market tick events streamed over low-latency WebSockets. If every incoming price update triggers complete SVG DOM reconstruction, garbage collection overhead will quickly degrade rendering performance. High-frequency SVG architectures implement three critical real-time optimizations:</p>

          <ul>
            <li><strong>Sliding Buffer Ring:</strong> Maintain a fixed-length circular buffer of visible candles (e.g., 60 bars). When a new candle completes, evict the oldest candle from the left margin, slide existing elements horizontally, and append the new candle to the right.</li>
            <li><strong>Direct DOM Mutation for Live Bar:</strong> The currently open candle (the active time bucket) fluctuates continuously on every matched tick. Rather than re-rendering the entire chart, the WebSocket message handler targets only the single active candle's <code>&lt;rect&gt;</code> and <code>&lt;line&gt;</code> DOM nodes, updating their <code>height</code>, <code>y</code>, and <code>y2</code> attributes directly in memory.</li>
            <li><strong>Throttled Price Scale Recalibration:</strong> Recalibrating the vertical price scale Y-axis on every tick causes the chart to jiggle vertically. Production systems recalculate the price domain only when a new tick exceeds the current visible high or low boundary, maintaining smooth visual continuity.</li>
          </ul>

          <h3>Architectural Boundary: When to Transition from SVG to Canvas/WebGL</h3>
          <p>A frequent technical debate among fintech architects centers on the exact boundary where Scalable Vector Graphics should yield to rasterized HTML5 2D Canvas or WebGL. Because SVG manages elements as individual C++ objects in the browser DOM, there is an upper threshold beyond which DOM layout calculations degrade rendering throughput:</p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Time Horizon &amp; Bar Count</th>
                  <th>Recommended Architecture</th>
                  <th>Strengths &amp; Operational Trade-offs</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Intraday Focus (1 to 200 bars)</strong></td>
                  <td>Pure SVG Vector DOM</td>
                  <td>Optimal for desktop and mobile dashboards. Razor-sharp vector scaling on 4K retina displays, zero blur on zoom, declarative CSS dark/light theming, effortless clipboard vector copy, and native screen reader accessibility.</td>
                </tr>
                <tr>
                  <td><strong>Multi-Day Swing (200 to 1,500 bars)</strong></td>
                  <td>Hybrid SVG + Path Bundling</td>
                  <td>Excellent performance when consolidating wicks and bodies into bundled <code>&lt;path&gt;</code> definitions. Minimal DOM footprint (under 20 total DOM elements) while retaining all SVG export and styling advantages.</td>
                </tr>
                <tr>
                  <td><strong>Multi-Year Tick History (1,500 to 100,000+ bars)</strong></td>
                  <td>HTML5 Canvas or WebGL 2.0</td>
                  <td>Required for massive historical backtesting and tick-by-tick visual playback where tens of thousands of data points must be repainted at 60 FPS. Sacrifices native DOM accessibility and clipboard vector export.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p>For executive reporting, interactive technical analysis widgets, customer-facing portfolio dashboards, and modern crypto exchange trading UIs—where viewports display between 30 and 150 candles at any given moment—SVG is unequivocally the superior technological foundation. It eliminates fuzzy bitmap artifacts, guarantees crisp integer-aligned wicks, and integrates seamlessly with web components and standard frontend styling frameworks.</p>
        </section>'''

assert target in code, "streaming target not found"
code = code.replace(target, replacement)

with open(r"D:\Project IconStash\IconStash\scripts\gen_nov21_article3.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Expanded gen_nov21_article3.py phase 2 successfully.")
