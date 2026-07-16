# The Performance College (tpc.edu.au) — Final Keyword Recommendations

**Date:** 16 July 2026
**Scope:** Revised general keyword set + reduced location set + final page architecture (nested hub-and-spoke).
**Data:** Google Ads search volume (Australia), KD from pipeline, live Google SERP checks + live-site verification, 16 Jul 2026.

---

## 1. Final URL architecture (nested hub-and-spoke)

```
/courses/online/                                  ← HUB (NEW)   → "online courses melbourne"
   ├── /courses/online/childcare/                 ← CATEGORY (NEW) → "online childcare courses"  ⭐ biggest new win
   │      ├── /certificate-iii-in-early-childhood-education-and-care-online-course/  (exists)
   │      └── /diploma-of-early-childhood-education-and-care-online-course/          (exists)
   └── (links to) /certificate-iii-in-individual-support-ageing-and-disability/     (exists, online-delivered)

Existing course pages (optimise, general/Melbourne intent):
   /certificate-in-child-care/
   /diploma-of-early-childhood-education-and-care/
   /diploma-of-community-services/

Existing hub:
   /courses/international/     ← international-students hub

Optional NEW:
   /disability-support-worker-course/   ← distinct disability intent (client decision)
```
- Nesting is fine for ranking — URL depth is not a ranking factor. Keep every page **1–2 clicks from the homepage** via nav + hub + footer links, and add BreadcrumbList schema (`Home › Courses › Online › Childcare`).
- Verified on the live site: TPC delivers Cert III ECEC (CHC30121), Diploma ECEC (CHC50121) **and** Individual Support (CHC33021) as "Online / Zoom Class" — so the online terms are legitimately targetable.

---

## 2. Final general keyword → URL map (priority order)

### ⭐ Tier 1 — new/high-value online pages (build first)

**P1 · `/courses/online/childcare/`** *(NEW category)*
- **Primary:** online childcare courses — **1,000/mo**
- Secondary: study childcare online, online early childhood course, child care course online
- Role: owns the generic online-childcare head; lists + links to the 2 course pages below.

**P2 · `/certificate-iii-in-early-childhood-education-and-care-online-course/`** *(exists)*
- **Primary:** certificate 3 in childcare online — **720/mo**
- Secondary: cert 3 childcare online, online certificate iii in early childhood education and care

**P3 · `/diploma-of-early-childhood-education-and-care-online-course/`** *(exists)*
- **Primary:** diploma of early childhood education online — **390/mo**
- Secondary: early childhood education online course (480), online diploma of early childhood education and care

**P4 · `/certificate-iii-in-individual-support-ageing-and-disability/`** *(exists, online-delivered)*
- **Primary:** chc33021 — **880/mo** (MEDIUM, index 37 — most winnable big care term)
- Secondary (same course, different phrasings): certificate iii in individual support online (1,000), aged care course online (1,000), aged care course melbourne (320), individual support course (1,600), certificate iii in individual support melbourne (90), certificate 3 in individual support ageing and disability (210)

### Tier 2 — general/Melbourne course pages (optimise existing)

**P5 · `/certificate-in-child-care/`** *(exists)*
- **Primary:** childcare courses melbourne — **110/mo**
- Secondary: study childcare melbourne (110), early childhood course melbourne (110), certificate iii in early childhood education and care melbourne (40), childcare training melbourne (10)

**P6 · `/diploma-of-early-childhood-education-and-care/`** *(exists)*
- **Primary:** early childhood diploma melbourne — **70/mo**
- Secondary: diploma in early childhood education australia (50), diploma of childcare melbourne (10), study childcare diploma melbourne

**P7 · `/diploma-of-community-services/`** *(exists)*
- **Primary:** diploma of community services melbourne — **90/mo**
- Secondary: diploma of community services online (~1,300 national, KD~3 per pipeline — strong; confirm delivery), community services course

**P8 · `/courses/online/`** *(NEW hub)*
- **Primary:** online courses melbourne — **140/mo**
- Secondary: nationally recognised online courses (90), online diploma courses (210)
- Role: funnel/hub; links down to the childcare category + individual-support online page. Modest SEO value; do NOT chase "online courses" (6,600) / "online tafe courses" (4,400) — unwinnable at DA 7 + intent/brand mismatch.

### Tier 3 — targeted, optional

**P9 · `/courses/international/`** *(exists hub)*
- **Primary:** childcare course for international students — 20/mo (cluster ~70 with cert 3 / diploma variants)
- Low volume but high commercial value (full-fee, HIGH comp, CPC $4.70). Add **CRICOS code + international fees/intake blocks** to each course page; leverage `/agents/`.

**P10 · `/disability-support-worker-course/`** *(OPTIONAL new page — client decision)*
- **Primary:** disability support worker course — **1,600/mo**
- Secondary: disability support course (390), disability support course online (90, MEDIUM index 59 — lowest-comp online care term)
- Distinct disability intent vs the ageing-led P4 page. Same qualification (CHC33021), so only build if they want to compete hard on the disability angle.

---

## 3. Location keywords — cut 69 → 6 (max 9)

Only 6/23 suburbs have any measured demand; `childcare course hoppers crossing` = <10. **Drop the entire "diploma of early childhood education and care {suburb}" silo** (zero demand, longest slugs, highest duplicate-content risk).

**Keep (real demand only), 2 silos × 3 suburbs = 6 pages:**
| Suburb | childcare course {suburb} | aged care course {suburb} |
|---|---|---|
| Geelong (40) | ✅ | ✅ |
| Werribee (30) | ✅ | ✅ |
| Dandenong (20) | ✅ | ✅ |

**Optional +3** (childcare silo only, 10/mo each): Bendigo, Frankston, Pakenham.

Build these as **genuine local landing pages** (campus access, transport, local placement partners) — not thin doorway duplicates — or don't build them at all.

---

## 4. Internal linking
- Main nav "Courses" → Online (hub) → Childcare (category) → 2 course pages.
- `/courses/online/childcare/` links to both online course pages; each online course page links **up** to the category and **across** to its classroom twin.
- `/courses/online/` links down to the childcare category + the Individual-Support-online page (topical clustering via links, not URL nesting).
- Kept location pages link up to their course pillar (childcare/aged-care).

## 5. Build caveats
1. **Code discrepancy — confirm with client:** live site uses **CHC30121 / CHC50121**; onboarding form lists **CHC30125 / CHC50125** (2025 codes). Affects exact-match targets + Course schema.
2. **AI Overviews on 80% of these SERPs** — every page needs Course + FAQ schema and PAA answers; ranking #1 alone won't guarantee the click.
3. **Avoid these modifiers:** geo on national/online heads (kills volume — "online childcare course melbourne" = 10); "free"/"government funded" (intent mismatch for a fee RTO — handle as an FAQ only).
4. **Confirm online delivery for Community Services** before targeting "diploma of community services online".

## 6. Summary
- **9 general primaries + 1 optional** (up from the original 5), anchored by the new nested online cluster.
- Biggest new wins: **online childcare courses (1,000)** on the new category page, and the **CHC33021 / online care cluster (~2,000+)** on the existing Individual Support page.
- **Location: 69 → 6** pages (demand suburbs, 2 silos), freeing effort for the online clusters that carry 10–100× the real demand.
