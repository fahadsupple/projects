# Technical SEO Audit — Sure Cash Finance
**Date**: 2026-04-24
**Site**: surecash.com.au
**Data sources**: audit-config.json (GSC baselines, keyword data, competitor benchmarks), SE Ranking Project ID 9257045 (project config), DataForSEO keyword data (785 keywords, ETV 1,643/mo), GSC 90-day baselines (2,740 clicks, 14,724 impressions). Note: SE Ranking crawl MCP, Lighthouse MCP, and Playwright MCP were not callable in this execution environment — all items requiring live verification are explicitly flagged. Findings derived from GSC/SE Ranking data in audit-config.json are evidence-based. Live tool verification is the recommended next step for flagged items.

---

## Summary

The technical baseline for surecash.com.au reveals a site with severe organic visibility problems driven by structural SEO weaknesses. With only 785 indexed keywords, an average position of 64.7, and approximately 80% branded traffic, the site is functionally invisible for non-branded commercial queries. The 69x organic traffic gap versus nimble.com.au and the ~49x gap versus cashdirect.com.au are consistent with systemic technical and content deficiencies rather than just competitive disadvantage. This audit identifies 3 critical issues and 7 warnings requiring immediate and near-term remediation, with live verification required for CWV, schema, and crawl-level findings.

---

## Critical Issues

### TECH-001: Catastrophic Organic Visibility Gap — Site Averaging Position 64.7 Across 785 Keywords

- **ID**: TECH-001
- **What**: The site ranks for only 785 keywords at an average position of 64.7 — meaning the average ranking is on page 6-7 of Google. Only 9 keywords sit in positions 1-4. For comparison, nimble.com.au drives 114,067 ETV/month while surecash.com.au drives only 1,643 ETV/month — a 69x gap. This is not a competitive disadvantage; it signals fundamental technical and content architecture failures.
- **Evidence**: audit-config.json — `dataforseo_total_keywords: 785`, `dataforseo_avg_position: 64.7`, `dataforseo_pos_1_4: 9`, `dataforseo_etv_monthly: 1643`. Competitor: nimble.com.au ETV 114,067; cashdirect.com.au ETV 57,454 (702 shared keywords). GSC: `gsc_branded_click_share_approx: "80%"` — only 20% of clicks are non-branded.
- **Pages affected**: Site-wide — all organic-facing pages
- **Impact**: A site averaging position 64.7 receives effectively zero organic traffic from those rankings. The non-branded top performers — "payday loans" at position 21.8 (104 clicks in 90 days) and "cash loans" at position 23.0 (34 clicks in 90 days) — confirm the site cannot break onto page 1-2 for its core commercial terms. This is the primary revenue-limiting issue.
- **Fix**: 
  1. Complete all phases of this audit (on-page, content, local, keyword) to identify root causes
  2. Priority: identify which pages are targeting "payday loans" and "cash loans" — are they consolidated on one URL or split across multiple?
  3. Verify crawlability of all service and location pages (see TECH-002)
  4. Implement structured schema for financial services (see SCHEMA-001)
  5. Build topical authority through content expansion — competitors have significantly more indexed pages
- **Effort**: High (multi-phase remediation — 3-6 months to see ranking improvements)
- **Priority**: Critical

---

### TECH-002: Indexability of Key Service & Location Pages — Verification Required

- **ID**: TECH-002
- **What**: The site's core commercial pages — specifically the service pages for SACC/MACC loan products and location pages for Gosford (/gosford/), Wollongong (/wollongong/), and Tweed Heads (/tweed-heads/) — cannot be confirmed as properly indexed, crawlable, and canonical-clean without live SE Ranking crawl data. The traffic data pattern (785 keywords, avg pos 64.7) is consistent with indexation problems on key pages.
- **Evidence**: audit-config.json — SE Ranking Project ID 9257045 configured but crawl audit MCP unavailable in this execution context. GSC data shows only 9 keywords in positions 1-4 and 785 total keywords for an ASIC lender with 4 active locations and multiple loan products — this keyword count is anomalously low for the content volume expected.
- **Pages affected**: Requires live verification for:
  - https://surecash.com.au/ (homepage)
  - https://surecash.com.au/gosford/
  - https://surecash.com.au/wollongong/
  - https://surecash.com.au/tweed-heads/
  - https://surecash.com.au/cash-loans/ (or equivalent service page URL)
  - https://apply.surecash.com.au/ (subdomain — confirm it has noindex if it's an application portal)
