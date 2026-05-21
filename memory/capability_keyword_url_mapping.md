---
name: capability-keyword-url-mapping
description: Full keyword → URL mapping capability: consolidated table format, URL selection logic (ecommerce + service), product vs category distinction, primary/secondary rules, location page pairing, SERP rank check, current rank column
metadata:
  type: feedback
---

# Keyword → URL Mapping Capability

**Rule:** Always deliver keyword mapping as a single consolidated table — no split tables by type, no narrative-only answers. One row per keyword, every time. Always present the result directly in the conversation as a table — never write it to an HTML file unless explicitly asked.

**Why:** Splitting into separate tables (general vs location, service vs product) forces the user to manually reconcile. One table = one handoff, no assembly required. Showing the result in the conversation means the analyst can review it immediately without opening a file.

**How to apply:** Every keyword mapping task, regardless of client type, ends with one consolidated table shown in the conversation. Apply URL selection logic, product vs category logic, and SERP rank check below before populating the table.

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
2. Fetch the homepage to read navigation and understand page hierarchy
3. Check `/robots.txt` for sitemap references
4. Browse 2–3 category/product URLs to confirm the site's actual URL pattern
5. Run a `site:domain.com` search to surface key indexed pages

**Step 3 — Exhaust existing pages before creating new ones**
Before assigning any keyword to a NEW page, confirm no existing page covers it:
- Check all category pages for the relevant product/service area
- Check all brand archive pages (WooCommerce brand plugins create `/brand/{slug}/` pages)
- Check all custom landing pages at the root level
- Check all location/service pages
- Only mark NEW when no existing page is a reasonable match

**Step 4 — SERP rank check (mandatory — run for every keyword)**
After URL mapping is drafted, check Google SERP for every keyword to see if the client's domain already ranks:
1. Search each keyword using Brave Search with Australian geo scope (`country=AU`)
2. Scan top 20 results for any URL from the client's domain
3. Record the position and the exact URL that is ranking
4. Compare the ranking URL to the mapped URL:
   - **Same URL:** mark as EXISTS — ranking pos X in the Current Rank column
   - **Different URL:** flag with ⚠️ — a different page is capturing this keyword; decide whether to (a) keep that page as the target, (b) redirect to the mapped URL, or (c) note it for the brief writer
   - **Not ranking:** mark as "Not ranking" in Current Rank column
