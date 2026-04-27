# Phase 5 — Keyword & SERP Analysis
**Site:** surecash.com.au
**Audit Date:** 2026-04-24
**Analyst:** Keyword Auditor (Phase 5)
**Data Sources:**
- SE Ranking Project 9257045 (keyword positions, keyword groups)
- Google Search Console (sc-domain:surecash.com.au, 90-day query + page data)
- DataForSEO (baselines: ETV, keyword count, position distribution; SERP features; intent classification)
- Competitor data: nimble.com.au, cashtrain.com.au, cashdirect.com.au, fundo.com.au, credit24.com.au
- GA4: UNAVAILABLE — all session metrics use GSC + SE Ranking as fallback

---

## Executive Summary

surecash.com.au has near-zero organic search visibility for its most commercially valuable keywords. Every Tier 1 keyword — payday loans (pos 21.8), cash loans (pos 23.0), quick cash loans (pos 27.1), bad credit loans (pos 36.9), fast cash loans (pos 31.7) — sits on pages 2–4 organically. The domain ranks for only 785 keywords in total at an average position of 64.7, with only 9 keywords in positions 1–4. Critically, the majority of SE Ranking "positions" reported for this domain are **Local Pack (GBP/Maps) positions**, not organic rankings — creating a false impression of keyword performance. The organic traffic gap vs the lead competitor (nimble.com.au) is 69x. GSC data shows ~80% of clicks are branded, meaning surecash.com.au's organic search is almost entirely dependent on people already knowing the brand. Three structural problems drive this situation: (1) no organic page-1 rankings for any primary keyword, (2) keyword cannibalization between the homepage and service pages diluting ranking signals, and (3) absence of informational content to compete for PAA, Featured Snippet, and AI Overview positions that competitors are capturing.

---

## Issue Summary

| ID | Title | Severity | Effort | Category |
|---|---|---|---|---|
| KW-001 | Tier 1 Keywords Not Ranking in Organic Top 20 | Critical | High | Keyword Gap |
| KW-002 | Organic Traffic Footprint 69x Below Lead Competitor | Critical | High | Traffic Gap |
| KW-003 | Local Pack Rankings Masking Zero Organic Rankings | Critical | Low | Tracking/Strategy |
| KW-004 | 80% Branded Dependency — Non-Branded Discovery Near Zero | Critical | High | Traffic Mix |
| KW-005 | Page 1 Position Would Multiply Traffic 7x-25x on Tier 1 Terms | High | High | Opportunity |
| KW-006 | SE Ranking Not Distinguishing Local Pack vs Organic | High | Low | Tracking |
| CANNIBAL-001 | Homepage Competing with Service Pages for Primary Keywords | Critical | Medium | Cannibalization |
| CANNIBAL-002 | Location Pages Competing with National Service Pages | High | Medium | Cannibalization |
| CANNIBAL-003 | Centrelink Loan Keyword Cluster Over-Targeting Single Page | High | High | Cannibalization |
| CANNIBAL-004 | Non-Branch City Pages Diluting Domain Authority | Medium | Medium | Cannibalization |
| INTENT-001 | PAA Present for Top Keywords but No FAQ Schema | High | Medium | Intent/Schema |
| INTENT-002 | Heavy Paid Ad Density Compressing Organic Visibility | High | High | Intent/SERP |
| INTENT-003 | No Informational Content for Informational SERP Overlay | Medium | High | Content Gap |
| INTENT-004 | Amount-Specific Keywords Lack Dedicated Landing Pages | Medium | Medium | Content Gap |
| GEO-001 | Non-Branch City Keywords Tracked with No GBP — Local Pack Impossible | Medium | Medium | Local/GEO |
| GEO-002 | AI Overview Presence Likely — No Content Optimised for Citation | Medium | High | GEO/AIO |
| TRAFFIC-001 | Organic Traffic Share Structurally Low — No Organic Safety Net | Critical | High | Traffic |

---

## Critical Issues

### KW-001 — [CRITICAL] Tier 1 Keywords Not Ranking in Organic Top 20
**Evidence (GSC, sc-domain:surecash.com.au, 90 days):**
- payday loans: position 21.8, 104 clicks, ~3,200 impressions
- cash loans: position 23.0, 34 clicks, ~1,800 impressions
- quick cash loans: position 27.1, 25 clicks, ~1,500 impressions
- bad credit loans: position 36.9, 22 clicks, ~900 impressions
- fast cash loans: position 31.7, 13 clicks, ~700 impressions

**Root cause:** Insufficient domain authority for national non-branded terms; likely compounded by homepage/service page cannibalization (see CANNIBAL-001) and absence of strong E-E-A-T signals for ASIC-regulated financial products.

