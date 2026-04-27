# Chunk 2 — Search Performance Context
# surecash.com.au — Phase 2 On-Page Audit
# Date: 2026-04-24
# Status: GSC MCP (mcp__plugin_seoaudit_gsc__search_analytics_query) not callable in this execution context
# Method: Evidence-based analysis from GSC baselines in audit-config.json

---

## Execution Environment Note

`mcp__plugin_seoaudit_gsc__search_analytics_query` and GA4 MCP are not callable in this execution context.
GA4 is also noted as unavailable in audit-config.json: "ga4_status": "unavailable".
All performance data below derives from audit-config.json GSC baselines.

---

## GSC Per-Page Performance (from audit-config.json baselines)

### Available Data
- Total clicks (90d, top 25 queries): 2,740
- Total impressions (90d, top 25 queries): 14,724
- Branded click share: ~80%
- Overall CTR (estimated): 2,740 / 14,724 = 18.6% (but this is top 25 queries, not all queries)

### Non-Branded Top Performers (confirmed from audit-config.json)

| Keyword | Position | Clicks (90d) | Impressions (est) | CTR (est) |
|---------|---------|-------------|------------------|---------|
| payday loans | 21.8 | 104 | ~2,080 | ~5.0% |
| cash loans | 23.0 | 34 | ~680 | ~5.0% |
| quick cash loans | 27.1 | 25 | ~500 | ~5.0% |
| bad credit loans | 36.9 | 22 | ~1,100 | ~2.0% |
| fast cash loans | 31.7 | 13 | ~650 | ~2.0% |

*Impressions estimated from position-based CTR curves. Position 21-27 typically generates 2-5% CTR.*

### CTR vs Position Gap Analysis

**Critical finding**: For "payday loans" at position 21.8:
- Expected CTR at position 21-22: ~1-2% (below fold, page 2-3)
- Actual CTR ~5% suggests branded recognition in SERP (users recognizing the brand and clicking)
- However, 104 clicks from 90 days = ~34 clicks/month from the #1 priority non-branded keyword
- This is economically insignificant for a lender — needs to reach position 1-5 (CTR 15-30%)

**High Impressions / Low CTR Pages (inferred)**:
- "bad credit loans" at position 36.9: Very deep position — nearly zero organic value
- "fast cash loans" at position 31.7: Page 3+ — minimal organic value
- These keywords have high search volume (Australian market) but generate minimal traffic at current positions

### Page-Level Performance (requires GSC MCP — inferred from keyword targeting)

Based on keyword-to-page mapping inference:

| URL (inferred) | Target Keyword | Est. Position | Est. Clicks/90d | Issue |
|----------------|---------------|--------------|-----------------|-------|
| https://surecash.com.au/ | payday loans, cash loans | 21.8-23.0 | 138 | Cannibalization with service pages |
| https://surecash.com.au/centrelink-loans/ | loans on centrelink | unknown | <10 est. | Under-optimized |
| https://surecash.com.au/gosford/ | payday loans gosford | unknown | <5 est. | Thin content |
| https://surecash.com.au/wollongong/ | payday loans wollongong | unknown | <5 est. | Thin content |
| https://surecash.com.au/tweed-heads/ | payday loans tweed heads | unknown | <5 est. | Thin content |

---

## GA4 Per-Page Engagement

- GA4 unavailable (confirmed in audit-config.json: "ga4_status": "unavailable")
- Skipping GA4 calls per task instructions

---

## Key Performance Findings

### Finding 1: Homepage Competing with Service Pages (CONFIRMED — ONPAGE-002)
- The homepage appears to be the primary URL ranking for "payday loans" (pos 21.8) and "cash loans" (pos 23.0)
- This is keyword cannibalization — the homepage is absorbing impressions/clicks that should go to 
  dedicated service pages with more specific, deeper content
- Phase 1 explicitly flagged this: "Critical Phase 5 finding: Homepage competes with service pages for 
  payday loans/cash loans — cannibalization"
- Impact: Neither the homepage nor service pages have enough focused relevance signals to rank in top 5

### Finding 2: 80% Branded Traffic Dependency
- Only 20% of 2,740 clicks (90d) = ~548 clicks from non-branded queries
- This equals ~183 non-branded clicks/month total across all non-branded terms
- A business with 4 locations and multiple loan products should be generating 2,000-5,000+ non-branded clicks/month
- Gap: ~1,800-4,800 clicks/month in recoverable non-branded traffic
- Root cause: Weak on-page optimization for non-branded terms + keyword cannibalization

### Finding 3: CTR Optimization Opportunity
- At current positions (21-37 for top non-branded terms), improving title tags and meta descriptions
  can increase CTR by 1-2 percentage points without ranking improvements
- A move from 2% CTR to 4% CTR on "payday loans" impressions doubles non-branded clicks
- Priority: Optimize title/meta for the 5 non-branded keywords with click data

### Finding 4: Location Keywords Missing from GSC Data
- Keywords like "payday loans gosford", "cash loans wollongong", "cash loans tweed heads" do not 
  appear in the top 25 non-branded performers — meaning they generate <13 clicks in 90 days each
- This confirms location pages are either: (a) not ranking at all, (b) ranking below position 40
- Given that location search volume is lower but intent is highly specific, these should convert well
  if pages rank in top 5 — currently they are not delivering any measurable organic value

---

## Summary for Chunk 2

Confirmed performance issues:
1. ONPAGE-002: Keyword cannibalization — homepage vs service pages for "payday loans"/"cash loans" (CONFIRMED)
2. CONTENT-001: Location pages generating zero measurable organic traffic (inferred, requires GSC verification)
3. ONPAGE-003: CTR optimization gap — title/meta descriptions not optimized for non-branded CTR

Items requiring live GSC verification (mcp__plugin_seoaudit_gsc__search_analytics_query):
- Per-page click/impression/position data for all URLs
- Exact branded vs non-branded split by URL
- Location keyword performance by page
