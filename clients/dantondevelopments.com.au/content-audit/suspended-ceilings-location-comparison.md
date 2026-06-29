# Content Comparison Audit — Suspended Ceilings Location Pages
**Danton Developments — Live vs Staging**

- **Live domain:** https://dantondevelopments.com.au
- **Staging domain:** https://dantondevelstg.wpenginepowered.com
- **Audit date:** 2026-06-29
- **Pages checked:** 13 suspended ceilings location pages
- **Method:** Playwright browser snapshot (Epping, Truganina) + WebFetch content extraction (all 13 pages)

---

## Important Context: Staging is a Full Site Redesign

The staging site is **not just an update to the live site** — it is a complete redesign with a new theme and new page template structure. Every page on staging has these additions compared to live:

| Element | Live | Staging |
|---|---|---|
| Trust badge strip in hero | Not present | 4 badges: 25+ Years, Premium Materials, 3000+ Projects, Fully Insured |
| Breadcrumb navigation | Not present | Home > Areas > [Location] |
| Hero sidebar form | Simple (Name, Email, Phone, Subject, Message) | Expanded (First Name, Last Name, Phone, Email, Service dropdown, Message) |
| "Other Services" cards section | Not present | Plaster Ceilings, Grid Ceilings, Ceiling Repairs, Drop Ceilings cards |
| "Our Recent Work" photo gallery | Not present | Present (repeats on some pages) |
| Mid-page "Get in Touch" section | Not present | Present with duplicate contact form |
| Brand logos strip | Not present | "Built on Experience. Driven by Quality." with 16 brand logos |
| CTA banner above footer | Not present | "Maintenance & Emergency Repairs" banner |
| Footer | Simple (Quick Links, Our Services, Contact Us) | Full-column redesign with expanded services, ABN, opening hours, Instagram |
| Opening hours | Not in footer | Monday–Friday 7am–5pm, Saturday 8am–5pm |
| Instagram link | Not present | Added |
| ABN | Not present | ABN: 38 105 969 589 |
| FAQ display | Fully expanded (all answers visible) | Accordion (collapsed by default, first question expanded) |

These are **intentional redesign changes** and are consistent across all 13 pages. They are noted here for completeness but are not content regressions.

The focus of the comparisons below is **actual body copy text, headings within the content sections, and page titles** — the content that was written specifically for each location page.

---

## Page-by-Page Results

---

### 1. /suspended-ceilings-epping/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-epping/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-epping/

**Status: DIFFERENCES FOUND**

#### Page Title
| | Text |
|---|---|
| Live | Suspended Ceilings Epping \| Expert Installation Services |
| Staging | Suspended Ceilings Epping \| Expert Installation Services \| Danton Developments |

**Difference:** Staging appends `| Danton Developments` to the title. All other pages on both sites already include `| Danton Developments` in their title — this appears to be an inconsistency on the staging version (or a fix applied to staging to standardise titles).

#### H1
- Live: `Suspended Ceilings Epping`
- Staging: `Suspended Ceilings Epping`
- **MATCH**

#### Content Headings (H2/H3 in page body)
| Heading | Live level | Staging level |
|---|---|---|
| Why Epping Properties Need Modern Ceiling Services | H2 | H2 |
| Drop Ceilings Epping – Versatile Services for Every Space | H2 | H2 |
| Your Local Suspended Ceiling Experts in Epping | H2 | H2 |
| Why Choose Danton Developments Pty Ltd | H2 | H2 |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H2 | H3 (demoted) |

#### Body Copy
All body paragraphs match verbatim between live and staging. Confirmed paragraph by paragraph via Playwright full-page snapshot.

#### FAQ Content
Same 6 questions and answers on both. Live displays all answers expanded; staging uses accordion (answers collapsed but content is present).

---

### 2. /suspended-ceilings-truganina/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-truganina/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-truganina/

**Status: ✅ BODY COPY MATCH**

#### Page Title
- Live: `Suspended Ceilings Truganina | Danton Developments`
- Staging: `Suspended Ceilings Truganina | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Truganina`
- Staging: `Suspended Ceilings Truganina`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Drop Ceilings Truganina – Versatile Services for Every Space | H2 | H2 |
| Tailored Installation for Local Building Styles | H3 | H3 |
| Your Local Suspended Ceiling Specialists in Truganina | H2 | H2 |
| Why Choose Danton Developments for Suspended Ceilings | H2 | H2 |
| Transform Your Truganina Property Today | H2 | H2 |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H2 | H3 (demoted) |