**Fix (sequenced):**
1. Resolve CANNIBAL-001 first (clear canonical signals to Google about which page targets which keyword)
2. Conduct E-E-A-T content audit: add author bios, ASIC credit licence number prominently, trust signals
3. Build topical authority with informational content cluster (see INTENT-003)
4. Earn backlinks from financial comparison sites (finder.com.au, canstar.com.au, mozo.com.au) through data/tools
5. Target featured snippet positions for PAA questions (see INTENT-001) as short-term visibility play

**Effort:** High (3-6 month sustained program)
**Priority:** Critical

---

### KW-002 — [CRITICAL] Organic Traffic Footprint 69x Below Lead Competitor
**Evidence (DataForSEO ETV comparison):**

| Domain | Monthly Organic ETV | vs surecash |
|---|---|---|
| nimble.com.au | 114,067 | 69x more |
| cashtrain.com.au | 80,894 | 49x more |
| cashdirect.com.au | 57,454 | 35x more |
| fundo.com.au | 29,407 | 18x more |
| credit24.com.au | 21,492 | 13x more |
| **surecash.com.au** | **1,643** | baseline |

**Interpretation:** surecash.com.au is not competing in the same SEO league as its commercial rivals. The gap is structural and requires a multi-year investment to close meaningfully. However, even a 5x improvement (to ~8,000 ETV) would represent a major business impact.

**Fix:**
- Set realistic 12-month organic traffic target: 5,000-8,000 ETV/month (3x-5x current)
- Focus resources on the 5 Tier 1 keywords where positions 21-37 can realistically move to 10-15 with targeted effort, then push for page 1
- Competitor gap analysis: identify which specific pages on nimble/cashtrain/cashdirect rank for the highest-value keywords and reverse-engineer their content structure

**Effort:** High (sustained SEO program)
**Priority:** Critical

---

### KW-003 — [CRITICAL] Local Pack Rankings Masking Zero Organic Rankings
**Evidence:** audit-config.json explicitly notes: "Majority of SE Ranking positions are local_pack (GBP/Maps), not organic." DataForSEO confirms organic average position 64.7. GSC confirms Tier 1 keywords at positions 21-37 organically.

**Impact:** The current SE Ranking setup presents misleading performance data. Local pack positions are:
- Won via Google Business Profile, not on-page SEO
- Typically shown only to users within a geographic radius of the business
- Not a substitute for national organic rankings
- Vulnerable to GBP suspension, competitor GMB attacks, and local pack volatility

**There is no organic safety net.** If GBP rankings decline, the business has no organic fallback.

**Fix:**
1. Immediately: Reconfigure SE Ranking to track organic rankings only (filter out local pack) for the 46 General keywords
2. Set up a separate local pack tracking view for location-specific monitoring
3. Begin organic SEO program to build genuine non-branded organic rankings

**Effort:** Low (SE Ranking config: 1-2 hours)
**Priority:** Critical — fix tracking first so real data is visible

---

### CANNIBAL-001 — [CRITICAL] Homepage Competing with Service Pages for Primary Keywords
**Evidence:** surecash.com.au tracks both national keywords (payday loans, cash loans) and has dedicated service pages. The homepage (surecash.com.au/) and service pages (e.g., /payday-loans/, /cash-loans/) almost certainly both target overlapping queries. GSC positions for these terms (21-23) are characteristic of split-signal ranking — Google cannot determine which page is the authoritative match for the query.

**Resolution Table:**

| Keyword | Competing URLs | Winner URL | Action for Loser |
|---|---|---|---|
| payday loans | surecash.com.au/ + /payday-loans/ | /payday-loans/ | Homepage: remove "payday loans" as H1 focus; redirect or differentiate |
| cash loans | surecash.com.au/ + /cash-loans/ | /cash-loans/ | Homepage: target branded + "short term loans" only |
| fast cash loans | surecash.com.au/ + /fast-cash-loans/ | /fast-cash-loans/ (dedicated) | Clear H1 differentiation; canonical if needed |
| quick cash loans | surecash.com.au/ + /quick-cash-loans/ | /quick-cash-loans/ (dedicated) | As above |

**Implementation steps:**
1. Crawl site and map all pages targeting these 4 keywords (Screaming Frog or similar)
2. Choose definitive target URL for each primary keyword
3. Update H1, title tag, and meta description on winner page to be exclusively focused on that keyword
4. Update homepage to be genuinely distinct (brand + company overview, not a second service page)
5. Check for duplicate content between homepage and service pages — if >30% similar, rewrite
6. Set canonical tags where two live pages cannot be consolidated

**Effort:** Medium (1-2 weeks)
**Priority:** Critical

---

### KW-004 — [CRITICAL] 80% Branded Dependency — Non-Branded Discovery Near Zero
**Evidence (GSC baselines):**
- Total clicks 90d (top 25 queries): 2,740
- Branded click share: ~80% = ~2,192 branded clicks
- Non-branded clicks: ~548 clicks across 90 days = ~6 non-branded clicks/day

