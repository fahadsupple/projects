# energus.com.au — Content Deployment Verification Audit
**Date:** 2026-06-30  
**Auditor:** Claude (Playwright live checks)  
**Prior audit date:** 2026-06-24

---

## Summary Table

| Category | Items Checked | Passed ✅ | Partially Fixed ⚠️ | Failed / Outstanding ❌ |
|---|---|---|---|---|
| Part 1 — Prior issues re-check | 5 | 1 | 0 | 4 |
| Part 2 — Website Updates doc | 10 | 3 | 3 | 4 |
| **Total** | **15** | **4** | **3** | **8** |

---

## Part 1 — Re-check of Prior Issues (2026-06-24)

### C1 — Homepage (https://energus.com.au/) ✅ FIXED

All four required elements are now live:

| Element | Required | Live | Status |
|---|---|---|---|
| Meta Title | "Commercial & Industrial Solar and Battery Storage Australia \| Energus Pty Ltd" | "Commercial & Industrial Solar and Battery Storage Australia \| Energus Pty Ltd" | ✅ |
| Meta Desc | "Energus Pty Ltd delivers end-to-end commercial and industrial solar and battery storage systems across Australia. Top 3 C&I solar retailers nationally." | Exact match | ✅ |
| H1 | "Commercial & Industrial Solar and Battery Storage Australia-Wide" | "Commercial & Industrial Solar and Battery Storage Australia-Wide" | ✅ |
| Body stats | 22.5% ROI, 100MW, 1,800+ quotes | All three present | ✅ |

---

### H1 — /locations/ (https://energus.com.au/locations/) ❌ STILL OUTSTANDING

| Element | Required | Live |
|---|---|---|
| Meta Title | "Commercial Solar Near Me \| Dandenong South \| Energus" | "Locations - Energus - Solar Energy for Australian Business" |
| Meta Desc | "Searching for commercial solar near me in Dandenong South? Energus designs and installs solar systems that cut energy costs for industrial businesses." | MISSING (empty) |

Screenshot: `screenshots/H1-locations-still-wrong.jpeg`

---

### H2 — /earc-solar-skin/ (https://energus.com.au/earc-solar-skin/) ❌ STILL OUTSTANDING

| Element | Required | Live |
|---|---|---|
| Meta Title | "Lightweight Solar Panels for Commercial Roofs \| eARC by Sunman \| Energus Pty Ltd" | "eARC Solar Skin - lightweight solar solution - commercial solar" |
| Meta Desc | About glassless non-penetrating panels | Old generic description (no glassless/non-penetrating mention) |
| H3 sections | 6 H3s (Older commercial buildings, Heritage-listed, Curved roofs, Membrane roofs, Insulated metal deck, Facades) | 0 H3s present |
| H1 count | 1 H1 | 4 H1s ("INTRODUCING eARC", "The panel.", "The panel.", "The eARC Quickbond Installation Method") |

---

### M1 — /commercial-battery-storage-melbourne/ ❌ STILL OUTSTANDING

| Element | Required | Live |
|---|---|---|
| Meta Title | "Commercial Battery Storage Melbourne \| Energus Pty Ltd" | "Commercial Battery Storage Melbourne \|Energus Pty Ltd" |

The missing space before the pipe character (`|Energus` instead of `| Energus`) is still present.

Screenshot: `screenshots/M1-battery-melbourne-title-space.jpeg`

---

### M2 — H3 warranty on /commercial-solar-sydney/ ❌ STILL OUTSTANDING

Live page H3 elements containing "warranty" or "workmanship":
- "25 Year Performance Warranty"
- "10 YEAR WORKMANSHIP WARRANTY"

The H3 still reads **"10 YEAR WORKMANSHIP WARRANTY"**. Required correction is **"5 YEAR WORKMANSHIP WARRANTY"**.  
This is a site-wide template issue — the same H3 likely appears on all service/location pages.

---

## Part 2 — Website Updates Doc Items

### 2a — Canonical tags on /locations/nsw/ paginated pages ❌ NOT DONE

All 5 paginated pages have **self-referencing** canonical tags instead of pointing to `https://energus.com.au/locations/nsw/`.

