# STYLD Melbourne — Live Heading Audit
**Date:** 2026-06-22
**Auditor:** Claude (automated Playwright audit)
**Base URL:** https://www.styldmelbourne.com.au

---

## Summary Table

| # | Page | Status | H1 | Missing H2s | Notes |
|---|------|--------|----|-------------|-------|
| 1 | /home-staging/ | PARTIAL | ✓ | FAQ H2 rendered as H1 | "Thoughtful Home Styling in Melbourne" is H2 (should be H3) |
| 2 | /property-styling/ | PARTIAL | ✓ | FAQ H2 rendered as H1 | "Our Property Styling Process" is H3 ✓ |
| 3 | /furniture-staging/ | PASS | ✓ | None | All H2s and FAQ present correctly |
| 4 | /real-estate-staging/ | PASS | ✓ | None | All 6 H2s including "Get Your Melbourne Property Market-Ready" present ✓ |
| 5 | /home-staging-cost/ | PASS | ✓ | None | All 5 H2s present correctly |
| 6 | /full-property-styling/ | PARTIAL | ✓ | "Styling Packages for Every Property and Budget" rendered as H3 | "Our Property Styling Services" is H3 ✓; "How We Work" is H2 but approved as H3 |
| 7 | /partial-property-styling/ | PASS | ✓ | None | All 6 H2s present correctly |
| 8 | /luxury-property-styling/ | PARTIAL | ✓ | None | "Our Luxury Styling Process" is H2 (should be H3); "Curated Concepts for Prestige Properties" is H3 ✓ |
| 9 | /home-staging-prahran/ | PARTIAL | ✓ | FAQ H2 rendered as H1 | "Bringing Life to Local Apartments" is H3 ✓ |
| 10 | /home-staging-south-yarra/ | PASS | ✓ | None | All H2s present; "A Full-Service Solution for Time-Poor Vendors" is H3 ✓ |
| 11 | /home-staging-st-kilda/ | PARTIAL | ✓ | FAQ H2 rendered as H1 | "Cutting Through Apartment Market Saturation" is H2 (should be H3); H3s ✓ |
| 12 | /home-staging-richmond/ | PARTIAL | ✓ | FAQ H2 rendered as H1 | All 4 approved H2s present; all 3 approved H3s present ✓ |
| 13 | /home-staging-middle-park/ | PARTIAL | ✓ | FAQ H2 rendered as H1 | All other H2s present correctly |
| 14 | /home-staging-port-melbourne/ | PARTIAL | ✓ | FAQ H2 rendered as H1 | All other H2s present correctly |
| 15 | /home-staging-south-melbourne/ | PARTIAL | ✓ | FAQ H2 rendered as H1 | All other H2s present correctly |
| 16 | /home-staging-albert-park/ | PASS | ✓ | None | All H2s correct; "Styling Solutions for Every Property and Strategy" is H3 ✓ |
| 17 | /home-staging-windsor/ | PARTIAL | ✓ | FAQ H2 rendered as H1 | All other H2s present; "Differentiating Your Apartment..." is H3 ✓ |
| 18 | /home-staging-caulfield/ | PARTIAL | ✓ | "Home Styling Packages in Caulfield" rendered as H3 (should be H2) | FAQ H2 present ✓ |
| 19 | /home-staging-brighton/ | PARTIAL | ✓ | FAQ H2 rendered as H1 | All other H2s present correctly |
| 20 | /home-staging-northcote/ | PASS | ✓ | None | All H2s present correctly; FAQ is H2 ✓ |
| 21 | /areas-we-serve/ | PARTIAL | ✓ | FAQ H2 rendered as H1 | "Three Package Tiers for Every Property" is H3 ✓ |

**Overall: 6 pass / 15 partial / 0 fail out of 21 pages**

Pass: pages 3, 4, 5, 7, 10, 16, 20
Partial: pages 1, 2, 6, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 21

---

## Page-by-Page Findings

