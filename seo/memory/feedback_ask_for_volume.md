---
name: Always ask for GKP data when needed
description: When GKP data is missing or insufficient to make a keyword decision, ask the user to run specific terms in Google Keyword Planner before deciding
type: feedback
---

Always ask the user to run specific keywords in Google Keyword Planner when:
- A keyword is SERP-validated but has no volume data in the files provided
- The provided GKP files may have gaps (e.g. only broad terms were searched, not Melbourne-modified variants)
- A decision (add vs reject a keyword/page) hinges on volume or bid data that isn't available

**Why:** The user provides GKP files but they may not cover every term needed. Rather than making decisions with incomplete data or rejecting keywords purely because they weren't in the file, ask for the specific terms to search. This leads to better, data-backed decisions.

**How to apply:** When you identify a gap in GKP coverage, list the exact keywords you need searched and ask the user to run them before finalising the recommendation. Don't guess or extrapolate from related terms if the specific term matters.
