# Black Truffle Catering — SERP Relevance & Form Compliance Check

**Client:** blacktruffle.net.au (Black Truffle Catering)
**Scope:** the 20 shortlisted general keywords from `research/v1/keywords.json` (Phase 5 selection, v1)
**Date:** 31 July 2026
**Method:** live Google SERP pull, one request per keyword — DataForSEO `serp/google/organic/live/advanced`, `location_name = Melbourne,Victoria,Australia`, `language_code = en`, desktop, depth 20. Raw payloads: `research/v1/live-serp-2026-07-31/`.
**Reference:** client onboarding form response `P4SJ9rz7` (27/07/2026).

Note: the original Phase 3c probes ran at `location_code 2036` (Australia). This check re-ran at Melbourne city level, which is what a real customer sees. Differences are called out where they matter.

---

## 1. Verdict summary

| Verdict | Count | Keywords |
|---|---|---|
| **Relevant — proceed as planned** | 12 | 1, 2, 3, 5, 9, 10, 11, 12, 13, 15, 16, 17, 18 (see table) |
| **Relevant, but page mapping is wrong** | 4 | 4 `food catering`, 6 `party catering melbourne`, 14 `office catering melbourne cbd`, 19 `home catering melbourne` |
| **Relevant, but duplicates another selection** | 3 | 7 `home party catering melbourne`, 8 `birthday party catering melbourne`, 19 `home catering melbourne` |
| **Reject — intent mismatch** | 1 | 20 `ready made meals melbourne` |

19 of 20 return a SERP that a Melbourne catering company can legitimately compete in. One does not.

---

## 2. Per-keyword SERP relevance

`LP` = local pack results. `BT-LP` = Black Truffle present in local pack. `BT-org` = Black Truffle organic position. `Deep/10` = how many of the top 10 are dedicated sub-pages rather than homepages — this is the signal for whether Google wants a dedicated page or a general catering page.

