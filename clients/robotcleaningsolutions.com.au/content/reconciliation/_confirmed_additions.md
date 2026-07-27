# Confirmed additions — client-approved 2026-07-27

The client CONFIRMED the following are genuine, so they may now be stated as fact. Add each ONLY to the pages listed, woven in as native prose. Small surgical additions, not rewrites. Preserve every existing sentence, heading, link, bullet, CTA and fact.

## HARD RULES (unchanged)
- NEVER use em-dashes, en-dashes, or double hyphens.
- Keep the single H1, all internal links, pricing framing (on-quote / "from $150 per week"), and "5-star rated on Google" (no review count). Parkdale stays suburb-level.
- Only add the specific item assigned to each page below. Do not invent extra capabilities or numbers.

## Confirmed-real capabilities and the wording to base it on (reword to fit each page's voice)
- **ARTWORK_ANTIQUES**: careful cleaning around valuable artwork, antiques and delicate heirloom pieces, treated with extra care and discretion. (A genuine high-end capability.)
- **HEPA**: HEPA-filter vacuums that trap fine dust, pollen and allergens instead of recirculating them into the air. Tie it to that page's existing dust/pollen local angle.
- **SAND_CAPTURE**: specialised vacuum equipment and fine microfibre tools that lift beach sand and grit without grinding it into floors, grout and surfaces. Tie it to that page's existing coastal-sand angle.

## Confirmed commercial items and wording
- **PROMO_50**: New clients receive $50 off their first clean. (Active offer.)
- **MEMBER_OFFERS**: 24/7 Clean members also enjoy exclusive member-only offers. (Keep generic; do NOT tie it to Airbnb/commercial/builders services or to carpet/upholstery shampooing, which the client declined.)

## Placement is provided by the caller (per page). After editing each file, verify:
```
cd /home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content && python3 - <<PY
import re
from pathlib import Path
E="<ENTRY_ID>"
t=Path(f"content/{E}/generated.md").read_text()
issues=[]
if t.count("—") or t.count("–") or t.count("--"): issues.append("dash chars")
if len([l for l in t.splitlines() if l.startswith("# ")])!=1: issues.append("H1 count != 1")
print("CHECK:", "PASS" if not issues else "FAIL "+"; ".join(issues), "| words", len(t.split()))
PY
```
Must print PASS. Do NOT git commit. Return one line per page: entry + what was added.
