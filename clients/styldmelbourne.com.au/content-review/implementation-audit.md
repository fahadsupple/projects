# STYLD Melbourne — Content Implementation Audit
**Audit Date:** 2026-06-19  
**Auditor:** Claude Code  
**Scope:** 21 pages audited against client-approved content (meta title, H1, H2s, H3s)  
**Method:** Live Playwright browser extraction — all pages visited in sequence

---

## Key to Status Codes
- PASS — all approved headings present, no structural issues
- PARTIAL — approved content present but either (a) an approved H2/H3 is missing, or (b) approved headings have been demoted/promoted to a different level
- FAIL — H1 wrong, meta title wrong, or multiple critical issues

---

## PAGE-BY-PAGE BREAKDOWN

---

### PAGE 1: /home-staging/
**URL:** https://www.styldmelbourne.com.au/home-staging/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Melbourne \| STYLD MELBOURNE | Home Staging Melbourne \| STYLD MELBOURNE |
| H1 | Home Staging Melbourne | Home Staging Melbourne |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Home Styling Melbourne Tailored to Your Property | Home Styling Melbourne Tailored to Your Property | PASS |
| 2 | Property Styling Packages for Melbourne Homes | Thoughtful Home Styling in Melbourne | FAIL — approved H2 moved; "Thoughtful Home Styling in Melbourne" appears as H2 on live but is approved as an H3 |
| 3 | Why Choose STYLD for Home Staging in Melbourne? | Property Styling Packages for Melbourne Homes | FAIL — wrong position |
| 4 | FAQs About Home Staging in Melbourne | Why Choose STYLD for Home Staging in Melbourne? | FAIL — wrong position |

**Issues:**
- "Thoughtful Home Styling in Melbourne" is approved as an **H3** but is rendered as an **H2** on the live page (heading level demotion/promotion error)
- "FAQs About Home Staging in Melbourne" (approved H2) is **missing** from the live page — the FAQ section uses H3s for individual questions instead of an H2 section header
- H2 order on live: [H2-1, H3-promoted-to-H2, H2-3, H2-4] — missing FAQs H2

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| Thoughtful Home Styling in Melbourne | NOT present as H3 (promoted to H2) | FAIL |

**Extra headings on live (not in approved):**
- H3s: "What is home staging?", "Do you offer both full and partial property styling?", "Can you style occupied homes?", "What areas of the property can you style?", "How long does the styling stay in place?", "Can the styling concept be adjusted?", "Does home staging really have an impact on sale price?", "How do I get started?" — these are FAQ question H3s; acceptable as FAQ implementation detail but "FAQs About Home Staging in Melbourne" H2 header is missing

---

### PAGE 2: /property-styling/
**URL:** https://www.styldmelbourne.com.au/property-styling/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Property Staging Melbourne \| STYLD MELBOURNE | Property Staging Melbourne \| STYLD MELBOURNE |
| H1 | Property Staging Melbourne | Property Staging Melbourne |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Pre-Sale Property Styling for Melbourne Homes | Pre-Sale Property Styling for Melbourne Homes | PASS |
| 2 | Styling Packages for Every Melbourne Property | Styling Packages for Every Melbourne Property | PASS |
| 3 | Why Clients Turn to Us for Property Staging in Melbourne | Why Clients Turn to Us for Property Staging in Melbourne | PASS |
| 4 | FAQs About Property Staging Melbourne | MISSING | FAIL |

**Issues:**
- "FAQs About Property Staging Melbourne" (approved H2) is **missing** — no FAQ section H2 wrapper present; FAQ questions are under "Our Property Styling Process" H3 which itself is incorrectly rendered
- "Our Property Styling Process" is approved as an **H3** but is rendered as an **H3** — correct level, but it appears inside the H2 flow before the FAQ H2, suggesting the FAQ H2 was never added

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| Our Property Styling Process | Our Property Styling Process (as H3) | PASS |

---

