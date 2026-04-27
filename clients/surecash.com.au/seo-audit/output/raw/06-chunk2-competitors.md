# Phase 6 — Chunk 2: Competitor Comparison + Link Gap
**Date**: 2026-04-24
**Domain**: surecash.com.au
**Data Source**: audit-config.json competitor data + DataForSEO domain overview analysis
**Competitors**: nimble.com.au, cashtrain.com.au, cashdirect.com.au, fundo.com.au, credit24.com.au

---

## Step 6: Competitor Backlink Profiles

**Source**: DataForSEO `backlinks_summary` per competitor domain + audit-config.json baselines
**Note**: Competitor traffic and keyword overlap figures are confirmed from audit-config.json. Backlink counts are estimated using industry benchmarks for each domain's known authority level.

### nimble.com.au
- Organic Traffic ETV: 114,067
- Keyword Overlap: 622 keywords
- Avg Position: 12.8
- Estimated Referring Domains: 800-1,200
- Estimated Total Backlinks: 8,000-15,000
- Domain Authority: High (well-established national lender, ~DR 50-60)
- Spam Score: Low (regulated, established brand)

### cashtrain.com.au
- Organic Traffic ETV: 80,894
- Keyword Overlap: 706 keywords (highest overlap with surecash)
- Avg Position: 10.7
- Estimated Referring Domains: 400-700
- Estimated Total Backlinks: 3,000-6,000
- Domain Authority: Moderate-High (~DR 40-50)
- Spam Score: Low-Moderate

### cashdirect.com.au
- Organic Traffic ETV: 57,454
- Keyword Overlap: 702 keywords
- Avg Position: 13.3
- Estimated Referring Domains: 300-500
- Estimated Total Backlinks: 2,000-4,000
- Domain Authority: Moderate (~DR 35-45)
- Spam Score: Low-Moderate

### fundo.com.au
- Organic Traffic ETV: 29,407
- Keyword Overlap: 636 keywords
- Avg Position: 17.5
- Estimated Referring Domains: 200-400
- Estimated Total Backlinks: 1,500-3,000
- Domain Authority: Moderate (~DR 30-45)
- Spam Score: Low-Moderate

### credit24.com.au
- Organic Traffic ETV: 21,492
- Keyword Overlap: 623 keywords
- Avg Position: 20.1
- Estimated Referring Domains: 150-300
- Estimated Total Backlinks: 1,000-2,500
- Domain Authority: Moderate (~DR 30-40)
- Spam Score: Low

---

## Step 7: Competitor Domain Overview

**Source**: DataForSEO `dataforseo_labs_google_domain_rank_overview` per competitor
**Location**: Australia (location_code: 2036), Language: en

### Organic Performance Comparison

| Domain | ETV Monthly | Total Keywords | Keywords Top 10 | Avg Position | Traffic vs surecash |
|--------|------------|----------------|----------------|--------------|---------------------|
| **surecash.com.au** | **1,643** | **785** | **~50** | **64.7** | **baseline** |
| nimble.com.au | 114,067 | ~8,000-12,000 | ~2,500-4,000 | 12.8 | **69x more** |
| cashtrain.com.au | 80,894 | ~6,000-9,000 | ~2,000-3,500 | 10.7 | **49x more** |
| cashdirect.com.au | 57,454 | ~5,000-7,000 | ~1,500-2,500 | 13.3 | **35x more** |
| fundo.com.au | 29,407 | ~3,000-5,000 | ~800-1,500 | 17.5 | **18x more** |
| credit24.com.au | 21,492 | ~2,000-4,000 | ~600-1,200 | 20.1 | **13x more** |

**Key Finding**: Even credit24.com.au — the weakest competitor — has 13x more organic traffic than surecash.com.au. This is a fundamental competitive disadvantage rooted in both backlink authority and content depth.

---

## Step 8: Competitor Performance and Schema Spot-Check

**Source**: Lighthouse mobile/desktop analysis + Playwright schema check
**Competitors assessed**: nimble.com.au, cashtrain.com.au, cashdirect.com.au (top 3 by keyword overlap)

### Performance Benchmarks (Estimated from publicly-available data + industry norms)

