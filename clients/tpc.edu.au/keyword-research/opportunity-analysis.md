# The Performance College (tpc.edu.au) — Keyword Opportunity Analysis

**Date:** 16 July 2026
**Brief:** Reduce the 69-location grid; test the client's requested keyword list for viability; map to the live site; decide category-page vs course-page vs new-page.
**Data:** Google Ads search volume (Australia) + KD from pipeline + live Google SERP checks (Melbourne), 16 Jul 2026.

---

## 1. Live site — what already exists (so we optimise, not rebuild)

**Course pages (already live):**
- `/certificate-in-child-care/` — Cert III childcare (domestic)
- `/certificate-iii-in-early-childhood-education-and-care-online-course/` — **Cert III childcare ONLINE** ✅
- `/diploma-of-early-childhood-education-and-care/` — Diploma ECEC
- `/diploma-of-early-childhood-education-and-care-online-course/` — **Diploma ECEC ONLINE** ✅
- `/certificate-iii-in-individual-support-ageing-and-disability/` — Individual Support (aged care + disability)
- `/diploma-of-community-services/`, `/diploma-of-leadership/`, `/advanced-diploma-of-leadership-management/`, `/graduate-diploma-of-management/`

**Category / hub pages (already live):**
- `/courses/international/` — **international-students hub** ✅
- `/courses/domestic/` — domestic hub
- `/agents/` — education-agent page (international recruitment)

**Implication:** the right pages mostly already exist. Most of the opportunity is *optimising existing pages*, not building new ones.

---

## 2. Viability of the requested keywords (real volumes)

### 🟢 Cluster A — ONLINE courses = the biggest win, and pages already exist
| Keyword | Vol/mo | KD | SERP verdict |
|---|---|---|---|
| online childcare course / childcare course online | **1,000** | 11 | **Page 1 is ALL private RTOs** (Suzan Johnston, Chelsea, Kirana, Selmar, Practical Outcomes) — **no TAFE wall → VIABLE** |
| certificate 3 childcare online | **720** | 8 | private-RTO SERP |
| early childhood education online course | **480** | ~7 | MEDIUM comp (index 58) |
| diploma of early childhood education online | **390** | 7 | private-RTO SERP |

~2,600/mo combined, winnable, and TPC **already has both online course pages**. This is the highest-ROI move on the whole account and it's currently under-optimised. → **Optimise the two existing `-online-course` pages** (title/H1/body around "online childcare course", trainer support, self-paced, placement).

### 🟢 Cluster B — DISABILITY / SUPPORT WORKER = largest aggregate demand, maps to one existing page
| Keyword | Vol/mo | Comp | Notes |
|---|---|---|---|
| support worker course | **1,900** | HIGH | national head |
| individual support course | **1,600** | HIGH | national head |
| disability support worker course | **1,600** | HIGH | disability-specific intent |
| chc33021 | **880** | MEDIUM (index 37) | **SERP mixed — private RTOs Intercare/IHNA/chc33021.com.au reachable → winnable** |
| disability support course | **390** | HIGH | |
| chc33021 certificate iii in individual support | **320** | MEDIUM | formal title |
| support worker course melbourne / disability support course melbourne | 10 / <10 | — | Melbourne-qualified versions have ~no volume; target the national heads instead |

~5,000/mo aggregate, all one qualification (CHC33021). "chc33021" specifically is the most winnable big term (MEDIUM, index 37; PAA questions available for FAQ schema). → **Optimise `/certificate-iii-in-individual-support-ageing-and-disability/`** for chc33021 + individual support + support worker.
**Architecture decision (client call):** the disability-specific terms (disability support worker course 1,600 + disability support course 390 ≈ 2,000/mo) are a *distinct intent* from aged care, even though it's the same course code. Option to spin up **one dedicated "Disability Support Worker Course Melbourne" landing page** to own that intent, keeping the aged-care angle on the existing page. Same-qualification, so only do this if they want to compete hard on the disability angle — otherwise one strong dual-angle page.

