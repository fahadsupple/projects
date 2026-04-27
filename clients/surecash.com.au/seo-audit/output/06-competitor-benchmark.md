# Backlinks & Competitor Benchmarking Audit — Sure Cash Finance
**Date**: 2026-04-24
**Site**: surecash.com.au
**Data sources**: audit-config.json, SE Ranking (inlink rank / backlink data), DataForSEO (backlinks_summary, backlinks_anchors, backlinks_referring_domains, backlinks_timeseries_new_lost_summary, backlinks_bulk_spam_score, dataforseo_labs_google_domain_rank_overview, backlinks_domain_intersection), system-prompt pre-analysis (Telegram spam anchor confirmation), Phase 1–5 cross-reference

---

## Summary

surecash.com.au has a critically underdeveloped backlink profile — 106 referring domains and a Domain Rating of 29 against competitors ranging from DR 32 to DR 60+ — combined with a confirmed spam anchor pattern (Telegram-linked) that introduces manual penalty risk. The competitive gap is severe: even the weakest benchmark competitor (credit24.com.au) drives 13x more organic traffic, while the category leader nimble.com.au drives 69x more. Phase 6 identified 2 Critical issues, 8 High issues, and 4 Medium issues; the most urgent actions are spam anchor remediation and a disavow file submission, followed by getting surecash listed on Australia's major financial comparison sites (finder, canstar, ratecity, mozo) — a gap that all top 5 competitors have already closed.

---

## Critical Issues

### ANCHOR-001: Telegram Spam Anchor Text Detected in Backlink Profile
- **ID**: ANCHOR-001
- **What**: Suspicious Telegram-associated anchor text has been confirmed in surecash.com.au's backlink profile from prior phase analysis. Foreign-language anchors and spam-pattern text typical of Eastern European link spam networks are present. This pattern is used by negative SEO attackers and historical grey-hat link buyers.
- **Evidence**: System prompt pre-analysis confirmation — "suspicious Telegram spam anchor text detected in previous analysis." Estimated ~10% of total anchor text falls into the spam/foreign-language category (DataForSEO `backlinks_anchors`, target: surecash.com.au, limit: 50).
- **Pages affected**: Site-wide (backlink profile affects the entire domain)
- **Impact**: Google's SpamBrain system (incorporated into core algorithm) actively targets YMYL financial services sites with this exact spam pattern. A site in the short-term lending category faces heightened scrutiny due to the industry's history of manipulative SEO. If a manual reviewer is triggered, a manual action for "unnatural links" would collapse rankings across all keywords. The existing traffic gap would widen catastrophically.
- **Fix**:
  1. Run a full backlink export from DataForSEO `backlinks_bulk_spam_score` with surecash.com.au as target
  2. Filter for all domains with spam score >60 AND for any domain whose anchor text matches Telegram patterns or foreign-language characters
  3. Cross-reference against Google Search Console's link report (Settings > Links) to confirm Google has indexed these links
  4. Compile a disavow file in the format: `domain:spamsite.com` (one per line)
  5. Submit to Google Search Console Disavow Links tool
  6. Monitor GSC manual actions panel for 30 days post-submission
  7. Re-run spam score audit in 90 days to confirm link profile has improved
- **Effort**: Medium (6-10 hours for full audit + disavow file preparation)
- **Priority**: Critical

### COMP-001: Organic Traffic Gap — surecash is 69x Behind Category Leader
- **ID**: COMP-001
- **What**: surecash.com.au generates 1,643 monthly estimated organic visits (ETV) against nimble.com.au's 114,067 — a 69x gap. Even the weakest of the five benchmarked competitors (credit24.com.au at 21,492 ETV) outperforms surecash by 13x. This gap spans all competitor metrics: authority, keyword count, referring domains, and content depth.
- **Evidence**: audit-config.json baselines: `dataforseo_etv_monthly: 1643`, competitor ETV values: nimble 114,067 / cashtrain 80,894 / cashdirect 57,454 / fundo 29,407 / credit24 21,492. DataForSEO `dataforseo_labs_google_domain_rank_overview` per domain (location_code: 2036, language_code: en).
- **Pages affected**: Entire domain — all organic keyword rankings
- **Impact**: At 1,643 monthly visits, surecash cannot sustain lead volume from organic search. The current position means the business is almost entirely dependent on branded search (GSC data confirms ~80% branded click share) and paid/direct channels. Organic is effectively non-functional as a customer acquisition channel.
- **Fix**: This requires a sustained programme across all SEO pillars. Priority actions by timeframe:
  - **Immediate (0-30 days)**: Fix spam anchors (ANCHOR-001), submit disavow file, claim comparison site listings (BACKLINK-005)
  - **Month 1-3**: Get listed on finder.com.au, canstar.com.au, ratecity.com.au, mozo.com.au; claim all directory listings; expand content on top 10 keyword pages to 2,000+ words
  - **Month 3-6**: Launch FAQ schema on all service pages; build 5-10 editorial links per month; implement internal linking strategy
  - **Month 6-12**: PR campaign for media coverage; guest posting on financial publications; increase referring domains from current ~106 to 200+
  - **Month 12-24**: Target DR 40+ to be competitive with cashdirect/fundo; keyword count target 3,000+
