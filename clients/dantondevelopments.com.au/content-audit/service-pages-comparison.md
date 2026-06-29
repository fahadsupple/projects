# Danton Developments — Service Pages Content Comparison Audit

**Date:** 2026-06-29
**Live domain:** https://dantondevelopments.com.au
**Staging domain:** https://dantondevelstg.wpenginepowered.com
**Auditor:** Claude (automated WebFetch extraction)
**Scope:** 5 service pages — main content area only (headings, body copy, lists, CTAs; navigation and footer excluded)

---

## Summary Table

| Page | Status |
|---|---|
| /suspended-ceilings/ | ⚠️ DIFFERENCES FOUND (see below) |
| /office-partition-walls/ | ❌ 404 ON BOTH LIVE AND STAGING |
| /glass-partition-walls/ | ⚠️ STAGING HAS ADDITIONS (core content matches) |
| /plasterboard-partitions/ | ⚠️ STAGING HAS ADDITIONS + 1 CONTENT DIFFERENCE |
| /ceiling-replacement-repairs/ | ✅ CONTENT MATCH |

---

## Recurring Pattern — New Sections on Staging (Across Multiple Pages)

The staging site has been redesigned with several new UI sections added to service pages. These are **additions on staging** not present on live:

1. **Key Features badge bar** (top of page) — "25+ Years Industry Experience | Premium Materials & Guaranteed Workmanship | 3000+ Successful Projects | Fully Insured & Compliant"
2. **Dual CTA bar** — "Get a Free Quote" + "Talk to Expert 0403 709 884" (live only has a single "Get A Free Quote" button)
3. **Breadcrumb navigation** — e.g. "Home > Services > Partition Walls > Glass"
4. **"Built on Experience. Driven by Quality." section** — brand logo strip (Makita, Armstrong, USG Boral, Gyprock, Hilti, Rondo, DeWalt, etc.)
5. **"Maintenance & Emergency Repairs" CTA section**
6. **"Transform Your Space With Confidence" bottom CTA** — checklist of benefits + quote form prompt
7. **Inline CTAs** — repeated "Get a Free Quote | Call: 0403 709 884" inserted between sections throughout the page

These additions appear intentional (staging is a redesign). No core copy was removed to accommodate them. Flag with the developer/client for sign-off before launch.

---

## Page 1: /suspended-ceilings/

**Live URL:** https://dantondevelopments.com.au/suspended-ceilings/
**Staging URL:** https://dantondevelstg.wpenginepowered.com/suspended-ceilings/

### Critical Issue — JS Redirect on Live Site

The live /suspended-ceilings/ page contains JavaScript that redirects the browser to /suspended-ceilings-epping/ (a suburb location page). The staging site does NOT have this redirect — the service page loads normally. This is a significant difference. Either:
- The redirect should be removed from live before launch (staging is the correct behaviour), OR
- The redirect needs to be added to staging

**Action required:** Confirm with client/developer whether the redirect from /suspended-ceilings/ → /suspended-ceilings-epping/ is intentional on live and whether staging should replicate it.

### H1

| | Content |
|---|---|
| Live | Suspended Ceilings Melbourne |
| Staging | Suspended Ceilings Melbourne |
| Result | ✅ Match |

### Page Structure — H2/H3 Heading Order

**Live page headings:**
1. H2: Drop Ceilings Melbourne – Complete Commercial Services
2. H2: Grid Ceilings Melbourne and Office Partitions
3. H3: Commercial Fitouts and Retail Spaces
4. H3: Extensive Ceiling Services Across Melbourne
5. H3: Safety Standards and Quality Assurance
6. H3: Why Choose Danton Developments Pty Ltd
7. H3: Serving Melbourne and Geelong from Thomastown
8. H3: Get Your Free Quote Today
9. H3: FAQs About Suspended Ceilings

