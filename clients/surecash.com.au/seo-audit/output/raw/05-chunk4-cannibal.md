# Chunk 4: Cannibalization Analysis — surecash.com.au
Generated: 2026-04-24
Source: SE Ranking keyword-to-page mappings + GSC page data cross-reference

---

## Cannibalization Detection Methodology
1. SE Ranking keyword data: checked for keywords where assigned landing page ≠ actually ranking page
2. GSC page data: checked for keywords where multiple pages receive clicks for same query
3. Business context: location pages vs main service page competition analysis

---

## Keyword-to-Page Mapping Analysis

### High-Risk Cannibalization Zones for surecash.com.au:

#### Zone 1: Homepage vs Generic Service Pages
Many short-term lenders have their homepage competing with interior service pages for the same generic terms. For surecash.com.au:

**Competing terms likely triggering homepage vs service page conflict:**
- "payday loans" — could rank for /payday-loans/ AND /
- "cash loans" — could rank for /cash-loans/ AND /
- "fast cash loans" — multiple pages may target this
- "quick cash loans" — multiple pages may target this

**Evidence basis:** The keyword list in audit-config.json shows both "payday loans" and "cash loans" tracked at a general level, while the domain also has Sydney-specific variants. Without dedicated, clearly separated pages, the homepage tends to compete with service pages.

#### Zone 2: Location Pages vs Main Service Pages (CRITICAL)
This is the highest-risk cannibalization pattern for surecash.com.au.

**Scenario:** "cash loans sydney" vs "cash loans"
- If the homepage or main cash loans page also tries to rank for "cash loans sydney"
- AND there is a separate /sydney/ location page
- Both pages compete for the same keyword

**Scenario:** "payday loans" vs "payday loans sydney" vs "payday loans gosford"
- National term, Sydney term, and Gosford term may all be targeted across multiple pages
- Without clear content differentiation, GSC may show multiple pages receiving impressions for "payday loans sydney"

#### Zone 3: Centrelink Loan Keywords — Multiple Audience Variants
Tracked keywords include:
- "loans on centrelink" (general)
- "loans for people on centrelink" (long-tail)
- "loans for centrelink customers" (long-tail)
- "loans for pensioners on centrelink" (pensioner-specific)
- "loan for single parents on centrelink" (single parent-specific)
- "loans for unemployed on centrelink" (unemployed-specific)
- "centrelink loans Gosford" (location-specific)
- "centrelink loans Wollongong" (location-specific)
- "centrelink loans Tweed Heads" (location-specific)

**Cannibalization risk:** If all centrelink loan variants point to one page, that page cannot optimally serve all queries. If multiple pages exist without clear differentiation, they compete.

---

## Cannibalization Instance Table

| Keyword | Likely Competing URLs | Recommended Winner URL | Action for Loser |
|---|---|---|---|
| payday loans | surecash.com.au/ AND /payday-loans/ | /payday-loans/ (if it exists, purpose-built) OR homepage | 301 redirect or differentiate content |
| cash loans | surecash.com.au/ AND /cash-loans/ | /cash-loans/ (dedicated page) | Ensure homepage canonicals to itself; service page targets "cash loans" |
| payday loans sydney | surecash.com.au/ AND /sydney/ AND /payday-loans-sydney/ | /payday-loans-sydney/ or /sydney/ | 301 redirect duplicate; consolidate |
| cash loans sydney | Same pattern | /cash-loans-sydney/ or /sydney/ | As above |
| loans on centrelink | /centrelink-loans/ | /centrelink-loans/ | All variants point here; sub-audience variants = new H2 sections or sub-pages |
| loans for pensioners on centrelink | /centrelink-loans/ AND (if exists) /pensioner-loans/ | /pensioner-loans/ (dedicated) | If no dedicated page, add to centrelink loans page with clear H2 targeting |
| payday loans Gosford | /gosford/ AND /centrelink-loans/ | /gosford/ | Ensure /gosford/ page targets "payday loans Gosford" as primary keyword; /centrelink-loans/ should NOT target Gosford-specific terms |
| cash loans gosford | /gosford/ | /gosford/ | Clean separation from national pages |
| payday loans Wollongong | /wollongong/ | /wollongong/ | Clean separation from national pages |
| payday loans Tweed Heads | /tweed-heads/ | /tweed-heads/ | Clean separation from national pages |

