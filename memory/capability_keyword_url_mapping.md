---
name: capability-keyword-url-mapping
description: Full keyword → URL mapping capability: consolidated table format, URL selection logic (ecommerce + service), primary/secondary rules, location page pairing, SERP pattern method for missing secondaries
metadata:
  type: feedback
---

# Keyword → URL Mapping Capability

**Rule:** Always deliver keyword mapping as a single consolidated table — no split tables by type, no narrative-only answers. One row per page, every time.

**Why:** Splitting into separate tables (general vs location, service vs product) forces the user to manually reconcile. One table = one handoff, no assembly required.

**How to apply:** Every keyword mapping task, regardless of client type, ends with one consolidated table. Apply URL selection logic below before populating the table.

---

## Deliverable Table Format

Always use this exact column set:

| # | Keyword | URL | Role | Status |
|---|---------|-----|------|--------|
| 1 | commercial solar sydney | https://energus.com.au/commercial-solar/sydney/ | P | NEW |
| 2 | solar installation sydney | https://energus.com.au/commercial-solar/sydney/ | S | NEW |
| 3 | home brew shop melbourne | https://brewerschoice.net.au/ | P | EXISTS |

- **URL:** Always `https://` + domain (no www) + path + trailing slash
- **Role:** P = Primary, S = Secondary
- **Status:** EXISTS (live page), NEW (page to be created), OPTIMISE (page exists but needs on-page work), CONSOLIDATE (multiple pages to merge into this one)
- **#:** Sequential row number across the whole table, not per-section

---

## Primary vs Secondary Rules

### Primary
- One primary keyword per page — never two
- The primary drives: URL slug, H1, title tag, meta description, and page content focus
- Choose the primary with the highest commercial volume and clearest SERP intent match

### Secondary
- Secondaries sit on the same page only if SERP is the same page type (same intent, same format)
- SERP check: if the competing URLs for the secondary are different from the primary's competing URLs, it needs its own page
- Secondaries appear in: subheadings, body copy, FAQ, schema — not forced into title or H1
- Linguistic subsets can share a page (e.g., "commercial solar installer sydney" and "commercial solar installation company sydney")
- Different topic = different page even if related (e.g., "commercial solar sydney" and "battery storage sydney" → separate pages)

---

## URL Selection Logic

### Service Businesses (law, solar, HVAC, builders, etc.)

1. If the page already exists → use the existing URL, mark OPTIMISE
2. If a new page is needed → create a slug from the primary keyword: `/[service]-[city]/` or `/[service]/[city]/`
3. No trailing brand in slugs — `/commercial-solar-sydney/` not `/commercial-solar-sydney-energus/`
4. Follow existing slug convention on the site (check before creating: does the site use hyphens? city as subfolder or suffix?)
5. When changing a URL: the old URL gets a 301 redirect to the new one. Both URLs must be documented in the mapping table.

### Ecommerce (WooCommerce, Shopify, etc.)

Priority order for URL selection:

**1. WooCommerce category page** (`/product-category/[parent]/[child]/`)
- Use for: category-intent keywords (e.g., "home brew supplies", "turbo yeast", "air stills")
- Prefer over individual product pages — category pages have product count, internal links, and broader intent match
- Use the **most specific** matching category that covers the keyword's intent — never the parent if a matching child exists
- **Category relevance check (mandatory before mapping):** Browse or search the category page to confirm the product mix. If the page contains products outside the keyword's scope — unrelated product types, mixed categories — do NOT use it. Create a new dedicated page instead.
  - Example: "oak barrels" → category "Wine Barrel & Chips" contains glass demijohns and wood chips → too mixed → create `/oak-barrels/`
  - Example: "top shelf essence" → parent "Essences & Chips" contains all brands + wood chips/staves → too broad → use the Top Shelf subcategory instead
  - Example: "copper stills" → parent "Stills Kit & Parts" contains Turbo 500, Air Stills, AlcoEngine, Pure Distilling → too broad → create `/copper-stills/`
- A category that mixes unrelated product types (e.g., "Boilers & Accessories" where accessories ≠ boilers) is borderline — flag with ⚠️ for developer to review
- WooCommerce admin tagging errors (products mis-tagged into a category) can pollute the page — verify what actually appears on the front-end page, not just what SKUs are tagged in admin

