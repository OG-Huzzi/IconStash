import re
import sys

def check_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    clean_body = re.sub(r'<(script|style)[^>]*>[\s\S]*?</\1>', '', content, flags=re.I)
    clean_body = re.sub(r'<[^>]+>', ' ', clean_body)
    words = [w for w in clean_body.split() if w]
    print(f"File: {path}")
    print(f"  Total words: {len(words)}")

    article_match = re.search(r'<article[^>]*class=["\'][^"\']*article-main[^"\']*["\'][\s\S]*?</article>', content, re.I)
    if article_match:
        art = article_match.group(0)
        art_clean = re.sub(r'<(script|style)[^>]*>[\s\S]*?</\1>', '', art, flags=re.I)
        art_clean = re.sub(r'<[^>]+>', ' ', art_clean)
        art_words = [w for w in art_clean.split() if w]
        print(f"  Article body words: {len(art_words)}")

        pure_prose = re.sub(r'<(script|style|svg|pre)[^>]*>[\s\S]*?</\1>', ' ', art, flags=re.I)
        pure_prose = re.sub(r'<[^>]+>', ' ', pure_prose)
        pure_words = [w for w in pure_prose.split() if w]
        print(f"  Pure prose words: {len(pure_words)}")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'articles/svg-signature-pad-and-smooth-vector-drawing-guide/index.html'
    check_file(target)