### PAGE 3: /furniture-staging/
**URL:** https://www.styldmelbourne.com.au/furniture-staging/  
**Status: PASS**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Furniture Staging Melbourne \| STYLD MELBOURNE | Furniture Staging Melbourne \| STYLD MELBOURNE |
| H1 | Furniture Staging Melbourne | Furniture Staging Melbourne |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Furniture Styling Melbourne Tailored to Every Property | Furniture Styling Melbourne Tailored to Every Property | PASS |
| 2 | Furniture Staging Packages for Melbourne Homes | Furniture Staging Packages for Melbourne Homes | PASS |
| 3 | Why We're the Go-to Source for Property Styling in Melbourne | Why We're the Go-to Source for Property Styling in Melbourne | PASS |
| 4 | FAQs About Furniture Staging in Melbourne | FAQs About Furniture Staging in Melbourne | PASS |

**H3s:** Approved = none. Live has FAQ question H3s (acceptable). No structural issues.

---

### PAGE 4: /real-estate-staging/
**URL:** https://www.styldmelbourne.com.au/real-estate-staging/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Real Estate Styling Melbourne \| STYLD MELBOURNE | Real Estate Styling Melbourne \| STYLD MELBOURNE |
| H1 | Real Estate Styling Melbourne | Real Estate Styling Melbourne |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Tailored Real Estate Staging Melbourne Vendors Trust | Tailored Real Estate Staging Melbourne Vendors Trust | PASS |
| 2 | A Considered Real Estate Stylist Melbourne Process | A Considered Real Estate Stylist Melbourne Process | PASS |
| 3 | Property Styling Packages for Every Melbourne Home | Property Styling Packages for Every Melbourne Home | PASS |
| 4 | Why Choose STYLD MELBOURNE for Real Estate Styling | Why Choose STYLD MELBOURNE for Real Estate Styling | PASS |
| 5 | FAQs About Real Estate Styling in Melbourne | FAQs About Real Estate Styling in Melbourne | PASS |
| 6 | Get Your Melbourne Property Market-Ready | MISSING | FAIL |

**Issues:**
- "Get Your Melbourne Property Market-Ready" (approved 6th H2) is **missing** from the live page

**H3s:** Approved = none. Live has FAQ question H3s (acceptable).

---

### PAGE 5: /home-staging-cost/
**URL:** https://www.styldmelbourne.com.au/home-staging-cost/  
**Status: PASS**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Cost Melbourne \| STYLD MELBOURNE | Home Staging Cost Melbourne \| STYLD MELBOURNE |
| H1 | Home Staging Cost Melbourne | Home Staging Cost Melbourne |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Property Styling Packages for Melbourne Vendors | Property Styling Packages for Melbourne Vendors | PASS |
| 2 | What Influences Home Staging Cost in Melbourne | What Influences Home Staging Cost in Melbourne | PASS |
| 3 | The STYLD Melbourne Difference | The STYLD Melbourne Difference | PASS |
| 4 | Get a Tailored Home Staging Quote in Melbourne | Get a Tailored Home Staging Quote in Melbourne | PASS |
| 5 | FAQs About Home Staging Cost in Melbourne | FAQs About Home Staging Cost in Melbourne | PASS |

**H3s:** Approved = none. Live has FAQ question H3s (acceptable).

---

### PAGE 6: /full-property-styling/
**URL:** https://www.styldmelbourne.com.au/full-property-styling/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Full Property Styling Melbourne \| STYLD MELBOURNE | Full Property Styling Melbourne \| STYLD MELBOURNE |
| H1 | Full Property Styling Melbourne | Full Property Styling Melbourne |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Comprehensive Home Staging Tailored to Every Melbourne Property | Comprehensive Home Staging Tailored to Every Melbourne Property | PASS |
| 2 | Styling Packages for Every Property and Budget | How We Work | FAIL — approved H2 demoted to H3 on live |
| 3 | Why Clients Choose Us for Full Property Styling in Melbourne | Why Clients Choose Us for Full Property Styling in Melbourne | PASS |
| 4 | FAQs About Full Property Styling in Melbourne | FAQs About Full Property Styling in Melbourne | PASS |

**Issues:**
- "Styling Packages for Every Property and Budget" is approved as an **H2** but on the live page it is rendered as an **H3** (heading level demotion)
- "How We Work" is approved as an **H3** but on the live page it is rendered as an **H2** (heading level promotion)
- These two headings have been swapped in level: "How We Work" became H2, "Styling Packages for Every Property and Budget" became H3

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| Our Property Styling Services | Our Property Styling Services (H3) | PASS |
| How We Work | How We Work — promoted to H2 on live | FAIL |

