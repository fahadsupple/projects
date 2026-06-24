# McKinnon Heating & Cooling — Content & Image Audit
**Date:** 2026-06-24
**Auditor:** Claude (via Playwright)
**Scope:** 118 pages from page-sitemap.xml — full review of 13 core pages + 3 location page samples + gallery index

---

## Summary

| Category | Count |
|---|---|
| Critical issues | 4 |
| High priority fixes | 6 |
| Medium priority fixes | 5 |
| Low / advisory notes | 4 |
| **Total issues** | **19** |

Screenshots saved to: `content-review/screenshots/`

---

## Pages Audited

| # | URL | Screenshot |
|---|---|---|
| 1 | `/` (Homepage) | 01-homepage.jpeg |
| 2 | `/about-us/` | 02-about-us.jpeg |
| 3 | `/specials/` | 03-specials.jpeg |
| 4 | `/faqs/` | 04-faqs.jpeg |
| 5 | `/testimonials/` | 05-testimonials.jpeg |
| 6 | `/contact-us/` | 06-contact-us.jpeg |
| 7 | `/areas-we-serve/` | 07-areas-we-serve.jpeg |
| 8 | `/energy-efficiency-and-cost-savings/` | 08-veu-energy.jpeg |
| 9 | `/servicing-repair-requests/` | 09-servicing-repairs.jpeg |
| 10 | `/locality-guide/` | 10-locality-guide.jpeg |
| 11 | `/shop/` | 11-shop.jpeg |
| 12 | `/galleries/` | 15-galleries.jpeg |
| 13 | `/heating-and-cooling-moorabbin/` (sample) | 12-location-heating-cooling-moorabbin.jpeg |
| 14 | `/ducted-heating-brighton/` (sample) | 13-location-ducted-brighton.jpeg |
| 15 | `/air-conditioning-moorabbin/` (sample) | 14-location-aircon-moorabbin.jpeg |

---

## CRITICAL Issues

### C1 — Broken internal links embedded as plain text (`/areas-we-serve/`)
**Page:** `/areas-we-serve/`
**Severity:** Critical — broken user experience + SEO cannibalization risk

Three internal hyperlinks were not converted properly and appear as plain text fragments in the middle of sentences:
- `"provides expert heating and cooling services/heating-and-cooling-services/ across Melbourne"` — raw URL path left in body text
- `"We specialise in ducted heating systems/ducted-heating/ that we properly design"` — raw URL path in body text
- `"Our team also leads the way in gas to electric conversions/gas-to-electric-conversions/"` — raw URL path in body text

These look like the editor used markdown-style link syntax that didn't render, or placeholders that were never converted to live links. Users see the URL paths as text. These services pages may not exist at those paths.

**Fix:** Convert each to a proper hyperlink pointing to the correct service page, or remove the URL fragment if the destination page doesn't exist.

---

### C2 — `/ducted-heating/` redirects to a suburb page, not a service page
**Page:** Multiple location pages (e.g. `/air-conditioning-moorabbin/`) link to `/ducted-heating/`
**Severity:** Critical — SEO redirect sends users to wrong page

When a user clicks the internal link labelled "ducted reverse cycle air conditioning" on the AC Moorabbin page, they are redirected to `/ducted-heating-brighton/` (a Brighton suburb location page). This is clearly wrong.

**Fix:** Update all internal links pointing to `/ducted-heating/` to point to the correct service page: `/heating/gas-ducted-heating/`

---

### C3 — `"Years In Business" counter displaying "0"` (Homepage)
**Page:** `/` (Homepage)
**Severity:** Critical — visible to all users, damages trust

The homepage counter showing "0 Years In Business" appears to be a JavaScript animation that's not initialising. When the page loads, the counter value stays at 0. As of 2026, McKinnon Heating & Cooling has been operating since 1973 — 53 years.

**Fix:** Check the counter plugin/JS. Set a fallback static value of "53" so it shows correctly even if the animation fails.

---

### C4 — Email link split into two broken anchor tags (Homepage)
**Page:** `/` (Homepage)
**Severity:** Critical — broken link in body content

In the homepage body copy, the email `sales@mckinnonheating.com.au` is split into two separate anchor tags:
- First link: "sale" → `mailto:sales@mckinnonheating.com.au`
- Second link: "s@mckinnonheating.com.au" → `mailto:sales@mckinnonheating.com.au`

Visually it may look like the email address, but the link structure is broken and will confuse screen readers and bots.

**Fix:** Merge into a single clean anchor: `<a href="mailto:sales@mckinnonheating.com.au">sales@mckinnonheating.com.au</a>`

---

## HIGH Priority Issues

### H1 — Inconsistent Google rating across pages (3 different values)
**Pages:** Homepage, `/areas-we-serve/`, location pages
**Severity:** High — undermines credibility, looks unprofessional

Three different Google ratings are cited across the site:
- Homepage feature box: **"4.7/5 Google Rating"**
- Homepage "Why Choose" section: **"4/5 Google rating"**
- `/areas-we-serve/` and all location pages: **"4.4 out of 5 Google rating"**