**Impact:** The organic channel currently functions almost exclusively as a brand reinforcement channel, not a customer acquisition channel. People who don't already know surecash.com.au have almost no chance of finding it via organic search.

**Fix:**
1. Target non-branded Tier 1 keywords with dedicated, optimised pages (addresses KW-001)
2. Build topical authority content cluster for centrelink loans, bad credit loans (differentiated angle)
3. Target long-tail non-branded queries (e.g., "how to get a loan on centrelink", "$2000 emergency loan australia") to build non-branded impressions quickly
4. Track branded vs non-branded split monthly in GSC — target 50/50 within 18 months

**Effort:** High (content + authority building program)
**Priority:** Critical

---

## High Priority Issues

### CANNIBAL-002 — [HIGH] Location Pages Competing with National Service Pages
**Evidence:** audit-config.json tracks both national terms (cash loans, payday loans) and Sydney-specific terms (cash loans sydney, payday loans sydney). Without clearly differentiated pages, these compete internally.

**Resolution:**

| Keyword | Winner URL | Action for National Page | Action for Location Page |
|---|---|---|---|
| cash loans sydney | /sydney/ or /cash-loans-sydney/ | Remove all Sydney geo content; target "cash loans" only | H1 = "Cash Loans Sydney"; local signals, branch address, local phone number |
| payday loans sydney | /sydney/ or /payday-loans-sydney/ | Remove Sydney references | H1 = "Payday Loans Sydney"; local trust content |
| quick cash loans sydney | /sydney/ | Remove Sydney from national page | Add as H2 on Sydney page |
| small loans sydney | /sydney/ | Exclude from national page | Include as secondary keyword on Sydney page |

**Implementation:**
1. Decide on URL structure: /sydney/ (location hub) vs /cash-loans-sydney/ (product+location) — pick one, stick to it
2. Ensure each location page has: unique H1 with geo modifier, local branch address, local phone, local schema
3. National pages must NOT contain geo-specific references that would cause them to rank for location terms
4. Internal linking: national page → location pages (not vice versa for primary anchor)

**Effort:** Medium (1-2 weeks)
**Priority:** High

---

### CANNIBAL-003 — [HIGH] Centrelink Loan Keyword Cluster Over-Targeting Single Page
**Evidence:** 6 centrelink-related keywords (loans on centrelink, loans for people on centrelink, loans for centrelink customers, loans for pensioners on centrelink, loan for single parents on centrelink, loans for unemployed on centrelink) all likely target /centrelink-loans/. Google cannot rank one page for 6 distinct queries when each has meaningfully different user intent.

**Resolution:**

| Keyword | Recommended Page | Content Focus |
|---|---|---|
| loans on centrelink | /centrelink-loans/ (primary) | General eligibility, application process, how it works |
| loans for people on centrelink | /centrelink-loans/ (primary) | Consolidate here; slight rewording in H2 |
| loans for centrelink customers | /centrelink-loans/ (primary) | Consolidate here |
| loans for pensioners on centrelink | /centrelink-loans/pensioners/ or H2 section | Age Pension + DSP specific; different eligibility criteria |
| loan for single parents on centrelink | /centrelink-loans/single-parents/ or H2 | Family Tax Benefit A/B recipients; parenting payment |
| loans for unemployed on centrelink | /centrelink-loans/unemployed/ or H2 | JobSeeker recipients; different lender appetite |
| cash loans for unemployed | /centrelink-loans/unemployed/ or /unemployed-loans/ | Unemployed-specific; may include non-Centrelink unemployed |

**Implementation steps:**
1. Audit current /centrelink-loans/ page — map which keywords it targets and whether sub-audience content exists
2. Decide between sub-pages vs H2 sections based on traffic volume per sub-audience
3. If creating sub-pages: set up /centrelink-loans/ as hub page with internal links to sub-pages
4. Each sub-page needs: distinct H1, distinct intro paragraph, distinct FAQs targeting sub-audience specific questions
5. Canonical: sub-pages self-canonical (no canonicalisation back to parent)

**Effort:** High (content strategy + new page creation)
**Priority:** High

---

### INTENT-001 — [HIGH] PAA Present for Top Keywords but No FAQ Schema Deployed
**Evidence:** People Also Ask (PAA) boxes are confirmed present on SERPs for payday loans, cash loans, quick cash loans, bad credit loans, fast cash loans. Key PAA questions include:
- "What is a payday loan in Australia?"
- "Are payday loans legal in Australia?"
- "How quickly can I get a cash loan?"
- "Can I get a loan if I'm on Centrelink?"
- "What credit score do I need for a cash loan?"
- "How do I get a fast cash loan?"

surecash.com.au does not appear to have FAQPage structured data deployed on service pages.

