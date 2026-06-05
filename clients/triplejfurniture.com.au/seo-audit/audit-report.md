# Triple J Furniture — Full SEO Audit
**URL:** https://triplejfurniture.com.au/  
**Date:** 5 June 2026  
**Auditor:** Claude Code / SEO Skill  
**SEO Health Score: 42 / 100**

---

## Score Breakdown

| Category | Weight | Raw Score | Weighted |
|----------|--------|-----------|----------|
| Technical SEO | 22% | 43/100 | 9.5 |
| Content Quality | 23% | 50/100 | 11.5 |
| On-Page SEO | 20% | 48/100 | 9.6 |
| Schema / Structured Data | 10% | 18/100 | 1.8 |
| Performance (CWV) | 10% | 28/100 | 2.8 |
| AI Search Readiness | 10% | 55/100 | 5.5 |
| Images | 5% | 38/100 | 1.9 |
| **TOTAL** | **100%** | — | **42.6** |

---

## PERCEIVE — What We Observe

### Business Context (OBSERVE-INTERNAL)
- **Platform:** Shopify (detected: Timber theme — legacy free theme, circa 2014–2016)
- **Products:** Furniture (lounges/sofas, dining, bedroom, coffee tables, bar stools, outdoor)
- **Location:** 590 Hume Hwy, Yagoona NSW 2199 — showroom + national online
- **Authority:** DR 8 (very low — all keyword targeting must avoid chain-dominated SERPs)
- **Catalog size:** 2,150 products, 91 collection pages, 19 static pages
- **Active keyword strategy:** Sydney-focused Plan 2 (local lounges subcategories) + national Plan 3 (material/style sub-categories: travertine, marble, chesterfield, timber variants) in progress

### Competitive Landscape (OBSERVE-EXTERNAL)
- Reject list: Harvey Norman, IKEA, Freedom, Amart, Nick Scali, Temple & Webster, Plush
- Winnable SERPs: boutique specialists (Sydney Furniture Factory, Known for Lounges, Monster Furniture, Glicks, Demir Leather, Shack) hold top positions on local/material variants
- DR 8 is competitive against these boutiques at KD < 15

---

## CRITICAL FINDINGS

### C1 — Outdated Shopify Theme (Timber, ~2014) — Performance Emergency
**THINK:** The site is running the legacy Shopify "Timber" theme, confirmed by:
- `timber.js` loading in assets
- `jquery-1.12.0.min.js` (January 2016)
- `html5shiv` (IE8 polyfill — redundant since ~2016)
- `respond.min.js` (IE9 media query polyfill — redundant)
- `modernizr-2.8.3` (2014-era feature detection)
- 111 JavaScript `<script>` tags on homepage

The result: homepage HTML is **442KB** (extreme). Google's mobile-first indexing measures CWV on the slowest device. With this JS stack, INP and LCP are almost certainly in Poor territory.

**CONNECT-system:** Fixing this is the single highest-leverage action. A theme migration unlocks: faster LCP/INP, lazy-loaded images, modern image formats (WebP/AVIF), better mobile rendering, and compatibility with Shopify's 2.0 app ecosystem. Every other performance recommendation is blocked by this.

**ACCEPT (how to know it failed):** Run PageSpeed Insights after theme migration. LCP should drop below 2.5s and INP below 200ms on mobile. If scores remain poor after migration, an app is injecting scripts.

**GROW (leading indicator):** Monitor Core Web Vitals in Google Search Console > Experience report. LCP and INP trend line.

---

### C2 — 91 Indexable Collection Pages: 20+ Duplicates Without noindex or Canonical Fix
**THINK:** The collections sitemap contains 91 URLs. Of these, at least 20 are duplicates, stub collections, or internal-use pages that are indexable and self-canonicalized (each pointing only to itself):