**Staging page headings (additional sections noted):**
1. [NEW] H2: Suspended Ceilings Services (with category tabs)
2. H2: Drop Ceilings Melbourne – Complete Commercial Services
3. H2: Grid Ceilings Melbourne and Office Partitions
4. H2: Commercial Fitouts and Retail Spaces
5. H2: Extensive Ceiling Services Across Melbourne
6. H2: Safety Standards and Quality Assurance
7. H2: Get Your Free Quote Today
8. H2: Why Choose Danton Developments Pty Ltd
9. [NEW] H3: Our Recent Work (gallery)
10. Serving Melbourne and Geelong from Thomastown
11. H3: Get in Touch
12. FAQs About Suspended Ceilings
13. [NEW] H3: Built on Experience. Driven by Quality. (brand logos)

Note: Live uses H3 for "Commercial Fitouts and Retail Spaces", "Safety Standards", etc. Staging promotes these to H2. This is a heading level change that affects SEO — confirm it is intentional.

### Content Differences

**DIFFERENCE 1 — Intro paragraph (live only, not confirmed on staging)**

Live has an introductory paragraph before the first H2:
> "Looking for reliable suspended ceilings in Melbourne? Danton Developments brings more than 25 years of experience to every commercial and office fitout across Melbourne and Geelong. From our Thomastown base, we deliver professional ceiling and partition solutions that transform workspaces while meeting your budget and timeline."
>
> "Whether you're a landlord upgrading a property, a business owner refreshing your office, or a tenant needing repairs, our team handles projects from $3,000 to more than $300,000 with the same commitment to quality and reliability."

Staging extraction did not return this intro text. It may be missing or it may be present but not extracted. **Verify visually.**

**DIFFERENCE 2 — Bullet point wording in Grid Ceilings section**

| | Text |
|---|---|
| Live | "Office partition walls creating meeting rooms **and private spaces**" |
| Staging | "Office partition walls creating meeting rooms" |

"and private spaces" is missing from the staging bullet point.

**DIFFERENCE 3 — New section on staging: "Suspended Ceilings Services"**

Staging has an entirely new H2 section below the hero with service category tabs:
"Plaster Ceilings | Grid Ceilings | Ceiling Replacement Repairs | Drop Ceilings"

This section does not exist on live.

### FAQs

Both live and staging have the same 8 FAQs with identical questions and answers:
1. What's the difference between suspended ceilings and drop ceilings?
2. How long does ceiling installation take?
3. Do you handle insurance work?
4. Can you match existing ceiling systems?
5. What maintenance do suspended ceilings require?
6. Are suspended ceilings suitable for retail shopfronts in Melbourne?
7. Can you install ceilings in high-clearance industrial warehouses?
8. Do you provide acoustic reports for ceiling installations?

Result: ✅ FAQs match

---

## Page 2: /office-partition-walls/

**Live URL:** https://dantondevelopments.com.au/office-partition-walls/
**Staging URL:** https://dantondevelstg.wpenginepowered.com/office-partition-walls/

### Result: ❌ 404 NOT FOUND ON BOTH LIVE AND STAGING

Neither the live nor staging site has a page at /office-partition-walls/. Both return HTTP 404.

The footer on the live site lists /partition-walls/ as a service page, not /office-partition-walls/. The correct URL may be one of:
- https://dantondevelopments.com.au/partition-walls/
- https://dantondevelopments.com.au/office-partitions/

**Action required:** Confirm the correct URL slug for this page and re-run the audit against the correct URL.

---

## Page 3: /glass-partition-walls/

**Live URL:** https://dantondevelopments.com.au/glass-partition-walls/
**Staging URL:** https://dantondevelstg.wpenginepowered.com/glass-partition-walls/

### H1

| | Content |
|---|---|
| Live | Glass Partition Walls Melbourne |
| Staging | Glass Partition Walls Melbourne |
| Result | ✅ Match |

### Core Content Comparison

All main body sections match between live and staging:

