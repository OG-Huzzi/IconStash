def update_articles_index():
    path = "articles/index.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update count: 135 guides -> 138 guides
    assert '<span class="count">135 guides</span>' in content, "Guide count 135 not found"
    content = content.replace('<span class="count">135 guides</span>', '<span class="count">138 guides</span>')

    # 2. Append to ItemList schema: positions 187, 188, 189
    ternary_item = '{ "@type": "ListItem", "position": 186, "url": "https://iconstash.io/articles/svg-ternary-plots-and-triangular-composition-diagram-guide/", "name": "Mastering SVG Ternary Plots & Triangular Composition Diagrams: Barycentric Coordinates, Equilateral Grid Math & Phase Triangles (2026)" }'
    assert ternary_item in content, "Ternary item 186 not found in schema"

    new_schema_items = ternary_item + """,
      { "@type": "ListItem", "position": 187, "url": "https://iconstash.io/articles/svg-line-charts-and-multi-series-time-series-guide/", "name": "Mastering SVG Line Charts & Multi-Series Time-Series Graphs: Monotone Cubic Splines, Bisector Crosshairs & Axis Scaling (2026)" },
      { "@type": "ListItem", "position": 188, "url": "https://iconstash.io/articles/svg-blob-generator-and-organic-shapes-guide/", "name": "SVG Blob Generator & Organic Shapes: Catmull-Rom Splines, Seeded PRNG & CSS clip-path Morphing (2026)" },
      { "@type": "ListItem", "position": 189, "url": "https://iconstash.io/articles/shadcn-ui-icons-complete-guide-2026/", "name": "Shadcn UI Icons Complete Guide (2026): Lucide vs. Phosphor vs. Hugeicons vs. Tabler & CLI Migration" }"""

    content = content.replace(ternary_item, new_schema_items)

    # 3. Prepend 3 cards to Guides & Tutorials grid
    target_grid = '<div class="section-head"><h2>Guides &amp; Tutorials</h2><span class="count">138 guides</span></div>\n  <div class="grid">'
    if target_grid not in content:
        target_grid = '<div class="section-head"><h2>Guides &amp; Tutorials</h2><span class="count">138 guides</span></div>\r\n  <div class="grid">'
    assert target_grid in content, "Guides & Tutorials grid target not found"

    new_cards = target_grid + """
    <a class="card" href="/articles/svg-line-charts-and-multi-series-time-series-guide/">
      <span class="tag">Data Visualization</span>
      <h3>Mastering SVG Line Charts &amp; Multi-Series Time-Series Graphs: Monotone Cubic Splines, Bisector Crosshairs &amp; Axis Scaling (2026)</h3>
      <p>Build zero-dependency SVG line charts with Fritsch-Carlson monotone cubic splines, Heckbert nice-number axis ticks, O(log n) crosshair bisectors, and WCAG 2.2 AA accessibility.</p>
    </a>
    <a class="card" href="/articles/svg-blob-generator-and-organic-shapes-guide/">
      <span class="tag">Vector Graphics Engineering</span>
      <h3>SVG Blob Generator &amp; Organic Shapes: Catmull-Rom Splines, Seeded PRNG &amp; CSS clip-path Morphing (2026)</h3>
      <p>Generate deterministic organic SVG blobs with Mulberry32 PRNG seeds, cyclic Catmull-Rom cubic B&eacute;zier splines, responsive objectBoundingBox CSS masks, and smooth morphing.</p>
    </a>
    <a class="card" href="/articles/shadcn-ui-icons-complete-guide-2026/">
      <span class="tag">UI Engineering &amp; Icon Systems</span>
      <h3>Shadcn UI Icons Complete Guide (2026): Lucide vs. Phosphor vs. Hugeicons vs. Tabler &amp; CLI Migration</h3>
      <p>Compare Lucide, Phosphor, Hugeicons, Tabler, and Remix Icon in shadcn/ui, run npx shadcn migrate icons, configure Tailwind v4 sizing, and optimize Next.js tree-shaking.</p>
    </a>"""

    content = content.replace(target_grid, new_cards, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("articles/index.html successfully updated.")

def update_articles_sitemap():
    path = "articles-sitemap.xml"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    hub_target = "<url><loc>https://iconstash.io/articles/</loc><lastmod>2026-11-22</lastmod></url>"
    hub_replace = "<url><loc>https://iconstash.io/articles/</loc><lastmod>2026-11-25</lastmod></url>"
    assert hub_target in content, "Hub URL not found in articles-sitemap.xml"
    content = content.replace(hub_target, hub_replace)

    new_urls = """  <url>
    <loc>https://iconstash.io/articles/svg-line-charts-and-multi-series-time-series-guide/</loc>
    <lastmod>2026-11-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/svg-blob-generator-and-organic-shapes-guide/</loc>
    <lastmod>2026-11-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/shadcn-ui-icons-complete-guide-2026/</loc>
    <lastmod>2026-11-25</lastmod>
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

    target = "<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-22</lastmod></sitemap>"
    replace = "<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-25</lastmod></sitemap>"
    assert target in content, "articles-sitemap entry not found in sitemap.xml"
    content = content.replace(target, replace)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("sitemap.xml successfully updated.")

def update_llms():
    path = "llms.txt"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace("- Last updated: 2026-11-22", "- Last updated: 2026-11-25")
    content = content.replace("Last updated: 2026-11-22", "Last updated: 2026-11-25")

    ternary_link = "- [Mastering SVG Ternary Plots & Triangular Composition Diagrams: Barycentric Coordinates, Equilateral Grid Math & Phase Triangles (2026)](https://iconstash.io/articles/svg-ternary-plots-and-triangular-composition-diagram-guide/)"
    assert ternary_link in content, "Ternary link not found in llms.txt"

    new_links = ternary_link + """
- [Mastering SVG Line Charts & Multi-Series Time-Series Graphs: Monotone Cubic Splines, Bisector Crosshairs & Axis Scaling (2026)](https://iconstash.io/articles/svg-line-charts-and-multi-series-time-series-guide/)
- [SVG Blob Generator & Organic Shapes: Catmull-Rom Splines, Seeded PRNG & CSS clip-path Morphing (2026)](https://iconstash.io/articles/svg-blob-generator-and-organic-shapes-guide/)
- [Shadcn UI Icons Complete Guide (2026): Lucide vs. Phosphor vs. Hugeicons vs. Tabler & CLI Migration](https://iconstash.io/articles/shadcn-ui-icons-complete-guide-2026/)"""

    content = content.replace(ternary_link, new_links)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("llms.txt successfully updated.")

if __name__ == "__main__":
    update_articles_index()
    update_articles_sitemap()
    update_sitemap()
    update_llms()
