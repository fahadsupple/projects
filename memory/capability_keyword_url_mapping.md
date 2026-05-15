---
name: capability-keyword-url-mapping
description: Full keyword → URL mapping capability: consolidated table format, URL selection logic (ecommerce + service), product vs category distinction, primary/secondary rules, location page pairing, SERP pattern method for missing secondaries
metadata:
  type: feedback
---

# Keyword → URL Mapping Capability

**Rule:** Always deliver keyword mapping as a single consolidated table — no split tables by type, no narrative-only answers. One row per keyword, every time.

**Why:** Splitting into separate tables (general vs location, service vs product) forces the user to manually reconcile. One table = one handoff, no assembly required.

**How to apply:** Every keyword mapping task, regardless of client type, ends with one consolidated table. Apply URL selection logic and product vs category logic below before populating the table.

---

## Deliverable Table Format

Always use this exact column set:

| # | Keyword | URL | Role | Type | Status |
|---|---------|-----|------|------|--------|
| 1 | turbo 500 stills | https://brewerschoice.net.au/product-category/spirit-making/stills-and-parts/turbo-500-stills/ | P | Category | EXISTS — optimise |
| 2 | air still pro | https://brewerschoice.net.au/product-category/spirit-making/stills-and-parts/air-stills/ | P | Product → Category | EXISTS — ⚠️ verify product mix |
| 3 | still spirits classic 8 | https://brewerschoice.net.au/product-category/spirit-making/yeast-consumable/ | S | Product | No standalone page — secondary on turbo yeast page |
| 4 | home brew shop croydon | https://brewerschoice.net.au/home-brew-shop/croydon/ | P | Location | NEW |
| 5 | home distilling kit croydon | https://brewerschoice.net.au/home-brew-shop/croydon/ | S | Location | NEW |

- **URL:** Always `https://` + domain (no www) + path + trailing slash
- **Role:** P = Primary, S = Secondary
- **Type:** Category / Product / Location (see Type column rules below)
- **Status:** EXISTS — optimise, EXISTS — ⚠️ [flag], NEW, CONSOLIDATE
- **#:** Sequential row number across the whole table, not per-section
- Secondary keywords that share a URL with their primary get their own row in the table

---

## Type Column Rules

### Category
A page that lists multiple products of the same type. Always uses the site's category URL structure.
- WooCommerce: `/product-category/[parent]/[child]/`
- Examples: turbo 500 stills, fresh wort kit, turbo yeast, oak barrels, copper stills

### Product
A page for a single specific product (exact brand/model search intent).
- WooCommerce: `/product/[slug]/`
- Examples: still spirits classic 8, specific still spirits t500 kit
- If no standalone product page exists and the item is only sold in bundles → map as Secondary on the closest category page, flag with developer note

### Product → Category
Keyword has product-specific intent (names a particular model) but no standalone product page exists — mapped to the closest category page as a fallback.
- Flag with ⚠️ and a developer note to check if a dedicated product page exists
- Example: "air still pro" → specific Still Spirits product, but no product page found → mapped to air stills category

### Location
A suburb-level page for a physical store or local service business.
- URL pattern: `/[service]/[suburb]/` or `/home-brew-shop/[suburb]/`
- Home suburb always maps to homepage (see Location Page Rules section)

---

## Primary vs Secondary Rules

### Primary
- One primary keyword per page — never two
- The primary drives: URL slug, H1, title tag, meta description, and page content focus
- Choose the primary with the highest commercial volume and clearest SERP intent match

### Secondary
- Secondaries sit on the same page only if SERP is the same page type (same intent, same format)
- SERP check: if competing URLs for the secondary differ from the primary's, it needs its own page
- Secondaries appear in: subheadings, body copy, FAQ, schema — not forced into title or H1
- Linguistic subsets can share a page (e.g., "commercial solar installer sydney" and "commercial solar installation company sydney")
- Different topic = different page even if related (e.g., "commercial solar sydney" and "battery storage sydney" → separate pages)
- A product keyword with no standalone page becomes a Secondary on the closest category page — never a Primary on a page it doesn't own

---

## URL Selection Logic

### Service Businesses (law, solar, HVAC, builders, etc.)

1. If page already exists → use existing URL, mark EXISTS — optimise
2. New page needed → slug from primary keyword: `/[service]-[city]/` or `/[service]/[city]/`
3. No trailing brand in slugs
4. Match existing site slug conventions before creating
5. URL change → old URL gets 301 redirect; document both in the table

### Ecommerce (WooCommerce, Shopify, etc.)

Apply in this priority order:

