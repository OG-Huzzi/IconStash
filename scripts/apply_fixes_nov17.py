import re

# ==========================================
# FIX ARTICLE 1
# ==========================================
path1 = 'articles/svg-donut-charts-and-circular-percentage-visualization-guide/index.html'
with open(path1, 'r', encoding='utf-8') as f:
    c1 = f.read()

# Add light theme table header rule
table_rule = '''    html[data-theme="light"] .formula-card {
      background: #FFFFFF;
      border-color: #E2E8F0;
    }
    html[data-theme="light"] .data-table th {
      background: #F1F5F9;
      color: #0F172A;
      border-color: #E2E8F0;
    }'''

assert 'html[data-theme="light"] .formula-card {' in c1
c1 = c1.replace('''    html[data-theme="light"] .formula-card {
      background: #FFFFFF;
      border-color: #E2E8F0;
    }''', table_rule)

# In sidebar, replace <div class="sidebar-title"> with <h3 class="sidebar-title">
c1 = c1.replace('<div class="sidebar-title">Table of Contents</div>', '<h3 class="sidebar-title">Table of Contents</h3>')

with open(path1, 'w', encoding='utf-8') as f:
    f.write(c1)
print("Article 1 fixed.")


# ==========================================
# FIX ARTICLE 2
# ==========================================
path2 = 'articles/svg-bar-charts-and-column-graph-visualization-guide/index.html'
with open(path2, 'r', encoding='utf-8') as f:
    c2 = f.read()

# Shorten meta description to 154 chars
old_desc = 'Master SVG bar charts and column graphs: grouped series, stacked accumulators, coordinate math, and accessible WCAG 2.2 AA patterns for data visualization.'
new_desc = 'Master SVG bar charts: grouped series, stacked accumulators, coordinate math, and accessible WCAG 2.2 AA patterns for high-performance data visualization.'
assert len(new_desc) <= 155
c2 = c2.replace(old_desc, new_desc)

# Add light theme table header rule
assert 'html[data-theme="light"] .formula-card {' in c2
c2 = c2.replace('''    html[data-theme="light"] .formula-card {
      background: #FFFFFF;
      border-color: #E2E8F0;
    }''', table_rule)

# In sidebar, replace <div class="sidebar-title"> with <h3 class="sidebar-title">
c2 = c2.replace('<div class="sidebar-title">Table of Contents</div>', '<h3 class="sidebar-title">Table of Contents</h3>')

with open(path2, 'w', encoding='utf-8') as f:
    f.write(c2)
print("Article 2 fixed.")


# ==========================================
# FIX ARTICLE 3
# ==========================================
path3 = 'articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/index.html'
with open(path3, 'r', encoding='utf-8') as f:
    c3 = f.read()

# Shorten schema description
old_schema_desc = '''      "headline": "Mastering SVG Sparklines & Micro-Charts: Inline Trendlines, Area Gradients & Dashboard Metrics Guide (2026)",
      "description": "Comprehensive engineering guide to building lightweight, production-grade SVG sparklines and micro-charts. Covers Edward Tufte's data-ink principles, coordinate projection math, Catmull-Rom spline interpolation, dual-tone gradient area fills, endpoint halo markers, and high-density 120 FPS virtualization.",'''

new_schema_desc = '''      "headline": "Mastering SVG Sparklines & Micro-Charts: Inline Trendlines, Area Gradients & Dashboard Metrics Guide (2026)",
      "description": "Build high-performance SVG sparklines: inline trendlines, Catmull-Rom splines, zero-anchored gradient fills, Tufte data-ink rules, and 120 FPS dashboard metrics.",'''

assert old_schema_desc in c3
c3 = c3.replace(old_schema_desc, new_schema_desc)

# Remove /tools/ in header
c3 = c3.replace('''      <nav class="nav-links">
        <a href="/">Icons</a>
        <a href="/articles/">Articles</a>
        <a href="/tools/">Tools</a>
        <a href="/about/">About</a>
      </nav>''', '''      <nav class="nav-links">
        <a href="/">Icons</a>
        <a href="/articles/">Articles</a>
        <a href="/about/">About</a>
      </nav>''')

# Replace footer with standard footer
standard_footer = '''  <!-- Site Footer -->
  <footer class="site-footer" style="border-top: 1px solid var(--border); padding: 2.5rem 0; margin-top: 5rem; text-align: center; color: var(--text-dim); font-size: 0.875rem;">
    <div class="container">
      <p>&copy; 2026 IconStash.io &bull; Precision Vector Graphics &amp; Developer Resources.</p>
      <p style="margin-top: 8px;"><a href="/">Home</a> &bull; <a href="/articles/">Articles</a> &bull; <a href="/about/">About</a> &bull; <a href="/privacy/">Privacy</a></p>
    </div>
  </footer>'''

footer_match = re.search(r'<!-- Site Footer -->[\s\S]*?</footer>', c3)
assert footer_match, "Footer not found in Article 3"
c3 = c3[:footer_match.start()] + standard_footer + c3[footer_match.end():]

# Add for attribute to checkbox labels
c3 = c3.replace('<label class="checkbox-item">\n                      <input type="checkbox" id="chkShowEndDot"', '<label class="checkbox-item" for="chkShowEndDot">\n                      <input type="checkbox" id="chkShowEndDot"')
c3 = c3.replace('<label class="checkbox-item">\n                      <input type="checkbox" id="chkShowMinMax"', '<label class="checkbox-item" for="chkShowMinMax">\n                      <input type="checkbox" id="chkShowMinMax"')
c3 = c3.replace('<label class="checkbox-item">\n                      <input type="checkbox" id="chkZeroBaseline"', '<label class="checkbox-item" for="chkZeroBaseline">\n                      <input type="checkbox" id="chkZeroBaseline"')

with open(path3, 'w', encoding='utf-8') as f:
    f.write(c3)
print("Article 3 fixed.")