| Section | Live | Staging |
|---|---|---|
| Intro paragraphs | ✅ | ✅ Same |
| H2: Premium Glass Office Partitions Melbourne | ✅ | ✅ Same |
| — Full-height frameless glass walls | ✅ | ✅ Same |
| — Aluminium-framed glass partitions | ✅ | ✅ Same |
| — Acoustic glass services for sound control | ✅ | ✅ Same |
| — Manifestation and privacy films | ✅ | ✅ Same |
| — Sliding and hinged glass doors | ✅ | ✅ Same |
| — Fire-rated glass partition systems | ✅ | ✅ Same |
| H2: Aluminium Partitions and Complete Office Services | ✅ | ✅ Same |
| — Powder-coated finishes in an array of colours | ✅ | ✅ Same |
| — Integration with solid panels or glazing | ✅ | ✅ Same |
| — Cost-effective space division | ✅ | ✅ Same |
| — Quick installation with minimal disruption | ✅ | ✅ Same |
| — Flexibility for future reconfigurations | ✅ | ✅ Same |
| H2: Professional Installation Process (5 steps) | ✅ | ✅ Same |
| H3: Fire-Rated and Compliance Systems | ✅ | ✅ Same |
| H2: Why Choose Danton Developments Pty Ltd (5 points) | ✅ | ✅ Same |
| H2: Serving Melbourne and Geelong from Thomastown | ✅ | ✅ Same |
| H2: Get Your Free Quote Today | ✅ | ✅ Same |
| FAQs (8 questions) | ✅ | ✅ Same |

### Staging-Only Additions (not differences — new UI elements)

- Key Features badge bar
- Breadcrumb: Home > Services > Partition Walls > Glass
- "Built on Experience. Driven by Quality." brand logos section
- "Maintenance & Emergency Repairs" CTA

### Result: ✅ CORE CONTENT MATCH (staging has additions only, no content removed or changed)

---

## Page 4: /plasterboard-partitions/

**Live URL:** https://dantondevelopments.com.au/plasterboard-partitions/
**Staging URL:** https://dantondevelstg.wpenginepowered.com/plasterboard-partitions/

### H1

| | Content |
|---|---|
| Live | Plasterboard Partitions Melbourne |
| Staging | Plasterboard Partitions Melbourne |
| Result | ✅ Match |

### Core Content Comparison

| Section | Live | Staging |
|---|---|---|
| Intro paragraphs (2 paragraphs) | ✅ | ✅ Same |
| H2: Metal Stud Partitions Melbourne for Modern Workspaces | ✅ | ✅ Same |
| — Integration features list (5 items) | ✅ | ✅ Same |
| H2: Complete Plasterboard Services Across Melbourne | ✅ | ✅ Same |
| H3: Commercial Office Fitouts (5 items) | ✅ | ✅ Same |
| H3: Retail and Hospitality Partitions (5 items) | ✅ | ✅ Same |
| H2: Professional Installation Process (7 steps) | ✅ | ✅ Same |
| H2: Why Choose Danton Developments Pty Ltd (5 points) | ✅ | ✅ Same |
| H2: Service Areas and Availability (6 locations) | ✅ | ✅ Same |
| H2: Frequently Asked Questions (5 questions) | ✅ | ✅ Same |

### Content Differences

**DIFFERENCE 1 — Phone number formatting in "Get Your Free Partition Quote Today"**

| | Text |
|---|---|
| Live | "Call 0403709884 or email dantondevelopments@outlook.com" |
| Staging | "Call 0403 709 884 or email dantondevelopments@outlook.com" |

Live has no spaces in the phone number ("0403709884"). Staging has the correctly formatted number ("0403 709 884"). This is a live site typo that the staging has corrected, or a genuine content discrepancy. Either way, confirm which version is correct.

**DIFFERENCE 2 — Section order (possible)**

Staging extraction suggests "Get Your Free Partition Quote Today" may appear before "Why Choose Danton Developments Pty Ltd", whereas live places it after. Needs visual confirmation as WebFetch ordering may not be perfectly reliable.

### Staging-Only Additions

