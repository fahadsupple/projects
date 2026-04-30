---
name: FAQ Review Capability
description: How to perform FAQ review for content pages — count existing questions, write additional Q&As to reach 8 per page, save as text file
type: feedback
---

# FAQ Review Capability

## What it does
Reviews content pages in a document, counts existing FAQ questions per page, writes additional Q&As to bring each page to exactly 8 questions, and saves output as a text file.

## Process
1. Parse the document — identify each page by page number, URL, primary keyword
2. Count existing FAQ questions under each page's H2: Frequently Asked Questions section
3. For each page that has fewer than 8, write additional Q&As to reach exactly 8
4. Save a text file at: `clients/[domain]/content/faq-additions.txt`
5. Update MEMORY.md and push to GitHub

## Writing rules for new Q&As
- Match the exact tone and style of the existing Q&As on that page
- Questions must add genuine visitor value — answer what someone visiting that specific page would actually ask
- Use location-specific references where the page has a geographic focus (Sydney suburbs, landmarks, commute references)
- Draw on confirmed client facts only (USPs, hours, services, delivery times, warranty — from client memory file)
- Do not invent services, policies or products not confirmed in client memory
- Mark new Q&As clearly as "NEW ADDITIONS" in the output file
- Keep answers concise but complete — typically 2–4 sentences

## Output file format
```
PAGE [number]
URL: [full URL]
Primary keyword: [keyword]
----------------
EXISTING ([count]):
Q1: ...
A: ...

NEW ADDITIONS ([count]):
Q5: ...
A: ...
```

## Good question types for furniture/local pages
- Distance/travel time to showroom
- Assembly and installation services
- Warranty terms
- Buying individual vs. full sets
- Weekend/after-hours access
- Accessibility (NDIS, lift recliners, mobility)
- Price Beat Guarantee mechanics
- Delivery coordination for apartments/high-rise
- Upholstery/material options
- Stock availability / lead times

**Why:** Consistent FAQ depth (8 per page) improves E-E-A-T signals, supports featured snippet opportunities, and reduces pre-purchase friction for visitors.