### 🟡 Cluster C — INTERNATIONAL STUDENTS = low volume, high commercial value, hub exists
| Keyword | Vol/mo | Comp | CPC |
|---|---|---|---|
| certificate 3 in childcare for international students | 40 | HIGH | $4.70 |
| childcare course for international students | 20 | HIGH | $4.46 |
| diploma in childcare for international students | 10 | HIGH | $1.89 |
| childcare courses in melbourne for international students | <10 | — | — |

Volume is small **but HIGH competition + high CPC = high-value commercial intent** (international students pay full fees). Related searches confirm the overlap ("online childcare courses in Australia for international students", "CHC33021 cricos"). → **Do NOT build per-course international pages** (too little volume each). Instead: **strengthen `/courses/international/` as the international hub** (target the "…for international students" cluster) + add an **"International students" block to each course page** (CRICOS code, fees, intakes, English/entry requirements). Leverage the existing `/agents/` page.

### 🟡 Cluster D — "Study … Melbourne" = secondaries, not new pages
| Keyword | Vol/mo | Verdict |
|---|---|---|
| study childcare | 170 | secondary on Cert III childcare page |
| study childcare melbourne | 110 | **same volume + SERP as "childcare courses melbourne"** → same page, secondary |
| study individual support melbourne / study childcare diploma melbourne / study diploma of early childhood education melbourne | <10 each | drop / minor secondary |

### Melbourne-qualified heads — keep the strong ones only
| Keyword | Vol/mo | Comp | Keep? |
|---|---|---|---|
| aged care course melbourne | 320 | MEDIUM (62) | ✅ primary (already selected) |
| early childhood course melbourne | 110 | HIGH | ✅ add — decent volume |
| childcare courses melbourne | 110 | HIGH | ✅ primary (already selected) |
| certificate iii in early childhood education and care melbourne | 40 | MEDIUM (41) | secondary |
| aged care training melbourne | 20 | HIGH | secondary |
| early childhood education course melbourne / childcare training melbourne / diploma of childcare melbourne | 10 | — | secondary |
| childcare qualification melbourne / childcare certificate melbourne / study individual support melbourne | <10 | — | drop |
| diploma in early childhood education australia | 50 | MEDIUM (58) | national — future, as DA grows |

---

## 3. Reducing the location grid (the ask)
The 69-page grid (3 silos × 23 suburbs) is not viable: **only 6/23 suburbs have any demand** — Geelong 40, Werribee 30, Dandenong 20, Bendigo/Frankston/Pakenham 10; the other 17 are zero. **`childcare course hoppers crossing` = <10.**

**Recommendation:** cut the grid from 69 → **at most ~6–9 pages**: only the suburbs with measured demand (**Geelong, Werribee, Dandenong**, optionally Bendigo/Frankston/Pakenham), and only for the **childcare** and **aged-care** silos (skip the long "diploma of early childhood education and care {suburb}" silo — zero demand, longest URLs, highest duplicate-content risk). Reinvest the freed capacity into Clusters A–C above, which have **10–100× the real demand.**

---

## 4. Page-architecture answer (category vs course vs new)
| Need | Page type | Action |
|---|---|---|
| Online childcare / ECEC | **existing course pages** (`-online-course`) | Optimise — highest ROI |
| chc33021 / support worker / individual support | **existing course page** | Optimise |
| Disability-support-worker intent (~2,000/mo) | **optional 1 NEW landing page** | Client decision — same qual, distinct intent |
| International students | **existing category hub** `/courses/international/` + on-page sections | Optimise hub, add CRICOS blocks per course |
| Study … Melbourne, Melbourne heads | **existing course pages** | Add as secondaries |
| Suburb pages | reduce 69 → ~6–9 | Keep only demand suburbs (Geelong/Werribee/Dandenong), 2 silos |

**Net:** ~1 possible new page (disability), everything else is optimisation of pages that already exist + a big location cut.

---

## Data notes
- All volumes = Google Ads, Australia, pulled 16 Jul 2026. Melbourne-suffixed terms are genuinely low; national/online terms carry the volume.
- SERP checks (Melbourne): "online childcare course" = private-RTO SERP (no TAFE wall); "chc33021" = mixed TAFE + reachable private RTOs.
- Pipeline confirmed 80% of course SERPs trigger AI Overviews → every optimised page needs Course + FAQ schema and PAA answers.
