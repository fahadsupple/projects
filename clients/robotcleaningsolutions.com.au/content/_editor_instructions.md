# Page editor — content pass (CTAs, bullets, meta title/description)

You are editing ONE already-written page. **This is a surgical content pass, not a rewrite.** Preserve the page's angle, structure, facts, voice and internal links. Do not add new claims.

## Fixed context
- Working directory: `/home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content`
- Page file: `content/<ENTRY_ID>/generated.md`
- Entry file: `entries/<ENTRY_ID>.json`
- Read `client-profile.json` for facts. Phone is **0421 633 370**. Business name **Robot Cleaning Solutions**.

## HARD RULES (violating any of these fails the audit gate)
- **NEVER use em-dashes (—), en-dashes (–), or double hyphens (--).** Zero tolerance. Use commas, colons, full stops or parentheses.
- Publish as hard fact ONLY: founded **2024**, **100+ clients**, **95% repeat rate**, phone, the service list, guarantees, **$10m public liability**, **5-star rated on Google** (NEVER a review count). **CLIENT MANDATE 2026-07-27: NO price figures for services/membership ("from $150 per week" is BANNED) and NO competitor prices.** Only $10m insurance and the homepage "$50 off first clean" promo may carry dollar figures. Pricing is described model-only: fixed, all-inclusive, tailored, free on-site quote.
- Business location: may say based in **Parkdale** (suburb level). **NEVER a street address.**
- Keep every existing internal link exactly as-is. Keep the single H1. Keep all headings' wording.

## Task 1 — Bullets
Convert prose that is naturally a list into markdown bullets: what's included / covered, service lists, features, audience or best-for descriptions, process steps, ranges, comparisons. Better scannability and stronger for featured snippets and AI answers.
- Do NOT bulletise narrative or persuasive prose. Ledes, positioning arguments and the credibility block stay as prose.
- Keep bullet items parallel in grammar and reasonably short. Bold a leading label where it aids scanning (e.g. `- **Kitchen:** ...`).
- If a section is already bulleted, leave it.

## Task 2 — CTAs
After every section where it naturally makes sense, add a short call to action that writes the number explicitly, e.g.:
`**Call us now on 0421 633 370** for a free, no-obligation quote.`
- Vary the wording between sections so it does not read as a repeated stamp.
- Use judgement: after service/inclusions, pricing, membership and coverage sections, yes. After the lede or immediately before the existing closing CTA, no. Roughly 3 to 5 across the page, plus the existing closing CTA.
- Never invent an alternative phone number or an email that is not already in the page.

## Task 3 — Meta title and meta description
Write them and store them in `entries/<ENTRY_ID>.json` under `attributes`:
- `attributes.meta_title` — compelling, includes the primary keyword, **MUST end with ` | Robot Cleaning Solutions`** even if that pushes it past 60 characters.
- `attributes.meta_description` — roughly 140 to 160 characters, includes the primary keyword, benefit led, ends with a light call to action. No fabricated claims, no review count.
Use the Python snippet below so the JSON stays valid:
```
cd /home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content && python3 - <<'PY'
import json
from pathlib import Path
p=Path("entries/<ENTRY_ID>.json"); d=json.loads(p.read_text())
d.setdefault("attributes",{})["meta_title"]="...YOUR TITLE | Robot Cleaning Solutions"
d["attributes"]["meta_description"]="...YOUR DESCRIPTION"
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+"\n")
print("meta_title:",d["attributes"]["meta_title"])
print("len:",len(d["attributes"]["meta_title"]),"| desc len:",len(d["attributes"]["meta_description"]))
PY
```

## Verify before finishing
```
cd /home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content && python3 - <<'PY'
import json,re
from pathlib import Path
E="<ENTRY_ID>"
t=Path(f"content/{E}/generated.md").read_text()
d=json.loads(Path(f"entries/{E}.json").read_text()).get("attributes",{})
issues=[]
if t.count("—") or t.count("–") or t.count("--"): issues.append("dash characters present")
if sum(1 for l in t.splitlines() if l.startswith("# "))!=1: issues.append("H1 count != 1")
if "0421 633 370" not in t: issues.append("phone missing")
if not d.get("meta_title","").endswith("| Robot Cleaning Solutions"): issues.append("meta_title suffix missing")
if not d.get("meta_description"): issues.append("meta_description missing")
print("CHECK:", "PASS" if not issues else "FAIL "+"; ".join(issues))
print("words:",len(t.split()),"| bullets:",sum(1 for l in t.splitlines() if l.strip().startswith("- ")),"| CTA mentions:",t.count("0421 633 370"))
PY
```
Must print PASS. Return one line: entry, word count, bullet count, number of CTAs added, and the meta title.
