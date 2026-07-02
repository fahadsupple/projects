# skyflex.au — Client Memory

## Business
- Skyflex Pty Ltd (est. 2023). Melbourne-based (Epping showroom, appointment-based). ABN 70 670 127 287.
- Model: online product retailer + DIY kits, plus an "approved installer network" — NOT a construction/installer company.
- Services/products: Louvred pergolas, DIY pergola kits, Retractable Roof Systems, Folding Arm Awnings, BBQ Pods, Smart Outdoor TVs, Smartoilets.
- Service areas per questionnaire: Melbourne, Sydney, Queensland — but see directive below, QLD paused.
- DA (DataForSEO) at time of research: 16.

## Engagement history
- **Original delivery** (ref: `Skyflex.au-Keyword-URL-Meta.xlsx`): 20 general keywords, all pergola-focused, Melbourne+Sydney pairs across 8 pages:
  - Homepage → Louvred pergolas melbourne, Louvred roof pergolas melbourne
  - /louvred-pergolas-sydney/ → Louvred pergolas sydney, Louvred roof pergolas sydney
  - /aluminium-pergolas/ → Aluminium pergola melbourne/sydney
  - /outdoor-pergolas/ → Outdoor/Garden pergolas melbourne/sydney
  - /pergola-kits/ → Pergola kits + Diy pergola melbourne/sydney
  - /black-pergolas/, /white-pergolas/, /motorised-pergolas/ → melbourne/sydney pairs each
