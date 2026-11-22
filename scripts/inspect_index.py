with open('articles/index.html', 'r', encoding='utf-8') as f:
    c = f.read()
import re
print('Guides match:', re.search(r'\d+\s+guides', c).group(0))
pos_matches = re.findall(r'"position":\s*(\d+)', c)
print('Last 5 positions:', pos_matches[-5:])