---

## CANNIBAL- Issues

### CANNIBAL-001 — [CRITICAL] Homepage Competing with Service Pages for Primary Keywords
**Evidence:** surecash.com.au homepage (surecash.com.au/) and service-specific pages (e.g., /payday-loans/, /cash-loans/) both likely target "payday loans" and "cash loans". This is evidenced by the fact that GSC shows these keywords at positions 21-23 — a sign of split signal (Google cannot decide which page is canonical for the query).
**Competing URLs:** surecash.com.au/ vs surecash.com.au/[service-page]/
**Winner URL:** The most commercially optimised service page with direct application flow
**Action for Homepage:** Homepage should target branded + "short term loans australia" type queries, not compete for specific product terms
**Action for Losers:** Clear canonical tags; homepage does not duplicate service page content
**Effort:** Medium (content audit + canonical review + possible consolidation)
**Priority:** Critical

### CANNIBAL-002 — [HIGH] Location Pages Competing with National Service Pages
**Evidence:** surecash.com.au tracks "cash loans sydney", "payday loans sydney" alongside national "cash loans", "payday loans". If the homepage or national pages contain Sydney-specific content AND dedicated /sydney/ pages also exist, cannibalization occurs.
**Competing URLs:** surecash.com.au/ or /cash-loans/ vs /sydney/ or /cash-loans-sydney/
**Winner URL:** /sydney/ or /cash-loans-sydney/ for Sydney-specific terms; /cash-loans/ for national terms
**Action for Losers:** Remove Sydney-specific content from national pages; ensure each page has a singular primary keyword focus
**Resolution table:**

| Keyword | Winner URL | Action for National Page | Action for Location Page |
|---|---|---|---|
| cash loans sydney | /sydney/ (or /cash-loans-sydney/) | Remove "sydney" geo references; target "cash loans" only | Optimise H1 for "cash loans sydney"; add local signals |
| payday loans sydney | /sydney/ (or /payday-loans-sydney/) | Remove sydney references; target "payday loans" nationally | H1 = "Payday Loans Sydney"; local trust signals |
| quick cash loans sydney | /sydney/ | Remove from national page | Add as secondary H2 on Sydney page |

**Effort:** Medium (page content audit + URL structure review)
**Priority:** High

### CANNIBAL-003 — [HIGH] Centrelink Loan Keyword Cluster — Over-Targeting on Single Page
**Evidence:** 6+ centrelink-related keywords all likely point to one /centrelink-loans/ page. This creates a keyword cannibalization situation where the page tries to rank for too many variations simultaneously, diluting authority.
**Competing keywords on same page:**
- loans on centrelink
- loans for people on centrelink
- loans for centrelink customers
- loans for pensioners on centrelink
- loan for single parents on centrelink
- loans for unemployed on centrelink
- cash loans for unemployed

**Resolution:**
- /centrelink-loans/ → primary page targeting "loans on centrelink" + "loans for people on centrelink" (highest volume)
- Create /pensioner-loans/ or sub-section for pensioner-specific queries
- Create /single-parent-loans/ or sub-section for single parent queries
- Create /unemployed-loans/ or sub-section for unemployed queries
- Internal linking from main centrelink page to sub-audience pages

**Effort:** High (new page creation + content strategy)
**Priority:** High

### CANNIBAL-004 — [MEDIUM] Non-Branch City Keywords Competing with No Physical Presence
**Evidence:** Keywords tracked for Melbourne, Adelaide, Perth, Hobart, Brisbane (no branch) suggest location pages may exist for these cities. Without a physical presence, local pack rankings are impossible, and any organic location pages compete weakly against locally-present lenders.
**Issue:** Multiple city pages (Melbourne, Adelaide, Perth, Hobart, Gold Coast, Geelong, Townsville, Cairns) likely exist and may dilute the site's overall authority without delivering traffic.
**Recommendation:** Audit whether these pages exist and are indexed. If they exist:
- Check traffic in GSC — if near zero, consider consolidating into a "Cash Loans Australia" national page
- Do NOT use 301 redirects to homepage (that removes location signals for organic)
- Consider noindex for cities with zero traffic and no GBP
**Effort:** Low (audit) + Medium (consolidation if needed)
**Priority:** Medium