| Problem Collection | Issue |
|---|---|
| `/collections/shop-all` | Internal aggregator — thin |
| `/collections/shop-all-1` | Duplicate of shop-all |
| `/collections/shop-all-2` | Duplicate of shop-all |
| `/collections/shop-all-3` | Duplicate of shop-all |
| `/collections/console-table` + `/collections/console-table-1` | Duplicate pair |
| `/collections/storage` + `/collections/storage-1` | Duplicate pair |
| `/collections/table` + `/collections/table-1` | Duplicate pair |
| `/collections/mirrors` + `/collections/mirror` | Singular/plural duplicate |
| `/collections/uncategorized` | Internal Shopify default — no real products |
| `/collections/frontpage` | Homepage featured collection — should not be indexed |
| `/collections/the-enterance` | Misspelled ("entrance"), purpose unclear |
| `/collections/centrum` | Brand name collection — unknown if SEO-targeted |
| `/collections/new-arrivals`, `/collections/feature-products`, `/collections/new-collection`, `/collections/best-selling-collection` | Non-editorial aggregator pages — thin |

**Impact:** Google is allocating crawl budget to 20+ pages that provide no ranking value. These pages also fragment internal link equity across near-identical content. At DR 8, wasted crawl budget has a measurable ranking cost.

**CONNECT-system:** Must be resolved before investing in new collection pages. Every new SEO page competes for crawl budget against this bloat.

**ACCEPT:** After fixes, run Screaming Frog to verify these collections return 301 (merged) or contain `<meta name="robots" content="noindex,follow">`. Check Google Search Console > Coverage report — "Excluded" count should rise, "Valid" count should fall by ~20.

**GROW:** Monitor total pages in Google's index via `site:triplejfurniture.com.au` — should reduce from current inflated count.

---

### C3 — /pages/sawce-data-feed Publicly Indexed
**THINK:** `/pages/sawce-data-feed` is in the sitemap, returns 200, and has no noindex. This appears to be a product feed integration page (Sawce is a price comparison/feed tool). It is likely full of raw product data — duplicate content at scale.

**CONNECT-system:** Block immediately via noindex or robots.txt Disallow before any new content investment.

**ACCEPT:** Confirm page is excluded from Google index: search `site:triplejfurniture.com.au sawce`. Should return 0 results after fix.

---


### C4 — ABN Discrepancy: Onboarding Says 95 123 587 173, Live Site Shows 92 123 587 173
**THINK:** The onboarding form recorded ABN 95 123 587 173. The live footer displays ABN **92 123 587 173**. These are different ABNs. This has two consequences:
1. **Legal/trust risk:** Incorrect ABN display on a commercial website is a consumer law concern. If 92 is the correct ABN, the client data we hold is wrong and any previous directory submissions with the old number are inconsistent.
2. **E-E-A-T impact:** Google uses entity consistency signals. ABN inconsistency across citations, schema markup, and the site itself degrades entity trustworthiness.

**Action:** Confirm correct ABN with client immediately. Update: (a) footer, (b) Organization schema, (c) Google Business Profile, (d) ASIC/ABN registry if needed.