**1. Existing WooCommerce category page** (`/product-category/[parent]/[child]/`)
- Use for category-intent keywords
- Always use the **most specific** subcategory — never the parent when a child matches
- **Category relevance check (mandatory):** Confirm the product mix by searching or browsing the page. If the category contains products outside the keyword's scope, do NOT use it — create a new dedicated category instead.
  - "oak barrels" → "Wine Barrel & Chips" contains glass demijohns and wood chips → mixed → create new `/product-category/wine-making/oak-barrels/`
  - "top shelf essence" → parent "Essences & Chips" contains all brands + wood chips → too broad → use `/product-category/.../still-spirits-top-shelf/` subcategory
  - "copper stills" → parent "Stills Kit & Parts" contains all still types → too broad → create new `/product-category/.../copper-pot-stills/`
- A category mixing unrelated product types (e.g., "Boilers & Accessories") is borderline — flag ⚠️ for developer review
- WooCommerce admin tagging errors can pollute category pages — verify the front-end page, not just admin tags
- **Legacy URLs on old platforms:** If a site has migrated platforms (e.g., old `www.` subdomain vs new WooCommerce), the legacy URL is NOT the right choice — use the current `/product-category/` path. Example: `www.brewerschoice.net.au/turbo-500-stills` is the old platform; the correct URL is `brewerschoice.net.au/product-category/spirit-making/stills-and-parts/turbo-500-stills/`

**2. Existing WooCommerce product page** (`/product/[slug]/`)
- Use when: keyword is a specific product search AND a dedicated product page exists
- Only use a product page when no matching category covers the intent
- If the product only exists inside a bundle (not sold standalone) → no product page → map as Secondary on the category page instead

**3. New WooCommerce category page** (category-intent keyword, no existing category or existing category is mixed)
- Use the site's category URL structure: `/product-category/[parent]/[child-slug]/`
- NEVER use a bare custom slug like `/copper-stills/` for a product listing page — custom slugs are for content/landing pages only
- Developer instruction: create the WooCommerce category with the matching slug, move/tag relevant products into it
- Examples:
  - "copper stills" → `/product-category/spirit-making/stills-and-parts/copper-pot-stills/` NEW
  - "oak barrels" → `/product-category/wine-making/oak-barrels/` NEW
  - "distilling starter kit" → `/product-category/spirit-making/distilling-starter-kits/` NEW

**4. New standalone content/location page** (informational or location intent — NOT a product listing)
- Use a clean descriptive slug: `/[keyword-slug]/` or `/[service]/[suburb]/`
- Only appropriate for: blog articles, guide pages, location pages, city pages
- Examples: `/home-brew-shop/croydon/`, `/home-brewing-supplies/melbourne/`
- Do NOT use for any page that will list products

---

## Location Page Rules

### Home suburb rule
The suburb where the store/office is physically located maps to the **homepage** — not a standalone location page.
- Bayswater (Brewers Choice store) → `https://brewerschoice.net.au/` — the homepage is the Bayswater page
- A separate /bayswater/ page would cannibalize the homepage

### Location page pairing (physical retail / local service)
Each location suburb gets **one page** carrying two keywords:
- P: `[primary category] [suburb]` — highest-volume term for that suburb
- S: `[secondary category] [suburb]` — supporting term that shares the same page and SERP intent

Example:
- P: home brew shop croydon → `/home-brew-shop/croydon/`
- S: home distilling kit croydon → same URL, same page

Both get their own row in the table, same URL, P and S roles respectively.

### Suburb selection criteria
- Within reasonable travel/delivery distance of the business
- Sufficient local population to justify a page
- Excludes the home suburb (maps to homepage)
- Prioritise client-specified suburbs, then fill remaining slots with high-population nearby suburbs

---

## SERP Pattern Method (Finding Missing Secondaries)

1. Search the primary keyword in Brave/Google
2. Look at page titles of top 5–10 results — note terms that appear repeatedly
3. If a term appears in 3+ competitor titles → SERP-confirmed secondary candidate
4. Check: does that term have its own standalone SERP (different URLs ranking)? If yes → separate page. If no → secondary on same page.
5. Document confirmed secondaries in the table on the same row as the primary

---

## Cannibalization Prevention

- Never map the same keyword as Primary on two different pages
- If a keyword currently ranks on an old page being redirected → note the 301 in the Status column
- When consolidating pages (e.g., 3 battery pages → 1): mark all old pages as CONSOLIDATE with destination URL, list 301 redirects required
- For ecommerce: check if WooCommerce auto-generates duplicate paths (e.g., `/product-category/stills/` and `/stills/`) — flag both, identify canonical

---

## Developer Handoff Flags

Add inline to the Status column when developer action is needed:
- `🔧 301 required from [old-url]`
- `🔧 Create WooCommerce category at this URL, move [product type] products into it`
- `⚠️ Verify product mix on front-end — admin tags may include unrelated products`
- `❓ URL unconfirmed — verify with developer before implementing`

---

## Links

- [[feedback_keyword_url_mapping]] — earlier version of URL mapping rules (service businesses, wslegal)
- [[keyword_research_master]] — full keyword research process this capability feeds into
