# Reconciliation report — live (old) vs new content

**Scope:** 23 pages with live content (20 suburb pages + homepage + house-clean + areas-we-serve). The two service hubs (regular-house-cleaning, luxury-house-cleaning) are new URLs (404 live), so nothing to reconcile there.

**Method:** each live page text was re-fetched and diffed against the new generated page. Deliberate campaign changes were explicitly ignored (rigid price tables → on-quote framing; "Why Choose Us" heading removed; hard review counts → "5-star rated on Google"; End-of-Lease de-emphasis; boilerplate/nav).

## Verdicts
- **CLEAN (2):** black-rock, house-clean
- **MINOR (16):** bentleigh, carnegie, caulfield, cheltenham, elsternwick, gardenvale, hampton, highett, mckinnon, mentone, moorabbin, mordialloc, ormond, parkdale, homepage, areas-we-serve
- **ACTION (5):** aspendale, beaumaris, brighton, murrumbeena, sandringham

**No commercial content, service, or guarantee was lost on any page.** Every new page is materially stronger on pricing clarity, trust ($10M cover, 95% repeat), FAQs and internal linking. The one systematic loss is **per-suburb local colour**: the fresh suburb pages replaced each live page's suburb-specific "local cleaning challenge" and named landmarks with a uniform "same dedicated team + price the home not the hour" positioning. That made the 20 suburb pages read more alike than the live set did.

---

## Category 1 — SAFE to restore now (geographic/architectural FACTS, groundable, improve local SEO + differentiation)
A short per-suburb "local challenge / local colour" paragraph, drawn from verifiable geography and housing stock:

- **Coastal salt-spray / beach sand** (Port Phillip Bay): Aspendale, Beaumaris, Brighton, Hampton, Cheltenham, Sandringham, Parkdale, Gardenvale (western side), Elsternwick
- **Sandbelt dust:** Highett, Moorabbin, Cheltenham
- **Street-tree pollen / leafy-suburb allergen load** (Plane/Eucalyptus/Elm): Bentleigh, Caulfield, McKinnon, Murrumbeena, Elsternwick, Ormond
- **Heritage / period housing stock** (Heritage Overlay, Edwardian/Federation/Californian Bungalow, leadlight, fretwork, Baltic pine): Brighton, Sandringham, Elsternwick, Ormond, Mentone, Bentleigh
- **Named local landmarks/streets:** Beaumaris (Ricketts Point, Table Rock Point, The Concourse, Beach Road), Bentleigh (Allnutt Park, Patterson Rd, Bentleigh Reserve), Carnegie (Koornang Rd, Packer Park), Caulfield (Caulfield Park), Gardenvale (Martin Street Village, Gardenvale Park), Mordialloc (Main Street, Mordialloc Creek), Murrumbeena (Neerim Rd, Murrumbeena Station), Sandringham (Station Street, yacht club), Ormond (North Road)

## Category 2 — VERIFY with client before restoring (capability claims NOT in the client profile)
Do NOT re-add these unless the client confirms they are genuinely true — they are specific capabilities absent from `client-profile.json`:
- **HEPA-filter vacuuming** — appears on Hampton, McKinnon, Moorabbin, Murrumbeena live pages.
- **Specialised sand-capture vacuum + microfibre systems** — Sandringham, Aspendale.
- **pH-neutral salt-spray treatment products / specialised salt-spray window cleaning** — Aspendale, Brighton, Cheltenham.
- **Cleaning around valuable artwork & antiques** — Brighton (high-end capability).
- **Heritage-specific surface protocols** (original marble, period timber) — Brighton, Sandringham, Elsternwick. (A generic "extra care with delicate and period surfaces" line is safe; the specific protocols are the part to confirm.)

## Category 3 — CONFIRM with client (commercial / scope decisions)
- **"$50 off your first clean" promo** — prominent on the live homepage hero; dropped. Still running?
- **Additional services** named on the live homepage but not featured on the new top-level pages: Airbnb/short-stay, Commercial/Office, Builders/post-construction, Corporate. (Note: the confirmed service list already includes Corporate/Office, End of Lease/Bond, Move-In, Tile & Grout — so some of these are legitimate to surface if the client wants them on these pages.)
- **"Exclusive member perks/offers"** and **carpet/upholstery shampooing as an arrangeable add-on** (Caulfield, Gardenvale) — offer still available?

## Category 4 — Useful FAQ topics dropped (safe to add as generic reassurance)
- **"How do I arrange access if I'm not home?"** (key collection / lockbox / building access) — Carnegie, Caulfield, Cheltenham, Mordialloc, areas-we-serve.
- **"How are pets handled during the clean?"** — Elsternwick, Gardenvale.
- **"Can I change or cancel my booking?" / "How often should I book?"** — areas-we-serve.
These can be answered generically ("let us know your access preference and pet routine when you book") without asserting unverifiable policy.

## Category 5 — No action (correctly changed)
- Live "2 yearly emergency cleans" (Black Rock, homepage) → new "1 yearly emergency clean" **matches the confirmed client profile** — the new pages are correct; do not revert.
- Price tables, review counts, "Why Choose Us", EOL emphasis — all intentional campaign changes.
