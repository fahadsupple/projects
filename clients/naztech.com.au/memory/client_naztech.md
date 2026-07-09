# Client Memory — naztech.com.au

## Business Overview
- **Name:** NAZTECH Mobile Auto Electrical & Air Conditioning
- **Owner:** Sharfraz Nazim
- **ABN:** 25 435 345 491 (Sole Trader, Active since Apr 2023)
- **Founded:** 2025
- **Address:** 91 Sundance Promenade, Pakenham VIC 3810
- **Phone:** 0449 992 695
- **Email:** info@naztech.com.au
- **Website:** https://naztech.com.au
- **Hours:** Mon–Fri 7:30am–5pm | Sat 7:30am–1pm | Sun closed

## What They Do
Fully mobile auto electrical and air conditioning service. Technician comes to the vehicle — no towing required. Three sectors:
1. **Light Automotive** — Cars, 4WDs, Caravans, Motorhomes, Marine
2. **Heavy Transport** — Trucks, Truck Trailers
3. **Heavy Equipment** — Earthmoving, Civil, Mining, Construction, Forklifts, Tractors, Farming Equipment

## Service Area
South East Melbourne + Gippsland. 10 LGAs (priority order):
1. Cardinia Shire Council
2. Casey City Council
3. Yarra Ranges Shire Council
4. Baw Baw Shire Council
5. Greater Dandenong City Council
6. Bass Coast Shire Council
7. Frankston City Council
8. Mornington Peninsula Shire Council
9. South Gippsland Shire Council
10. Latrobe City Council

## Key USPs
- ARC Licensed — No. AU066885 (mandatory for A/C refrigerant work)
- Fully mobile — minimal downtime, no towing costs
- PO/account arrangements for commercial clients (councils, fleets, mining)
- 43+ Google Reviews | 400+ vehicles repaired | 200+ installations
- 8 years Hitachi/Tutt Bryant/William Adams Cat/Sherrin Rentals experience
- 3 years Jungheinrich & Manitou material handling experience
- $10M public & product liability insurance
- E.A.C.H. values: Explanation, Acknowledgment, Connection, Honesty

## Certifications
- ARC (Australian Refrigeration Council) Licence No. AU066885
- Certificate III in Automotive Electrical Technology
- Certificate II in Automotive Air Conditioning Technology

## Competitors
- Auto Remedies Pty Ltd T/A Budget Mobile Auto Electrics (Cranbourne North) — in Local Pack
- JCM Auto Electrics (Narre Warren/Pakenham) — in Local Pack, named competitor
- Kent Auto Air & Electrical
- Lonsdale St. Auto Electrics
- TRI-LEC AUTO ELECTRICAL

## KWR Package — FINALISED (Phase 0 complete)
- **Type:** location_only
- **Total:** 45 location keywords
- **Silos:** 3 × 15 suburbs
- **Silo 1:** `mobile auto electrician` — KD 4, suburb vol 20–50/mo
- **Silo 2:** `mobile aircon regas` — KD 4, 390/mo national, ARC licence differentiator
- **Silo 3:** `mobile car battery replacement` — KD 10, 1,300/mo national, $8.56 CPC, +60% YoY
- **Mode:** fresh

## Suburb Selection (15 suburbs across 10 LGAs)
| Priority | Suburb | LGA |
|---|---|---|
| 1 | Pakenham | Cardinia Shire |
| 2 | Officer | Cardinia Shire |
| 3 | Berwick | Casey City |
| 4 | Narre Warren | Casey City |
| 5 | Cranbourne | Casey City |
| 6 | Clyde North | Casey City |
| 7 | Lilydale | Yarra Ranges |
| 8 | Mooroolbark | Yarra Ranges |
| 9 | Warragul | Baw Baw |
| 10 | Dandenong | Greater Dandenong |
| 11 | Wonthaggi | Bass Coast |
| 12 | Frankston | Frankston |
| 13 | Mornington | Mornington Peninsula |
| 14 | Leongatha | South Gippsland |
| 15 | Traralgon | Latrobe City |

## Key Research Findings (Phase 0)
- `mobile auto electrician melbourne` — 110/mo, KD 4, high paid competition (0.66). SERP dominated by small local businesses, winnable.
- `mobile car battery replacement` national — 1,600/mo, KD 10, $7.86–$8.56 CPC, +60% YoY growth. Emergency/impulse service NAZTECH can serve same-day.
- `mobile car ac regas` national — 390/mo, KD 4. ARC licence (AU066885) is legal differentiator — competitors without ARC cannot legally do regas.
- Suburb-level A/C regas and battery keywords below SE Ranking threshold — traffic captured via geo-personalisation, not volume-tracked.
- Melbourne modifier kills specialty terms (truck, heavy vehicle, dual battery) — those better as general pages if added later.
- JCM Auto Electrics is the biggest direct competitor (Narre Warren/Pakenham overlap, also in Local Pack).