- **Upgrade round v1** (2026-07-01, pipeline run in `research/v1/`): 10 additional general keywords, weighted toward 4 new priority products (smart toilet, folding arm awning, outdoor TV, BBQ pods) + 2 Melbourne/Sydney GSC quick-wins + 2 QLD geo-expansion picks.
- **Upgrade round v2** (2026-07-02): client said "focus Sydney & Melbourne only, Melbourne primary, don't get ahead of ourselves on QLD yet." Dropped both QLD keywords (`pergola brisbane` 390/mo, `pergola kits brisbane` 40/mo), replaced with `folding arm awning sydney` and `retractable roof systems melbourne`. Rejected `pergola builders melbourne/sydney` as installer-intent mismatch (see lesson below).
- **Upgrade round v3** (2026-07-02, same day correction): client's location instruction actually applied to **all 10 keywords**, not just the 2 QLD slots — the 4 new-product keywords still used the "australia" national qualifier, which was wrong per the client's explicit Sydney/Melbourne-only, Melbourne-primary directive. Corrected all 4:
  - `smart toilet australia` (880/mo) → `smart toilet melbourne` (50/mo, KD0). Clean product-retailer SERP, good swap.
  - `bidet toilet australia` (390/mo, KD1) → `bidet toilet melbourne` (40/mo, **KD jumps to 42**) — flagged: the Melbourne SERP pulls in 2 local installer/plumber local-pack results ("Bidet R Us Australia", "BIDET AUSTRALIA") not present on the bare-Australia SERP. Timeline pushed from 4-6mo to 6-12mo (strategic) to reflect the harder competitive set.
  - `outdoor tv australia` (880/mo) → `outdoor tv melbourne` (**0/mo measured — zero, not just low**) — flagged prominently for client sign-off. Outdoor TVs are a nationally-searched product category in Australia; no keyword-planner tool showed ANY Melbourne-qualified volume for this phrase. SERP itself is still winnable/retailer-dominated, but the keyword string won't register in rank-tracking. Recommended the analyst confirm with the client whether this 0-volume label is acceptable or whether the page should keep "outdoor tv"/"outdoor tv australia" as its real tracked target with Melbourne trust signals layered onto the content instead.
  - `bbq pod australia` (390/mo, singular) → `bbq pods melbourne` (30/mo, **switched to plural** — singular "bbq pod melbourne" measures 0/mo while plural measures 30/mo; even the category's own Instagram handle @bbqpodsmelb uses plural).
  - **Net effect:** combined volume for these 4 slots dropped from 2,150/mo (australia-qualified) to 120/mo (melbourne-qualified) as the direct cost of full geo-consistency. Flagged transparently rather than absorbed silently — this is a real trade-off, not an error to hide.
  - **Lesson learned:** when a client gives a location-focus instruction, apply it to the ENTIRE keyword set and re-check every keyword, not just the most obviously location-related ones (the 2 QLD swaps were the obvious fix; the 4 "australia" qualifiers were the same instruction being violated less obviously). Always ask "does this instruction apply narrower or broader than the first thing I fixed?"
- **Rejected candidate** (both rounds): `pergola builders melbourne/sydney` (260/mo, 210/mo) — live SERP check showed 100% local installer/tradie intent (Mr Verandah, MBV, Totally Outdoors, hipages / Pergola Land, Urban Exteriors, Hi-Craft) — wrong business-model fit for a product/DIY-kit retailer. **Lesson: always live-SERP-check any "builder/installer" style candidate against the client's actual business model before selecting, even if volume/KD look attractive.**

## Final 10 (v3, 2026-07-02 — current/live version)
1. smart toilet melbourne — 50/mo, KD0 — optimise /product/u7-smartoilet/
2. bidet toilet melbourne — 40/mo, KD42 (flagged, harder than expected) — new /smart-toilets/
3. folding arm awning melbourne — 170/mo, KD0 — optimise /product/delta-commercial-folding-arm/
4. retractable awning melbourne — 320/mo, KD0 — new /retractable-awnings/
5. outdoor tv melbourne — 0/mo measured (flagged, needs client sign-off) — optimise /product/skyflex-4k-android-smart-outdoor-tv/
6. bbq pods melbourne — 30/mo, KD0 (plural) — optimise /product/skyflex-bbq-pods/
7. pergola sydney — 1,300/mo, already #5 — optimise /louvred-pergolas-sydney/
8. pergola melbourne — 1,300/mo, already #12 — optimise /outdoor-pergolas/
9. folding arm awning sydney — 110/mo, KD0 — optimise /product/delta-commercial-folding-arm/
10. retractable roof systems melbourne — 50/mo, KD4 — optimise /product/delta-pro-retractable-roof/

Effective keyword reach: 3,370/mo (primary volumes) — down from 5,500/mo in v2 due to the geo-correction above.

## File locations
- Deliverable v1 original: `clients/skyflex.au/Keyword Research Report - skyflex.au.html`
- Deliverable v2 (QLD dropped, still had "australia" qualifiers — superseded): `clients/skyflex.au/Keyword Research Report - skyflex.au (v2 - Sydney-Melbourne focus).html`
- **Deliverable v3 (current, all keywords Melbourne/Sydney-qualified): `clients/skyflex.au/Keyword Research Report - skyflex.au (v3 - Melbourne-Sydney corrected).html`**
- Updated raw JSON (keywords.json, all-candidates.json, merged-candidates.json etc.) for v3: `clients/skyflex.au/research-v3-updated/`
- Reference file for original 20 keywords + meta: `clients/skyflex.au/Skyflex.au-Keyword-URL-Meta.xlsx`
- Pipeline lives in the plugin cache at runtime (`~/.claude/plugins/cache/colana-mp/kwr/0.3.0/clients/<domain>/`) — this client's data was copied in temporarily each round to run `write_keywords.py` / `validate_selection.py` / `generate_report.py`, then removed after regenerating the report to avoid polluting the shared plugin client list. `.active-client` was restored to `naztech.com.au` afterward each time.

## Open items / next decision points
- **`outdoor tv melbourne` (rank 5) needs explicit client/analyst sign-off** — it's the one keyword in the final 10 with zero measured search volume. Decide before sending v3 to the client: accept as-is for geo-consistency, or keep the page's real tracked target as "outdoor tv"/"outdoor tv australia" with Melbourne trust signals layered on top of the content only.
- QLD (Brisbane) pergola expansion is shelved, not abandoned — candidates retained in all-candidates.json appendix for a future round if the client re-opens that market.
- Client's "approved installer network" USP exists but their site is a DTC/DIY-kit funnel, not a lead-gen quote site — avoid "builder/installer" intent keywords going forward unless the site adds a genuine installer-lead funnel.
- `bidet toilet melbourne` (rank 2) is now KD42 with a 6-12mo timeline — set client expectations accordingly, this is not a quick win despite being in the "product page" pattern with the others.
