# Audit — carpet-cleaning-dandenong (pilot, service-location-carpet-cleaning)

## Scores
- Humanity: 100/100 — PASS
- Differentiation: 85/100 — PASS (siblings: the two hubs; spoke legitimately references hub concepts)
- SEO: 85/100 — PASS (literal secondary-keyword match; advisory not authoritative)
- Machine audit gate: **0 blocking**

## Pilot findings (fixed before scaling to the other 19 suburbs)
1. honesty_corpus_contradiction (was 3 blocking) — the gate reduces an approved-corpus "we do not <verb>" line to the bare verb and flags any "we <verb>" on other pages. The commercial hub's "we do not give / use / publish" phrasings poisoned every spoke that said "we give/use...". FIXED at root: reworded the hub to positive phrasing; corpus negative_assertions is now empty.
2. SEO score crater (was 31) — the 24 generic supporting-keywords copied onto every carpet page (many un-claimable, e.g. "certified quality management systems") deducted -3 each. FIXED: trimmed all 20 carpet entries' secondary_keywords to a grounded, localized 6-term set. Stuffing was rejected as it would create ungrounded claims.

## Guardrails verified
0 em-dashes; primary keyword in H1 + lede; lean spoke credibility (founder, 2019, 1,200+, guarantee) with 2 links up to the carpet hub; suburb grounding from suburb-data (SE commercial/residential hub, high rental turnover -> end-of-lease angle); Oneflare not Google; no fabricated suburb facts.
