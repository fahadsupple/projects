# Skyflex.au — Upgrade Re-Check (27 July 2026)

**Follow-up to:** `review-skyflex-upgrade-2026-07-24.md`
**Method:** All 7 live pages re-fetched from skyflex.au today and compared string-by-string against `Skyflex - Content for Additional Keywords (Approved) (1).docx`, `Skyflex - Daily Tasks for Upgrade (July 2026).docx` and `Skyflex.au-Keyword-URL-Meta.xlsx`.

**Bottom line:** Schema work has been done since the last check — **FAQPage schema is now live on all 7 pages** and the stale homepage/Sydney FAQ markup has been regenerated. That clears both schema items from the 24 July list. However, **the two High-priority H1 fixes were not made**, the US-spelling clean-up was not made, and the re-check surfaced **4 issues that were not visible on 24 July**, including a whole approved CTA section missing from the Delta Pro page and a product-page size dropdown that now contradicts the new copy.

---

## Status of the 24 July action list

| # | Priority | Item | Status today |
|---|----------|------|--------------|
| 1 | **High** | `/product/delta-commercial-folding-arm/` — add second H1 line "A Retractable Awning Melbourne Buyers Own Outright" | ❌ **Not done.** Live H1 is still just "Delta Commercial Folding Arm". Primary keyword *retractable awning melbourne* still appears nowhere in the H1, and the tagline text is not anywhere on the page. |
| 2 | **High** | `/product/skyflex-4k-android-smart-outdoor-tv/` — add second H1 line "A Waterproof TV Australia Backyards Can Actually Use" | ❌ **Not done.** Live H1 is still just "Skyflex 4K Android Smart Outdoor TV". Primary keyword *waterproof tv australia* still absent from the H1. |
| 3 | Medium | `/` and `/louvred-pergolas-sydney/` — regenerate stale FAQPage schema | ✅ **Done.** Homepage schema now carries all 8 visible questions (was 5); Sydney schema now carries all 11 visible questions. Markup matches visible content. (One new defect on the homepage — see 4.2.) |
| 4 | Low | `/product/skyflex-bbq-pods/` — add H1 tagline "An Outdoor Kitchen Made to Your Configuration" | ❌ **Not done.** H1 is still "Skyflex BBQ Pods Melbourne" (keyword is present, so still cosmetic). |
| 5 | Low | Fix US spellings in existing product copy | ❌ **Not done.** Still live: `/delta-pro-retractable-roof/` "aluminum track"; `/delta-commercial-folding-arm/` "6063 aluminum alloy", "Customization Is Available", "resists fading and Mold"; `/skyflex-bbq-pods/` "Exterior Color", "Customization Options", "Customizable" (7× color, 2× customization, 5× customizable). |
| 6 | Low / opp. | Add FAQPage schema to the 4 product pages + `/smart-toilets/` | ✅ **Done.** All five now emit FAQPage with the full approved question set (8 each). |
| 7 | Confirm | Delta Pro specs presented as WooCommerce attributes instead of the approved standalone block | ⚠️ **Unchanged** — still no "Delta Pro specifications" H2 or bullet list. Every value is live somewhere (PVC roof on aluminium track, sizes 3×3 to 6×4, Beige/Black/White fabric, Black/Charcoal/White frame, 40W DC 24V IP67 Dooya motor, handheld remote, integrated LED, 100% waterproof closed) — just spread across the attributes table and FAQ answers. Client decision. |

---

## New issues found in this pass

### 4.1 Delta Pro is missing its entire closing CTA section — Medium
The approved doc ends `/product/delta-pro-retractable-roof/` with an H2 **"Order your Delta Pro"** and the line *"Choose your size, fabric and frame colour and add the Delta Pro to your cart, or call the Skyflex team in Melbourne on 03 9498 0505 to talk through the right size for your space before you buy."* Neither the heading nor the sentence is on the live page. Every other page in the round received its closing CTA ("Talk to the Skyflex team", "Book a BBQ pod consultation", "Pre-order your Skyflex outdoor TV", "Enquire about a Skyflex Smartoilet") — Delta Pro is the only one that lost it. **Fix:** add the approved H2 + paragraph at the end of the Delta Pro description.

### 4.2 Homepage FAQPage schema contains an empty question — Medium
The regenerated homepage FAQ markup has **9 `mainEntity` items, but the 9th has an empty `name` and an empty `acceptedAnswer.text`**. An empty Question object is invalid structured data and can invalidate the whole FAQ block in Google's parser. It is almost certainly an empty accordion row left in the FAQ block. **Fix:** delete the blank FAQ item on the homepage so the markup outputs exactly 8 questions.

