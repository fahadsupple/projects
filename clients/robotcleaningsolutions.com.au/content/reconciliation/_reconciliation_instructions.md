# Reconciliation agent — old-live vs new-generated diff

The new house-cleaning pages were written FRESH (not edited from the live copy). Your job: for each assigned page, find any **genuinely valuable content that exists on the LIVE page but is missing or materially weaker on the NEW page**, so nothing worthwhile is silently lost before client delivery.

## Inputs per page (all under /home/invoi/fahad_projects/clients/robotcleaningsolutions.com.au/content)
- LIVE (old): `intake/raw-pages/<ENTRY_ID>.txt`  (extracted text of the current live page: TITLE, META DESC, Headings, Body)
- NEW: `content/<ENTRY_ID>/generated.md`
- Context if useful: `entries/<ENTRY_ID>.json`, `client-profile.json`

## What COUNTS as a valuable dropped item (flag these)
- Suburb-specific LOCAL detail: named landmarks, streets, precincts, station/beach/park names, local housing stock (period homes, apartments, coastal properties), demographic or lifestyle specifics tied to that suburb.
- A concrete SERVICE, inclusion, or capability offered on the live page but absent from the new one.
- A specific, TRUE differentiator or trust element (a real guarantee, a genuine process detail) not carried over.
- A useful FAQ TOPIC answered on the live page but not on the new one (topic, not exact wording).
- Any genuinely useful specific the new page would be stronger for keeping.

## What to IGNORE (these were changed DELIBERATELY — do NOT flag them)
- Rigid PRICE TABLES / per-tier dollar figures ($150/$200/$250 "Small/Medium/Large", "End of Lease from $310"). New pages intentionally use on-quote / "from $150 per week, tailored" framing. Do not flag missing price tables.
- The banned "Why Choose Us" / "Why Choose Robot" heading — intentionally removed.
- Hard Google REVIEW COUNTS (e.g. "13 reviews") — intentionally replaced with "5-star rated on Google".
- End-of-Lease / bond as a TARGETED service — EOL keywords were dropped from this campaign; EOL is only cross-linked, not featured. Do not flag reduced EOL emphasis.
- Boilerplate/navigation/footer text, cookie notices, generic marketing filler.
- Pure wording/tone differences where the substance is present in the new page.
- Em-dashes or styling.

## Output
Append a section to `reconciliation/findings-<BATCH>.md` for EACH page:
```
### <ENTRY_ID>
- verdict: CLEAN | MINOR | ACTION
- dropped items (valuable): <bullet list, or "none">
  - [severity: nice-to-have | should-add] <the item> — <where it was on live> — <recommended action>
- live unique angle: <the live page's angle, e.g. Brighton "coastal challenge"> — carried over? yes/no
- notes: <anything else worth the analyst seeing>
```
Be strict: only list items that are BOTH valuable AND genuinely absent/weaker on the new page. If the new page covers it in different words, it is NOT dropped. Most pages may be CLEAN — that is a fine and expected result.

## Return (short text)
One line per page: `<entry>: <verdict> (<n dropped items>)`. Then one sentence naming the single most important dropped item across your batch, if any.