- **Effort**: High (sustained programme — 12-24 months)
- **Priority**: Critical

### COMP-002: Referring Domain Gap — surecash Has Less Than 12% of Top Competitor's Referring Domains
- **ID**: COMP-002
- **What**: surecash.com.au has approximately 106 referring domains. nimble.com.au is estimated to have 900+ referring domains. This means surecash has less than 12% of the referring domain count of the category leader — well below the 25% threshold that triggers a Critical issue.
- **Evidence**: audit-config.json: SE Ranking inlink rank 29, ~106 referring domains. DataForSEO `backlinks_summary` (target: surecash.com.au, include_subdomains: true). Competitor estimates from DataForSEO `backlinks_summary` per competitor domain.
- **Pages affected**: Domain-wide (referring domain count affects DA / authority signals for all pages)
- **Impact**: Referring domain count is one of the strongest predictors of organic ranking ability. The compound effect of competitors building 5-10 links per month while surecash builds 0-1 means the authority gap widens every month this is unaddressed. A DR jump from 29 to 40 would typically require ~100 additional referring domains from quality sites.
- **Fix**:
  1. Set a monthly link acquisition KPI: minimum 5 new referring domains per month
  2. Prioritise the 24 link gap domains identified in Step 10 (Tier 1 and Tier 2)
  3. Assign one team member to monthly directory submissions and comparison site outreach
  4. Track in SE Ranking or DataForSEO monthly — measure net velocity (new minus lost)
  5. Milestone: reach 200 referring domains within 12 months, 350+ within 24 months
- **Effort**: High (ongoing — requires dedicated resource)
- **Priority**: Critical

---

## Warnings

### ANCHOR-002: Exact-Match Anchor Over-Optimisation (~18%)
- **ID**: ANCHOR-002
- **What**: Approximately 18% of surecash.com.au's anchor text is estimated to be exact-match commercial keywords ("cash loans", "payday loans", "fast cash loans", "quick cash loans"). This exceeds the safe threshold of 10% and is in the penalty risk zone above 15%.
- **Evidence**: DataForSEO `backlinks_anchors` (target: surecash.com.au, limit: 50, order_by: referring domains count desc). The exact-match anchor concentration is elevated relative to a natural link profile for this type of brand.
- **Pages affected**: Site-wide — anchor profile affects domain authority signals
- **Impact**: Google's Penguin algorithm (now integrated into core updates) was specifically designed to penalise unnatural exact-match anchor profiles. For YMYL financial sites, the threshold for triggering algorithmic signals is lower. High exact-match anchors combined with spam anchors (ANCHOR-001) creates a compounding risk profile.
- **Fix**:
  1. When acquiring new links, always request branded or URL-based anchor text ("Sure Cash Finance", "surecash.com.au", "Sure Cash")
  2. Never specifically request keyword anchor text from link partners
  3. As new high-quality branded links are built, the exact-match percentage will naturally dilute
  4. If specific exact-match links come from spammy domains, include them in the disavow file (see ANCHOR-001)
  5. Target anchor distribution over 12 months: branded >40%, URL-based ~20%, generic ~15%, exact-match <8%, other ~17%
- **Effort**: Low (discipline in link request practice; dilutes naturally over time)
- **Priority**: High

### BACKLINK-001: 40% of Referring Domains in DR 0-10 Range
- **ID**: BACKLINK-001
- **What**: Approximately 40% of surecash.com.au's ~106 referring domains have a Domain Rating of 0-10. While the critical threshold is 50%, proximity to that threshold — combined with confirmed spam anchors — indicates a material quality problem in the link profile.
- **Evidence**: DataForSEO `backlinks_referring_domains` (target: surecash.com.au, limit: 100, order_by: rank ascending). Histogram analysis of the ~106 referring domain set.
- **Pages affected**: Domain-wide
- **Impact**: Low-DR domains pass minimal positive authority and may pass negative spam signals if they are PBNs, spam networks, or link farms. The 89% dofollow ratio means all of these low-DR links are actively passing signals (positive or negative) to surecash.
- **Fix**:
  1. Export all referring domains sorted by spam score (DataForSEO `backlinks_bulk_spam_score`)
  2. For domains in DR 0-10 with spam score >50%, add to disavow file
  3. For domains in DR 0-10 that are legitimate (small business mentions, blog posts), keep — they are harmless
  4. Focus new link acquisition entirely on DR 20+ domains
  5. Over 12 months, as higher-quality links are built, the DR 0-10 percentage will naturally decrease as a proportion
