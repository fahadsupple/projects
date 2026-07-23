# Publish notes — manual steps at CMS publish time

## 1. End-of-Lease cross-links (hyperlink these)

**Context (analyst-confirmed 2026-07-23):** End-of-lease keywords were part of the *initial* campaign and have now been **removed from targeting**. The existing EOL pages themselves are **NOT being removed** — they stay live. The new house-cleaning pages were therefore written to *complement* them, not replace or cannibalise them.

Several generated pages reference the client's existing End of Lease suburb pages **by name in prose**. Those URLs are not in the Meta File / `entries/`, so no URL was guessed. Hyperlink each at publish:

| Page | Reference to hyperlink | Why it matters |
|---|---|---|
| `cleaners-ormond` | "End of Lease Cleaning Ormond page" (body + FAQ) | client's EOL Ormond page already ranks **#7** for `house cleaning ormond` |
| `cleaners-moorabbin` | "End of Lease Cleaning Moorabbin page" (body + FAQ) | client's EOL Moorabbin page already ranks **#13** for `house cleaning moorabbin` |
| `cleaners-mordialloc` | "End of Lease Cleaning Mordialloc page" (×2) | client's EOL Mordialloc page already ranks **#8** |
| `cleaners-carnegie` | "End of Lease Cleaning Carnegie page" | client's Carnegie page currently ranks for EOL only |
| `cleaners-aspendale`, `cleaners-mckinnon` | EOL referenced generically in prose | link if a matching EOL page exists |

Do **not** guess slugs — confirm each in the CMS.

## 2. Business location — suburb level ONLY

**Confirmed:** Robot Cleaning Solutions is based in **Parkdale, VIC 3195**.

**Constraint:** the client has **never published a complete street address**. Content may say the business is based in Parkdale (suburb level) and may use the postcode 3195, but must **never** state or invent a street number/name.

- Verified: zero street addresses appear anywhere across the 22 pages.
- `cleaners-parkdale` leads on this proximity advantage using suburb-level phrasing only ("the suburb this business is based in", "a team already in the neighbourhood").
- Recorded in `client-profile.json > business_address` (locality/region/postcode only; `street_address` intentionally omitted).

## 3. Review count

Content deliberately says **"5-star rated on Google"** and never a hard review count, because the count is growing (13 at time of writing). Keep it that way so the copy does not go stale.

## 4. Pricing

Membership is referenced as **"from $150 per week, tailored to your home size"** with a free on-site quote. No rigid price table was published, and no competitor prices are quoted anywhere.