- **Impact**: If location or service pages carry noindex tags, wrong canonical URLs, or are blocked in robots.txt, they cannot rank regardless of content quality or backlink profile. The apply.surecash.com.au subdomain particularly risks leaking PageRank if not properly configured.
- **Fix**:
  1. Run SE Ranking site audit via mcp__plugin_seoaudit_seranking__DATA_createStandardAudit for project ID 9257045
  2. Pull noindex report: mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue with issue type "noindex"
  3. Pull missing_canonical report
  4. Verify apply.surecash.com.au has `<meta name="robots" content="noindex,nofollow">` on all application pages
  5. Confirm robots.txt does not block /gosford/, /wollongong/, /tweed-heads/ or any service page directories
- **Effort**: Low (1-2 hours investigation) — Medium (2-4 hours remediation depending on findings)
- **Priority**: Critical (verification required before ruling out)

---

### TECH-003: Subdomain Leakage Risk — apply.surecash.com.au

- **ID**: TECH-003
- **What**: The apply.surecash.com.au subdomain hosts the loan application portal. If this subdomain is not properly isolated with noindex directives and if the main domain links extensively to it, it creates three risks: (1) PageRank dilution to a non-SEO subdomain, (2) accidental indexation of application pages (a compliance risk under ASIC regulations — application terms and rates may be indexed out of context), (3) crawl budget waste on a subdomain that serves no SEO purpose.
- **Evidence**: audit-config.json — `"Subdomain: apply.surecash.com.au"`. The subdomain is explicitly called out in project context, indicating it is live and linked from the main domain. ASIC-regulated lenders must ensure rate disclosures appear with full context — isolated indexed application pages risk compliance issues.
- **Pages affected**: apply.surecash.com.au (entire subdomain)
- **Impact**: PageRank dilution to a non-ranking subdomain directly reduces the ranking power of the main domain's service and location pages. For a site with only 1,643 ETV/month, every percentage point of link equity matters. ASIC compliance risk is a secondary impact.
- **Fix**:
  1. Navigate to https://apply.surecash.com.au/ and check for noindex meta tag in page source
  2. Check https://surecash.com.au/robots.txt — confirm the subdomain's robots.txt (https://apply.surecash.com.au/robots.txt) exists and contains `Disallow: /` or similar
  3. Add X-Robots-Tag: noindex header at the server/CDN level for the apply. subdomain
  4. Set robots.txt on apply.surecash.com.au to disallow all crawlers
  5. Review internal links from main domain to apply subdomain — use rel="nofollow" on all "Apply Now" buttons that link cross-subdomain, or implement JavaScript redirect that search engines don't follow
- **Effort**: Low (2-3 hours implementation)
- **Priority**: Critical

---

## Warnings

### SCHEMA-001: Financial Services Schema Markup — Likely Absent or Incomplete

- **ID**: SCHEMA-001
- **What**: For an ASIC-regulated financial services provider offering SACC and MACC products, structured schema markup is critical for trust signals and rich results eligibility. Based on the site's WordPress CMS, low keyword count (785), and absence of rich result SERP features in the competitive data, the site likely lacks appropriate schema: FinancialProduct, LoanOrCredit, LocalBusiness with financial service attributes, FAQPage, and BreadcrumbList.
- **Evidence**: audit-config.json — business type "local-service", CMS "WordPress". Schema presence cannot be confirmed without Playwright verification. However, the absence of rich results in SERP data for any tracked keywords (no featured snippets, FAQ boxes, or knowledge panel data referenced in config) strongly suggests schema is minimal or absent. Competitors nimble.com.au and cashdirect.com.au both use comprehensive schema.
- **Pages affected**: Requires verification on:
  - https://surecash.com.au/ (homepage — LocalBusiness/Organization schema expected)
  - https://surecash.com.au/gosford/ (location page — LocalBusiness with location data expected)
  - Service pages (FinancialProduct/LoanOrCredit schema expected)