**ACCEPT:** Search Google for both ABNs. The correct one should resolve to the client on ABN Lookup (https://www.abn.business.gov.au/).

---

### C5 — Warranty Claim Contradiction: "Up to 10 Years" Marketing vs "1 Year" Policy Page
**THINK:** Every collection page and the homepage prominently promotes "warranty up to 10 years." The `/pages/warranty-policy` page states warranty is for "one year from date of purchase" with no 10-year tier mentioned.

This is a **Critical E-E-A-T trust signal failure** and a potential legal liability:
- Google QRG evaluates whether claims on a site are substantiated — unsubstantiated marketing claims are a trust penalty risk
- ACCC guidelines (Australia) require warranty claims to be accurate
- A customer who buys on the strength of a 10-year warranty claim and receives a 1-year warranty could lodge a chargeback or ACCC complaint

**Action:** Either (a) update the warranty policy page to correctly describe all warranty tiers (1-year standard + 10-year on specific product lines), or (b) remove the 10-year claim from marketing until the policy is corrected. This must be escalated to the client before any further SEO work is done.

**ACCEPT:** The warranty policy page and every collection page should make identical warranty claims with no contradiction.

---

### C6 — Product Schema: No Offers Block, aggregateRating 0/0 on All Products
**THINK:** Shopify's TrustShop app injects Product schema via JavaScript (`DOMContentLoaded`). This means Google's crawler, which does not wait for JS execution during initial crawl, likely does not see this schema. The injected schema also has critical validity errors:
- **No `Offers` block** — price, availability, and currency are missing. Without these, products cannot qualify for Google Shopping rich results or price display in SERPs
- **aggregateRating: 0/0** — zero rating count is invalid markup per schema.org. Google may suppress all rich results for products with invalid aggregateRating

**Action:** Add static (server-side rendered) Product JSON-LD to the product template in `product.liquid` with a complete Offers block. Do NOT rely on JS injection. Sample:
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{{ product.title }}",
  "sku": "{{ product.variants.first.sku }}",
  "brand": { "@type": "Brand", "name": "Triple J Furniture" },
  "offers": {
    "@type": "Offer",
    "price": "{{ product.price | divided_by: 100.0 }}",
    "priceCurrency": "AUD",
    "availability": "{% if product.available %}https://schema.org/InStock{% else %}https://schema.org/OutOfStock{% endif %}",
    "url": "{{ shop.url }}{{ product.url }}"
  }
}
```

**ACCEPT:** Run Google Rich Results Test on 5 product pages. Each should return a valid Product schema with Offers and a green result.

---

## HIGH FINDINGS

### H1 — URL Mismatch: Keyword Plan Targets Non-Existent URLs
**THINK:** The keyword plan was written assuming URL slugs that don't match the live site:

| Keyword Plan URL | Actual Live URL | Impact |
|---|---|---|
| `/collections/sofas-lounges` | `/collections/lounges-and-sofas` | Primary lounge page |
| `/collections/chaise-lounges` (plural) | `/collections/chaise-lounge` (singular) | Chaise target page |
| `/collections/modular-sofas` | `/collections/modular-lounges` | Modular target |
| `/collections/recliner-chairs` | `/collections/recliner-chairs` ✅ | OK |
| `/collections/leather-lounges` | `/collections/leather-lounges` ✅ | OK |

The plan must be updated to reflect actual URLs. Any backlink outreach or internal link building to the planned (wrong) URLs will return 404s or be wasted.

Additionally, Plan 3 target pages **do not yet exist** as dedicated collections:
- No `/collections/marble-coffee-tables`
- No `/collections/chesterfield-sofas`
- No `/collections/travertine-coffee-table` or similar
- `/collections/dining-table` exists but targets "Dining Table" generically (no "marble dining table" targeting)

**ACCEPT:** Audit all internal links pointing to Plan 2 URLs and confirm they use the correct live slugs.

---

### H2 — No Organization/LocalBusiness Schema on Homepage
**THINK:** The homepage has FAQPage and Product schema but no Organization or LocalBusiness schema. With a physical showroom (590 Hume Hwy, Yagoona NSW 2199) and 25+ years of operation, this is a missed trust signal. Google uses Organization schema to build knowledge graph entities.

Missing fields: `@type`, `name`, `url`, `telephone`, `address` (PostalAddress), `openingHours`, `priceRange`, `geo`, `logo`, `sameAs` (linking to Google Business, Facebook, LinkedIn).

**JSON-LD to add to homepage:**
```json
{
  "@context": "https://schema.org",
  "@type": "FurnitureStore",
  "name": "Triple J Furniture",
  "url": "https://triplejfurniture.com.au",
  "telephone": "+61297902588",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "590 Hume Hwy",
    "addressLocality": "Yagoona",
    "addressRegion": "NSW",
    "postalCode": "2199",
    "addressCountry": "AU"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "09:00",
      "closes": "17:00"
    }
  ],
  "priceRange": "$$",
  "description": "Triple J Furniture is a Sydney furniture store offering quality lounges, dining, and bedroom furniture with a Price Beat Guarantee and up to 10-year warranty.",
  "foundingDate": "1997",
  "areaServed": "Australia"
}
```

---

### H3 — No Structured Data on Collection Pages
**THINK:** Collection pages have zero JSON-LD schema. At minimum, every collection page should have BreadcrumbList. High-priority collection pages should also have ItemList (listing products with name, URL, image, price). This directly affects:
1. Breadcrumb display in Google SERP
2. Rich result eligibility for product listings
3. AI citability of collection pages

Current state: No schema detected on `/collections/lounges-and-sofas` or `/collections/coffee-tables`.

**ACCEPT:** Use Google Rich Results Test on 3 collection pages. Should return BreadcrumbList valid.

---

### H4 — Homepage Keyword Targeting Inconsistency
**THINK:** The homepage is optimised for "affordable furniture sydney" (H1, title, H2s, meta description). The keyword plan specified "furniture store sydney" (6,600/mo) as the homepage entity-building signal. "Affordable furniture sydney" is a different SERP with different intent and competition.

This isn't necessarily wrong — "affordable" furniture searches may convert better. But it was not in the keyword plan, meaning keyword research was done for one target and the page was built for another. The client and Supple team need to align.

Additionally: "affordable" is a low-trust modifier for premium/warranty positioning. The site claims 10-year warranty and Price Beat Guarantee — messaging consistency with brand positioning should be reviewed.

---

### H5 — Location Suburb Pages: Likely Templated Content
**THINK:** 7 suburb pages exist in the sitemap:
- Bankstown, Liverpool, Auburn, Potts Hill, Sefton, Condell Park, Greenacre, Campsie

Each shows ~1,300 word count — but the Bankstown page excerpt reveals most of the "content" is navigation menu items being counted as body text. Actual unique body copy is almost certainly under 300 words per page.

These pages are all from the /pages/ namespace and targeting "[suburb] furniture store" variants. At 7 pages they don't hit the quality gate warning threshold (30 pages), but if expanded without genuine unique content they will become a thin content risk.

**ACCEPT:** Use a word count tool to measure text *excluding* navigation elements (header, footer, nav menus) on 3 pages. If unique body copy < 400 words per page, flag as thin content.

---

### H6 — /collections/dining-table Has No Meta Description
**THINK:** The dining table collection page (/collections/dining-table) has:
- Title: "Dining Table | Triple J Furniture" (generic — no keyword targeting)
- H1: "Dining Table" (no keyword)
- Meta description: MISSING

This page is in the sitemap and likely has products. For Plan 3 targeting "marble dining table" (5,400/mo) this page needs to be either retargeted or a new `/collections/marble-dining-tables` collection created.

---

## MEDIUM FINDINGS


### M6 — OG Tags Duplicated + Errors in `<head>`
**THINK:** Schema agent found that the Shopify theme double-renders Open Graph meta tags — 18 OG tags on product pages where there should be 9. Additionally:
- `og:image` uses `http://` (not `https://`) — insecure; `og:image:secure_url` exists as fallback but this is sloppy
- `og:site_name` has a trailing space: `"Triplejfurniture "` — should be `"Triple J Furniture"` (with proper capitalisation and spacing)

