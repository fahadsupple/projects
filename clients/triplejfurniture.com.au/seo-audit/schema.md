# Schema Audit — triplejfurniture.com.au

**Audit date:** 5 June 2026  
**Pages audited:**
- Homepage: `https://triplejfurniture.com.au/`
- Collection page: `https://triplejfurniture.com.au/collections/lounges-and-sofas`
- Product page: `https://triplejfurniture.com.au/products/ma-jaguar-dining-set-5-piece-fixed`
- Contact page: `https://triplejfurniture.com.au/pages/contact`
- About page: `https://triplejfurniture.com.au/pages/about-us`
- FAQ page: `https://triplejfurniture.com.au/pages/faq`
- Location page: `https://triplejfurniture.com.au/pages/furniture-store-bankstown`

---

## Summary

| Page type | JSON-LD present | Schema types | Status |
|---|---|---|---|
| Homepage | Yes | FAQPage | Partial — no Organization/LocalBusiness |
| Collection pages | No | None | Missing |
| Product pages | Runtime JS only | Product (via TrustShop app, JS-injected) | Incomplete — no Offers, AggregateRating is 0/0 |
| Contact page | No | None | Missing |
| About page | No | None | Missing |
| FAQ page | Yes | FAQPage | Present — 9 questions |
| Location pages | No | None | Missing |

---

## Page-by-Page Findings

### 1. Homepage (`/`)

**JSON-LD blocks: 1**

**FAQPage schema — present**
- 8 questions covering delivery, showroom hours, price beat guarantee, assembly, custom furniture, and general buying questions
- All answers are clean plain text (no HTML tags)
- Schema is valid JSON-LD

**Issues:**
- No `Organization` or `LocalBusiness` schema present anywhere on the homepage or site
- The business has a physical showroom at Yagoona, NSW — `LocalBusiness` with `address`, `telephone`, `openingHours`, and `geo` is missing site-wide
- `og:image` uses HTTP not HTTPS (`http://triplejfurniture.com.au/cdn/shop/...`) — the `og:image:secure_url` tag exists as a workaround but the primary URL should use HTTPS
- **Duplicate OG tags:** All Open Graph tags appear twice in the `<head>` — 14 total OG tags, only 7 unique. This is a Shopify theme double-render issue. Affects all pages.
- `og:site_name` value is `Triplejfurniture ` (lowercase, trailing space) — should be `Triple J Furniture`
- `twitter:card` is `summary` (small image) — `summary_large_image` would give better social previews for a furniture retailer

---

### 2. Collection pages (e.g. `/collections/lounges-and-sofas`)

**JSON-LD blocks: 0 — no schema present**

**Issues:**
- No `CollectionPage` or `ItemList` schema
- No breadcrumb schema despite breadcrumb HTML being rendered on the page
- Duplicate OG tags (same issue as homepage — 14 tags, 7 unique)
- `og:type` is `website` on collection pages — should be `website` or ideally omitted/left as-is, but more critically there is no product listing markup
- No `BreadcrumbList` JSON-LD despite breadcrumb HTML present

**Note:** URL `https://triplejfurniture.com.au/collections/sofas-lounges` (tested in brief) returns a 404. The correct slug is `/collections/lounges-and-sofas`. Any internal links or external links pointing to the old slug will land on a 404.

---

### 3. Product pages (e.g. `/products/ma-jaguar-dining-set-5-piece-fixed`)

**JSON-LD blocks: 0 in static HTML**

**TrustShop app — JS-injected Product schema (runtime only)**

