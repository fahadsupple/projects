import re
from pathlib import Path

CLIENT = Path("/home/invoi/fahad_projects/clients/skyflex.au/content")
B = "https://skyflex.au"
# verified-live URL map (all returned 200; from sitemap)
U = {
    "about": f"{B}/about-us/", "contact": f"{B}/contact-us/",
    "kits": f"{B}/pergola-kits/", "products": f"{B}/our-products/",
    "outdoor": f"{B}/outdoor-pergolas/",
    "light": f"{B}/product/delta-light-motorised/",
    "motorised": f"{B}/product/delta-motorized/",
    "opensky": f"{B}/product/delta-open-sky/",
    "roof": f"{B}/product/delta-pro-retractable-roof/",
    "awning": f"{B}/product/delta-commercial-folding-arm/",
    "tv": f"{B}/product/skyflex-4k-android-smart-outdoor-tv/",
    "bbq": f"{B}/product/skyflex-bbq-pods/",
    "u6": f"{B}/product/u6-smartoilet/",
    "u7": f"{B}/product/u7-smartoilet/",
}

# per-page ordered (anchor phrase, url). Longest/most-specific first.
PLAN = {
    "homepage": [
        ("Delta Pro retractable roof", U["roof"]),
        ("Delta Light Motorised", U["light"]),
        ("folding-arm awnings", U["awning"]),
        ("outdoor 4K TV", U["tv"]),
        ("Delta Open Sky", U["opensky"]),
        ("Delta Motorised", U["motorised"]),
        ("BBQ pods", U["bbq"]),
        ("DIY kit", U["kits"]),
    ],
    "louvred-pergolas-sydney": [
        ("Delta Light Motorised", U["light"]),
        ("About page", U["about"]),
        ("kit", U["kits"]),
    ],
    "smart-toilets": [
        ("U6 Smartoilet", U["u6"]),
        ("U7 Smartoilet", U["u7"]),
        ("outdoor-living brand", U["about"]),
    ],
    "delta-pro-retractable-roof": [
        ("outdoor-living company", U["about"]),
        ("a range", U["products"]),
    ],
    "delta-commercial-folding-arm": [
        ("outdoor-living retailer", U["about"]),
        ("the range", U["products"]),
    ],
    "skyflex-4k-android-smart-outdoor-tv": [
        ("outdoor-living brand", U["about"]),
        ("pergolas and louvred roofs", U["outdoor"]),
    ],
    "skyflex-bbq-pods": [
        ("showroom in Epping", U["contact"]),
    ],
}

def linkable(line, idx):
    # skip title (0), meta (1), headings, CTA bold lines, empty lines
    if idx <= 1: return False
    s = line.lstrip()
    if s.startswith("#"): return False
    if s.startswith("**"): return False   # CTA / label lines
    if not s.strip(): return False
    return True

report = {}
for slug, pairs in PLAN.items():
    p = CLIENT / f"content/{slug}/generated.md"
    lines = p.read_text().splitlines()
    done = []
    for phrase, url in pairs:
        placed = False
        for i, line in enumerate(lines):
            if not linkable(line, i):
                continue
            # find phrase not already inside a markdown link: not preceded by '[' and the
            # occurrence not immediately part of '](' ... use a regex on the raw phrase.
            pat = re.compile(r"(?<!\[)" + re.escape(phrase) + r"(?!\]\()")
            m = pat.search(line)
            if m:
                # also ensure we are not inside an existing [..](..) span
                before = line[:m.start()]
                if before.count("[") != before.count("]"):
                    continue  # inside an open link bracket
                lines[i] = line[:m.start()] + f"[{phrase}]({url})" + line[m.end():]
                placed = True
                done.append((phrase, url))
                break
        # if not placed, silently skip (report)
    p.write_text("\n".join(lines) + "\n")
    report[slug] = done

for slug, done in report.items():
    print(f"{slug}: {len(done)} links")
    for ph, url in done:
        print(f"    [{ph}] -> {url}")
