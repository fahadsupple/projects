# energus.com.au — Content Deployment Verification

**Date:** 2026-07-13
**Method:** Live crawl of all 42 pages in `Energus.com.au (Approved).docx`, desktop + mobile user-agents, compared against the approved spec (meta title, meta description, H1, H2/H3, body copy). Plus a site-wide factual consistency scan and a re-check of items outstanding from the 2026-06-30 audit.

---

## Headline

**`/earc-solar-skin/` is fixed — the content is now live.** Facts are consistent site-wide with no contradictions found. Desktop and mobile serve identical content on all 42 pages. Three real defects remain, one of which is site-wide and high priority.

---

## 1. `/earc-solar-skin/` — ✅ FIXED

| Element | Required | Live | Status |
|---|---|---|---|
| Meta Title | "Lightweight Solar Panels for Commercial Roofs \| eARC by Sunman \| Energus Pty Ltd" | Exact match | ✅ |
| Meta Description | Glassless / non-penetrating copy | Exact match | ✅ |
| H1 count | 1 | 1 ("INTRODUCING eARC") — was **4** | ✅ |
| 6 × H3 sections | Older commercial buildings, Heritage-listed, Curved roofs, Membrane roofs, Insulated metal deck, Facades | All 6 present | ✅ |
| H2 sections | 2 | Both present | ✅ |
| Body copy | 7 blocks | All 7 present | ✅ |

The only nit: the H2 renders as "How it differs from conventional glass panels" without the trailing colon in the doc. Immaterial.

---

## 2. Also fixed since 30 June

- **`/commercial-battery-storage-melbourne/` title spacing** — now correctly "Commercial Battery Storage Melbourne | Energus Pty Ltd". (Note: the *approved doc itself* contains the typo "|Energus" — the live site is correct and the doc is wrong.)
- **10-year workmanship warranty** — corrected site-wide. **Zero** pages now claim 10 years; all say 5-year. This was the M2 item.
- **`/commercial-solar/` multiple H1s** — now a single H1. Was 4.
- **`/commercial-battery-storage/` H3 "National Footprint, Local Expertise"** — now present.
- **`/industrial_solar_energy/` noindex** — now `noindex,follow`. Was `noodp` only.

---

## 3. Deployment status across all 42 approved pages

| Check | Result |
|---|---|
| Pages live (HTTP 200) | **42 / 42** ✅ |
| Meta title matches approved | **42 / 42** ✅ |
| Meta description matches approved | **42 / 42** ✅ (but see defect A) |
| H1 matches approved | **42 / 42** ✅ (single H1 on every page) |
| Body copy fully deployed | 36 / 42 |
| **Desktop vs mobile identical** | **42 / 42** ✅ — same title, same H1, same body on every page. No mobile parity issue. |

---

## DEFECT A — Duplicate `<title>` and meta description tags on all 42 pages 🔴 HIGH

Every page outputs **two `<title>` tags and two-to-three `<meta name="description">` tags.** The first description in the `<head>` is a hardcoded theme default:

```html
<meta name="description" content="Commercial Solar Installations">   <-- theme default, FIRST
...
<meta name="description" content="Energus delivers commercial solar installation in Sydney..."/>   <-- correct, SECOND
```

The approved descriptions **are** on the page, but they are preceded by a generic one. Google is free to pick either, and a duplicate-tag conflict routinely means the approved description never gets used. This silently undermines all 42 meta descriptions we wrote.

Same for titles — `/industrial-solar-sydney/` serves **three** `<title>` tags.

**Fix:** the theme is emitting its own title/description block in addition to the SEO plugin's. The theme's block must be removed. This is a single template-level fix, not 42 page edits.

---

## DEFECT B — Industrial solar pages: headings pasted as plain text 🟠 MEDIUM

On all five `/industrial-solar-*/` pages, the approved H2 headings were pasted as **ordinary paragraph text instead of being marked up as headings.** The copy is on the page; the heading structure is not.

| Page | H2s that should be headings but are body text |
|---|---|
| industrial-solar-sydney | Solar for Manufacturing Sydney…, End-to-End Industrial Solar Delivery Across Sydney, Proven Industrial Solar Experience Across Australia, Why Choose Energus Pty Ltd |
| industrial-solar-melbourne | Industrial Solar in Melbourne for Business Growth…, Why Choose Energus Pty Ltd, Power Your Melbourne Operations…, Solar for Manufacturing Melbourne |
| industrial-solar-brisbane | End-to-End Solar Delivery for Brisbane Industrial Sites, Why Choose Energus Pty Ltd, Get a Free Quote for Industrial Solar in Brisbane |
| industrial-solar-adelaide | Solar for Manufacturing Adelaide…, End-to-End Industrial Solar Project Delivery in Adelaide, Why Choose Energus Pty Ltd |
| industrial-solar-gold-coast | Industrial Solar Services for Gold Coast Businesses, End-to-End Project Delivery…, Proven Experience Across Australia's Biggest Projects, Why Choose Energus Pty Ltd |

