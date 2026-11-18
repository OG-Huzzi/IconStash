import os
import re

print("=== APPLYING FIXES TO GENERATORS AND ARTICLES ===")

# Fix Article 1
with open('scripts/gen_nov18_article1.py', 'r', encoding='utf-8') as f:
    c1 = f.read()

# 1. Descriptions <= 155 chars
short_desc1 = "Build SVG scatter plots & bubble charts: multivariate coordinates, area radius scaling, OLS trendlines, quadtree hit-testing & interactive SVG export."
assert len(short_desc1) <= 155

c1 = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{short_desc1}">', c1)
c1 = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{short_desc1}">', c1)
c1 = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{short_desc1}">', c1)
c1 = re.sub(r'"description":\s*"[^"]*",(\s*"image":\s*"https://iconstash.io/assets/articles/svg-scatter-plots)', f'"description": "{short_desc1}",\\1', c1)

# 2. Heading skips: replace <h4> with <div class="warning-title"> / <div class="cta-title">
c1 = c1.replace('<h4>Critical Architectural Pitfall:', '<div class="warning-title">Critical Architectural Pitfall:')
c1 = c1.replace('</h4>', '</div>')
c1 = c1.replace('<h4>Explore Related Guides</h4>', '<div class="cta-title">Explore Related Guides</div>')

# Update CSS for warning-title and cta-title
c1 = c1.replace('.warning-box h4 {', '.warning-box .warning-title, .warning-box h4 {')
c1 = c1.replace('.cta-sidebar-box h4 {', '.cta-sidebar-box .cta-title, .cta-sidebar-box h4 {')
c1 = c1.replace('html[data-theme="light"] .warning-box h4 {', 'html[data-theme="light"] .warning-box .warning-title, html[data-theme="light"] .warning-box h4 {')
c1 = c1.replace('html[data-theme="light"] .cta-sidebar-box h4 {', 'html[data-theme="light"] .cta-sidebar-box .cta-title, html[data-theme="light"] .cta-sidebar-box h4 {')

# 3. Clean nav and internal links
header_old = '''    <nav>
      <a href="/articles/">Articles</a>
      <a href="/tools/">Tools</a>
      <a href="/about/">About</a>
      <button class="theme-toggle-btn" id="theme-toggle" aria-label="Toggle visual theme" type="button">
        <svg id="theme-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>
      </button>
      <a href="/tools/" class="header-cta">Studio Tools</a>
    </nav>'''

header_new = '''    <nav>
      <a href="/#/">Search 134K+ Icons</a>
      <a href="/articles/">Articles &amp; Guides</a>
      <a href="/Listicles/best-free-icon-sets-2026/">Best Sets</a>
      <a href="/Glossary/icon-svg-terminology/">Glossary</a>
      <a href="/about/">About</a>
      <a href="/#/" class="header-cta">Browse Library</a>
      <button class="theme-toggle-btn" id="theme-toggle" aria-label="Toggle visual theme" type="button">
        <svg id="theme-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>
      </button>
    </nav>'''

c1 = c1.replace(header_old, header_new)

footer_old = '''  <footer class="site-footer">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px; align-items: center;">
      <p>&copy; 2026 IconStash. Published by Great Software Company. All rights reserved.</p>
      <p><a href="/about/">About IconStash &amp; Jouni Flemming</a> &bull; <a href="/articles/">All Visualization Guides</a> &bull; <a href="/tools/">Developer Vector Tools</a></p>
    </div>
  </footer>'''

footer_new = '''  <footer class="site-footer">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px; align-items: center;">
      <p>&copy; 2026 IconStash. Published by Great Software Company. All rights reserved.</p>
      <p><a href="/about/">About IconStash &amp; Jouni Flemming</a> &bull; <a href="/articles/">All Visualization Guides</a> &bull; <a href="/privacy/">Privacy Policy</a></p>
    </div>
  </footer>'''

c1 = c1.replace(footer_old, footer_new)

# Fix sidebar links
c1 = c1.replace('href="/articles/svg-line-charts-and-continuous-data-visualization-guide/"', 'href="/articles/svg-gauges-and-circular-progress-bars-guide/"')
c1 = c1.replace('SVG Line Charts Guide', 'SVG Gauges Guide')
c1 = c1.replace('href="/articles/svg-heatmaps-and-density-matrix-visualization-guide/"', 'href="/articles/svg-heatmaps-and-activity-matrix-visualization-guide/"')
c1 = c1.replace('SVG Heatmaps Guide', 'SVG Activity Heatmaps Guide')

with open('scripts/gen_nov18_article1.py', 'w', encoding='utf-8') as f:
    f.write(c1)
print("Updated scripts/gen_nov18_article1.py")


# Fix Article 2
with open('scripts/gen_nov18_article2.py', 'r', encoding='utf-8') as f:
    c2 = f.read()