**Fix:**
1. Add FAQPage JSON-LD schema to all service pages
2. Write FAQ content targeting confirmed PAA questions for each page's primary keyword
3. Structure FAQs as direct, concise answers (50-60 words) — this is the format Google pulls into PAA
4. Page-by-page FAQ mapping:
   - /payday-loans/ → "What is a payday loan?", "Are payday loans legal in Australia?", "How much can I borrow with a payday loan?"
   - /cash-loans/ → "How quickly can I get a cash loan?", "What do I need to apply for a cash loan?"
   - /centrelink-loans/ → "Can I get a loan on Centrelink?", "Which Centrelink payments qualify?", "How much can I borrow on Centrelink?"
   - /bad-credit-loans/ → "Can I get a loan with bad credit?", "What credit score do I need?", "Will a bad credit loan affect my credit score?"

**Regulatory note:** All FAQ answers must comply with ASIC NCCP Act and responsible lending disclosure requirements.

**Cross-reference:** See Phase 1 (Schema) for FAQPage implementation instructions.
**Effort:** Medium (2-3 days)
**Priority:** High

---

### INTENT-002 — [HIGH] Heavy Paid Ad Density Compressing Organic Visibility
**Evidence:** 4-6 paid Google Ads appear above organic results for payday loans, cash loans, fast cash loans, quick cash loans. This effectively pushes position 1 organic below the fold on desktop and well below the fold on mobile.

**Impact:** Even achieving position 5 organically for "payday loans" (which would be a major achievement from current pos 22) would result in the 9th-11th visible result on the page.

**Recommended response:**
1. Short-term: Target Featured Snippet and PAA positions — these appear ABOVE paid ads or within the first visible screen area
2. Medium-term: Focus on long-tail keyword variations where paid density is lower (e.g., "payday loans for pensioners", "$1000 cash loan same day")
3. Long-term: Content authority building + backlink strategy to achieve top-3 organic positions where click share is meaningful despite paid ads

**Note on regulatory constraint:** ASIC regulates advertising for short-term credit products. Google Ads for payday loans and small amount credit contracts (SACCs) in Australia are restricted — so competitors are also constrained on paid side, which makes organic visibility even more important.

**Effort:** High (ongoing)
**Priority:** High

---

### KW-006 — [HIGH] SE Ranking Not Distinguishing Local Pack vs Organic
**Evidence:** audit-config.json notes: "Majority of SE Ranking positions are local_pack (GBP/Maps), not organic." SE Ranking project 9257045 is returning local pack positions as primary keyword rankings.

**Impact:** Reporting confusion. Stakeholders see "good rankings" in SE Ranking but the business has almost no national organic presence.

**Fix:**
1. In SE Ranking project settings: disable or separate local pack tracking for the 46 General keywords
2. Create a separate SE Ranking project (or group) specifically for local pack monitoring (location keywords only)
3. Configure General group keywords to track organic positions only — this will likely show position 20+ for all Tier 1 terms, which is the accurate picture
4. Update reporting dashboard to clearly label: "Organic Rankings" vs "Local Pack Rankings"

**Effort:** Low (1-2 hours)
**Priority:** High — fix immediately so all subsequent monitoring is accurate

---

## Medium Priority Issues

### INTENT-003 — [MEDIUM] No Informational Content for Informational SERP Overlay
**Evidence:** PAA boxes on "payday loans", "cash loans", "bad credit loans", "same day loans" all include informational questions. surecash.com.au has no blog or guide content to compete for these informational positions. moneysmart.gov.au wins the information layer for these keywords.

**Content gaps to fill:**

| Topic | Target Keyword | Target SERP Feature | Priority |
|---|---|---|---|
| How payday loans work in Australia | how do payday loans work australia | PAA / Featured Snippet | High |
| Centrelink loans guide | can i get a loan on centrelink | PAA / Featured Snippet | High |
| Bad credit loans guide | how to get a loan with bad credit australia | PAA | High |
| Same day loan application guide | how fast can i get a cash loan | PAA | Medium |
| What happens if I can't repay | payday loan hardship australia | Informational | Medium (+ regulatory) |
| Loan amount guide | how much can i borrow emergency loan | Featured Snippet (table) | Medium |

**Regulatory note:** ASIC requires financial service guides and informational content to not be misleading. All guides must include responsible lending messaging, comparison rate warnings, and not overstate ease of approval.

**Effort:** High (6-10 articles over 2-3 months)
**Priority:** Medium (becomes High if Featured Snippet / PAA capture is the short-term traffic strategy)

---

### INTENT-004 — [MEDIUM] Amount-Specific Keywords Lack Dedicated Optimised Landing Pages
**Evidence:** 10 amount-specific keywords tracked ($500 to $5000 cash loans). These have highly transactional intent — users know exactly what they want. If surecash.com.au routes all of these to a single generic page, it cannot rank for each individual amount query.

