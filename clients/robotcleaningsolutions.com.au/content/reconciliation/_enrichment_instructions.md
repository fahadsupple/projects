# Enrichment agent — restore safe local colour + safe FAQ topics

You are making a SMALL, surgical addition to already-approved pages. This is NOT a rewrite. Preserve every existing sentence, heading, internal link, bullet, CTA and fact. Only ADD the two things below.

## Fixed context
- Working dir (all paths resolve here): `/home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content`
- Per-page spec: `reconciliation/enrichment-spec.json` — for your ENTRY_ID it gives `local` (the local-colour text to weave in, or null) and `faq` (a code, or null).

## HARD RULES (absolute)
- **NEVER use em-dashes, en-dashes, or double hyphens.** Use commas, colons, full stops or parentheses.
- **FACTS ONLY.** You may state the geographic / architectural local colour in the spec's `local` field (coast, salt spray, sand, sandbelt dust, tree pollen, named landmarks/streets/parks, heritage/period housing stock). You may reword it to fit the page's voice, but you MUST NOT add any capability the business has not confirmed: NO "HEPA filter", NO "specialised vacuum/equipment", NO "microfibre systems", NO "pH-neutral products", NO "artwork/antiques handling", NO specific heritage surface protocols (marble/timber treatments). Keep any care language generic ("we take extra care with delicate and period features").
- Do NOT touch pricing (stays on-quote / "from $150 per week, tailored"), the review framing ("5-star rated on Google", no count), the single H1, or any internal link. Do NOT add a "Why Choose Us" heading. Parkdale stays suburb-level, no street address.

## Task 1 — weave in the local colour (only if spec.local is not null)
Add the local-colour content as 2 to 4 sentences in the natural place: ideally near the top (in or just after the opening/lede or the page's "challenge"/why-local section). It should read as native prose in the page's voice, not a bolted-on block. Keep it SUBURB-SPECIFIC and distinct.

## Task 2 — add ONE FAQ (only if spec.faq is not null)
Add ONE question + short answer to the page's existing "Frequently Asked Questions" block. **Vary the exact question wording so it does not read identically to other suburb pages** (the audit gate blocks if sibling FAQ question sets overlap by 50%+). Use these as the basis:
- `access`  → topic: entering the home when the client is out. e.g. "How do you get into my home if I am not there?" Answer (reword): many clients are at work when we clean, so just tell us your preferred arrangement when you book, whether that is a key, a lockbox code or building access, and your dedicated, vetted and insured team will follow it.
- `pets`    → topic: pets during the clean. e.g. "What happens with my pets during a clean?" Answer (reword): let us know about your pets when you book and we will work around them, keep doors and gates secure, and use eco-friendly, non-toxic products that are safe around animals.
- `areas`   → add TWO short FAQs to areas-we-serve: (1) "Can I change or cancel my clean?" → yes, just call 0421 633 370 and we will reschedule or adjust the booking; (2) "How often should I book a clean?" → most homes suit a weekly or fortnightly membership, and we will recommend the right rhythm at your free quote.

## Finish
Write the updated file back to `content/<ENTRY_ID>/generated.md`. Then verify:
```
cd /home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content && python3 - <<PY
import re
from pathlib import Path
E="<ENTRY_ID>"
t=Path(f"content/{E}/generated.md").read_text()
issues=[]
if t.count("—") or t.count("–") or t.count("--"): issues.append("dash chars")
if len([l for l in t.splitlines() if l.startswith("# ")])!=1: issues.append("H1 count != 1")
for bad in ["HEPA","microfibre system","pH-neutral","pH neutral","antique","artwork"]:
    if bad.lower() in t.lower(): issues.append(f"banned capability claim: {bad}")
print("CHECK:", "PASS" if not issues else "FAIL "+"; ".join(issues), "| words", len(t.split()))
PY
```
Must print PASS. Return one line: entry, words added (approx), whether a FAQ was added, and the local landmark(s)/angle you wove in. Do NOT git commit.