5. When the SERP reveals a product page already ranking for a specific-intent keyword mapped to a brand/category page → update the mapping to the product page (that page has traction; don't abandon it)
6. When the SERP reveals a product page ranking for a category-intent keyword (bulk buy, wholesale) → keep the category page as the long-term target, flag the product page in Current Rank

**Step 5 — Self-review before delivering**
Before presenting results:
- Scan for any URL with two P keywords — fix immediately
- Confirm all NEW pages follow the site's existing slug conventions
- Verify every Brand page slug is plausible; flag if unconfirmed
- Confirm Current Rank is populated for every row

---

## Deliverable Table Format

Always use this exact column set — always shown in the conversation, not written to a file:

| # | Keyword | URL | Role | Type | Status | Current Rank |
|---|---------|-----|------|------|--------|--------------|
| 1 | wholesale chocolate australia | https://foodistribute.com.au/product-category/chocolate-patisserie/wholesale-chocolate-supplies/ | P | Category | EXISTS — optimise | 2 |
| 2 | fabbri amarena cherries | https://foodistribute.com.au/product/fabbri-amarena-cherries-in-syrup-opaline-jar-600g/ | P | Product | EXISTS — optimise | 2 |
| 3 | food suppliers sydney | https://foodistribute.com.au/areas-we-serve/sydney/ | P | Location | EXISTS — optimise | 4 |
| 4 | food distributors brisbane | https://foodistribute.com.au/areas-we-serve/brisbane/ | P | Location | NEW | 13 (homepage) |
| 5 | hospitality food suppliers | https://foodistribute.com.au/cafe-and-restaurant-food-suppliers/ | S | Landing Page | EXISTS — optimise | Not ranking |

- **URL:** Always `https://` + domain (no www) + path + trailing slash
- **Role:** P = Primary, S = Secondary
- **Type:** Category / Product / Product → Category / Location / Brand / Homepage / Landing Page (see Type column rules below)
- **Status:** EXISTS — optimise, EXISTS — ⚠️ [flag], EXISTS — verify slug, NEW, CONSOLIDATE
- **Current Rank:** Position number if ranking (e.g., "4"), "Not ranking" if not found in top 20, or "X (homepage)" / "X (product page)" when a different page from the mapped URL is ranking
- **#:** Sequential row number across the whole table, not per-section
- Secondary keywords that share a URL with their primary get their own row in the table

---

## Type Column Rules

### Category
A page that lists multiple products of the same type. Always uses the site's category URL structure.
- WooCommerce: `/product-category/[parent]/[child]/`
- Examples: cheese & dairy, chocolate & patisserie subcategory, wholesale bakery supplies

### Product
A page for a single specific product (exact brand/model search intent).
- WooCommerce: `/product/[slug]/`
- Use when: keyword names a specific product or brand+product combination AND a product page is confirmed to exist (via sitemap or SERP check)
- If no standalone product page exists → map as Secondary on the closest category page, flag with developer note

### Product → Category
Keyword has product-specific intent (names a particular model/variant) but no standalone product page confirmed — mapped to the closest category page as a fallback.
- Flag with ⚠️ and a developer note to check if a dedicated product page exists

### Brand
A brand archive page generated by a WooCommerce brand plugin. Lists all products from that brand.
- URL pattern: `/brand/[slug]/`
- Use for broad brand queries where the searcher wants any product from that brand (not one specific item)
- If SERP check reveals a product page is ranking for this keyword instead, update mapping to the product page
- Always flag as "EXISTS — verify slug" when slug is not confirmed from sitemap crawl

### Location
A city or suburb-level page for a business serving multiple geographic areas.
- URL pattern: `/areas-we-serve/[city]/` or `/[service]/[suburb]/` — follow the site's existing convention
- Home location maps to homepage, not a standalone page

### Homepage
The root domain page. Use only for the highest-volume general term that represents the brand's core proposition.
- One Primary keyword on homepage; all other general terms on homepage are Secondary
- Never put more than 1P + 4S on the homepage — if more keywords need a home, create a landing page

### Landing Page
A custom service or informational page at a root-level slug (e.g., `/cafe-and-restaurant-food-suppliers/`, `/wholesale-food-supplier/`).
- Use for general service terms that don't fit a product category but need their own page
- One Primary per landing page; related terms can be Secondary if same SERP intent

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
- **Category relevance check (mandatory):** Confirm the product mix by browsing the page. If the category contains products outside the keyword's scope, do NOT use it — create a new dedicated category instead.
  - "oak barrels" → "Wine Barrel & Chips" contains glass demijohns and wood chips → mixed → create new `/product-category/wine-making/oak-barrels/`
  - "copper stills" → parent "Stills Kit & Parts" contains all still types → too broad → create new `/product-category/.../copper-pot-stills/`
- WooCommerce admin tagging errors can pollute category pages — verify the front-end page, not just admin tags
- **Legacy URLs on old platforms:** If a site has migrated platforms, the legacy URL is NOT the right choice — use the current `/product-category/` path

**2. Existing WooCommerce brand page** (`/brand/[slug]/`)
- Use for broad brand queries where the searcher wants any product from that brand
- Prefer over generic category page when the keyword names a specific brand
- If both a brand page AND a brand-specific subcategory exist, prefer the subcategory
- If SERP check reveals a product page (not the brand page) is ranking → update mapping to the product page
- Always confirm slug from sitemap before citing; flag as "EXISTS — verify slug" when unconfirmed

**3. Existing WooCommerce product page** (`/product/[slug]/`)
- Use when: keyword is a specific product search AND a dedicated product page is confirmed (from sitemap or SERP check)
- Only use a product page when no matching category covers the intent
- If the product only exists inside a bundle (not sold standalone) → no product page → map as Secondary on the category page instead
- **SERP-confirmed product pages:** If SERP check shows a product page already ranking for a specific-intent keyword, always map to that product page — don't override ranking traction with an untested category/brand page

**4. New WooCommerce category page** (category-intent keyword, no existing category or existing category is mixed)
- Use the site's category URL structure: `/product-category/[parent]/[child-slug]/`
- NEVER use a bare custom slug like `/copper-stills/` for a product listing page — custom slugs are for content/landing pages only
- Developer instruction: create the WooCommerce category with the matching slug, move/tag relevant products into it

**5. New standalone content/location page** (informational or location intent — NOT a product listing)
- Use a clean descriptive slug: `/[keyword-slug]/` or `/[service]/[city]/`
- Only appropriate for: blog articles, guide pages, location pages, city pages
- Do NOT use for any page that will list products

---

## Location Page Rules

### Home location rule
The city/suburb where the business is headquartered maps to the **homepage** — not a standalone location page.
- A separate city page for the headquarters location would cannibalize the homepage

### Location page URL conventions
Always match the site's existing convention. Examples:
- foodistribute.com.au → `/areas-we-serve/[city]/`
- brewerschoice.net.au → `/home-brew-shop/[suburb]/`
- Service businesses → `/[service]/[city]/` or `/[service]-[city]/`

### Location page pairing (city/suburb pages)
Each location city gets **one page** carrying:
- P: primary keyword for that city (highest-volume distributor/service term)
- S: supporting term that shares the same page and SERP intent

Both get their own row in the table, same URL, P and S roles respectively.

### When homepage is already ranking for a new city's keyword
If a city page doesn't exist yet but the homepage is already ranking (typically pos 8–18) for that city's keyword:
- Mark the mapped URL as NEW
- In Current Rank, record: "X (homepage)" — shows the homepage is capturing the keyword as a fallback
- Building the dedicated city page will almost always push the ranking higher than the homepage fallback

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
- `EXISTS — verify slug` — brand page exists but exact slug needs confirming in WooCommerce admin
- `❓ URL unconfirmed — verify with developer before implementing`

---

## Links

- [[feedback_keyword_url_mapping]] — earlier version of URL mapping rules (service businesses, wslegal)
- [[keyword_research_master]] — full keyword research process this capability feeds into
