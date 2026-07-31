# Page generation — task contract

Client folder (CWD for every path below): `/home/invoi/fahad_projects/clients/globallocksmiths.com.au/content`

## Your governing persona — read it in full, first

`/home/invoi/.claude/plugins/cache/colana-mp/content/0.17.0/agents/writer-agent.md`
(ignore its YAML frontmatter). It is 847 lines and it is the contract. Read **all** of
it before writing a word. This file does not replace it; it adds the client-specific
bindings and the load list.

## Mandatory reads before drafting (all of them, every time)

1. `clusters/<CLUSTER>/plan.lock.json` — the locked plan. `universal_required`,
   `cluster_specific_required`, your entry's `per_entry_unique_angle`,
   `client_data_signals`, and `publishable_facts`. **This is the contract; every
   requirement must appear in the output.**
2. `clusters/<CLUSTER>/research/keyword-<ENTRY>.json` — this entry's SERP research.
   Note: `synthesis` is `{}` by design in this project. The real signal is in the
   normalised fields: `serp_results`, `paa_questions`, `related_searches`,
   `competitor_pages`, `ai_overview`, `intent`. **`search_volume` is 0 for every
   suburb entry — that is an absent database record, not measured zero demand. Never
   write about search volume or rankings; it is analyst data (Cardinal rule 5).**
3. **Service-location pages only:** `clusters/<CLUSTER>/research/suburb-data/<SUBURB-SLUG>-smart-lock-installation.json`
   — your local proof MUST come from here, never from training data. Where a field
   reads `"Insufficient local data"`, write nothing in its place. Several bundles are
   deliberately thin because wrong-place records were discarded; a shorter honest page
   is the required outcome. Some carry a `_requery` or `_geo_guard_notes` key recording
   what was discarded and why — read it, and do not reintroduce what was thrown out.
4. `voice-profile.md` — corpus-derived, so match it: second person ("you/your") outpaces
   "we/our", plain explanatory register, defines the technology before selling it,
   moderate ~18-word average sentence, free-quote call to action.
5. `corpus.md`, `corpus_structural_shapes.json`, `corpus_operational_truth.json` — read
   all three. Avoid any sibling's H2 sequence, lede shape, opening hook and closing
   pattern. On the first entry these are near-empty; that is expected.
6. `client-context.md` and `client-notes.md` — the "Content Restrictions" section is a
   hard constraint.
7. `entries/<ENTRY>.json` — honour its `notes` field if present.

## Client-specific hard constraints (binding, analyst-resolved)

These are the ones that will get the page rejected. They are not style preferences.

- **Availability is Monday to Friday, 9am to 5pm. Full stop.** The business does NOT
  offer round-the-clock service, after-hours callout, or any urgent-response promise,
  and makes NO arrival-time commitment. Never imply otherwise, and never write an
  urgency framing the business cannot honour. Lockout work is in scope; urgency framing
  around it is not.
  **The live website and several competitor records in your research contradict this** —
  they advertise round-the-clock availability and fast arrival windows. That copy is
  wrong and is being corrected by the client. Do not mirror it, and do not compete on
  the availability axis.
- **Tenure is written ONLY as the literal phrase in `client_data_signals.tenure_phrasing`.**
  Never express tenure as an elapsed count of years, and never derive one by subtracting
  the founding year from the current year. The profile field that would have supplied a
  count was deliberately removed.
- **There are no premises anywhere.** `operating_model` is `mobile_service_area`, and
  `business_address` is deliberately absent, not a gap. Never write "based in", "our
  [suburb] branch", "depot", "showroom", "come in", or "drop by". The van travels to the
  customer. Per persona Cardinal rule 6 (servicing-from-afar): describe coverage
  positively, never claim local presence, and never volunteer non-presence either.
- **Pricing is on quote, always.** Only ONE fact is confirmed in the ledger
  (`company.founding-year`). Publish no price, no range, no count, no percentage and no
  duration that is not in `publishable_facts` or this entry's research bundle. "Free,
  no-obligation quote before any work begins" is the correct and sufficient phrasing.
- **Australian door vocabulary only.** Smart mortice lock, smart deadbolt, fire-rated
  smart lock for unit doors; the incumbent hardware a retrofit mates with is Lockwood,
  Lane or Lemaar. British door conventions entered the raw research through UK homonym
  results: never write uPVC, anti-snap, or UK lock brand names. They would read as
  obviously foreign on a Melbourne page.
- **Never source an FAQ answer from `checkatrade.com`.** It is a UK trade directory. It
  survived the Melbourne-scoped searches on several entries and reached at least one PAA
  answer. Its pricing is in pounds and its install timings do not describe Australian
  practice.
- **This is a security business.** The `safety_critical` audit adapter is armed: no
  attack-vector language. Do not write about weak points, easy access, vulnerabilities,
  or how a door could be defeated. Frame everything as what the customer gains.

## Credibility block — check `page_type` and get this right

- `page_type: service` (the hub): **FULL** block. Business-named H2, all of founder,
  since-2002, projects completed, accreditations, licensed and insured, warranty,
  guarantee. Placed as section 2 or 3.
- `page_type: service-location` (the 40 spokes): **LEAN** block. Business-named H2
  carrying only the trust floor — founder, founding year, client count, licensed and
  insured — then a link to the hub for the full credentials. Do NOT repeat the full
  accreditation and warranty set here; that is what makes forty suburb pages read as one
  templated page. Keep the whole floor; move only the extras.