### Page 1: /home-staging/
**Status:** PARTIAL
**Live H1:** Home Staging Melbourne
**Live H2s:**
- Home Styling Melbourne Tailored to Your Property
- Thoughtful Home Styling in Melbourne ← **WRONG LEVEL** (should be H3)
- Property Styling Packages for Melbourne Homes
- Why Choose STYLD for Home Staging in Melbourne?

**Live H3s (FAQ accordion):**
- What is home staging?
- Do you offer both full and partial property styling?
- Can you style occupied homes?
- What areas of the property can you style?
- How long does the styling stay in place?
- Can the styling concept be adjusted?
- Does home staging really have an impact on sale price?
- How do I get started?

**Issues:**
1. "FAQs About Home Staging in Melbourne" is rendered as **H1** (level=1) — should be H2. This is a critical heading level error; the page now has two H1 tags.
2. "Thoughtful Home Styling in Melbourne" is rendered as **H2** — should be H3 per the approved spec.

---

### Page 2: /property-styling/
**Status:** PARTIAL
**Live H1:** Property Staging Melbourne
**Live H2s:**
- Pre-Sale Property Styling for Melbourne Homes
- Styling Packages for Every Melbourne Property
- Why Clients Turn to Us for Property Staging in Melbourne

**Live H3s:**
- Our Property Styling Process ✓ (approved H3)
- (FAQ questions as H3 inside accordion buttons)

**Issues:**
1. "FAQs About Property Staging Melbourne" is rendered as **H1** (level=1) — should be H2. Page now has two H1 tags.

---

### Page 3: /furniture-staging/
**Status:** PASS
**Live H1:** Furniture Staging Melbourne
**Live H2s:**
- Furniture Styling Melbourne Tailored to Every Property
- Furniture Staging Packages for Melbourne Homes
- Why We're the Go-to Source for Property Styling in Melbourne
- FAQs About Furniture Staging in Melbourne ✓

**Live H3s:** None approved; FAQ questions inside accordion are H3 (correct).

**Issues:** None.

---

### Page 4: /real-estate-staging/
**Status:** PASS
**Live H1:** Real Estate Styling Melbourne
**Live H2s:**
- Tailored Real Estate Staging Melbourne Vendors Trust
- A Considered Real Estate Stylist Melbourne Process
- Property Styling Packages for Every Melbourne Home
- Why Choose STYLD MELBOURNE for Real Estate Styling
- FAQs About Real Estate Styling in Melbourne
- Get Your Melbourne Property Market-Ready ✓

**Live H3s:** None approved; FAQ questions inside accordion are H3 (correct).

**Issues:** None.

---

### Page 5: /home-staging-cost/
**Status:** PASS
**Live H1:** Home Staging Cost Melbourne
**Live H2s:**
- Property Styling Packages for Melbourne Vendors
- What Influences Home Staging Cost in Melbourne
- The STYLD Melbourne Difference
- Get a Tailored Home Staging Quote in Melbourne
- FAQs About Home Staging Cost in Melbourne ✓

**Live H3s:** None approved; FAQ questions inside accordion are H3 (correct).

**Issues:** None.

---

### Page 6: /full-property-styling/
**Status:** PARTIAL
**Live H1:** Full Property Styling Melbourne
**Live H2s:**
- Comprehensive Home Staging Tailored to Every Melbourne Property
- How We Work ← **WRONG LEVEL** (approved as H3)
- Why Clients Choose Us for Full Property Styling in Melbourne
- FAQs About Full Property Styling in Melbourne ✓

**Live H3s:**
- Our Property Styling Services ✓ (approved H3)
- Styling Packages for Every Property and Budget ← **WRONG LEVEL** (approved as H2, rendered as H3)

**Issues:**
1. "Styling Packages for Every Property and Budget" is rendered as **H3** — should be H2 per the approved spec.
2. "How We Work" is rendered as **H2** — should be H3 per the approved spec.
3. These two headings have been swapped in heading level.