The TrustShop reviews app (`trustshop-rating-styles`) injects a `Product` schema block at runtime via `DOMContentLoaded`. The injected schema structure is:

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "@id": "https://triplejfurniture.com.au/products/ma-jaguar-dining-set-5-piece-fixed#product",
  "name": "MA Jaguar Dining Set 5 Piece Fixed",
  "brand": {
    "@type": "Brand",
    "name": "Matic"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": 0,
    "ratingCount": 0
  }
}
```

**Issues with the injected Product schema:**
1. **No `Offers` block** — price, currency, availability, and URL are absent. This means the product cannot qualify for Google's rich results (price callouts in search). Google requires `Offers` with `price`, `priceCurrency`, and `availability` for Product rich results.
2. **`aggregateRating` is 0/0** — `ratingValue: 0` and `ratingCount: 0`. Google will likely discard or flag this as invalid. An `AggregateRating` requires at least one real review. If TrustShop has no reviews collected yet, this block is invalid markup.
3. **JS-only injection** — The schema is not present in the raw HTML response. Googlebot renders JavaScript, so it should pick this up, but static HTML delivery is more reliable and not dependent on render budget.
4. **No `image`, `description`, `sku`, or `url` properties** — minimum recommended properties for Product rich results are absent.

**Product meta description quality issue (separate from schema):**
The tested product (`MA Jaguar Dining Set 5 Piece Fixed`) has a meta description of only 44 characters: `"Jaguar 5 piece Dinning with a pedestal base."` — this contains a typo ("Dinning" should be "Dining") and is too short to be effective.

**Duplicate OG tags:** 18 OG tags present, only 9 unique — same theme double-render issue.

---

### 4. Contact page (`/pages/contact`)

**JSON-LD blocks: 0 — no schema present**

**Issues:**
- No `LocalBusiness` schema with address, phone, hours
- This is the highest-value page for LocalBusiness schema

---

### 5. About page (`/pages/about-us`)

**JSON-LD blocks: 0 — no schema present**

**Issues:**
- No `Organization` schema with `name`, `url`, `logo`, `description`, `foundingDate`, `contactPoint`

---

### 6. FAQ page (`/pages/faq`)

**JSON-LD blocks: 1**

**FAQPage schema — present, 9 questions**

Questions present:
- What kind of designs in furniture are famous among people?
- Why is Australian made furniture so costly?
- What furniture brands are of high quality?
- What if I am not at home when the delivery arrives?
- What do I do if I have a problem with furniture post delivery?
- Is Custom Furniture in Australia Expensive?
- How to find a modern designer furniture store in Australia?
- What is the latest trend in furniture?
- How do I care for Outdoor furniture?

**Issues:**
- FAQ page has no `<meta name="description">` tag — blank
- FAQ page title is `Faq | Triple J Furniture` — "Faq" should be "FAQ" (capitalisation)
- Questions are generic/generic-SEO-style rather than buyer intent questions (e.g. "What furniture brands are of high quality?" is vague; no questions about Triple J's specific policies like price beat, warranty, delivery timeframes)
- The homepage also has a separate FAQPage schema with 8 different questions — there are now two FAQPage schemas across the site with overlapping topics but different questions. Google only uses FAQPage from a given URL.

---

### 7. Location pages (e.g. `/pages/furniture-store-bankstown`)

**JSON-LD blocks: 0 — no schema present**

**Issues:**
- No `LocalBusiness` schema with area-specific address/service area markup
- These pages are strong candidates for `LocalBusiness` with `areaServed` and `serviceArea` properties

---

## Critical Missing Schema (Priority Order)

| Priority | Schema type | Where | Why it matters |
|---|---|---|---|
| P1 | `Product` with `Offers` | All product pages | Required for price rich results and product SERP features |
| P1 | `LocalBusiness` | Homepage or contact page | Establishes entity, helps Google Business Profile association |
| P2 | `BreadcrumbList` | All collection + product pages | Breadcrumb trails in SERP URLs |
| P2 | `Organization` | Homepage | Brand entity, `sameAs` links to socials/GBP |
| P3 | `ItemList` / `CollectionPage` | Collection pages | Category page rich results |
| P3 | `LocalBusiness` with `areaServed` | Location pages | Local SEO signals for suburb targeting |

---

## Validation Issues Summary

| Issue | Pages affected | Severity |
|---|---|---|
| Duplicate OG meta tags (all tags appear twice) | All pages | Medium — Facebook/social parsers take first occurrence but it's messy |
| `og:image` uses HTTP not HTTPS | All pages | Low — `og:image:secure_url` present as fallback |
| `og:site_name` has trailing space and wrong casing | All pages | Low |
| `twitter:card` is `summary` not `summary_large_image` | All pages | Low |
| Product schema has `aggregateRating: 0/0` | All product pages | High — invalid markup, may cause rich result suppression |
| Product schema has no `Offers` block | All product pages | High — blocks price rich results entirely |
| Product schema is JS-injected only (no static HTML) | All product pages | Medium — render-dependent |
| FAQ page has no meta description | `/pages/faq` | Medium |
| FAQ page title capitalisation (`Faq`) | `/pages/faq` | Low |

---

## Recommendations

### Immediate (P1)

1. **Add static Product JSON-LD to all product page templates** — do not rely on TrustShop's JS injection. Include at minimum: `name`, `image`, `description`, `sku`, `brand`, `offers` (with `price`, `priceCurrency`, `availability`, `url`). Remove the TrustShop `aggregateRating: 0/0` injection until real reviews are collected.

   Example minimal block:
   ```json
   {
     "@context": "https://schema.org",
     "@type": "Product",
     "name": "{{ product.title }}",
     "image": "{{ product.featured_image | img_url: 'grande' }}",
     "description": "{{ product.description | strip_html | truncate: 500 }}",
     "sku": "{{ product.selected_or_first_available_variant.sku }}",
     "brand": { "@type": "Brand", "name": "{{ product.vendor }}" },
     "offers": {
       "@type": "Offer",
       "price": "{{ product.price | money_without_currency }}",
       "priceCurrency": "AUD",
       "availability": "{% if product.available %}https://schema.org/InStock{% else %}https://schema.org/OutOfStock{% endif %}",
       "url": "{{ shop.url }}{{ product.url }}"
     }
   }
   ```

2. **Add `LocalBusiness` schema to the contact page or homepage** — include `name`, `address` (PostalAddress), `telephone`, `openingHoursSpecification`, `url`, `image`, `priceRange`, `sameAs` (Facebook, Instagram, Google Business Profile URLs).

### Short-term (P2)

3. **Fix duplicate OG tags** — the Shopify theme is rendering the OG block twice. This is usually caused by a theme snippet being called in both `theme.liquid` and a section. Locate and remove the duplicate include.

4. **Add `BreadcrumbList` JSON-LD** to product and collection page templates — breadcrumb HTML is already present; this is a matter of adding the JSON-LD counterpart.

5. **Fix `og:image` to use HTTPS** — update the theme's asset URL output to use `https://` or use `{{ 'logo.png' | asset_url }}` which Shopify should serve over HTTPS.

### Nice-to-have (P3)

6. **Add `Organization` schema to homepage** with `sameAs` links.
7. **Add `LocalBusiness` with `areaServed`** to each `/pages/furniture-store-*` location page.
8. **Add `ItemList`** to major collection pages listing top products.
9. **Fix FAQ page meta description** and improve title capitalisation.
10. **Update `twitter:card` to `summary_large_image`** for better social sharing previews.