---

### PAGE 7: /partial-property-styling/
**URL:** https://www.styldmelbourne.com.au/partial-property-styling/  
**Status: PASS**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Partial Property Styling Melbourne \| STYLD MELBOURNE | Partial Property Styling Melbourne \| STYLD MELBOURNE |
| H1 | Partial Property Styling Melbourne | Partial Property Styling Melbourne |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Tailored Partial Home Styling Across Melbourne | Tailored Partial Home Styling Across Melbourne | PASS |
| 2 | A Seamless Styling Process From Walkthrough to Install | A Seamless Styling Process From Walkthrough to Install | PASS |
| 3 | Packages to Suit Every Property and Every Budget | Packages to Suit Every Property and Every Budget | PASS |
| 4 | Why STYLD is the Go-to Team for Partial Property Styling in Melbourne | Why STYLD is the Go-to Team for Partial Property Styling in Melbourne | PASS |
| 5 | Book Your Partial Property Styling Consultation | Book Your Partial Property Styling Consultation | PASS |
| 6 | FAQs About Partial Property Styling in Melbourne | FAQs About Partial Property Styling in Melbourne | PASS |

**H3s:** Approved = none. Live has FAQ question H3s (acceptable).

---

### PAGE 8: /luxury-property-styling/
**URL:** https://www.styldmelbourne.com.au/luxury-property-styling/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Luxury Property Styling Melbourne \| STYLD MELBOURNE | Luxury Property Styling Melbourne \| STYLD MELBOURNE |
| H1 | Luxury Property Styling Melbourne | Luxury Property Styling Melbourne |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | High-End Property Styling Tailored to Your Home | High-End Property Styling Tailored to Your Home | PASS |
| 2 | Styling Packages Designed for Every Property Type | Our Luxury Styling Process | FAIL — approved H2 demoted; approved H3 promoted |
| 3 | Why Choose Us for Luxury Property Styling in Melbourne | Styling Packages Designed for Every Property Type | FAIL — wrong position |
| 4 | FAQs About Luxury Property Styling in Melbourne | Why Choose Us for Luxury Property Styling in Melbourne | FAIL — wrong position |
| — | — | FAQs About Luxury Property Styling in Melbourne | PASS (present, in position 5) |

**Issues:**
- "Our Luxury Styling Process" is approved as an **H3** but rendered as **H2** on live (heading level promotion)
- "Curated Concepts for Prestige Properties" is approved as an **H3** and is present as H3 on live — PASS
- Order on live is: [H2-1, H2-"Our Luxury Styling Process" (should be H3), H2-2, H2-3, H2-4] — the H3 was promoted to H2 position 2

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| Curated Concepts for Prestige Properties | Curated Concepts for Prestige Properties (H3) | PASS |
| Our Luxury Styling Process | Our Luxury Styling Process — promoted to H2 on live | FAIL |

---

### PAGE 9: /home-staging-prahran/
**URL:** https://www.styldmelbourne.com.au/home-staging-prahran/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Prahran \| Property Styling Experts \| STYLD MELBOURNE | Home Staging Prahran \| Property Styling Experts \| STYLD MELBOURNE |
| H1 | Home Staging Prahran | Home Staging Prahran |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | A Seamless End-to-End Styling Process | A Seamless End-to-End Styling Process | PASS |
| 2 | Styling Packages Tailored to Your Sale Strategy | Styling Packages Tailored to Your Sale Strategy | PASS |
| 3 | Why Choose STYLD for Home Staging in Prahran? | Why Choose STYLD for Home Staging in Prahran? | PASS |
| 4 | Frequently Asked Questions | MISSING | FAIL |

**Issues:**
- "Frequently Asked Questions" (approved H2) is **missing** from the live page — FAQ questions exist as H3s but the section header H2 is absent

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| Bringing Life to Local Apartments | Bringing Life to Local Apartments (H3) | PASS |

---