- **Never title it "Why Choose Us"** in either case. The templating gate blocks it.

## Output

Write to `content/<ENTRY>/generated.md`. Create the directory if needed. If a
`generated.md` already exists, first copy it to `content/<ENTRY>/versions/generated-<n>.md`.

YAML frontmatter then the body:

```yaml
---
title: <primary keyword led, brand only if it fits, aim ~60 chars, NEVER over 70>
meta_description: <50 to 160 characters, counted; no monetary threshold>
primary_keyword: <the entry's primary keyword>
entry_id: <ENTRY>
---
```

Body rules that get mechanically checked:

- Primary keyword **exactly** in the H1. The first paragraph must cover every word of it
  naturally, in any order. Never force the exact phrase where it does not read.
- **Zero em-dashes in the body.** Not `—`, not `--`, anywhere: prose, bullets, headings,
  label-value pairs. This blocks at count one. Use a full stop, a comma, a colon, or "to"
  for ranges. (The `---` frontmatter fences are delimiters, not em-dashes.)
- No postcode in the H1, any heading, or the first paragraph.
- No bolded keyword phrase anywhere outside the H1.
- **Length: target 1200 words, treat 1500 as a ceiling you do not cross.** The hub page
  landed at 1491, inside the band, while carrying a lock-type comparison, a retrofit
  explanation, a door-situations list, an FAQ and the coverage block. A suburb page has
  far less to carry: one door-situation angle and a handful of local concerns. If yours
  is running past 1500, you are padding.
  **If your suburb bundle is thin, write a SHORTER page.** 900 honest words beat 1600
  with 700 of filler, and padding is what makes forty suburb pages read as one. This is
  the persona's own rule: output with fewer data-grounded words beats output with more
  assumed words.
- Australian English spelling.
- H2s read as natural language a customer would say aloud.
- **H2 shapes that BLOCK the page (`templating_section_check`, learned the hard way on
  the Maidstone page).** Every spoke has to cover pricing and booking, so those sections
  are exactly where a process-recital heading creeps in and the gate blocks it:
  - Never `## How our/the/we [something] works` in any tense. The check's regex matches
    the stem `work`, so **"How the Price Is Worked Out" trips it** even though nothing
    about that heading looks like a step list.
  - Never a heading containing `N steps`, `N-step`, or `step-by-step`.
  - Never `## Your first [visit|appointment|consultation|call|session]`.
  - Never `## Why Choose Us` or any variant.
  - Safe instead: anchor the heading to THIS page's subject, e.g. "What Moves the Price
    on a [Suburb] Door", "Getting a Price Before Anything Is Cut", "What the Quote
    Covers". Headings opening "How much" or "How to book" are explicitly allow-listed.
  The pricing CONTENT still belongs on the page: the plan requires it. Keep it short,
  make it specific to this suburb's doors, and never enumerate a universal booking flow.

## The closer is the highest-risk element on the page (BLOCKING, and it worsens as the run grows)

`cluster_template_detection > closing_pattern_overlap` blocks at 45% shared boilerplate
with any sibling's closer. It has already blocked one page in this run. Every page in the
cluster ends by asking for the same action, on the same phone number, in the same hours,
so the closer is where forty pages converge hardest, and each new page has more siblings
to collide with than the last.

The trap is the **shape**, not the phone number. This construction is now used up:

> "Tell us [what is on the door] and [which model you are considering], on 1300 333 565
> between 9am and 5pm, or through the online enquiry form."

Any closer that asks the reader to supply two pieces of information and then lists the
phone and the form will read as a slot template no matter which two things you name.

**The single rule that matters: your LAST LINE must contain something only this page would
say.** The gate measures the closing line. A final line made only of contact details is
100% boilerplate by construction, because every one of the 41 pages carries the same phone
number, the same hours and the same form. It does not matter how distinctive the paragraph
above it is.

This exact final line was blocked against FOUR siblings at once (63%, 63%, 47%, 47%):

> "Quotes get booked on 1300 333 565 between 9am and 5pm on weekdays, or through the
> online enquiry form."

Nothing in it belongs to any particular page, so it belongs to all of them.

**The fix is to fold this page's specific thing INTO the contact line**, not to put it in
the sentence before. Two worked examples from pages that were blocked and then cleared:

- A page about identifying old hardware ends by asking for a photo close enough to read
  the brand stamp on the faceplate, then gives the number.
- A page about house doors versus business doors ends "Lead with that word on
  1300 333 565, weekdays, or in the first line of the enquiry form", where "that word"
  is the house/business distinction the whole page is built on.

Both are contact lines. Neither could be moved to another page without breaking.

Keep it to at most two sentences before the contact line, and make the contact line itself
carry the page.

Run the persona's self-tests: Questions 1 to 5 (quality), 6 to 9 (honesty), and the craft
pass C1 to C7. The two that catch the most here are **Q2 the name-swap test** (if
replacing the suburb name makes the page generic, rewrite) and **C3 repeated cadence**
(no more than one rhetorical question on the page; do not lean on the same sentence
skeleton section after section).

**Report exactly:** the output path, body word count, em-dash count in the body (must be
0), meta_description character count, the H2 sequence you used, and any plan requirement
you could not satisfy along with why. Nothing else.