### 4.3 Outdoor TV — the closing CTA was built inside the FAQ accordion — Medium
On `/product/skyflex-4k-android-smart-outdoor-tv/` the closing CTA **"Pre-order your Skyflex outdoor TV"** is marked up as an **H3 inside the FAQ block**, not as an H2 after it. Consequence: it is emitted in the FAQPage schema as a 9th *question*, with the CTA sentence as its *answer*. Google sees a call-to-action posing as an FAQ. **Fix:** move the CTA out of the accordion and make it an H2, matching how the folding-arm, BBQ and smart-toilet pages did it.

### 4.4 BBQ pod size dropdown still shows the old, wrong dimensions — Medium
The new approved copy on `/product/skyflex-bbq-pods/` correctly states **2200W x 2300H x 720D** and **2850W x 2300H x 720D** (both appear twice, in the sizes section and the FAQ). But the WooCommerce **Size** variation dropdown on the same page still offers **"2200w x 2300h x 770w"** and **"2850w x 2300h x 770w"** — the old value, with depth mislabelled as a second "w". A buyer sees two different depths on one page. This was raised as a client/dev item when the copy was corrected; it is still outstanding. **Fix:** update the two Woo variation labels to `2200W x 2300H x 720D` and `2850W x 2300H x 720D`.

---

## Re-confirmed as correct

- **All 7 pages return HTTP 200**, including `/smart-toilets/`.
- **Meta titles: 7/7 character-exact** against the approved doc.
- **Meta descriptions: 7/7 character-exact.**
- **H1: 4/7 exact** (homepage, Sydney, Delta Pro, Smart Toilets). Exactly one H1 per page on all 7.
- **Indexability:** `index, follow` on all 7; self-referencing canonical on all 7.
- **Schema base:** WebPage + WebSite + BreadcrumbList on all 7; Product on the 4 product pages; **FAQPage now on all 7**.
- **Navigation:** "View All Smart Toilets" → `/smart-toilets/` still present.
- **Body content:** every approved paragraph is live on `/delta-commercial-folding-arm/`, `/skyflex-4k-android-smart-outdoor-tv/`, `/skyflex-bbq-pods/` and `/smart-toilets/` — including the "Who it is for" audience blocks, pricing lines, IP-rating explanations, the power-point warning and all "Call us now on 03 9498 0505" CTAs. Homepage, Sydney and Delta Pro are complete apart from the items listed above.
- **Homepage / Sydney partial FAQ merge** (4 of 8 approved questions on the homepage, 11 of 12 on Sydney) is unchanged and remains consistent with the client's "don't change existing content" instruction — schema now matches whatever is visible, which is the important part.
- **New copy is clean Australian English** on all 7 pages; the only US spellings are in the pre-existing manufacturer blocks listed in item 5.

---

## Developer action list (what still needs doing)

| Priority | Page | Action |
|---|---|---|
| **High** | `/product/delta-commercial-folding-arm/` | Add "A Retractable Awning Melbourne Buyers Own Outright" as smaller text inside the H1 tag. Still outstanding from 24 July. |
| **High** | `/product/skyflex-4k-android-smart-outdoor-tv/` | Add "A Waterproof TV Australia Backyards Can Actually Use" inside the H1 tag. Still outstanding from 24 July. |
| **Medium** | `/product/delta-pro-retractable-roof/` | Add the missing closing CTA: H2 "Order your Delta Pro" + the approved sentence. |
| **Medium** | `/` | Remove the blank FAQ item producing an empty Question in the FAQPage schema. |
| **Medium** | `/product/skyflex-4k-android-smart-outdoor-tv/` | Move "Pre-order your Skyflex outdoor TV" out of the FAQ accordion and mark it up as an H2 so it stops appearing as an FAQ question in schema. |
| **Medium** | `/product/skyflex-bbq-pods/` | Change the two Woo Size options from `...x 770w` to `2200W x 2300H x 720D` / `2850W x 2300H x 720D`. |
| **Low** | `/product/skyflex-bbq-pods/` | Add the H1 tagline "An Outdoor Kitchen Made to Your Configuration". |
| **Low** | Delta Pro, Folding Arm, BBQ Pods | US → AU spelling in the existing manufacturer copy: aluminum→aluminium, Customization→Customisation, Mold→Mould, Color→Colour, Customizable→Customisable. |

## Still open with the client

- **Delta Pro "100% waterproof when closed"** — the claim is live; confirm it is accurate before it stays.
- **U6 / U7 Smartoilet products** still sit in WooCommerce "Uncategorized" rather than being associated with the new `/smart-toilets/` collection page.
- **"Delta Pro specifications"** — confirm the WooCommerce-attribute presentation is acceptable in place of the approved standalone bullet block (all values are present, just relocated).