## Project Status
- kwr:init complete — 2026-06-15
- Phase 0 (budget allocation): **COMPLETE** — 2026-06-15
- Phase 1 (seeds): pending
- Phase 2 (suburbs): skipped — analyst-selected in Phase 0
- Plugin client dir: `/home/invoi/.claude/plugins/cache/colana-mp/kwr/0.3.0/clients/naztech.com.au/`

## Daily Tasks — Dev Handoff (9 Jul 2026)
Deliverable: `clients/naztech.com.au/daily-task/Naztech.com.au - Daily Tasks.docx`
Source: `Naztech.com.au-Keyword-URL-Meta.xlsx`, "Meta Data" sheet ONLY (client rule: always ignore "Hardy" sheets and other sheets in this file).

**Live site structure at time of review (11 pages total):** `/`, `/gallery/`, `/pakenham/`, `/services/`, `/cars/`, `/about/`, `/areas-we-serve/`, `/air-conditioning/`, `/auto-electrical-services/`, `/mobile-air-conditioning-repairs-servicing/`, `/contact/`.

**Meta Data sheet color rule confirmed by client:** yellow-highlighted URL rows = new pages to be created. Redirects only where the sheet has an explicit "Current URL: https://..." note.

**Renames + 301 (2):** `/pakenham/` → `/mobile-auto-electrician-pakenham/`; `/cars/` → `/car-aircon-regas/`.

**New pages (44 total):** 13 mobile-auto-electrician suburb pages (Pakenham excluded, handled via rename) + 14 car-aircon-regas suburb pages + 14 car-battery-replacement suburb pages + `/car-aircon-regas/` (root) + `/car-battery-replacement/` (root) + `/areas-we-serve/` (marked yellow despite already existing — flagged as a full rebuild into the suburb-hub page for all 3 silos).

**Template:** `/pakenham/` (soon `/mobile-auto-electrician-pakenham/`) used as the structural template for all new suburb pages. No existing page in the car-aircon-regas or car-battery-replacement suburb silos — first suburb page built in each becomes that silo's new template.

**Client decision (asked directly, 9 Jul 2026):** `/auto-electrical-services/` and `/mobile-air-conditioning-repairs-servicing/` are richer content matches for `/mobile-auto-electrician/` and `/car-aircon-regas/` respectively, but client chose to follow the Meta Data sheet literally — no redirect from either page, sheet's `/cars/` → `/car-aircon-regas/` note stands as-is.

**Open flag (unresolved):** `/mobile-auto-electrician/` currently 404s but is NOT marked yellow and has no "Current URL" note in the sheet — inconsistent with every other row. Needs client/analyst confirmation before dev starts on that specific page.

**Suburb list discrepancy flagged:** Meta Data sheet uses 14 suburbs incl. "Clyde" (not "Clyde North") and excludes Mooroolbark, vs. the earlier finalised KWR Phase 0 plan (15 suburbs, Mooroolbark included, "Clyde North"). Daily task doc follows the Meta Data sheet per client instruction; discrepancy flagged in the doc's Open Items section for confirmation.

**Nav/footer changes specified:** remove standalone "Cars"/"Pakenham" nav items; add 3 new "Services" dropdown items (Mobile Auto Electrician / Car Aircon Regas / Car Battery Replacement); footer "Services" column gets the same 3 links replacing the single "Air Conditioning" link.

**Content note:** Title/Description/H1/H2/H3/Interlinking words columns are blank for every row in the Meta Data sheet — this daily task doc covers URL structure/redirects/templates/nav/footer only. Page copy is a separate, not-yet-started deliverable.

## Daily Tasks — Update (9 Jul 2026, same day)
Client requested two changes after initial doc was built:
1. **Template switch:** use the homepage (not Pakenham) as the template for all 42 location pages. Pakenham's content will be rebuilt to the new homepage-based template too, on top of its URL rename. Doc updated accordingly — trimmed-per-silo instruction added (don't duplicate the full homepage structure verbatim on every suburb page).
2. **Homepage neutrality fix:** homepage was found to be heavily industrial/commercial-skewed — hero image (truck/toolbox scene), "Brands & Equipment We Work On" 20-tile grid (completely empty, no logos loading), 6 equipment-list columns (Heavy Equipment x3, Trucks, Farming, Mining — zero Light Automotive column), "Industries & Equipment We Service" grid (7/8 tiles industrial, only "General Vehicles" for light auto), and reviews heading "Trusted by Commercial Operators Across Melbourne" (excludes private/light-vehicle customers). New Section 4 added to the daily task doc with 4 annotated screenshots (hero, brands grid, equipment lists, industries grid) specifying what needs to change to represent all 3 service sectors (Light Automotive / Heavy Transport / Heavy Equipment) neutrally.

Updated deliverable still at: `clients/naztech.com.au/daily-task/Naztech.com.au - Daily Tasks.docx` (now 11 sections, 6 embedded screenshots).