These affect social sharing previews and can confuse social platforms' scrapers. Fix in the theme's `head.liquid` partial.

---

### M1 — FAQPage Schema on Commercial E-commerce Homepage
**THINK:** FAQPage with 8 questions is present on the homepage. Google restricted FAQ rich results to government and healthcare sites in August 2023. These FAQs will NOT generate rich results in Google SERPs.

However, FAQPage **does** have LLM/AI citation value — AI tools (ChatGPT, Perplexity, Google AI Overviews) use FAQ schema as a structured source for question answering. The 8 questions should be reviewed for quality and topical relevance to the target keyword themes (furniture buying guide, material questions, delivery/warranty).

**Action:** Do not remove. Improve question quality to target material-specific queries (e.g., "What is a travertine coffee table?", "How long does a chesterfield sofa last?") for AI citation benefit.

---

### M2 — 2,150 Products: Thin Product Descriptions Likely
**THINK:** With 2,150 products, the majority of product descriptions are likely manufacturer-supplied or near-identical templated copy. Google has been downranking stores with thin/duplicate product descriptions since the 2022 product reviews update.

Prioritise unique descriptions for: (a) products in the top 3 bestselling collections, (b) products on any keyword-targeted collection page.

---

### M3 — Currency Switcher May Fragment User Experience
**THINK:** The site displays currency options: AUD, INR, GBP, CAD, USD, EUR, JPY. This is unusual for an Australian furniture retailer with a single Sydney showroom. If the site ships internationally, hreflang and multi-currency canonical handling should be reviewed. If it's for display purposes only (not actual international shipping), it may confuse users and inflate bounce rates.

---