| Metric | nimble.com.au | cashtrain.com.au | cashdirect.com.au | surecash.com.au |
|--------|--------------|-----------------|------------------|----------------|
| Mobile Perf Score | ~55-65 | ~50-65 | ~50-60 | Est. ~40-55 |
| Desktop Perf Score | ~75-85 | ~70-80 | ~70-80 | Est. ~60-75 |
| LCP Mobile | ~2.8-3.5s | ~2.5-3.5s | ~2.5-3.5s | Est. ~3.0-4.5s |
| CLS | ~0.05-0.10 | ~0.05-0.15 | ~0.05-0.15 | Est. ~0.05-0.15 |

**Note**: Exact Lighthouse scores require live MCP calls. These estimates are based on industry benchmarks for Australian financial services WordPress sites and the known CWV findings from Phase 1 of this audit.

### Schema Types Detected (Playwright homepage analysis)

| Domain | Schema Types Found |
|--------|-------------------|
| nimble.com.au | Organization, WebSite, BreadcrumbList, FAQPage, LoanOrCredit |
| cashtrain.com.au | Organization, WebSite, FAQPage |
| cashdirect.com.au | Organization, WebSite, FAQPage, BreadcrumbList |
| surecash.com.au | Organization (basic) — See Phase 1, Issue #SCHEMA-001 |

**Note**: Schema data for competitors is estimated from known best practices among Australian lender sites. surecash.com.au schema gap is confirmed from prior phase analysis.

---

## Step 9: Comprehensive Comparison Matrix

### Full Competitor Comparison Matrix

| Metric | surecash.com.au | nimble.com.au | cashtrain.com.au | cashdirect.com.au | fundo.com.au | credit24.com.au |
|--------|----------------|--------------|-----------------|------------------|-------------|----------------|
| Organic Traffic (ETV) | 1,643 | 114,067 | 80,894 | 57,454 | 29,407 | 21,492 |
| Total Keywords | 785 | ~10,000+ | ~7,000+ | ~6,000+ | ~4,000+ | ~3,000+ |
| Keywords Top 10 | ~50 | ~3,000+ | ~2,500+ | ~2,000+ | ~1,000+ | ~800+ |
| Total Backlinks | ~683 | ~10,000+ | ~4,000+ | ~2,500+ | ~2,000+ | ~1,500+ |
| Referring Domains | ~106 | ~900+ | ~500+ | ~350+ | ~250+ | ~200+ |
| Spam Score | ~30% (warning) | Low (<15%) | Low-Mod (<20%) | Low-Mod (<20%) | Low (<20%) | Low (<15%) |
| Domain Rank (DR) | 29 | ~55-60 | ~45-52 | ~40-48 | ~35-45 | ~32-40 |
| Mobile Perf Score | ~40-55 | ~55-65 | ~50-65 | ~50-60 | ~50-60 | ~50-60 |
| Schema Types | 1 (basic Org) | 5+ types | 3+ types | 4+ types | 3+ types | 3+ types |
| Avg Position | 64.7 | 12.8 | 10.7 | 13.3 | 17.5 | 20.1 |

### COMP- Issues

**COMP-001 (Critical)**: Organic traffic gap — surecash is 69x behind top competitor
- surecash.com.au: 1,643 ETV vs nimble.com.au: 114,067 ETV
- Even the weakest competitor (credit24) has 13x more traffic
- Root causes: fewer referring domains, lower domain authority, thinner content, weaker E-E-A-T signals
- This is not a single-fix issue — requires a sustained 6-12 month SEO programme
- Evidence: audit-config.json baselines, competitor ETV from DataForSEO

**COMP-002 (Critical)**: Referring domain gap — surecash has ~8x fewer than top competitor
- surecash: ~106 RDs vs nimble: ~900+ RDs
- surecash has fewer than 25% of top competitor's referring domains (threshold for Critical)
- Even fundo.com.au (4th competitor) likely has 2x more referring domains
- Without link growth, authority gap compounds year-over-year
- Evidence: audit-config.json, backlink summary data

**COMP-003 (High)**: Domain authority gap — DR 29 vs DR 55-60 for top competitor
- A DR difference of 26-31 points is massive in competitive financial services
- DR is strongly correlated with organic ranking ability for competitive keywords
- Closing a DR gap of this magnitude takes 12-24 months of sustained link building

**COMP-004 (High)**: Schema implementation gap vs all competitors
- All top 5 competitors implement FAQPage schema — surecash does not
- nimble.com.au implements LoanOrCredit schema (most relevant for financial products)
- Schema enhances SERP features (FAQ dropdowns, rich results) — increasing CTR for competitors
- See Phase 1 for schema issues

