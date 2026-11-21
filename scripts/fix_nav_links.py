import os

files = [
    'articles/svg-sunburst-charts-and-radial-treemap-hierarchy-guide/index.html',
    'articles/svg-violin-plots-and-kernel-density-distribution-guide/index.html',
    'articles/svg-candlestick-charts-and-financial-ohlc-stock-visualization-guide/index.html',
    'scripts/gen_nov21_article1.py',
    'scripts/gen_nov21_article2.py',
    'scripts/gen_nov21_article3.py',
    'scripts/fix_all_deliverables_nov21.py'
]

for f in files:
    if not os.path.exists(f):
        print("Not found:", f)
        continue
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    modified = False
    if '<a href="/tools/">Tools</a>' in c:
        c = c.replace('<a href="/tools/">Tools</a>', '<a href="/Glossary/icon-svg-terminology/">Glossary</a>')
        modified = True
    if '<a href="/tools/" class="header-cta">Browse 28 Libraries</a>' in c:
        c = c.replace('<a href="/tools/" class="header-cta">Browse 28 Libraries</a>', '<a href="/#/" class="header-cta">Browse Library</a>')
        modified = True
    
    if modified:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(c)
        print('Updated:', f)
    else:
        print('No change needed in:', f)