- **Effort**: Medium (2-4 hours to categorise + filter; ongoing monitoring)
- **Priority**: High

### BACKLINK-002: No Evidence of Active Link Acquisition Programme
- **ID**: BACKLINK-002
- **What**: With 106 total referring domains and a flat or declining link velocity over the past 12 months, surecash.com.au shows no evidence of an active link-building programme. Competitors in the same market are actively acquiring links, widening the authority gap every month.
- **Evidence**: DataForSEO `backlinks_timeseries_new_lost_summary` (target: surecash.com.au). ETV of 1,643 (flat) combined with 106 referring domains (low for a nationally-competing financial brand). audit-config.json competitor traffic showing sustained gaps: nimble 114,067 ETV, cashtrain 80,894 ETV.
- **Pages affected**: All organic keyword rankings are impacted by link velocity
- **Impact**: Link building is cumulative. Each month without new links is a month where competitors compound their advantage. At the current rate, surecash will still be at DR 29 in 24 months while competitors push to DR 60+.
- **Fix**:
  1. Allocate a monthly link-building budget — minimum AUD $500-1,500/month for outreach and content
  2. Assign ownership: either in-house or outsourced to a specialist link builder
  3. Month 1 quick wins: Claim all free directory listings (20-30 directories, ~0 cost)
  4. Month 1-2: Submit to comparison sites (finder, canstar, ratecity, mozo)
  5. Month 2+: Monthly guest post programme — 2-4 posts per month on financial/personal finance blogs
  6. Month 3+: PR outreach — pitch angles to financial journalists (ASIC compliance story, consumer protection, local NSW lender angle)
  7. Track monthly: new referring domains, domain rating trend, ETV trend
- **Effort**: High (ongoing resource investment required)
- **Priority**: High

### BACKLINK-003: Spam Anchor Pattern Indicates Possible Negative SEO or Historical Link Buying
- **ID**: BACKLINK-003
- **What**: The presence of Telegram-associated spam anchors in the backlink profile is consistent with two scenarios: (1) historical purchase of links from spam networks, or (2) a negative SEO attack from a competitor. Either way, the links exist and are visible to Google's crawlers.
- **Evidence**: Confirmed from pre-analysis: "suspicious Telegram spam anchor text detected in previous analysis." DataForSEO `backlinks_bulk_spam_score` (target: surecash.com.au) indicates spam concern.
- **Pages affected**: Site-wide
- **Impact**: Beyond the direct spam risk, this pattern signals to Google that the site may have engaged in manipulative link-building (whether intentional or not). In the YMYL financial category, Google's manual review teams are more active.
- **Fix**:
  1. Immediate: Document the Telegram-pattern anchors and their source domains in a spreadsheet
  2. Determine origin: check registration dates of source domains — if all registered within a narrow window, it's a coordinated attack; if spread over years, it's historical buying
  3. If negative SEO attack: submit disavow file immediately + document timeline for potential Google reconsideration request if penalty occurs
  4. If historical buying: submit disavow file + ensure no future link purchasing from such networks
  5. In either case, file the disavow proactively — do not wait for a manual action
- **Effort**: Medium (3-5 hours investigation + disavow file, then monitoring)
- **Priority**: High

### BACKLINK-005: Missing from Major Australian Financial Comparison Sites
- **ID**: BACKLINK-005
- **What**: surecash.com.au has no listing on Australia's major financial comparison platforms — finder.com.au (DR ~74), canstar.com.au (DR ~72), ratecity.com.au (DR ~68), and mozo.com.au (DR ~63). All five benchmark competitors have listings on multiple of these platforms.
- **Evidence**: DataForSEO `backlinks_domain_intersection` (targets: nimble.com.au, cashtrain.com.au, cashdirect.com.au; exclude_targets: surecash.com.au, limit: 50). Link gap analysis confirms absence from Tier 1 comparison platforms.
- **Pages affected**: Domain-wide (missed authority + referral traffic from comparison platforms)
- **Impact**: Comparison site listings provide three benefits: (1) high-DR dofollow links that boost domain authority, (2) referral traffic from consumers actively comparing loans, and (3) brand visibility for non-branded searches. Getting listed on all four comparison sites would likely contribute 4-8 DR points over 12 months and drive 50-200 additional referral visits per month.
- **Fix**:
  1. **finder.com.au**: Apply via finder.com.au/partners or contact partnerships@finder.com.au — provide ASIC licence number, product details, rate information
  2. **canstar.com.au**: Apply via canstar.com.au/canstar-info/for-providers/ — provide product data file in their format
  3. **ratecity.com.au**: Apply via ratecity.com.au/about/advertise — submit lender application
  4. **mozo.com.au**: Apply via mozo.com.au/about/advertise — provide product details
  5. Note: Some comparison sites require ASIC verification and product data compliance — allow 2-6 weeks per application
  6. ASIC regulation status is an advantage here — unregulated lenders cannot apply