### PAGE 10: /home-staging-south-yarra/
**URL:** https://www.styldmelbourne.com.au/home-staging-south-yarra/  
**Status: PASS**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging South Yarra \| Property Styling \| STYLD MELBOURNE | Home Staging South Yarra \| Property Styling \| STYLD MELBOURNE |
| H1 | Home Staging South Yarra | Home Staging South Yarra |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Property Styling Built for South Yarra's Discerning Buyers | Property Styling Built for South Yarra's Discerning Buyers | PASS |
| 2 | Your Local Home Staging South Yarra Experts | Your Local Home Staging South Yarra Experts | PASS |
| 3 | Why Choose STYLD for Home Styling in South Yarra? | Why Choose STYLD for Home Styling in South Yarra? | PASS |
| 4 | Frequently Asked Questions About Home Staging South Yarra | Frequently Asked Questions About Home Staging South Yarra | PASS |

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| A Full-Service Solution for Time-Poor Vendors | A Full-Service Solution for Time-Poor Vendors (H3) | PASS |

---

### PAGE 11: /home-staging-st-kilda/
**URL:** https://www.styldmelbourne.com.au/home-staging-st-kilda/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging St Kilda \| Property Styling \| STYLD MELBOURNE | Home Staging St Kilda \| Property Styling \| STYLD MELBOURNE |
| H1 | Home Staging St Kilda | Home Staging St Kilda |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Why Choose STYLD for Home Styling in St Kilda | Cutting Through Apartment Market Saturation | FAIL — approved H2 missing; unexpected H2 present |
| 2 | Frequently Asked Questions | Why Choose STYLD for Home Styling in St Kilda | FAIL — wrong position |

**Issues:**
- "Cutting Through Apartment Market Saturation" appears as H2 on the live page but is **not in the approved H2 list** — it is approved as an **H3** (unexpected promotion to H2)
- "Frequently Asked Questions" (approved H2) is **missing** from the live page
- Approved H2 count: 2. Live H2 count: 2. But one is a different heading entirely (promoted from H3)

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| Cutting Through Apartment Market Saturation | Promoted to H2 on live — not present as H3 | FAIL |
| Making Compact and Challenging Floor Plans Feel Generous | Making Compact and Challenging Floor Plans Feel Generous (H3) | PASS |
| Honouring Character Without Looking Dated | Honouring Character Without Looking Dated (H3) | PASS |

---

### PAGE 12: /home-staging-richmond/
**URL:** https://www.styldmelbourne.com.au/home-staging-richmond/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Richmond \| Property Styling \| STYLD MELBOURNE | Home Staging Richmond \| Property Styling \| STYLD MELBOURNE |
| H1 | Home Staging Richmond | Home Staging Richmond |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Home Staging for Richmond Properties of Various Different Styles | Home Staging for Richmond Properties of Various Different Styles | PASS |
| 2 | Home Styling Packages in Richmond | Home Styling Packages in Richmond | PASS |
| 3 | Why Choose STYLD for Home Staging in Richmond? | Why Choose STYLD for Home Staging in Richmond? | PASS |
| 4 | Frequently Asked Questions | MISSING | FAIL |

**Issues:**
- "Frequently Asked Questions" (approved H2) is **missing** from the live page — FAQ questions exist as H3s but the section header H2 is absent

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| Bespoke Styling for Heritage Terraces | Bespoke Styling for Heritage Terraces (H3) | PASS |
| Smart Styling for Modern Apartments | Smart Styling for Modern Apartments (H3) | PASS |
| End-to-End Management for Time-Poor Vendors | End-to-End Management for Time-Poor Vendors (H3) | PASS |

---

### PAGE 13: /home-staging-middle-park/
**URL:** https://www.styldmelbourne.com.au/home-staging-middle-park/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Middle Park \| Property Styling \| STYLD MELBOURNE | Home Staging Middle Park \| Property Styling \| STYLD MELBOURNE |
| H1 | Home Staging Middle Park | Home Staging Middle Park |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | A Considered Property Staging Process | A Considered Property Staging Process | PASS |
| 2 | Local Home Staging in Middle Park | Local Home Staging in Middle Park | PASS |
| 3 | Why Choose STYLD for Home Styling in Middle Park? | Why Choose STYLD for Home Styling in Middle Park? | PASS |
| 4 | Frequently Asked Questions | MISSING | FAIL |

**Issues:**
- "Frequently Asked Questions" (approved H2) is **missing** from the live page

**H3s:** Approved = none. Live has FAQ question H3s (acceptable).

---

