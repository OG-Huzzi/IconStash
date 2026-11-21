import os
import re

with open(r"D:\Project IconStash\IconStash\scripts\gen_nov21_article3.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Expand Section 1
sec1_target = r'''          <p>In modern web applications, rendering high-density financial charts historically forced developers to rely on heavy, proprietary canvas packages or clunky third-party iframes that broke responsive styling, hindered screenshot generation, and prevented accessibility. Modern Scalable Vector Graphics (SVG) completely transforms this landscape. By leveraging declarative DOM paths, native CSS animations, GPU hardware acceleration, and SVG's unique <code>shape-rendering="crispEdges"</code> engine, developers can author blazing-fast, institutional-grade financial dashboards directly in clean HTML5.</p>
        </section>'''

sec1_replacement = r'''          <p>In modern web applications, rendering high-density financial charts historically forced developers to rely on heavy, proprietary canvas packages or clunky third-party iframes that broke responsive styling, hindered screenshot generation, and prevented accessibility. Modern Scalable Vector Graphics (SVG) completely transforms this landscape. By leveraging declarative DOM paths, native CSS animations, GPU hardware acceleration, and SVG's unique <code>shape-rendering="crispEdges"</code> engine, developers can author blazing-fast, institutional-grade financial dashboards directly in clean HTML5.</p>

          <h3>Market Microstructure &amp; The Mechanics of Discrete Time Resampling</h3>
          <p>Underneath every clean OHLC candlestick lies the microscopic reality of the Limit Order Book (LOB). An electronic exchange matches buy limit orders (bids) and sell limit orders (asks). When incoming market orders execute against resting limit orders, a trade event is emitted with three atomic properties: execution price, executed trade size (volume), and high-resolution UNIX timestamp. A liquid asset like Apple or Bitcoin can generate hundreds of discrete trade executions within a single second.</p>

          <p>To convert this continuous asynchronous trade feed into periodic candlestick intervals, quantitative data pipelines execute temporal bucket resampling. An interval window of duration &Delta;t (such as 60 seconds) is established. The first trade executed at or after timestamp t0 sets the Open price; the maximum price among all trades within [t0, t0 + &Delta;t) defines the High; the minimum price defines the Low; and the final trade before t0 + &Delta;t defines the Close. The volume metric accumulates the sum of all trade shares executed throughout the window. If no trades occur during a quiet interval, the candle is formed as a flat horizontal tick matching the previous period's Close with zero volume, maintaining unbroken temporal continuity across the time series.</p>
        </section>'''

assert sec1_target in code, "sec1_target not found"
code = code.replace(sec1_target, sec1_replacement)

# 2. Expand Section 2
sec2_target = r'''          <p>In SVG markup, the upper and lower wicks can either be rendered as two distinct line elements or consolidated into a single continuous vertical line stretching from <code>scaleY(High)</code> to <code>scaleY(Low)</code> rendered underneath the real body rectangle. Consolidating wicks into a single line reduces DOM element count by 33%, delivering significant rendering efficiency on dense timeframes.</p>
        </section>'''

sec2_replacement = r'''          <p>In SVG markup, the upper and lower wicks can either be rendered as two distinct line elements or consolidated into a single continuous vertical line stretching from <code>scaleY(High)</code> to <code>scaleY(Low)</code> rendered underneath the real body rectangle. Consolidating wicks into a single line reduces DOM element count by 33%, delivering significant rendering efficiency on dense timeframes.</p>

          <h3>Taxonomy of Candlestick Morphology &amp; Reversal Patterns</h3>
          <p>Quantitative algorithmic trading models parse candlestick geometry to identify shifts in supply-demand equilibrium. By evaluating the ratio between real body height, upper shadow length, and lower shadow length, algorithmic screeners classify candle silhouettes into standardized morphological categories:</p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Candlestick Pattern</th>
                  <th>Visual Geometric Properties</th>
                  <th>Market Psychology &amp; Sentiment</th>
                  <th>Trading Bias</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Hammer / Pin Bar</strong></td>
                  <td>Small real body at top; lower wick &ge; 2&times; body height; negligible upper wick.</td>
                  <td>Intense intra-session selling pressure completely absorbed by institutional buying at session lows.</td>
                  <td>Bullish Reversal</td>
                </tr>
                <tr>
                  <td><strong>Shooting Star</strong></td>
                  <td>Small real body at bottom; upper wick &ge; 2&times; body height; negligible lower wick.</td>
                  <td>Intra-session buying breakout rejected by aggressive overhead liquidity and institutional distribution.</td>
                  <td>Bearish Reversal</td>
                </tr>
                <tr>
                  <td><strong>Bullish Engulfing</strong></td>
                  <td>Large green real body whose vertical span completely encloses the preceding red body.</td>
                  <td>Complete sentiment shift; buyers overpower earlier selling momentum with expanding volume.</td>
                  <td>Bullish Continuation / Reversal</td>
                </tr>
                <tr>
                  <td><strong>Bearish Engulfing</strong></td>
                  <td>Large red real body whose vertical span completely encloses the preceding green body.</td>
                  <td>Buyers trapped at market peak; institutional liquidation triggers cascading stop-loss selling.</td>
                  <td>Bearish Continuation / Reversal</td>
                </tr>
                <tr>
                  <td><strong>Marubozu</strong></td>
                  <td>Full solid rectangle spanning entire High-to-Low range; zero or microscopic wicks.</td>
                  <td>Unilateral one-directional domination from opening bell to closing cross; maximum trend conviction.</td>
                  <td>Strong Trend Continuation</td>
                </tr>
                <tr>
                  <td><strong>Dragonfly Doji</strong></td>
                  <td>Open, High, and Close share identical coordinate; elongated lower wick; zero upper wick.</td>
                  <td>Severe downward rejection at major support levels; bears failed to hold lower ground.</td>
                  <td>Bullish Exhaustion / Pivot</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>'''

assert sec2_target in code, "sec2_target not found"
code = code.replace(sec2_target, sec2_replacement)

# 3. Expand Section 3
sec3_target = r'''          <p>This guarantees ample breathing room for technical indicator overlays, price callout pill badges, and horizontal gridlines.</p>
        </section>'''

sec3_replacement = r'''          <p>This guarantees ample breathing room for technical indicator overlays, price callout pill badges, and horizontal gridlines.</p>

          <h3>Temporal Axis Discretization: Trading Session Calendar vs. Continuous Time</h3>
          <p>A critical architectural decision when designing financial charting engines is handling non-trading periods. Unlike sensor networks or IoT metrics that generate telemetry continuously 24/7/365, equity markets operate on rigid trading calendars: the New York Stock Exchange is open weekdays from 9:30 AM to 4:00 PM EST, closing entirely on weekends and Federal holidays.</p>

          <p>If an engine projects candle positions along a continuous linear chronological timestamp axis, massive empty voids appear on the chart corresponding to weekend closures and overnight gaps. These empty chasms distort technical indicator calculations and waste valuable horizontal screen space. Professional charting engines therefore map candlestick bars to <strong>ordinal discrete slot indices</strong>: candle i is mapped to <code>x = paddingLeft + slotWidth * (i + 0.5)</code> regardless of the chronological time delta between candle i and candle i - 1. A companion time lookup table translates slot indices to formatted dates on the X-axis, ensuring an unbroken, continuous visual progression across market sessions.</p>
        </section>'''

assert sec3_target in code, "sec3_target not found"
code = code.replace(sec3_target, sec3_replacement)

# 4. Expand Section 5
sec5_target = r'''          <p>To render these indicators in SVG, the engine evaluates the rolling values across the dataset, maps each valid point to <code>(cx, scaleY(MA_val))</code>, and concatenates them into a continuous SVG path: <code>&lt;path d="M x0 y0 L x1 y1 ..." fill="none" stroke="#F59E0B" stroke-width="2" /&gt;</code>. Applying a subtle drop-shadow or outer glow filter highlights the trend lines above dense background candlestick clusters.</p>
        </section>'''

sec5_replacement = r'''          <p>To render these indicators in SVG, the engine evaluates the rolling values across the dataset, maps each valid point to <code>(cx, scaleY(MA_val))</code>, and concatenates them into a continuous SVG path: <code>&lt;path d="M x0 y0 L x1 y1 ..." fill="none" stroke="#F59E0B" stroke-width="2" /&gt;</code>. Applying a subtle drop-shadow or outer glow filter highlights the trend lines above dense background candlestick clusters.</p>

          <h3>Multi-Band Indicator Architecture: Bollinger Bands &amp; VWAP</h3>
          <p>Beyond single-line moving averages, advanced algorithmic trading dashboards visualize statistical dispersion bands:</p>

          <div class="formula-card">
            <div class="formula-title">Volume Weighted Average Price (VWAP) Formulation</div>
            <div class="formula-body">
              VWAP_t = &sum;_{i=1}^{t} (TypicalPrice_i * Volume_i) / &sum;_{i=1}^{t} Volume_i<br>
              where TypicalPrice_i = (High_i + Low_i + Close_i) / 3
            </div>
            <div class="formula-desc">
              Computes cumulative volume-weighted benchmark price from session opening bell, representing institutional transaction equilibrium.
            </div>
          </div>

          <p><strong>Bollinger Bands</strong>, developed by John Bollinger in the 1980s, overlay an envelope of volatility surrounding an SMA baseline: <code>Upper = SMA + 2 * &sigma;</code> and <code>Lower = SMA - 2 * &sigma;</code>, where &sigma; is the rolling standard deviation. In SVG vector graphics, Bollinger Bands can be rendered not merely as two disconnected lines, but as a continuous semi-transparent shaded ribbon. The vector path starts along the upper band from left to right, connects down to the rightmost lower band coordinate, traces backward along the lower band from right to left, and closes with <code>Z</code>: <code>fill="rgba(56, 189, 248, 0.08)" stroke="#38BDF8" stroke-width="1"</code>. This shaded channel provides immediate visual awareness of volatility squeezes and range expansions.</p>
        </section>'''

assert sec5_target in code, "sec5_target not found"
code = code.replace(sec5_target, sec5_replacement)

# 5. Expand Section 6
sec6_target = r'''          <p>The volume bars share identical horizontal X coordinates with the corresponding price candles. Each bar's height is scaled linearly from zero to the maximum volume observed within the window: <code>barHeight = (Volume / maxVolume) * volumePanelHeight</code>. Crucially, each volume bar adopts the color of its companion candlestick: green for bullish accumulation bars and red for bearish distribution bars, creating immediate visual synergy between volume and price momentum.</p>
        </section>'''

sec6_replacement = r'''          <p>The volume bars share identical horizontal X coordinates with the corresponding price candles. Each bar's height is scaled linearly from zero to the maximum volume observed within the window: <code>barHeight = (Volume / maxVolume) * volumePanelHeight</code>. Crucially, each volume bar adopts the color of its companion candlestick: green for bullish accumulation bars and red for bearish distribution bars, creating immediate visual synergy between volume and price momentum.</p>

          <h3>Horizontal Volume Profile: High-Volume Nodes &amp; Liquidity Voids</h3>
          <p>While standard bottom volume histograms depict volume through time (volume-by-time), quantitative market makers increasingly rely on <strong>Volume Profile</strong> (volume-by-price). A volume profile partitions the vertical price range into discrete horizontal price bins, accumulating total traded volume executed at each specific price level regardless of when the transactions occurred.</p>

          <p>In SVG rendering, volume profile is visualized as horizontal bars protruding from the left or right margin into the price canvas: <code>&lt;rect x="pad.left" y="scaleY(bin_price)" width="bin_volume_width" height="bin_height" fill="rgba(255,255,255,0.06)" /&gt;</code>. Zones of dense horizontal bars—known as <strong>High-Volume Nodes (HVN)</strong>—represent areas of institutional fair-value consensus where assets spend significant time consolidating. Conversely, hollow gaps with minimal horizontal bar width represent <strong>Low-Volume Nodes (LVN)</strong> or liquidity voids, indicating price levels where the market moved so rapidly that minimal liquidity was exchanged, often serving as high-velocity slip zones during subsequent retests.</p>
        </section>'''

assert sec6_target in code, "sec6_target not found"
code = code.replace(sec6_target, sec6_replacement)

with open(r"D:\Project IconStash\IconStash\scripts\gen_nov21_article3.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Expanded gen_nov21_article3.py successfully.")