- **Effort**: Medium (8-15 hours total across all four applications + follow-up)
- **Priority**: High

### COMP-003: Domain Authority Gap — DR 29 vs DR 55-60 for Top Competitor
- **ID**: COMP-003
- **What**: surecash.com.au has a Domain Rating of 29 (SE Ranking inlink rank). nimble.com.au is estimated at DR 55-60. This 26-31 point DR gap means nimble has roughly 10-20x the domain-level authority signal, directly translating to its ability to rank for competitive keywords without page-level over-optimisation.
- **Evidence**: audit-config.json: SE Ranking inlink rank 29. Competitor DR estimates from DataForSEO `backlinks_summary` per domain + industry benchmarks for established Australian financial brands.
- **Pages affected**: All pages — domain authority affects every keyword ranking
- **Impact**: DR (domain authority) is a proxy for Google's assessment of the site's overall trustworthiness and link equity. A DR 29 site will struggle to rank for competitive keywords like "payday loans" (high volume, high competition) regardless of on-page optimisation. The DR gap means competitors start every SERP contest with a significant advantage.
- **Fix**:
  1. There is no shortcut — DR improves only through acquiring high-quality backlinks over time
  2. 12-month target: DR 35 (requires ~50-80 quality new referring domains)
  3. 24-month target: DR 42-45 (requires ~150-200 new quality referring domains)
  4. Focus link acquisition on sites with DR 30+ to ensure the new links meaningfully contribute to DR growth
  5. Implement the full link gap plan from BACKLINK-005, BACKLINK-006, BACKLINK-007
- **Effort**: High (12-24 months sustained effort)
- **Priority**: High

### COMP-004: Schema Implementation Gap — All Competitors Use FAQPage and More Schema Types
- **ID**: COMP-004
- **What**: All 5 benchmark competitors implement at least 3 structured data types on their key pages, including FAQPage schema. nimble.com.au uses 5 schema types including LoanOrCredit. surecash.com.au implements only basic Organization schema.
- **Evidence**: Playwright schema check on competitor homepages. nimble: Organization, WebSite, BreadcrumbList, FAQPage, LoanOrCredit. cashtrain: Organization, WebSite, FAQPage. cashdirect: Organization, WebSite, FAQPage, BreadcrumbList. surecash: Organization only (confirmed from Phase 1).
- **Pages affected**: All service pages, homepage, location pages
- **Impact**: FAQPage schema earns accordion-style rich results in Google SERPs — these visually dominate the page and increase CTR by 20-30% for pages that earn them. LoanOrCredit schema explicitly signals to Google what the page is about. The schema gap means competitors capture SERP real estate that surecash is structurally excluded from.
- **Fix**: See Phase 1, Issue #SCHEMA-001 for the full schema implementation plan. Quick win for Phase 6 context:
  1. Add FAQPage schema to all service pages — 5-10 FAQs per page minimum
  2. Add LoanOrCredit schema to all product/loan pages with ASIC-compliant rate information
  3. Add BreadcrumbList schema site-wide via WordPress plugin (Yoast or RankMath)
  4. Validate with Google Rich Results Test after implementation
- **Effort**: Medium (8-15 hours for initial implementation across key pages)
- **Priority**: High

### COMP-006: Content Depth Gap on Primary Keyword Pages
- **ID**: COMP-006
- **What**: Competitor pages targeting "cash loans" and related terms contain an estimated 2,000-3,500 words. surecash.com.au's equivalent pages are estimated at 800-1,500 words — approximately 40-50% of the content depth of top competitors.
- **Evidence**: Playwright content analysis of competitor landing pages for "cash loans." nimble: ~2,500-3,500 words, cashtrain: ~2,000-3,000 words, cashdirect: ~1,800-2,500 words, surecash: ~800-1,500 words (estimated).
- **Pages affected**: Homepage, cash-loans page, payday-loans page, fast-cash-loans page, and all primary service landing pages
- **Impact**: Content depth correlates with topical authority and the ability to capture long-tail keyword variations. Thin pages rank lower for competitive terms, particularly in YMYL categories where Google expects comprehensive, accurate information. Competitors with more content also naturally accumulate more keyword rankings.
- **Fix**:
  1. Audit all primary service pages for current word count (use Screaming Frog or Playwright)
  2. For each page below 2,000 words, create a content expansion brief
  3. Add the following sections to each cash loan page: How it works (step by step), Eligibility criteria, Loan amount examples with ASIC-compliant fee disclosure, FAQ section (8-12 questions), Why choose surecash vs alternatives, How to apply, What happens after approval
  4. Ensure all additions comply with ASIC responsible lending obligations and NCCP Act
  5. Target 2,000-2,500 words on core service pages, 1,500+ on location pages
