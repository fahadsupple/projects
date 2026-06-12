# McKinnon Heating & Cooling — Implementation Review
**Date:** 12 June 2026  
**Pages checked:** 57  
**Method:** Full HTML audit — meta tags, canonical, Open Graph, Twitter Card, JSON-LD schema (with @graph parsing), heading hierarchy, images, breadcrumbs, FAQs.

---

## Summary

| Category | Result |
|---|---|
| All 57 URLs live (200 OK) | ✅ Pass |
| Meta titles | ✅ All 57 correct |
| Meta descriptions | ✅ All 57 correct |
| Canonical tags | ✅ All 57 correct, no redirect chains |
| Noindex | ✅ Zero pages noindexed |
| Image alt attributes | ✅ No missing or empty alts |
| Internal linking | ✅ All pages have sufficient links |
| H1 tags | ⚠️ 55/57 correct — 2 text fixes needed |
| og:image | ❌ 53/57 pages missing |
| og:type | ❌ 56/57 pages wrong (set to "article") |
| Twitter:image | ❌ All 57 pages missing |
| FAQPage schema | ❌ 54/57 pages missing despite FAQ content |
| Schema entity type | ❌ Wrong type (HomeGoodsStore) on 53 pages |
| Schema page type | ❌ CollectionPage on 4 service pages |
| BreadcrumbList schema | ❌ 0/57 pages (HTML breadcrumbs present but no markup) |
| Article schema on non-articles | ❌ 53 pages affected |
| Internal WP username exposed | ⚠️ 1 page (homepage Twitter meta) |

---

## Issue 1 — H1 Fixes (from previous review)

### 1a. Split System Page H1
**URL:** `https://www.mckinnonheating.com.au/cooling/wall-split-systems-cooling/`  
**Live:** `Wall Split Systems`  
**Approved:** `Split System Installation Melbourne`  
**Fix:** Update H1 in CMS.

### 1b. Areas We Serve Page H1
**URL:** `https://www.mckinnonheating.com.au/areas-we-serve/`  
**Live:** `Heating and Cooling Near Me`  
**Approved:** `Heating and Cooling Near Me: Melbourne's Trusted Local Team`  
**Fix:** Update H1 in CMS.

---

## Issue 2 — og:image Missing on 53 Pages ❌

**Impact:** High — when pages are shared on Facebook, LinkedIn or X, no image appears. Social previews show blank/generic.

**Affected pages:**
- Homepage (`/`)
- All 51 location pages (e.g. `/heating-and-cooling-frankston/`, `/air-conditioning-brighton/`, etc.)

**Pages that already have og:image:** The 4 original service pages (ducted heating, air conditioning, split system, hydronic) each have a featured image set in WordPress, so these are fine.

**Fix:** In WordPress, open each affected page and set a **Featured Image**. Rank Math (the SEO plugin in use) will automatically pull this into the og:image tag. A single relevant hero/banner image per page type would suffice — location pages can share a common McKinnon branded image.

---

## Issue 3 — og:type = "article" on 56/57 Pages ❌

**Impact:** Medium — Facebook and other social parsers see these service and location pages as blog articles. Incorrect classification.

**Breakdown:**
- Homepage: `og:type: website` ✅ (correct)
- All 56 other pages: `og:type: article` ❌

Service and location pages should use `og:type: website` (the default and correct type for non-article web pages). The WordPress/Rank Math setting is defaulting all new pages to `article`.

**Fix:** In Rank Math → Titles & Meta → Posts/Pages settings, change the default og:type for pages from `article` to `website`. Or update individually per page in the Rank Math sidebar.

---

## Issue 4 — Twitter:image Missing on ALL 57 Pages ❌

**Impact:** High — all 57 pages have `twitter:card: summary_large_image` set, which promises a large image preview. But none have `twitter:image` defined, so when shared on X/Twitter, the card shows as text-only (the large image slot stays blank).

This is directly linked to Issue 2 — setting Featured Images in WordPress (Issue 2 fix) will automatically populate `twitter:image` via Rank Math.

**Additional finding:** The homepage Twitter meta exposes the internal WordPress username:
```
twitter:label1 = "Written by"
twitter:data1  = "mckinnonhea9741"
```
This is the raw WP admin username — not professional if visible. Fix: In Rank Math, disable the Twitter "Written by" label, or rename the WP user display name.

---

## Issue 5 — FAQPage Schema Missing on 54/57 Pages ❌

**Impact:** High — every page in the approved content has 7–8 FAQ questions. FAQPage schema enables Google's FAQ rich results (expandable Q&A directly in the SERP snippet), which significantly increases click-through rate.

**Current state:**
- 3 pages have FAQPage schema: Air Conditioning, Split System, Hydronic Heating
- 54 pages are missing it: Homepage, Ducted Heating (the main service page!), and all 51 location pages

**Note on the 3 pages that do have FAQPage schema:** These also have `CollectionPage` schema type (see Issue 6), so even the partial implementation is incorrect.

**Fix:** Add FAQPage schema to all pages. In Rank Math, there's a dedicated FAQ block — content should be re-added using Rank Math's FAQ block (not WPBakery accordion) so Rank Math auto-generates the FAQPage JSON-LD. Alternatively, manually add FAQPage schema via the Rank Math Custom Schema field for each page.

