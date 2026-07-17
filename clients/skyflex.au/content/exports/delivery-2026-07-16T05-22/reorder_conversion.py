import re
from pathlib import Path
CLIENT = Path("/home/invoi/fahad_projects/clients/skyflex.au/content")

# slug -> (audience_heading, insert_before_heading)
MOVES = {
"homepage": ("## Who a Skyflex louvred pergola suits", "## About Skyflex"),
"louvred-pergolas-sydney": ("## Who a Skyflex pergola in Sydney suits", "## About Skyflex"),
"delta-pro-retractable-roof": ("## Who the Delta Pro is best for", "## A retractable roof pergola you can order today"),
"delta-commercial-folding-arm": ("## Who the Delta Commercial Folding Arm suits", "## Pricing, sizes and how to order"),
"skyflex-4k-android-smart-outdoor-tv": ("## Who the Skyflex outdoor TV is best for", "## Pricing, sizes and pre-order"),
"skyflex-bbq-pods": ("## Who a Skyflex BBQ pod is for", "## What you are buying, and how these BBQ pods compare"),
"smart-toilets": ("## Who a smart toilet is best for", "## About Skyflex"),
}

def extract_section(text, heading):
    # from heading line to just before the next '## ' heading (or end)
    m = re.search(re.escape(heading) + r'.*?(?=\n## |\Z)', text, re.S)
    return m.group(0) if m else None

for slug, (aud_h, before_h) in MOVES.items():
    p = CLIENT / f"content/{slug}/generated.md"
    text = p.read_text()
    sec = extract_section(text, aud_h)
    if not sec:
        print(f"{slug}: audience section NOT FOUND"); continue
    # remove it (with surrounding blank lines)
    text2 = text.replace("\n" + sec.rstrip() + "\n", "\n", 1)
    if text2 == text:
        text2 = text.replace(sec, "", 1)
    # insert before target heading
    block = sec.rstrip() + "\n\n"
    if before_h in text2:
        text2 = text2.replace(before_h, block + before_h, 1)
    else:
        print(f"{slug}: before-heading '{before_h}' NOT FOUND, appending")
        text2 = text2.rstrip() + "\n\n" + block
    # tidy multiple blank lines
    text2 = re.sub(r'\n{3,}', '\n\n', text2)
    p.write_text(text2.rstrip() + "\n")
    print(f"{slug}: moved '{aud_h}' to before '{before_h}'")
print("done")
