---
name: Meta Titles & Descriptions
description: Full process and rules for auditing and writing optimised meta titles and descriptions for any client website
type: capability
---

# Capability: Meta Titles & Descriptions

## Goal
Improve CTR and rankings by writing meta titles and descriptions that match SERP intent signals, include verified differentiators, and follow technical length constraints.

---

## Meta Title Rules

### Format
```
Primary Keyword | Differentiator | Brand Name
```
- Separator between sections: ` | ` (pipe with spaces) — never ` - ` (dash)
- Brand at end, always
- Primary keyword first — exactly as searched

### Length target
- 50–65 characters
- Anything 66+ risks truncation in Google

### What to include
- Primary keyword (exact or close variant)
- One urgency/trust signal (24/7, Emergency, Fast, Licensed)
- Brand name at end

### What to avoid
- Superlatives: "Best", "Top", "Leading", "#1" — Google rewrites these
- Unicode symbols (▷, ★, etc.)
- Repeating the keyword in both keyword slot AND differentiator slot
- Long pipe chains e.g. "| Door & Window Locks | Mobile Locksmith" (adds chars, dilutes signal)
- Lowercase brand signals in pipe sections

### Common existing title problems to fix
| Problem | Fix |
|---|---|
| 80-85 chars from long pipe chains | Replace chain with single differentiator |
| Unicode arrow ▷ | Remove |
| Lowercase "mobile locksmith [suburb]" in pipe | Capitalise or replace |
| Missing brand name | Add "| Brand Name" at end |
| Superlative in title | Rewrite without it |
| ` - Brand` separator | Replace with ` | Brand` |

---

## Meta Description Rules

### Format (service/local pages)
```
[Action opener + service summary]. [Differentiator]. [Phone] for a free quote.
```

### Format (suburb/location pages — template)
```
Need a locksmith in [Suburb]? [Brand] offers 24/7 emergency lockouts & repairs. Fast 30-min arrival. Call [phone] for a free quote.
```

### Length target
- 140–160 characters
- Anything 270+ chars will be truncated — rewrite from scratch

### What to include
- Action-oriented opener (question or imperative)
- 24/7 availability (if verified on site)
- Arrival time / response time (if claimed on site)
- Phone number
- "free quote" CTA (if offered on site)

### What to avoid
- Repeating the title verbatim
- Generic filler ("We are the leading...")
- No CTA or phone number
- Narrative/passive descriptions ("Concerned about the safety of your loved ones...")

---

## Differentiators to include when verified

Before using any claim, verify it exists on the live site (crawl or browse). Do not invent claims.

| Claim | Where to verify |
|---|---|
| 24/7 | Homepage or service pages |
| Mobile locksmith | About or service pages |
| 30-min arrival | Homepage or service pages |
| Free quote | CTAs on site |
| 20+ years experience | About page |
| Licensed & insured | About or footer |
| Master Locksmiths accredited | About page or badges |
| 12-month warranty | Service pages |
| 5-star rated | Review widgets or Google rating |

---

## SERP Pattern Analysis — Locksmith Industry (AU)

Key patterns from top-ranking competitors across 16 Australian keywords:
- "24/7 emergency" — near-universal signal
- "within 30 minutes" or "fast 30-min arrival" — used by top-3 results
- "mobile" — universal
- "licensed" — strong trust signal
- "free quote" — universal CTA
- "residential, commercial & emergency" — common service summary pattern
- Emergency framing outperforms generic framing for CTR

---

## Service Page Descriptions — Global Locksmiths Templates

These include 12-month warranty as a CTR differentiator (no competitor uses this):

- **/safes/**: "Expert safe supply & installation in Melbourne for homes & businesses. High-security safes, 12-month warranty, 20+ years experience. Call [phone] for a free quote."
- **/digital-locks/**: "Upgrade your home security with digital & smart door locks. Keyless entry & fingerprint locks installed across Melbourne. 12-month warranty. Call [phone]."
- **/rekeying-locks/**: "Need your locks rekeyed in Melbourne? Fast, affordable rekeying — new homes, lost keys or extra security. 12-month warranty. Call [phone] for a free quote."
- **/commercial-door-locks/**: "Secure your business with commercial-grade door locks. Supply & install for offices, shopfronts & warehouses. 12-month warranty. Call [phone]."
- **/locks-in-general/**: "Expert lock repair, installation & rekeying across Melbourne. Licensed 24/7 mobile locksmiths, 20+ years experience. 12-month warranty. Call [phone]."

---

## Suburb/Location Page Templates

### Title
```
Locksmith [Suburb] | Fast 24/7 Mobile | [Brand]
```

### Description
```
Need a locksmith in [Suburb]? [Brand] offers 24/7 emergency lockouts & repairs. Fast 30-min arrival. Call [phone] for a free quote.
```

---

## Region Hub Page Templates

### Title
```
Locksmith [Region] Melbourne | 24/7 | [Brand]
```

### Description
```
Need a locksmith in Melbourne's [Region] Suburbs? [Brand] offers 24/7 emergency lockouts, repairs & installations. Fast 30-min arrival. Call [phone].
```

---

## Audit Process (how to run this for a new client)

1. **Crawl all pages** — extract URL, current title, current description for all pages
2. **Group by page type**: homepage, service pages, location/suburb pages, hub/region pages, other
3. **Run SERP analysis** via DataForSEO on 10–20 core keywords — identify top wording patterns used by ranking competitors
4. **Verify claims** against live site — browse or crawl to confirm every differentiator before including it
5. **Identify primary keyword** for each page — map to the most likely target query
6. **Write new titles**: primary keyword first | differentiator | brand
7. **Write new descriptions**: action opener + verified differentiators + phone + CTA
8. **QA checklist**:
   - All titles 50–65 chars
   - All descriptions 140–160 chars
   - No titles using dash before brand (should be pipe)
   - No superlatives
   - No unicode symbols
   - All missing descriptions filled
   - Brand name present on every title
9. **Output format** — `.txt` file with one entry per URL:

```
https://www.example.com/page/
PRIMARY KEYWORD: [keyword]
CURRENT TITLE:   [existing title]
NEW TITLE:       [new title]
CURRENT DESC:    [existing desc or [MISSING]]
NEW DESC:        [new description]
---
```

10. **Commit to client folder**: `clients/[domain]/meta-tags/meta-tags-update.txt`

---

## Notes from globallocksmiths.com.au audit (May 2026)

- 90 pages total: homepage, 5 service pages, 5 hub/region pages, 79 suburb pages
- 7 pages had missing descriptions — filled from scratch
- ~22 titles were 80-85 chars from "| Door & Window Locks | Mobile Locksmith" pattern — replaced with "| Fast 24/7 Mobile"
- 3 titles missing brand — added
- Suburb pages used lowercase keyword in pipe — fixed
- 2 descriptions were 270+ chars (Albert Park, Spotswood) — replaced
- Business hours showed Mon-Fri 9-5 on site but 24/7 confirmed as valid claim by client
- 12-month warranty added to 5 service page descriptions — unused differentiator, no competitor uses it
