import re
import os

forbidden = ['jv16', 'winfindr', 'uninstalr']

# 1. Update articles/index.html
with open('articles/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Update guide count 126 -> 129
assert '<span class="count">126 guides</span>' in idx_content, "Expected 126 guides in articles/index.html"
idx_content = idx_content.replace('<span class="count">126 guides</span>', '<span class="count">129 guides</span>')

# Prepend cards in the Guides & Tutorials section
target_grid_marker = '<div class="section-head"><h2>Guides &amp; Tutorials</h2><span class="count">129 guides</span></div>\n  <div class="grid">'
new_cards = '''    <a class="card" href="/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide/">
      <span class="tag">Statistical Data Visualization</span>
      <h3>Mastering SVG Box Plots &amp; Whisker Charts: Five-Number Summaries, Quartile Calculus &amp; Distribution Visualizations (2026)</h3>
      <p>Master non-parametric five-number summaries, Tukey 1.5 &times; IQR outlier boundary fences, notched 95% confidence intervals, and jittered observation overlays.</p>
    </a>
    <a class="card" href="/articles/svg-area-charts-and-stacked-streamgraph-visualization-guide/">
      <span class="tag">Temporal Area Visualizations</span>
      <h3>Mastering SVG Area Charts &amp; Stacked Streamgraphs: Baseline Offsets, Catmull-Rom Splines &amp; Vector Geometry (2026)</h3>
      <p>Master Byron-Wattenberg wiggle-minimization baselines, Catmull-Rom cubic Bézier conversion, Fritsch-Carlson monotone clamping, and 120 FPS cursor scrubbing.</p>
    </a>
    <a class="card" href="/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/">
      <span class="tag">High-Dimensional Visualizations</span>
      <h3>Mastering SVG Parallel Coordinates: High-Dimensional Geometry, Axis Normalization &amp; Dynamic Range Brushing (2026)</h3>
      <p>Master Alfred Inselberg projective point-line duality, dynamic heterogeneous axis normalization, smooth cubic Bézier bundling, and real-time range brushing.</p>
    </a>
'''

assert target_grid_marker in idx_content, "Target grid marker not found in articles/index.html"
idx_content = idx_content.replace(target_grid_marker, target_grid_marker + '\n' + new_cards)

# Add schema ItemList entries for 178, 179, 180
schema_target = '{ "@type": "ListItem", "position": 177, "url": "https://iconstash.io/articles/svg-choropleth-maps-and-geographic-vector-visualization-guide/", "name": "Mastering SVG Choropleth Maps: GeoJSON Projections, Color Quantization & Vector GIS Guide (2026)" }'
new_schema_items = ''',
      { "@type": "ListItem", "position": 178, "url": "https://iconstash.io/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide/", "name": "Mastering SVG Box Plots & Whisker Charts: Five-Number Summaries, Quartile Calculus & Distribution Visualizations (2026)" },
      { "@type": "ListItem", "position": 179, "url": "https://iconstash.io/articles/svg-area-charts-and-stacked-streamgraph-visualization-guide/", "name": "Mastering SVG Area Charts & Stacked Streamgraphs: Baseline Offsets, Catmull-Rom Splines & Vector Geometry (2026)" },
      { "@type": "ListItem", "position": 180, "url": "https://iconstash.io/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/", "name": "Mastering SVG Parallel Coordinates: High-Dimensional Geometry, Axis Normalization & Dynamic Range Brushing (2026)" }'''

assert schema_target in idx_content, "Schema target position 177 not found in articles/index.html"
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
assert '<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-18</lastmod>' in sitemap_content, "Hub lastmod not found in articles-sitemap.xml"
sitemap_content = sitemap_content.replace('<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-18</lastmod>', '<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-20</lastmod>')

new_sitemap_urls = '''  <url>
    <loc>https://iconstash.io/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide/</loc>
    <lastmod>2026-11-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/svg-area-charts-and-stacked-streamgraph-visualization-guide/</loc>
    <lastmod>2026-11-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/</loc>
    <lastmod>2026-11-20</lastmod>
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

assert '<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-18</lastmod></sitemap>' in parent_sitemap, "articles-sitemap.xml entry not found in sitemap.xml"
parent_sitemap = parent_sitemap.replace('<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-18</lastmod></sitemap>', '<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-20</lastmod></sitemap>')

for word in forbidden:
    assert word not in parent_sitemap.lower(), f"Forbidden brand '{word}' detected in sitemap.xml"

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(parent_sitemap)
print("Updated sitemap.xml successfully.")


# 4. Update llms.txt
with open('llms.txt', 'r', encoding='utf-8') as f:
    llms_content = f.read()

assert '- Last updated: 2026-11-18' in llms_content, "Header lastmod not found in llms.txt"
llms_content = llms_content.replace('- Last updated: 2026-11-18', '- Last updated: 2026-11-20')

assert 'Last updated: 2026-11-18' in llms_content, "Footer lastmod not found in llms.txt"
llms_content = llms_content.replace('Last updated: 2026-11-18', 'Last updated: 2026-11-20')

guide_target = '- [Mastering SVG Choropleth Maps: GeoJSON Projections, Color Quantization & Vector GIS Guide (2026)](https://iconstash.io/articles/svg-choropleth-maps-and-geographic-vector-visualization-guide/)'
new_llms_guides = '''- [Mastering SVG Choropleth Maps: GeoJSON Projections, Color Quantization & Vector GIS Guide (2026)](https://iconstash.io/articles/svg-choropleth-maps-and-geographic-vector-visualization-guide/)
- [Mastering SVG Box Plots & Whisker Charts: Five-Number Summaries, Quartile Calculus & Distribution Visualizations (2026)](https://iconstash.io/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide/)
- [Mastering SVG Area Charts & Stacked Streamgraphs: Baseline Offsets, Catmull-Rom Splines & Vector Geometry (2026)](https://iconstash.io/articles/svg-area-charts-and-stacked-streamgraph-visualization-guide/)
- [Mastering SVG Parallel Coordinates: High-Dimensional Geometry, Axis Normalization & Dynamic Range Brushing (2026)](https://iconstash.io/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/)'''

assert guide_target in llms_content, "Choropleth guide not found in llms.txt"
llms_content = llms_content.replace(guide_target, new_llms_guides)

for word in forbidden:
    assert word not in llms_content.lower(), f"Forbidden brand '{word}' detected in llms.txt"

with open('llms.txt', 'w', encoding='utf-8') as f:
    f.write(llms_content)
print("Updated llms.txt successfully.")
