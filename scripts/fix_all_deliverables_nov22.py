import re

def fix_article(path, is_article2=False):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Header CTA & links
    old_header_links = '''    <nav>
      <a href="/articles/">Articles</a>
      <a href="/Glossary/icon-svg-terminology/">Glossary</a>
      <a href="/about/">About</a>
      <button class="theme-toggle-btn" id="theme-toggle" aria-label="Toggle Theme">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="2" x2="12" y2="6"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
      </button>
      <a href="/#/" class="header-cta">Browse Library</a>
    </nav>'''

    new_header_links = '''    <nav>
      <a href="/articles/">Articles</a>
      <a href="/about/">About</a>
      <a href="/stats/">Stats</a>
      <button class="theme-toggle-btn" id="theme-toggle" aria-label="Toggle Theme">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="2" x2="12" y2="6"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
      </button>
      <a href="/articles/" class="header-cta">Browse 135 Guides</a>
    </nav>'''
    content = content.replace(old_header_links, new_header_links)

    # 2. Sidebar CTA: replace /tools/
    old_sidebar_cta = '''        <div class="cta-sidebar-box">
          <h4 class="cta-title">Explore 28 SVG Icon Sets</h4>
          <p>Supercharge your data visualizations and dashboards with IconStash's unified, accessible vector icons.</p>
          <a href="/tools/" class="header-cta" style="display:inline-block; text-align:center;">Open Icon Explorer</a>
        </div>'''

    new_sidebar_cta = '''        <div class="sidebar-card cta-sidebar-box">
          <div class="cta-title">Explore Related Guides</div>
          <p>Expand your data visualization capabilities with our companion technical engineering deep dives:</p>
          <div style="display:flex; flex-direction:column; gap:8px; font-size:13px;">
            <a href="/articles/svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide/">SVG Candlestick Charts</a>
            <a href="/articles/svg-sunburst-charts-and-radial-treemap-hierarchy-guide/">SVG Sunburst Charts</a>
            <a href="/articles/svg-sankey-diagrams-and-alluvial-flow-guide/">SVG Sankey Diagrams</a>
          </div>
        </div>'''
    content = content.replace(old_sidebar_cta, new_sidebar_cta)

    # 3. Footer links: replace /tools/
    old_footer_links = '''      <div style="display:flex; gap:20px;">
        <a href="/articles/">Articles</a>
        <a href="/tools/">Icon Libraries</a>
        <a href="/about/">About &amp; Author</a>
        <a href="/privacy/">Privacy Policy</a>
      </div>'''

    new_footer_links = '''      <div style="display:flex; gap:20px;">
        <a href="/about/">About &amp; Author</a>
        <a href="/articles/">All Visualization Guides</a>
        <a href="/stats/">Statistics</a>
        <a href="/privacy/">Privacy Policy</a>
      </div>'''
    content = content.replace(old_footer_links, new_footer_links)

    # 4. If Article 2, fix meta description length
    if is_article2:
        old_desc2 = "Master SVG chord diagrams: square bilateral flow matrices, radial arc trigonometry, quadratic Bézier ribbon calculus, and interactive multi-entity routing."
        new_desc2 = "Master SVG chord diagrams: bilateral flow matrices, radial arc layout, quadratic Bézier ribbons, and accessible multi-entity interactive routing."
        assert len(new_desc2) <= 155
        content = content.replace(old_desc2, new_desc2)

    # 5. Fix XML entities in inline SVGs (no undefined entities like &Delta;, &times;, &deg;)
    def replace_svg_entities(match):
        svg_text = match.group(0)
        svg_text = svg_text.replace("&Delta;", "&#916;")
        svg_text = svg_text.replace("&times;", "&#215;")
        svg_text = svg_text.replace("&deg;", "&#176;")
        svg_text = svg_text.replace("&plusmn;", "&#177;")
        svg_text = svg_text.replace("&le;", "&#8804;")
        svg_text = svg_text.replace("&ge;", "&#8805;")
        svg_text = svg_text.replace("&sum;", "&#8721;")
        svg_text = svg_text.replace("&minus;", "&#8722;")
        return svg_text

    # Replace within all <svg> tags outside scripts
    # Find script blocks and preserve them while replacing in HTML/SVG
    parts = re.split(r'(<script[\s\S]*?<\/script>)', content)
    for i in range(len(parts)):
        if not parts[i].startswith('<script'):
            parts[i] = re.sub(r'<svg[\s\S]*?<\/svg>', replace_svg_entities, parts[i])
    content = ''.join(parts)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {path}")

if __name__ == "__main__":
    fix_article("articles/svg-waterfall-charts-and-financial-variance-bridge-guide/index.html")
    fix_article("articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/index.html", is_article2=True)
    fix_article("articles/svg-ternary-plots-and-triangular-composition-diagram-guide/index.html")
