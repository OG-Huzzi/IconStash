import re

forbidden = ['jv16', 'winfindr', 'uninstalr']

# 1. Update articles/index.html
with open('articles/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Update guide count 123 -> 126
assert '<span class="count">123 guides</span>' in idx_content
idx_content = idx_content.replace('<span class="count">123 guides</span>', '<span class="count">126 guides</span>')

# Prepend cards in the Guides & Tutorials section
target_grid_marker = '<div class="section-head"><h2>Guides &amp; Tutorials</h2><span class="count">126 guides</span></div>\n  <div class="grid">'
new_cards = '''    <a class="card" href="/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide/">
      <span class="tag">Multivariate Visualizations</span>
      <h3>Mastering SVG Scatter Plots &amp; Bubble Charts: Continuous Coordinates, Radius Scaling &amp; Interactive Physics (2026)</h3>
      <p>Master continuous Cartesian mapping, perceptual square-root radius scaling, Ordinary Least Squares (OLS) regression trendlines, and O(log N) quadtree hit-testing.</p>
    </a>
    <a class="card" href="/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide/">
      <span class="tag">Graph Topology &amp; Physics</span>
      <h3>Mastering SVG Network Graphs &amp; Force-Directed Layouts: Physics Simulation, Node-Link Geometry &amp; Drag Guide (2026)</h3>
      <p>Master Coulomb electrostatic repulsion, Hooke spring tension, Barnes-Hut quadtree acceleration, curved quadratic Bézier links, and kinematic drag pinning.</p>
    </a>
    <a class="card" href="/articles/svg-choropleth-maps-and-geographic-vector-visualization-guide/">
      <span class="tag">Geospatial Vector Graphics</span>
      <h3>Mastering SVG Choropleth Maps: GeoJSON Projections, Color Quantization &amp; Vector GIS Guide (2026)</h3>
      <p>Master forward spherical-to-planar projections, Albers equal-area conic mapping, multi-ring GeoJSON parsing, quantile color classification, and viewBox auto-centering.</p>
    </a>
'''

# Note: target_grid_marker was updated with 126 guides above
assert target_grid_marker in idx_content
idx_content = idx_content.replace(target_grid_marker, target_grid_marker + '\n' + new_cards)

# Add schema ItemList entries for 175, 176, 177
schema_target = '{ "@type": "ListItem", "position": 174, "url": "https://iconstash.io/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/", "name": "Mastering SVG Sparklines & Micro-Charts: Inline Trendlines, Area Gradients & Dashboard Metrics Guide (2026)" }'
new_schema_items = ''',
      { "@type": "ListItem", "position": 175, "url": "https://iconstash.io/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide/", "name": "Mastering SVG Scatter Plots & Bubble Charts: Multivariate Coordinates, Radius Scaling & Interactive Hover Guide (2026)" },
      { "@type": "ListItem", "position": 176, "url": "https://iconstash.io/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide/", "name": "Mastering SVG Network Graphs & Force-Directed Layouts: Physics Simulation, Node-Link Geometry & Drag Guide (2026)" },
      { "@type": "ListItem", "position": 177, "url": "https://iconstash.io/articles/svg-choropleth-maps-and-geographic-vector-visualization-guide/", "name": "Mastering SVG Choropleth Maps: GeoJSON Projections, Color Quantization & Vector GIS Guide (2026)" }'''

assert schema_target in idx_content
idx_content = idx_content.replace(schema_target, schema_target + new_schema_items)

for word in forbidden:
    assert word not in idx_content.lower(), f"Forbidden brand '{word}' detected in articles/index.html"

with open('articles/index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("Updated articles/index.html successfully.")


# 2. Update articles-sitemap.xml
with open('articles-sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

# Update articles hub lastmod
assert '<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-17</lastmod>' in sitemap_content
sitemap_content = sitemap_content.replace('<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-17</lastmod>', '<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-18</lastmod>')

new_sitemap_urls = '''  <url>
    <loc>https://iconstash.io/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide/</loc>
    <lastmod>2026-11-18</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide/</loc>
    <lastmod>2026-11-18</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/svg-choropleth-maps-and-geographic-vector-visualization-guide/</loc>
    <lastmod>2026-11-18</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>'''

assert '</urlset>' in sitemap_content
sitemap_content = sitemap_content.replace('</urlset>', new_sitemap_urls)

for word in forbidden:
    assert word not in sitemap_content.lower(), f"Forbidden brand '{word}' detected in articles-sitemap.xml"

with open('articles-sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Updated articles-sitemap.xml successfully.")


# 3. Update sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    parent_sitemap = f.read()

assert '<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-17</lastmod></sitemap>' in parent_sitemap
parent_sitemap = parent_sitemap.replace('<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-17</lastmod></sitemap>', '<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-18</lastmod></sitemap>')

for word in forbidden:
    assert word not in parent_sitemap.lower(), f"Forbidden brand '{word}' detected in sitemap.xml"

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(parent_sitemap)
print("Updated sitemap.xml successfully.")


# 4. Update llms.txt
with open('llms.txt', 'r', encoding='utf-8') as f:
    llms_content = f.read()

assert '- Last updated: 2026-11-17' in llms_content
llms_content = llms_content.replace('- Last updated: 2026-11-17', '- Last updated: 2026-11-18')

assert 'Last updated: 2026-11-17' in llms_content
llms_content = llms_content.replace('Last updated: 2026-11-17', 'Last updated: 2026-11-18')

guide_target = '- [Mastering SVG Sparklines & Micro-Charts: Inline Trendlines, Area Gradients & Dashboard Metrics Guide (2026)](https://iconstash.io/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/)'
new_llms_guides = '''- [Mastering SVG Sparklines & Micro-Charts: Inline Trendlines, Area Gradients & Dashboard Metrics Guide (2026)](https://iconstash.io/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/)
- [Mastering SVG Scatter Plots & Bubble Charts: Multivariate Coordinates, Radius Scaling & Interactive Hover Guide (2026)](https://iconstash.io/articles/svg-scatter-plots-and-bubble-charts-multivariate-visualization-guide/)
- [Mastering SVG Network Graphs & Force-Directed Layouts: Physics Simulation, Node-Link Geometry & Drag Guide (2026)](https://iconstash.io/articles/svg-network-graphs-and-force-directed-node-link-visualization-guide/)
- [Mastering SVG Choropleth Maps: GeoJSON Projections, Color Quantization & Vector GIS Guide (2026)](https://iconstash.io/articles/svg-choropleth-maps-and-geographic-vector-visualization-guide/)'''

assert guide_target in llms_content
llms_content = llms_content.replace(guide_target, new_llms_guides)

for word in forbidden:
    assert word not in llms_content.lower(), f"Forbidden brand '{word}' detected in llms.txt"

with open('llms.txt', 'w', encoding='utf-8') as f:
    f.write(llms_content)
print("Updated llms.txt successfully.")