Only one can be correct. If the real current rating is 4.4, the other two references must be updated.

**Fix:** Agree on the current rating (check Google Business Profile) and standardise across all pages site-wide. Search for "4.7" and "4/5" in the CMS and update all instances.

---

### H2 — Business age stated incorrectly across multiple pages (Homepage)
**Page:** `/` (Homepage hero text)
**Severity:** High — factual inaccuracy, business founded 1973

The homepage hero says **"over 51 years of experience"**. As of 2026, McKinnon Heating & Cooling has been operating since 1973 = **53 years**. Other pages correctly say "over 50 years" (which rounds down acceptably), but "51 years" is a stale specific number from a previous year.

**Fix:** Update hero text to "over 53 years" or use the safe generic "over 50 years" as used elsewhere.

---

### H3 — `/air-conditioning-installation/` page missing from sitemap
**Page:** `/air-conditioning-installation/`
**Severity:** High — page is live and linked from location pages and shop, but not submitted to search engines

The page exists (confirmed via Playwright) and is linked from multiple AC location pages and the shop. However, it does not appear in `/page-sitemap.xml`. This means Google may not crawl it efficiently.

**Fix:** Add `/air-conditioning-installation/` to the page sitemap via Rank Math.

---

### H4 — Duplicate bullet point in Servicing & Repairs page
**Page:** `/servicing-repair-requests/`
**Severity:** High — looks like a copy-paste error, unprofessional

Two consecutive bullet points are identical:
- "Labour to fix a part under warranty is chargeable."
- "Labour to fix a part under warranty is chargeable."

**Fix:** Delete one of the duplicate bullet points.

---

### H5 — Double H1 on Specials page
**Page:** `/specials/`
**Severity:** High — SEO error

The page header generates an H1 ("2026 Specials Ending Soon"), and there is a second H1 inside the content area ("Rinnai Air Winter Cashback Promotion 2026"). Having two H1 tags on a single page is an SEO issue — only one H1 is allowed.

**Fix:** Change the Rinnai promotion title from H1 to H2 in the WordPress editor.

---

### H6 — Typo: "Terms & Conditons" on Specials page
**Page:** `/specials/`
**Severity:** High — visible spelling error on a promotional legal link

The T&C link reads "Terms & Conditons" (missing "i" in Conditions).

**Fix:** Correct to "Terms & Conditions".

---

## MEDIUM Priority Issues

### M1 — Typo: "please sent it to" on Contact page
**Page:** `/contact-us/`
**Severity:** Medium — grammar error, first impressions page

Body text reads: "If you'd rather send us an email, please sent it to sales@mckinnonheating.com.au"

"sent" should be "send".

**Fix:** Change "please sent it to" → "please send it to"

---

### M2 — Business hours formatting error in header
**Page:** All pages (site-wide header)
**Severity:** Medium — visible on every page

The header bar shows: `"Mon - Fri / 9:00AM - 4: 30PM"` — there is a space before "30" in "4: 30PM".

**Fix:** Remove the space: `Mon - Fri / 9:00AM - 4:30PM`

---

### M3 — "Factory" language on Locality Guide page
**Page:** `/locality-guide/`
**Severity:** Medium — inaccurate description of the business

The page states: "Our factory is now located in Moorabbin..."

McKinnon Heating & Cooling is a service business, not a factory. The word "factory" appears to be legacy copy carried over from a much older version of the website and creates the wrong impression.

**Fix:** Update to: "Our office is located in Moorabbin, servicing Melbourne & the Mornington Peninsula."

---

### M4 — Unclosed parenthesis on location pages (VEU mention)
**Pages:** `/heating-and-cooling-moorabbin/`, `/air-conditioning-moorabbin/` (and likely all location pages)
**Severity:** Medium — looks sloppy, appears on 50 pages

Two instances of unclosed brackets found in location page content:
- "through the Victorian Energy Upgrades (VEU Program, which can help..." → missing closing `)`
- Bullet point: "Energy efficiency upgrades (VEU Program" → missing closing `)`

**Fix:** Update template content to: "through the Victorian Energy Upgrades (VEU) Program, which can help..." and "Energy efficiency upgrades (VEU Program)"

---

### M5 — Duplicate intro paragraph on FAQ page
**Page:** `/faqs/`
**Severity:** Medium — duplicate content (same paragraph as About Us page)

The FAQ page opens with the same introductory paragraph as the About Us page: "For over half a century, McKinnon Heating & Cooling has been at the forefront of providing exceptional heating and cooling solutions..."

This is duplicate content that adds no value on the FAQ page and may slightly dilute SEO.

**Fix:** Remove or replace the intro paragraph on the FAQ page with content specific to FAQs (e.g., "Have a question about heating or cooling? Browse our most frequently asked questions below.").

---

## LOW / Advisory Notes

### L1 — Navigation "Areas" submenu items link to "#" (dead links)
**Page:** All pages (sitewide nav)
**Severity:** Low — dropdown items don't work but the Areas page itself is accessible