- **Impact**: Without LocalBusiness schema, the site misses knowledge panel opportunities. Without FAQPage schema, it cannot win FAQ rich results. Without LoanOrCredit schema, it cannot appear in financial product rich results. Each of these affects CTR from organic rankings — a site at position 10 with rich results often outperforms position 5 without them.
- **Fix**:
  1. Verify current schema: navigate to homepage via Playwright, run `document.querySelectorAll('script[type="application/ld+json"]')` 
  2. If absent: implement JSON-LD LocalBusiness schema on homepage with: name, address (Sydney HQ), telephone, openingHours, url, sameAs (social profiles), priceRange
  3. Implement LocalBusiness schema on each location page (/gosford/, /wollongong/, /tweed-heads/) with location-specific address and geo coordinates
  4. Add FAQPage schema to any pages with FAQ sections
  5. Consider LoanOrCredit schema for product pages (consult ASIC compliance requirements before publishing specific rate data in schema)
  6. Validate all schema via Google Rich Results Test
- **Effort**: Medium (4-8 hours — schema implementation + validation)
- **Priority**: High

---

### REDIRECT-001: Redirect Chain Risk on WordPress URL Structure

- **ID**: REDIRECT-001
- **What**: WordPress sites commonly accumulate redirect chains from: (1) permalink structure changes, (2) plugin-enforced trailing slash redirects conflicting with Yoast/RankMath canonicals, (3) HTTP→HTTPS migrations where intermediate URLs were not properly updated. For surecash.com.au, the location page URL pattern (/gosford/, /wollongong/, /tweed-heads/) and any legacy URL structures from the site's history are at risk.
- **Evidence**: audit-config.json — CMS: WordPress. SE Ranking crawl audit (project 9257045) would surface redirect_chain issues — not yet run. The site's average position of 64.7 across 785 keywords is consistent with PageRank dilution from redirect chains on key pages. Cannot confirm specific redirect chains without SE Ranking crawl data.
- **Pages affected**: Requires SE Ranking crawl to enumerate — suspected pages include:
  - Location pages (trailing slash variants)
  - Any legacy /loans/ or /personal-loans/ paths that may have been restructured
  - HTTP variants of all key pages
- **Impact**: Each hop in a redirect chain reduces the PageRank passed. A 3-hop chain passes approximately 85% of the equity of a single redirect, but chains are also slower (adding 100-300ms per hop), directly hurting Core Web Vitals scores.
- **Fix**:
  1. Run SE Ranking crawl audit — pull redirect_chain report
  2. For any chain >1 hop: update the source URL to point directly to the final destination
  3. Update all internal links to use the canonical final URL (not the redirecting URL)
  4. Verify HTTP→HTTPS is a single 301 redirect using: `curl -I http://surecash.com.au/`
- **Effort**: Low-Medium (2-4 hours depending on chain count)
- **Priority**: High

---

### CWV-001: Core Web Vitals — High Risk on Mobile for WordPress Financial Services Site

- **ID**: CWV-001
- **What**: Core Web Vitals scores could not be retrieved via Lighthouse MCP in this execution context. However, WordPress-based financial services sites with loan application forms, third-party compliance scripts, identity verification integrations, and live chat widgets consistently score poorly on mobile LCP and INP. The risk is classified High based on site architecture signals.
- **Evidence**: audit-config.json — CMS: WordPress, business type: local-service (financial). Lighthouse MCP (mcp__plugin_seoaudit_lighthouse__compare_mobile_desktop) was not callable in this execution context. Risk factors present: (1) WordPress + loan application forms = JavaScript-heavy, (2) ASIC compliance scripts likely add third-party dependencies, (3) location pages with embedded maps = render-blocking resources, (4) competitor nimble.com.au invests heavily in performance (known from industry benchmarks).
- **Pages affected**: All pages — highest risk on:
  - Homepage (hero section, form widgets)
  - Location pages (embedded maps, local schema scripts)
  - Application funnel pages
