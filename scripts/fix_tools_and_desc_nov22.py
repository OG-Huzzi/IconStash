import re

articles = [
    "articles/svg-waterfall-charts-and-financial-variance-bridge-guide/index.html",
    "articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/index.html",
    "articles/svg-ternary-plots-and-triangular-composition-diagram-guide/index.html"
]

for path in articles:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Header Tools link
    content = content.replace('<a href="/tools/">Tools</a>', '<a href="/stats/">Stats</a>')
    content = content.replace('<a href="/tools/" class="header-cta">Studio Tools</a>', '<a href="/articles/" class="header-cta">Browse 135 Guides</a>')

    # 2. Sidebar Open Icon Explorer link
    content = content.replace(
        '<a href="/tools/" class="header-cta" style="display:inline-block; text-align:center;">Open Icon Explorer</a>',
        '<a href="/articles/" class="header-cta" style="display:inline-block; text-align:center;">Explore All Guides</a>'
    )
    # Also in case there's any other /tools/ in sidebar
    content = content.replace('href="/tools/"', 'href="/articles/"')

    # 3. Footer Developer Studio link
    content = content.replace('<a href="/tools/">Developer Studio</a>', '<a href="/stats/">Platform Statistics</a>')

    # 4. In Chord article, fix description length <= 155
    if "svg-chord-diagrams" in path:
        desc_old = 'Master SVG chord diagrams: bilateral flow matrices, circular ribbon arcs, quadratic &amp; cubic Bézier curves, self-linking chords, and accessible rendering.'
        desc_new = 'Master SVG chord diagrams: bilateral flow matrices, circular ribbon arcs, quadratic and cubic Bézier curves, self-linking chords, and accessible rendering.'
        content = content.replace(desc_old, desc_new)

        # In JSON-LD, description might have unescaped &
        json_desc_old = 'Master SVG chord diagrams: bilateral flow matrices, circular ribbon arcs, quadratic & cubic Bézier curves, self-linking chords, and accessible rendering.'
        json_desc_new = 'Master SVG chord diagrams: bilateral flow matrices, circular ribbon arcs, quadratic and cubic Bézier curves, self-linking chords, and accessible rendering.'
        content = content.replace(json_desc_old, json_desc_new)

    # Any remaining /tools/
    content = re.sub(r'href="/tools/?"', 'href="/articles/"', content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {path}")
