"""Single source of truth for Twinkle Clean page metadata.

Produces exports/meta.json (consumed by both the .docx builder and the .txt
deliverable) so the two can never drift apart.

Per page: page number, URL, keywords (primary first, then secondary),
supporting keywords (from the client Meta File, where present), meta title,
meta description.
"""
import csv
import glob
import json
from pathlib import Path

CD = Path("/home/invoi/fahad_projects/clients/twinkleclean.com.au/content")
BRAND = " | Twinkle Clean"
DESC_LIMIT = 158

ANGLE_T = {
    "Office": "Office & Workplace Cleaning",
    "Retail": "Shopfront & Retail Cleaning",
    "Industrial": "Warehouse & Factory Cleaning",
    "Medical": "Medical & Consulting Rooms",
    "Hospitality": "Cafe & Restaurant Cleaning",
}
ANGLE_D = {
    "Office": "offices and workplace tenancies",
    "Retail": "shopfronts and retail tenancies",
    "Industrial": "warehouses, factories and workshops",
    "Medical": "consulting rooms and health premises",
    "Hospitality": "cafes, restaurants and venues",
}
BEN = [
    "Police-checked cleaners and no lock-in contracts.",
    "Insured cleaners, seven days a week at no extra charge.",
    "After-hours cleaning, no lock-in contracts.",
    "Seven days including public holidays, no surcharge.",
    "100% satisfaction guarantee, no lock-in contracts.",
    "Police-checked cleaners.",
    "No lock-in contracts.",
    "Seven days a week.",
]
CBEN = [
    "Pet stain and odour treatment, plus end-of-lease work.",
    "Bond-back guarantee on end-of-lease cleans.",
    "Stain and traffic-lane treatment included.",
    "Police-checked cleaners and a satisfaction guarantee.",
    "Seven days a week at no extra charge.",
    "Stain and odour treatment.",
    "Bond-back guarantee available.",
]
CTA = [
    "Call 0498 182 989 for a free quote.",
    "Free, no-obligation quote: 0498 182 989.",
    "Ring 0498 182 989 for a free quote.",
    "Free quote: 0498 182 989.",
    "Call 0498 182 989.",
]


def suburb(entry_id, prefix):
    return entry_id[len(prefix):].replace("-", " ").title().replace("Cbd", "CBD")


def fit(lead, bens, i):
    """Pick the first benefit+CTA combination that fits the description limit."""
    for bo in range(len(bens)):
        for co in range(len(CTA)):
            d = f"{lead} {bens[(i + bo) % len(bens)]} {CTA[(i + co) % len(CTA)]}"
            if len(d) <= DESC_LIMIT:
                return d
    return f"{lead} {bens[-1]} {CTA[-1]}"


def load_supporting():
    rows = list(csv.DictReader(open(CD / "meta-file.csv", encoding="utf-8-sig")))
    out = {}
    for r in rows:
        u = (r.get("URL") or "").strip()
        if not u:
            continue
        sup = (r.get("Supporting Keywords") or "").strip()
        if sup:
            out[u.rstrip("/") + "/"] = [s.strip() for s in sup.split(",") if s.strip()]
    return out


def build():
    supporting = load_supporting()
    ent = {}
    for f in glob.glob(str(CD / "entries" / "*.json")):
        d = json.load(open(f))
        ent[d["entry_id"]] = d

    order = ["homepage", "commercial-cleaning", "carpet-cleaning"]
    order += sorted(e for e in ent if e.startswith("commercial-cleaning-"))
    order += sorted(e for e in ent if e.startswith("carpet-cleaning-"))
    assert sorted(order) == sorted(ent), "entry/order mismatch"

    pages = []
    for i, e in enumerate(order):
        d = ent[e]
        if e == "homepage":
            title = "Commercial Cleaning Company Melbourne"
            desc = ("Melbourne commercial and office cleaning, plus carpet cleaning for homes "
                    "and rentals. Police-checked cleaners, no lock-in contracts. Free quote.")
        elif e == "commercial-cleaning":
            title = "Commercial Cleaning Services Melbourne | Office Cleaning"
            desc = ("Commercial and office cleaning across Melbourne. Police-checked, insured "
                    "cleaners, after-hours scheduling, no lock-in contracts. Free quote: 0498 182 989.")
        elif e == "carpet-cleaning":
            title = "Carpet Cleaning Services Melbourne | Steam Cleaning"
            desc = ("Carpet steam cleaning across Melbourne using hot water extraction. Stain and "
                    "odour treatment, end-of-lease work, satisfaction guarantee. Free quotes.")
        elif e.startswith("commercial-cleaning-"):
            s = suburb(e, "commercial-cleaning-")
            a = (d.get("attributes") or {}).get("lead_angle") or "Office"
            title = f"Commercial Cleaning {s} | {ANGLE_T[a]}"
            desc = fit(f"Commercial cleaning in {s} for {ANGLE_D[a]}.", BEN, i)
        else:
            s = suburb(e, "carpet-cleaning-")
            title = f"Carpet Cleaning {s} | Steam Cleaning & Stain Removal"
            desc = fit(f"Carpet cleaning in {s} using hot water extraction.", CBEN, i)

        url = d["url"]
        pages.append({
            "page_no": i + 1,
            "entry_id": e,
            "url": url,
            # primary first, then secondary — no separate secondary heading
            "keywords": [d["primary_keyword"]] + list(d.get("secondary_keywords") or []),
            "supporting_keywords": supporting.get(url.rstrip("/") + "/", []),
            "meta_title": title + BRAND,
            "meta_description": desc,
        })

    for p in pages:
        assert p["meta_title"].endswith("| Twinkle Clean"), p["entry_id"]
        assert len(p["meta_description"]) <= 160, p["entry_id"]

    (CD / "exports").mkdir(exist_ok=True)
    (CD / "exports/meta.json").write_text(json.dumps(pages, indent=2, ensure_ascii=False) + "\n")

    # readable .txt deliverable from the same data
    out = [
        "TWINKLE CLEAN - META TITLES & DESCRIPTIONS (63 pages)",
        'Every meta title ends with "| Twinkle Clean" per client convention.',
        "Page numbers match twinkleclean-content-63-pages.docx.",
        "",
    ]
    for p in pages:
        out += [
            f"Page {p['page_no']} - {p['entry_id']}",
            f"URL:                  {p['url']}",
            f"Keywords:             {', '.join(p['keywords'])}",
        ]
        if p["supporting_keywords"]:
            out.append(f"Supporting Keywords:  {', '.join(p['supporting_keywords'])}")
        out += [
            f"Meta Title:           {p['meta_title']}  [{len(p['meta_title'])}]",
            f"Meta Description:     {p['meta_description']}  [{len(p['meta_description'])}]",
            "",
        ]
    (CD / "exports/meta-titles-and-descriptions.txt").write_text("\n".join(out))
    return pages


if __name__ == "__main__":
    pages = build()
    print(f"pages: {len(pages)}")
    print(f"with supporting keywords: {sum(1 for p in pages if p['supporting_keywords'])}")
    print("wrote exports/meta.json + exports/meta-titles-and-descriptions.txt")