---

## Issue 6 — CollectionPage Schema on Service Pages ❌

**Impact:** Medium — `CollectionPage` is a schema.org type for e-commerce category listing pages (e.g. a page listing all products in a category). Using it on HVAC service pages sends incorrect signals to Google.

**Affected pages (4):**
- `/heating/gas-ducted-heating/` → `CollectionPage` only (no FAQPage, no Service)
- `/air-conditioning-installation/` → `CollectionPage` + `FAQPage`
- `/cooling/wall-split-systems-cooling/` → `CollectionPage` + `FAQPage`
- `/heating/hydronic-heating/` → `CollectionPage` + `FAQPage`

**Should be:** `Service` or `WebPage` schema type.

**Fix:** Update the Rank Math page type setting on these 4 pages from `CollectionPage` to `WebPage` (in Rank Math → Edit Page → Schema → Page Type).

---

## Issue 7 — Wrong Organisation Entity Type (HomeGoodsStore) ❌

**Impact:** Medium — the global site-wide schema identifies McKinnon Heating & Cooling as a `HomeGoodsStore` (a retail shop). This is incorrect for an HVAC service business.

```json
"@type": ["HomeGoodsStore", "Organization"]
```

**Should be:**
```json
"@type": ["HVACBusiness", "LocalBusiness"]
```
or at minimum `LocalBusiness`. Google uses this type to understand what kind of business this is for Knowledge Panel and local results.

**Fix:** In Rank Math → Titles & Meta → Local SEO (or the Schema settings), update the business type from `HomeGoodsStore` to `HVACBusiness`.

---

## Issue 8 — Article Schema on Non-Article Pages ❌

**Impact:** Low–Medium — 53 pages (homepage + all location pages) have `Article` schema type in their JSON-LD. These pages are not articles or blog posts.

```
Homepage:       ['Place', 'HomeGoodsStore', 'Organization', 'WebSite', 'WebPage', 'Person', 'Article']
Location pages: same block (shared global schema)
```

This is a Rank Math default for WordPress pages set up as "posts". The `Article` type should be removed from service and location pages.

**Fix:** Connected to Issue 6 — correcting the page schema type in Rank Math will resolve this. Each page should be set to `WebPage` (and `Service` where applicable), removing the `Article` type.

---

## Issue 9 — No BreadcrumbList Schema on Any Page ⚠️

**Impact:** Low–Medium — all 57 pages have breadcrumb navigation visible in the HTML, but none have `BreadcrumbList` schema markup. This is a missed opportunity for breadcrumb rich results in Google SERPs (the URL line shows the breadcrumb path instead of the raw URL).

**Fix:** Enable BreadcrumbList schema in Rank Math → Titles & Meta → Breadcrumbs. This is typically a one-click setting. Alternatively, enable via the Yoast/Rank Math breadcrumb component.

---

## What Is Correct ✅

| Check | Detail |
|---|---|
| All 57 URLs live | 200 OK, no broken pages |
| Meta titles | All 57 match approved document exactly |
| Meta descriptions | All 57 match approved document exactly |
| Canonical tags | All 57 self-referencing, no mismatches |
| og:url vs canonical | 0 mismatches across all 57 pages |
| Noindex | 0 pages noindexed — all pages indexable |
| Image alt tags | 0 missing, 0 empty — 731 images across 57 pages all have alt text |
| Internal links | All pages have 5+ internal links |
| Single H1 per page | 0 pages with multiple H1s, 0 pages missing H1 |
| og:title, og:description | All 57 pages correct |
| Schema parse errors | 0 — all JSON-LD is valid, parseable JSON |
| Breadcrumb HTML | Present on all 57 pages |
| Location page content | Suburb-specific content confirmed on all sampled pages |
| Service page content | All approved copy confirmed present on all 5 service pages |

---

## Priority Fix List for Developer

| Priority | Issue | Pages Affected | Effort |
|---|---|---|---|
| 🔴 High | Set Featured Image on all pages (fixes og:image + twitter:image in one step) | 53 pages | Medium — bulk action in WP media library |
| 🔴 High | Add FAQPage schema to homepage, ducted heating page, and all 51 location pages | 54 pages | High — needs per-page schema entry or bulk script |
| 🟠 Medium | Fix og:type from "article" to "website" on all service/location pages | 56 pages | Low — Rank Math global setting |
| 🟠 Medium | Fix organisation entity type from HomeGoodsStore → HVACBusiness | Global (1 setting) | Low — Rank Math local SEO setting |
| 🟠 Medium | Fix CollectionPage → WebPage/Service schema on 4 service pages | 4 pages | Low — Rank Math per-page setting |
| 🟡 Low | Enable BreadcrumbList schema | Global (1 setting) | Low — Rank Math toggle |
| 🟡 Low | Remove Article schema from non-article pages | 53 pages | Low — resolves with page type fix |
| 🟡 Low | Remove internal WP username from Twitter meta on homepage | 1 page | Low — Rank Math Twitter settings |
| 🟡 Low | Fix 2 H1 texts (split system + areas-we-serve) | 2 pages | Low — CMS text edit |