#### Body Copy
All body paragraphs verified verbatim via Playwright snapshot — match confirmed.

#### FAQ Content
Same 7 questions and answers on both.

---

### 3. /suspended-ceilings-williams-landing/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-williams-landing/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-williams-landing/

**Status: ✅ BODY COPY MATCH**

#### Page Title
- Live: `Suspended Ceilings Williams Landing | Danton Developments`
- Staging: `Suspended Ceilings Williams Landing | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Williams Landing`
- Staging: `Suspended Ceilings Williams Landing`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Professional Drop Ceilings Williams Landing Services | H2 | H2 |
| Your Local Ceiling Specialists Serving Williams Landing | H2 | H2 |
| Why Choose Danton Developments Pty Ltd | H2 | H2 |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H2 | H3 (demoted) |

#### Body Copy
All intro paragraphs, service descriptions, local specialist section, and FAQ content match between live and staging.

---

### 4. /suspended-ceilings-preston/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-preston/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-preston/

**Status: HEADING LEVEL DIFFERENCE (body copy matches)**

#### Page Title
- Live: `Suspended Ceilings Preston | Danton Developments`
- Staging: `Suspended Ceilings Preston | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Preston`
- Staging: `Suspended Ceilings Preston`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Extensive Drop Ceilings Preston Services | H2 | H2 |
| Commercial Office Services | **H3** | **H2** (promoted) |
| Retail & Hospitality Fitouts | **H3** | **H2** (promoted) |
| Your Local Suspended Ceiling Experts in Preston | H2 | H2 |
| Complete Range of Ceiling & Partition Services | H2 | H2 |
| Why Choose Danton Developments Pty Ltd | H2 | H2 |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H3 | H3 |

**Difference:** "Commercial Office Services" and "Retail & Hospitality Fitouts" are H3 subheadings under "Extensive Drop Ceilings Preston Services" on live, but are promoted to H2 on staging. This is a structural/SEO change — the content text under those headings appears the same.

#### Body Copy
Content under all headings appears to match.

---

### 5. /suspended-ceilings-cheltenham/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-cheltenham/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-cheltenham/

**Status: HEADING STRUCTURE DIFFERENCE in "Why Choose" section (body copy present but restructured)**

#### Page Title
- Live: `Suspended Ceilings Cheltenham | Danton Developments`
- Staging: `Suspended Ceilings Cheltenham | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Cheltenham`
- Staging: `Suspended Ceilings Cheltenham`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Why Cheltenham Properties Need Modern Ceiling Services | H2 | H2 |
| Extensive Drop Ceilings Cheltenham Services | H2 | H2 |
| Tailored Services for Every Property Type | H2 | H2 |
| Your Local Suspended Ceiling Experts in Cheltenham | H2 | H2 |
| Why Choose Danton Developments Pty Ltd | H2 | H2 |
| Premium Materials & Guaranteed Workmanship | **H3** | **Not present as H3** |
| Direct Access to Knowledgeable Professionals | **H3** | **Not present as H3** |
| Complete Project Management | **H3** | **Not present as H3** |
| Flexible Service Options | **H3** | **Not present as H3** |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H2 | H3 (demoted) |

**Difference:** The four H3 subheadings within the "Why Choose Danton Developments Pty Ltd" section on live (Premium Materials, Direct Access, Complete Project Management, Flexible Service Options) are **not present as headings** on staging. The content for each sub-section appears to still be in the page as bold-text paragraphs, but the heading tags have been removed. This is a structural/SEO change — the actual copy text is preserved.

#### Body Copy
All body paragraph text matches. The "Why Choose" content is restructured (bold paragraphs instead of H3 headings) but the words are the same.

---

### 6. /suspended-ceilings-cremorne/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-cremorne/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-cremorne/

**Status: HEADING LEVEL DIFFERENCE (body copy matches)**

#### Page Title
- Live: `Suspended Ceilings Cremorne | Danton Developments`
- Staging: `Suspended Ceilings Cremorne | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Cremorne`
- Staging: `Suspended Ceilings Cremorne`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Solving Cremorne's Unique Acoustic Challenges | H2 | H2 |
| Drop Ceilings Cremorne – Concealing Services with Style | H2 | H2 |
| End-to-End Ceiling Services Include: | **H3** | **H2** (promoted) |
| Complete Interior Services Beyond Ceilings | H2 | H2 |
| Why Choose Danton Developments | H2 | H2 |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H2 | H3 (demoted) |