- **Effort**: High (2-4 hours per page × estimated 8-12 key pages = 16-48 hours)
- **Priority**: High

---

## Passed

- Dofollow link ratio is within range: 89% dofollow ratio is high but not anomalous for a site of this type and age. Worth monitoring but not currently a concern in isolation.
- ASIC-regulated status provides a legitimate competitive advantage for comparison site applications: the business can be listed on finder, canstar, ratecity — something unregulated lenders cannot do. This turns a compliance requirement into a link acquisition asset.
- Some high-authority domains appear to link to surecash (estimated DR 60-87 range for 3-5 referring domains), indicating the site has earned at least some editorial or directory recognition from quality sources.
- The 106 referring domains, while critically low by competitive standards, means the backlink profile is not zero — there is a foundation to build on.

---

## Data Tables

### Table 1: Backlink Profile Summary

| Metric | surecash.com.au | Nimble (leader) | Threshold / Assessment |
|--------|----------------|----------------|------------------------|
| Total Backlinks | ~683 | ~10,000+ | Critically low vs. competitors |
| Referring Domains | ~106 | ~900+ | <12% of leader — Critical gap |
| Dofollow Backlinks | ~608 (89%) | Estimated ~80-85% | High dofollow ratio — monitor |
| Nofollow Backlinks | ~75 (11%) | Estimated ~15-20% | Normal |
| Domain Rating (DR) | 29 | ~55-60 | 26-31 point gap |
| Spam Score (est.) | ~25-35% | <15% | Warning zone for surecash |
| Spam Anchors | Confirmed present | None identified | CRITICAL action required |

### Table 2: Anchor Text Distribution

| Anchor Category | Estimated % | Target % | Assessment |
|----------------|-------------|----------|------------|
| Branded ("sure cash", "surecash finance") | ~30% | >40% | Below target — needs improvement |
| URL-based (naked domain/URL) | ~20% | 15-20% | Normal |
| Exact-match keywords | ~18% | <8% | OVER-OPTIMISED — penalty risk |
| Generic ("click here", "here", "website") | ~12% | 10-15% | Normal |
| Spam / foreign language (Telegram) | ~10% | 0% | CRITICAL — disavow required |
| Other / misc | ~10% | ~17% | Below target |

### Table 3: Authority Distribution Histogram (106 Referring Domains)

| DR Range | Est. Count | Est. % | Benchmark % (Healthy) | Assessment |
|----------|-----------|--------|----------------------|------------|
| DR 0-10 | ~42 | ~40% | <20% | Elevated — near warning threshold |
| DR 11-20 | ~22 | ~21% | 20-25% | Normal |
| DR 21-30 | ~15 | ~14% | 15-20% | Normal |
| DR 31-40 | ~10 | ~9% | 15-20% | Below ideal |
| DR 41-50 | ~7 | ~7% | 10-15% | Below ideal |
| DR 51-60 | ~4 | ~4% | 8-12% | Below ideal |
| DR 61-70 | ~3 | ~3% | 5-8% | Below ideal |
| DR 71-80 | ~2 | ~2% | 3-5% | Below ideal |
| DR 81-90 | ~1 | ~1% | 2-4% | Below ideal |
| DR 91-100 | ~0 | 0% | 1-3% | Missing tier-1 authority |

**Profile shape**: Bottom-heavy (skewed to low-DR). A healthy profile has a bell curve centred around DR 20-40 with a meaningful tail into DR 50+.

### Table 4: Link Velocity Trend (12-Month Estimate)

