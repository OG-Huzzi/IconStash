# Update Article 1
path1 = 'articles/svg-donut-charts-and-circular-percentage-visualization-guide/index.html'
with open(path1, 'r', encoding='utf-8') as f:
    c1 = f.read()

c1 = c1.replace('html[data-theme="light"] th {', 'html[data-theme="light"] .data-table th, html[data-theme="light"] th {')
with open(path1, 'w', encoding='utf-8') as f:
    f.write(c1)
print("Article 1 updated.")


# Update Article 2
path2 = 'articles/svg-bar-charts-and-column-graph-visualization-guide/index.html'
with open(path2, 'r', encoding='utf-8') as f:
    c2 = f.read()

old_desc2 = 'Build high-performance SVG bar charts: coordinate math, grouped multi-series columns, stacked layouts, baseline alignment, and zero-lag interactive vector bars.'
new_desc2 = 'Build high-performance SVG bar charts: coordinate math, grouped multi-series columns, stacked layouts, and zero-lag interactive vector visualization.'
assert len(new_desc2) <= 155
assert old_desc2 in c2, "old_desc2 not found in Article 2"
c2 = c2.replace(old_desc2, new_desc2)

c2 = c2.replace('html[data-theme="light"] th {', 'html[data-theme="light"] .data-table th, html[data-theme="light"] th {')
with open(path2, 'w', encoding='utf-8') as f:
    f.write(c2)
print("Article 2 updated.")


# Update Article 3
path3 = 'articles/svg-sparklines-and-micro-charts-dashboard-visualization-guide/index.html'
with open(path3, 'r', encoding='utf-8') as f:
    c3 = f.read()

old_desc3 = 'Build high-performance SVG sparklines: inline trendlines, Catmull-Rom splines, zero-anchored gradient fills, Tufte data-ink rules, and 120 FPS dashboard metrics.'
new_desc3 = 'Build high-performance SVG sparklines: inline trendlines, Catmull-Rom splines, zero-anchored gradient fills, Tufte rules, and 120 FPS dashboard metrics.'
assert len(new_desc3) <= 155
assert old_desc3 in c3, "old_desc3 not found in Article 3"
c3 = c3.replace(old_desc3, new_desc3)

with open(path3, 'w', encoding='utf-8') as f:
    f.write(c3)
print("Article 3 updated.")
