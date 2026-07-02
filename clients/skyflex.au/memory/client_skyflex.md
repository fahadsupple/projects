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
- **Upgrade round v1 revision** (2026-07-02): client said "focus Sydney & Melbourne only, Melbourne primary, don't get ahead of ourselves on QLD yet." Dropped both QLD keywords (`pergola brisbane` 390/mo, `pergola kits brisbane` 40/mo), replaced with:
  - `folding arm awning sydney` (110/mo, KD0) — Sydney sister-city extension of the already-selected Melbourne pick, same product page (/product/delta-commercial-folding-arm/). Confirmed clean retailer SERP (sydneyblinds.com.au, obaau.com.au, wynstan.com.au).
  - `retractable roof systems melbourne` (50/mo, KD4) — new 5th "keyword-starved new-product page" (/product/delta-pro-retractable-roof/, a live product with zero organic targeting, matching the same pattern found for the other 4 priority products). GSC shows real fragmented demand hitting the homepage already.
  - Rejected candidate during this process: `pergola builders melbourne/sydney` (260/mo, 210/mo) — live SERP check showed 100% local installer/tradie intent (Mr Verandah, MBV, Totally Outdoors, hipages / Pergola Land, Urban Exteriors, Hi-Craft) — wrong business-model fit for a product/DIY-kit retailer. **Lesson: always live-SERP-check any "builder/installer" style candidate against the client's actual business model before selecting, even if volume/KD look attractive.**

## Final 10 (v1 revised, 2026-07-02)
1. smart toilet australia — 880/mo — optimise /product/u7-smartoilet/
2. bidet toilet australia — 390/mo — new /smart-toilets/
3. folding arm awning melbourne — 170/mo — optimise /product/delta-commercial-folding-arm/
4. retractable awning melbourne — 320/mo — new /retractable-awnings/
5. outdoor tv australia — 590/mo — optimise /product/skyflex-4k-android-smart-outdoor-tv/
6. bbq pod australia — 390/mo — optimise /product/skyflex-bbq-pods/
7. pergola sydney — 1,300/mo, already #5 — optimise /louvred-pergolas-sydney/
8. pergola melbourne — 1,300/mo, already #12 — optimise /outdoor-pergolas/
9. folding arm awning sydney — 110/mo — optimise /product/delta-commercial-folding-arm/ (NEW, replaces pergola brisbane)
10. retractable roof systems melbourne — 50/mo — optimise /product/delta-pro-retractable-roof/ (NEW, replaces pergola kits brisbane)

Effective keyword reach: 5,500/mo (primary volumes).

## File locations
- Deliverable v1 original: `clients/skyflex.au/Keyword Research Report - skyflex.au.html`
- Deliverable v1 revised (Sydney/Melbourne focus): `clients/skyflex.au/Keyword Research Report - skyflex.au (v2 - Sydney-Melbourne focus).html`
- Updated raw JSON (keywords.json, all-candidates.json, merged-candidates.json etc.): `clients/skyflex.au/research-v2-updated/`
- Reference file for original 20 keywords + meta: `clients/skyflex.au/Skyflex.au-Keyword-URL-Meta.xlsx`
- Pipeline lives in the plugin cache at runtime (`~/.claude/plugins/cache/colana-mp/kwr/0.3.0/clients/<domain>/`) — this client's data was copied in temporarily to run `write_keywords.py` / `validate_selection.py` / `generate_report.py`, then removed after regenerating the report to avoid polluting the shared plugin client list. `.active-client` was restored to `naztech.com.au` afterward.

## Open items / next decision points
- QLD (Brisbane) pergola expansion is shelved, not abandoned — candidates retained in all-candidates.json appendix for a future round if the client re-opens that market.
- Client's "approved installer network" USP exists but their site is a DTC/DIY-kit funnel, not a lead-gen quote site — avoid "builder/installer" intent keywords going forward unless the site adds a genuine installer-lead funnel.