---

### Page 7: /partial-property-styling/
**Status:** PASS
**Live H1:** Partial Property Styling Melbourne
**Live H2s:**
- Tailored Partial Home Styling Across Melbourne
- A Seamless Styling Process From Walkthrough to Install
- Packages to Suit Every Property and Every Budget
- Why STYLD is the Go-to Team for Partial Property Styling in Melbourne
- Book Your Partial Property Styling Consultation
- FAQs About Partial Property Styling in Melbourne ✓

**Live H3s:** None approved; FAQ questions inside accordion are H3 (correct).

**Issues:** None.

---

### Page 8: /luxury-property-styling/
**Status:** PARTIAL
**Live H1:** Luxury Property Styling Melbourne
**Live H2s:**
- High-End Property Styling Tailored to Your Home
- Our Luxury Styling Process ← **WRONG LEVEL** (should be H3)
- Styling Packages Designed for Every Property Type
- Why Choose Us for Luxury Property Styling in Melbourne
- FAQs About Luxury Property Styling in Melbourne ✓

**Live H3s:**
- Curated Concepts for Prestige Properties ✓ (approved H3)

**Issues:**
1. "Our Luxury Styling Process" is rendered as **H2** — should be H3 per the approved spec. This is a heading level swap (mirroring the same error pattern seen on page 6).

---

### Page 9: /home-staging-prahran/
**Status:** PARTIAL
**Live H1:** Home Staging Prahran
**Live H2s:**
- A Seamless End-to-End Styling Process
- Styling Packages Tailored to Your Sale Strategy
- Why Choose STYLD for Home Staging in Prahran?

**Live H3s:**
- Bringing Life to Local Apartments ✓ (approved H3)

**Issues:**
1. "Frequently Asked Questions" is rendered as **H1** (level=1) — should be H2. Page now has two H1 tags.

---

### Page 10: /home-staging-south-yarra/
**Status:** PASS
**Live H1:** Home Staging South Yarra
**Live H2s:**
- Property Styling Built for South Yarra's Discerning Buyers
- Your Local Home Staging South Yarra Experts
- Why Choose STYLD for Home Styling in South Yarra?
- Frequently Asked Questions About Home Staging South Yarra ✓

**Live H3s:**
- A Full-Service Solution for Time-Poor Vendors ✓ (approved H3)

**Issues:** None.

---

### Page 11: /home-staging-st-kilda/
**Status:** PARTIAL
**Live H1:** Home Staging St Kilda
**Live H2s:**
- Cutting Through Apartment Market Saturation ← **WRONG LEVEL** (should be H3)
- Why Choose STYLD for Home Styling in St Kilda

**Live H3s:**
- Making Compact and Challenging Floor Plans Feel Generous ✓ (approved H3)
- Honouring Character Without Looking Dated ✓ (approved H3)

**Issues:**
1. "Frequently Asked Questions" is rendered as **H1** (level=1) — should be H2. Page now has two H1 tags.
2. "Cutting Through Apartment Market Saturation" is rendered as **H2** — should be H3 per the approved spec.

---

### Page 12: /home-staging-richmond/
**Status:** PARTIAL
**Live H1:** Home Staging Richmond
**Live H2s:**
- Home Staging for Richmond Properties of Various Different Styles
- Home Styling Packages in Richmond
- Why Choose STYLD for Home Staging in Richmond?

**Live H3s:**
- Bespoke Styling for Heritage Terraces ✓ (approved H3)
- Smart Styling for Modern Apartments ✓ (approved H3)
- End-to-End Management for Time-Poor Vendors ✓ (approved H3)

**Issues:**
1. "Frequently Asked Questions" is rendered as **H1** (level=1) — should be H2. Page now has two H1 tags.

---

