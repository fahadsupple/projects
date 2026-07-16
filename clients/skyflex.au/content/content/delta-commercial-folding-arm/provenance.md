# Provenance — delta-commercial-folding-arm

Mode: rewrite-existing. Source live page: https://skyflex.au/product/delta-commercial-folding-arm/
(snapshot: research/raw/playwright-product-delta-commercial-folding-arm.json)

The page is a near-complete rewrite. Almost all prose is NEW. Only discrete product
identifiers, spec values, price values and the phone number are carried from the live page.
Below, EXISTING lists only spans reproduced VERBATIM (exact string). Where a live value was
reformatted (case, US to en-AU spelling, dash to "to", dropped .00 or ®) it is listed under
REFORMATTED — value is from the live page but the string is not verbatim, so it should NOT be
highlighted as unchanged-existing.

## EXISTING (verbatim from the live page — highlight yellow)

- `Delta Commercial Folding Arm` — product name (live schema_name / H1). Used in H1, spec section, pricing section, CTA.
- `Dooya Silent` — motor brand (live "Motor Specs > Brand: Dooya Silent").
- `DC 240V` — motor rated voltage (live "Rated Voltage: DC 240V").
- `IP67` — motor IP class / waterproof grade (live "Motor Waterproof Grade: IP67" and "IP Class: IP67").
- `3000W x 2500P` — size option (live variation_selects attribute_pa_size).
- `4000W x 3000P` — size option (live variation_selects attribute_pa_size).
- `Black` / `White` — colour options (live variation_selects attribute_pa_colour).
- `03 9498 0505` — phone number (live header + "TALK TO OUR AUSTRALIAN TEAM" + footer).
- Numeric spec/price values reproduced exactly: `6063` (aluminium alloy grade), `$2,000`, `$2,300`, `50%` (deposit), `30` (degrees pitch), `40` (watts).

## REFORMATTED (value from live page, string changed — treat as new text carrying an existing value)

- Fabric brand: live `Dickson®` -> written `Dickson` (® dropped).
- Frame alloy: live `6063 aluminum alloy` (US) -> `6063 aluminium alloy` (en-AU).
- Motor power: live `40w` -> `40W`.
- Connection: live `AU Plug In` -> `AU plug-in`.
- Motor `Remote control` -> `remote controlled`.
- Pitch: live `Pitch can be adjusted up and down by up to 30°` -> `projection angle adjustable up to 30 degrees`.
- Mounts: live `Wall or Ceiling mounts included` -> `wall or ceiling brackets included`.
- Price range: live `$2,000.00 – $2,300.00` `(Supplied)` -> `from $2,000 to $2,300, supplied` / `from $2,000`.
- Deposit: live `Pay a deposit of 50% per item` + `PRE ORDER NOW!` -> `pre-order item with a 50% deposit per unit`.
- Value claim: live H3 `UP TO 8X CHEAPER` -> `up to 8x cheaper than comparable systems` (grounded on this product's own live page).
- Customisation: live `Customization Is Available with Additional Charges – Contact Us` -> `customisation is available on request, with any additional charges quoted before you commit`.
- Install manual: live download `Installation Manual: Full Cassette Awning` -> `the full-cassette installation manual included in the box`.
- Trade: live `Buying 5+ units? Get in touch to receive exclusive trade discounts.` -> `Orders of five units or more qualify for trade pricing`.
- Core description tokens (`Fully Enclosed, Motorised`, `Full Cassette Retractable Awning`, `integrated dimmable LED lighting`, `fade-resistant Dickson® fabric`, `all-weather protection`) were rewritten into new prose, not copied.

## NEW (newly written for this engagement — no highlight)

- Title tag and meta description (product-accurate; the live page had NO meta description).
- The H1 wording and the entire lede.
- All five H2 headings and all body prose: the open-arm vs full-cassette differentiation, the
  "waterproof retractable awning" framing, the spec-list framing, the supply-basis pricing/order
  explanation, and the CTA.
- "About Skyflex" credibility passage. Facts within it are grounded, but the SENTENCES are new:
  - Founder `Christopher Mitsopoulos`, established `2023`, `100+` customers, `50%` referral rate —
    sourced from plan.lock.json publishable_facts + client_data_signals, NOT from this live product
    page. Grounded-new, not existing-page content.
  - Showroom `Epping` by appointment — from client_data_signals / live footer address
    (`Unit 10/63 Ricky Way Epping 3076, Victoria`), paraphrased.

## Deliberately NOT carried (guardrails honoured)

- No FAQ block: research returned ZERO PAA and zero community questions for this keyword (plan data-gated FAQ rule).
- No 15-year warranty and no "most affordable louvre roof" award: those are pergola-line claims; this product's live page states no warranty length, so none was asserted.
- No RRP strike-through / discount percentage (`Save 18%`, `$2,450`, `$2,799`): suppressed per analyst decision #6 (volatile promo pricing).
- Live-page US spelling ("aluminum", "Customization") corrected to en-AU.
- Live-page "0-87 degrees of louver opening" spec omitted: reads as a louvre-product copy-paste on a folding-arm awning and would confuse buyers; omission is safe (no fabricated value added).