**2. Legacy/custom clean URL** (e.g., `/turbo-500-stills/`, `/pure-distilling-stills/`)
- Use when: the page is already indexed, the slug is cleaner than the WooCommerce path, and the content matches the keyword
- Do not replace a clean already-indexed URL with a longer WooCommerce category path
- Flag for developer confirmation if uncertain which is canonical

**3. WooCommerce product page** (`/product/[slug]/`)
- Use only when: no matching category exists, and the keyword is a specific product search (exact brand/model)
- Example: "still spirits classic 8 pack" → `/product/still-spirits-classic-8-pack/` (if no category covers it)

**4. New WooCommerce category page** (no existing category, but keyword is category-intent)
- Use the site's category URL structure even though the category doesn't exist yet: `/product-category/[parent]/[child-slug]/`
- Example: "copper stills" (no subcategory exists) → `/product-category/spirit-making/stills-and-parts/copper-pot-stills/` NEW
- Example: "oak barrels" (existing category is mixed) → `/product-category/wine-making/oak-barrels/` NEW
- NEVER use a bare custom slug like `/copper-stills/` or `/oak-barrels/` for a product listing page — custom slugs are for standalone content/landing pages only, not product category listings
- Developer instruction: create the WooCommerce category with the matching slug and move/tag relevant products into it

**5. New standalone content page** (no existing match, and keyword is informational/service intent — not a product listing)
- Use a clean descriptive slug from the primary keyword: `/[keyword-slug]/`
- Only appropriate for: blog articles, guide pages, location pages, service landing pages
- Do NOT use for any page that will list products

---

## Location Page Rules

### Home suburb rule
The suburb where the store/office is physically located maps to the **homepage** — not a standalone location page.
- Bayswater (Brewers Choice store) → `https://brewerschoice.net.au/` — homepage is the Bayswater page
- The homepage already has local signals (address, schema, NAP) — a separate /bayswater/ page would create cannibalization

### Location page pairing (physical retail / local service)
Each location suburb gets **one page** carrying:
- P: `[primary category] [suburb]` — highest-volume term for that suburb
- S: `[secondary category] [suburb]` — supporting term(s) that share SERP intent

Example for Brewers Choice:
- P: home brew shop croydon
- S: home distilling kit croydon

### Suburb selection criteria
- Within reasonable travel/delivery distance of the business
- Sufficient local population to justify a page (avoid ghost suburbs)
- Excludes the home suburb (which maps to homepage)
- Prioritise suburbs the client specified, then fill remaining slots with high-population nearby suburbs

---

## SERP Pattern Method (Finding Missing Secondaries)

Use this to check whether additional secondaries should be added to a page after the primary is mapped.

1. Search: `[primary keyword]` in Brave/Google
2. Look at page titles of the top 5–10 results — note which other terms appear repeatedly
3. If a term appears in 3+ competitor titles, it is a SERP-confirmed secondary candidate
4. Check: does that term have its own standalone SERP (different URLs ranking)? If yes → separate page. If not → secondary on same page.
5. Common pattern: "commercial solar [city]" titles often include "installation", "systems", "panels", "installer" → these become secondaries

Document confirmed secondaries in the mapping table on the same row as the primary.

---

## Cannibalization Prevention

- Never map the same keyword as Primary on two different pages
- If a keyword currently ranks on an old page that will be redirected → note the 301 in the Status column
- When consolidating pages (e.g., 3 battery pages → 1): mark all old pages as CONSOLIDATE with the destination URL, and list the 301 redirects required
- For ecommerce: check if WooCommerce creates both `/product-category/stills/` and `/stills/` (common plugin behavior) — flag both if found, identify which is canonical

---

## Developer Handoff Notes

Add a notes column or inline flag when the URL requires developer action:
- `🔧 301 required from [old-url]`
- `🔧 Confirm canonical — two URLs found for this category`
- `🔧 Create new page at this URL`
- `❓ URL unconfirmed — verify with developer before mapping`

These flags stay in the table so the developer gets a complete briefing from one document.

---

## Links

- [[feedback_keyword_url_mapping]] — earlier version of URL mapping rules (service businesses, wslegal)
- [[keyword_research_master]] — full keyword research process this capability feeds into
