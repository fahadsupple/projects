# Skyflex.au — Upgrade Work Review (July 2026)

**Date reviewed:** 24 July 2026
**Method:** Approved content doc + meta file (this folder) compared against the 7 live pages, scraped directly from skyflex.au.
**Source files:** `Skyflex - Content for Additional Keywords (Approved) (1).docx`, `Skyflex - Daily Tasks for Upgrade (July 2026).docx`, `Skyflex.au-Keyword-URL-Meta.xlsx`

**Bottom line:** The upgrade has been implemented and is live. All 7 pages return HTTP 200 (including the brand-new `/smart-toilets/` page, which was a 404 before), every meta title and description matches the approved doc exactly, every page has exactly one H1, all pages are indexable with self-referencing canonicals, and the navigation change was made correctly. The body content is on the pages. There are **5 issues to fix**, of which **2 are high-priority H1 misses on the awning and outdoor-TV pages**, and the rest are technical/consistency clean-ups.

---

## Scope checked (7 pages + 1 nav change, per the Daily Tasks doc)

| # | Page | URL | Live status |
|---|------|-----|-------------|
| 1 | Homepage | `/` | 200 ✓ |
| 2 | Louvred Pergolas Sydney | `/louvred-pergolas-sydney/` | 200 ✓ |
| 3 | Delta Pro Retractable Roof | `/product/delta-pro-retractable-roof/` | 200 ✓ |
| 4 | Delta Commercial Folding Arm | `/product/delta-commercial-folding-arm/` | 200 ✓ |
| 5 | Skyflex 4K Outdoor TV | `/product/skyflex-4k-android-smart-outdoor-tv/` | 200 ✓ |
| 6 | Skyflex BBQ Pods | `/product/skyflex-bbq-pods/` | 200 ✓ |
| 7 | Smart Toilets (NEW) | `/smart-toilets/` | 200 ✓ (was 404) |
| — | Nav: "View All Smart Toilets" under INDOOR PRODUCTS | → `/smart-toilets/` | ✓ Added correctly |

---

## PART 1 — Content matching (approved doc vs live)

### Meta titles — 7/7 correct ✓
Every page's `<title>` matches the approved SEO title exactly, e.g.:
- `/` → "Pergolas Melbourne | Louvred Pergola Kits and Installation | Skyflex" ✓
- `/product/delta-commercial-folding-arm/` → "Retractable Awning Melbourne | Delta Commercial Folding Arm | Skyflex" ✓
- `/smart-toilets/` → "Smart Toilets Melbourne | U6 & U7 Smartoilet | Skyflex" ✓

### Meta descriptions — 7/7 correct ✓
Every page's meta description matches the approved doc verbatim.

### H1 — 4/7 fully correct, 3/7 missing the second line ⚠️
The approved doc gives three product pages a **two-part H1**: the product name, then a keyword-rich descriptive line that the design comment (screenshot in the Daily Tasks doc, "make it smaller text… but it will be part of the H1 tag") said to render as smaller text **inside the same H1 tag**. On three pages that second line was not added at all — the live H1 is just the default product name.

| Page | Approved H1 | Live H1 | Primary keyword in H1? |
|------|-------------|---------|------------------------|
| `/` | Pergolas Melbourne | Pergolas Melbourne | ✓ |
| `/louvred-pergolas-sydney/` | Pergolas Sydney | Pergolas Sydney | ✓ |
| `/product/delta-pro-retractable-roof/` | Delta Pro Retractable Roof System Melbourne | Delta Pro Retractable Roof System Melbourne | ✓ |
| `/smart-toilets/` | Smart Toilets Melbourne: The U6 and U7 Smartoilet from Skyflex | (same, full) | ✓ |
| `/product/skyflex-bbq-pods/` | Skyflex BBQ Pods Melbourne: **An Outdoor Kitchen Made to Your Configuration** | Skyflex BBQ Pods Melbourne | ✓ keyword still present |
| `/product/delta-commercial-folding-arm/` | Delta Commercial Folding Arm: **A Retractable Awning Melbourne Buyers Own Outright** | Delta Commercial Folding Arm | ✗ **"retractable awning melbourne" absent from H1** |
| `/product/skyflex-4k-android-smart-outdoor-tv/` | Skyflex 4K Android Smart Outdoor TV: **A Waterproof TV Australia Backyards Can Actually Use** | Skyflex 4K Android Smart Outdoor TV | ✗ **"waterproof tv australia" absent from H1** |

The awning and TV pages are the material misses: their **primary keyword now appears nowhere in the H1**. On BBQ pods the keyword ("BBQ Pods Melbourne") is still in the H1, so only the descriptive tagline is missing — low priority. Note the pattern is inconsistent: Delta Pro and Smart Toilets received their full keyword-rich H1, so the developer clearly can do it on a product page — it was just skipped on three.

### Body content — present on all 7 pages ✓
Every approved body section is live: the intros, the "Is this right for you / Who it suits" blocks, the "About Skyflex" sections, and the FAQ answers all appear. Spot-checks of distinctive sentences (pricing, IP ratings, warranty, spec values, the $18,990 competitor comparison, the "power point / GPO" smart-toilet warning) all pass. The apparent "missing" blocks in an automated diff were formatting differences only (bulleted labels rendered with bold, spec values moved into the WooCommerce attributes table) — the text itself is on the page.

One genuine content note on **Delta Pro**: the approved standalone **"Delta Pro specifications"** bulleted list is not rendered as written. The values themselves are all live — some in the WooCommerce "Additional information" attributes (Brand: Dooya, IP Class: IP67, Connection: AU Plug In) and some in the FAQ answers (the six sizes, fabric/frame colours) — but the discrete spec block from the approved doc, with its own H2, isn't there. All data is present, just relocated; confirm the client is happy with the WooCommerce-attribute presentation rather than the approved bullet list.

