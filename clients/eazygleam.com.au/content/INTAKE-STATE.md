# content:init — PARKED (awaiting client intake forms)

**Client:** eazygleam.com.au
**Status:** Intake started 2026-07-22, parked pending client forms.

## Decisions locked in
- **Mode:** UPGRADE (client has existing live Shopify content)
- **Meta File:** `content/Meta-file-for-content.xlsx` — AUTHORITATIVE.
  - Ignore `Eazygleam.com.au-Keyword-URL-Meta.xlsx` in the main client folder (superseded).
  - Ignore the `.xlsx:Zone.Identifier` artifact.

## Blocking on
- **Form 1** (welcome/onboarding questionnaire) — client still completing.
- **Form 2** (brand/voice or business-detail form) — client still completing.
- Do NOT source form data from `memory/` or `keyword-research/` unless the analyst explicitly authorises it.

## Meta File parsed preview — 9 target pages
**Location landing pages (4 cities, 4 keywords each — Perth from the original 5-city plan is NOT in this file):**
- `/car-detailing-products-brisbane` — car detailing products/supplies brisbane, detailing supplies brisbane, car care products brisbane
- `/car-detailing-products-sydney` — (same 4-keyword set, Sydney)
- `/car-detailing-products-melbourne` — (same set, Melbourne)
- `/car-detailing-products-adelaide` — (same set, Adelaide)
- Shared supporting keywords per location page: professional detailing supplies, premium car care, auto detailing equipment, paint protection & ceramic coatings, microfibre towels and wash mitts, exterior and interior cleaners, car wash and snow foam, cutting compounds and polishes, machine polishers and buffing pads, automotive cleaning chemicals, bulk car wash products, showroom finish

**Collection pages:**
- `/collections/tyre-shine-products` — tyre shine, tyre shine products, car tyre shine, truck tyre shine
- `/collections/brake-cleaners` — brake cleaners, brake cleaner products
  - INSTRUCTION: product pages currently rank for these keywords; product-page content should link back to this collection page so Google picks up the category for rankings over time.

**Product pages (add-content / boost-ranking mode — NOT full rewrites):**
- `/products/brake-cleaner-4l` — brake cleaner
  - INSTRUCTION: already ranking; add additional content to boost from 2nd page to 1st page.
- `/products/brake-cleaner-20-l` — brake cleaner 20l
  - INSTRUCTION: already ranking; add additional content to boost from 4th page to 1st page.
- `/products/new-tyre-slick-20l` — tyre shine, tyre shine products
  - INSTRUCTION: collection page targets 'tyre shine' too, but this product already ranks for 2 keywords, so optimise it as well; add internal link back to the tyre-shine collection page; content is ADDITIVE on top of existing page content.

> These per-page instructions must survive into each `entries/<slug>.json` and drive writer mode (add-blocks/augment vs rewrite).

## Resume checklist (next session)
1. `cd /home/invoi/fahad_projects && git pull`
2. Take Form 1 + Form 2 pastes → write verbatim to `content/intake/form1.md`, `content/intake/form2.md`
3. `scripts/parse_forms.py` → write `client-profile.json`
4. `scripts/parse_meta_file.py` on `content/Meta-file-for-content.xlsx`
5. Derive services/locations vocab from Meta File keywords + slugs → `scripts/auto_classifier.py` → `entries/<slug>.json`
6. Create cluster dirs per unique cluster_id
7. UPGRADE triage: fetch each live URL via Playwright → classify corpus/working-entry/skip → `triage-table.md`
8. Place `AGENTS.md` + `CLAUDE.md` from templates
9. `scripts/wiki_rebuild.py:rebuild_all()`
10. Log `intake_complete` to `events.jsonl`
