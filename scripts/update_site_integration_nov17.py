import re

# 1. Update articles/index.html
with open('articles/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Update guide count 120 -> 123
assert '<span class="count">120 guides</span>' in idx_content
idx_content = idx_content.replace('<span class="count">120 guides</span>', '<span class="count">123 guides</span>')

# Prepend cards in the Guides & Tutorials section
target_grid_marker = '<div class="section-head"><h2>Guides &amp; Tutorials</h2><span class="count">123 guides</span></div>\n  <div class="grid">'
new_cards = '''    <a class="card" href="/articles/svg-donut-charts-and-circular-percentage-visualization-guide/">
      <span class="tag">Circular Visualizations</span>
      <h3>Mastering SVG Donut Charts &amp; Circular Percentages: Stroke-Dasharray Math &amp; Animation Guide (2026)</h3>
      <p>Master polar-to-Cartesian trigonometry, stroke-dasharray circumferences, annular path geometry, slice explosion offsets, and 120 FPS progress rings.</p>
    </a>
    <a class="card" href="/articles/svg-bar-charts-and-column-graph-visualization-guide/">
      <span class="tag">Cartesian Visualizations</span>
      <h3>Mastering SVG Bar Charts &amp; Column Graphs: Grouped Series &amp; Stacked Layouts Guide (2026)</h3>
      <p>Master inverted Cartesian Y-coordinates, sub-slot category bandwidths, stacked cumulative accumulators, rounded corner masks, and high-density bar grids.</p>
    </a>
    <a class="card" href="/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/">
      <span class="tag">Micro-Visualizations</span>
      <h3>Mastering SVG Sparklines &amp; Micro-Charts: Inline Trendlines, Splines &amp; Dashboard Metrics Guide (2026)</h3>
      <p>Master Edward Tufte's data-ink rules, Catmull-Rom cubic splines, zero-anchored gradient fills, terminal dot markers, and 120 FPS table virtualization.</p>
    </a>
'''

assert target_grid_marker in idx_content
idx_content = idx_content.replace(target_grid_marker, target_grid_marker + '\n' + new_cards)

# Add schema ItemList entries for 172, 173, 174
schema_target = '{ "@type": "ListItem", "position": 171, "url": "https://iconstash.io/articles/svg-funnel-charts-and-conversion-pipeline-visualization-guide/", "name": "Mastering SVG Funnel Charts & Conversion Pipelines: The Complete E-Commerce & Lead Generation Visualizer Guide (2026)" }'
new_schema_items = ''',
      { "@type": "ListItem", "position": 172, "url": "https://iconstash.io/articles/svg-donut-charts-and-circular-percentage-visualization-guide/", "name": "Mastering SVG Donut Charts & Circular Percentages: Stroke-Dasharray Math, Slice Geometry & Animation Guide (2026)" },
      { "@type": "ListItem", "position": 173, "url": "https://iconstash.io/articles/svg-bar-charts-and-column-graph-visualization-guide/", "name": "Mastering SVG Bar Charts & Column Graphs: Grouped Series, Stacked Layouts & Coordinate Math Guide (2026)" },
      { "@type": "ListItem", "position": 174, "url": "https://iconstash.io/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/", "name": "Mastering SVG Sparklines & Micro-Charts: Inline Trendlines, Area Gradients & Dashboard Metrics Guide (2026)" }'''

assert schema_target in idx_content
idx_content = idx_content.replace(schema_target, schema_target + new_schema_items)

with open('articles/index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("Updated articles/index.html successfully.")


# 2. Update articles-sitemap.xml
with open('articles-sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

# Update articles hub lastmod
assert '<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-16</lastmod>' in sitemap_content
sitemap_content = sitemap_content.replace('<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-16</lastmod>', '<loc>https://iconstash.io/articles/</loc><lastmod>2026-11-17</lastmod>')

new_sitemap_urls = '''  <url>
    <loc>https://iconstash.io/articles/svg-donut-charts-and-circular-percentage-visualization-guide/</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/svg-bar-charts-and-column-graph-visualization-guide/</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://iconstash.io/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>'''

assert '</urlset>' in sitemap_content
sitemap_content = sitemap_content.replace('</urlset>', new_sitemap_urls)

with open('articles-sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Updated articles-sitemap.xml successfully.")


# 3. Update sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    parent_sitemap = f.read()

assert '<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-16</lastmod></sitemap>' in parent_sitemap
parent_sitemap = parent_sitemap.replace('<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-16</lastmod></sitemap>', '<sitemap><loc>https://iconstash.io/articles-sitemap.xml</loc><lastmod>2026-11-17</lastmod></sitemap>')

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(parent_sitemap)
print("Updated sitemap.xml successfully.")


# 4. Update llms.txt
with open('llms.txt', 'r', encoding='utf-8') as f:
    llms_content = f.read()

assert '- Last updated: 2026-11-16' in llms_content
llms_content = llms_content.replace('- Last updated: 2026-11-16', '- Last updated: 2026-11-17')

assert 'Last updated: 2026-11-16' in llms_content
llms_content = llms_content.replace('Last updated: 2026-11-16', 'Last updated: 2026-11-17')

guide_target = '- [Mastering SVG Funnel Charts & Conversion Pipelines: The Complete E-Commerce & Lead Generation Visualizer Guide (2026)](https://iconstash.io/articles/svg-funnel-charts-and-conversion-pipeline-visualization-guide/)'
new_llms_guides = '''- [Mastering SVG Funnel Charts & Conversion Pipelines: The Complete E-Commerce & Lead Generation Visualizer Guide (2026)](https://iconstash.io/articles/svg-funnel-charts-and-conversion-pipeline-visualization-guide/)
- [Mastering SVG Donut Charts & Circular Percentages: Stroke-Dasharray Math, Slice Geometry & Animation Guide (2026)](https://iconstash.io/articles/svg-donut-charts-and-circular-percentage-visualization-guide/)
- [Mastering SVG Bar Charts & Column Graphs: Grouped Series, Stacked Layouts & Coordinate Math Guide (2026)](https://iconstash.io/articles/svg-bar-charts-and-column-graph-visualization-guide/)
- [Mastering SVG Sparklines & Micro-Charts: Inline Trendlines, Area Gradients & Dashboard Metrics Guide (2026)](https://iconstash.io/articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/)'''

assert guide_target in llms_content
llms_content = llms_content.replace(guide_target, new_llms_guides)

with open('llms.txt', 'w', encoding='utf-8') as f:
    f.write(llms_content)
print("Updated llms.txt successfully.")