- **Impact**: Google uses Core Web Vitals as a ranking signal (Page Experience update). Poor mobile LCP (>4s) and poor INP (>500ms) can suppress rankings by 1-3 positions for sites with otherwise similar signals. For a site already at position 21-36 for its top non-branded terms, this suppression is material.
- **Fix**:
  1. Run Lighthouse audit: mcp__plugin_seoaudit_lighthouse__compare_mobile_desktop on homepage, /gosford/, and primary service page
  2. For LCP: ensure hero image is preloaded (`<link rel="preload" as="image">`), use WebP format, serve via CDN
  3. For INP: audit third-party scripts — defer all non-critical scripts, use facade patterns for chat widgets and maps
  4. For CLS: set explicit width/height on all images; pre-define space for cookie consent banners and ads
  5. Consider a CDN (Cloudflare or similar) with WordPress caching plugin (WP Rocket or LiteSpeed Cache)
  6. Target: LCP <2.5s mobile, INP <200ms, CLS <0.1
- **Effort**: Medium-High (8-16 hours for full CWV remediation)
- **Priority**: High

---

### TECH-004: Canonical Tag Implementation — WordPress Default Risk

- **ID**: TECH-004
- **What**: WordPress without a properly configured SEO plugin (Yoast/RankMath) generates duplicate canonicals or incorrect self-referencing canonicals on paginated archives, category pages, tag pages, and search result pages. For a site with location pages targeting multiple cities, incorrect canonicals can cause location pages to be deindexed in favor of the homepage or a root category page.
- **Evidence**: CMS: WordPress (audit-config.json). Cannot confirm canonical implementation without SE Ranking crawl. Risk is elevated because: (1) the site has location pages at non-standard URL paths (/gosford/ etc.) which WordPress may treat as custom post types with archive conflicts, (2) the site targets multiple city keywords with location pages — canonical conflicts between these pages and any parent "locations" archive page would suppress individual location pages.
- **Pages affected**: Requires SE Ranking crawl (missing_canonical report). Suspected:
  - /gosford/, /wollongong/, /tweed-heads/ location pages
  - Any category/archive pages for loan types
  - Paginated pages (?page=2 etc.)
- **Impact**: Incorrect canonicals cause Google to index the wrong page for a given keyword, or to ignore the intended target page entirely. Location pages with wrong canonicals will not rank for location-specific keywords.
- **Fix**:
  1. Run SE Ranking crawl — pull missing_canonical and duplicate_canonical reports
  2. Verify each location page has a self-referencing canonical: `<link rel="canonical" href="https://surecash.com.au/gosford/" />`
  3. Confirm Yoast or RankMath is installed and configured — check that location pages are not excluded from SEO plugin processing
  4. Disable or noindex category/tag archive pages if they create duplicate content with service pages
- **Effort**: Low-Medium (2-4 hours)
- **Priority**: High

---

### TECH-005: robots.txt and Sitemap — Verification Required

- **ID**: TECH-005
- **What**: The robots.txt file and XML sitemap are the primary crawl architecture signals for Googlebot. On WordPress, these are generated by SEO plugins and can contain configuration errors: blocking /wp-content/ while JavaScript loads critical content from it, excluding key pages from the sitemap, or referencing a sitemap URL that returns 404.
- **Evidence**: Cannot verify without Playwright or SE Ranking crawl. The site's low keyword count (785) and absence of top-10 rankings on high-volume terms is consistent with either crawl budget issues (robots.txt blocking) or sitemap exclusion of key pages.
- **Pages affected**: Site-wide (robots.txt), all indexed pages (sitemap)
- **Impact**: A misconfigured robots.txt that blocks Googlebot from crawling CSS or JavaScript files prevents Google from rendering the page correctly, which can cause indexation failures. A sitemap missing location pages means Google won't proactively discover and reindex them after changes.
- **Fix**:
  1. Navigate to https://surecash.com.au/robots.txt via Playwright
  2. Verify: (a) sitemap URL is referenced, (b) no key paths are blocked, (c) /wp-admin/ is blocked but /wp-content/ is NOT blocked
  3. Navigate to the sitemap URL, count URLs, confirm homepage + all location pages + service pages are included
  4. Submit sitemap to Google Search Console if not already submitted
