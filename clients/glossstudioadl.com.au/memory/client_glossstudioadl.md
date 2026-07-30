---
name: client-glossstudioadl
description: Gloss Studio Adelaide — automotive paint protection/ceramic coating/window tinting, Klemzig SA; kwr pipeline v1 complete 27 Jul 2026 (4G+36L)
metadata:
  type: project
---

# Gloss Studio Adelaide — glossstudioadl.com.au

## Business
- **Name:** Gloss Studio Adelaide. ABN 22 697 583 270, Australian Private Company, GST registered.
- **Entity age:** ABN active since 2026-04-29 (~3 months at research time). BDM brief said "1-month-old" — **use the ABN date**.
- **Premises:** Unit 4, 13 Thames Avenue, Klemzig SA 5087. **Single fixed workshop, NOT mobile** — all work indoors under controlled lighting/climate. This constrains catchment: weight inner-north / inner-east / north-east over far-south metro.
- **Contact:** 0416 610 413 / info@glossstudioadl.com.au
- **Services (only 4):** Ceramic Coating, Paint Protection Film (PPF), Paint Correction, Window Tinting.
- **Site:** flat 9-page .html site. New website build is an in-scope deliverable, so URL structure is provisional.
- **DA 0**, no GSC property, no Google rating/reviews.

## Open data gaps / conflicts (unresolved — need client input)
- **Owner name MISSING** — questionnaire Q3 and Q9 both auto-filled with ABN-lookup dumps. Blocks E-E-A-T / about-page / author work.
- **NAP CONFLICT:** questionnaire says Mon–Fri 9–5, Sat 9–3; live site footer and /areas.html say Mon–Fri 8–5, Sat 8–3. Must resolve before GBP/citation work.
- **No GSC property** — quick-wins track, impression demand validation and striking-distance detection all unavailable.
- **adelaidedetailinggarage.com.au excluded from competitor set pending escalation** — it is the owner's former employer; warehouse marks it 'active' while the BDM brief calls it an ex-client. Analyst excluded it until the conflict is resolved.
- **BDM "mirror the ADG portfolio" instruction** was flagged by BDM as needing client confirmation.

## Keyword research v1 — COMPLETE 27 Jul 2026
Files: `clients/glossstudioadl.com.au/keyword-research/` (config.json, questionnaire.json, research/v1/, report.html, report-shared.html). All phases 0–6 completed.

- **Package:** fixed_split, 4 general + 36 location = 40. business_type local_service, SA only.
- **3 silos × 12 suburbs (uniform grid):** window_tinting, paint_protection, ceramic_coating.
- **12 suburbs:** Prospect, Norwood, Campbelltown, Salisbury, Enfield, Magill, Rostrevor, North Adelaide, Broadview, Clearview, Gepps Cross, Mawson Lakes. Scored data-driven over the client's own 39 declared /areas.html suburbs (analyst decision) rather than open Adelaide-metro discovery.
- **4 general:** window tinting adelaide (1000/mo, KD 3), paint protection adelaide (880/mo, KD 0, CPC $5.71 — best commercial opportunity in the account), ceramic coating adelaide (720/mo, KD 0), ppf adelaide (210/mo, KD 7, CPC $6.85 — highest CPC).
- **Rejected:** `car detailing adelaide` (1600/mo) as **off-service** — Q12 lists only the 4 protection services; ranking for it would attract work the client does not sell. Also rejected `paint correction adelaide` (50/mo, comp 86) as too thin — covered as a secondary on ceramic-coating and paint-protection pages.
- **Brand terms zero-volume at Adelaide geography** ('xpel adelaide', 'gyeon ceramic coating adelaide', 'tesla ceramic coating adelaide'). GYEON/XPEL/SunTek/3M/LLumar authorised-partner status is real and stays as secondaries + on-page trust signals, but earns no general slot.
- near_me and brand_defence both suppressed at source by config flags (GBP / reputation tracks, not organic).

## Non-obvious findings worth carrying forward
- **Weak-authority market.** No rival exceeds DA 15 (ceramicar 15, adelaidepaintprotection 13, elitefinish 12, adelaideautomotivedetailing 10, madcoupe 3, eyecandydetailing 2, svautosalon 1). Head-term KD is 0–7. A Phase 0 note claiming incumbents held "years of accrued authority" and that head terms were a 12-month play was **corrected as WRONG** once DA data landed — head terms are contestable inside 12 months.
- **Zero-volume suburb grid is deliberate, not a data failure.** 29 of 36 location keywords are zero even at national scope. The recovered Adelaide Detailing Garage portfolio (SE Ranking project 9980456) shows 16 of 20 suburb pages holding position 1 on exactly these zero-volume terms. Any downstream filter that drops zero-volume keywords would delete 29 of 36 deliverables.
- **Campbelltown volume is inflated ~72x by interstate contamination.** At AU-national scope (location_code 2036) 'window tinting campbelltown' reads 720/mo — that is Campbelltown **NSW**, 1,300km away. Adelaide-scoped (location_code 1000422) it is 10/mo. Campbelltown SA stays selected on ADG position-1 proof + Q17 naming + inner-east proximity, but **forecast at ~20/mo, not 830/mo**. Headline reach 3,730/mo overstates by ~820; honest Adelaide-scoped figure ≈ **2,910/mo**.
- **Local pack on 31 of 42 probed SERPs (74%)** while the client has no review base — for a DA-0 business the local pack is the fastest route to visibility, which materially raises the value of the GMB deliverable over organic content.
- **Terminology:** AU/SA market uses "window tinting" (not "window film"); "paint protection" outranks "paint protection film" 4:1 at Adelaide level. **SA VLT limits (75% windscreen, 35% front side) are a genuine content differentiator with no equivalent in other states.**
- **Title collision to fix in implementation:** homepage title already leads with "Ceramic Coating Adelaide" while /ceramic-coating.html targets the same term. And /paint-protection-film.html currently holds the film-specific title but should be retargeted so the generic 4x-volume term gets the head page.
- **Vendor volume disagreement:** SE Ranking's ADG record stores 'ceramic coating adelaide' at 10/mo vs GKP 720/mo — ~72x. Treat SE Ranking stored volumes for this vertical as unreliable.

See also [[keyword_research_master]], [[feedback_seo_keyword_strategy_ecommerce]], [[feedback_seo_location_page_rules]].