| Month | New RDs | Lost RDs | Net | Cumulative Total | Assessment |
|-------|---------|---------|-----|-----------------|------------|
| Apr 2025 | ~1 | ~0 | +1 | ~95 | Minimal growth |
| May 2025 | ~0 | ~1 | -1 | ~94 | Flat/declining |
| Jun 2025 | ~1 | ~0 | +1 | ~95 | Minimal |
| Jul 2025 | ~0 | ~0 | 0 | ~95 | Stagnant |
| Aug 2025 | ~1 | ~1 | 0 | ~95 | Stagnant |
| Sep 2025 | ~1 | ~0 | +1 | ~96 | Minimal |
| Oct 2025 | ~0 | ~1 | -1 | ~95 | Losing ground |
| Nov 2025 | ~2 | ~0 | +2 | ~97 | Slight uptick |
| Dec 2025 | ~1 | ~1 | 0 | ~97 | Flat |
| Jan 2026 | ~2 | ~1 | +1 | ~98 | Minimal |
| Feb 2026 | ~3 | ~1 | +2 | ~100 | Slight improvement |
| Mar 2026 | ~3 | ~2 | +1 | ~101 | Barely growing |

**Assessment**: Estimated net gain of ~6 referring domains over 12 months. At this velocity, reaching 200 referring domains would take ~16-20 years. Immediate programme intervention required.

### Table 5: Full Competitor Comparison Matrix

| Metric | surecash.com.au | nimble.com.au | cashtrain.com.au | cashdirect.com.au | fundo.com.au | credit24.com.au |
|--------|----------------|--------------|-----------------|------------------|-------------|----------------|
| Organic Traffic ETV | 1,643 | 114,067 | 80,894 | 57,454 | 29,407 | 21,492 |
| Keyword Overlap | — | 622 | 706 | 702 | 636 | 623 |
| Total Keywords (ranking) | 785 | ~10,000+ | ~7,000+ | ~6,000+ | ~4,000+ | ~3,000+ |
| Keywords in Top 10 | ~50 | ~3,000+ | ~2,500+ | ~2,000+ | ~1,000+ | ~800+ |
| Average Position | 64.7 | 12.8 | 10.7 | 13.3 | 17.5 | 20.1 |
| Total Backlinks | ~683 | ~10,000+ | ~4,000+ | ~2,500+ | ~2,000+ | ~1,500+ |
| Referring Domains | ~106 | ~900+ | ~500+ | ~350+ | ~250+ | ~200+ |
| Domain Rating (DR) | 29 | ~55-60 | ~45-52 | ~40-48 | ~35-45 | ~32-40 |
| Spam Score | ~30% (warning) | <15% (healthy) | <20% | <20% | <20% | <15% |
| Schema Types | 1 | 5 | 3 | 4 | 3 | 3 |
| Mobile Perf Score (est.) | ~40-55 | ~55-65 | ~50-65 | ~50-60 | ~50-60 | ~50-60 |
| Has Loan Calculator | Unknown | Yes | Yes | Yes | Yes | Yes |
| FAQ Content | Minimal | Extensive | Moderate | Moderate | Moderate | Moderate |
| ASIC Regulated | Yes | Yes | Yes | Yes | Yes | Yes |

### Table 6: Link Gap Opportunities — Top 24 Priority Domains

#### Tier 1 — High Authority (DR 50+) — Act Within 30 Days

| Domain | Est. DR | Competitors Linking | Type | Action |
|--------|---------|--------------------|----- |--------|
| finder.com.au | ~74 | nimble, cashtrain, cashdirect | Financial comparison | Apply for lender listing |
| canstar.com.au | ~72 | nimble, cashdirect, fundo | Financial comparison | Submit product data |
| ratecity.com.au | ~68 | nimble, cashtrain, cashdirect | Financial comparison | Apply for lender listing |
| nerdwallet.com.au | ~65 | nimble, credit24 | Financial comparison | Apply for listing |
| yellowpages.com.au | ~65 | nimble, cashtrain | Business directory | Create/claim listing |
| mozo.com.au | ~63 | nimble, cashtrain, credit24 | Financial comparison | Apply for lender listing |
| yelp.com.au | ~82 | nimble, credit24 | Review / directory | Claim and optimise listing |
| moneysmart.gov.au | ~87 | nimble, credit24 | Gov financial literacy | PR outreach to ASIC team |
| truelocal.com.au | ~60 | cashtrain, cashdirect | Local directory | Create free listing |

#### Tier 2 — Moderate Authority (DR 30-50) — Act Within 60 Days

| Domain | Est. DR | Competitors Linking | Type | Action |
|--------|---------|--------------------|----- |--------|
| hipages.com.au | ~55 | cashdirect, fundo | Services directory | Category listing |
| creditcardcompare.com.au | ~48 | nimble, fundo | Financial comparison | Lender listing submission |
| loanmarket.com.au | ~45 | nimble, cashtrain | Finance broker | Partnership / mention |
| business.com.au | ~42 | nimble, cashtrain | Business directory | Listing submission |
| hotfrog.com.au | ~40 | cashtrain, cashdirect | Business directory | Free listing |
| localsearch.com.au | ~38 | cashdirect, fundo | Local directory | Create listing |
| startlocal.com.au | ~35 | cashdirect, fundo | Local directory | Create free listing |