| # | Keyword | LP | BT-LP | BT-org | Deep/10 | SERP composition | Relevant? |
|---|---|---|---|---|---|---|---|
| 1 | caterers melbourne | 3 | — | **7** | 3/10 | 9/10 direct Melbourne caterers, 1 directory (Yelp #10). Top 3 = The Catering Company, Devour It, Elizabeth Andrews | ✅ Yes — cleanest commercial SERP in the set |
| 2 | wedding catering melbourne | 3 | **YES** | >20 | 4/10 | 8/10 Melbourne wedding caterers, 2 directories (Easy Weddings #2, ABIA #5) | ✅ Yes |
| 3 | wedding caterers melbourne | 3 | **YES** | 12 | 3/10 | Same set, directory at #1 (Easy Weddings) | ✅ Yes |
| 4 | food catering | 3 | — | 12 | 3/10 | All Melbourne caterers, mostly **homepages** | ⚠️ Relevant, wrong page |
| 5 | catering melbourne cbd | 3 | — | **8** | 5/10 | 10/10 Melbourne caterers, zero directories | ✅ Yes |
| 6 | party catering melbourne | 3 | **YES** | **7** | **0/10** | 10/10 Melbourne caterers, **every result a homepage** | ⚠️ Relevant, wrong page |
| 7 | home party catering melbourne | 3 | — | **7** | 1/10 | General Melbourne caterers | ⚠️ Duplicate (see §3) |
| 8 | birthday party catering melbourne | 3 | **YES** | 16 | 5/10 | Dedicated birthday pages — but 3/10 are **kids' party** catering (HLB, Blakeaway, Rustik) | ✅ Yes, with a caveat |
| 9 | vegan catering melbourne | 2 | — | >20 | 8/10 | Dedicated vegan catering pages from mainstream Melbourne caterers | ✅ Yes |
| 10 | gluten free catering melbourne | 3 | — | >20 | **10/10** | Every result a dedicated gluten-free/dietary page | ✅ Yes |
| 11 | afternoon tea catering | 3 | — | >20 | 9/10 | Melbourne-dominated even without a modifier; 2/10 Sydney (Feedwell, Catering Project) | ✅ Yes |
| 12 | catering morning tea | 3 | — | >20 | 10/10 | Same; AI Overview present | ✅ Yes |
| 13 | corporate catering melbourne cbd | 3 | — | **3** | 6/10 | 10/10 Melbourne corporate caterers | ✅ Yes — strongest position already held |
| 14 | office catering melbourne cbd | 3 | — | **5** | 6/10 | Near-identical to #13 (8/10 same domains) | ⚠️ Relevant, over-split |
| 15 | lunch catering melbourne | 3 | — | **5** | 7/10 | 10/10 Melbourne caterers | ✅ Yes — client's stated Q11 priority |
| 16 | breakfast catering melbourne | 3 | — | >20 | **10/10** | Every result a dedicated breakfast catering page | ✅ Yes |
| 17 | finger food catering melbourne | 3 | — | **9** | 5/10 | Canapé/finger food pages, Melbourne | ✅ Yes |
| 18 | canape catering melbourne | 3 | — | 10 | 8/10 | Dedicated canapé pages, Melbourne | ✅ Yes |
| 19 | home catering melbourne | **0** | — | **3** | 1/10 | No local pack. AI Overview present. Generic Melbourne catering SERP | ⚠️ Duplicate (see §3) |
| 20 | ready made meals melbourne | 3 | — | >20 | 6/10 | **Zero caterers.** Subscription meal-delivery brands only | ❌ **Reject** |

---

## 3. Problems found

### 3.1 `ready made meals melbourne` — reject, intent mismatch

The top 10 is entirely direct-to-consumer subscription meal-delivery: Dinnerladies, Blakeaway, Dineamic, Pippa's Kitchen, We Feed You, Wilding Foods, FairFeed, FED Group, QVM, FoodSt. The local pack is meal-prep operators (FED Group, Hartwell Food Co, Lifestyle Meal Prep). There is not a single catering company in the results.

Two independent reasons this fails:

1. **Business-model mismatch.** These SERPs reward published per-meal pricing, weekly rotating menus and subscription checkout. Q14 of the form states plainly that "specific pricing details or fixed price lists are not published on our website — customers are encouraged to get in touch for a tailored quote." Black Truffle's model is the opposite of what ranks here.
2. **It shares a URL with a disjoint SERP.** The plan assigns both `ready made meals melbourne` and `home catering melbourne` to `/at-home-catering-melbourne/`. Their top-10 overlap is **0/10** — they are completely different SERPs. One page cannot rank for both.

Black Truffle's "At Home Meals / Re-heat Meals" service (Q10) is real, but it is a caterer's re-heat offering, not a meal-subscription product. Recommend dropping this keyword and replacing it. Better-fitting alternatives to test: `heat at home catering melbourne`, `re heat meals melbourne`, `catering platters melbourne`.

### 3.2 Page mapping errors

**`food catering` → `/corporate-catering/cocktail-party/`.** The SERP is 3/10 deep pages — Google returns general catering homepages (Fabulous, Devour It, Everyday Food, Brisk). This is a homepage-intent head term. Pointing it at a cocktail-party sub-page will not rank. Compounding it, the tracked 50 already aims `Cocktail Party Catering Melbourne`, `Cocktail Food Catering Melbourne` and `Cocktail Finger Food Catering` at that same page. Re-map to the homepage or a general catering page.

**`party catering melbourne` → new `/party-catering-melbourne/` page.** Deep/10 is **0** — every single top-10 result is a homepage. Black Truffle already sits at #7 with its homepage and holds a local pack slot. Creating a dedicated page here works against the observed SERP pattern; the homepage is already the right asset.

**`office catering melbourne cbd` → `/corporate-catering/office/melbourne-cbd/`.** Its SERP overlaps `corporate catering melbourne cbd` by **8/10**, yet the plan builds two separate URLs. Google is treating these as one query. Also, the tracked 50 already contains `Office Catering Melbourne` and `Office Catering`, so a third office page compounds the split. Recommend one `/corporate-catering/melbourne-cbd/` page carrying both, with "office" as a secondary.

### 3.3 Cannibalisation between selections

Top-10 domain overlap across keywords the plan sends to *different* URLs:

| Overlap | Keyword A (URL) | Keyword B (URL) |
|---|---|---|
| **9/10** | home party catering melbourne (`/home-party-catering-melbourne/`) | home catering melbourne (`/at-home-catering-melbourne/`) |
| **8/10** | party catering melbourne (`/party-catering-melbourne/`) | home party catering melbourne |
| **8/10** | party catering melbourne | home catering melbourne |
| **8/10** | corporate catering melbourne cbd | office catering melbourne cbd |
| **8/10** | catering melbourne cbd (`/catering-melbourne-cbd/`) | corporate catering melbourne cbd |
| 7/10 | office catering melbourne cbd | lunch catering melbourne |
| 7/10 | caterers melbourne (`/caterers-melbourne/`) | party catering melbourne |

Keywords 6, 7 and 19 (`party` / `home party` / `home catering`) return 8–9/10 the same domains and are assigned three separate pages. They should be one page, or one page plus a genuinely distinct at-home-meals page. The same applies to 5, 13 and 14 in the CBD cluster.

Also worth noting: `caterers melbourne` (#1) is scheduled as a new `/caterers-melbourne/` page, but its SERP overlaps the homepage-intent cluster by 7/10 and Black Truffle's **homepage already ranks #7** for it. A separate page competes with the client's own strongest asset.

### 3.4 Groupings the SERP data confirms as correct

| Overlap | Grouped onto one page | Verdict |
|---|---|---|
| 6/10 | wedding catering melbourne + wedding caterers melbourne → `/wedding-catering-melbourne/` | ✅ correct |
| 5/10 | afternoon tea catering + catering morning tea → `/morning-afternoon-tea-catering-melbourne/` | ✅ correct |
| 5/10 | vegan + gluten free → `/dietary-catering-melbourne/` | ⚠️ borderline — see below |

**On the dietary pair:** 5/10 overlap is right at the threshold, and the competitor evidence points the other way. Elizabeth Andrews, Brisk, Blakeaway and Nosh each run a *separate* vegan page and a *separate* gluten-free page, and those separate pages are what rank. `gluten free catering melbourne` is 10/10 dedicated pages. Recommend splitting into `/vegan-catering-melbourne/` and `/gluten-free-catering-melbourne/` rather than one combined dietary page.

### 3.5 Google Business Profile gap

Black Truffle holds a local pack slot on the **private/event** terms — `wedding catering melbourne`, `wedding caterers melbourne`, `party catering melbourne`, `birthday party catering melbourne` — and on **none** of the corporate terms: `caterers melbourne`, `catering melbourne cbd`, `corporate catering melbourne cbd`, `office catering melbourne cbd`, `lunch catering melbourne`. Competitors Nosh and Brisk hold those slots repeatedly.

That is a GBP category/service configuration issue, not a keyword issue, but it directly caps the corporate keywords this package is built on. Outside the scope of a keyword plan — flagged for the client.

---

## 4. Compliance against the client form (`P4SJ9rz7`)

### 4.1 Services (Q10) — coverage

| Service listed by client | Covered by | Status |
|---|---|---|
| At Home Meals / Re-heat Meals | 19 home catering melbourne, 20 ready made meals melbourne | ⚠️ #20 rejected — service is now thinly covered |
| Corporate Catering (drop-off, boardroom, meal boxes) | 13, 14, 15 + 40 of the tracked 50 | ✅ Strong |
| Full-Service Catering (on-site, staff, equipment) | — | ❌ **No keyword targets this** |
| Functions & Events (private parties, weddings, cocktail/canapé) | 2, 3, 6, 7, 8, 17, 18 | ✅ Strong |
| Morning & Afternoon Teas, Lunches, Plated Boardroom Meals | 11, 12, 15 | ✅ Covered |
| Specific Food Packages (canapés, finger food, platters, beverages) | 17, 18 | ⚠️ Platters and beverages unaddressed |

Two gaps against the client's own service list: **Full-Service Catering** (their stated differentiator in Q8 — "one experienced team managing the food, beverages, equipment, staffing and coordination") has no keyword at all, and **platters** has none. The tracked 50 includes `Full Service Catering`, so the term is at least monitored, but the highest-margin service line gets no new demand capture in this package.

### 4.2 Keyword preferences (Q11) — the client named four

| Client's stated preference | Status |
|---|---|
| "Lunch catering in Melbourne" | ✅ #15 `lunch catering melbourne` — direct match |
| "Best caterers in Melbourne" | ✅ #1 `caterers melbourne`, with `best caterers melbourne` (110/mo) as a listed secondary |
| "Melbourne catering companies" | ✅ Already in the tracked 50 as `Catering Companies Melbourne` — correctly excluded as a duplicate |
| "cocktail function catering" | ✅ Covered by the tracked 50 (`Cocktail Party Catering`, `Cocktail Catering Melbourne`, `Cocktail Function`-adjacent, 6 cocktail terms total) |

All four client-nominated terms are accounted for across the combined 70. Good.

### 4.3 Target locations (Q12) — the significant gap

The client named 14 areas: Melbourne CBD, East/South/North/West Melbourne, Docklands, Richmond, South Yarra, Carlton, Collingwood, Abbotsford, St Kilda, Fitzroy, Parkville.

Only **Melbourne CBD** is targeted (#5, #13, #14). The other **13 suburbs have zero coverage**, because `config.json` was set to `location_keywords: 0` / `keyword_type: general_only`.

This is a defensible package decision — Black Truffle is a delivery business with one facility, not a multi-location operator, and suburb pages for a caterer are weak. But it is a direct divergence from what the client asked for in Q12 and should be explained to them rather than left silent. If they push back, the inner-north/inner-east suburbs (Richmond, South Yarra, Carlton, Fitzroy) are the only ones with plausible standalone demand.

### 4.4 Ideal customer (Q9) — balance check

Q9 names three groups: corporate/CBD/government/university, private individuals (birthdays, anniversaries, retirements), and residential re-heat meals.

- Corporate: #13, 14, 15, plus 11, 12, 16 skewing corporate in their SERPs ≈ **6/20 (30%)** — matches the Phase 0 allocation of 30% corporate ✅
- Private events: #2, 3, 6, 7, 8, 17, 18 ≈ **7/20 (35%)** ✅
- Residential re-heat: #19, #20 — and #20 is rejected, leaving **1/20** ⚠️
- General/head: #1, 4, 5 ✅

The residential at-home segment is the weak leg and gets weaker once #20 is dropped.

### 4.5 Other form claims

- **Q13** (6,000 deliveries/functions per year, 1,000+ companies) supports competing on head terms and local pack — consistent with the selection ✅
- **Q7 / Q16** (dietary requirement management, allergen management, HACCP) substantiates #9 and #10, even though dietary is not a named service line in Q10 ✅ — the claim is supportable, so these keywords are legitimate
- **Q14** (no published pricing) is the direct reason #20 fails, and is worth remembering for any future "cheap" / "price" / "cost" modifiers — those SERPs reward published pricing
- **Q5 / Q14** (deliveries from 7:30am) supports #16 `breakfast catering melbourne`, which is otherwise not a named service in Q10 ✅

---

## 5. Recommended changes

| Priority | Action |
|---|---|
| 1 | **Drop #20 `ready made meals melbourne`.** Replace with a re-heat/platter term that returns a catering SERP. |
| 2 | **Merge 6 / 7 / 19** (`party` / `home party` / `home catering melbourne`) into one page — 8–9/10 SERP overlap. |
| 3 | **Merge 13 / 14** into `/corporate-catering/melbourne-cbd/` — 8/10 overlap, and `Office Catering Melbourne` is already tracked. |
| 4 | **Re-map #4 `food catering`** off `/corporate-catering/cocktail-party/` and onto the homepage or a general catering page — the SERP is homepage-intent. |
| 5 | **Split the dietary page** into separate vegan and gluten-free pages — every ranking competitor runs them separately, and GF is 10/10 dedicated pages. |
| 6 | **Reconsider #1 and #6 as new pages** — the homepage already ranks #7 for both and their SERPs are homepage-dominated. |
| 7 | **Add a keyword for Full-Service Catering** — the client's stated differentiator has no coverage. |
| 8 | **Raise the Q12 suburb gap with the client** — explain why 13 of their 14 named areas are not targeted. |
| 9 | **Raise the GBP gap** — no local pack presence on any corporate term, which caps the package's core segment. |

---

*Raw SERP payloads: `research/v1/live-serp-2026-07-31/serp-<keyword>.json` (20 files, full top-20 organic + local pack + SERP features).*