- Key Features badge bar
- Breadcrumb: Home > Services > Partition Walls > Plasterboard
- Inline CTAs inserted throughout page body
- "Built on Experience. Driven by Quality." brand logos section
- "Maintenance & Emergency Repairs" CTA
- "Transform Your Space With Confidence" bottom CTA with feature checklist

### Result: ⚠️ 1 CONFIRMED CONTENT DIFFERENCE (phone number formatting)

---

## Page 5: /ceiling-replacement-repairs/

**Live URL:** https://dantondevelopments.com.au/ceiling-replacement-repairs/
**Staging URL:** https://dantondevelstg.wpenginepowered.com/ceiling-replacement-repairs/

### H1

| | Content |
|---|---|
| Live | Ceiling Replacement Melbourne |
| Staging | Ceiling Replacement Melbourne |
| Result | ✅ Match |

### Core Content Comparison

| Section | Live | Staging |
|---|---|---|
| H2: Professional Ceiling Repair Melbourne Services | ✅ | ✅ Same |
| — Common issues list (7 items) | ✅ | ✅ Same |
| — Body paragraphs | ✅ | ✅ Same |
| H2: Complete Ceiling Replacement Melbourne Solutions | ✅ | ✅ Same |
| — Replacement options list (6 items) | ✅ | ✅ Same |
| — Body paragraph | ✅ | ✅ Same |
| H3: Commercial Office Ceiling Upgrades (5 factors) | ✅ | ✅ Same |
| H3: Specialised Commercial Ceiling Repairs | ✅ | ✅ Same |
| H3: Retail and Hospitality Ceiling Solutions | ✅ | ✅ Same |
| Why Choose Danton Developments Pty Ltd (5 points) | ✅ | ✅ Same |
| Our Ceiling Replacement Process (6 steps) | ✅ | ✅ Same |
| H3: Maintenance Programs Available | ✅ | ✅ Same |
| Get Your Ceiling Replacement Melbourne Quote Today | ✅ | ✅ Same |
| FAQs (8 questions) | ✅ | ✅ Same |

### FAQs — Verified Match (8 questions)

1. How fast can you respond to ceiling damage?
2. What types of ceiling systems do you repair and replace?
3. Do you handle insurance claims for ceiling damage?
4. Can you match existing ceiling tiles during repairs?
5. How long does ceiling replacement take?
6. Do you handle the disposal of old ceiling materials?
7. Can you repair ceilings that have sagged due to heavy insulation?
8. What is the most common cause of commercial ceiling failure in Melbourne?

### Result: ✅ CONTENT MATCH

---

## Action Items Before Launch

| Priority | Item | Page |
|---|---|---|
| HIGH | Investigate JS redirect: live /suspended-ceilings/ redirects to /suspended-ceilings-epping/ — staging does not. Confirm intended behaviour. | /suspended-ceilings/ |
| HIGH | /office-partition-walls/ returns 404 on both environments. Confirm correct URL slug (possibly /partition-walls/) and re-audit that page. | /office-partition-walls/ |
| MEDIUM | Verify staging has intro paragraphs for /suspended-ceilings/ — the two opening paragraphs from live were not confirmed in staging extraction. | /suspended-ceilings/ |
| MEDIUM | Restore missing words: staging bullet point reads "Office partition walls creating meeting rooms" — should end "and private spaces" (as on live). | /suspended-ceilings/ |
| LOW | Fix phone number format on /plasterboard-partitions/: live has "0403709884" (no spaces). Staging correctly shows "0403 709 884". Apply fix to whichever environment is wrong. | /plasterboard-partitions/ |
| LOW | Confirm heading level changes (H3 → H2 on staging for several sections on /suspended-ceilings/) are intentional — this affects SEO heading hierarchy. | /suspended-ceilings/ |
| INFO | All staging pages have new UI sections (Key Features bar, brand logos, bottom CTA, inline CTAs, breadcrumbs) — these are additions only, no content removed. Client/dev sign-off recommended before launch. | All pages |