In the main navigation, the "Areas" dropdown contains three sub-items — "Air Conditioning", "Ducted Heating", "Heating and Cooling" — that all link to `#` (the current page top). These should link to the `/areas-we-serve/` page or to anchor sections listing the relevant location pages.

**Fix:** Update the href for each dropdown item to point to the relevant section on `/areas-we-serve/` using anchor IDs, or link directly to `/areas-we-serve/`.

---

### L2 — FAQ content is dated and generic
**Page:** `/faqs/`
**Severity:** Low — content quality issue

The FAQ content (especially the hydronic heating and gas ducted sections) references sources from 2000 ("Source: Assessment of Greenhouse Gas Emissions from Natural Gas, Australian Gas Association, 2000") and contains generic boilerplate questions. This weakens E-E-A-T signals.

**Fix:** Review and refresh FAQ content. Prioritise company-specific FAQs (pricing, process, lead times, brands) over generic industry text. Remove or update the 2000 source citation.

---

### L3 — Shop page: Gree multi-head product shows "Add-On-Cooling-Brochure" image
**Page:** `/shop/`
**Severity:** Low — image relevance issue

The Gree multi-head split system product listing displays an image with the alt text "Add-On-Cooling-Brochure" — this appears to be a generic brochure/document image rather than an actual photo of the Gree unit.

**Fix:** Replace with an appropriate product image of the Gree multi-head split system.

---

### L4 — Location pages have 0 images in sitemap (all 50 pages)
**Sitemap:** `page-sitemap.xml`
**Severity:** Low-advisory — image SEO opportunity

All 50 location pages (ducted-heating, air-conditioning, heating-and-cooling sub-pages) show 0 images in the sitemap. These pages have no visible inline images, which misses an opportunity to add visual trust signals and image SEO value.

**Advisory:** Consider adding at least one relevant image per location page (e.g., an installed unit in a local home from the galleries, with the suburb name in the alt text).

---

## Image Relevance Assessment

| Page | Images Present | Assessment |
|---|---|---|
| Homepage | 15 (hero, gallery, brand logos, partner images) | Relevant — HVAC equipment, local homes |
| About Us | 3 (about-mckinnon images) | Relevant — team/office photos |
| Specials | 4 (Rinnai promotion + Zip Pay) | Relevant |
| FAQs | 8 | Relevant — service-related imagery |
| Testimonials | 0 | No images — acceptable for review page |
| Contact | 0 | Acceptable |
| Areas We Serve | 0 | Weak — map embed but no images |
| VEU / Energy | 1 | Relevant |
| Servicing & Repairs | 0 | Weak |
| Locality Guide | 0 | No images |
| Shop | 2 per product | Generally relevant (see L3 above) |
| Galleries | 17+ | Excellent — real project photos |
| All 50 location pages | 0 | See L4 |

---

## Pages NOT Audited (Status Notes)

| Page Type | Count | Status |
|---|---|---|
| `galleries/homes-completed-gallery/[project]/` | ~30 pages | Image-only gallery pages — spot-checked structure only, content is photo collections of real completed jobs, no text content issues expected |
| All specific gallery category pages | ~14 | Screenshotted main `/galleries/` index page; individual galleries appear to be legitimate photo collections |
| `/trading-terms/` | 1 | Legal page — not audited for content quality, review with solicitor |
| `/disclaimer/` | 1 | Legal page — not audited |

---

## Recommended Fix Priority Order

| Priority | Issue | Fix Time (est.) |
|---|---|---|
| 1 | C4 — Broken email link (Homepage) | 5 min |
| 2 | C3 — Years counter showing 0 (Homepage) | 15 min |
| 3 | C1 — Broken text links on /areas-we-serve/ | 20 min |
| 4 | C2 — /ducted-heating/ redirecting to Brighton suburb page | 10 min |
| 5 | H6 — Typo "Conditons" on Specials | 2 min |
| 6 | M1 — Typo "sent" on Contact | 2 min |
| 7 | H4 — Duplicate bullet on Servicing page | 2 min |
| 8 | H5 — Double H1 on Specials | 5 min |
| 9 | H1 — Standardise Google rating site-wide | 30 min |
| 10 | H2 — Update "51 years" to "53 years" on homepage | 5 min |
| 11 | M4 — Fix unclosed parentheses on location pages | 15 min (template edit) |
| 12 | M2 — Fix header hours formatting | 5 min |
| 13 | M3 — Fix "factory" language on Locality Guide | 5 min |
| 14 | H3 — Add /air-conditioning-installation/ to sitemap | 5 min |
| 15 | L1 — Fix nav dropdown dead links | 15 min |
| 16 | M5 — Remove duplicate intro from FAQ page | 5 min |
| 17 | L3 — Fix Gree product image | 10 min |
| 18 | L2 — Refresh FAQ content | 2–4 hrs |
| 19 | L4 — Add images to location pages | Ongoing |

---

*Audit completed: 2026-06-24. Audited via live Playwright browser session against https://www.mckinnonheating.com.au*
