# Content Refinement Checklist (post-generation)

Reusable instruction set for refining content-plugin output after the initial pages are generated and audited. Derived from the skyflex.au engagement (2026-07). Apply per client; not every item fits every page type.

## Content

**1. Page structure — homepage / brand / service pages**
- Lead with a section whose **heading contains the broad primary keyword** (e.g. "Pergolas Melbourne").
- Demote the more specific product section (e.g. "Louvred Pergolas Melbourne") to the **second** section.
- Add an **"About [brand]"** section.
- Write a **meta title + meta description** targeting the broad primary term.
- Fix the lead section so it genuinely targets the broad primary keyword (not the narrower product term).
- The homepage does **not** have to be limited to 2 paragraphs — make it as strong as the keyword warrants.

**2. Page structure — product pages (H1 / H2 rule)**
- Keep the H1 (it **replaces the existing product-page H1** at the top of the page).
- The content block is **added lower on the page**, not under the H1, so it must **start with an H2** (content must not sit orphaned under the H1).
- Apply across **all product pages**.

**3. FAQs**
- **At least 8 per page**, but only the ones **genuinely helpful for end users** (no padding, no fabrication).
- Ground answers in on-page facts + the client's forms (their "top customer questions" and "customer worries") + research PAA.
- FAQ **questions = H3**.

**4. Audience / AEO section ("Who it's for")**
- Add a section giving context on **who the product or category is best for**, so LLMs and search engines understand the target audience and use cases.
- Include **who it's NOT for** where genuinely useful (reduces mismatched purchases, sharpens AI targeting).
- **Render this section as bullet points.**

**5. Formatting — bullets (general)**
- **Any content that can naturally be a list should be bullet points**: audience/best-for, features, specs, what's included, process steps, ranges/options.
- Don't bury list-shaped content in paragraphs. Better scannability, stronger for featured snippets and AI answers.

**6. CTAs**
- Add **"Call us now"** with the **phone number written explicitly in the text**.
- Place after **each section where a call is a natural next step** (not after every FAQ item).
- Vary the wording so the repetition/templating gates stay clean.

**7. Conversion sequence**
- Order sections for conversion. Landed on:
  - **Product pages:** intro → features → specs → **Who it's for** → pricing / how to order → About (trust) → FAQ → closing CTA.
  - **Brand/category pages:** intro → product detail (or education) → **Who it's for** → About → FAQ → CTA.
- Principle: the reader understands the product, confirms it fits them, then sees price + trust, then objections, then acts. The "Who it's for" self-qualifier goes right after the product substance, before the commercial/trust close.

## Accuracy

**8. Fact-check against source**
- Fact-check every claim against the **client's forms/spec sheet** AND the **live site**.
- Reproduce specifics faithfully from the source (don't invent) — but when the source (live page) is itself wrong, **flag it** rather than silently copying.
- Known trap: content can be 100% faithful to the live page yet still wrong because the live page has the error (e.g. BBQ dims `720` vs `770`; wrong title tag `Delta Motorised`). Surface these as client action items.

**9. Internal links — verified against the website**
- Add internal links, but **fact-check every target against the live site** (pull the sitemap; 200-check the URLs).
- Link only to **real, existing pages**. No invented URLs, no self-links.
- Watch slug traps (e.g. product name "Delta Motorised" but URL slug `delta-motorized`).
- Don't link *to* a page that doesn't exist yet (e.g. a category page still in "Uncategorized").

## Deliverable format

**10. Existing-vs-new highlighting**
- Any page with existing content: show existing content on a **yellow background, in position**, so the developer sees **what to keep and where it sits** relative to the new content.
- Applies most to add-blocks pages (existing kept wholesale) and any verbatim-retained spans on rewrites.

**11. .docx handoff**
- Heading tags **`H1:` / `H2:` / `H3:`** (with a colon) prefixed to each heading.
- Headings **bold** but at the **same font size as body** (no oversized heading fonts).
- **FAQ questions = H3.**
- **No yellow existing-content** in the .docx — new content only.
- CTAs stay as bold callouts, NOT headings.
- Internal links as **live hyperlinks**.

## Process preferences (recurring)
- Prefer **speed**; use **parallel agents** where safe (watch session limits).
- Work **cluster-by-cluster**; confirm before **locking** / **approving**.
- **Approve** once everything is gate-clean (0 blocking).
- After any content change: re-run the audit gate, re-approve, and rebuild the deliverables (HTML + .docx).
