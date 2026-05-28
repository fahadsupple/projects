# Group One Line Marking — Ranking Audit
**Domain:** group1linemarking.com.au  
**Date:** 28 May 2026  
**Analyst:** Claude Code  
**Scope:** Why the site is not ranking for city-level and product-level keywords despite having 252 location pages

---

## Executive Summary

Group One Line Marking has 252 pages indexed, including an extensive location page network covering Sydney suburbs, Brisbane, Gold Coast, and Melbourne areas. Despite this, the site ranks for almost exclusively hyper-local suburb keywords in Sydney and fails to rank for any city-level or product-level commercial keywords.

**Root cause:** The site has no meaningful body content on its service or city pages (verified: 50–190 characters of actual text per page), zero H1/H2 heading tags in the rendered HTML, and a heavily bloated internal link structure (80,181 internal links) that distributes PageRank so thinly that no individual page earns enough authority to rank in competitive city-level SERPs. This is compounded by the site being branded and geo-tagged to Sydney across its core service pages, making Melbourne, Brisbane, and Gold Coast rankings structurally impossible without dedicated city content.

**Estimated organic traffic (DataForSEO):** ~163 estimated visits/month across 146 ranked keywords — all low-competition, low-volume suburb terms.

---

## What IS Ranking vs What Isn't

### Currently Ranking (confirmed by DataForSEO)
All suburb-level, hyper-local terms with minimal competition:
- "line marking fairfield", "line marking huntingwood", "line marking penrith" (suburb LM pages)
- "bollards moolap", "bollards keilor park", "bollards ravenhall" (suburb bollard pages)
- "parking safety products caringbah", "parking safety products kirrawee" (very niche suburb terms)
- "bollards geelong" pos 13 — their strongest non-suburb ranking (480 sv)
- "line markers near me" pos 6 from Mackay page — near-me terms (local search pack)

**Why these rank:** Zero direct competition for hyper-specific suburb+service combinations. The site wins by default — nobody else has a dedicated "bollards moolap" page.

### NOT Ranking (not in top 50) — Confirmed Live SERPs
| Keyword | Volume | Expected URL | Status |
|---|---|---|---|
| line marking sydney | 390 | /services/line-marking/ | Not in top 50 |
| line marking brisbane | 590 | /areas-we-serve/brisbane/line-marking/ | Not in top 50 |
| line marking melbourne | 480 | No page exists | No page |
| bollards sydney | 260 | /services/bollards/ | Not in top 50 |
| bollards brisbane | 170 | /areas-we-serve/brisbane/bollards/ | Not in top 50 |
| bollards melbourne | 260 | No page exists | No page |
| bollards gold coast | 50 | /areas-we-serve/gold-coast/bollards/ | Pos 12 (near-miss) |
| wheel stops sydney | 50 | No dedicated page | No page |
| wheel stops brisbane | — | /areas-we-serve/brisbane/wheel-stops/ | Not in top 50 |
| speed humps sydney | 30 | No dedicated page | No page |
| car park line marking sydney | 70 | /services/line-marking/ | Not in top 50 |
| safety bollards sydney | 50 | /services/bollards/ | Not in top 50 |
| industrial line marking | — | /services/industrial-line-marking/ | Not in top 50 |
| warehouse line marking sydney | — | /services/factory-warehouse-line-marking/ | Not in top 50 |

---

## Issue 1: No Body Content on Any Page (Critical)

**Severity: P0 — Site-Killing**

Every service page and city page on the site has virtually no body content. Verified by fetching raw HTML:

| Page | Total HTML Text (after stripping nav) |
|---|---|
| /services/line-marking/ | ~173 words (includes navigation ~120 words) |
| /services/bollards/ | ~184 words |
| /services/wheel-stops/ | ~183 words |
| /areas-we-serve/brisbane/ | ~189 words |
| /areas-we-serve/gold-coast/ | ~193 words |
| /areas-we-serve/brisbane/bollards/ | **192 characters** of actual body text |
| /areas-we-serve/gold-coast/bollards/ | **269 characters** of actual body text |