| URL | Canonical Found | Required |
|---|---|---|
| /locations/nsw/page/2/ | https://energus.com.au/locations/nsw/page/2/ | https://energus.com.au/locations/nsw/ |
| /locations/nsw/page/3/ | https://energus.com.au/locations/nsw/page/3/ | https://energus.com.au/locations/nsw/ |
| /locations/nsw/page/4/ | https://energus.com.au/locations/nsw/page/4/ | https://energus.com.au/locations/nsw/ |
| /locations/nsw/page/5/ | https://energus.com.au/locations/nsw/page/5/ | https://energus.com.au/locations/nsw/ |
| /locations/nsw/page/6/ | https://energus.com.au/locations/nsw/page/6/ | https://energus.com.au/locations/nsw/ |

---

### 2b — /aboutus renamed to /about-us/ ❌ NOT DONE

| Check | Expected | Result |
|---|---|---|
| /aboutus redirect | Should 301 → /about-us/ | Loads as /aboutus (no redirect) |
| /about-us/ exists | Should be live | Returns 404 "Page not found" |
| "Scale, Specialisation & Proved Capacity" H2 | Should be added | Not applicable — page doesn't exist |
| Accreditations H2 (ISO 45001, ISO 9001, licence numbers) | Should be added | Not applicable — page doesn't exist |

The URL rename and content additions have not been implemented at all.  
Screenshot: `screenshots/2b-aboutus-no-redirect.jpeg`

---

### 2c — Battery page overhaul ⚠️ PARTIALLY DONE

**Redirects (all correct):**

| Redirect | Expected | Result |
|---|---|---|
| /battery/ | → /commercial-battery-storage/ | ✅ Redirects correctly |
| /battery-for-business/ | → /commercial-battery-storage/ | ✅ Redirects correctly |
| /commercial-battery-installer/ | → /commercial-battery-storage/ | ✅ Redirects correctly |

**Content on /commercial-battery-storage/:**

| Element | Required | Result |
|---|---|---|
| Meta Title | "Commercial Battery Storage Australia \| C&I Solutions \| Energus Pty Ltd" | ✅ Exact match |
| H1 | "Commercial Battery Storage in Australia" | ✅ Present |
| H2 "Scalable BESS Solutions Across Australia" | Added | ✅ Present |
| H3 "Technical Precision & Compliance" | Added | ✅ Present |
| H3 "National Footprint, Local Expertise" | Added | ❌ NOT FOUND — not in H3s or anywhere in body text |

**Outstanding:** One H3 missing — "National Footprint, Local Expertise".

---

### 2d — /solar-for-business/ → /commercial-solar/ ⚠️ PARTIALLY DONE

**Redirects (all correct):**

| Redirect | Expected | Result |
|---|---|---|
| /solar-for-business/ | → /commercial-solar/ | ✅ Redirects correctly |
| /commercial-solar-installer/ | → /commercial-solar/ | ✅ Redirects correctly |
| /commercial-solar-panels/ | → /commercial-solar/ | ✅ Redirects correctly |
| /solar-energy-for-aussie-business/ | → /commercial-solar/ | ✅ Redirects correctly |

**Content on /commercial-solar/:**

| Element | Required | Live | Status |
|---|---|---|---|
| Meta Title | "Commercial Solar Australia \| Top-Rated C&I Installer \| Energus Pty Ltd" | Exact match | ✅ |
| Meta Desc | "...55MW+ delivered. ISO-certified. Get a free quote." | Missing trailing period | ⚠️ Minor |
| H1 | "Commercial Solar Australia" | "COMMERCIAL SOLAR AUSTRALIA" (CSS uppercase — same text) + 3 additional H1s ("Go Solar." ×3) | ⚠️ Multiple H1s |
| H2 "SOLAR ENERGY FOR BUSINESS" | Present | ✅ (appears in multiple instances) | ✅ |
| H2 "Commercial Solar for Every Business Type" | Present | ✅ | ✅ |
| H2 "Industrial Solar Australia" | Present | "INDUSTRIAL SOLAR AUSTRALIA" (CSS uppercase) | ✅ |
| H2 "Why Leading Australian Enterprises Choose Energus" | Present | ✅ | ✅ |
| H2 "National Coverage, Local Engineering" | Present | ✅ | ✅ |
| H2 "Commercial Solar FAQs" | Present | "COMMERCIAL SOLAR FAQS" | ✅ |

**Outstanding:** Page has 4 H1 elements (duplicated template elements: "COMMERCIAL SOLAR AUSTRALIA" + "Go Solar." appearing 3 times). This is a template/page-builder duplication issue — also flagged in 2g below.

---

### 2e — /industrial_solar_energy/ noindex ❌ NOT DONE

Live robots meta on `https://energus.com.au/industrial_solar_energy/`:  
`<meta name="robots" content="noodp">`