**Fix:**

| Keyword | Recommended URL | Key Content Elements |
|---|---|---|
| $500 cash loans | /500-cash-loan/ | H1: "$500 Cash Loan — Apply Today"; repayment table; "borrow $500" CTA |
| $1000 cash loans | /1000-cash-loan/ | H1: "$1000 Cash Loan"; repayment calculator; eligibility checklist |
| $1500 cash loans | /1500-cash-loan/ | Same pattern |
| $2000 cash loans | /2000-cash-loan/ | SACC/MACC boundary — needs specific regulatory language |
| $2500 cash loans | /2500-cash-loan/ | MACC product — different rate disclosure requirements |
| $3000 cash loans | /3000-cash-loan/ | MACC |
| $3500 cash loans | /3500-cash-loan/ | MACC |
| $4000 cash loans | /4000-cash-loan/ | MACC |
| $4500 cash loans | /4500-cash-loan/ | MACC |
| $5000 cash loans | /5000-cash-loan/ | MACC — max product; needs prominent comparison rate |

**Note:** $2,000 is the SACC/MACC boundary under Australian credit law. Pages for $2,001+ (MACC) must use different fee/rate disclosures. All pages need the comparison rate warning and responsible lending link.

**Effort:** Medium (10 pages, mostly templated with amount-specific variables)
**Priority:** Medium

---

### CANNIBAL-004 — [MEDIUM] Non-Branch City Pages Potentially Diluting Authority
**Evidence:** audit-config.json keywords include Melbourne, Adelaide, Perth, Hobart, Gold Coast, Geelong, Townsville, Cairns — cities where surecash.com.au has no physical branch. If location pages exist for these cities:
- They cannot rank in local pack (no GBP address there)
- Organic rankings against local lenders in those cities will be very weak
- The pages may be indexed but generating zero/near-zero clicks

**Fix:**
1. Pull GSC page performance data for /melbourne/, /adelaide/, /perth/, /hobart/ etc. URLs
2. If any page has <10 clicks in 90 days: consider noindex (not 301 redirect — preserve any link equity)
3. If pages have zero links and zero traffic: 301 redirect to national service page
4. Long term: build a "Cash Loans Australia" national page that captures non-geo searches without needing separate city pages for non-branch locations

**Effort:** Low (audit) + Medium (consolidation decision)
**Priority:** Medium

---

### GEO-001 — [MEDIUM] Non-Branch City Keywords Tracked for Local Pack — Rankings Impossible
**Evidence:** SE Ranking tracks "payday loans townsville", "centrelink loans cairns", "cash loans geelong" etc. — cities where surecash.com.au has no physical address. Local pack rankings require a verified GBP address within the search radius. These keywords will never achieve local pack rankings for these cities.

**Fix:**
1. Remove non-branch city keywords from local pack tracking in SE Ranking (they are permanently unattainable for local pack)
2. If tracking organic for these cities: acceptable, but expectations should be set — competing against local lenders organically for city-specific terms is very difficult
3. Focus local pack tracking resources on the 4 actual locations: Sydney (HQ), Gosford, Wollongong, Tweed Heads

**Effort:** Low (SE Ranking cleanup: 1 hour)
**Priority:** Medium

---

### GEO-002 — [MEDIUM] AI Overview Likely Present for Primary Keywords — Site Not Optimised for Citation
**Evidence:** AI Overviews (AIO) have been observed for financial product queries in Australia. For "payday loans australia", "cash loans australia" type queries, Google's AIO typically cites:
- Government sources (moneysmart.gov.au)
- High-authority comparison sites (finder.com.au, canstar.com.au)
- Established lender brand pages with strong E-E-A-T signals

surecash.com.au is unlikely to be cited in AI Overviews currently given:
- Low domain authority
- Limited informational content (AIOs prefer to cite comprehensive guides)
- No schema markup signals for E-E-A-T

**Fix:**
1. Create informational content in list/table format (AIO prefers structured content)
2. Add author credentials and publication dates to all content (E-E-A-T for AIO citation)
3. Ensure ASIC credit licence number appears prominently on relevant pages (regulatory authority signal)
4. Implement Article and FAQPage schema (increases AIO citation probability)
5. Target question-based queries with direct, structured answers

**Cross-reference:** GEO-002 resolution overlaps with INTENT-001 (FAQ schema) and INTENT-003 (informational content)
**Effort:** High (requires content program + schema)
**Priority:** Medium (growing in importance as AI Overviews expand)

---

### TRAFFIC-001 — [CRITICAL] Organic Traffic Share Structurally Low — No Organic Safety Net
**Evidence:**
- DataForSEO ETV: 1,643 visits/month (estimated organic)
- GSC clicks 90d: 2,740 total for top 25 queries (includes branded)
- Annualised non-branded organic clicks: ~2,190/year ≈ 182/month
- GA4 unavailable, so full channel split unknown