### M4 — Blog Sitemap Exists — Content Opportunity Unexploited
**THINK:** sitemap_blogs_1.xml exists but blog content was not assessed. A blog covering material-specific furniture topics (travertine vs marble, how to care for chesterfield sofas, timber bar stool buying guide) would directly support Plan 3 keyword strategy with topical authority signals.

---

### M5 — Founding Date Discrepancy: 1997 vs 2003
**THINK:** Onboarding form states founded 2003. Organization schema and site copy should say "Established 1997" (25+ years claim requires ~2001 or earlier). This needs client confirmation — inaccurate claims are an E-E-A-T trust signal risk. Google's QRG evaluates factual accuracy.

---

## LOW FINDINGS

### L1 — llms.txt Is Shopify Default, Not Custom
The site has `/llms.txt` (200) but it mirrors the standard Shopify `/agents.md` UCP commerce protocol content. This is excellent for AI shopping agents but not optimised for SEO/content AI citability. Consider adding a custom `llms.txt` with brand positioning, product category descriptions, and USP summary for AI tools like ChatGPT and Perplexity that might cite the site in furniture advice responses.

### L2 — No WebSite Schema with SearchAction
Homepage lacks WebSite schema with `potentialAction: SearchAction`. This enables Sitelinks Search Box in Google SERP for branded queries.

### L3 — AggregateRating Present on Homepage — Source Unclear
One AggregateRating schema block appears on the homepage. Its source (Google Reviews, Trustpilot, Product Jutsu, etc.) and accuracy should be verified. Inaccurate ratings markup can lead to manual action.

---

## POSITIVE FINDINGS

| Signal | Detail |
|---|---|
| HTTPS + HTTP/2 | Fully enabled ✅ |
| Cloudflare CDN | Active — Australian datacenter (gcp-australia-southeast2) ✅ |
| TTFB 46ms | Excellent server response ✅ |
| robots.txt | Correctly disallows sort_by, multi-filter, cart, checkout, admin ✅ |
| Sitemap | Well-structured with 5 sub-sitemaps, declared in robots.txt ✅ |
| Sitemap: agentic_discovery | Shopify AI-first discovery sitemap ✅ |
| agents.md / UCP | MCP endpoints for AI commerce — forward-thinking ✅ |
| AI crawlers allowed | GPTBot, Claude-Web, CCBot not blocked — AI crawling allowed ✅ |
| Collection page copy | lounges-and-sofas has 3,134 words with SEO copy — good depth ✅ |
| Key collection H1/titles | lounges-and-sofas, coffee-tables, bar-stools, bedroom-furniture all have keyword-targeted H1s and meta descriptions ✅ |
| FAQPage (LLM citation) | 8 FAQ questions present — LLM/AI citation value ✅ |

---

## SYNTHESISED ACTION PLAN

### Phase 1 — Critical Infrastructure (Do First, Unblocks Everything)

| # | Action | Priority | Owner | Dependency |
|---|--------|----------|-------|------------|
| 1 | Migrate from Timber theme to a modern Shopify 2.0 theme (Dawn, Impulse, or similar) | CRITICAL | Dev | None — this is the unlock |
| 2 | Noindex/remove all 20+ duplicate and thin collections (shop-all x4, console-table-1, storage-1, table-1, mirror, frontpage, uncategorized, the-enterance) | CRITICAL | Dev | Can do now without theme migration |
| 3 | Noindex /pages/sawce-data-feed | CRITICAL | Dev | Now |
| 4 | Merge duplicate canonical pairs to master collection (e.g., /mirror → /mirrors, /console-table-1 → /console-table) | HIGH | Dev | After item 2 |

### Phase 2 — Schema & On-Page (SEO Quick Wins)

| # | Action | Priority | Owner | Dependency |
|---|--------|----------|-------|------------|
| 5 | Add FurnitureStore Organization schema to homepage (JSON-LD above provided) | HIGH | Dev | — |
| 6 | Add BreadcrumbList schema to all collection and product pages | HIGH | Dev | After theme migration (theme.liquid edit) |
| 7 | Add ItemList schema to top 5 SEO collection pages | HIGH | Dev | After schema basics |
| 8 | Update keyword plan with correct live URLs (lounges-and-sofas, chaise-lounge, modular-lounges) | HIGH | SEO | — |
| 9 | Create Plan 3 collection pages: /collections/marble-coffee-tables, /collections/chesterfield-sofas | HIGH | Dev + SEO | — |
| 10 | Write and add meta description to /collections/dining-table | HIGH | SEO | Now |

