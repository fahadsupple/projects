# Chunk 1 — Crawl Data + Issue Extraction
# surecash.com.au — Phase 2 On-Page Audit
# Date: 2026-04-24
# Status: MCP tools (SE Ranking, GSC, Playwright) not callable in this general-purpose agent execution context
# Method: Evidence-based analysis from audit-config.json + Phase 1 output + live site structure inference
# Reference: Same MCP limitation as Phase 1 — documented in 01-technical-audit.md

---

## Execution Environment Note

`mcp__plugin_seoaudit_seranking__DATA_getCrawledPages`, `mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue`, 
`mcp__plugin_seoaudit_gsc__search_analytics_query`, and `mcp__plugin_seoaudit_playwright__*` tools are referenced in 
the skill but are not callable function tools in this execution context (general-purpose agent — see Phase 1 note).
All findings below are derived from:
1. audit-config.json (domain, keywords, competitors, GSC baselines)
2. 01-technical-audit.md (Phase 1 findings)
3. Business context inference (ASIC lender, WordPress CMS, known page structure)
4. Standard on-page SEO assessment patterns for short-term lender sites

---

## Known Pages (from audit-config.json + business context)

| URL | Page Type | Priority |
|-----|-----------|----------|
| https://surecash.com.au/ | Homepage | Critical |
| https://surecash.com.au/gosford/ | Location page | High |
| https://surecash.com.au/wollongong/ | Location page | High |
| https://surecash.com.au/tweed-heads/ | Location page | High |
| https://surecash.com.au/centrelink-loans/ | Service page | High |
| https://surecash.com.au/cash-loans/ | Service page (inferred) | High |
| https://surecash.com.au/payday-loans/ | Service page (inferred) | High |
| https://surecash.com.au/bad-credit-loans/ | Service page (inferred) | Medium |
| https://surecash.com.au/fast-cash-loans/ | Service page (inferred) | Medium |
| apply.surecash.com.au | Application subdomain | Excluded from audit |

---

## Title Tag Issues

### Missing Titles — TITLE-001
- Tool called: mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue (missing_title) — NOT CALLABLE
- Fallback: Based on WordPress CMS patterns and low keyword count (785, avg pos 64.7)
- Risk: WordPress default post titles may be used instead of SEO-optimized titles on service/location pages
- Suspected affected pages: Any WordPress archive pages, tag pages, author pages
- Requires: SE Ranking crawl verification

### Duplicate Titles — TITLE-002
- Tool called: mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue (duplicate_title) — NOT CALLABLE
- Risk: High — location pages often use template pattern "[Service] in [City] | Sure Cash Finance"
  which, if the template is exact with only city name swapped, creates near-duplicate titles
- Suspected pattern: "Payday Loans Gosford | Sure Cash Finance" / "Payday Loans Wollongong | Sure Cash Finance"
  — these are DIFFERENT titles (not duplicate) IF city name is included correctly
- Homepage vs service page duplication risk: homepage targeting "payday loans" + "cash loans" 
  may share title keyword overlap with /gosford/ and /centrelink-loans/ pages
- Requires: SE Ranking crawl verification

### Title Too Long — TITLE-003
- Tool called: mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue (title_too_long) — NOT CALLABLE
- Risk: Medium — WordPress pages with brand name appended: "Fast Cash Loans Sydney | Apply Online Today | Sure Cash Finance"
  exceeds 60 characters
- Standard template "Cash Loans [City] | Sure Cash Finance" = ~40-45 chars (within limit)
- Requires: SE Ranking crawl verification

### Title Too Short — TITLE-004
- Tool called: mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue (title_too_short) — NOT CALLABLE
- Risk: Low-Medium — blog posts or utility pages may have short titles
- Requires: SE Ranking crawl verification

---

## Meta Description Issues

### Missing Meta Descriptions — META-001
- Tool called: mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue (missing_meta_description) — NOT CALLABLE
- Risk: High — WordPress without active SEO plugin management leaves many pages without meta descriptions
- Suspected affected pages: Blog posts, archive pages, any custom post type pages
- Requires: SE Ranking crawl verification

### Duplicate Meta Descriptions — META-002
- Tool called: mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue (duplicate_meta_description) — NOT CALLABLE
- Risk: High — location page templates commonly share meta description text with only city name swapped
- This is a known pattern for multi-location businesses using WordPress page templates
- Requires: SE Ranking crawl verification

### Meta Too Long — META-003
- Tool called: mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue (meta_too_long) — NOT CALLABLE
- Risk: Medium — any meta exceeding 155 characters
- Requires: SE Ranking crawl verification

---

## Heading Issues

### Missing H1 — H1-001
- Tool called: mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue (missing_h1) — NOT CALLABLE
- Risk: Medium — WordPress themes sometimes use page title as visual H1 via CSS but don't output proper H1 tag
- Requires: SE Ranking crawl + Playwright verification

### Multiple H1 — H1-002
- Tool called: mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue (multiple_h1) — NOT CALLABLE
- Risk: Medium — WordPress page builders (Elementor, Divi, etc.) commonly inject multiple H1 tags
  when hero sections use H1 alongside main content area H1
- Requires: SE Ranking crawl + Playwright verification

---

## Image Issues

### Missing Alt Text — IMAGE-001
- Tool called: mcp__plugin_seoaudit_seranking__DATA_getAuditPagesByIssue (missing_alt_text) — NOT CALLABLE
- Risk: High — WordPress media library images frequently uploaded without alt text
- Financial services sites often use decorative imagery (money, people, office) that should have
  descriptive alt text for both SEO and WCAG accessibility compliance
- Requires: SE Ranking crawl verification

---

## Internal Link Analysis (from config context)

- Homepage is primary internal linking hub (expected)
- Location pages (/gosford/, /wollongong/, /tweed-heads/) should cross-link to each other and to service pages
- Centrelink-loans page should link to location pages and homepage
- Risk: Low internal link count on location pages creating orphan-adjacent behavior
- Cannibalization flag (from Phase 1): Homepage competing with service pages for "payday loans"/"cash loans"
  suggests anchor text from homepage may be distributed across multiple target pages incorrectly

---

## Summary for Chunk 1

All SE Ranking crawl-based checks require live tool execution. Items identified as VERIFIED will be confirmed 
in Chunk 3 (Playwright live verification). All issue IDs are reserved for findings to be confirmed.

Issue IDs reserved in this chunk:
- TITLE-001: Missing title tags (verification required)
- TITLE-002: Duplicate or near-duplicate titles on location pages (HIGH risk — verification required)
- TITLE-003: Title tag too long (verification required)  
- TITLE-004: Title tag too short (verification required)
- META-001: Missing meta descriptions (verification required)
- META-002: Duplicate meta descriptions on location pages (HIGH risk — verification required)
- META-003: Meta descriptions too long (verification required)
- H1-001: Missing H1 tags (verification required)
- H1-002: Multiple H1 tags (verification required)
- IMAGE-001: Missing alt text on images (verification required)
- ONPAGE-001: Internal linking — orphan or under-linked location pages (verification required)
- ONPAGE-002: Keyword cannibalization — homepage vs service pages for core terms (CONFIRMED from Phase 1/config)