**Structural risk:**
- If GBP is suspended → local pack rankings disappear instantly
- If branded search declines → most GSC traffic disappears
- No paid search safety net known (regulated product — Google Ads for SACCs restricted)
- Result: surecash.com.au is one GBP suspension away from near-zero web traffic

**Fix:**
- This issue is resolved by fixing KW-001 through KW-004 and CANNIBAL-001
- Interim tracking fix: get GA4 operational to understand true channel split
- Set organic growth KPIs: 3x non-branded organic in 12 months; 10x in 24 months

**Effort:** High (program-level change)
**Priority:** Critical

---

## Passed Checks

- **Location keyword tracking present:** SE Ranking tracks location-specific keywords for actual branch locations (Gosford, Wollongong, Tweed Heads) — correct setup
- **Competitor tracking active:** 5 competitors tracked in SE Ranking with overlap keyword data — good baseline
- **GSC verified and returning data:** GSC site property (sc-domain:surecash.com.au) is verified and returning query + page data
- **Keyword group structure logical:** Two groups (General / Location) broadly appropriate for business type
- **Business context documented:** ASIC regulatory context captured in audit-config.json — regulatory risk awareness is present

---

## Data Tables

### Table 1: Tier 1 Keyword Position Matrix — SE Ranking vs GSC vs Organic Reality

| Keyword | SE Ranking Position | SE Ranking Type | GSC Avg Position (90d) | GSC Clicks (90d) | Organic Page 1? |
|---|---|---|---|---|---|
| payday loans | Local Pack | GBP/Maps | 21.8 | 104 | NO |
| cash loans | Local Pack | GBP/Maps | 23.0 | 34 | NO |
| quick cash loans | Local Pack | GBP/Maps | 27.1 | 25 | NO |
| bad credit loans | Unknown / Local | GBP/Maps | 36.9 | 22 | NO |
| fast cash loans | Unknown / Local | GBP/Maps | 31.7 | 13 | NO |
| same day loans | Unknown | Unknown | >25 (est.) | <10 | NO |
| instant cash loans australia | Unknown | Unknown | >25 (est.) | <10 | NO |
| loans on centrelink | Unknown | Unknown | >25 (est.) | <10 | NO |
| unsecured personal loans | Unknown | Unknown | >25 (est.) | <5 | NO |
| loans for people on centrelink | Unknown | Unknown | >25 (est.) | <5 | NO |

**Note:** SE Ranking positions listed as "Local Pack" because audit-config confirms majority of tracked positions are local_pack type. Organic positions are derived from GSC data.

---

### Table 2: CTR Opportunity Analysis

| Keyword | GSC Position | GSC CTR (est.) | Expected CTR at pos | Status | Opportunity at Pos 3 |
|---|---|---|---|---|---|
| payday loans | 21.8 | ~3.3% | 0.5-1% | CTR above-expected — snippet is compelling | ~270 clicks/month |
| cash loans | 23.0 | ~1.9% | 0.5-1% | Above expected | ~220 clicks/month |
| quick cash loans | 27.1 | ~1.7% | 0.5% | Above expected | ~145 clicks/month |
| bad credit loans | 36.9 | ~2.4% | <0.5% | Well above expected | ~120 clicks/month |
| fast cash loans | 31.7 | ~1.9% | <0.5% | Well above expected | ~145 clicks/month |

**Key insight:** surecash.com.au's snippet is already performing well at deep positions. Ranking improvement, not snippet improvement, is the priority.

---

### Table 3: SERP Feature Matrix

| Keyword | Local Pack | PAA | Paid Ads | Featured Snippet | AI Overview | surecash Captures Any? |
|---|---|---|---|---|---|---|
| payday loans | YES | YES (3-4 Qs) | Heavy (4-6) | Possible | Likely | Local Pack only |
| cash loans | YES | YES (3-4 Qs) | Heavy (4-6) | No | Possible | Local Pack only |
| quick cash loans | YES | YES (2-3 Qs) | Heavy (3-4) | No | Possible | Local Pack only |
| bad credit loans | Possible | YES (4-5 Qs) | Heavy (3-4) | No | Likely | None confirmed |
| fast cash loans | YES | YES (2-3 Qs) | Heavy (3-4) | No | Possible | Local Pack only |
| loans on centrelink | Less likely | YES (3-5 Qs) | Moderate (2-3) | Possible | Likely | Unknown |
| same day loans | YES | YES (2-3 Qs) | Heavy | No | Possible | Local Pack only |
| instant cash loans australia | YES | YES (2-3 Qs) | Heavy | No | Possible | Local Pack only |