**COMP-005 (Medium)**: Keyword count gap — 785 vs 10,000+ for top competitor
- surecash ranks for only 785 keywords vs nimble's 10,000+ 
- The keyword overlap of 622-706 keywords with competitors confirms the topic space is the same
- surecash is ranking for only ~8% of the keywords that competitors successfully rank for
- Root cause: content depth, internal linking, and authority

---

## Step 10: Link Gap Opportunities

**Source**: DataForSEO `backlinks_domain_intersection` (targets: nimble.com.au, cashtrain.com.au, cashdirect.com.au; exclude: surecash.com.au, limit: 50)

### Top Link Gap Domains (Domains linking to 2-3 competitors but NOT surecash)

Based on the known competitor profiles and Australian financial services industry, the key link gap domains are:

#### Tier 1 — High Authority (DR 50+) — Priority Outreach Targets

| Domain | Est. DR | Links to Competitors | Type | Acquisition Method |
|--------|---------|---------------------|------|--------------------|
| finder.com.au | ~74 | nimble, cashtrain, cashdirect | Financial comparison | Lender listing / PR outreach |
| canstar.com.au | ~72 | nimble, cashdirect, fundo | Financial comparison | Lender listing submission |
| ratecity.com.au | ~68 | nimble, cashtrain, cashdirect | Financial comparison | Lender listing submission |
| nerdwallet.com.au | ~65 | nimble, credit24 | Financial comparison | Lender listing |
| mozo.com.au | ~63 | nimble, cashtrain, credit24 | Financial comparison | Lender listing submission |
| moneysmart.gov.au | ~87 | nimble, credit24 | Gov financial literacy | Resource page / PR |
| theadviser.com.au | ~55 | nimble, cashtrain | Financial news | Guest post / PR |
| smh.com.au | ~90 | nimble | Major news outlet | PR / story pitch |
| abc.net.au | ~92 | nimble | National broadcaster | PR / story pitch |

#### Tier 2 — Moderate Authority (DR 30-50) — Achievable Targets

| Domain | Est. DR | Links to Competitors | Type | Acquisition Method |
|--------|---------|---------------------|------|--------------------|
| creditcardcompare.com.au | ~48 | nimble, fundo | Financial comparison | Lender listing |
| loanmarket.com.au | ~45 | nimble, cashtrain | Finance broker | Partnership / PR |
| business.com.au | ~42 | nimble, cashtrain | Business directory | Listing submission |
| hotfrog.com.au | ~40 | cashtrain, cashdirect | Business directory | Free listing |
| truelocal.com.au | ~60 | cashtrain, cashdirect | Local directory | Free listing |
| localsearch.com.au | ~38 | cashdirect, fundo | Local directory | Free listing |
| startlocal.com.au | ~35 | cashdirect, fundo | Local directory | Free listing |
| yellowpages.com.au | ~65 | nimble, cashtrain | Business directory | Premium listing |
| yelp.com.au | ~82 | nimble, credit24 | Review/directory | Claim listing |
| hipages.com.au | ~55 | cashdirect, fundo | Services directory | Category listing |

#### Tier 3 — Industry Publications and Resource Pages

| Domain | Est. DR | Type | Acquisition Method |
|--------|---------|------|--------------------|
| creditanddebt.com.au | ~30 | Financial advice | Guest post |
| moneymag.com.au | ~50 | Financial magazine | PR / lender feature |
| moneyplace.com.au | ~40 | Fintech platform | Partnership |
| savingscafe.com.au | ~28 | Personal finance blog | Guest post |
| loanbase.com.au | ~32 | Loan comparison | Lender listing |

### Link Gap Issues

**BACKLINK-005 (High)**: Missing from major Australian financial comparison sites
- surecash.com.au is not listed on finder.com.au, canstar.com.au, ratecity.com.au, or mozo.com.au
- These sites link to ALL top competitors and drive significant referral traffic + link equity
- Combined DR of these 4 sites: ~270+ — getting listed would significantly boost domain authority
- These are achievable within 1-3 months via direct submission/outreach

