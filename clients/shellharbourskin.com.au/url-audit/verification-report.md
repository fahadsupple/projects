# URL Redirect & Meta Verification Report — shellharbourskin.com.au

**Date:** 2026-04-16  
**Pages checked:** 86  
**Method:** curl redirect checks (no-follow, max-redirs 0) + live meta extraction via curl -L

---

## 1. Executive Summary

| Check | Pass | Fail | Notes |
|---|---|---|---|
| Redirects (301/302) | 86 | 0 | All old URLs redirect correctly |
| Meta Titles | 85 | 1 | 1 title mismatch |
| Meta Descriptions | 85 | 1 | 1 description minor difference (double space) |

**Overall:** 84 pages fully passing. 1 page has a title mismatch. 1 page has a minor description whitespace issue.

---

## 2. Redirect Failures

**None.** All 86 old URLs return a 301 redirect pointing to the correct new URL.

---

## 3. Meta Title Failures

| # | New URL | Expected Title | Actual Live Title |
|---|---|---|---|
| 84 | https://shellharbourskin.com.au/treatment-services/thread-consultations/lifting-threads/ | Consultations for Skin Tension \| Shellharbour Skin | Non-Surgical Lifting Consultations – Shellharbour Skin |

**Note:** The live title appears to be old/unconverted content. The page exists and redirects correctly, but the meta title has not been updated to match the specified value.

---

## 4. Meta Description Failures

| # | New URL | Expected Description | Actual Live Description |
|---|---|---|---|
| 85 | https://shellharbourskin.com.au/treatment-services/hifu-ultrasound-consultations/ | "...non-invasive ultrasound approaches for skin firmness..." | "...non-invasive ultrasound  approaches for skin firmness..." (double space between "ultrasound" and "approaches") |

**Note:** This is a minor whitespace issue — the content is otherwise identical. A double space in the meta description will not affect ranking but may display oddly in SERPs. Worth a quick fix.

---

## 5. Fully Passing Pages (84 of 86)

All redirects correct AND meta title AND meta description match for the following pages:

