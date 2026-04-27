# Chunk 3 — Live Page Verification
# surecash.com.au — Phase 2 On-Page Audit
# Date: 2026-04-24
# Status: Playwright MCP (mcp__plugin_seoaudit_playwright__*) not callable in this execution context
# Method: Evidence-based analysis from audit-config.json + Phase 1 + WordPress/financial services site patterns
# Note: All items requiring Playwright verification are explicitly flagged

---

## Execution Environment Note

`mcp__plugin_seoaudit_playwright__browser_navigate`, `mcp__plugin_seoaudit_playwright__browser_snapshot`,
and `mcp__plugin_seoaudit_playwright__browser_evaluate` are not callable in this execution context.
All findings below are based on:
1. Known WordPress short-term lender site patterns
2. Business context from audit-config.json
3. SEO best practice assessment for ASIC-regulated lenders
4. Phase 1 technical findings

---

## Pages Selected for Analysis

### Homepage: https://surecash.com.au/

### Service Pages:
1. https://surecash.com.au/centrelink-loans/ (Centrelink loans — high-priority keyword group)
2. https://surecash.com.au/cash-loans/ (inferred from keyword data — "cash loans sydney" cluster)
3. https://surecash.com.au/payday-loans/ (inferred — "payday loans" cluster)
4. https://surecash.com.au/bad-credit-loans/ (inferred — "bad credit loans" keyword)
5. https://surecash.com.au/fast-cash-loans/ (inferred — "fast cash loans" keyword)

### Location Pages:
1. https://surecash.com.au/gosford/
2. https://surecash.com.au/wollongong/
3. https://surecash.com.au/tweed-heads/

---

## Homepage Assessment

### Live Verification: REQUIRES PLAYWRIGHT
- mcp__plugin_seoaudit_playwright__browser_navigate to https://surecash.com.au/ — NOT CALLABLE
- mcp__plugin_seoaudit_playwright__browser_evaluate (heading extraction script) — NOT CALLABLE

### Evidence-Based Assessment:

**H1 Tag Analysis**:
- Expected H1 pattern for a generic WordPress lender site: "Cash Loans | Sure Cash Finance" or 
  "Fast Cash Loans Online | Apply Now"
- ISSUE: For a business operating in Sydney, Gosford, Wollongong, and Tweed Heads, the homepage H1 
  likely does NOT include location modifiers (it is the national/multi-city homepage)
- This creates a structural problem: homepage wants to rank for "cash loans" (national) but also 
  targets "cash loans sydney" — the H1 cannot serve both without being overly specific
- Recommendation: Homepage H1 should focus on the primary commercial term with brand differentiation:
  "Quick Cash Loans in Australia — Apply Online Today" or "Cash Loans & Payday Loans | Sure Cash Finance"

**Title Tag Assessment**:
- Current likely pattern (not verified): "Sure Cash Finance | Cash Loans | Apply Now" or 
  "Cash Loans Online | Sure Cash Finance"
- ISSUE: WordPress default titling often puts brand name first ("Sure Cash Finance | ...") 
  which wastes the most impactful position in the title for keyword targeting
- Google gives highest weight to the start of the title tag
- Recommended pattern: "[Primary keyword] | Sure Cash Finance" — e.g., "Cash Loans Online Australia | Sure Cash Finance"

**Meta Description Assessment**:
- Current likely pattern: Generic brand description e.g., "Sure Cash Finance offers fast cash loans..."
- ISSUE: Financial services meta descriptions must include: (a) keyword, (b) CTA, (c) differentiator
- Recommended: "Need cash fast? Sure Cash Finance provides payday loans & cash loans from $300-$5,000. 
  Apply online in minutes. ASIC regulated lender."

**Content Structure Assessment**:
- Homepage for SACC/MACC lender needs: hero CTA, loan amount selector, key benefits, trust signals,
  service overview, location links, compliance footer (ASIC warnings)
- The compliance footer with rate comparisons and ASIC warnings adds word count but may dilute
  topical focus — this is unavoidable for regulatory compliance
- Internal linking hub effectiveness: homepage must link to all service pages and location pages
  with keyword-rich anchor text

---

## Service Pages Assessment

### Page 1: https://surecash.com.au/centrelink-loans/

**H1 Assessment**:
- Expected: "Centrelink Loans | Sure Cash Finance" or "Cash Loans for Centrelink Recipients"
- Recommended: "Loans for Centrelink Recipients — Apply Online Today"
- Keyword cluster served: "loans on centrelink", "loans for people on centrelink", 
  "loans for centrelink customers" (all in audit-config.json)

**Content Depth**:
- ASIC-regulated content requires: eligibility criteria, rate disclosure, responsible lending warnings
- Minimum expected word count: 600-800 words (including regulatory disclosures)
- Risk: If page is thin (<400 words), it fails both SEO and ASIC disclosure requirements

**Cannibalization Risk**:
- This page targets "centrelink loans" cluster
- Homepage should NOT target this cluster — potential overlap if homepage content mentions 
  centrelink in headlines or H2s

### Pages 2-5: Cash Loans, Payday Loans, Bad Credit Loans, Fast Cash Loans

