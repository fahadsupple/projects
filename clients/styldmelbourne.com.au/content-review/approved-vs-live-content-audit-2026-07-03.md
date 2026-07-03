# STYLD Melbourne — Approved Content vs Live Site Audit
**Date:** 2026-07-03
**Source of truth:** `styldmelbourne.com.au (Approved).docx` (21 pages)
**Method:** Extracted all 21 pages from the approved doc (meta title, meta description, H1/H2/H3, body copy, FAQs) and cross-checked against the live rendered HTML of each corresponding URL (fetched directly, WIX serves this content server-side so no rendering gaps).
**Scope note (per brief):** The "Packages" section on every page (intro line + Market Ready / Signature / Premium bullet copy) is known to be swapped out for the live 3-card package widget — that swap was excluded from the checks below and is not reported as an issue.

## Headline result
- **Meta titles:** 21/21 match exactly. ✅
- **Meta descriptions:** 21/21 match exactly. ✅
- **Body copy:** 20/21 pages match almost word-for-word (aside from the packages swap). Two pages have real content gaps (below).
- **Heading structure (H1/H2/H3 levels):** This is where the real problems are — the same defects flagged in the 22 Jun audit are still live, 11 days later.

---

## 1. Still-unresolved heading bugs (carried over from the 19/22 Jun audits — not fixed)

### Bug A — FAQ section heading renders as a second H1 instead of H2
Confirmed still live on **11 of 21 pages**:
- `/home-staging/` — "FAQs About Home Staging in Melbourne"
- `/property-styling/` — "FAQs About Property Staging Melbourne"
- `/home-staging-prahran/` — "Frequently Asked Questions"
- `/home-staging-st-kilda/` — "Frequently Asked Questions"
- `/home-staging-richmond/` — "Frequently Asked Questions"
- `/home-staging-middle-park/` — "Frequently Asked Questions"
- `/home-staging-port-melbourne/` — "Frequently Asked Questions"
- `/home-staging-south-melbourne/` — "Frequently Asked Questions"
- `/home-staging-windsor/` — "Frequently Asked Questions"
- `/home-staging-brighton/` — "FAQs About Home Staging in Brighton"
- `/areas-we-serve/` — "Frequently Asked Questions"

Each of these pages now has two `<h1>` tags. This is a template-level issue (same FAQ block across many pages), not a one-off — worth pushing to the developer as a single fix rather than 11 manual edits.

**Pages where this was previously broken and is now fixed:** `/furniture-staging/`, `/real-estate-staging/`, `/home-staging-cost/`, `/full-property-styling/`, `/partial-property-styling/`, `/luxury-property-styling/`, `/home-staging-south-yarra/`, `/home-staging-albert-park/`, `/home-staging-caulfield/`, `/home-staging-northcote/` — 10 pages now correctly render FAQ as H2.

### Bug B — H2/H3 level swaps (4 of the original 5 still live)
- `/home-staging/` — "Thoughtful Home Styling in Melbourne" is H2, should be H3
- `/full-property-styling/` — "How We Work" is H2 (should be H3); "Styling Packages for Every Property and Budget" is H3 (should be H2) — these two are swapped with each other
- `/luxury-property-styling/` — "Our Luxury Styling Process" is H2, should be H3
- `/home-staging-st-kilda/` — "Cutting Through Apartment Market Saturation" is H2, should be H3

**Fixed since 22 Jun:** `/home-staging-caulfield/` — "Home Styling Packages in Caulfield" is now correctly H2.

---

## 2. New issue found — duplicated/orphaned FAQ answer on `/full-property-styling/`
The FAQ block has come apart at one question:

**Approved:**
> Do you offer vacant property staging and partial styling?
> Yes. We provide complete vacant property staging, and partial styling for occupied homes that already have suitable foundations in place.
>
> How long does the styling stay in place?
> Our standard campaign styling period is six weeks. You can extend it, or arrange collection at the end of the campaign.

**Live (actual rendered order):**
> Do you offer vacant property staging and partial styling?
> Yes. We provide complete vacant property staging, and partial styling for occupied homes that already have suitable foundations in place.
> *[same answer repeats a second time, verbatim]*
> Our standard campaign styling period is six weeks. You can extend it, or arrange collection at the end of the campaign.

The question **"How long does the styling stay in place?"** has been dropped from the accordion, its answer got tacked onto the previous answer, and the previous answer duplicated itself. This reads as a broken/misconfigured FAQ item in the CMS — worth a specific developer ticket, not just a copy fix.

---

## 3. Missing paragraph — `/property-styling/`
Under H2 "Pre-Sale Property Styling for Melbourne Homes", the approved intro sentence is missing entirely from live. The page jumps straight from the H2 to the bullet-list intro line.

**Approved (missing on live):**
> "No two listings call for the same approach, and we plan accordingly. Some homes need a full transformation. Others just need a refined layer over what's already there, and our stylists shape the brief around what actually matters for your campaign. Whatever the brief, our team aligns each decision with the property's architecture, location and likely buyer."

---

## 4. Minor content drift (low priority, not urgent)
A handful of pages have small wording additions beyond the approved copy — none change meaning, all read fine, but they are technically off-script from what was approved:
- Several pages had the word **"artwork"** inserted into sentences that didn't have it in the approved doc (e.g. Prahran FAQ, Albert Park intro, Full/Partial Property Styling FAQs, Port Melbourne intro, Luxury Property Styling intro). Reads like a deliberate later copy tweak rather than an error.
- `/real-estate-staging/` FAQ has a subject–verb agreement slip: live reads *"...a layout and design that **highlight** the home's features..."* — approved copy correctly reads *"...that **highlights** the home's features..."*. Small grammar fix worth queuing.
- A few Oxford-comma differences (e.g. "furniture, rugs, lighting and more" vs approved "furniture, rugs, lighting, and more") — cosmetic only, not worth actioning.

---

## Recommended next steps
1. **Priority 1 (developer):** Fix the FAQ-heading-as-H1 template bug across the 11 affected pages — likely one shared component fix.
2. **Priority 2 (developer):** Fix the 4 remaining H2/H3 level swaps individually (home-staging, full-property-styling ×2, luxury-property-styling, home-staging-st-kilda).
3. **Priority 3 (developer):** Investigate and fix the duplicated/orphaned FAQ item on `/full-property-styling/` — likely a CMS repeater item that got deleted incorrectly.
4. **Priority 4 (content, low urgency):** Restore the missing intro paragraph on `/property-styling/`; fix the "highlight" → "highlights" typo on `/real-estate-staging/`.
5. No action needed on the Packages sections — confirmed intentional (replaced by the live package card widget on every page) and on meta titles/descriptions (21/21 match).