### Page 13: /home-staging-middle-park/
**Status:** PARTIAL
**Live H1:** Home Staging Middle Park
**Live H2s:**
- A Considered Property Staging Process
- Local Home Staging in Middle Park
- Why Choose STYLD for Home Styling in Middle Park?

**Live H3s:** None (no H3s approved).

**Issues:**
1. "Frequently Asked Questions" is rendered as **H1** (level=1) — should be H2. Page now has two H1 tags.

---

### Page 14: /home-staging-port-melbourne/
**Status:** PARTIAL
**Live H1:** Home Staging Port Melbourne
**Live H2s:**
- Property Styling Tailored to the Port Melbourne Market
- Local Property Styling Services in Port Melbourne
- Why Choose STYLD for Home Styling in Port Melbourne?

**Live H3s:** None (no H3s approved).

**Issues:**
1. "Frequently Asked Questions" is rendered as **H1** (level=1) — should be H2. Page now has two H1 tags.

---

### Page 15: /home-staging-south-melbourne/
**Status:** PARTIAL
**Live H1:** Home Staging South Melbourne
**Live H2s:**
- Tailored Home Styling in South Melbourne for Every Property Type
- A Seamless Property Staging Process, Managed End-to-End
- Why Choose STYLD for Property Staging in South Melbourne?

**Live H3s:** None (no H3s approved).

**Issues:**
1. "Frequently Asked Questions" is rendered as **H1** (level=1) — should be H2. Page now has two H1 tags.

---

### Page 16: /home-staging-albert-park/
**Status:** PASS
**Live H1:** Home Staging Albert Park
**Live H2s:**
- Property Styling Tailored to Albert Park's Architecture
- Local Home Staging Experts Across Albert Park
- Why Choose STYLD for Home Staging in Albert Park?
- Frequently Asked Questions About Home Staging in Albert Park ✓

**Live H3s:**
- Styling Solutions for Every Property and Strategy ✓ (approved H3)

**Issues:** None.

---

### Page 17: /home-staging-windsor/
**Status:** PARTIAL
**Live H1:** Home Staging Windsor
**Live H2s:**
- Property Staging That Stands Out
- Your Local Home Styling Windsor Specialists
- Why Choose STYLD for Property Staging in Windsor?

**Live H3s:**
- Differentiating Your Apartment in a High-Density Market ✓ (approved H3)

**Issues:**
1. "Frequently Asked Questions" is rendered as **H1** (level=1) — should be H2. Page now has two H1 tags.

---

### Page 18: /home-staging-caulfield/
**Status:** PARTIAL
**Live H1:** Home Staging Caulfield
**Live H2s:**
- Strategic Home Staging in Caulfield to Maximise Your Sale Price
- Why Choose STYLD for Home Staging in Caulfield?
- Frequently Asked Questions About Home Staging in Caulfield ✓

**Live H3s:**
- Home Styling Packages in Caulfield ← **WRONG LEVEL** (should be H2)

**Issues:**
1. "Home Styling Packages in Caulfield" is rendered as **H3** — should be H2 per the approved spec.

---

### Page 19: /home-staging-brighton/
**Status:** PARTIAL
**Live H1:** Home Staging Brighton
**Live H2s:**
- A Seamless End-to-End Property Styling Service
- Local Property Staging Services in Brighton
- Why Choose STYLD for Home Styling in Brighton?

**Live H3s:** None (no H3s approved).

**Issues:**
1. "FAQs About Home Staging in Brighton" is rendered as **H1** (level=1) — should be H2. Page now has two H1 tags.

---

### Page 20: /home-staging-northcote/
**Status:** PASS
**Live H1:** Home Staging Northcote
**Live H2s:**
- Property Styling Tailored to Northcote's Architectural Character
- Your Local Home Styling Experts in Northcote
- Why Choose STYLD for Home Staging in Northcote?
- Frequently Asked Questions About Home Staging in Northcote ✓

**Live H3s:** None (no H3s approved).

**Issues:** None.

---