### PAGE 14: /home-staging-port-melbourne/
**URL:** https://www.styldmelbourne.com.au/home-staging-port-melbourne/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Port Melbourne \| Property Styling \| STYLD MELBOURNE | Home Staging Port Melbourne \| Property Styling \| STYLD MELBOURNE |
| H1 | Home Staging Port Melbourne | Home Staging Port Melbourne |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Property Styling Tailored to the Port Melbourne Market | Property Styling Tailored to the Port Melbourne Market | PASS |
| 2 | Local Property Styling Services in Port Melbourne | Local Property Styling Services in Port Melbourne | PASS |
| 3 | Why Choose STYLD for Home Styling in Port Melbourne? | Why Choose STYLD for Home Styling in Port Melbourne? | PASS |
| 4 | Frequently Asked Questions | MISSING | FAIL |

**Issues:**
- "Frequently Asked Questions" (approved H2) is **missing** from the live page

**H3s:** Approved = none. Live has FAQ question H3s (acceptable).

---

### PAGE 15: /home-staging-south-melbourne/
**URL:** https://www.styldmelbourne.com.au/home-staging-south-melbourne/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging South Melbourne \| STYLD MELBOURNE | Home Staging South Melbourne \| STYLD MELBOURNE |
| H1 | Home Staging South Melbourne | Home Staging South Melbourne |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Tailored Home Styling in South Melbourne for Every Property Type | Tailored Home Styling in South Melbourne for Every Property Type | PASS |
| 2 | A Seamless Property Staging Process, Managed End-to-End | A Seamless Property Staging Process, Managed End-to-End | PASS |
| 3 | Why Choose STYLD for Property Staging in South Melbourne? | Why Choose STYLD for Property Staging in South Melbourne? | PASS |
| 4 | Frequently Asked Questions | MISSING | FAIL |

**Issues:**
- "Frequently Asked Questions" (approved H2) is **missing** from the live page

**H3s:** Approved = none. Live has FAQ question H3s (acceptable).

---

### PAGE 16: /home-staging-albert-park/
**URL:** https://www.styldmelbourne.com.au/home-staging-albert-park/  
**Status: PASS**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Albert Park \| Property Styling \| STYLD MELBOURNE | Home Staging Albert Park \| Property Styling \| STYLD MELBOURNE |
| H1 | Home Staging Albert Park | Home Staging Albert Park |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Property Styling Tailored to Albert Park's Architecture | Property Styling Tailored to Albert Park's Architecture | PASS |
| 2 | Local Home Staging Experts Across Albert Park | Local Home Staging Experts Across Albert Park | PASS |
| 3 | Why Choose STYLD for Home Staging in Albert Park? | Why Choose STYLD for Home Staging in Albert Park? | PASS |
| 4 | Frequently Asked Questions About Home Staging in Albert Park | Frequently Asked Questions About Home Staging in Albert Park | PASS |

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| Styling Solutions for Every Property and Strategy | Styling Solutions for Every Property and Strategy (H3) | PASS |

---

### PAGE 17: /home-staging-windsor/
**URL:** https://www.styldmelbourne.com.au/home-staging-windsor/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Windsor \| STYLD MELBOURNE | Home Staging Windsor \| STYLD MELBOURNE |
| H1 | Home Staging Windsor | Home Staging Windsor |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Property Staging That Stands Out | Property Staging That Stands Out | PASS |
| 2 | Your Local Home Styling Windsor Specialists | Your Local Home Styling Windsor Specialists | PASS |
| 3 | Why Choose STYLD for Property Staging in Windsor? | Why Choose STYLD for Property Staging in Windsor? | PASS |
| 4 | Frequently Asked Questions | MISSING | FAIL |

**Issues:**
- "Frequently Asked Questions" (approved H2) is **missing** from the live page

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| Differentiating Your Apartment in a High-Density Market | Differentiating Your Apartment in a High-Density Market (H3) | PASS |

---

### PAGE 18: /home-staging-caulfield/
**URL:** https://www.styldmelbourne.com.au/home-staging-caulfield/  
**Status: PASS**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Caulfield \| Property Styling \| STYLD MELBOURNE | Home Staging Caulfield \| Property Styling \| STYLD MELBOURNE |
| H1 | Home Staging Caulfield | Home Staging Caulfield |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Strategic Home Staging in Caulfield to Maximise Your Sale Price | Strategic Home Staging in Caulfield to Maximise Your Sale Price | PASS |
| 2 | Why Choose STYLD for Home Staging in Caulfield? | Why Choose STYLD for Home Staging in Caulfield? | PASS |
| 3 | Frequently Asked Questions About Home Staging in Caulfield | Frequently Asked Questions About Home Staging in Caulfield | PASS |

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| Home Styling Packages in Caulfield | Home Styling Packages in Caulfield (H3) | PASS |

