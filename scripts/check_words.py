import sys
import re

if len(sys.argv) < 2:
    print("Usage: python check_words.py <path_to_html>")
    sys.exit(1)

path = sys.argv[1]
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

art_match = re.search(r'<article[^>]*class="[^"]*article-main[^"]*"[\s\S]*?</article>', content)
if not art_match:
    print("No <article class='article-main'> container found!")
    sys.exit(1)

clean_art = re.sub(r'<(script|style|svg|pre)[^>]*>[\s\S]*?</\1>', ' ', art_match.group(0), flags=re.IGNORECASE)
pure_prose = re.sub(r'<[^>]+>', ' ', clean_art)
pure_words = [w for w in pure_prose.split() if w]

clean_total = re.sub(r'<(script|style)[^>]*>[\s\S]*?</\1>', ' ', content, flags=re.IGNORECASE)
total_words = [w for w in re.sub(r'<[^>]+>', ' ', clean_total).split() if w]

print(f"File: {path}")
print(f"Total Words (clean body): {len(total_words)}")
print(f"Pure Prose Words (excluding pre, svg, script, style): {len(pure_words)}")