**Difference:** "End-to-End Ceiling Services Include:" is H3 on live but H2 on staging. Content under the heading appears to match.

#### Body Copy
All body paragraphs match between live and staging.

---

### 7. /suspended-ceilings-richmond/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-richmond/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-richmond/

**Status: CONTENT DIFFERENCE — word changed in heading**

#### Page Title
- Live: `Suspended Ceilings Richmond | Danton Developments`
- Staging: `Suspended Ceilings Richmond | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Richmond`
- Staging: `Suspended Ceilings Richmond`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Expert Drop Ceilings Richmond for Modern Workspaces | H2 | H2 |
| Wide-Ranging Ceiling Services for Richmond Businesses | H2 | H2 |
| Grid Ceilings and Office Partitions | H3 | H3 |
| Complete Fitout Services | H3 | H3 |
| Your Local Suspended Ceiling Experts in Richmond | H2 | H2 |
| Suspended Ceilings for Richmond: Why Choose Danton Developments | **H2 (live)** | **Suspended Ceilings for Richmond Homes: Why Choose Danton Developments** (staging) |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H2 | H3 (demoted) |

**CONTENT DIFFERENCE:**
- Live heading: `Suspended Ceilings for Richmond: Why Choose Danton Developments`
- Staging heading: `Suspended Ceilings for Richmond Homes: Why Choose Danton Developments`
- The word **"Homes"** has been added in the staging version. This is a content change — the live version does not say "Homes", and the Richmond pages are primarily commercial-focused pages. This should be reviewed before launch.

#### Body Copy
All other body paragraphs appear to match between live and staging.

---

### 8. /suspended-ceilings-port-melbourne/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-port-melbourne/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-port-melbourne/

**Status: ✅ BODY COPY MATCH**

#### Page Title
- Live: `Suspended Ceilings Port Melbourne | Danton Developments`
- Staging: `Suspended Ceilings Port Melbourne | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Port Melbourne`
- Staging: `Suspended Ceilings Port Melbourne`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Drop Ceilings Port Melbourne – Solutions for Every Commercial Space | H2 | H2 |
| Complete Interior Fitout Solutions Beyond Ceilings | H2 | H2 |
| Your Local Commercial Interior Experts in Port Melbourne | H2 | H2 |
| Why Choose Danton Developments for Suspended Ceilings Port Melbourne | H2 | H2 |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H2 | H3 (demoted) |

#### Body Copy
All content paragraphs, bullet lists, and FAQ content match between live and staging.

---

### 9. /suspended-ceilings-collingwood/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-collingwood/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-collingwood/

**Status: ✅ BODY COPY MATCH**

#### Page Title
- Live: `Suspended Ceilings Collingwood | Danton Developments`
- Staging: `Suspended Ceilings Collingwood | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Collingwood`
- Staging: `Suspended Ceilings Collingwood`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Solving Collingwood's Acoustic Challenges with Expert Ceiling Services | H2 | H2 |
| Your Local Suspended Ceiling Industry Experts in Collingwood | H2 | H2 |
| Why Choose Danton Developments for Suspended Ceilings in Collingwood | H2 | H2 |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H2 | H3 (demoted) |

#### Body Copy
All body paragraphs, service list items, and FAQ content match verbatim between live and staging.

---

### 10. /suspended-ceilings-southbank/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-southbank/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-southbank/

**Status: ✅ BODY COPY MATCH**

#### Page Title
- Live: `Suspended Ceilings Southbank | Danton Developments`
- Staging: `Suspended Ceilings Southbank | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Southbank`
- Staging: `Suspended Ceilings Southbank`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Professional Drop Ceilings Southbank – Complete Acoustic Services | H2 | H2 |
| Your Local Suspended Ceiling Experts in Southbank | H2 | H2 |
| Why Choose Danton Developments Pty Ltd | H2 | H2 |
| Wide-Ranging Ceiling Services Beyond Acoustics | H2 | H2 |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H3 | H3 |

#### Body Copy
All body paragraphs, service list items, and FAQ content match between live and staging.

---

### 11. /suspended-ceilings-geelong/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-geelong/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-geelong/

**Status: ✅ BODY COPY MATCH**

#### Page Title
- Live: `Suspended Ceilings Geelong | Danton Developments`
- Staging: `Suspended Ceilings Geelong | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Geelong`
- Staging: `Suspended Ceilings Geelong`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Drop Ceilings Geelong for Modern Commercial Spaces | H2 | H2 |
| Extensive Ceiling and Partition Solutions | H2 | H2 |
| Why Choose Danton Developments Pty Ltd | H2 | H2 |
| Professional Process from Quote to Completion | H2 | H2 |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H2 | H3 (demoted) |

