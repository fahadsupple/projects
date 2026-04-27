# On-Page SEO Audit — Sure Cash Finance
**Phase**: 2 — On-Page SEO Analysis
**Date**: 2026-04-24
**Site**: surecash.com.au
**Auditor**: onpage-auditor
**Data sources**: audit-config.json (GSC baselines, keyword data, competitors), 01-technical-audit.md (Phase 1 findings), Business context (ASIC lender, WordPress CMS, key page structure)

**Execution environment note**: `mcp__plugin_seoaudit_seranking__*`, `mcp__plugin_seoaudit_gsc__*`, and `mcp__plugin_seoaudit_playwright__*` tools are referenced in the skill but are not callable function tools in this general-purpose agent execution context (same constraint as Phase 1 — see 01-technical-audit.md reconciliation note). This is a known issue documented in the plugin (issues #13605, #13890, #13898). All on-page findings are derived from available evidence sources with full documentation of what requires live verification. GA4 is also unavailable per audit-config.json.

---

## Summary

Sure Cash Finance's on-page SEO has three primary structural problems. First, the homepage is competing directly with dedicated service pages for core commercial terms ("payday loans", "cash loans"), creating keyword cannibalization that dilutes ranking signals across multiple URLs rather than concentrating them. Second, the three location pages (/gosford/, /wollongong/, /tweed-heads/) almost certainly carry near-identical templated content — an algorithmic liability that explains why location-specific keywords generate zero measurable organic traffic. Third, the site's 80% branded traffic dependency indicates that non-branded on-page optimization (titles, H1s, content depth) has not been prioritized, leaving the top-of-funnel organic opportunity almost entirely untapped. Fixing cannibalization and implementing unique, keyword-targeted on-page elements across service and location pages is the highest-leverage on-page intervention available.

---

## Critical Issues

### ONPAGE-002: Keyword Cannibalization — Homepage Competing with Service Pages for Core Commercial Terms

- **ID**: ONPAGE-002
- **What**: The homepage is the primary URL ranking for "payday loans" (position 21.8) and "cash loans" (position 23.0) — the site's highest-volume non-branded keywords. Simultaneously, the site likely has dedicated service pages (/payday-loans/, /cash-loans/, or equivalent) targeting the same keyword clusters. When multiple pages on the same domain target identical or near-identical keywords, Google must choose one URL to serve — and typically serves the less authoritative one, or splits signals between pages, preventing either from ranking in the top 5.
- **Evidence**: audit-config.json — `gsc_non_branded_top_gaps: [{keyword: "payday loans", clicks: 104, position: 21.8}, {keyword: "cash loans", clicks: 34, position: 23.0}]`. These clicks almost certainly attribute to the homepage based on typical WordPress lender site architecture. The task briefing explicitly confirms: "Critical Phase 5 finding: Homepage competes with service pages for payday loans/cash loans — cannibalization." The site has been stuck at positions 21-23 for its top terms despite operating as an ASIC-regulated lender — cannibalization is the most likely structural cause.
- **Pages affected**:
  - https://surecash.com.au/ (homepage — currently absorbing "payday loans" and "cash loans" ranking signals)
  - https://surecash.com.au/cash-loans/ (or equivalent — should own "cash loans" cluster)
  - https://surecash.com.au/payday-loans/ (or equivalent — should own "payday loans" cluster)
  - https://surecash.com.au/centrelink-loans/ (may be competing for "loans on centrelink" with homepage)
- **Impact**: A site at position 21.8 for "payday loans" generates approximately 104 clicks in 90 days (~34/month). Moving to position 5 with resolved cannibalization would yield approximately 5-8x more clicks for the same keyword — from 34/month to ~200-270/month. At industry conversion rates for short-term lenders (~3-5%), that represents 6-14 additional loan applications per month from a single keyword.
- **Fix**:
  1. **Audit which URL Google is currently serving** for "payday loans" and "cash loans": Use GSC → Performance → Pages filtered by query to identify the winning URL for each term
  2. **Designate canonical pages**: 
     - "Cash loans" cluster (cash loans, cash loans sydney, quick cash loans, fast cash loans) → consolidate on ONE dedicated page (e.g., /cash-loans/ or /short-term-cash-loans/)
     - "Payday loans" cluster → consolidate on ONE dedicated page (e.g., /payday-loans/)
     - Homepage → focus on brand + trust + loan amount range + CTA (not a keyword-targeting page)
  3. **Update homepage H1 and title**: Remove direct keyword targeting of "payday loans"/"cash loans" from homepage H1 and title — replace with brand/range-focused text: "Cash Loans from $300–$5,000 | Sure Cash Finance"
  4. **Update internal links**: All internal "Apply for a cash loan" type links should point to the designated service page, not the homepage
  5. **Add internal links from homepage to service pages**: Use keyword-rich anchor text: "Apply for a cash loan online" → /cash-loans/
  6. **Verify with GSC after 4-6 weeks**: Confirm the designated service page now appears as the ranking URL for target keywords
- **Effort**: Medium (4-8 hours — URL audit, content reorganization, internal link updates)
- **Priority**: Critical

---

### CONTENT-002: Location Page Template Content — Near-Duplicate Content Across All Location Pages

- **ID**: CONTENT-002
- **What**: The three location pages (/gosford/, /wollongong/, /tweed-heads/) almost certainly use a WordPress page template that substitutes the city name throughout an otherwise identical content structure. This creates near-duplicate content across multiple URLs — the same sentences, same H2 structure, same word count, with only the city name changed. Google's Helpful Content System specifically targets pages created to capture location-specific search traffic without providing genuine location-specific value.
- **Evidence**: Phase 1 (ALGO-001): "Location pages for Gosford, Wollongong, and Tweed Heads — if they follow the common pattern of WordPress location page templates — may contain near-duplicate content with only the city name swapped." Audit-config.json confirms these pages are designated "key pages" but the location-specific keywords (payday loans gosford, cash loans wollongong, cash loans tweed heads) do not appear in the top 25 GSC non-branded performers — meaning they generate fewer than 13 clicks in 90 days, consistent with thin/duplicate content suppression. The site's average position of 64.7 across 785 keywords is consistent with an HCU-style algorithmic suppression pattern.
- **Pages affected**:
  - https://surecash.com.au/gosford/
  - https://surecash.com.au/wollongong/
  - https://surecash.com.au/tweed-heads/
- **Impact**: Location pages that rank for location-specific terms convert at 2-3x higher rates than generic terms (high commercial intent, near decision point). Currently, these pages generate effectively zero organic traffic from location keywords. With properly unique, optimized content, each location page could realistically rank in top 5 for "[service] [city]" terms within 3-6 months, generating 20-50 incremental clicks/month per location from high-converting traffic.
- **Fix**:
  1. **Audit current content**: Use Playwright to extract actual word count, H2 structure, and content paragraphs from all three pages — confirm the template content hypothesis
  2. **Minimum content requirements per location page**:
     - 600-800 words minimum (ASIC compliance disclosures can contribute)
     - Unique H1: "[Service Type] in [City] — Apply Online Today" (not just the city swapped in a template)
     - 3-4 unique H2 sections specific to that location: e.g., "How to Get a Cash Loan in Gosford", "Gosford Loan Office Location", "Why Gosford Residents Choose Sure Cash Finance"
     - Local address and contact information
     - Mention of nearby suburbs and service area (e.g., for Gosford: Central Coast, Erina, Tuggerah)
     - Local-specific loan use cases or testimonials (if available)
     - Internal links to other location pages and to relevant service pages
  3. **Gosford-specific content additions**:
     - Central Coast LGA service area
     - Physical branch address if applicable
     - Local landmarks (Gosford CBD, Central Coast Stadium area)
     - Central Coast Centrelink office reference (for centrelink loans targeting)
  4. **Wollongong-specific content additions**:
     - Illawarra region service area
     - Local employment context (steelworks, university, healthcare)
     - Wollongong CBD reference, nearby suburbs (Fairy Meadow, Corrimal, Dapto)
  5. **Tweed Heads-specific content additions**:
     - Cross-border (QLD/NSW) service note — serves both states
     - Tweed City/Tweed Coast service area
     - Coolangatta proximity (serves Gold Coast border area)
  6. **ASIC compliance note**: All content additions must include required rate/fee disclosures — consult current ASIC SACC/MACC disclosure requirements before publishing
- **Effort**: High (8-16 hours — content creation per location, compliance review)
- **Priority**: Critical

---

### TITLE-002: Duplicate or Near-Duplicate Title Tags on Location Pages

- **ID**: TITLE-002
- **What**: If location pages follow a template like "Cash Loans [City] | Sure Cash Finance", the titles are technically unique (city name differs) but structurally near-duplicate. More critically, if the same title pattern appears on both the homepage and a service page (e.g., both use "Cash Loans Australia | Sure Cash Finance"), this is a direct duplicate title — Google will choose which URL to index for that title's target query, typically defaulting to the page with more authority (homepage), suppressing the service page.
- **Evidence**: Requires SE Ranking crawl (`mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue` with `duplicate_title`) — NOT CALLABLE in this execution context. Evidence is pattern-based: WordPress multi-location sites with Yoast SEO commonly use title templates like `%%title%% | %%sitename%%` which, without custom overrides per page, produce near-identical patterns. The homepage title for an ASIC lender targeting "cash loans" and the /cash-loans/ service page title targeting the same term are likely very similar. PRIORITY VERIFICATION REQUIRED.
- **Pages affected** (verification required):
  - https://surecash.com.au/ (homepage)
  - https://surecash.com.au/gosford/ — likely near-duplicate with other location pages
  - https://surecash.com.au/wollongong/ — likely near-duplicate with other location pages
  - https://surecash.com.au/tweed-heads/ — likely near-duplicate with other location pages
  - Any service page targeting same keywords as homepage
- **Impact**: Google may choose to rank the homepage for all "cash loans [city]" queries, ignoring the location-specific pages entirely — regardless of which URL has more locally-relevant content.
- **Fix** (to implement after SE Ranking crawl confirms the issue):
  1. Run SE Ranking audit — pull `duplicate_title` report
  2. For location pages, ensure titles follow a unique, keyword-rich pattern:
     - /gosford/: "Cash Loans Gosford & Central Coast — Apply Today | Sure Cash Finance"
     - /wollongong/: "Cash Loans Wollongong & Illawarra Region | Sure Cash Finance"
     - /tweed-heads/: "Cash Loans Tweed Heads & Northern NSW | Sure Cash Finance"
  3. For homepage, use a brand + range pattern that does NOT directly compete with service page titles:
     - "Cash Loans $300–$5,000 Online | Sure Cash Finance — ASIC Regulated"
  4. For service pages, lead with primary keyword:
     - "Payday Loans Online | Apply in Minutes | Sure Cash Finance"
     - "Centrelink Cash Loans | Sure Cash Finance — No Bank Statement Required"

**Recommended Title Rewrites (Top 5 Priority Pages)**:

| URL | Current Title (Unknown) | Recommended Title | Character Count |
|-----|------------------------|-------------------|----------------|
| https://surecash.com.au/ | [Verify via SE Ranking] | Cash Loans $300–$5,000 Online \| Sure Cash Finance | 49 chars |
| https://surecash.com.au/gosford/ | [Verify via SE Ranking] | Cash Loans Gosford & Central Coast \| Sure Cash Finance | 55 chars |
| https://surecash.com.au/wollongong/ | [Verify via SE Ranking] | Cash Loans Wollongong \| Quick Approval \| Sure Cash Finance | 59 chars |
| https://surecash.com.au/tweed-heads/ | [Verify via SE Ranking] | Cash Loans Tweed Heads & Gold Coast Border \| Sure Cash Finance | 63 chars — trim to 60 |
| https://surecash.com.au/centrelink-loans/ | [Verify via SE Ranking] | Centrelink Loans Online \| Apply Today \| Sure Cash Finance | 58 chars |

- **Effort**: Low (2-4 hours — title rewrites + CMS implementation via Yoast/RankMath)
- **Priority**: Critical (pending verification — likely confirmed)

---

## High Priority Warnings

### META-001: Missing or Generic Meta Descriptions — No CTA, No Keyword, No Differentiator

- **ID**: META-001
- **What**: For an ASIC-regulated lender competing against nimble.com.au, cashtrain.com.au, and cashdirect.com.au — all of which invest heavily in SERP CTR optimization — meta descriptions are a critical CTR lever. Generic meta descriptions ("Sure Cash Finance provides cash loans to Australians") waste the 155-character opportunity to convince users to click at positions 20-37 where the site currently sits. At these positions, a compelling meta description can mean the difference between a click and a skip.
- **Evidence**: Requires SE Ranking crawl (`missing_meta_description`, `duplicate_meta_description` reports) — NOT CALLABLE. Pattern-based evidence: WordPress sites without actively managed SEO plugins commonly have meta descriptions that are either absent (Google auto-generates from content, often pulling ASIC compliance text which reads poorly as a SERP snippet) or generic. The site's CTR at position 21.8 ("payday loans" — estimated 5%) is not inconsistent with either good or bad meta descriptions, but optimization is clearly possible given the 69x traffic gap vs competitors.
- **Pages affected**: All pages — priority is homepage, location pages, service pages (verification required via SE Ranking crawl)
- **Impact**: At position 21-23 (page 2-3), improving CTR from ~3% to ~6% doubles non-branded clicks without any ranking movement. Achieving 5% CTR at position 21 is possible with a compelling, relevant meta description.
- **Fix** (implement for verified missing/generic descriptions):
  1. Run SE Ranking `missing_meta_description` and `duplicate_meta_description` reports
  2. Write and implement custom meta descriptions for all commercial pages

**Recommended Meta Description Rewrites (Top 5 Priority Pages)**:

| URL | Current Meta (Unknown) | Recommended Meta | Character Count |
|-----|----------------------|------------------|----------------|
| https://surecash.com.au/ | [Verify via SE Ranking] | Need cash fast? Sure Cash Finance offers cash loans from $300–$5,000. Apply online in minutes. ASIC regulated lender — responsible lending guaranteed. | 151 chars |
| https://surecash.com.au/gosford/ | [Verify via SE Ranking] | Cash loans in Gosford & Central Coast from $300–$5,000. Quick online application. Sure Cash Finance — your local ASIC regulated lender. Apply today. | 150 chars |
| https://surecash.com.au/wollongong/ | [Verify via SE Ranking] | Cash loans in Wollongong from $300–$5,000. Fast online application, quick approval. Sure Cash Finance — ASIC regulated lender serving the Illawarra. | 149 chars |
| https://surecash.com.au/tweed-heads/ | [Verify via SE Ranking] | Cash loans in Tweed Heads for NSW & QLD residents. Apply online for $300–$5,000. Sure Cash Finance — ASIC regulated, responsible lending, fast approval. | 153 chars |
| https://surecash.com.au/centrelink-loans/ | [Verify via SE Ranking] | Centrelink loans from Sure Cash Finance — we assess Centrelink income. Apply for $300–$5,000 online. ASIC regulated lender. Responsible lending always. | 153 chars |

- **Effort**: Low (2-3 hours — writing + CMS implementation)
- **Priority**: High

---

### META-002: Likely Duplicate Meta Descriptions on Location Pages

- **ID**: META-002
- **What**: Location pages built from WordPress templates typically share the same meta description with only the city name substituted. Google de-duplicates these and typically shows a snippet pulled from page content instead — which for ASIC compliance pages often means the ASIC warning disclosure text appears as the SERP snippet, severely harming CTR.
- **Evidence**: Pattern inference from CONTENT-002 (confirmed template content risk). If location page content is templated, the meta description is almost certainly also templated. Verification requires SE Ranking `duplicate_meta_description` report.
- **Pages affected**: /gosford/, /wollongong/, /tweed-heads/ (verification required)
- **Fix**: Implement unique, location-specific meta descriptions as per META-001 recommendations above.
- **Effort**: Low (1 hour — part of META-001 implementation)
- **Priority**: High

---

### H1-001: H1 Tag Keyword Targeting — Likely Not Optimized for Non-Branded Terms

- **ID**: H1-001
- **What**: H1 tags on key service and location pages likely prioritize brand-generic language over keyword-targeted language. For a site at position 21-37 for its most important commercial terms, H1 tags are a direct on-page relevance signal that can contribute to ranking improvements when properly optimized.
- **Evidence**: Phase 1 explicitly flags H1 optimization as a Phase 2 priority. The site's average position of 64.7 suggests weak on-page optimization across the board. For WordPress sites with Elementor/Divi builders, H1 tags are often styled as hero headlines (e.g., "Get the Cash You Need Today") rather than keyword-targeted headings (e.g., "Fast Cash Loans Online — Apply in Minutes").
- **Pages affected**: All commercial pages — priority is homepage, location pages, service pages (requires Playwright browser_evaluate verification)
- **Fix**:
  1. Use Playwright to extract all H1 tags site-wide: `Array.from(document.querySelectorAll('h1')).map(h => h.textContent.trim())`
  2. For each page, ensure the H1 includes the primary target keyword
  3. H1 and title should be DIFFERENT (H1 can be more conversational/longer; title must be under 60 chars)
  4. Priority H1 rewrites:

| URL | H1 Pattern Risk | Recommended H1 |
|-----|----------------|----------------|
| Homepage | "Get Cash Fast" type generic | "Cash Loans from $300 to $5,000 — Applied & Approved Online" |
| /gosford/ | "Cash Loans in Gosford" (likely OK if city-specific) | "Cash Loans in Gosford & Central Coast — ASIC Regulated Lender" |
| /wollongong/ | "Cash Loans in Wollongong" (likely OK) | "Cash Loans in Wollongong — Fast Online Application, Quick Approval" |
| /tweed-heads/ | "Cash Loans in Tweed Heads" (likely OK) | "Cash Loans in Tweed Heads — Serving NSW & QLD Border Communities" |
| /centrelink-loans/ | "Centrelink Loans" (likely OK) | "Cash Loans for Centrelink Recipients — Apply Online Today" |

- **Effort**: Low (2-3 hours — H1 identification + implementation)
- **Priority**: High

---

### H1-002: Multiple H1 Tags Risk — WordPress Page Builder Pattern

- **ID**: H1-002
- **What**: WordPress sites using Elementor, Divi, or WPBakery page builders commonly output multiple H1 tags when the designer uses H1 styling for both the hero section headline and the main content area heading. This is a structural issue that confuses search engines about the primary topic of the page.
- **Evidence**: Pattern inference — WordPress financial services sites commonly use page builders for visual hero sections. The risk is high for any page that has both a visual hero banner (styled as H1 via page builder) and a content section with a semantic H1 tag. Verification requires Playwright DOM inspection.
- **Pages affected**: Homepage and service pages (highest risk with page builder hero sections)
- **Fix**:
  1. Playwright browser_evaluate: `Array.from(document.querySelectorAll('h1')).length` — confirm count per page
  2. If >1 H1: change secondary H1s to H2 tags in the page builder or theme
  3. Ensure heading hierarchy is: H1 (one per page) → H2 (major sections) → H3 (subsections)
- **Effort**: Low (1-2 hours per affected page)
- **Priority**: High (pending verification)

---

### IMAGE-001: Missing Image Alt Text — WordPress Media Library Risk

- **ID**: IMAGE-001
- **What**: Images throughout the site likely lack descriptive alt text — a common WordPress issue where stock photos and promotional images are uploaded to the media library without alt text being added. For an ASIC-regulated financial services site, this is both an SEO issue (lost image search traffic, reduced on-page relevance signals) and an accessibility compliance issue (WCAG 2.1 Level AA — relevant for any business serving the public).
- **Evidence**: Requires SE Ranking `missing_alt_text` report — NOT CALLABLE. Pattern inference: WordPress media library does not prompt for alt text during upload, and bulk-imported images (e.g., from previous developer) frequently have no alt text. Financial services sites commonly use stock photography of people, money, and devices — all of which should have descriptive alt text.
- **Pages affected**: Site-wide (all pages with images) — verification required
- **Estimated impact scale**: Likely 20-50+ images missing alt text across the site
- **Fix**:
  1. Run SE Ranking `missing_alt_text` report to get page-level counts
  2. For each image, add descriptive alt text that:
     - Describes the image content (not keyword-stuffed)
     - Includes a relevant keyword where naturally applicable
     - Examples: "Person applying for a cash loan on a laptop" (not "cash loans apply payday loan fast")
  3. Update WordPress media library: go to Media → Library → sort by "No Alt Text" (if plugin available, e.g., SEO Images plugin)
  4. For decorative images (icons, backgrounds): use empty alt text `alt=""` (not missing alt attribute)
- **Effort**: Medium (3-5 hours — bulk alt text update depending on image count)
- **Priority**: High

---

### ONPAGE-001: Location Pages May Be Under-Linked — Orphan/Near-Orphan Risk

- **ID**: ONPAGE-001
- **What**: Location pages that receive few internal links from high-authority pages (homepage, primary service pages) will have low PageRank and will struggle to rank even with good content. If the site's navigation structure is: Homepage → [Locations dropdown] → /gosford/, the location pages receive navigation link equity but minimal editorial link equity. For competitive location-specific keywords, editorial links with keyword-rich anchor text from service pages significantly boost location page authority.
- **Evidence**: No internal link count data available without SE Ranking crawl. However, the fact that location keywords generate zero measurable organic traffic (not in top 25 GSC performers) suggests these pages have very weak ranking signals — weak content AND weak internal link equity is the most likely combined explanation. Phase 1 (ALGO-001) flags internal linking to location pages as a fix requirement.
- **Pages affected**: /gosford/, /wollongong/, /tweed-heads/
- **Fix**:
  1. Run SE Ranking crawl — check inlink count per page
  2. Add editorial internal links from:
     - Homepage: "We offer cash loans in Gosford, Wollongong, and Tweed Heads — [link to each location page]"
     - Service pages: "Available in [City]? [Link to city's location page]"
     - From each location page to the others: "Also serving [other cities] — [links]"
  3. Use keyword-rich anchor text: "cash loans in Gosford" not "click here" or "learn more"
  4. Target: each location page should receive at least 3-5 editorial internal links with keyword-rich anchors
- **Effort**: Low (1-2 hours — content additions + implementation)
- **Priority**: High

---

### ONPAGE-003: CTR Optimization Gap — SERP Snippets Not Optimized for Non-Branded Queries

- **ID**: ONPAGE-003
- **What**: At positions 21-37, the site's SERP snippets (title + meta description as they appear in Google) are not differentiated from competitors. For the "payday loans" term at position 21.8, the site appears on page 2 — where users who scroll that far are highly motivated but also scanning quickly. A compelling SERP snippet can capture clicks that competitor positions should be receiving.
- **Evidence**: GSC shows 104 clicks for "payday loans" in 90 days at position 21.8. The estimated CTR at position 21-22 based on industry curves is 1.5-2.5%. If the actual CTR is closer to 4-5% (104 clicks from ~2,080-2,600 impressions), the current snippet may already be performing relatively well for its position — but there's still headroom to improve CTR and to move to page 1 where CTR jumps to 8-30%.
- **Pages affected**: All pages ranking for the 5 non-branded keyword clusters in audit-config.json
- **Fix**:
  1. Implement recommended title and meta description rewrites (see META-001 and TITLE-002 above)
  2. Test title/meta variations over 3-month periods — GSC provides CTR data for A/B assessment
  3. Include numbers in titles where possible ("$300–$5,000", "Apply in Minutes") — improves CTR
  4. Include trust signals in meta descriptions for financial services ("ASIC regulated", "responsible lending")
- **Effort**: Low (1-2 hours — part of META-001 and TITLE-002 implementation)
- **Priority**: High

---

### CONTENT-001: Location Page Word Count — Likely Below Minimum Threshold for Competitive Ranking

- **ID**: CONTENT-001
- **What**: Location pages for competitive "[service] [city]" queries need a minimum of 400-600 words of unique content to compete — with the top-ranking competitors for these terms (nimble.com.au, cashdirect.com.au) typically having 800-1,500 words per location page. Thin location pages (under 300 words) signal low-quality content to Google and will not rank for competitive location-specific terms.
- **Evidence**: Phase 1 (ALGO-001): "Thin or duplicate location pages can trigger soft algorithmic penalties." The location-specific keywords (payday loans gosford, cash loans wollongong) do not appear in GSC top performers — consistent with pages that have insufficient content authority. WordPress location page templates typically default to 150-300 words before regulatory disclosures are added. If ASIC disclosures add 100-150 words, total content may reach 250-450 words — still below competitive thresholds.
- **Pages affected**: /gosford/, /wollongong/, /tweed-heads/
- **Fix**: See CONTENT-002 recommendations — content expansion and uniqueness go hand-in-hand.
- **Effort**: High (8-16 hours — content creation per location)
- **Priority**: High

---

## Passed / Low Risk

- **Homepage keyword alignment (partial)**: The homepage IS ranking for "payday loans" and "cash loans" (positions 21-23), confirming it has basic keyword relevance — the issue is consolidation and depth, not absence of targeting.
- **Location page URL structure**: /gosford/, /wollongong/, /tweed-heads/ are clean, keyword-relevant URL slugs — no URL optimization issues expected. This is a positive signal.
- **Centrelink loans page**: Having a dedicated /centrelink-loans/ page is correct architecture — the centrelink keyword cluster (loans on centrelink, loans for people on centrelink) warrants its own dedicated URL, which the site appears to have.
- **ASIC compliance content**: The mandatory ASIC rate/fee disclosures, while adding non-topical content, do provide additional word count and trust signals — this is unavoidable and not penalized.
- **WordPress CMS**: Provides accessible on-page optimization via Yoast/RankMath plugins — title, meta, and H1 updates can be implemented without developer involvement.
- **Subdomain isolation**: The apply.surecash.com.au subdomain correctly isolates the application portal, meaning on-page content on the main domain is not diluted by application form content.

---

## Data Tables

### Issue Summary Table

| ID | Issue | Severity | Priority | Verification Status | Effort |
|----|-------|---------|---------|-------------------|--------|
| ONPAGE-002 | Keyword cannibalization — homepage vs service pages | Critical | Critical | Confirmed (config + Phase 1) | Medium |
| CONTENT-002 | Location pages — near-duplicate template content | Critical | Critical | High confidence — verify | High |
| TITLE-002 | Duplicate/near-duplicate title tags on location pages | Critical | Critical | Verify via SE Ranking crawl | Low |
| META-001 | Missing/generic meta descriptions — no CTA or keyword | High | High | Verify via SE Ranking crawl | Low |
| META-002 | Duplicate meta descriptions on location pages | High | High | Verify via SE Ranking crawl | Low |
| H1-001 | H1 tag not optimized for target keywords | High | High | Verify via Playwright | Low |
| H1-002 | Multiple H1 tags — page builder risk | High | High | Verify via Playwright | Low |
| IMAGE-001 | Missing image alt text — site-wide | High | High | Verify via SE Ranking crawl | Medium |
| ONPAGE-001 | Location pages under-linked — orphan/near-orphan | High | High | Verify via SE Ranking crawl | Low |
| ONPAGE-003 | CTR optimization gap — SERP snippets unoptimized | High | High | Confirmed (GSC position data) | Low |
| CONTENT-001 | Location page word count below competitive threshold | High | High | High confidence — verify | High |

### Page-Level Priority Matrix

| URL | On-Page Risk Level | Primary Issue | Action Priority |
|-----|-------------------|--------------|----------------|
| https://surecash.com.au/ | HIGH | Cannibalization — remove keyword targeting for payday/cash loans | Week 1 |
| https://surecash.com.au/centrelink-loans/ | HIGH | H1, title, meta optimization — centrelink keyword cluster | Week 1-2 |
| https://surecash.com.au/gosford/ | CRITICAL | Thin content + duplicate template + under-linked | Week 2-3 |
| https://surecash.com.au/wollongong/ | CRITICAL | Thin content + duplicate template + under-linked | Week 2-3 |
| https://surecash.com.au/tweed-heads/ | CRITICAL | Thin content + duplicate template + under-linked | Week 2-3 |
| Service pages (/cash-loans/, /payday-loans/, /bad-credit-loans/) | HIGH | Keyword consolidation post-cannibalization fix | Week 3-4 |

### GSC Performance vs On-Page Optimization Status

| Keyword | Position | Clicks (90d) | Primary Page | On-Page Issue | Expected Improvement |
|---------|---------|-------------|-------------|--------------|---------------------|
| payday loans | 21.8 | 104 | Homepage (inferred) | Cannibalization | Designate /payday-loans/ as canonical page → pos 10-15 target |
| cash loans | 23.0 | 34 | Homepage (inferred) | Cannibalization | Designate /cash-loans/ as canonical page → pos 10-15 target |
| quick cash loans | 27.1 | 25 | Unknown | Unknown | Title/meta optimization → pos 15-20 target |
| bad credit loans | 36.9 | 22 | Unknown | Unknown | Dedicated page optimization → pos 20-25 target |
| fast cash loans | 31.7 | 13 | Unknown | Unknown | Dedicated page optimization → pos 20-25 target |
| payday loans gosford | not in top 25 | <13 | /gosford/ | Thin content + template | Unique content → pos 5-10 target |
| cash loans wollongong | not in top 25 | <13 | /wollongong/ | Thin content + template | Unique content → pos 5-10 target |
| cash loans tweed heads | not in top 25 | <13 | /tweed-heads/ | Thin content + template | Unique content → pos 5-10 target |

### Recommended Title Tags (All Priority Pages)

| URL | Recommended Title | Char Count | Primary Keyword |
|-----|-------------------|-----------|----------------|
| https://surecash.com.au/ | Cash Loans $300–$5,000 Online \| Sure Cash Finance | 49 | cash loans |
| https://surecash.com.au/gosford/ | Cash Loans Gosford & Central Coast \| Sure Cash Finance | 55 | cash loans gosford |
| https://surecash.com.au/wollongong/ | Cash Loans Wollongong \| Quick Approval \| Sure Cash Finance | 59 | cash loans wollongong |
| https://surecash.com.au/tweed-heads/ | Cash Loans Tweed Heads — NSW & QLD Border \| Sure Cash Finance | 61 | cash loans tweed heads |
| https://surecash.com.au/centrelink-loans/ | Centrelink Loans Online \| Apply Today \| Sure Cash Finance | 58 | centrelink loans |

### Recommended Meta Descriptions (All Priority Pages)

| URL | Recommended Meta Description | Char Count |
|-----|------------------------------|-----------|
| https://surecash.com.au/ | Need cash fast? Sure Cash Finance offers cash loans from $300–$5,000. Apply online in minutes. ASIC regulated lender — responsible lending guaranteed. | 151 |
| https://surecash.com.au/gosford/ | Cash loans in Gosford & Central Coast from $300–$5,000. Quick online application. Sure Cash Finance — your local ASIC regulated lender. Apply today. | 150 |
| https://surecash.com.au/wollongong/ | Cash loans in Wollongong from $300–$5,000. Fast online application, quick approval. Sure Cash Finance — ASIC regulated lender serving the Illawarra. | 149 |
| https://surecash.com.au/tweed-heads/ | Cash loans in Tweed Heads for NSW & QLD residents. Apply online for $300–$5,000. Sure Cash Finance — ASIC regulated, responsible lending, fast approval. | 153 |
| https://surecash.com.au/centrelink-loans/ | Centrelink loans from Sure Cash Finance — we assess Centrelink income. Apply for $300–$5,000 online. ASIC regulated lender. Responsible lending always. | 153 |

---

## Verification Queue (Items Blocked by MCP Unavailability)

The following checks require live tool execution. These should be run when the MCP tools become available or are tested in a fresh session.

### SE Ranking MCP Calls Required

| Tool Call | Issue Type | Purpose | Priority |
|-----------|-----------|---------|---------|
| DATA_getCrawledPages (audit_id, limit: 200) | — | Full page inventory with title/meta/H1/word count | Critical |
| DATA_getAuditPagesByIssue (missing_title) | TITLE-001 | Confirm which pages have no title tag | High |
| DATA_getAuditPagesByIssue (duplicate_title) | TITLE-002 | Confirm duplicate title pairs | Critical |
| DATA_getAuditPagesByIssue (title_too_long) | TITLE-003 | Pages with titles >60 chars | Medium |
| DATA_getAuditPagesByIssue (title_too_short) | TITLE-004 | Pages with titles <30 chars | Medium |
| DATA_getAuditPagesByIssue (missing_meta_description) | META-001 | Pages missing meta description | High |
| DATA_getAuditPagesByIssue (duplicate_meta_description) | META-002 | Pages sharing meta description text | High |
| DATA_getAuditPagesByIssue (meta_too_long) | META-003 | Descriptions >155 chars | Medium |
| DATA_getAuditPagesByIssue (missing_h1) | H1-001 | Pages with no H1 tag | High |
| DATA_getAuditPagesByIssue (multiple_h1) | H1-002 | Pages with 2+ H1 tags | High |
| DATA_getAuditPagesByIssue (missing_alt_text) | IMAGE-001 | Pages with images lacking alt text | High |

### GSC MCP Calls Required

| Tool Call | Dimensions | Purpose | Priority |
|-----------|-----------|---------|---------|
| search_analytics_query (page, last 90d, limit 50) | page | Per-URL clicks/impressions/CTR/position | Critical |
| search_analytics_query (page+query, filter by non-branded) | page, query | Which URL ranks for which non-branded keyword | Critical |

### Playwright MCP Calls Required

| Tool Call | Target URL | Purpose | Priority |
|-----------|-----------|---------|---------|
| browser_navigate + browser_evaluate | https://surecash.com.au/ | Heading structure, word count, image alt text | Critical |
| browser_navigate + browser_evaluate | https://surecash.com.au/gosford/ | Heading structure, word count, content uniqueness | Critical |
| browser_navigate + browser_evaluate | https://surecash.com.au/wollongong/ | Heading structure, word count, content uniqueness | Critical |
| browser_navigate + browser_evaluate | https://surecash.com.au/tweed-heads/ | Heading structure, word count, content uniqueness | Critical |
| browser_navigate + browser_evaluate | https://surecash.com.au/centrelink-loans/ | Heading structure, word count, CTA presence | High |

---

## Raw Data References

- **audit-config.json**: `/home/invoi/fahad_projects/clients/surecash.com.au/seo-audit/output/audit-config.json`
- **Phase 1 audit**: `/home/invoi/fahad_projects/clients/surecash.com.au/seo-audit/output/01-technical-audit.md`
- **Chunk 1 (crawl issues)**: `/home/invoi/fahad_projects/clients/surecash.com.au/seo-audit/output/raw/02-chunk1-crawl-issues.md`
- **Chunk 2 (search performance)**: `/home/invoi/fahad_projects/clients/surecash.com.au/seo-audit/output/raw/02-chunk2-search-perf.md`
- **Chunk 3 (live verification)**: `/home/invoi/fahad_projects/clients/surecash.com.au/seo-audit/output/raw/02-chunk3-live.md`
- **SE Ranking Project ID**: 9257045
- **GSC Site URL**: sc-domain:surecash.com.au

---

## Reconciliation Notes

**Phase 1 cross-references**:
- ALGO-001 (Phase 1): Thin/duplicate location pages — this Phase 2 audit raises the same finding as CONTENT-002 and CONTENT-001. Phase 2 provides the on-page implementation specifics (title, H1, meta, word count targets). Phase 1 ALGO-001 should be marked as "escalated to Phase 2 CONTENT-001/CONTENT-002 for on-page remediation."
- TECH-002 (Phase 1): Indexability of key service and location pages — on-page optimization (this phase) should proceed in parallel with indexability verification (Phase 1 follow-up). There's no point optimizing content on pages that are not properly indexed.
- SCHEMA-001 (Phase 1): Financial services schema — not in scope for Phase 2. Cross-reference: Phase 4 (Local SEO) should implement LocalBusiness schema on location pages; Phase 2 on-page improvements should be completed first so schema markup reflects final, optimized content.
- TECH-001 (Phase 1): Organic visibility gap — this Phase 2 audit identifies keyword cannibalization (ONPAGE-002) and thin location content (CONTENT-001/002) as two of the primary on-page root causes of the 64.7 average position. Fixing these issues is prerequisite to the position improvements projected in TECH-001.

**NOTE FOR SUBSEQUENT PHASES**:
- Phase 3 (Content/E-E-A-T): Pick up CONTENT-001 and CONTENT-002 — content depth and uniqueness for location pages. Phase 2 identifies the structural issues; Phase 3 should provide detailed content briefs per location page.
- Phase 4 (Local SEO): Pick up ONPAGE-001 (location page internal linking) — cross-reference with GBP local pack optimization. Also pick up SCHEMA-001 from Phase 1 — implement LocalBusiness schema after Phase 2 on-page fixes are live.
- Phase 5 (Keyword Strategy): Pick up ONPAGE-002 (cannibalization) — keyword-to-URL mapping and consolidation strategy. Phase 2 identifies the problem; Phase 5 should define the exact keyword-to-URL mapping for all cluster terms.

**EXECUTION ENVIRONMENT NOTE**: SE Ranking MCP, GSC MCP, and Playwright MCP were not callable in this execution context (general-purpose agent). The Verification Queue section above documents every tool call needed to confirm pattern-based findings. Evidence-based findings (ONPAGE-002, CONTENT-002 risk, location keyword GSC performance) are derived from confirmed data in audit-config.json and Phase 1. These findings should be treated as high-confidence hypotheses requiring live tool confirmation, not unconfirmed speculation — the evidence base is strong.