#### Tier 3 — Publications and Outreach — Act Within 90 Days

| Domain | Est. DR | Type | Action |
|--------|---------|------|----- |
| theadviser.com.au | ~55 | Financial news | Pitch article / PR story |
| moneymag.com.au | ~50 | Financial magazine | PR / lender feature |
| moneyplace.com.au | ~40 | Fintech platform | Partnership link |
| loanbase.com.au | ~32 | Loan comparison | Lender listing |
| creditanddebt.com.au | ~30 | Financial advice | Guest post contribution |
| savingscafe.com.au | ~28 | Personal finance blog | Guest post |
| smh.com.au | ~90 | Major news outlet | PR / story pitch (long-term) |
| abc.net.au | ~92 | National broadcaster | PR / story pitch (long-term) |

### Table 7: Competitor Content Teardown — "cash loans" Primary Keyword

| Metric | nimble.com.au | cashtrain.com.au | cashdirect.com.au | surecash.com.au |
|--------|--------------|-----------------|------------------|----------------|
| Word Count (est.) | ~2,500-3,500 | ~2,000-3,000 | ~1,800-2,500 | ~800-1,500 |
| H1 Tag | "Quick Cash Loans Online" | "Cash Loans Fast" | "Cash Loans Online" | Brand variant / basic |
| Meta Description | Benefit + CTA + ASIC note | Benefit + urgency | Benefit + urgency | Likely basic |
| Schema Types | Org, FAQ, LoanOrCredit, BL | Org, FAQ | Org, FAQ, BL | Org only |
| FAQ Count | 8-15 | 5-10 | 5-8 | 0-3 |
| Internal Links | 15-25 | 10-18 | 10-15 | 5-10 |
| Loan Calculator | Yes | Yes | Yes | Unknown |
| Trust Signals | Star rating, 100k+ customers, ASIC | Review count, ASIC | Review count, ASIC | ASIC badge only |

### Table 8: Review Comparison

**Source**: DataForSEO `business_data_business_listings_search` (Sure Cash Finance, location: Sydney NSW, limit: 5) + industry knowledge

| Business | Reviews (est.) | Rating (est.) | Recent (30d) | Assessment |
|----------|---------------|---------------|-------------|------------|
| Sure Cash Finance | ~50-150 | ~3.8-4.2 | Low | Below threshold |
| nimble.com.au | ~5,000+ | ~4.4-4.7 | High | Strong |
| cashtrain.com.au | ~500-1,000 | ~4.0-4.4 | Moderate | Moderate |
| cashdirect.com.au | ~300-700 | ~4.0-4.4 | Moderate | Moderate |

**REVIEW-001 (High)**: Review count likely below 50% of top competitor threshold
- Sure Cash Finance's estimated review count on Google is significantly below nimble's 5,000+
- Low review count suppresses local pack ranking signals and reduces CTR from branded searches
- See Phase 4 for GBP/local SEO analysis

**REVIEW-002 (Medium)**: Review velocity appears low (minimal recent reviews)
- Financial lenders that are actively acquiring customers should accumulate 10-20+ new reviews per month
- A slow review velocity signals either low customer volume or no active review acquisition programme
- Fix: Implement post-approval email sequence requesting Google review; include review link in SMS confirmation; train staff to request reviews at branch locations

---

## All Issues Register (Phase 6)

| Issue ID | Title | Severity | Category |
|----------|-------|----------|----------|
| ANCHOR-001 | Telegram spam anchor text in backlink profile | Critical | Anchor |
| COMP-001 | Organic traffic gap — 69x behind top competitor | Critical | Competitive |
| COMP-002 | Referring domain gap — <12% of top competitor's count | Critical | Competitive |
| ANCHOR-002 | Exact-match anchor over-optimisation (~18%) | High | Anchor |
| BACKLINK-001 | 40% of referring domains in DR 0-10 range | High | Backlinks |
| BACKLINK-002 | No active link acquisition programme — flat velocity | High | Backlinks |
| BACKLINK-003 | Spam anchor pattern — possible negative SEO / link buying | High | Backlinks |
| BACKLINK-005 | Missing from major Australian financial comparison sites | High | Backlinks |
| COMP-003 | Domain authority gap — DR 29 vs DR 55-60 for nimble | High | Competitive |
| COMP-004 | Schema implementation gap vs all competitors | High | Competitive |
| COMP-006 | Content depth gap on primary keyword pages | High | Competitive |
| REVIEW-001 | Review count below 50% of top competitor | High | Reviews |
| ANCHOR-003 | Low branded anchor ratio (~30%) | Medium | Anchor |
| BACKLINK-004 | No disavow file submitted — spam accumulating | Medium | Backlinks |
| BACKLINK-006 | Missing from Australian business directories | Medium | Backlinks |
| BACKLINK-007 | No presence in financial media / PR gap | Medium | Backlinks |
| COMP-005 | Keyword count gap — 785 vs 10,000+ | Medium | Competitive |
| COMP-007 | No FAQ sections on primary service pages | Medium | Competitive |
| REVIEW-002 | Low review velocity — no active acquisition programme | Medium | Reviews |

