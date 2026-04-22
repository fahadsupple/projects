---
name: surecash.com.au project context
description: Sure Cash Finance — ASIC-regulated short-term lender, SEO audit complete Apr 2026
type: project
---

Sure Cash Finance (surecash.com.au) — ASIC-regulated short-term cash loan lender, Sydney HQ.

**Why:** SEO audit completed Apr 2026. Business is SACC/MACC lender operating under ACL 390591 (Shimtec Pty Ltd ACN 001928516), AFCA #43334. Regulatory constraints apply to all content.

**How to apply:** Treat any content or keyword recommendations with awareness of ASIC responsible lending obligations and NCCP Act. Do not recommend content that implies guaranteed approval, targets vulnerable groups, or makes claims that could breach AFCA/ASIC standards.

---

## Business Profile

| Field | Value |
|---|---|
| Legal entity | Shimtec Pty Ltd |
| ACN | 001928516 |
| ACL | 390591 |
| AFCA # | 43334 |
| Products | SACC $300–$2,000 / MACC $2,001–$5,000 |
| Branches | Sydney (HQ), Gosford, Wollongong, Tweed Heads |
| CMS | WordPress 6.9.4 + WPBakery + Yoast SEO + WP Rocket |
| Theme | DT The7 v14.3.1 |
| Apply subdomain | apply.surecash.com.au (Microsoft IIS — different server) |
| Server | LiteSpeed, PHP 8.3.30 |

---

## SE Ranking

- **Project ID:** 9257045
- **Tracked keywords:** 100
- **Critical note:** Rankings in SE Ranking are almost entirely `local_pack` type (Google Business Profile / Maps), NOT organic. This significantly impacts strategy — local pack improvements ≠ organic SEO wins.

---

## Baseline Metrics (as of Apr 2026)

| Metric | Value |
|---|---|
| Domain Authority (InLink Rank) | 29 |
| Total keywords (DataForSEO) | 785 |
| Estimated monthly traffic value | 1,643 |
| Avg position | 64.7 |
| Keywords in top 10 | 9 |
| GSC clicks (90d, homepage) | 2,822 at avg pos 24 |
| Branded query share (approx) | ~70% |

**Top GSC pages (90d clicks):**
- `/gosford/` — 456 (404 ERROR — redirect missing)
- `/centrelink-loans/` — 369 (404 ERROR — redirect missing)
- `/tweed-heads/` — 302 (404 ERROR — redirect missing)
- `/wollongong/` — 283 (404 ERROR — redirect missing)

**SE Ranking trend:** Improving — top-3 positions grew 20→28, not-ranking shrank 16→4.

**Key mover:** "loans on centrelink" (22,200 vol) moved pos 80→42.

**New entrants at pos 70–80:** "payday loans" (33,100), "cash loans" (22,200), "same day loans" (6,600).

---

## Top Organic Competitors

| Domain | DataForSEO ETV/mo |
|---|---|
| nimble.com.au | 114,067 |
| cashtrain.com.au | 80,894 |
| cashdirect.com.au | 57,454 |
| fundo.com.au | 29,407 |
| credit24.com.au | 21,492 |

---

## Audit Status

- **Initialized:** 2026-04-22
- **Audit completed:** 2026-04-22
- Phase 1 (Technical): COMPLETE
- Phase 2 (On-Page): COMPLETE
- Phase 3 (Content): COMPLETE
- Phase 4 (Local): COMPLETE
- Phase 5 (Keywords): COMPLETE
- Phase 6 (Backlinks): COMPLETE
- Report: COMPLETE — `/home/invoi/fahad_projects/clients/surecash.com.au/seo-audit/report.html`

---

## Key Audit Findings (Apr 2026)

### Critical Issues (4)
1. **4 missing 301 redirects** — 1,410+ clicks/90d lost to 404 errors from URL migration
   - /gosford/ → /service-areas/gosford/
   - /centrelink-loans/ → /loans/loans-for-people-on-centrelink/
   - /tweed-heads/ → /service-areas/tweed-heads/
   - /wollongong/ → /service-areas/wollongong/
2. **HTTP does not redirect to HTTPS** — http:// serves site without redirect
3. **20+ service area pages are 98%+ duplicate content** — near-clone template pages for non-branch cities
4. **4 admin pages publicly indexed** — /leads/, /citations/, /brand-page/, /lm-buy/

### Key Technical Flags
- WordPress user enumeration exposed via /wp-json/wp/v2/users
- Sitemap index uses HTTP URLs (fix: set WP Site URL to HTTPS)
- user-scalable=0 on viewport (WCAG violation)
- Blog category/tag pages indexed with no unique content
- Homepage canonical missing trailing slash
- Title typo: Tweed Heads page says "Headss"

### Key On-Page/Content Flags
- 6 important pages have no meta description
- 9 loan amount pages are 92–96% identical
- FAQ sections only 3 items per page (competitors have 8–12)
- No LocalBusiness schema on any branch location page
- No physical addresses on any branch page
- Branch pages missing opening hours, phone numbers, map embeds

### Key Opportunity Flags
- /loans/same-day-loans/ — site ranking at 70-80 for 6,600/mo keyword without a page
- /loans/online-loans/ — major competitor keyword, no surecash presence
- Finder.com.au product listing — high-DA link + referral traffic
- AFCA/ASIC directory listings — ensure URLs are correct

### ASIC Compliance Status
- COMPLIANT: Warning About Borrowing page, ACL/AFCA disclosures, responsible lending all present

---

## GA4 Warning
`plugin:seoaudit:ga4` not connecting. Phases 2 and 5 used GSC + SE Ranking fallback.