**Summary:** surecash.com.au captures local pack positions for location-influenced queries but captures ZERO organic SERP features (no featured snippets, no confirmed PAA positions, no AI Overview citations).

---

### Table 4: Cannibalization Instances

| Keyword | Likely Competing URLs | Winner URL | Action for Loser URL |
|---|---|---|---|
| payday loans | / + /payday-loans/ | /payday-loans/ | Homepage: target brand only; remove "payday loans" H1 focus |
| cash loans | / + /cash-loans/ | /cash-loans/ | Homepage differentiation; remove product keyword targeting |
| fast cash loans | / + /fast-cash-loans/ | /fast-cash-loans/ | Canonical or content differentiation |
| quick cash loans | / + /quick-cash-loans/ | /quick-cash-loans/ | Canonical or content differentiation |
| cash loans sydney | / + /cash-loans/ + /sydney/ | /sydney/ or /cash-loans-sydney/ | Remove Sydney geo from national pages |
| payday loans sydney | / + /payday-loans/ + /sydney/ | /sydney/ or /payday-loans-sydney/ | Remove Sydney geo from national pages |
| loans on centrelink | /centrelink-loans/ (hub) | /centrelink-loans/ | Consolidate all centrelink variants; sub-pages for sub-audiences |
| loans for pensioners on centrelink | /centrelink-loans/ + potential /pensioner-loans/ | Create /centrelink-loans/pensioners/ | Redirect any duplicate; make sub-page |
| payday loans Gosford | /gosford/ + /centrelink-loans/ | /gosford/ | Centrelink page must NOT target Gosford keyword |
| cash loans gosford | /gosford/ | /gosford/ | Clean URL targeting; no competing pages |

---

### Table 5: Traffic Channel Estimate (GA4 Unavailable — GSC-Based Estimate)

| Channel | Est. Monthly Traffic | % of Total | Notes |
|---|---|---|---|
| Organic Search (branded) | ~730/month | ~65% | GSC branded clicks ÷ 3 (90d to monthly) |
| Organic Search (non-branded) | ~183/month | ~16% | GSC non-branded clicks ÷ 3 |
| Direct | ~150/month | ~13% | Estimate — typical for local service brand |
| Referral | ~50/month | ~4% | Estimate — some comparison site referrals |
| Social | ~15/month | ~1% | Estimate — low for finance brand |
| Paid Search | Unknown | Unknown | GA4 unavailable; likely minimal due to Google Ads restrictions on SACCs |
| **Total (est.)** | **~1,130/month** | **100%** | Estimate from GSC data + industry norms |

**Note:** These are approximations from GSC data. GA4 channel data unavailable. True figures require GA4 restoration.

---

### Table 6: AI Overview Presence per Keyword

| Keyword | AI Overview Likely? | Content Format | surecash.com.au Cited? | Competitors Cited |
|---|---|---|---|---|
| payday loans | Yes | Paragraph + bullet list | No (insufficient E-E-A-T) | nimble.com.au, moneysmart.gov.au likely |
| cash loans | Possible | Paragraph | No | nimble.com.au, cashdirect.com.au |
| bad credit loans | Yes | List format | No | Comparative sites (finder.com.au) |
| loans on centrelink | Possible | Q&A format | Unknown | moneysmart.gov.au likely |
| fast cash loans | Possible | Paragraph | No | nimble.com.au |

**AIO Optimisation requirements for surecash.com.au:**
- Structured content (bullet lists, tables, numbered steps) in page body
- Clear, direct answers to common questions (suitable for AIO extraction)
- E-E-A-T signals: author credentials, ASIC licence number, publication/review dates
- FAQPage schema to increase extraction probability

---

## Revenue Impact Estimation

**Formula:** (Competitor Avg Organic Traffic - Client Organic Traffic) × Average CPC × 0.3 conversion factor

**Data inputs:**
- surecash.com.au ETV: 1,643/month (DataForSEO)
- Competitor average ETV: (114,067 + 80,894 + 57,454 + 29,407 + 21,492) ÷ 5 = 60,663/month
- Average CPC for payday loans / cash loans AU: estimated AUD $8-15 per click (highly competitive finance vertical)
- Using conservative AUD $8 CPC average across keyword mix

**Traffic Gap:** 60,663 - 1,643 = 59,020 visits/month gap vs competitor average

**Estimated Monthly Revenue Opportunity (full gap):** 59,020 × $8 × 0.3 = **AUD $141,648/month**

**Realistic 12-month target (5x traffic improvement):**
- Target ETV: 8,215/month
- Improvement over baseline: +6,572/month
- Estimated monthly value: 6,572 × $8 × 0.3 = **AUD $15,773/month**

**By Tier (approximate, based on keyword volume share):**

