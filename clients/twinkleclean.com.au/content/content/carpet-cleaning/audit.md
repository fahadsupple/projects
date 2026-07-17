# Audit — carpet-cleaning (service-hubs)

## Scores
- Humanity: 100/100 — PASS
- Differentiation: 89/100 — PASS (well above the 85 warning band; sibling = the other hub)
- SEO: 91/100 — PASS
- Machine audit gate (audit-gate.json): **0 blocking, 0 active findings**
- Cross-cluster coherence: 0 overlapping pairs

## LLM auditor coverage verdict (authoritative over the literal matcher)
`seo_check` emits "universal/cluster-required topic missing" flags by literal string-match of the requirement text; its own docstring notes these do NOT affect the score and are dropped by the machine gate (the LLM auditor judges real coverage). Verified per-topic — all required topics are genuinely covered:
- Primary keyword in H1 + lede, Melbourne positioning, who-it's-for intro: covered
- Trust/compliance (police checks, $20M PL + WorkCover, 100% guarantee, QA): covered
- Flexibility (7-day no-surcharge, no lock-in, free quotes): covered
- Verified social proof (20+ yrs combined, 1,200+, 90% retention, 40% referral, Oneflare 5/5 not Google): covered
- Pricing-without-inventing-prices: covered
- 8-question PAA-grounded FAQ, em-dash-free: covered
- Grounded method/process passage: covered
- AI-visibility citable answer blocks + NAP: covered (FAQ Q&A blocks; NAP now includes Ringwood locality + phone + email)
- Hub positioning + scope: covered

## Deferred (not a defect)
- "Areas we service / Suburbs we cover" section is present with descriptive anchor text but internal LINKS to the suburb spokes are deferred to a re-link pass once the location clusters are generated (linker returned 0 live-target edges — linking now would 404).

## Info (non-blocking)
- Some secondary keywords not present verbatim (covered semantically); can be woven in during a later optimisation pass if desired.

## Guardrails verified
- 0 em-dashes; founded 2019 with 20+ years stated as COMBINED experience (no "20 years in business"); reviews attributed to Oneflare not Google; business name and NAP verbatim; no fabricated statistics; no fake testimonials; no "Why Choose Us" heading.