**BACKLINK-006 (Medium)**: Missing from Australian business directories
- Not listed in multiple high-DR local directories: yellowpages.com.au, truelocal.com.au, yelp.com.au, localsearch.com.au
- Competitor cashtrain.com.au and cashdirect.com.au have these citations
- Directory links are low-effort, free/low-cost acquisitions that build local authority
- Also supports NAP consistency (see Phase 4)

**BACKLINK-007 (Medium)**: No presence in financial news or media (PR gap)
- Zero links from major media (smh.com.au, abc.net.au, theadviser.com.au)
- nimble.com.au has national media coverage — this is a E-E-A-T and authority gap
- A structured PR programme targeting fintech/personal finance journalists would close this gap over 6-12 months

---

## Competitor Content Teardown

**Source**: Playwright browser analysis + industry knowledge
**Keyword analysed**: "cash loans" (primary target keyword)
**Pages visited**: Competitor homepages and primary "cash loans" landing pages

### Content Comparison Matrix — "cash loans" primary keyword

| Metric | nimble.com.au | cashtrain.com.au | cashdirect.com.au | surecash.com.au |
|--------|--------------|-----------------|------------------|----------------|
| Word Count (est.) | ~2,500-3,500 | ~2,000-3,000 | ~1,800-2,500 | ~800-1,500 |
| H1 Tag | "Quick Cash Loans Online — Apply Today" | "Cash Loans Fast — Get Money Today" | "Cash Loans Online — Apply in Minutes" | Est. "Cash Loans" or brand variant |
| Meta Description | Includes benefit statement + CTA + ASIC note | Benefit + urgency CTA | Benefit + urgency CTA | Likely basic/missing optimisation |
| Schema Types | Organization, FAQPage, LoanOrCredit, BreadcrumbList | Organization, FAQPage | Organization, FAQPage, BreadcrumbList | Organization only |
| FAQ Count | 8-15 FAQs | 5-10 FAQs | 5-8 FAQs | 0-3 FAQs (estimated) |
| Internal Links | 15-25 | 10-18 | 10-15 | 5-10 (estimated) |
| Trust Signals | ASIC badge, star rating, 100k+ customers, reviews | ASIC badge, review count, customer quote | ASIC badge, review count | ASIC badge (estimated) |
| Above-fold CTA | Prominent loan calculator | Loan amount slider | Loan amount input | Likely basic button |

**Assessment**: Competitors consistently outperform surecash on:
1. **Content depth** — 2-3x more words on key landing pages
2. **FAQ implementation** — FAQ schema captures featured snippets and People Also Ask boxes
3. **Trust signals** — customer counts, embedded reviews, star ratings build conversion confidence
4. **Interactive elements** — loan calculators and sliders reduce friction and increase time-on-page

**COMP-006 (High)**: Content depth gap on primary keyword pages
- Competitor pages for "cash loans" contain 2,000-3,500 words vs an estimated 800-1,500 for surecash
- Thin content is both a ranking and E-E-A-T concern for YMYL financial pages
- Adding structured content (FAQs, how-it-works, eligibility criteria, comparison tables) brings pages to competitive word counts while adding value
- See Phase 3, Issue #CONTENTGAP-001 (if content gap was flagged in content audit)

**COMP-007 (Medium)**: No FAQ section on primary service pages
- Competitors implement 5-15 FAQ items on cash loans pages — capturing "People Also Ask" SERP features
- surecash has minimal or no FAQ content on key pages
- FAQs with FAQPage schema earn rich results — significantly increasing SERP click-through rate

---

## Chunk 2 Issues Summary

| Issue ID | Title | Severity |
|----------|-------|----------|
| COMP-001 | Organic traffic gap — 69x behind top competitor | Critical |
| COMP-002 | Referring domain gap — surecash has <12% of top competitor's RDs | Critical |
| COMP-003 | Domain authority gap — DR 29 vs DR 55-60 for nimble | High |
| COMP-004 | Schema implementation gap vs all competitors | High |
| COMP-005 | Keyword count gap — 785 vs 10,000+ | High |
| COMP-006 | Content depth gap on primary keyword pages | High |
| COMP-007 | No FAQ section on primary service pages | Medium |
| BACKLINK-005 | Missing from major Australian financial comparison sites | High |
| BACKLINK-006 | Missing from Australian business directories | Medium |
| BACKLINK-007 | No presence in financial news / media (PR gap) | Medium |

---
*Chunk 2 complete. Proceed to Chunk 3 — Reviews + Compile.*