### Page 21: /areas-we-serve/
**Status:** PARTIAL
**Live H1:** Home Staging Near Me in Melbourne
**Live H2s:**
- Tailored Home Styling Near Me Across Melbourne
- Why Choose STYLD for Home Staging in Melbourne?

**Live H3s:**
- Three Package Tiers for Every Property ✓ (approved H3)

**Issues:**
1. "Frequently Asked Questions" is rendered as **H1** (level=1) — should be H2. Page now has two H1 tags.

---

## Issue Registry

### Issue Type A — FAQ heading rendered as H1 instead of H2
Affects **12 pages**: 1, 2, 9, 11, 12, 13, 14, 15, 17, 19, 21, and (Brighton = page 19).

Full affected page list:
- /home-staging/ — "FAQs About Home Staging in Melbourne" → H1
- /property-styling/ — "FAQs About Property Staging Melbourne" → H1
- /home-staging-prahran/ — "Frequently Asked Questions" → H1
- /home-staging-st-kilda/ — "Frequently Asked Questions" → H1
- /home-staging-richmond/ — "Frequently Asked Questions" → H1
- /home-staging-middle-park/ — "Frequently Asked Questions" → H1
- /home-staging-port-melbourne/ — "Frequently Asked Questions" → H1
- /home-staging-south-melbourne/ — "Frequently Asked Questions" → H1
- /home-staging-windsor/ — "Frequently Asked Questions" → H1
- /home-staging-brighton/ — "FAQs About Home Staging in Brighton" → H1
- /home-staging-northcote/ — FIXED ✓ (H2, correct)
- /areas-we-serve/ — "Frequently Asked Questions" → H1

Pages with FAQ H2 **fixed** (correct H2 level): 3, 4, 5, 6, 7, 8, 10, 16, 20 — 9 pages.

### Issue Type B — Heading level swap (H2/H3 inverted)
- /home-staging/ (page 1): "Thoughtful Home Styling in Melbourne" is H2, should be H3
- /full-property-styling/ (page 6): "How We Work" is H2 (should be H3); "Styling Packages for Every Property and Budget" is H3 (should be H2)
- /luxury-property-styling/ (page 8): "Our Luxury Styling Process" is H2 (should be H3)
- /home-staging-st-kilda/ (page 11): "Cutting Through Apartment Market Saturation" is H2 (should be H3)
- /home-staging-caulfield/ (page 18): "Home Styling Packages in Caulfield" is H3 (should be H2)

---

## Overall Verdict

**Six pages now pass completely** (/furniture-staging/, /real-estate-staging/, /home-staging-cost/, /partial-property-styling/, /home-staging-south-yarra/, /home-staging-albert-park/, /home-staging-northcote/) — this represents meaningful progress from the Jun 19 audit, particularly on the FAQ H2 fix for those seven pages. /home-staging-northcote/ is a notable win, confirming the FAQ heading fix was deployed correctly there.

**The dominant remaining issue is the FAQ accordion heading being rendered as H1 instead of H2 on 12 pages.** This is almost certainly a CMS template-level bug rather than a page-by-page content error — the same FAQ section block is outputting the section heading at the wrong level across the majority of suburb and some service pages. Pages that have it fixed (Northcote, Albert Park, South Yarra, the four service pages without this issue) appear to have been individually corrected or use a different block variant. The developer should audit which block/component is rendering the FAQ heading and ensure it outputs `<h2>` universally, then bulk-apply to the 12 remaining affected pages.

**Heading level swaps on five pages** are the secondary concern. Pages 6 (/full-property-styling/) and 8 (/luxury-property-styling/) both have H3-designated headings promoted to H2, and page 11 (/home-staging-st-kilda/) and page 1 (/home-staging/) have similar inversions. Page 18 (/home-staging-caulfield/) has an approved H2 demoted to H3. These are individual page errors that require targeted fixes rather than a systemic template change. The pattern suggests these headings may have been manually styled in the CMS editor at the wrong level.