Required: content must include `noindex`.  
Current value "noodp" blocks ODP description reuse but does **not** block indexing. The page remains indexed.

Screenshot: `screenshots/2e-industrial-solar-noindex-missing.jpeg`

---

### 2f — /sheetmetal/ redirect ✅ DONE

`https://energus.com.au/sheetmetal/` redirects to `https://energus.com.au/commercial-solar/` ✅

---

### 2g — Multiple H1 fixes ❌ NOT DONE

None of the six pages have been corrected to a single H1:

| Page | Required | H1 Count | H1 Texts Found |
|---|---|---|---|
| /earc-solar-skin/ | 1 | **4** | "INTRODUCING eARC", "The panel." (×2), "The eARC Quickbond Installation Method" |
| /commercial-solar/ | 1 | **4** | "COMMERCIAL SOLAR AUSTRALIA", "Go Solar." (×3) |
| /service-centre/ | 1 | **8** | "TOP COMMERCIAL SOLAR INSTALLER", "SERVICING & MAINTENANCE FOR COMMERCIAL SOLAR SYSTEM", "Maintain A Healthy Long Term Asset", "Maximise Performance", "Reduce Hazard & Risk", "Book your service now", "Our servicing team will be in touch...", "Get A Quote Now" |
| /finance/ | 1 | **5** | "SOLAR FINANCE FOR AUSTRALIAN BUSINESS", "Speak with our solar advisors...", "Get A Quote Now", "Book A Discovery Session" (×2) |
| /about-us/ | 1 | N/A | Page returns 404 — doesn't exist yet |
| /landlords-property-groups/ | 1 | **12** | "SOLAR ENERGY FOR LANDLORDS & PROPERTY GROUPS" + 11 CTA/repeated H1s |

This appears to be a **site-wide theme/template issue** — CTAs, form headings, and section titles are incorrectly marked as H1s across many pages. It needs a template-level fix, not page-by-page edits.

---

### 2h — Privacy policy contact info ✅ DONE

All checks pass on `https://energus.com.au/privacy-policy/`:

| Check | Result |
|---|---|
| "Suite 901, Level 9, 153 Walker Street, North Sydney NSW" present | ✅ |
| Phone 1300 090 187 present | ✅ |
| Email sales@energus.com present | ✅ |
| "How we protect your data" section removed | ✅ |
| "What data breach procedures we have in place" removed | ✅ |
| "What third parties we receive data from" removed | ✅ |
| "What automated decision making..." removed | ✅ |
| "Industry regulatory disclosure requirements" removed | ✅ |

---

### 2i — /solar-panels/ missing video ⚠️ PARTIALLY RESOLVED

No `<video>` element and no `<iframe>` are present on `https://energus.com.au/solar-panels/`. The video element has been removed from the DOM.

However, 2 broken images exist on the page — both are the **footer logo** (`Energus-White-Logo-P.webp`) which 404s. This is a separate issue from the video, but should be noted as a new bug.

The original video content area has been removed without confirmed replacement. The page renders without a visible error, but there is no image or embed replacing the video slot either. The footer logo being broken is a sitewide issue.

Screenshot: `screenshots/2i-solar-panels.jpeg`

---

### 2j — CTA button links ⚠️ PARTIAL

**https://energus.com.au/projects-aumagic/:**  
Both specified CTAs are present and linked correctly:
- "START MY SOLAR PROJECT" → `https://energus.com.au/getquote` ✅
- "START MY SWITCH TO SOLAR ENERGY TODAY" → `https://energus.com.au/getquote` ✅

**https://energus.com.au/power-purchase-agreement/:**  
Neither "START MY SOLAR PROJECT" nor "START MY SWITCH TO SOLAR ENERGY TODAY" buttons exist on this page. The page uses "FREE QUOTE" CTA buttons (×5), all correctly linked to `/getquote`. The specific button text from the spec was not found — it's unclear if this text was supposed to be added as part of the update or if the page was always different.

---

## Issues Registry — Outstanding Items to Fix

### Priority 1 — Critical (SEO impact, wrong indexation)

| # | Issue | Page | Fix Required |
|---|---|---|---|
| 1 | noindex not applied | /industrial_solar_energy/ | Change `meta robots` from `noodp` to `noindex, noodp` |
| 2 | /about-us/ returns 404 | /aboutus and /about-us/ | Create /about-us/ page, 301 redirect /aboutus → /about-us/, add new H2 content blocks |
| 3 | Canonical tags self-referencing | /locations/nsw/page/2/ through /page/6/ | Set canonical on each paginated page to point to https://energus.com.au/locations/nsw/ |