---

## PART 2 — Content issues

### 2.1 Existing product copy still uses US spelling (sits next to the new AU copy) — Low
The newly-added approved copy is clean Australian English. But the **pre-existing** manufacturer copy still on the product pages contains US spellings, so each page now mixes both:
- `/product/delta-pro-retractable-roof/` — "aluminum track"
- `/product/delta-commercial-folding-arm/` — "customization", "resists fading and mold", "6063 aluminum alloy"
- `/product/skyflex-bbq-pods/` — "exterior color", "customizable / customization"

These aren't from this content round, but they're visible on the same pages as the new copy. Recommend correcting to **aluminium, customisation, mould, colour** while the pages are open.

### 2.2 Homepage / Sydney FAQ — only partially updated (likely intentional) — confirm
The client's note in the meta file said the homepage and Sydney page have "existing content we don't want to change." Accordingly, both pages kept their **existing** FAQ section (heading "Frequently Asked Questions About Pergolas in Melbourne / …Sydney") and the developer merged in only *some* of the approved FAQ questions (e.g. "Do I need council approval…", "Can I install a louvred pergola myself?", "What warranty comes with a Skyflex pergola?" were added; "How do louvred pergolas handle Melbourne's weather?" and "What is the difference between the Delta models?" were not). This is consistent with the "don't change existing content" instruction, so it's probably **as intended** — but flagging it so it's a conscious decision, not an oversight. (The full approved FAQ set is only fully live on the new/dedicated pages.)

---

## PART 3 — Coding / SEO issues

**Good — verified correct on all 7 pages:**
- Exactly **one H1** per page ✓
- **Indexable:** `robots = index, follow` on every page (not noindex) ✓
- **Canonical** present and self-referencing on every page ✓
- **Open Graph** titles present and correct ✓
- **Schema present:** WebPage + BreadcrumbList + WebSite everywhere; Product + AggregateOffer on the four product pages; FAQPage on the homepage and Sydney page ✓
- **Navigation:** "View All Smart Toilets" added under INDOOR PRODUCTS, linking to `/smart-toilets/` ✓

### 3.1 FAQ schema is stale on the homepage & Sydney page — Medium
Both pages now show a **mix of old and newly-added FAQ questions in the visible content**, but the **FAQPage JSON-LD schema still lists only the 5 original questions** — it wasn't regenerated when the new questions were added. Google sees a visible-FAQ-vs-markup mismatch. Update the FAQ schema on `/` and `/louvred-pergolas-sydney/` to match what's now on the page (or regenerate it via the FAQ block/Yoast).

### 3.2 New FAQ blocks have no FAQPage schema — Low / opportunity
The four product pages and the new `/smart-toilets/` page all carry substantial approved FAQ sections in visible content, but none of them output **FAQPage** schema (product pages emit Product/Offer only; smart-toilets emits WebPage only). Adding FAQPage markup to these five pages would make the Q&A eligible for FAQ-rich treatment and helps AI/AEO surfacing — worth doing given how much FAQ content was written for them.

---

## PART 4 — Items for the client (not developer defects)

- **Delta Pro "100% waterproof when closed" spec** carried a client comment in the approved doc ("Kindly confirm if these are correct"). The spec is live on the page — confirm the waterproof claim is accurate before it stays. (Consistent with the standing open item in client memory about not letting "waterproof" copy get ahead of the actual product's certified rating.)
- The **U6 and U7 Smartoilet** products still need to be pulled out of WooCommerce's "Uncategorized" bucket and associated with the new `/smart-toilets/` collection page so the category taxonomy is clean (long-standing to-do from the keyword round).

---

## Summary — action list for the developer

| Priority | Page(s) | Action |
|----------|---------|--------|
| **High** | `/product/delta-commercial-folding-arm/` | Add the approved second H1 line "A Retractable Awning Melbourne Buyers Own Outright" as smaller text **inside the H1 tag** (per the design comment). Primary keyword is currently absent from the H1. |
| **High** | `/product/skyflex-4k-android-smart-outdoor-tv/` | Add the approved second H1 line "A Waterproof TV Australia Backyards Can Actually Use" inside the H1 tag. Primary keyword currently absent from the H1. |
| **Medium** | `/` and `/louvred-pergolas-sydney/` | Update FAQPage schema so it matches the newly-added visible FAQ questions (currently stale — lists only the old 5). |
| **Low** | `/product/skyflex-bbq-pods/` | Add the approved H1 tagline "An Outdoor Kitchen Made to Your Configuration" inside the H1 tag (keyword already present, so cosmetic). |
| **Low** | `/product/delta-pro-retractable-roof/`, `/delta-commercial-folding-arm/`, `/skyflex-bbq-pods/` | Fix US spellings in the existing product copy: aluminum→aluminium, customization→customisation, mold→mould, color→colour. |
| **Low / opp.** | 4 product pages + `/smart-toilets/` | Add FAQPage schema to the new FAQ sections. |
| **Confirm** | `/product/delta-pro-retractable-roof/` | Confirm the WooCommerce-attributes + FAQ presentation of specs is acceptable in place of the approved standalone "Delta Pro specifications" block (all values are present). |

**What was done correctly:** new `/smart-toilets/` page built and live; all 7 meta titles + descriptions exact; 4/7 H1s exact; all body content present; nav link added; canonicals, robots (indexable), OG, and base schema all correct; new copy in clean AU English.