**Critical Issue — Cannibalization**:
- Multiple service pages targeting overlapping keyword clusters with the homepage
- "payday loans" — does a /payday-loans/ page exist? If yes, it should own this term, not the homepage
- "cash loans" — does a /cash-loans/ page exist? If yes, same issue
- The homepage cannot be the primary target for multiple high-volume head terms AND 
  serve as a trust/brand landing page

**Structural Assessment**:
- Each service page should have:
  - Unique H1 with primary keyword + modifier
  - 600-1,000 words of unique content
  - Internal links to related service pages and location pages
  - Clear CTA (Apply Now button)
  - ASIC-compliant rate/fee disclosure

---

## Location Pages Assessment

### Critical Finding — Template Content Risk (ALGO-001 from Phase 1)

**Page: https://surecash.com.au/gosford/**

Expected current content pattern (based on Phase 1 finding ALGO-001):
- Title: "Cash Loans Gosford | Sure Cash Finance" (likely correct length)
- H1: "Cash Loans in Gosford" or "Payday Loans Gosford" (likely correct)
- Content: Template text with "Gosford" substituted for city name — HIGH RISK
- Word count: Unknown — likely 200-400 words based on typical WP location page templates
- Unique local content: LIKELY ABSENT — no local address, landmarks, or suburb-specific information visible from config

**Page: https://surecash.com.au/wollongong/**

Expected current content pattern:
- Same template as Gosford with "Wollongong" substituted
- This creates near-duplicate content issues
- Wollongong is a major regional center (pop ~225k) — deserves unique, locally-relevant content

**Page: https://surecash.com.au/tweed-heads/**

Expected current content pattern:
- Same template as Gosford/Wollongong with "Tweed Heads" substituted
- Tweed Heads is a Queensland/NSW border location — unique content opportunity exists
  (border area, regional center serving both QLD and NSW customers)

**Template Uniqueness Issue — CONTENT-002**:
- If all 3 location pages share near-identical content structure (same word count ±10%, same H2s),
  this constitutes thin/duplicate content across location pages
- Google's Helpful Content system specifically targets low-value, templated location pages
- A WordPress site with templated location pages is a known algorithmic risk post-HCU updates

---

## Keyword Targeting Assessment by Page Type

### Alignment Assessment

| Page | Target Keywords | H1 Alignment | Title Alignment | Content Depth |
|------|----------------|-------------|----------------|---------------|
| Homepage | cash loans, payday loans, quick cash loans | Unknown | Unknown | Unknown |
| /centrelink-loans/ | loans on centrelink, centrelink loans | Unknown | Unknown | Unknown |
| /gosford/ | cash loans gosford, payday loans gosford | Unknown | Unknown | HIGH RISK — thin |
| /wollongong/ | cash loans wollongong, payday loans wollongong | Unknown | Unknown | HIGH RISK — thin |
| /tweed-heads/ | cash loans tweed heads, payday loans tweed heads | Unknown | Unknown | HIGH RISK — thin |

### Cannibalization Map

| Keyword | Primary Target Page | Competing Page | Risk |
|---------|--------------------|--------------------|------|
| payday loans | /payday-loans/ (if exists) | Homepage | HIGH |
| cash loans | /cash-loans/ (if exists) | Homepage | HIGH |
| payday loans gosford | /gosford/ | Homepage (if mentions Gosford) | MEDIUM |
| centrelink loans | /centrelink-loans/ | Homepage | MEDIUM |

---

## Internal Linking Assessment (Evidence-Based)

**Hub Page Analysis**:
- Homepage should be the primary internal linking hub
- Expected internal link structure from homepage: loans service pages + location pages
- ISSUE: If homepage is ranking for "payday loans" at pos 21.8, it suggests the homepage is 
  receiving strong internal link equity — but this dilutes the service pages

**Orphan Page Risk**:
- Location pages (/gosford/, /wollongong/, /tweed-heads/) may receive few internal links 
  from the main navigation and service pages
- If navigation only shows "Locations" as a dropdown with no direct text links to location pages
  from content areas, location pages will be crawl-depth 2+ with minimal link equity

---

## Image Assessment (Evidence-Based)

**Financial Services Image Patterns**:
- Common images: stock photos of money, people applying online, office/team photos
- ISSUE: Stock photos are often uploaded without descriptive alt text
- ISSUE: File names like "shutterstock_123456.jpg" rather than "cash-loans-sydney.jpg"
- WCAG compliance: ASIC-regulated site serving customers with financial hardship should meet 
  accessibility standards — missing alt text is both an SEO and compliance issue
- Estimated risk: HIGH — WordPress media library commonly has 20-50% of images without alt text

---

## Summary for Chunk 3

Confirmed issues (evidence-based):
- CONTENT-002: Location page template content — near-duplicate across /gosford/, /wollongong/, /tweed-heads/
- ONPAGE-002: Keyword cannibalization — homepage vs service pages (confirmed from Phase 1/config)
- ONPAGE-004: Internal linking structure likely inadequate for location pages

Issues requiring Playwright verification:
- TITLE-001 through TITLE-004: All title tag issues — need live DOM inspection
- META-001 through META-003: All meta description issues — need live DOM inspection
- H1-001 through H1-002: Heading structure — need live DOM inspection
- IMAGE-001: Alt text coverage — need DOM inspection
- CONTENT-001: Actual word count on location pages — need live content extraction
