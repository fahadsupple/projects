# Interleaved dispatch order — remaining 32 suburb pages

The locked plan's `execution_order_within_cluster` grouped seven consecutive
apartment/shared-entrance suburbs right after three already generated in that territory.
Ten near-consecutive pages on one angle is how a suburb matrix converges into one
templated page. This order breaks that up: no two consecutive dispatches share a primary
territory. Deviation logged to events.jsonl (event 01KYV9S4YC546HTJCNXND70TBM); the
locked plan itself is untouched.

Territory codes: APT apartment/shared · SUP customer-supplied · PRC price/quote
· COV coverage/travel · PREP door-prep/drilling · RET retrofit-existing · MIX other

## Done (8)
| # | suburb | territory |
|---|---|---|
| 1 | melbourne (hub) | pillar |
| 2 | kensington | APT (permission, master key) |
| 3 | maidstone | MIX (which doors take a deadbolt) |
| 4 | richmond | APT/RET (fire-rated, finished face) |
| 5 | newport | MIX (bifold, non-hinged) |
| 6 | tarneit | PREP/SUP (cutting an unprepared door) |
| 7 | sunshine | MIX (security screen clearance) |
| 8 | port-melbourne | APT (interior-only locking) |
| 9 | st-kilda | APT (complex entrance, master key) |

## Remaining (32), interleaved

| # | suburb | territory | angle in one line |
|---|---|---|---|
| 10 | kingsville | MIX | joining an existing keying/access-control regime |
| 11 | flemington | APT | keeping the existing cylinder while adding smart entry |
| 12 | seddon | PREP | a door with no deadbolt bore at all |
| 13 | essendon | APT | which credential, and whether a key override remains |
| 14 | ascot-vale | RET | legacy Australian lockset retrofit |
| 15 | prahran | APT | onto the deadlock already fitted in a unit |
| 16 | altona | PREP | aluminium frame with glazed panel, drilling |
| 17 | truganina | PRC | what drives price across house vs commercial door |
| 18 | south-melbourne | APT | permission before hardware on an apartment entry |
| 19 | spotswood | PREP | what gets permanently drilled |
| 20 | south-yarra | APT/RET | retrofit onto existing hardware vs full replace |
| 21 | werribee | MIX | multi-door job, wood door with differing frames |
| 22 | hawthorn | APT | what is reversible and what is permanent |
| 23 | point-cook | MIX | does the handle-and-lock set come out |
| 24 | footscray | MIX | lever/latch conversion, door still closes and locks |
| 25 | braybrook | SUP | fit-only on hardware the customer owns |
| 26 | moonee-ponds | MIX | onto just the existing top lock |
| 27 | deer-park | PRC | what a free per-door quote covers |
| 28 | williamstown | RET | preserving the look and action of an original door |
| 29 | hoppers-crossing | SUP | will the retail lock already bought fit |
| 30 | maribyrnong | RET/SUP | retrofit onto an existing door, supplied hardware |
| 31 | kew | PRC | hardware cost vs labour in the quote |
| 32 | altona-north | PREP | aluminium/glazed plus model-specific licensing |
| 33 | toorak | MIX | the honest case for staying mechanical |
| 34 | williams-landing | MIX | the straightforward single front door |
| 35 | yarraville | PRC | not knowing what it should cost |
| 36 | caroline-springs | SUP/RET | modern and established homes in one estate |
| 37 | brighton | COV | bayside coverage, does a specialist travel here |
| 38 | wyndham-vale | SUP | fit-only on new-estate front doors |
| 39 | sunshine-west | MIX | hole coverage and filling after a swap |
| 40 | st-albans | COV | specialists don't serve the west; a mobile locksmith does |

Brighton and St Albans both sit in COV and are deliberately separated (37 and 40) rather
than run back to back. They are also the two thinnest bundles, so they benefit from the
densest possible corpus by the time they run.

## Per-dispatch differentiation duty

For each entry, the dispatch prompt must name the two or three nearest siblings BY
TERRITORY (not by geography) and state what ground each already owns. Geographic
adjacency is irrelevant to templating; angle adjacency is the whole risk.