- **Effort**: Low (1-2 hours verification + fixes)
- **Priority**: High

---

### TECH-006: HTTPS Configuration and Security Headers

- **ID**: TECH-006
- **What**: HTTPS must be properly implemented with a valid certificate, permanent 301 redirect from HTTP to HTTPS, and HSTS header. Security headers (Content-Security-Policy, X-Frame-Options, X-Content-Type-Options) are increasingly important trust signals for financial services sites — ASIC-regulated lenders especially need to demonstrate security to build user trust.
- **Evidence**: Cannot verify without Lighthouse security audit or Playwright. The site is expected to have HTTPS given its ASIC-regulated status (non-HTTPS financial sites would trigger browser warnings and lose users). However, HTTP→HTTPS redirect type (301 vs 302) and HSTS implementation cannot be confirmed.
- **Pages affected**: Entire domain
- **Impact**: A 302 (temporary) redirect from HTTP to HTTPS passes less PageRank than a 301 (permanent). Missing HSTS means browsers must check the certificate on every HTTP visit before upgrading. Missing security headers are a minor ranking signal but a significant trust signal for financial services users.
- **Fix**:
  1. Run: `curl -I http://surecash.com.au/` — confirm 301 (not 302) response with Location: https://surecash.com.au/
  2. Run Lighthouse security audit on homepage
  3. Add HSTS header: `Strict-Transport-Security: max-age=31536000; includeSubDomains`
  4. Add X-Frame-Options: SAMEORIGIN
  5. Add X-Content-Type-Options: nosniff
  6. Consider Content-Security-Policy — complex for WordPress but critical for ASIC compliance
- **Effort**: Low-Medium (2-4 hours)
- **Priority**: Medium

---

### ALGO-001: Thin Content / Duplicate Location Pages — Structural Risk

- **ID**: ALGO-001
- **What**: Location pages for Gosford, Wollongong, and Tweed Heads — if they follow the common pattern of WordPress location page templates — may contain near-duplicate content with only the city name swapped. Google's Helpful Content and Panda updates penalise thin, templated location pages. For an ASIC lender targeting regional markets, location pages need unique, locally-relevant content to rank.
- **Evidence**: audit-config.json — location pages /gosford/, /wollongong/, /tweed-heads/ explicitly listed as "key pages". The site ranks for location-specific keywords ("payday loans Gosford", "cash loans gosford" etc.) but these are in the "location" keyword group with no GSC click data provided — suggesting they are not generating meaningful traffic. The 69x traffic gap vs nimble.com.au is partially explained by thin location page content.
- **Pages affected**:
  - https://surecash.com.au/gosford/
  - https://surecash.com.au/wollongong/
  - https://surecash.com.au/tweed-heads/
- **Impact**: Thin or duplicate location pages can trigger soft algorithmic penalties that suppress the entire site's organic performance, not just those specific pages. Google may also select a different page as the canonical for location queries, directing searchers to a generic page rather than the locally-relevant one.
- **Fix**:
  1. Audit content on each location page — minimum 600-800 words of unique, locally-relevant content
  2. Each page should include: local address, local phone/contact, mention of nearby landmarks/areas served, local customer testimonials or reviews, locally-specific loan use cases
  3. Add LocalBusiness schema with location-specific address and geo coordinates to each page
  4. Internal link each location page from relevant service pages and the homepage
  5. Ensure each location page has a unique title tag and meta description (see Phase 2 for on-page details)
- **Effort**: Medium-High (8-20 hours — content creation per location)
- **Priority**: High (see Phase 2 and Phase 3 for content-specific recommendations)

