---
name: capability-keyword-url-mapping
description: Full keyword → URL mapping capability: mapping table format, URL selection logic (ecommerce + service), product vs category distinction, primary/secondary rules, location page pairing, SERP rank check
metadata:
  type: feedback
---

# Keyword → URL Mapping Capability

**Rule:** Always deliver keyword mapping as a single consolidated mapping table — no split tables, no categorisations, no narrative-only answers. One row per keyword, every time. Always show the result directly in the conversation — never write to a file unless explicitly asked.

**The mapping table is always the result.** It answers two questions per keyword: (1) which URL does it map to, and (2) is that page existing or new. Everything else — site research, SERP checks, URL logic — is process that feeds into the table. The table is what gets handed off.

---

## Pre-Mapping Checklist (mandatory — do this before touching a single keyword)

**Step 1 — Identify site type**
Before mapping anything, determine what type of site this is:
- **Ecommerce** (WooCommerce, Shopify, Magento, etc.) → product-category URL logic applies
- **Service business** (law, solar, HVAC, builders, etc.) → service/location slug logic applies
- **Distributor / B2B with ecommerce** → hybrid: has category pages AND service landing pages AND location pages; apply ecommerce logic for product keywords, service logic for general terms
- Misidentifying site type = wrong URL structure. Get this right first.

**Step 2 — Map the existing URL structure**
Never guess at URLs. Always:
1. Fetch `/sitemap.xml` (and all linked sitemaps: page-sitemap, product-sitemap, category-sitemap, brand-sitemap, etc.)
2. Fetch the homepage to understand navigation and page hierarchy
3. Check `/robots.txt` for sitemap references
4. Browse 2–3 category/product URLs to confirm the actual URL pattern
5. Run a `site:domain.com` search to surface key indexed pages

**Step 3 — Exhaust existing pages before creating new ones**
Before assigning any keyword to a NEW page, confirm no existing page covers it:
- Check all category pages for the relevant product/service area
- Check all brand archive pages (WooCommerce brand plugins create `/brand/{slug}/` pages)
- Check all custom landing pages at the root level
- Check all location/service pages
- Only mark New when no existing page is a reasonable match

**Step 4 — SERP rank check (mandatory — every keyword)**
After URL mapping is drafted, check Google SERP for every keyword:
1. Search each keyword using Brave Search with Australian geo scope (`country=AU`)
2. Scan top 20 results for any URL from the client's domain
3. Record position and exact ranking URL
4. If the ranking URL differs from the mapped URL — decide: keep that page as the target, or flag for correction
5. When a product page is already ranking for a specific-intent keyword → update mapping to that product page; don't abandon ranking traction
6. When a product page ranks for a category-intent keyword (bulk, wholesale) → keep category page as long-term target; record the product page in Current Rank with a note
7. When homepage ranks for a keyword mapped to a NEW city/location page → record as "X (homepage)" in Current Rank; the dedicated page will improve it

**Step 5 — Self-review before delivering**
- No URL has two P keywords
- All NEW pages follow the site's existing slug convention
- Every brand page slug flagged if not confirmed from sitemap
- Current Rank populated for every row

---

## Mapping Table Format (the deliverable — always show this in the conversation)

| # | Keyword | URL | Role | Page | Current Rank |
|---|---------|-----|------|------|-------------|
| 1 | wholesale chocolate australia | https://foodistribute.com.au/product-category/chocolate-patisserie/wholesale-chocolate-supplies/ | P | Existing | 2 |
| 2 | fabbri amarena cherries | https://foodistribute.com.au/product/fabbri-amarena-cherries-in-syrup-opaline-jar-600g/ | P | Existing | 2 |
| 3 | food suppliers sydney | https://foodistribute.com.au/areas-we-serve/sydney/ | P | Existing | 4 |
| 4 | food distributors brisbane | https://foodistribute.com.au/areas-we-serve/brisbane/ | P | New | 13 (homepage) |
| 5 | hospitality food suppliers | https://foodistribute.com.au/cafe-and-restaurant-food-suppliers/ | S | Existing | Not ranking |

