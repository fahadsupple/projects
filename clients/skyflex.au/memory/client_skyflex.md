# skyflex.au — Client Memory

## Business
- Skyflex Pty Ltd (est. 2023). Melbourne-based (Epping showroom, appointment-based). ABN 70 670 127 287.
- Model: online product retailer + DIY kits, plus an "approved installer network" — NOT a construction/installer company.
- **Exactly 9 SKUs total** (confirmed via sitemap + live product pages): delta-commercial-folding-arm, delta-light-motorised, delta-motorized, delta-open-sky, delta-pro-retractable-roof (5 pergola/awning/roof family), skyflex-4k-android-smart-outdoor-tv (1), skyflex-bbq-pods (1), u6-smartoilet + u7-smartoilet (2). Thin catalog per category — factor this into any category-page content plan.
- Service areas: Melbourne, Sydney, Queensland (QLD paused per client instruction, see below).
- DA: report metadata cites 16 (older metric); fresh DataForSEO backlinks_bulk_ranks (0-100 scale) shows skyflex.au = 25 — use this fresher figure for any new competitive DA comparisons, note the source difference if asked.
- WooCommerce backend: **both U6 and U7 Smartoilet, and the Outdoor TV product, are currently filed under "Uncategorized"** — no custom product category taxonomy exists yet for smart toilets or outdoor TVs. Confirmed by directly visiting the live pages (Playwright), not inferred. This is a real to-do before the new category pages (`/smart-toilets/`) can be built properly.
- Testimonials block on the U6, U7, and Outdoor TV product pages currently shows **generic pergola/louvre-roof installation reviews** (wrong product) — a trust-signal defect worth flagging to the client separately from the keyword work.

## Engagement history
- **Original delivery** (ref: `Skyflex.au-Keyword-URL-Meta.xlsx`): 20 general keywords, all pergola-focused, Melbourne+Sydney pairs across 8 pages (homepage, /louvred-pergolas-sydney/, /aluminium-pergolas/, /outdoor-pergolas/, /pergola-kits/, /black-pergolas/, /white-pergolas/, /motorised-pergolas/).
- **Upgrade round v1** (2026-07-01): 10 additional keywords, weighted toward 4 new priority products (smart toilet, folding arm awning, outdoor TV, BBQ pods) + 2 pergola GSC quick-wins + 2 QLD geo-expansion.
- **v2** (2026-07-02): client said "focus Sydney & Melbourne, Melbourne primary, don't get ahead of ourselves on QLD." Dropped `pergola brisbane`/`pergola kits brisbane`, added `folding arm awning sydney` + `retractable roof systems melbourne`.
- **v3** (2026-07-02, same day): realized the location instruction applied to ALL 10 keywords, not just the 2 QLD slots — the 4 new-product keywords still used the national "australia" qualifier. Corrected to Melbourne-qualified equivalents.
- **v4 — FINAL** (2026-07-03): further refinement after deep SERP/competitive/catalog-depth analysis on 3 specific slots. See final table below.