#### Body Copy
All body paragraphs, ceiling type lists, process steps, and FAQ content match between live and staging.

---

### 12. /suspended-ceilings-grovedale/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-grovedale/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-grovedale/

**Status: ✅ BODY COPY MATCH**

#### Page Title
- Live: `Suspended Ceilings Grovedale | Danton Developments`
- Staging: `Suspended Ceilings Grovedale | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Grovedale`
- Staging: `Suspended Ceilings Grovedale`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Complete Range of Ceiling Services for Every Space | H2 | H2 |
| Why Choose Danton Developments | H2 | H2 |
| The Process: From Consultation to Completion | H2 | H2 |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H2 | H3 (demoted) |

#### Body Copy
All body paragraphs, service list items, process steps, and FAQ content match between live and staging.

---

### 13. /suspended-ceilings-moolap/

**Live:** https://dantondevelopments.com.au/suspended-ceilings-moolap/
**Staging:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings-moolap/

**Status: ✅ BODY COPY MATCH**

#### Page Title
- Live: `Suspended Ceilings Moolap | Danton Developments`
- Staging: `Suspended Ceilings Moolap | Danton Developments`
- **MATCH**

#### H1
- Live: `Suspended Ceilings Moolap`
- Staging: `Suspended Ceilings Moolap`
- **MATCH**

#### Content Headings
| Heading | Live level | Staging level |
|---|---|---|
| Solving Common Ceiling Challenges with Modern Services | H2 | H2 |
| Residential Ceiling Transformations | H2 | H2 |
| Commercial and Industrial Applications | H2 | H2 |
| Extensive Ceiling Services for Every Need | H2 | H2 |
| Your Local Suspended Ceiling Experts in Moolap | H2 | H2 |
| The Danton Developments Difference | H2 | H2 |
| From Planning to Completion – Our Process | H2 | H2 |
| Frequently Asked Questions | H2 | H3 (demoted) |
| Areas We Serve | H2 | H3 (demoted) |

#### Body Copy
All body paragraphs, bullet lists, process steps, and FAQ content match between live and staging.

---

## Summary of Findings

### Issues Requiring Action Before Launch

| # | Page | Issue | Severity |
|---|---|---|---|
| 1 | /suspended-ceilings-richmond/ | Heading changed: "Suspended Ceilings for Richmond: Why Choose Danton Developments" → "Suspended Ceilings for Richmond **Homes**: Why Choose Danton Developments" | **HIGH** — content change, word "Homes" inserted, inaccurate for a commercial-focused page |
| 2 | /suspended-ceilings-epping/ | Page title on staging appends `\| Danton Developments` not present on live: "…Expert Installation Services **\| Danton Developments**" | **MEDIUM** — likely intentional title standardisation, but differs from live; confirm intended |

### Structural/SEO Changes (Same Across All Pages — Likely Intentional Redesign)

These are consistent across all 13 pages and appear to be deliberate design/template changes rather than errors. Flag with the developer if any are unexpected:

| Change | Pages affected |
|---|---|
| "Frequently Asked Questions" demoted from H2 (live) → H3 (staging) | All 13 |
| "Areas We Serve" demoted from H2 (live) → H3 (staging) | Most pages |
| FAQ answers: fully expanded on live → accordion/collapsed on staging | All 13 |
| "Commercial Office Services" + "Retail & Hospitality Fitouts" promoted from H3 → H2 | Preston |
| "End-to-End Ceiling Services Include:" promoted from H3 → H2 | Cremorne |
| 4 H3 subheadings in "Why Choose" section removed as headings (content kept as bold text) | Cheltenham |

### Body Copy Status

| Page | Body copy status |
|---|---|
| Epping | ✅ Matches |
| Truganina | ✅ Matches |
| Williams Landing | ✅ Matches |
| Preston | ✅ Matches |
| Cheltenham | ✅ Matches |
| Cremorne | ✅ Matches |
| Richmond | ✅ Matches (heading differs, body copy same) |
| Port Melbourne | ✅ Matches |
| Collingwood | ✅ Matches |
| Southbank | ✅ Matches |
| Geelong | ✅ Matches |
| Grovedale | ✅ Matches |
| Moolap | ✅ Matches |

**All 13 pages: body copy content is intact and matches live. The only wording-level content difference found is the "Homes" insertion in the Richmond heading.**