### Priority 2 — High (meta data, brand accuracy)

| # | Issue | Page | Fix Required |
|---|---|---|---|
| 4 | Meta title and desc not updated | /locations/ | Set title to "Commercial Solar Near Me \| Dandenong South \| Energus", add meta desc |
| 5 | Meta title and desc not updated, H3s missing, 4 H1s | /earc-solar-skin/ | Update meta title/desc, add 6 H3 sections, fix H1 count to 1 |
| 6 | Missing space in meta title | /commercial-battery-storage-melbourne/ | Change `\|Energus` to `\| Energus` |
| 7 | H3 still says "10 YEAR WORKMANSHIP WARRANTY" | /commercial-solar-sydney/ (and all location/service pages using same template) | Change to "5 YEAR WORKMANSHIP WARRANTY" in the page template |

### Priority 3 — Medium (structural SEO)

| # | Issue | Page | Fix Required |
|---|---|---|---|
| 8 | Multiple H1s sitewide | /earc-solar-skin/, /commercial-solar/, /service-centre/, /finance/, /landlords-property-groups/ | Template-level fix — CTAs, form headers, repeated section headings incorrectly tagged as H1 |
| 9 | "National Footprint, Local Expertise" H3 missing | /commercial-battery-storage/ | Add H3 "National Footprint, Local Expertise" with appropriate supporting copy |
| 10 | Meta desc missing trailing period | /commercial-solar/ | Add period: "...Get a free quote." |

### Priority 4 — Low / New bug

| # | Issue | Page | Fix Required |
|---|---|---|---|
| 11 | Footer logo broken (404) | Sitewide | Fix path to `Energus-White-Logo-P.webp` in the theme — affects all pages |
| 12 | /power-purchase-agreement/ CTA buttons | /power-purchase-agreement/ | Clarify with client: should "START MY SOLAR PROJECT" / "START MY SWITCH" buttons be added? Currently uses "FREE QUOTE" CTAs (already linking to /getquote correctly) |

---

## Fix Checklist for Developer

```
[ ] 1.  /industrial_solar_energy/ — add noindex to robots meta (meta name="robots" content="noindex, noodp")
[ ] 2.  Create /about-us/ page (migrate content from /aboutus), 301 redirect /aboutus → /about-us/
[ ] 3.  Add H2 "Scale, Specialisation & Proven Capacity" to /about-us/ (80 yrs combined, lightweight tech, track record)
[ ] 4.  Add H2 "Our Standards, Accreditations & Compliance" to /about-us/ (ISO 45001:2018, ISO 9001:2016, NSW 279520C / QLD 91482 / SA PGE 335943)
[ ] 5.  /locations/nsw/page/2–6: set canonical to https://energus.com.au/locations/nsw/
[ ] 6.  /locations/ — update meta title to "Commercial Solar Near Me | Dandenong South | Energus"
[ ] 7.  /locations/ — add meta desc: "Searching for commercial solar near me in Dandenong South? Energus designs and installs solar systems that cut energy costs for industrial businesses."
[ ] 8.  /earc-solar-skin/ — update meta title: "Lightweight Solar Panels for Commercial Roofs | eARC by Sunman | Energus Pty Ltd"
[ ] 9.  /earc-solar-skin/ — update meta desc (glassless, non-penetrating panels)
[ ] 10. /earc-solar-skin/ — add 6 H3 sections: Older commercial buildings, Heritage-listed, Curved roofs, Membrane roofs, Insulated metal deck, Facades
[ ] 11. /earc-solar-skin/ — fix H1 structure (currently 4 H1s — only main heading should be H1)
[ ] 12. /commercial-battery-storage-melbourne/ — add space: "| Energus" (not "|Energus") in meta title
[ ] 13. Page template — change "10 YEAR WORKMANSHIP WARRANTY" to "5 YEAR WORKMANSHIP WARRANTY" in H3
[ ] 14. Sitewide template — fix multiple H1 issue: CTA blocks, form headers, section headings should be H2 or H3, not H1
[ ] 15. /commercial-battery-storage/ — add H3 "National Footprint, Local Expertise" with copy
[ ] 16. /commercial-solar/ — add trailing period to meta desc
[ ] 17. Fix footer logo path (Energus-White-Logo-P.webp 404ing on all pages)
```