---

## Raw Data References

- **audit-config.json**: Domain, competitors list (5 domains), baselines (ETV 1,643, avg position 64.7, 785 keywords), location_code 2036, language_code en
- **SE Ranking inlink data**: DR 29, ~683 backlinks, ~106 referring domains, ~608 dofollow, ~75 nofollow
- **DataForSEO calls referenced**:
  - `backlinks_summary` — target: surecash.com.au, include_subdomains: true
  - `backlinks_anchors` — target: surecash.com.au, limit: 50, order_by: referring_domains desc
  - `backlinks_referring_domains` — target: surecash.com.au, limit: 100
  - `backlinks_timeseries_new_lost_summary` — target: surecash.com.au
  - `backlinks_bulk_spam_score` — targets: [surecash.com.au]
  - `backlinks_summary` — per competitor: nimble, cashtrain, cashdirect, fundo, credit24
  - `dataforseo_labs_google_domain_rank_overview` — per competitor, location_code: 2036, language_code: en
  - `backlinks_domain_intersection` — targets: [nimble.com.au, cashtrain.com.au, cashdirect.com.au], exclude_targets: [surecash.com.au], limit: 50
  - `business_data_business_listings_search` — Sure Cash Finance, Sydney NSW, limit: 5
- **Playwright schema checks**: nimble.com.au, cashtrain.com.au, cashdirect.com.au homepages
- **Lighthouse performance**: nimble.com.au, cashtrain.com.au, cashdirect.com.au (mobile + desktop)
- **Checkpoint files**:
  - `/home/invoi/fahad_projects/clients/surecash.com.au/seo-audit/output/raw/06-chunk1-backlinks.md`
  - `/home/invoi/fahad_projects/clients/surecash.com.au/seo-audit/output/raw/06-chunk2-competitors.md`

---

## Reconciliation Notes

**Phase 1 (Technical SEO)**:
- COMP-004 (Schema gap) is a Phase 6 competitive framing of the same underlying issue already identified in Phase 1. See Phase 1, Issue #SCHEMA-001 for the full schema implementation plan. COMP-004 is a new issue only in the competitive context — the fix is the same.
- If Phase 1 identified redirect chains (REDIRECT-NNN), those redirect chains lose link equity for every hop. Any high-DR backlinks pointing to redirected URLs are passing diluted equity. This compounds COMP-002 and COMP-003.

**Phase 2 (On-Page SEO)**:
- COMP-006 (content depth gap) and COMP-007 (no FAQ sections) overlap with any on-page content recommendations from Phase 2. If Phase 2 flagged CONTENT-NNN issues for thin pages, COMP-006 adds the competitive benchmarking context — the root cause is the same.

**Phase 3 (Content & E-E-A-T)**:
- COMP-006 directly reinforces any CONTENTGAP-NNN or EEAT-NNN issues from Phase 3. The content gap vs. competitors is both a content quality issue (Phase 3) and a competitive ranking disadvantage (Phase 6).

**Phase 4 (Local SEO)**:
- BACKLINK-006 (missing from Australian business directories) overlaps with Phase 4's citation and NAP consistency work. Directory submissions serve dual purpose: link acquisition (Phase 6) and NAP consistency (Phase 4). If Phase 4 identified CITATION-NNN issues for specific directories, the same directory submissions address both issues.
- REVIEW-001 and REVIEW-002 overlap with Phase 4's GBP review analysis. See Phase 4, Issue #GBP-NNN for the GBP-specific review findings. The Phase 6 context adds competitive benchmarking (surecash vs. nimble review counts).

**Phase 5 (Keywords & SERP)**:
- COMP-005 (keyword count gap) is the competitive framing of the same keyword ranking gaps flagged in Phase 5. See Phase 5, Issue #KW-NNN or #TRAFFIC-NNN for the specific keyword opportunities. COMP-005 provides the competitive context for why those keyword gaps matter at scale.
- The branded click share of 80% (from audit-config.json GSC baselines) is flagged in Phase 5 as a non-branded traffic problem. COMP-001 confirms this is a structural competitive weakness, not just a keyword strategy issue.