---

### PAGE 19: /home-staging-brighton/
**URL:** https://www.styldmelbourne.com.au/home-staging-brighton/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Brighton \| Premium Property Styling \| STYLD MELBOURNE | Home Staging Brighton \| Premium Property Styling \| STYLD MELBOURNE |
| H1 | Home Staging Brighton | Home Staging Brighton |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | A Seamless End-to-End Property Styling Service | A Seamless End-to-End Property Styling Service | PASS |
| 2 | Local Property Staging Services in Brighton | Local Property Staging Services in Brighton | PASS |
| 3 | Why Choose STYLD for Home Styling in Brighton? | Why Choose STYLD for Home Styling in Brighton? | PASS |
| 4 | FAQs About Home Staging in Brighton | MISSING | FAIL |

**Issues:**
- "FAQs About Home Staging in Brighton" (approved H2) is **missing** from the live page

**H3s:** Approved = none. Live has FAQ question H3s (acceptable).

---

### PAGE 20: /home-staging-northcote/
**URL:** https://www.styldmelbourne.com.au/home-staging-northcote/  
**Status: PASS**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Northcote \| STYLD MELBOURNE | Home Staging Northcote \| STYLD MELBOURNE |
| H1 | Home Staging Northcote | Home Staging Northcote |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Property Styling Tailored to Northcote's Architectural Character | Property Styling Tailored to Northcote's Architectural Character | PASS |
| 2 | Your Local Home Styling Experts in Northcote | Your Local Home Styling Experts in Northcote | PASS |
| 3 | Why Choose STYLD for Home Staging in Northcote? | Why Choose STYLD for Home Staging in Northcote? | PASS |
| 4 | Frequently Asked Questions About Home Staging in Northcote | Frequently Asked Questions About Home Staging in Northcote | PASS |

**H3s:** Approved = none. Live has FAQ question H3s (acceptable).

---

### PAGE 21: /areas-we-serve/
**URL:** https://www.styldmelbourne.com.au/areas-we-serve/  
**Status: PARTIAL**

| Field | Approved | Live |
|---|---|---|
| Meta Title | Home Staging Near Me Melbourne CBD & Inner City \| STYLD MELBOURNE | Home Staging Near Me Melbourne CBD & Inner City \| STYLD MELBOURNE |
| H1 | Home Staging Near Me in Melbourne | Home Staging Near Me in Melbourne |

**H2 comparison:**

| # | Approved H2 | Live H2 | Match? |
|---|---|---|---|
| 1 | Tailored Home Styling Near Me Across Melbourne | Tailored Home Styling Near Me Across Melbourne | PASS |
| 2 | Why Choose STYLD for Home Staging in Melbourne? | Why Choose STYLD for Home Staging in Melbourne? | PASS |
| 3 | Frequently Asked Questions | MISSING | FAIL |

**Issues:**
- "Frequently Asked Questions" (approved H2) is **missing** from the live page

**H3 comparison:**

| Approved H3 | Live | Match? |
|---|---|---|
| Three Package Tiers for Every Property | Three Package Tiers for Every Property (H3) | PASS |

---

## SUMMARY TABLE