**Fix:** wrap each of these in `<h2>`.

---

## DEFECT C — Missing body copy and headings 🟠 MEDIUM

**Body copy never deployed:**

| Page | Missing |
|---|---|
| industrial-solar-gold-coast | The **entire 5-point "Why Choose Energus" list** (in-house engineering team, exclusive Tier 1 components, all-inclusive end-to-end service, ISO-certified systems, 1,800+ quotations) |
| industrial-solar-sydney | Both case studies — **Tip Top Bakery Chullora (2,018kW)** and **Sydney Art Gallery Extension (300kW)** |
| industrial-solar-brisbane | Closing contact CTA paragraph (1300 090 187 / sales@energus.com) |
| commercial-battery-storage-melbourne | Closing contact CTA paragraph |

**Headings never deployed:**

| Page | Missing heading |
|---|---|
| commercial-battery-storage-sydney | "Frequently Asked Questions About Commercial Battery Storage" |
| commercial-battery-storage-adelaide | "FAQs About Commercial Battery Storage in Adelaide" |
| commercial-battery-storage-brisbane | "Commercial Battery Storage for Brisbane Businesses: Why Choose Energus Pty Ltd" |

---

## DEFECT D — Homepage FAQ block ⚠️ NEEDS A DECISION, NOT A FIX

The approved doc specifies **8 FAQs on the homepage**, all about lightweight/eARC panels ("Why are some commercial roofs unsuitable for standard solar?", "How does eARC technology work?", etc.). **None of these are live.**

The homepage *does* have an FAQ section, but with a completely different set of questions (track record, NETCC certification, ISO standards, Top 5 National Installer in 40–100kW). That live set is arguably a better fit for a homepage than eight eARC questions.

**This needs a call, not a dev ticket:** either the dev ignored our FAQ block, or a different FAQ was approved elsewhere. The live FAQ introduces claims not in our doc — "SunWiz Top Solar Company Award Winner 2025", "NETCC Approved Seller", "Top 5 National Installer in the 40 to 100kW category (2023 and 2024)" — which should be confirmed as accurate with the client.

---

## 4. Factual consistency — ✅ CLEAN

Scanned all 42 live pages for every quantitative claim. **No contradictions found.**

| Claim | Live value | Pages | Consistent? |
|---|---|---|---|
| Average ROI | 22.5% | 37 | ✅ |
| Solar delivered | 100MW | all mentions | ✅ (no stale "55MW" anywhere) |
| Market position | Top 3 C&I solar retailer | 38 | ✅ |
| Quotations completed | 1,800+ | 37 | ✅ (minor: 20 pages omit the "+") |
| Workmanship warranty | **5-year** | site-wide | ✅ (zero "10-year" remaining) |
| Certifications | ISO 9001:2016 + ISO 45001:2018 | site-wide | ✅ |
| Phone | 1300 090 187 | 20 | ✅ |
| Email | sales@energus.com | site-wide | ✅ matches live site |

---

## 5. Still outstanding from the 30 June audit (outside the 42 content pages)

| Item | Status |
|---|---|
| 2b — `/aboutus` → `/about-us/` rename + 301 | ❌ **NOT DONE.** `/aboutus/` still 200s, `/about-us/` still 404s |
| 2a — `/locations/nsw/page/N/` canonicals → `/locations/nsw/` | ❌ **NOT DONE.** Still self-referencing |
| 2g — Multiple H1s on remaining pages | ❌ `/service-centre/` = **8 H1s**, `/landlords-property-groups/` = **12 H1s**, `/finance/` = **5 H1s** |
| robots meta = `noodp` on all 42 pages | ⚠️ Obsolete directive, harmless, but should be removed |

---

## Priority order for the developer

1. **Defect A** — remove the theme's duplicate title/description block (site-wide, one fix, protects all 42 meta descriptions).
2. **Defect C** — deploy the missing body copy, especially the whole "Why Choose Energus" list on `/industrial-solar-gold-coast/`.
3. **Defect B** — mark up the industrial-solar H2s as headings.
4. **2g** — template fix for CTA/section headings incorrectly tagged as H1 on `/service-centre/`, `/landlords-property-groups/`, `/finance/`.
5. **2b / 2a** — the about-us rename and the pagination canonicals.
