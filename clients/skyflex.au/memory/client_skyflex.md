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

## Final keyword-URL mapping — 10-keyword round, locked (2026-07-06)
After volume-check via Google Ads (folding arm awning melbourne 170/mo Medium comp, folding arm awning sydney 110/mo Low comp, retractable awning melbourne 320/mo High comp), analyst chose to swap Primary on `/product/delta-commercial-folding-arm/`:
- **P = retractable awning melbourne** (320/mo — highest volume of the three, matches client's own product copy "SKYFLEX Full Cassette Retractable Awning", trade-off is High competition vs Medium)
- S = folding arm awning melbourne (170/mo — matches literal product/SKU name)
- S = folding arm awning sydney (110/mo — too low-volume to justify its own page, unlike the pergola precedent at 1,300/mo each; recommend naming Sydney directly in an on-page secondary heading, Wynstan-style "Folding Arm Awning Melbourne & Sydney", rather than burying it in body copy only, since the Sydney SERP is local-pack-heavy/local-intent and a buried secondary is unlikely to rank against Sydney-specialist competitors)

Final locked table (10 keywords):
| # | Keyword | URL | Role | Page | Rank |
|---|---|---|---|---|---|
| 1 | smart toilets melbourne | /smart-toilets/ | P | New | Not ranking |
| 2 | bidet toilets melbourne | /smart-toilets/ | S | New | Not ranking |
| 3 | waterproof tv australia | /product/skyflex-4k-android-smart-outdoor-tv/ | S | Existing | Not ranking |
| 4 | bbq pods melbourne | /product/skyflex-bbq-pods/ | P | Existing | Not ranking |
| 5 | retractable awning melbourne | /product/delta-commercial-folding-arm/ | P | Existing | Not ranking |
| 6 | folding arm awning melbourne | /product/delta-commercial-folding-arm/ | S | Existing | Not ranking |
| 7 | folding arm awning sydney | /product/delta-commercial-folding-arm/ | S | Existing | Not ranking |
| 8 | retractable roof system melbourne | /product/delta-pro-retractable-roof/ | P | Existing | Not ranking |
| 9 | pergolas sydney | /louvred-pergolas-sydney/ | P | Existing | 5 |
| 10 | pergolas melbourne | / (homepage) | S* | Existing | 11 (homepage) |

**Only one item still open:** #10 pergolas melbourne — homepage (rank 11, confirmed live) vs `/outdoor-pergolas/` (targets singular "pergola melbourne") cannibalization risk. Not yet resolved with client — needs a decision on whether to consolidate onto one page or keep split.

Also confirmed only 1 folding-arm-awning SKU exists (Delta Commercial Folding Arm) and only 1 retractable-roof SKU (Delta Pro Retractable Roof) — no 2-product category page justified for either "retractable awning" or "retractable roof system"; both stay mapped onto their single existing product pages.

## Content pipeline — intake complete (2026-07-14)
`/content:init` run in `clients/skyflex.au/content/`. **Upgrade mode.** 7 entries from `Meta-file.xlsx`, 4 clusters (homepage, service-location-pergolas, product-categories, products). Forms 1 + 2 supplied by analyst and stored verbatim in `content/intake/`.

**Live probe — skyflex.au blocks default user-agents.** curl with a default UA returns **403 on every URL**; with normal browser headers the same URLs return true statuses. Any future probe of this domain MUST send browser headers or every page will be misread as blocked. (The Playwright MCP is also unusable here — Chromium isn't installed at `/opt/google/chrome/chrome`.)

**Confirmed by probe:** `/smart-toilets/` returns a real **404** — it does not exist, so it is `new-page`, not a rewrite. The other 6 URLs are 200.

**Client instruction embedded inside the Meta File keyword cells** (would have corrupted the parsed keyword if not stripped — extracted to `content/intake/client-instructions.md`): for BOTH `pergolas melbourne` (homepage) and `pergolas sydney` (/louvred-pergolas-sydney/), *"we just need two paragraphs of content for this keyword as the existing page has content we don't want to change."* → both entries forced to `mode: add-blocks`, 200 words. **Differentiation risk:** two 2-paragraph blocks, same product, same size, adjacent intent (Melbourne vs Sydney) — the planner must differentiate them explicitly or they'll read as swapped-suburb boilerplate.

**Live defects found (independent of content work, worth sending to the dev):**
- `/product/skyflex-bbq-pods/` page title is `Delta Motorised | Skyflex` — wrong product, copy-pasted from another SKU.
- `/smart-toilets/` can't ship until the WooCommerce category taxonomy exists (U6 + U7 still sit in "Uncategorized").

**Form-vs-reality conflicts recorded in `client-profile.json:_conflicts`:**
- Form1 Q11 lists **Queensland** as a focus area; Form2 Q11 names only Melbourne/Sydney, and the Meta File has zero QLD pages. Consistent with the earlier v2 decision to pause QLD — but the client's own form still says QLD, so confirm before any page mentions it.
- Form1 Q10 asks to focus on the **U7 Smartoilet product page**; the Meta File instead targets the new `/smart-toilets/` **category** page (U6+U7). Confirm the category approach satisfies the request.
- Form2 Q15 asks for the top 5 customer questions but supplies only 4, all louvred-pergola-specific — no client-supplied FAQs exist for smart toilets, awnings, BBQ pods, or the outdoor TV.

**Cardinal-rule traps in these forms (do not repeat downstream):** Form1 Q7 ("why did you start the business") is answered with agency meta-commentary — *"The website content does not explicitly state why the business was started"* — i.e. an **absence of data, not a founding story**. `why_started` was correctly OMITTED, not populated with that sentence. Form2 Q3 has the same shape ("No further credentials or formal qualifications are listed"). Several form answers are observations *about the website* rather than client statements — read Q&A answers for this client sceptically.

**`client-facts.json` false-positive conflicts.** The fact extractor regex-scrapes every number out of the verbatim form text, so it invented three conflicts: `founding-year=2026` (that's the form **submission date** 30/06/2026, not the founding year), `clients=30` (the `30` from that same date; other candidates were ABN/phone/post-dimension digits), and a `percentage` bucket collapsing six *unrelated* metrics (25%/18%/8% discounts, 100% retention, 50% referrals). Resolved via `facts_cli.py confirm` → founding-year=**2023**, clients=**100+**. `metrics.percentage` left pending — no single value is correct for it.

**Risky claims to fact-gate before they reach any page:** "voted Australia's most affordable motorised louvre roof system" (voted by *whom*? unattributed award = ACCC exposure), "up to 8x cheaper than competitors", "up to 15-year warranty", "maintenance-free", 100% retention / 50% referrals / 5-star. Also still open from the keyword round: **do not assert a waterproof/IP rating on the Outdoor TV** (primary kw is `waterproof tv australia` and 2 secondaries assert `ip55`) until the client confirms a certified IP rating actually exists.

---

## Content plugin — research round (2026-07-14)

Research phase complete for all 6 researchable entries (homepage is `research-skipped`). 90 raw fixtures, 6 synthesized bundles, Sydney suburb ground truth. Clusters: products (4), product-categories (1), service-location-pergolas (1), homepage (1).

### THE BIG FINDING — installer-intent is the recurring trap, but it is NOT universal
Skyflex's **geo-scoped** keywords skew to installer/vendor-discovery intent (local pack present + zero product pages ranking). **Non-geo** terms skew transactional. Consistent with the earlier "pergola builders" rejection.

**But do not over-apply it.** The right test is NOT "does a `/product/` URL rank" — it is **"do product *retailers* rank"**. On `pergolas sydney`, zero product-detail URLs rank, yet **Skyflex is #2** and DIY brand Pergolux is #7. Verify each SERP; don't pattern-match.

### Keyword corrections applied (all SERP-verified, live check depth 20)
| Entry | Old | New | Vol |
|---|---|---|---|
| delta-commercial-folding-arm | retractable awning melbourne | `waterproof retractable awning` | 320 |
| delta-pro-retractable-roof | retractable roof system melbourne | `retractable roof pergola` | 720 |
| skyflex-4k-android-smart-outdoor-tv | waterproof tv australia | `weatherproof tv` | 390 |
| skyflex-bbq-pods | bbq pods melbourne | `bbq pods` | 720 |
| smart-toilets | smart toilets melbourne | `smart toilets` | 2,400 |
| louvred-pergolas-sydney | (unchanged — **already ranks #2**) | `pergolas sydney` | 1,300 |

- **`bbq pods melbourne` and `louvred pergolas sydney` had ZERO volume — they were slugs, not keywords.** ⚠️ **Discrepancy with the v4 table above, which records `bbq pods melbourne` at 30/mo.** This round's DataForSEO pull returns no volume record for it at all, and keyword-suggestions on the head term return bbq pods perth (30) / sydney (30) / brisbane (10) but **no Melbourne variant**. Old figure left in place; treat 30/mo as unverified.
- **Never trust an agent's replacement keyword without a SERP check.** The first-choice replacement for the retractable-roof page (`retractable fabric roof`) was itself installer-owned (0 product URLs in top 20) — caught only by an explicit live SERP check, not by DataForSEO's intent label.

### Commercial model is PER-PRODUCT (analyst decision, Fahad)
The "DIY product retailer" premise is contradicted three ways on the live site. Model varies by SKU — each page must reflect its own live terms:
- `delta-commercial-folding-arm` — **supply-only**, $2,000–2,300 "(Supplied)", add-to-cart, no install.
- `skyflex-bbq-pods` — **consultation-led custom**, $13,500, *"Custom Order Product – Not available for direct online purchase. Consultation Required."* No buy-now/DIY framing.
- `louvred-pergolas-sydney` — live page says *"SkyFlex designs and installs"* + DIY kit via approved-installer network.

### Smart toilets — build, but NOT as an organic play (analyst decision, Fahad)
Research says a new page **will not rank**: 2 SKUs vs competitors' 8–31 faceted products, zero bathroom topical authority, and **no adjacent-vertical retailer ranks anywhere in the top 20**. Range problem, not copy problem. Decision: build as a **paid/direct conversion asset** — head term `smart toilets`, faceted-grid shape (12–13 of top 20 are collection pages; zero PDPs rank), on-page FAQ from 11 real PAAs. **Do not promise the client organic rankings.**

### Content-integrity guardrails (carried into planning/writing)
- Outdoor TV: **do not write "anti-glare screen" or "corrosion-resistant casing"** — zero volume AND absent from the live page. Both sit in the entry's secondary-keyword list, so they look legitimate. **1000 nits is the category floor, not a differentiator** (competitors class 1000-nit units as *partial sun*).
- Sydney suburb ground truth = **INSUFFICIENT** (Brave returned zero locations/discussions/FAQs). `prohibited_claims` list bans invented climate/council/building-stock claims.
- **Awning and BBQ pod pages: zero PAA, zero Brave discussions** — nothing to seed an FAQ from. Do not invent questions.

### Facts ledger
Extractor bucketed 7 unrelated percentages into one `metrics.percentage` fact. Split into 6 distinct facts. **Publishable:** `social-proof.referral-rate` = 50% of new business from referrals. **Suppressed (`off-page`):** 100% retention (unsubstantiated absolute claim — ACL misleading-representation risk) and all per-product discount figures (volatile promo pricing).

### Live-site defects for the client (independent of content work)
- BBQ pods page: title tag is `Delta Motorised | Skyflex`; meta description is about **louvred pergolas**. Never mentions BBQ pods.
- Sydney page: links to **`skyflex.com.au`** (wrong domain — live site is `skyflex.au`); shows a **Melbourne phone number**.
- Outdoor TV page: has **no body copy at all** (competitors carry 158–551 words); AI Overview cites competitor pricing/models across 8 refs and never mentions Skyflex.
- AEO gap: ChatGPT asked where to buy a louvred pergola in Sydney cites Acetech, Terra Nature Nest, Ozzy Backyards, Patios Coast2Coast — **not Skyflex**, despite Skyflex ranking #2 in Google. All four cited firms have physical Sydney addresses.

### Content pipeline COMPLETE (2026-07-16)
Full pipeline run end-to-end: init (pre-existing) → research (7 entries) → plan (4 clusters, all locked) → generate (7/7) → audit (7/7) → export.
- **All 7 pages generated + audited: 0 blocking gate findings, humanity 100, differentiation 100, coherence sweep 0 pairs above threshold.**
- Deliverables in `content/exports/delivery-2026-07-16T05-22/`: `review.html` (standard plugin review doc), `existing-vs-new-deliverable.html` (custom — existing content rendered YELLOW in intended page position per analyst directive), `index.csv`.
- **Yellow existing-vs-new deliverable is the analyst's key format requirement** (Fahad): for any page with existing content, show existing content on yellow background embedded IN POSITION within the new content, so the developer sees what to keep and where. add-blocks pages (homepage, sydney) have `deliverable.md` with [NEW]/[EXISTING — KEEP]/[EXISTING — RECOMMEND CORRECTING] markers; rewrite pages show new content + existing-being-replaced panel; new-page (smart-toilets) all new. Generator saved at `exports/.../build_existing-vs-new.py`. NOTE: the two add-blocks writers used DIFFERENT deliverable.md marker styles (homepage = markers-in-headings, sydney = bold-line markers) — the generator handles both.
- **TWO CLIENT ACTION ITEMS surfaced (blocking a clean go-live):** (1) U6/U7 Smartoilet product pages are EMPTY SHELLS ($0.00, no specs, both in WooCommerce Uncategorized) — must populate specs+pricing + create the smart-toilet taxonomy. (2) Existing-content defects to fix on live pages: Sydney page "designs and installs" contradiction + skyflex.com.au wrong-domain link + Melbourne phone on a Sydney page; homepage "Why Choose SkyFlex" recital heading + empty U6/U7 grid tiles; BBQ-pod page wrong title tag ("Delta Motorised") + pergola meta description.
- Entries left at status "audited" (not "approved") — formal /content:approve pending client sign-off on the review deliverable.

## Upgrade implementation review (2026-07-24)
Reviewed the July 2026 upgrade build against the approved content docx + meta xlsx in `clients/skyflex.au/review/`. Deliverable: `clients/skyflex.au/review/review-skyflex-upgrade-2026-07-24.md`. **Work is live and largely correct** — all 7 pages 200 (incl. new `/smart-toilets/`, previously 404), all 7 meta titles + descriptions match approved exactly, 1 H1 each, indexable + self-canonical + OG + base schema all present, nav "View All Smart Toilets"→/smart-toilets/ added, body content present, new copy clean AU English.

**Defects found (fix list):**
1. **HIGH — H1 second line missing on 2 product pages.** Approved H1s are two-part ("Product Name: keyword-rich line", the line to render as smaller text but inside the H1 tag per the design comment). On `/product/delta-commercial-folding-arm/` and `/product/skyflex-4k-android-smart-outdoor-tv/` only the product-name part is live, so the **primary keyword ("retractable awning melbourne" / "waterproof tv australia") is absent from the H1 entirely**. `/skyflex-bbq-pods/` also missing its tagline but keyword still present (Low). Delta Pro + Smart Toilets got their full H1 correctly — so the miss is inconsistent, not a template limitation.
2. **MEDIUM — FAQ schema stale on `/` and `/louvred-pergolas-sydney/`.** Visible FAQ merges old + newly-added approved questions, but FAQPage JSON-LD still lists only the original 5. Same stale-FAQ-schema pattern seen on Flourish. (Home/Sydney FAQ only partially updated — consistent with client "don't change existing content" note, so likely intentional; stale schema still needs fixing.)
3. **LOW — FAQPage schema absent** on the 4 product pages + `/smart-toilets/` despite substantial visible FAQ content (products emit Product/Offer only).
4. **LOW — existing product copy still US-spelled** (aluminum/customization/mold/color on delta-pro, folding-arm, bbq-pods) sitting next to the new AU copy. Predates this round.
5. **CONFIRM — Delta Pro** approved standalone "Delta Pro specifications" bullet block not rendered as written; values live via WooCommerce attributes + FAQ instead (all present).

Client-side (not dev): confirm Delta Pro "100% waterproof when closed" claim (carried a "kindly confirm" comment); U6/U7 still in WooCommerce "Uncategorized" — associate with /smart-toilets/.

**Method note:** review = approved docx + meta xlsx vs live scrape. skyflex.au 403s default UAs — used browser headers (per prior memory). Screenshots referenced in the Daily Tasks doc are NOT embedded (only 1 image = a Word design comment about the H1 sub-line); the approved-content docx is the text source of truth.