| # | Page | URL | Status | Issues |
|---|---|---|---|---|
| 1 | Home Staging | /home-staging/ | PARTIAL | "Thoughtful Home Styling in Melbourne" promoted from H3 to H2; "FAQs About Home Staging in Melbourne" H2 missing |
| 2 | Property Styling | /property-styling/ | PARTIAL | "FAQs About Property Staging Melbourne" H2 missing |
| 3 | Furniture Staging | /furniture-staging/ | PASS | None |
| 4 | Real Estate Staging | /real-estate-staging/ | PARTIAL | "Get Your Melbourne Property Market-Ready" H2 missing |
| 5 | Home Staging Cost | /home-staging-cost/ | PASS | None |
| 6 | Full Property Styling | /full-property-styling/ | PARTIAL | "Styling Packages for Every Property and Budget" demoted from H2 to H3; "How We Work" promoted from H3 to H2 |
| 7 | Partial Property Styling | /partial-property-styling/ | PASS | None |
| 8 | Luxury Property Styling | /luxury-property-styling/ | PARTIAL | "Our Luxury Styling Process" promoted from H3 to H2 |
| 9 | Home Staging Prahran | /home-staging-prahran/ | PARTIAL | "Frequently Asked Questions" H2 missing |
| 10 | Home Staging South Yarra | /home-staging-south-yarra/ | PASS | None |
| 11 | Home Staging St Kilda | /home-staging-st-kilda/ | PARTIAL | "Cutting Through Apartment Market Saturation" promoted from H3 to H2; "Frequently Asked Questions" H2 missing |
| 12 | Home Staging Richmond | /home-staging-richmond/ | PARTIAL | "Frequently Asked Questions" H2 missing |
| 13 | Home Staging Middle Park | /home-staging-middle-park/ | PARTIAL | "Frequently Asked Questions" H2 missing |
| 14 | Home Staging Port Melbourne | /home-staging-port-melbourne/ | PARTIAL | "Frequently Asked Questions" H2 missing |
| 15 | Home Staging South Melbourne | /home-staging-south-melbourne/ | PARTIAL | "Frequently Asked Questions" H2 missing |
| 16 | Home Staging Albert Park | /home-staging-albert-park/ | PASS | None |
| 17 | Home Staging Windsor | /home-staging-windsor/ | PARTIAL | "Frequently Asked Questions" H2 missing |
| 18 | Home Staging Caulfield | /home-staging-caulfield/ | PASS | None |
| 19 | Home Staging Brighton | /home-staging-brighton/ | PARTIAL | "FAQs About Home Staging in Brighton" H2 missing |
| 20 | Home Staging Northcote | /home-staging-northcote/ | PASS | None |
| 21 | Areas We Serve | /areas-we-serve/ | PARTIAL | "Frequently Asked Questions" H2 missing |

---

## OVERALL VERDICT

- **PASS: 6 pages** — Pages 3, 5, 7, 10, 16, 18, 20 (note: 7 pages total pass)
- **PARTIAL: 14 pages** — All other pages have at least one missing or mislevelled heading
- **FAIL: 0 pages** — No page has a wrong meta title, wrong H1, or completely absent content

**Corrected totals:**
- PASS: 7 pages (3, 5, 7, 10, 16, 18, 20)
- PARTIAL: 14 pages (1, 2, 4, 6, 8, 9, 11, 12, 13, 14, 15, 17, 19, 21)
- FAIL: 0 pages

### Two recurring issue patterns

**Pattern A — Missing "Frequently Asked Questions" H2 (affects 12 pages):**  
Pages 1, 2, 9, 11, 12, 13, 14, 15, 17, 19, 21, and implicitly page 4 (different wording). The FAQ section exists with individual question H3s, but the approved H2 wrapper ("Frequently Asked Questions" or "FAQs About X") was not added as a section header above the FAQ block. This is a single template-level fix: add the H2 above the FAQ accordion/block on all affected pages.

**Pattern B — Heading level promotion/demotion errors (affects 4 pages):**  
- Page 1: "Thoughtful Home Styling in Melbourne" — approved H3, live H2
- Page 6: "Styling Packages for Every Property and Budget" — approved H2, live H3; "How We Work" — approved H3, live H2
- Page 8: "Our Luxury Styling Process" — approved H3, live H2
- Page 11: "Cutting Through Apartment Market Saturation" — approved H3, live H2

**Pattern C — Missing H2 (non-FAQ) (affects 2 pages):**  
- Page 4: "Get Your Melbourne Property Market-Ready" — entire H2 section is missing from the live page
- Page 4 only (Pattern C is isolated to this page)

### Priority fix list

| Priority | Issue | Pages Affected |
|---|---|---|
| HIGH | Add missing FAQ section H2 above FAQ block | 1, 2, 9, 11, 12, 13, 14, 15, 17, 19, 21 |
| HIGH | Correct H2/H3 level swap | 1, 6, 8, 11 |
| MEDIUM | Add missing "Get Your Melbourne Property Market-Ready" H2 section | 4 |