## Final 10 (v4 — current/live version, validated clean)
| # | Keyword | Vol/mo | KD | Target | Timeline |
|---|---|---|---|---|---|
| 1 | smart toilets melbourne | 50 | 0 | New `/smart-toilets/` category page (U6+U7) | 3-6mo |
| 2 | japanese toilets melbourne | 70 | 0 | Same `/smart-toilets/` page | 4-6mo |
| 3 | folding arm awning melbourne | 170 | 0 | Optimise `/product/delta-commercial-folding-arm/` | 3-5mo |
| 4 | retractable awning melbourne | 320 | 0 | New `/retractable-awnings/` | 4-6mo |
| 5 | outdoor patio tv | 40 | 0 | Optimise `/product/skyflex-4k-android-smart-outdoor-tv/` | 6-12mo (strategic) |
| 6 | bbq pods melbourne | 30 | 0 | Optimise `/product/skyflex-bbq-pods/` | Quick win |
| 7 | pergola sydney | 1,300 | 8 | Optimise `/louvred-pergolas-sydney/` (already #5) | Quick win |
| 8 | pergola melbourne | 1,300 | 0 | Optimise `/outdoor-pergolas/` (already #12) | 3-5mo |
| 9 | folding arm awning sydney | 110 | 0 | Optimise `/product/delta-commercial-folding-arm/` | 3-5mo |
| 10 | retractable roof systems melbourne | 50 | 4 | Optimise `/product/delta-pro-retractable-roof/` | 4-6mo |

**Effective reach: 3,440/mo.** Validation passed clean (0 errors, 0 warnings).

## Key decisions and lessons from the review process

1. **#1/#2 (smart toilets/japanese toilets):** Switched smart toilet keyword to **plural** ("smart toilets melbourne") once client confirmed they're building a genuine 2-product category page (U6+U7) — plural matched the site structure, not just SEO preference, and Google Ads confirmed identical volume either way.
2. **#2 replacement (japanese toilets melbourne over bidet toilet melbourne):** `bidet toilet melbourne` was rejected — KD jumped to 42 (vs KD1 nationally) because the Melbourne SERP pulls in local installer/plumber businesses ("Bidet R Us Australia," "BIDET AUSTRALIA") not present nationally. `bidet melbourne` (90/mo, higher volume) was also rejected — live SERP showed the Shopping carousel is **entirely $35-$350 bidet seat attachments**, a completely different, cheaper product than Skyflex's $1,200 integrated units — classic intent contamination. `japanese toilets melbourne` (70/mo) won: zero installer contamination, clean bathroomware-specialist competitors (e&s, Sirius Design Centre, Cook & Bathe, ACS Bathrooms), and **verified directly against the live U6/U7 product pages** that the feature sets (warm water wash, air dry, UV sterilisation, automatic lid, voice control) functionally match the "Japanese toilet" category definition — though neither page currently uses the word "Japanese" (a content gap to fix, confirmed by visiting the live pages with Playwright, not assumed).
3. **#5 (outdoor TV) — the hardest slot, ~45 keyword variations checked across 3 rounds:**
   - `outdoor tv melbourne`: 0 measured volume — dropped.
   - `outdoor tv australia`: 880/mo but SERP has a full AI Overview naming competing brands, a Knowledge Graph entity, RTINGS.com (professional review authority) ranking "best outdoor TVs," and Harvey Norman/JB Hi-Fi/Bunnings/Amazon in Shopping — a mature, editorially-covered, big-box category. Rejected.
   - Spec-based long-tails (1000 nits, IP55, IP65, "android smart outdoor tv") — **all 0 volume**. Confirmed buyers don't search by exact spec in Australia.
   - `alfresco tv` (90/mo, deceptively LOW competition) — **false positive**: SERP is 90% about the 1980s British sketch comedy show *Alfresco* (Stephen Fry/Hugh Laurie), confirmed via Knowledge Graph entity. Rejected.
   - `affordable outdoor tv` (40/mo) — **rejected**: Google's own AI Overview defines this term as "buy a $199-$295 indoor TV + a $35-$100 weatherproof cover," a completely different (and cheaper) product/solution than Skyflex's purpose-built $1,785+ unit.
   - `outdoor tv enclosure` (320/mo, highest volume found) — **rejected**: wrong product entirely (a protective case for an existing indoor TV, not an outdoor-rated TV).
   - `waterproof outdoor tv` (260/mo, KD3) — real, substantial volume, but Shopping carousel is ~19/20 slots locked by Sylvox/Englaon/Spark (a brand-comparison query).
   - **`outdoor patio tv` (40/mo) — WINNER, selected as primary over the higher-volume `waterproof outdoor tv`.** Reasoning: carousel composition analysis showed Skyflex's own product (`SKYFLEX 4K Android Smart Outdoor Tv 55"`, $1,785) **already appears** in this term's Shopping carousel today, alongside another small seller (MWE Display) — versus almost total brand lock-out on "waterproof outdoor tv." This is a genuine signal (not proof) that Google's algorithm treats this as a more open, less brand-locked query. `waterproof outdoor tv` retained as the secondary/aspirational term on the same page.
   - **Open flag for the client:** if "waterproof"/weatherproof messaging is used anywhere on this page (primary or secondary), confirm the TV has an actual certified IP rating first — the current product page states only 4K UHD / 1000 nits / wide viewing angle, no IP/waterproof claim. Don't let SEO copy get ahead of the actual product spec.
4. **Rejected across all rounds:** `pergola builders melbourne/sydney` (260/mo, 210/mo — pure local installer/tradie intent, wrong business model), `bidet melbourne` (90/mo — attachment-product intent contamination).
5. **Meta-lesson:** Google Shopping carousel appearance ≠ organic rankability — they're different ranking systems (Merchant Center feed matching vs. backlinks/content/on-page SEO). Carousel composition is still a useful *diagnostic* signal (how brand-locked is this query?), just not a direct predictor of organic success. Used correctly here to choose between two real-volume candidates, not as a substitute for checking the organic SERP itself.
6. **Always fact-check "obvious" spec-based keyword suggestions against live Google Ads volume data before recommending** — technical/spec long-tails (nits, IP rating, OS name) consistently returned zero search volume in this vertical, even though they sound like plausible "educated buyer" search terms.

## File locations
- **Current/final deliverable:** `clients/skyflex.au/Keyword Research Report - skyflex.au (v4 - FINAL).html`
- Prior versions kept for audit trail: v1 (original, "australia"-qualified + QLD), v2 (QLD dropped, still "australia"-qualified), v3 (all Melbourne/Sydney-qualified, pre-final-refinement)
- Current raw JSON (keywords.json, all-candidates.json, merged-candidates.json, etc.): `clients/skyflex.au/research-v4-final/`
- Reference file for original 20 keywords + meta: `clients/skyflex.au/Skyflex.au-Keyword-URL-Meta.xlsx`
- Pipeline runs via the plugin cache at runtime (`~/.claude/plugins/cache/colana-mp/kwr/0.3.0/clients/<domain>/`) — copied in temporarily each round to run `write_keywords.py` / `validate_selection.py` / `generate_report.py`, then removed afterward. `.active-client` restored to `naztech.com.au` each time.

## Open items for the client conversation
- **Confirm real IP/waterproof rating for the Outdoor TV** before any "waterproof" messaging goes live on that page (rank 5/10 secondary term).
- **Build the `/smart-toilets/` category page** (currently doesn't exist — both U6 and U7 sit in WooCommerce's default "Uncategorized" bucket) with explicit "Japanese-style toilet" positioning language added to both product descriptions.
- **Fix the testimonials block** on U6, U7, and Outdoor TV product pages — currently showing unrelated pergola/louvre-roof installation reviews.
- QLD (Brisbane) pergola expansion is shelved, not abandoned — candidates retained in all-candidates.json for a future round if the client re-opens that market.

## Keyword → URL Mapping round (2026-07-06)
Applied the standard keyword-url-mapping capability (live SERP check, top 20, per keyword) to 10 keywords: smart toilets melbourne, bidet toilets melbourne, waterproof tv australia, bbq pods melbourne, folding arm awning melbourne/sydney, retractable awning melbourne, retractable roof system melbourne, pergolas sydney/melbourne.

**New findings:**
- **"bidet toilets melbourne" (plural)** — same intent-contamination pattern as the previously-rejected singular version: SERP surfaces "Bidet R Us Australia" and "BIDET AUSTRALIA" local packs + thebidetshop.com.au/bidetaustralia.com.au (cheap bidet-seat/attachment retailers), wrong product tier vs Skyflex's $1,200+ integrated units. Mapped as Secondary only on `/smart-toilets/`, never Primary.
- **"waterproof tv australia"** — same big-box brand-lock as "waterproof outdoor tv" (ENGLAON/SYLVOX/Spark/JB Hi-Fi/Harvey Norman/Amazon dominate Shopping). Secondary on the Outdoor TV product page; "outdoor patio tv" remains the primary target (unchanged from v4).
- **"pergolas melbourne" (plural) — NEW discovery, unresolved.** Live SERP shows the **homepage** (not `/outdoor-pergolas/`) ranking at position 11 for this exact query (title "Louvred Pergolas Melbourne"). The v4 plan targets `/outdoor-pergolas/` for "pergola melbourne" (singular, KD0). This is a potential cannibalization risk — two pages chasing near-identical Melbourne pergola intent. Not yet resolved with client; flagged as Secondary on homepage pending a decision on whether to consolidate onto one page.
- **"pergolas sydney" (plural)** confirmed still ranking at position 5 via `/louvred-pergolas-sydney/` — consistent with existing v4 mapping, no change needed.
- **"folding arm awning sydney"** has no dedicated Sydney SKU (only 9 total SKUs) — kept as Secondary on the same `/product/delta-commercial-folding-arm/` page rather than forcing a duplicate location page.
- No other keyword in this batch shows skyflex.au ranking in the top 20 (consistent with DA 25 competing against established Melbourne/Sydney awning, pergola, and bathroomware specialists).

## Folding arm / retractable awning — product count + classification confirmed (2026-07-06)
- Verified live via Playwright: only **1 folding arm awning SKU** exists — `Delta Commercial Folding Arm` (SKU DFA3X25BLK, /product/delta-commercial-folding-arm/). No second folding-arm product; confirmed against the full "Our Products" catalog listing (Pergolas & Shading / Outdoor Products / Indoor Products tabs). **No category page justified** for this term — would be thin/duplicate content over the single product page.
- The other 4 items in the "5 pergola/awning/roof family" SKUs (`delta-light-motorised`, `delta-motorized`, `delta-open-sky`, `delta-pro-retractable-roof`) are all **louvred pergola / retractable roof products** (category "Pergolas & Shading" per site), not additional awnings — despite "motorised"/"light"/"open sky" names sounding awning-adjacent.
- **Folding arm awning = retractable awning, confirmed first-party.** The Delta Commercial Folding Arm product page's own description reads: "The SKYFLEX Full Cassette Retractable Awning combines sleek design with high-performance features... Dickson® fabric..." — the client markets this exact SKU as a retractable awning in their own copy. This resolved the "retractable awning melbourne" mapping decision: no standalone `/retractable-awnings/` page needed; mapped as Secondary onto `/product/delta-commercial-folding-arm/` alongside "folding arm awning melbourne" (P) and "folding arm awning sydney" (S). All three keywords/one page, consistent with the "linguistic variants of the same intent → same page" mapping rule.
