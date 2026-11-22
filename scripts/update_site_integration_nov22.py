import re

def update_articles_index():
    path = "articles/index.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update count: 132 guides -> 135 guides
    assert '<span class="count">132 guides</span>' in content, "Guide count 132 not found"
    content = content.replace('<span class="count">132 guides</span>', '<span class="count">135 guides</span>')

    # 2. Append to ItemList schema: positions 184, 185, 186
    candlestick_item = '{ "@type": "ListItem", "position": 183, "url": "https://iconstash.io/articles/svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide/", "name": "Mastering SVG Candlestick Charts: Financial OHLC Data, Moving Averages & Time-Series Vector Graphics (2026)" }'
    assert candlestick_item in content, "Candlestick item not found in schema"

    new_schema_items = candlestick_item + """,
      { "@type": "ListItem", "position": 184, "url": "https://iconstash.io/articles/svg-waterfall-charts-and-financial-variance-bridge-guide/", "name": "Mastering SVG Waterfall Charts & Financial Variance Bridges: Running Totals, Floating Rectangles & Bridge Geometry (2026)" },
      { "@type": "ListItem", "position": 185, "url": "https://iconstash.io/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/", "name": "Mastering SVG Chord Diagrams & Bilateral Flow Matrices: Radial Arcs, Quadratic Ribbons & Circular Geometries (2026)" },
      { "@type": "ListItem", "position": 186, "url": "https://iconstash.io/articles/svg-ternary-plots-and-triangular-composition-diagram-guide/", "name": "Mastering SVG Ternary Plots & Triangular Composition Diagrams: Barycentric Coordinates, Equilateral Grid Math & Phase Triangles (2026)" }"""

    content = content.replace(candlestick_item, new_schema_items)

    # 3. Prepend 3 cards to Guides & Tutorials grid
    target_grid = '<div class="section-head"><h2>Guides &amp; Tutorials</h2><span class="count">135 guides</span></div>\n  <div class="grid">'
    assert target_grid in content, "Guides & Tutorials grid target not found"

    new_cards = target_grid + """
    <a class="card" href="/articles/svg-waterfall-charts-and-financial-variance-bridge-guide/">
      <span class="tag">Financial Data Visualization</span>
      <h3>Mastering SVG Waterfall Charts &amp; Financial Variance Bridges: Running Totals, Floating Rectangles &amp; Bridge Geometry (2026)</h3>
      <p>Master running balance accumulators, floating delta coordinates, dashed connector bridges, subtotal breakdown columns, and high-performance financial vector graphics.</p>
    </a>
    <a class="card" href="/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/">
      <span class="tag">Relational Flow Visualization</span>
      <h3>Mastering SVG Chord Diagrams &amp; Bilateral Flow Matrices: Radial Arcs, Quadratic Ribbons &amp; Circular Geometries (2026)</h3>
      <p>Master square bilateral adjacency matrices, radial arc layout math, quadratic Bézier ribbon calculus, directional flow chords, and high-performance interactive routing.</p>
    </a>
    <a class="card" href="/articles/svg-ternary-plots-and-triangular-composition-diagram-guide/">
      <span class="tag">Compositional Data Visualization</span>
      <h3>Mastering SVG Ternary Plots &amp; Triangular Composition Diagrams: Barycentric Coordinates, Equilateral Grid Math &amp; Phase Triangles (2026)</h3>
      <p>Master ternary compositional data normalization, equilateral Cartesian projection math, tri-axial grid generation, inverse barycentric cursor hit-testing, and phase diagrams.</p>
    </a>"""

    content = content.replace(target_grid, new_cards, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("articles/index.html successfully updated.")

def update_articles_sitemap():
    path = "articles-sitemap.xml"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update hub lastmod
    hub_target = "<url><loc>https://iconstash.io/articles/</loc><lastmod>2026-11-21</lastmod></url>"
    hub_replace = "<url><loc>https://iconstash.io/articles/</loc><lastmod>2026-11-22</lastmod></url>"
    assert hub_target in content, "Hub URL not found in articles-sitemap.xml"
    content = content.replace(hub_target, hub_replace)

    # Append 3 new URLs before </urlset>
    new_urls = """  <url>
    <loc>https://iconstash.io/articles/svg-waterfall-charts-and-financial-variance-bridge-guide/</loc>
    <lastmod>2026-11-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/</loc>
    <lastmod>2026-11-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/svg-ternary-plots-and-triangular-composition-diagram-guide/</loc>
    <lastmod>2026-11-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""

    assert "</urlset>" in content, "</urlset> tag not found"
    content = content.replace("</urlset>", new_urls)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("articles-sitemap.xml successfully updated.")

def update_sitemap():
    path = "sitemap.xml"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    target = "<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-21</lastmod></sitemap>"
    replace = "<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-22</lastmod></sitemap>"
    assert target in content, "articles-sitemap entry not found in sitemap.xml"
    content = content.replace(target, replace)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("sitemap.xml successfully updated.")

def update_llms():
    path = "llms.txt"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update top last updated
    content = content.replace("- Last updated: 2026-11-21", "- Last updated: 2026-11-22")

    # Update bottom last updated
    content = content.replace("Last updated: 2026-11-21", "Last updated: 2026-11-22")

    # Add 3 new links after candlestick
    candlestick_link = "- [Mastering SVG Candlestick Charts: Financial OHLC Data, Moving Averages & Time-Series Vector Graphics (2026)](https://iconstash.io/articles/svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide/)"
    assert candlestick_link in content, "Candlestick link not found in llms.txt"

    new_links = candlestick_link + """
- [Mastering SVG Waterfall Charts & Financial Variance Bridges: Running Totals, Floating Rectangles & Bridge Geometry (2026)](https://iconstash.io/articles/svg-waterfall-charts-and-financial-variance-bridge-guide/)
- [Mastering SVG Chord Diagrams & Bilateral Flow Matrices: Radial Arcs, Quadratic Ribbons & Circular Geometries (2026)](https://iconstash.io/articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/)
- [Mastering SVG Ternary Plots & Triangular Composition Diagrams: Barycentric Coordinates, Equilateral Grid Math & Phase Triangles (2026)](https://iconstash.io/articles/svg-ternary-plots-and-triangular-composition-diagram-guide/)"""

    content = content.replace(candlestick_link, new_links)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("llms.txt successfully updated.")

if __name__ == "__main__":
    update_articles_index()
    update_articles_sitemap()
    update_sitemap()
    update_llms()