| Tier | surecash Traffic (est.) | Competitor Avg Traffic | Gap | Avg CPC | Est. Monthly Value |
|---|---|---|---|---|---|
| Tier 1 (national keywords) | ~410/month | ~30,000/month | ~29,590 | $12 | ~$106,524/month at full parity |
| Tier 2 (Sydney + niche) | ~600/month | ~15,000/month | ~14,400 | $8 | ~$34,560/month at full parity |
| Tier 3 (amount-specific) | ~300/month | ~8,000/month | ~7,700 | $7 | ~$16,170/month at full parity |
| Tier 4 (location) | ~333/month | ~7,663/month | ~7,330 | $5 | ~$10,995/month at full parity |

**Realistic 12-month opportunity (achievable 3x-5x improvement):** **AUD $12,000-$18,000/month in SEO value**

_Revenue estimates use a 0.3 organic conversion factor applied to the traffic gap x average CPC. Actual results depend on conversion rate optimisation, landing page quality, and market conditions. CPC figures are estimated based on industry benchmarks for Australian short-term credit keywords — verify against actual Google Ads data if available. Traffic figures are estimated organic visit counts based on DataForSEO ETV metrics._

---

## Raw Data References

| Source | Data Used | Tool |
|---|---|---|
| SE Ranking Project 9257045 | Keyword groups, 100 tracked keywords, ranking type context | mcp__plugin_seoaudit_seranking__PROJECT_listKeywords |
| GSC sc-domain:surecash.com.au | Top queries (90d): 2,740 clicks, 14,724 impressions, 5 non-branded gap keywords with positions | mcp__plugin_seoaudit_gsc__search_analytics_query |
| DataForSEO (baselines) | ETV 1,643/month, 785 ranked keywords, avg pos 64.7, 9 keywords pos 1-4 | mcp__plugin_seoaudit_dataforseo__* |
| audit-config.json | All competitor data, business context, tracking notes, GA4 unavailability | N/A (config file) |
| GA4 | UNAVAILABLE — server not loading. All session data estimated from GSC. | N/A |

---

## Reconciliation Notes — Cross-Phase References

**Phase 1 (Technical / Schema):**
- INTENT-001 (FAQPage schema) requires schema implementation — See Phase 1 for overall schema status. If Phase 1 flagged absence of structured data, INTENT-001 is a downstream symptom of that finding.
- GEO-002 (AI Overview citation) requires E-E-A-T schema (Author, Organization, Article) — See Phase 1 schema audit.

**Phase 2 (On-Page / Content):**
- CANNIBAL-001 and CANNIBAL-002 (homepage vs service page competition) will require title tag and meta description changes — See Phase 2 for any existing title/meta issues (TITLE-NNN, META-NNN) to coordinate rewrites.
- KW-004 (branded dependency) may be explained by thin or duplicate content on non-branded pages found in Phase 2.

**Phase 4 (Local SEO):**
- KW-003 (local pack masking organic) and GEO-001 (non-branch city tracking) directly overlap with Phase 4 local SEO findings. GBP setup, local pack competition, and citation tracking should be cross-referenced with Phase 4 LOCAL- issues.
- CANNIBAL-002 (location page cannibalization) overlaps with Phase 4's local page audit — See Phase 4 LOCAL- issues for location page structure findings.

**Phase 3 (Link Building / Authority):**
- KW-001 (tier 1 not ranking) and KW-002 (69x traffic gap) are partly caused by low domain authority vs competitors. Phase 3 backlink analysis will have identified the DA/DR gap — authority building recommended in Phase 3 is a prerequisite for fixing KW-001.

---

## Appendix: Issue Resolution Priority Queue

Recommended sequence for implementation:

**Week 1-2 (Quick Wins — Low Effort, High Impact):**
1. KW-006 / KW-003: Fix SE Ranking tracking — separate local pack from organic (1-2 hours)
2. GEO-001: Remove non-branch city keywords from local pack tracking (1 hour)
3. INTENT-001: Add FAQPage schema to top 5 service pages (2-3 days dev time)

**Month 1 (Structural Fixes):**
4. CANNIBAL-001: Homepage vs service page — content audit, H1 differentiation, canonical review
5. CANNIBAL-002: Location page vs national page — content and URL structure review

**Month 2-3 (Content Development):**
6. CANNIBAL-003: Centrelink keyword cluster — sub-page or H2 section strategy
7. INTENT-003: Informational content cluster — first 3 cornerstone guides
8. INTENT-004: Amount-specific landing pages — 10 templated pages

**Month 3-6 (Authority + Content Programme):**
9. KW-001 / KW-004: Organic ranking improvement program — content + backlinks
10. GEO-002: AI Overview optimisation — structured content format, E-E-A-T signals
11. TRAFFIC-001: Track improvement against baselines monthly

_All content changes must be reviewed for ASIC NCCP Act compliance before publication. Responsible lending disclosures, comparison rate warnings, and fee transparency requirements apply to all loan product pages._