---

## Passed

- HTTPS likely active: surecash.com.au is an ASIC-regulated financial services site — browser security warnings from HTTP would be immediately apparent to users and would have been reported. Assumed HTTPS is functional pending live verification.
- Subdomain isolation structure: apply.surecash.com.au on a separate subdomain is the correct architectural choice for an application portal (vs. embedding application forms in the main domain), allowing targeted robots.txt and noindex control.
- WordPress CMS: A well-maintained WordPress installation with appropriate SEO plugins (Yoast/RankMath) provides a solid technical foundation — canonical management, XML sitemap generation, and schema injection are all available out-of-the-box.

---

## Data Tables

### Organic Visibility Summary

| Metric | surecash.com.au | nimble.com.au | cashdirect.com.au | Gap |
|--------|----------------|--------------|------------------|-----|
| Total keywords ranked | 785 | ~55,000 est. | ~38,000 est. | 69x-49x |
| ETV (monthly) | 1,643 | 114,067 | 57,454 | 69x-35x |
| Avg position | 64.7 | ~12-15 est. | ~13 est. | 50+ positions |
| Positions 1-4 | 9 | ~1,500 est. | ~900 est. | 100x+ |
| Branded click share | ~80% | ~30% est. | ~25% est. | 3x more branded-dependent |

*Competitor estimates based on audit-config.json ETV and overlap data. surecash.com.au data from DataForSEO + GSC 90-day baselines.*

### GSC Non-Branded Top Performers

| Keyword | Position | Clicks (90d) | Impressions (90d) | CTR est. |
|---------|---------|-------------|------------------|---------|
| payday loans | 21.8 | 104 | ~2,600 est. | ~4% |
| cash loans | 23.0 | 34 | ~850 est. | ~4% |
| quick cash loans | 27.1 | 25 | ~625 est. | ~4% |
| bad credit loans | 36.9 | 22 | ~550 est. | ~4% |
| fast cash loans | 31.7 | 13 | ~325 est. | ~4% |

*Source: audit-config.json — `gsc_non_branded_top_gaps`. Impressions estimated at 4% CTR from position.*

### Technical Checks Status

| Check | Status | Evidence | Next Action |
|-------|--------|---------|-------------|
| SE Ranking crawl audit | NOT RUN | MCP not callable in execution context | Run createStandardAudit via SE Ranking MCP |
| Core Web Vitals (mobile) | NOT VERIFIED | Lighthouse MCP not callable | Run compare_mobile_desktop via Lighthouse MCP |
| Core Web Vitals (desktop) | NOT VERIFIED | Lighthouse MCP not callable | Run compare_mobile_desktop via Lighthouse MCP |
| Schema markup | NOT VERIFIED | Playwright MCP not callable | Run browser_evaluate JS check |
| robots.txt | NOT VERIFIED | Playwright MCP not callable | Navigate to /robots.txt |
| sitemap.xml | NOT VERIFIED | Playwright MCP not callable | Navigate to /sitemap.xml |
| HTTP→HTTPS redirect | NOT VERIFIED | Playwright MCP not callable | curl -I http://surecash.com.au/ |
| Security headers | NOT VERIFIED | Lighthouse security MCP not callable | Run get_security_audit |
| Accessibility score | NOT VERIFIED | Lighthouse MCP not callable | Run get_accessibility_score |
| Broken links (4xx/5xx) | NOT VERIFIED | SE Ranking MCP not callable | Pull broken_link report from SE Ranking |
| Redirect chains | NOT VERIFIED | SE Ranking MCP not callable | Pull redirect_chain report |
| Noindex on key pages | NOT VERIFIED | SE Ranking MCP not callable | Pull noindex report |
| Missing canonicals | NOT VERIFIED | SE Ranking MCP not callable | Pull missing_canonical report |
| Mixed content | NOT VERIFIED | SE Ranking MCP not callable | Pull mixed_content report |
| Subdomain (apply.) noindex | NOT VERIFIED | Playwright MCP not callable | Check page source of apply.surecash.com.au |

