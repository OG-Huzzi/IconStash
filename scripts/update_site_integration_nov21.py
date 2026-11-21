import re
import os

forbidden = ['jv16', 'winfindr', 'uninstalr']

# 1. Update articles/index.html
with open('articles/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Update guide count 129 -> 132
assert '<span class="count">129 guides</span>' in idx_content, "Expected 129 guides in articles/index.html"
idx_content = idx_content.replace('<span class="count">129 guides</span>', '<span class="count">132 guides</span>')

# Prepend cards in the Guides & Tutorials section
target_grid_marker = '<div class="section-head"><h2>Guides &amp; Tutorials</h2><span class="count">132 guides</span></div>\n  <div class="grid">'
new_cards = '''    <a class="card" href="/articles/svg-sunburst-charts-and-radial-treemap-hierarchy-guide/">
      <span class="tag">Hierarchical Data Visualization</span>
      <h3>Mastering SVG Sunburst Charts: Radial Treemap Hierarchies, Arc Calculus &amp; Zoomable Partitions (2026)</h3>
      <p>Master multi-level radial treemap hierarchies, polar-to-Cartesian arc projection, large-arc-flag calculus, zoomable root navigation, and accessible tree structures.</p>
    </a>
    <a class="card" href="/articles/svg-violin-plots-and-kernel-density-distribution-guide/">
      <span class="tag">Statistical Data Visualization</span>
      <h3>Mastering SVG Violin Plots: Kernel Density Estimation, Spline Calculus &amp; Multimodal Distributions (2026)</h3>
      <p>Master Gaussian kernel density estimation, Silverman bandwidth calculus, mirrored cubic Bézier splines, embedded quartile boxes, and asymmetric split cohorts.</p>
    </a>
    <a class="card" href="/articles/svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide/">
      <span class="tag">Financial Data Visualization</span>
      <h3>Mastering SVG Candlestick Charts: Financial OHLC Data, Moving Averages &amp; Time-Series Vector Graphics (2026)</h3>
      <p>Master financial OHLC candlestick geometry, crispEdges pixel snapping, moving averages (SMA/EMA), volume histograms, and interactive HUD crosshair tracking.</p>
    </a>
'''

assert '<div class="section-head"><h2>Guides &amp; Tutorials</h2><span class="count">132 guides</span></div>\n  <div class="grid">' in idx_content, "Target grid marker not found in articles/index.html"
idx_content = idx_content.replace(target_grid_marker, target_grid_marker + '\n' + new_cards)

# Add schema ItemList entries for 181, 182, 183
schema_target = '{ "@type": "ListItem", "position": 180, "url": "https://iconstash.io/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/", "name": "Mastering SVG Parallel Coordinates: High-Dimensional Geometry, Axis Normalization & Dynamic Range Brushing (2026)" }'
new_schema_items = ''',
      { "@type": "ListItem", "position": 181, "url": "https://iconstash.io/articles/svg-sunburst-charts-and-radial-treemap-hierarchy-guide/", "name": "Mastering SVG Sunburst Charts: Radial Treemap Hierarchies, Arc Calculus & Zoomable Partitions (2026)" },
      { "@type": "ListItem", "position": 182, "url": "https://iconstash.io/articles/svg-violin-plots-and-kernel-density-distribution-guide/", "name": "Mastering SVG Violin Plots: Kernel Density Estimation, Spline Calculus & Multimodal Distributions (2026)" },
      { "@type": "ListItem", "position": 183, "url": "https://iconstash.io/articles/svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide/", "name": "Mastering SVG Candlestick Charts: Financial OHLC Data, Moving Averages & Time-Series Vector Graphics (2026)" }'''

assert schema_target in idx_content, "Schema target position 180 not found in articles/index.html"
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
assert '<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-20</lastmod>' in sitemap_content, "Hub lastmod not found in articles-sitemap.xml"
sitemap_content = sitemap_content.replace('<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-20</lastmod>', '<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-21</lastmod>')

new_sitemap_urls = '''  <url>
    <loc>https://iconstash.io/articles/svg-sunburst-charts-and-radial-treemap-hierarchy-guide/</loc>
    <lastmod>2026-11-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/svg-violin-plots-and-kernel-density-distribution-guide/</loc>
    <lastmod>2026-11-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide/</loc>
    <lastmod>2026-11-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>'''

assert '</urlset>' in sitemap_content, "</urlset> not found in articles-sitemap.xml"
sitemap_content = sitemap_content.replace('</urlset>', new_sitemap_urls)

for word in forbidden:
    assert word not in sitemap_content.lower(), f"Forbidden brand '{word}' detected in articles-sitemap.xml"

with open('articles-sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Updated articles-sitemap.xml successfully.")


# 3. Update sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    parent_sitemap = f.read()

assert '<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-20</lastmod></sitemap>' in parent_sitemap, "articles-sitemap.xml entry not found in sitemap.xml"
parent_sitemap = parent_sitemap.replace('<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-20</lastmod></sitemap>', '<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-21</lastmod></sitemap>')

for word in forbidden:
    assert word not in parent_sitemap.lower(), f"Forbidden brand '{word}' detected in sitemap.xml"

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(parent_sitemap)
print("Updated sitemap.xml successfully.")


# 4. Update llms.txt
with open('llms.txt', 'r', encoding='utf-8') as f:
    llms_content = f.read()

assert '- Last updated: 2026-11-20' in llms_content, "Header lastmod not found in llms.txt"
llms_content = llms_content.replace('- Last updated: 2026-11-20', '- Last updated: 2026-11-21')

assert 'Last updated: 2026-11-20' in llms_content, "Footer lastmod not found in llms.txt"
llms_content = llms_content.replace('Last updated: 2026-11-20', 'Last updated: 2026-11-21')

guide_target = '- [Mastering SVG Parallel Coordinates: High-Dimensional Geometry, Axis Normalization & Dynamic Range Brushing (2026)](https://iconstash.io/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/)'
new_llms_guides = '''- [Mastering SVG Parallel Coordinates: High-Dimensional Geometry, Axis Normalization & Dynamic Range Brushing (2026)](https://iconstash.io/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/)
- [Mastering SVG Sunburst Charts: Radial Treemap Hierarchies, Arc Calculus & Zoomable Partitions (2026)](https://iconstash.io/articles/svg-sunburst-charts-and-radial-treemap-hierarchy-guide/)
- [Mastering SVG Violin Plots: Kernel Density Estimation, Spline Calculus & Multimodal Distributions (2026)](https://iconstash.io/articles/svg-violin-plots-and-kernel-density-distribution-guide/)
- [Mastering SVG Candlestick Charts: Financial OHLC Data, Moving Averages & Time-Series Vector Graphics (2026)](https://iconstash.io/articles/svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide/)'''

assert guide_target in llms_content, "Parallel coordinates guide not found in llms.txt"
llms_content = llms_content.replace(guide_target, new_llms_guides)

for word in forbidden:
    assert word not in llms_content.lower(), f"Forbidden brand '{word}' detected in llms.txt"

with open('llms.txt', 'w', encoding='utf-8') as f:
    f.write(llms_content)
print("Updated llms.txt successfully.")
