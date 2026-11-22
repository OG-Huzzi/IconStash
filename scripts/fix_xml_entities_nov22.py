import re

entity_map = {
    "Theta": "&#920;",
    "pi": "&#960;",
    "delta": "&#948;",
    "Delta": "&#916;",
    "theta": "&#952;",
    "Eacute": "&#201;",
    "eacute": "&#233;",
    "tau": "&#964;",
    "times": "&#215;",
    "deg": "&#176;",
    "plusmn": "&#177;",
    "le": "&#8804;",
    "ge": "&#8805;",
    "sum": "&#8721;",
    "minus": "&#8722;",
    "sigma": "&#963;",
    "alpha": "&#945;",
    "beta": "&#946;",
    "gamma": "&#947;",
    "lambda": "&#955;",
    "mu": "&#956;",
    "omega": "&#969;",
    "Omega": "&#937;",
    "infin": "&#8734;",
    "ne": "&#8800;",
    "asymp": "&#8776;",
    "approx": "&#8776;"
}

articles = [
    "articles/svg-waterfall-charts-and-financial-variance-bridge-guide/index.html",
    "articles/svg-chord-diagrams-and-bilateral-flow-matrix-guide/index.html",
    "articles/svg-ternary-plots-and-triangular-composition-diagram-guide/index.html"
]

def fix_entities_in_svg(match):
    svg_content = match.group(0)
    for ent_name, num_ref in entity_map.items():
        svg_content = svg_content.replace(f"&{ent_name};", num_ref)
    return svg_content

for path in articles:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split on script blocks so we don't mess up JS strings
    parts = re.split(r'(<script[\s\S]*?<\/script>)', content)
    for i in range(len(parts)):
        if not parts[i].startswith('<script'):
            parts[i] = re.sub(r'<svg[\s\S]*?<\/svg>', fix_entities_in_svg, parts[i])
    content = ''.join(parts)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Cleaned XML entities in {path}")