**Column rules:**
- **URL** — always `https://` + domain (no www) + path + trailing slash
- **Role** — P = Primary (one per page, drives H1/title/meta) · S = Secondary (supports same page, in body/FAQs)
- **Page** — `Existing` (page already live) or `New` (must be created)
- **Current Rank** — position number (1–20) if ranking; "Not ranking" if absent from top 20; "X (homepage)" or "X (product page)" when a different page from the mapped URL is currently capturing the keyword
- **#** — sequential, no restarts per section

---

## URL Selection Logic

### Service Businesses (law, solar, HVAC, builders, etc.)
1. Existing page → use it, Page = Existing
2. New page → slug from primary keyword: `/[service]-[city]/` or `/[service]/[city]/`
3. Match existing slug conventions before inventing new patterns
4. URL change needed → note 301 redirect required in notes

### Ecommerce (WooCommerce, Shopify, etc.) — in priority order

**1. Existing category page** (`/product-category/[parent]/[child]/`)
- Use for category-intent keywords (wholesale X, bulk X, X supplier)
- Always use the most specific subcategory — never the parent when a child matches
- Category relevance check mandatory: if the category page mixes unrelated products, create a new subcategory instead

**2. Existing brand page** (`/brand/[slug]/`)
- Use for broad brand queries (searcher wants any product from that brand)
- If both a brand page AND a brand-specific subcategory exist, prefer the subcategory
- If SERP check shows a product page ranking for this keyword, update mapping to the product page
- Flag as "verify slug" if slug not confirmed from sitemap

**3. Existing product page** (`/product/[slug]/`)
- Use when keyword names a specific product AND the product page is confirmed (sitemap or SERP)
- SERP-confirmed product pages with ranking traction → always map to them, don't override with untested pages

**4. New category page** — when category-intent keyword has no matching existing category
- Use `/product-category/[parent]/[child-slug]/` — never a bare slug for a product listing
- Developer note: create WooCommerce category, tag relevant products into it

**5. New content/location page** — informational or location intent only
- Use clean slug: `/[keyword-slug]/` or `/[service]/[city]/`
- Never for product listings

### Homepage
- One P keyword only (highest-volume general brand/service term)
- Other general terms → S on homepage
- Hard limit: 1P + 4S maximum on homepage; anything beyond that needs its own landing page

### Landing Pages
- Custom root-level pages for service terms that don't fit a product category
- One P per page; related S keywords with same SERP intent can share the page

---

## Primary vs Secondary Rules

- **One P per page** — it drives the URL slug, H1, title tag, meta description
- **S keywords** sit on the same page only if SERP intent is identical (same page type in top results)
- S keywords appear in: subheadings, body copy, FAQs, schema — never forced into H1 or title
- Linguistic variants of the same intent → same page (e.g., "commercial solar installer sydney" + "commercial solar installation company sydney")
- Different topic = different page even if related (e.g., "commercial solar sydney" + "battery storage sydney")
- A product keyword with no standalone page → S on the closest category page; never P on a page it doesn't own

---

## Location Page Rules

- Business's own city/suburb → homepage (not a standalone page; separate page would cannibalize)
- New city pages follow site's existing URL convention (e.g., `/areas-we-serve/[city]/`)
- Each city page: one P keyword + one S keyword that shares the same SERP intent
- When homepage already ranks for a new city's keyword → mark page as New, record rank as "X (homepage)"

---

## SERP Pattern Method (Secondaries)

1. Search the primary keyword
2. Look at page titles in top 5–10 results — note recurring terms
3. If a term appears in 3+ competitor titles → secondary candidate
4. Check: does that term have its own standalone SERP (different URLs ranking)? Yes → separate page. No → secondary on same page.

---

## Cannibalization Prevention

- Never two P keywords on the same URL
- Page being redirected → note 301 in a footnote
- Consolidating pages → mark old URLs as CONSOLIDATE with destination URL

---

## Links

- [[feedback_keyword_url_mapping]] — earlier version (service businesses, wslegal)
- [[keyword_research_master]] — full keyword research process this capability feeds into
