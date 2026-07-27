# Price-removal agent — client-mandated, SURGICAL

The client has asked that **no prices appear on the website**. You are removing price FIGURES from already-approved pages without damaging them. The content is research-driven and final; this is scalpel work, not rewriting.

## Fixed context
- Working dir: `/home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content`
- Files: `content/<ENTRY_ID>/generated.md`

## What MUST be removed (every instance)
1. **The client's own service/membership prices** — "from $150 per week" and any other dollar figure attached to their services. Replace with the no-figure model framing: fixed, all-inclusive, tailored to your home's size, confirmed at a free on-site quote. (That framing usually already surrounds the figure — often you just excise the "from $150 per week" clause and smooth the sentence.)
2. **ALL competitor / marketplace / rate-card figures** — hourly bands ($20 to $30 an hour), job bands ($120 to $300), medians ($180), specific operator prices ($169, $45, $135, $60), end-of-lease bands, "listings as low as $90", etc. The ARGUMENT stays (hourly rates price time not outcome; three quotes, three scopes, no honest comparison; advertised rates rarely say what is included) — the NUMBERS go.
3. **Headings containing prices** (e.g. "## $20 an Hour, $300 a Job: ...", "## What the $180 Median Actually Buys in Moorabbin", "## A $45 Headline Rate and a $200 Median: ...") — rewrite the heading to carry the same idea without figures (e.g. "## Why Hourly Rates Tell You So Little in Mentone"). Keep heading LEVEL and position; keep it suburb-specific and distinct from sibling pages.
4. **FAQ questions containing prices** (e.g. "The 3163 rate card says $20 to $30 an hour. Is that what I should be paying?") — reword the question without figures (e.g. "Is an hourly rate the right way to compare cleaners in Murrumbeena?"), keep the answer's argument, strip its figures. Keep question wording DISTINCT from sibling pages (the audit gate blocks ≥50% FAQ overlap between siblings).

## What MUST be kept (do NOT touch)
- **$10 million public liability insurance** — explicitly allowed.
- **"$50 off their first clean"** promo (homepage) — explicitly allowed.
- The pricing MODEL language without figures: "fixed", "all-inclusive", "tailored to your home size", "no hidden fees", "priced on the home, not the hour", "confirmed at a free on-site quote". This framing is a core researched differentiator; keep it.
- Everything else: headings not about price, internal links, CTAs, phone number, facts (founded 2024, 100+ clients, 95% repeat, 5-star rated on Google), local colour, FAQ topics.

## Craft rules
- **Nothing may read incomplete.** After each cut, read the full paragraph/section aloud in your head: it must flow as if it was always written that way. If a bullet list was purely price bands, replace it with a single no-figure sentence carrying the point, or fold the point into the surrounding prose. If a sentence exists only to state a figure, delete the whole sentence and stitch the neighbours.
- **NEVER use em-dashes, en-dashes, or double hyphens.** Keep the single H1. Do not change word counts drastically (a page may shrink slightly; that is fine).
- Do not add new claims, numbers, or capabilities.

## Verify per page (must print PASS)
```
cd /home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content && python3 - <<PY
import re
from pathlib import Path
E="<ENTRY_ID>"
t=Path(f"content/{E}/generated.md").read_text()
issues=[]
# any $ figure other than $10m/$10 million/$50
for m in re.finditer(r'\$\s?\d[\d,.]*\s?(?:million|m\b)?', t):
    s=m.group(0).replace(" ","")
    if s.lower() not in ("$10million","$10m") and not s.startswith("$50"):
        issues.append(f"price figure remains: {m.group(0)}")
if t.count("—") or t.count("–") or t.count("--"): issues.append("dash chars")
if len([l for l in t.splitlines() if l.startswith("# ")])!=1: issues.append("H1 count != 1")
print("CHECK:", "PASS" if not issues else "FAIL "+"; ".join(set(issues)), "| words", len(t.split()))
PY
```

## Return (short)
One line per page: entry, number of figures removed, any heading/FAQ rewritten (give the new wording), final word count. Do NOT git commit.