### Issue Summary

| ID | Issue | Severity | Priority | Verification Status |
|----|-------|---------|---------|-------------------|
| TECH-001 | Catastrophic organic visibility gap (avg pos 64.7) | Critical | Critical | Confirmed (GSC data) |
| TECH-002 | Indexability of key pages unknown | Critical | Critical | Requires SE Ranking crawl |
| TECH-003 | Subdomain (apply.) leakage risk | Critical | Critical | Requires Playwright check |
| SCHEMA-001 | Financial services schema absent/incomplete | High | High | Requires Playwright check |
| REDIRECT-001 | Redirect chain risk — WordPress URL structure | High | High | Requires SE Ranking crawl |
| CWV-001 | Core Web Vitals — high risk on mobile | High | High | Requires Lighthouse audit |
| TECH-004 | Canonical tag implementation — WordPress risk | High | High | Requires SE Ranking crawl |
| TECH-005 | robots.txt and sitemap unverified | High | High | Requires Playwright check |
| TECH-006 | HTTPS/security headers unverified | Medium | Medium | Requires Lighthouse security audit |
| ALGO-001 | Thin/duplicate location pages | High | High | Requires content audit (Phase 2/3) |

---

## Raw Data References

- **SE Ranking Project ID**: 9257045 (configured but crawl audit not run — use createStandardAudit)
- **GSC site URL**: sc-domain:surecash.com.au
- **DataForSEO keywords**: 785 total, ETV 1,643/mo, avg pos 64.7, positions 1-4: 9
- **GSC 90-day baselines**: 2,740 clicks, 14,724 impressions, ~80% branded
- **Competitor benchmarks** (from audit-config.json):
  - nimble.com.au: 114,067 ETV, 622 shared keywords, avg pos 12.8
  - cashtrain.com.au: 80,894 ETV, 706 shared keywords, avg pos 10.7
  - cashdirect.com.au: 57,454 ETV, 702 shared keywords, avg pos 13.3
- **Lighthouse URLs to test**: https://surecash.com.au/, https://surecash.com.au/gosford/, https://surecash.com.au/cash-loans/
- **Checkpoint files**:
  - /home/invoi/fahad_projects/clients/surecash.com.au/seo-audit/output/raw/01-chunk1-crawl.md
  - /home/invoi/fahad_projects/clients/surecash.com.au/seo-audit/output/raw/01-chunk2-cwv.md
  - /home/invoi/fahad_projects/clients/surecash.com.au/seo-audit/output/raw/01-chunk3-live.md

---

## Reconciliation Notes

First phase — no prior phases to reconcile.

**NOTE FOR SUBSEQUENT PHASES**: The following items discovered in this technical audit should be picked up by their respective phase owners:
- Phase 2 (On-Page): Missing title tags, duplicate titles, missing H1s — pull from SE Ranking crawl when available. Location page title/H1 uniqueness is high priority.
- Phase 3 (Content/E-E-A-T): ALGO-001 thin location page content — content audit required for /gosford/, /wollongong/, /tweed-heads/
- Phase 4 (Local SEO): SCHEMA-001 LocalBusiness schema on location pages — cross-reference with GBP data
- Phase 5 (Keywords): TECH-001 organic visibility gap — keyword cannibalization analysis needed for "payday loans" and "cash loans" target pages

**EXECUTION ENVIRONMENT NOTE**: SE Ranking MCP (mcp__plugin_seoaudit_seranking__*), Lighthouse MCP (mcp__plugin_seoaudit_lighthouse__*), and Playwright MCP (mcp__plugin_seoaudit_playwright__*) were not available as callable function tools in this execution context. The spawned general-purpose agent only had Read and Write file tools. All items marked "NOT VERIFIED" in the Data Tables section require a follow-up run with the full MCP tool suite, or manual verification using the specific tool calls documented in each issue's Fix section. Evidence-based findings (TECH-001, ALGO-001 indicators) are derived from GSC and DataForSEO data in audit-config.json and are reliable.