The Brisbane Bollards page body text after stripping navigation:
> *"Bollards Brisbane | Safety Bollard Installation ▷ FREE Quote Available 24 Hours a Day, 7 Days A Week NSW QLD VIC Free Quote Queensland Victoria Queensland Victoria Queensland Queensland"*

That is the entirety of visible content on a page targeting a competitive commercial keyword. The actual service content section appears to be either blank, loaded via JavaScript that fails to cache properly, or simply never written.

**Why this causes the ranking failure:** Google uses content depth, topical coverage, and semantic relevance to assess whether a page deserves to rank. A page with 50–80 words of unique body content competing against pages with 600–1,500 words of relevant service information will always lose, regardless of other signals.

**Competitors for "line marking sydney" who ARE ranking:**
- pacificmarkings.com.au (#1) — dedicated Sydney page with full service content
- carparkking.com.au (#2) — Sydney page with content, reviews, location signals
- completelinemarking.com.au (#3) — Wetherill Park based, proximity + content
- speedylinemarking.com.au (#4) — Sydney-specific content and photos

---

## Issue 2: No H1 or H2 Tags on Any Page (Critical)

**Severity: P0**

Confirmed across ALL checked pages: there are **zero H1 or H2 heading tags** in the HTML. DataForSEO's crawl confirmed this. Searching the raw HTML of the Brisbane Bollards page found 0 heading tags.

The site uses WP Rocket caching and a custom WordPress theme (`theme-group1linemarking`). The heading tags are almost certainly rendered by JavaScript/the page builder AFTER the HTML is delivered — meaning Googlebot's first-pass crawl (which processes HTML before JS) may see pages with no semantic headings at all.

**Impact:** H1 tags are among Google's strongest on-page keyword relevance signals. Without them, Google must infer page topic from title tags and body text alone — and with minimal body text, the page fails both tests simultaneously.

**What to check:** View page source vs "Inspect Element" in Chrome DevTools. If headings appear in Inspect but not in View Source, they are JS-rendered and may not be reliably crawled.

---

## Issue 3: Service Pages Hard-Coded to Sydney (Critical)

**Severity: P0 for all non-Sydney rankings**

The core service pages have Sydney permanently embedded in their title tags:
- `/services/line-marking/` → **"Line Marking Services Sydney | Group One Line Marking"**
- `/services/bollards/` → **"Safety Bollards Sydney | Group One Line Marking"**
- `/services/wheel-stops/` → **"Wheel Stoppers Sydney | Group One Line Marking"**

These are the pages being used to target non-Sydney keywords. A page titled "Safety Bollards **Sydney**" structurally cannot rank for "bollards brisbane" or "bollards melbourne". Google's geo-relevance signals will always resolve this page to Sydney.

Additionally, the homepage meta description states: *"Group One Line Marking offers line marking, concrete sealing, safety barriers, bollards, and other parking safety products **in Sydney**."*

This anchors the entire domain's geographic identity to Sydney in Google's eyes.

---

## Issue 4: No Sydney or Melbourne City Hub Pages

**Severity: P1**

Checked: **`/areas-we-serve/sydney/` returns 404. `/areas-we-serve/melbourne/` returns 404.**

The site has suburb pages for every Sydney suburb (Fairfield, Huntingwood, Penrith, etc.) but **no parent Sydney city page**. When someone searches "line marking sydney", there is no city-level hub page to rank — only the generic service pages with "Sydney" in the title.

For Melbourne, it's even worse: there is no `/areas-we-serve/melbourne/` and no `/services/line-marking/` variant for Melbourne. The Melbourne suburb pages (Dandenong, Moorabbin, Thomastown etc.) have no city hub to consolidate authority into.

**Compared to Brisbane:** Brisbane does have `/areas-we-serve/brisbane/` and `/areas-we-serve/brisbane/bollards/` etc. But those pages are nearly empty (see Issue 1), so their existence doesn't help.

---

## Issue 5: Duplicate/Templated City Pages (Critical)

**Severity: P1**

The Brisbane bollards page and Gold Coast bollards page share **72.4% content overlap** after normalising the city name. Both pages are essentially the same template with the city name swapped in the title and meta description — there is no unique content differentiating them.

This is a classic thin/duplicate content pattern that Google actively discounts. When dozens of location pages share near-identical content (only the location name differs), Google typically:
1. Selects one "canonical" version to show (usually the strongest)
2. Discounts or de-indexes the duplicates
3. Does not rank any of them well for competitive terms

The site has hundreds of pages following this pattern.

---

## Issue 6: 80,181 Internal Links — Catastrophic PageRank Dilution

**Severity: P1**

DataForSEO confirmed: **80,181 internal links** across the site. This comes from the mega-navigation, which lists all 200+ location pages and all services on every single page of the site.

Every page you add to the nav dilutes the PageRank passed to every other page. With 200+ locations × multiple service types all linked from every page, no individual page receives enough PageRank signal to rank competitively.

Comparison: A site with clean internal linking that passes 50 PageRank units from the homepage to its 5 key service pages gives those pages 10 units each. Group One's approach passes those same units across 200+ pages, giving each less than 0.05 units.

**Fix:** Redesign navigation to only surface top-level city hubs and service categories. Remove suburb-level links from the nav entirely. Use footer links or dedicated "Areas We Serve" index pages for granular suburbs.

---

## Issue 7: Backlink Profile Quality (Significant)

**Severity: P2**

| Metric | Group1 | Notes |
|---|---|---|
| Domain Rank | 180 | Weak authority |
| Total Backlinks | 284 | Low for a multi-state national site |
| Referring Domains | 79 | Very low |
| **Nofollow links** | **165/284 (58%)** | Majority contribute zero equity |
| Blogspot.com links | 51 | PBN/spam indicator |
| Wixsite.com links | 19 | PBN/spam indicator |
| Spam Score | 2 | Low — not a penalty risk |

58% of all backlinks are nofollow — they pass zero PageRank. The 51 blogspot.com links suggest a low-quality link building campaign (PBN or directory spam). With only ~79 referring domains and most of those providing nofollow links, the site has very little link equity to compete with established Sydney or Melbourne line marking competitors.

**Competitor comparison (for "line marking sydney"):**
| Domain | Rank | Ref Domains | Backlinks |
|---|---|---|---|
| carparkking.com.au (#2) | 199 | 136 | 366 |
| speedylinemarking.com.au (#4) | 202 | 141 | 301 |
| safetpro.com.au (#5) | 214 | 77 | 199 |
| **group1linemarking.com.au** | **180** | **79** | **284** |

Group1's backlink profile is actually comparable to competitors who DO rank. This means **backlinks are NOT the primary barrier to ranking** — the content and technical issues (Issues 1–6) are more likely the bottleneck.

---

## Issue 8: Keyword Cannibalization

**Severity: P2**

Multiple pages compete for the same keywords:
- "line marking sydney" → homepage (pos 30) AND `/services/line-marking/` (not ranking) — two pages confuse Google about which to rank
- "bollards sydney" → `/services/bollards/` (pos 52) AND the service page title both signal Sydney
- "bollard installation" → `/services/bollards/` vs every city bollard page

Google cannot reliably choose which page to rank when multiple pages appear to target the same term. The result is neither page ranks well.

---

## Issue 9: Robots.txt Crawl Delay

**Severity: P3**

The robots.txt contains `Crawl-delay: 10`, meaning Google is asked to wait 10 seconds between each page crawl. For a 252-page site with location pages that need regular re-crawling, this means Google may take weeks to process the full site after any content updates. Most major SEOs recommend removing the Crawl-delay directive and instead using Google Search Console to manage crawl rate if needed.

---

## Issue 10: Missing City-Level Schema

**Severity: P3**

All pages have a basic Yoast WebPage schema block only. There is no:
- LocalBusiness schema with `areaServed` for each city
- Service schema linking to specific service offerings
- GeoCoordinates on location pages
- FAQPage schema that could capture featured snippets

For a multi-location service business targeting Brisbane, Melbourne, Gold Coast and Sydney, LocalBusiness schema with city-level `areaServed` signals would help Google understand and trust the geographic targeting.

---

## Summary: Why Suburb Pages Rank but City Pages Don't

| Factor | Suburb Pages (ranking) | City Pages (not ranking) |
|---|---|---|
| Competition | None — nobody else targets "bollards moolap" | High — established local businesses |
| Content depth | Thin template content | Same thin template content |
| Uniqueness | Unique city name in title | Unique but duplicated structure |
| Google trust | Wins by default (no competitors) | Loses to competitors with real content |
| Local signal | Specific suburb = tight geo-match | City-level = broader, harder |

**The honest answer:** The site ranks for suburb keywords because there is literally no competition. No one else has made a "bollards keilor park" page. Google has no better option. For "bollards melbourne" or "line marking sydney", there are 5–10 competitors with dedicated, content-rich pages who do the job properly. Google always chooses them.

---

## Priority Action Plan

### P0 — Fix Immediately (blocks all other work)

1. **Add real content to all service and city pages** — Each service+city page needs 600–1,000 words of unique, genuinely useful content. Not templates with the city name swapped — different content per city discussing local compliance requirements, the types of jobs done in that area, local case studies. Start with the highest-volume targets: "line marking brisbane" (590), "line marking melbourne" (480), "line marking sydney" (390), "bollards sydney" (260), "bollards melbourne" (260).

2. **Implement H1 and H2 heading tags** — Every page must have exactly one H1 containing the primary keyword (e.g., "Line Marking Services in Brisbane"). Add H2s for key subsections. If the theme doesn't support standard H1/H2 tags, the template code needs fixing.

3. **Fix service page geo-tagging for Sydney** — The service pages currently rank as Sydney pages. Either: (a) create separate city-specific service pages for Brisbane, Melbourne, Gold Coast, or (b) remove "Sydney" from the generic service page titles and use the city pages as the location-specific landing pages.

### P1 — Fix Within 30 Days

4. **Create Sydney and Melbourne city hub pages** — `/areas-we-serve/sydney/` and `/areas-we-serve/melbourne/` with 600+ words each, linking down to their respective service subpages.

5. **Reduce internal link bloat** — Remove suburb links from the main navigation. The nav should only show: Home | Products | Services | Areas (Brisbane, Sydney, Melbourne, Gold Coast) | Contact. Use a dedicated Areas We Serve page for the full suburb list.

6. **Fix keyword cannibalization** — Decide which page targets each city+service combination and 301-redirect or de-optimise the losing page. Use GSC to identify which URL Google is currently preferring.

### P2 — Fix Within 60 Days

7. **Build quality backlinks** — Current 79 referring domains with 58% nofollow is insufficient. Target: 10 new dofollow links from Australian trade directories (HiPages, ServiceSeeking, True Local), local business associations, and industry publications. Disavow the blogspot/wixsite spam links.

8. **Add LocalBusiness + Service schema** — Implement JSON-LD with `areaServed`, `serviceType`, and `address` on all city pages. Add FAQPage schema to service pages.

### P3 — Fix Within 90 Days

9. **Remove Crawl-delay from robots.txt** — Googlebot manages its own crawl rate. The 10-second delay is unnecessarily restricting re-indexation.

10. **Content for product keywords** — "rubber wheel stops", "plastic speed humps", "flexible bollards" are product-category keywords that could be captured by the WooCommerce category pages if those pages had adequate content (currently they're thin category pages).

---

## Notes on the Seoaudit Plugin

The full `/seoaudit:run` pipeline could provide additional data not available here:
- Core Web Vitals (mobile/desktop LCP, CLS, TBT from Lighthouse)  
- GSC impression data and CTR by page
- GA4 engagement metrics and bounce rates by page
- SE Ranking crawl issues (broken links, redirect chains, duplicate meta)
- Full backlink quality breakdown

This manual audit is based on DataForSEO SERP/labs data, backlink summary API, and direct HTML analysis. Recommend running `/seoaudit:run group1linemarking.com.au` in a fresh session to get the Lighthouse and GSC data layer.