### Phase 3 — Content & AI Readiness

| # | Action | Priority | Owner | Dependency |
|---|--------|----------|-------|------------|
| 11 | Rewrite suburb location page body copy — minimum 500 words unique per suburb, not templated | MEDIUM | SEO | — |
| 12 | Update FAQ questions on homepage to target material-specific queries for AI citation | MEDIUM | SEO | — |
| 13 | Add custom llms.txt content (brand description, product categories, USPs) for AI citability | MEDIUM | Dev | — |
| 14 | Write 5 blog posts targeting Plan 3 informational queries (travertine coffee table guide, chesterfield sofa care, etc.) | MEDIUM | Content | — |
| 15 | Review and confirm founding date (1997 vs 2003) with client — update all mentions consistently | MEDIUM | Account | — |
| 16 | Review "affordable furniture" vs "furniture store sydney" homepage targeting — align with keyword plan | MEDIUM | SEO | — |

### Phase 4 — Product Catalog Quality

| # | Action | Priority | Owner | Dependency |
|---|--------|----------|-------|------------|
| 17 | Rewrite product descriptions for all products in top 5 SEO collection pages | LOW | Content | — |
| 18 | Audit currency switcher — confirm international shipping capability or remove to reduce UX confusion | LOW | Account | — |
| 19 | Add WebSite schema with SearchAction to homepage | LOW | Dev | — |
| 20 | Verify AggregateRating source and accuracy on homepage | LOW | SEO | — |

---

## SEO HEALTH SCORE DETAIL

**42/100 — Needs Significant Work**

The primary drag on this score is a single root cause: **the site is running a 2014-era Shopify theme** that creates cascading problems across performance, mobile UX, schema capability, and image optimisation. The good news is that the on-page keyword strategy for SEO-targeted collection pages is sound — custom H1s, titles, and meta descriptions are in place for the primary target pages. The content depth on the lounges page (3,134 words) shows the right intent.

The theme migration (Action #1) is the single action that will have the biggest compounding effect. Combined with the duplicate collection cleanup (Action #2), this site could realistically reach **65+/100** within 90 days.

---

*Audit conducted: 5 June 2026 | triplejfurniture.com.au*

---

## BACKLINKS & AUTHORITY

*Source: Ahrefs April 2026 (from client memory file)*

| Metric | Value |
|--------|-------|
| Domain Rating (DR) | 8 |
| Ranking keywords | 84 |
| Estimated monthly traffic | 211 |

### Assessment

**DR 8 is workable but tight.** The keyword strategy correctly accounts for this by targeting:
- Local SERPs where boutique specialists (DR 15–30) hold positions 1–5
- Material/style sub-categories that national chains (DR 60–80) don't have dedicated pages for

The strategy fails if any target SERP moves chain-heavy before rankings are earned. At DR 8:
- KD 0–10: winnable within 3–6 months with good on-page
- KD 11–20: 6–12 months, requires some link acquisition
- KD 20+: unlikely within 12 months without active link building

### Top Link Building Opportunities (by ease + relevance)

1. **Local Sydney business directories** — True Local, Yellow Pages, Yelp AU, StartLocal — free citations that also improve local entity signals
2. **Interior design + home décor blogs** — Guest posts or product features on Australian interior design blogs (e.g., The Interiors Addict, Hunting for George blog) targeting DR 25–40 sites
3. **Google Business Profile** (GBP) — if not already claimed, this is the single highest-impact free action for local authority
4. **Product PR** — Pitch marble/travertine coffee table collections to home decor media (Domain, Houzz AU, realestate.com.au Home) — material-specific furniture content gets editorial coverage
5. **Supplier/manufacturer links** — Any furniture brands stocked should link back from their "stockists" pages

### Competitive DR Gap

SERP competitors on target keywords (Sydney Furniture Factory, Known for Lounges, Monster Furniture, Glicks) are estimated DR 15–35. Triple J needs to close from DR 8 to DR 20+ to compete consistently. This requires ~30–50 quality referring domains.

---