short_desc2 = "Build SVG network graphs & force layouts: Coulomb repulsion, Hooke springs, Barnes-Hut quadtrees, curved edges, and interactive node drag simulation."
assert len(short_desc2) <= 155

c2 = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{short_desc2}">', c2)
c2 = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{short_desc2}">', c2)
c2 = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{short_desc2}">', c2)
c2 = re.sub(r'"description":\s*"[^"]*",(\s*"image":\s*"https://iconstash.io/assets/articles/svg-network-graphs)', f'"description": "{short_desc2}",\\1', c2)

c2 = c2.replace('<h4>Critical Marker Geometry Pitfall:', '<div class="warning-title">Critical Marker Geometry Pitfall:')
c2 = c2.replace('</h4>', '</div>')
c2 = c2.replace('<h4>Explore Related Guides</h4>', '<div class="cta-title">Explore Related Guides</div>')

c2 = c2.replace('.warning-box h4 {', '.warning-box .warning-title, .warning-box h4 {')
c2 = c2.replace('.cta-sidebar-box h4 {', '.cta-sidebar-box .cta-title, .cta-sidebar-box h4 {')
c2 = c2.replace('html[data-theme="light"] .warning-box h4 {', 'html[data-theme="light"] .warning-box .warning-title, html[data-theme="light"] .warning-box h4 {')
c2 = c2.replace('html[data-theme="light"] .cta-sidebar-box h4 {', 'html[data-theme="light"] .cta-sidebar-box .cta-title, html[data-theme="light"] .cta-sidebar-box h4 {')

c2 = c2.replace(header_old, header_new)
c2 = c2.replace(footer_old, footer_new)

c2 = c2.replace('href="/articles/svg-line-charts-and-continuous-data-visualization-guide/"', 'href="/articles/svg-gauges-and-circular-progress-bars-guide/"')
c2 = c2.replace('SVG Line Charts Guide', 'SVG Gauges Guide')

with open('scripts/gen_nov18_article2.py', 'w', encoding='utf-8') as f:
    f.write(c2)
print("Updated scripts/gen_nov18_article2.py")


# Fix Article 3
with open('scripts/gen_nov18_article3.py', 'r', encoding='utf-8') as f:
    c3 = f.read()

short_desc3 = "Master SVG choropleth maps: GeoJSON to SVG path projection, Mercator and Albers conic math, color quantization, and responsive vector GIS scaling in SVG."
assert len(short_desc3) <= 155

c3 = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{short_desc3}">', c3)
c3 = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{short_desc3}">', c3)
c3 = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{short_desc3}">', c3)
c3 = re.sub(r'"description":\s*"[^"]*",(\s*"image":\s*"https://iconstash.io/assets/articles/svg-choropleth-maps)', f'"description": "{short_desc3}",\\1', c3)

c3 = c3.replace('<h4>Explore Related Guides</h4>', '<div class="cta-title">Explore Related Guides</div>')
c3 = c3.replace('</h4>', '</div>')

c3 = c3.replace('.warning-box h4 {', '.warning-box .warning-title, .warning-box h4 {')
c3 = c3.replace('.cta-sidebar-box h4 {', '.cta-sidebar-box .cta-title, .cta-sidebar-box h4 {')
c3 = c3.replace('html[data-theme="light"] .warning-box h4 {', 'html[data-theme="light"] .warning-box .warning-title, html[data-theme="light"] .warning-box h4 {')
c3 = c3.replace('html[data-theme="light"] .cta-sidebar-box h4 {', 'html[data-theme="light"] .cta-sidebar-box .cta-title, html[data-theme="light"] .cta-sidebar-box h4 {')

c3 = c3.replace(header_old, header_new)
c3 = c3.replace(footer_old, footer_new)

c3 = c3.replace('href="/articles/svg-heatmaps-and-density-matrix-visualization-guide/"', 'href="/articles/svg-heatmaps-and-activity-matrix-visualization-guide/"')
c3 = c3.replace('SVG Heatmaps Guide', 'SVG Activity Heatmaps Guide')

# Fix #legend-symbol anchor issue
c3 = c3.replace('<code>&lt;use href="#legend-symbol" /&gt;</code>', '<code>&amp;lt;use href=&amp;quot;#legend-symbol&amp;quot; /&amp;gt;</code>')

with open('scripts/gen_nov18_article3.py', 'w', encoding='utf-8') as f:
    f.write(c3)
print("Updated scripts/gen_nov18_article3.py")

# Regenerate all three articles
os.system('python scripts/gen_nov18_article1.py')
os.system('python scripts/gen_nov18_article2.py')
os.system('python scripts/gen_nov18_article3.py')

print("=== ALL THREE ARTICLES REGENERATED WITH FIXES ===")
