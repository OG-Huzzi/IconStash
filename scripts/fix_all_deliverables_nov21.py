import os
import re

print("Applying fixes across all November 21 deliverables...")

# -------------------------------------------------------------
# FIX 1: gen_nov21_article1.py
# -------------------------------------------------------------
with open(r"D:\Project IconStash\IconStash\scripts\gen_nov21_article1.py", "r", encoding="utf-8") as f:
    c1 = f.read()

# Fix meta description
old_desc1 = "Master SVG sunburst charts: radial treemap partitions, polar-to-Cartesian arc calculus, zoomable navigation, and accessible multi-level hierarchy rendering."
new_desc1 = "Master SVG sunburst charts: radial treemap partitions, polar arc calculus, zoomable navigation, and accessible multi-level hierarchy rendering."
assert len(new_desc1) <= 155
c1 = c1.replace(old_desc1, new_desc1)

# Fix heading skip and tools links in markup
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
      <a href="/articles/" class="header-cta">Browse 132 Guides</a>
    </nav>'''
c1 = c1.replace(old_header_links, new_header_links)

old_sidebar_cta = '''        <div class="cta-sidebar-box">
          <h4 class="cta-title">Explore 28 SVG Icon Sets</h4>
          <p>Supercharge your data visualizations and dashboards with IconStash's unified, accessible vector icons.</p>
          <a href="/tools/" class="header-cta" style="display:inline-block; text-align:center;">Open Icon Explorer</a>
        </div>'''

new_sidebar_cta = '''        <div class="sidebar-card cta-sidebar-box">
          <div class="cta-title">Explore Related Guides</div>
          <p>Expand your data visualization capabilities with our companion technical engineering deep dives:</p>
          <div style="display:flex; flex-direction:column; gap:8px; font-size:13px;">
            <a href="/articles/svg-box-plots-and-whisker-charts-statistical-distribution-guide/">SVG Box Plots &amp; Whisker Charts</a>
            <a href="/articles/svg-area-charts-and-stacked-streamgraph-visualization-guide/">SVG Area Charts &amp; Streamgraphs</a>
            <a href="/articles/svg-parallel-coordinates-and-multivariate-axis-visualization-guide/">SVG Parallel Coordinates</a>
          </div>
        </div>'''
c1 = c1.replace(old_sidebar_cta, new_sidebar_cta)

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
c1 = c1.replace(old_footer_links, new_footer_links)

# Fix JS script block entities in article 1
script_start = c1.find('<script>\n    // Theme toggle handling')
assert script_start != -1, "Script block not found in gen_nov21_article1.py"
script_part = c1[script_start:]
script_part = script_part.replace('&gt;', '>')
script_part = script_part.replace('&lt;', '<')
script_part = script_part.replace('&amp;&amp;', '&&')
c1 = c1[:script_start] + script_part

with open(r"D:\Project IconStash\IconStash\scripts\gen_nov21_article1.py", "w", encoding="utf-8") as f:
    f.write(c1)
print("Updated gen_nov21_article1.py")


# -------------------------------------------------------------
# FIX 2: gen_nov21_article2.py
# -------------------------------------------------------------
with open(r"D:\Project IconStash\IconStash\scripts\gen_nov21_article2.py", "r", encoding="utf-8") as f:
    c2 = f.read()

old_desc2 = "Master SVG violin plots: Gaussian kernel density estimation, Silverman bandwidth calculus, mirrored Bézier splines, and embedded box plot distribution glyphs."
new_desc2 = "Master SVG violin plots: Gaussian kernel density estimation, Silverman bandwidth calculus, mirrored Bézier splines, and embedded box plot glyphs."
assert len(new_desc2) <= 155
c2 = c2.replace(old_desc2, new_desc2)

c2 = c2.replace(old_header_links, new_header_links)
c2 = c2.replace(old_sidebar_cta, new_sidebar_cta)
c2 = c2.replace(old_footer_links, new_footer_links)

# Fix any script entities if any
script_start2 = c2.find('<script>\n    // Theme toggle handling')
if script_start2 != -1:
    script_part2 = c2[script_start2:]
    script_part2 = script_part2.replace('&gt;', '>')
    script_part2 = script_part2.replace('&lt;', '<')
    script_part2 = script_part2.replace('&amp;&amp;', '&&')
    c2 = c2[:script_start2] + script_part2

with open(r"D:\Project IconStash\IconStash\scripts\gen_nov21_article2.py", "w", encoding="utf-8") as f:
    f.write(c2)
print("Updated gen_nov21_article2.py")


# -------------------------------------------------------------
# FIX 3: gen_nov21_article3.py
# -------------------------------------------------------------
with open(r"D:\Project IconStash\IconStash\scripts\gen_nov21_article3.py", "r", encoding="utf-8") as f:
    c3 = f.read()

c3 = c3.replace(old_header_links, new_header_links)
c3 = c3.replace(old_sidebar_cta, new_sidebar_cta)
c3 = c3.replace(old_footer_links, new_footer_links)

script_start3 = c3.find('<script>\n    // Theme toggle handling')
if script_start3 != -1:
    script_part3 = c3[script_start3:]
    script_part3 = script_part3.replace('&gt;', '>')
    script_part3 = script_part3.replace('&lt;', '<')
    script_part3 = script_part3.replace('&amp;&amp;', '&&')
    c3 = c3[:script_start3] + script_part3

with open(r"D:\Project IconStash\IconStash\scripts\gen_nov21_article3.py", "w", encoding="utf-8") as f:
    f.write(c3)
print("Updated gen_nov21_article3.py")

# Regenerate all 3 articles
os.system(r'python "D:\Project IconStash\IconStash\scripts\gen_nov21_article1.py"')
os.system(r'python "D:\Project IconStash\IconStash\scripts\gen_nov21_article2.py"')
os.system(r'python "D:\Project IconStash\IconStash\scripts\gen_nov21_article3.py"')
print("All 3 articles regenerated.")
