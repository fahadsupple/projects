# Homepage (skyflex.au) — Provenance

**Entry:** homepage | **page_type:** homepage | **mode:** add-blocks | **primary keyword:** `pergolas melbourne`
**Source of existing content:** `content/homepage-existing.json` (live-page snapshot, https://skyflex.au/)

Render rule for the export: NEW = plain, EXISTING-KEPT = yellow highlight (verbatim), EXISTING-DEFECT = yellow + flagged for correction.

---

## NEW (newly written for this engagement — render plain)

The single added block, positioned as the page's lead narrative. Headings, in order:

1. H1 — `Pergolas Melbourne: Louvred Outdoor Living Made for the Local Climate` (contains primary keyword exact-match; becomes the page's single H1)
2. H2 — `A louvred pergola range built for Melbourne weather` (product proposition: adjustable aluminium louvred slats, motorised remote operation, perimeter lighting standard, all-weather aluminium build, the Delta range, year-round use in Melbourne's variable weather)
3. H2 — `See the range in Epping, then choose a kit or an installer` (Melbourne local presence + Epping showroom + DIY-kit vs approved-installer choice — the homepage differentiator vs the Sydney page)
4. H2 — `About Skyflex` (FULL credibility block: founder Christopher Mitsopoulos, established 2023, 100+ customers, 50% referral rate, up-to-15-year warranty, "most affordable motorised louvre roof" award + from $2,700, double-walled gasket-sealed louvres, 150x150 posts, hidden anchoring, designed in Europe, fully customisable)
5. H2 — `Browse the range or book a showroom visit` (CTA: order online / request a quote / book an Epping showroom visit)

Plus new `title` and `meta_description` lines proposed for the page.

Fact sources for NEW block:
- Founding year 2023, 100+ customers, 50% referral rate → `plan.lock.json > publishable_facts` (confirmed).
- Warranty, award + $2,700, gasket louvres, 150x150 posts, DIY-kit + installer, Europe design, customisation → `plan.lock.json > client_data_signals` (`awards`, `guarantees`, `usps_verbatim`).
- Showroom address + phone → existing live page (`homepage-existing.json`), consistent with client NAP.

## EXISTING-KEPT (current live page — preserve verbatim, render yellow)

- Hero product banners: Delta OpenSky (from $12,150), Delta Motorised (from $4,950), Delta Light Motorised (from $2,700) + their taglines.
- "Our Products" grid tiles: Delta Light Motorised, Delta Motorised, Delta Open Sky, Delta Pro Retractable Roof, Delta Commercial Folding Arm, Delta Elevating Pool & Spa Cover, Delta Roller Pool & Spa Cover, SKYFLEX 4K Android Smart Outdoor TV, SKYFLEX BBQ Pods.
- Existing Melbourne marketing sections: "Louvred Roof Pergolas in Melbourne – Enhance Your Outdoor Living"; "Premium Louvred Pergolas for Sale in Melbourne" (incl. "SkyFlex vs. Others", "Up to 8x cheaper", "The traditional Skyflex Way"); "Buy Louvred Pergolas in Melbourne from SkyFlex".
- Testimonials block ("What Our Clients Say About Us" — 6 reviews).
- FAQ block ("Frequently Asked Questions About Louvred Pergolas in Melbourne" — 4 answers).
- "Talk to our Australian Team" / footer: showroom address 10/63 Ricky Way, Epping VIC 3076; phone 03 9498 0505; copyright line.

## EXISTING-DEFECT (present on live page — flagged to correct, not fixed by this add-blocks pass)

1. **H2 "Why Choose SkyFlex for Louvred Pergolas in Melbourne?"** — the banned "Why Choose Us" recital pattern (self-praise reasons list). The new "About Skyflex" block already carries these signals as concrete proof. Recommend replacing the heading or folding its real points into the About block.
2. **Empty "U6 Smartoilet" and "U7 Smartoilet" grid tiles** — headings with no product body/price in the live grid. Populate both with product detail + a price/enquiry path, or remove until the range is ready.
3. **Dual-H1 risk (positioning note, not a live defect):** the existing H1 "Louvred Pergolas Melbourne" plus the new H1 would make two H1s. Recommend demoting the existing H1 to H2 (or folding its intro into the new lead). Heading-level change only; copy preserved.

Note: the existing hero-banner string "TO ANY SIZE — SETTING COLOUR!" contains an em-dash. It is EXISTING copy (kept verbatim, yellow); the em-dash ban applies only to the NEW block, which has zero.