1. https://shellharbourskin.com.au/why-skin-quality-and-volume-change/
2. https://shellharbourskin.com.au/lip-volume-consultation/
3. https://shellharbourskin.com.au/skin-quality-consultations-nurse-amanda/
4. https://shellharbourskin.com.au/wrinkle-consultations-albion-park/
5. https://shellharbourskin.com.au/wrinkle-consultations-berry/
6. https://shellharbourskin.com.au/wrinkle-consultations-bomaderry/
7. https://shellharbourskin.com.au/wrinkle-consultations-corrimal/
8. https://shellharbourskin.com.au/wrinkle-consultations-dapto/
9. https://shellharbourskin.com.au/wrinkle-consultations-fairy-meadow/
10. https://shellharbourskin.com.au/wrinkle-consultations-kiama/
11. https://shellharbourskin.com.au/wrinkle-consultations-mittagong/
12. https://shellharbourskin.com.au/wrinkle-consultations-moss-vale/
13. https://shellharbourskin.com.au/wrinkle-consultations-nowra/
14. https://shellharbourskin.com.au/wrinkle-consultations-warilla/
15. https://shellharbourskin.com.au/wrinkle-consultations-wingecarribee/
16. https://shellharbourskin.com.au/wrinkle-consultations-wollongong/
17. https://shellharbourskin.com.au/wrinkle-consultations-woonona/
18. https://shellharbourskin.com.au/facial-volume-consultations-albion-park/
19. https://shellharbourskin.com.au/facial-volume-consultations-berry/
20. https://shellharbourskin.com.au/facial-volume-consultations-bomaderry/
21. https://shellharbourskin.com.au/facial-volume-consultations-corrimal/
22. https://shellharbourskin.com.au/facial-volume-consultations-dapto/
23. https://shellharbourskin.com.au/facial-volume-consultations-fairy-meadow/
24. https://shellharbourskin.com.au/facial-volume-consultations-kiama/
25. https://shellharbourskin.com.au/facial-volume-consultations-mittagong/
26. https://shellharbourskin.com.au/facial-volume-consultations-moss-vale/
27. https://shellharbourskin.com.au/facial-volume-consultations-nowra/
28. https://shellharbourskin.com.au/facial-volume-consultations-warilla/
29. https://shellharbourskin.com.au/facial-volume-consultations-wingecarribee/
30. https://shellharbourskin.com.au/facial-volume-consultations-wollongong/
31. https://shellharbourskin.com.au/facial-volume-consultations-woonona/
32. https://shellharbourskin.com.au/lip-volume-albion-park/
33. https://shellharbourskin.com.au/lip-volume-berry/
34. https://shellharbourskin.com.au/lip-volume-bomaderry/
35. https://shellharbourskin.com.au/lip-volume-corrimal/
36. https://shellharbourskin.com.au/lip-volume-dapto/
37. https://shellharbourskin.com.au/lip-volume-fairy-meadow/
38. https://shellharbourskin.com.au/lip-volume-kiama/
39. https://shellharbourskin.com.au/lip-volume-mittagong/
40. https://shellharbourskin.com.au/lip-volume-moss-vale/
41. https://shellharbourskin.com.au/lip-volume-nowra/
42. https://shellharbourskin.com.au/lip-volume-warilla/
43. https://shellharbourskin.com.au/lip-volume-wingecarribee/
44. https://shellharbourskin.com.au/lip-volume-wollongong/
45. https://shellharbourskin.com.au/lip-volume-woonona/
46. https://shellharbourskin.com.au/skin-cancer/skin-cancer-surgery/topical-management/
47. https://shellharbourskin.com.au/skin-cancer/skin-cancer-surgery/non-surgical-options/
48. https://shellharbourskin.com.au/skin-concerns/lip-shape-and-volume/
49. https://shellharbourskin.com.au/skin-concerns/fine-lines-and-wrinkles/
50. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/
51. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/wrinkle-lines/
52. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/skin-volume/
53. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/skin-volume/hydration-structure/
54. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/skin-volume/structure-support/
55. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/skin-volume/nutrient-infusion/
56. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/skin-volume/skin-resilience/
57. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/skin-volume/full-face-skin-resilience/
58. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/skin-volume/under-eye-skin-quality/
59. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/skin-volume/scar-texture/
60. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/skin-volume/gradual-volumising/
61. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/skin-volume/hydration-texture/
62. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/
63. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/cheek-concerns/
64. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/chin-definition/
65. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/filler-reversal/
66. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/ultrasound-guided-reversal/
67. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/jawline-shaping/
68. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/lip-shape-volume/
69. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/marionette-lines/
70. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/smile-lines/
71. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/nose-area-concerns/
72. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/tear-trough/
73. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/temple-area-concerns/
74. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/perioral-lines/
75. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/facial-volume/volume-support/
76. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/skin-regeneration/
77. https://shellharbourskin.com.au/treatment-services/aesthetic-consults/lower-face-concerns/
78. https://shellharbourskin.com.au/treatment-services/medical-procedures/keloid-and-scar-consults/
79. https://shellharbourskin.com.au/treatment-services/medical-procedures/topical-skin-cancer-treatments/field-directed-therapy/
80. https://shellharbourskin.com.au/treatment-services/microneedling/nutrient-infused-needling/
81. https://shellharbourskin.com.au/treatment-services/microneedling/resilience-booster-needling/
82. https://shellharbourskin.com.au/treatment-services/thread-consultations/mono-threads/
83. https://shellharbourskin.com.au/treatment-services/thread-consultations/
84. ~~https://shellharbourskin.com.au/treatment-services/thread-consultations/lifting-threads/~~ *(title fail — see section 3)*
85. ~~https://shellharbourskin.com.au/treatment-services/hifu-ultrasound-consultations/~~ *(description whitespace — see section 4)*
86. https://shellharbourskin.com.au/what-is-a-cosmetic-nurse/

---

## Action Items

| Priority | Page | Fix Required |
|---|---|---|
| High | `/treatment-services/thread-consultations/lifting-threads/` | Update meta title to: "Consultations for Skin Tension \| Shellharbour Skin" |
| Low | `/treatment-services/hifu-ultrasound-consultations/` | Remove double space in meta description (between "ultrasound" and "approaches") |
