# flourishelc.com.au — "Before & After School Care" Removal Audit
**Date:** 2026-06-16  
**Scope:** 30 pages audited (all location pages + areas-we-serve + homepage + 6 additional nav pages)  
**Issue:** Client does not offer before and after school care (BASC/OSHC). All references must be removed.

---

## Result: 2 Pages Require Edits

---

### PAGE 1: `/areas-we-serve/`
**URL:** https://flourishelc.com.au/areas-we-serve/

**Removals required:**

**1. FAQ accordion item (visible HTML)**
- Question heading: `"Do you offer before and after school care?"`
- Answer body: `"While our primary focus is early learning for children under school age, some locations offer holiday care programs. Contact your preferred centre to discuss specific service offerings in your area."`
- Remove the entire accordion item (question + answer block)

**2. FAQ JSON-LD schema (in `<script type="application/ld+json">`)**
- Remove this entry from the FAQPage schema:
```json
{
  "@type": "Question",
  "name": "Do you offer before and after school care?",
  "acceptedAnswer": {
    "@type": "Answer",
    "text": "While our primary focus is early learning for children under school age, some locations offer holiday care programs. Contact your preferred centre to discuss specific service offerings in your area."
  }
}
```

---

### PAGE 2: `/daycare-childcare-bateman-wa/`
**URL:** https://flourishelc.com.au/daycare-childcare-bateman-wa/

**Removals required:**

**1. FAQ accordion item (visible HTML)**
- Question heading: `"Do you offer before and after school care?"`
- Answer body: `"Currently, we specialise in full-day early learning programs. However, we maintain strong relationships with local OSHC providers and can recommend quality services for your ongoing needs after your child starts school."`
- Remove the entire accordion item (question + answer block)
- Note: answer body also contains the term **OSHC** — this must be removed too

**2. FAQ JSON-LD schema (in `<script type="application/ld+json">`)**
- Remove this entry from the FAQPage schema:
```json
{
  "@type": "Question",
  "name": "Do you offer before and after school care?",
  "acceptedAnswer": {
    "@type": "Answer",
    "text": "Currently, we specialise in full-day early learning programs. However, we maintain strong relationships with local OSHC providers and can recommend quality services for your ongoing needs after your child starts school."
  }
}
```

---

## All Pages Audited

| # | URL | Clean? |
|---|-----|--------|
| 1 | https://flourishelc.com.au/ (homepage) | ✅ Clean |
| 2 | https://flourishelc.com.au/areas-we-serve/ | ❌ **Fix required** |
| 3 | https://flourishelc.com.au/daycare-childcare-oakville-nsw/ | ✅ Clean |
| 4 | https://flourishelc.com.au/daycare-childcare-box-hill-nsw/ | ✅ Clean |
| 5 | https://flourishelc.com.au/daycare-childcare-vineyard-nsw/ | ✅ Clean |
| 6 | https://flourishelc.com.au/daycare-childcare-gables-nsw/ | ✅ Clean |
| 7 | https://flourishelc.com.au/daycare-childcare-grantham-farm-nsw/ | ✅ Clean |
| 8 | https://flourishelc.com.au/daycare-childcare-riverstone-nsw/ | ✅ Clean |
| 9 | https://flourishelc.com.au/daycare-childcare-mulgrave-nsw/ | ✅ Clean |
| 10 | https://flourishelc.com.au/preschool-oakville-nsw/ | ✅ Clean |
| 11 | https://flourishelc.com.au/preschool-box-hill-nsw/ | ✅ Clean |
| 12 | https://flourishelc.com.au/preschool-vineyard-nsw/ | ✅ Clean |
| 13 | https://flourishelc.com.au/preschool-gables-nsw/ | ✅ Clean |
| 14 | https://flourishelc.com.au/preschool-grantham-farm-nsw/ | ✅ Clean |
| 15 | https://flourishelc.com.au/preschool-riverstone-nsw/ | ✅ Clean |
| 16 | https://flourishelc.com.au/preschool-mulgrave-nsw/ | ✅ Clean |
| 17 | https://flourishelc.com.au/daycare-childcare-bull-creek-wa/ | ✅ Clean |
| 18 | https://flourishelc.com.au/daycare-childcare-leeming-wa/ | ✅ Clean |
| 19 | https://flourishelc.com.au/daycare-childcare-bateman-wa/ | ❌ **Fix required** |
| 20 | https://flourishelc.com.au/daycare-childcare-rossmoyne-wa/ | ✅ Clean |
| 21 | https://flourishelc.com.au/daycare-childcare-shelley-wa/ | ✅ Clean |
| 22 | https://flourishelc.com.au/daycare-childcare-willetton-wa/ | ✅ Clean |
| 23 | https://flourishelc.com.au/daycare-childcare-brentwood-wa/ | ✅ Clean |
| 24 | https://flourishelc.com.au/kindergarten-bull-creek-wa/ | ✅ Clean |
| 25 | https://flourishelc.com.au/kindergarten-leeming-wa/ | ✅ Clean |
| 26 | https://flourishelc.com.au/kindergarten-bateman-wa/ | ✅ Clean |
| 27 | https://flourishelc.com.au/kindergarten-rossmoyne-wa/ | ✅ Clean |
| 28 | https://flourishelc.com.au/kindergarten-shelley-wa/ | ✅ Clean |
| 29 | https://flourishelc.com.au/kindergarten-willetton-wa/ | ✅ Clean |
| 30 | https://flourishelc.com.au/kindergarten-brentwood-wa/ | ✅ Clean |
| 31 | https://flourishelc.com.au/flourish-early-learning-centre-oakville-nsw/ | ✅ Clean |
| 32 | https://flourishelc.com.au/flourish-early-learning-centre-watanobbi-nsw/ | ✅ Clean |
| 33 | https://flourishelc.com.au/flourish-early-learning-bull-creek-wa/ | ✅ Clean |
| 34 | https://flourishelc.com.au/flourish-early-learning-centre-philosophy/ | ✅ Clean |
| 35 | https://flourishelc.com.au/the-curriculum-at-flourish-early-learning-centres/ | ✅ Clean |
| 36 | https://flourishelc.com.au/join-the-team-at-flourish-elc/ | ✅ Clean |

**Total pages audited: 36**  
**Pages requiring fixes: 2**  
**Pages clean: 34**
