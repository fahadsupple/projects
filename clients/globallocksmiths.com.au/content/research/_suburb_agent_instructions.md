# Suburb × service ground-truth — agent instructions

Client: **globallocksmiths.com.au** (Global Locksmiths, mobile locksmith, Melbourne)
Service (fixed for every pair): **smart lock installation**
Client folder: `/home/invoi/fahad_projects/clients/globallocksmiths.com.au/content`
`operating_model`: **`mobile_service_area`** → the **full physical contract** applies (all five keys below).

## What you do, in order

### Step 1 — one Brave local search, written verbatim

Call `mcp__plugin_content_brave-search__brave_local_search` with:

- `query`: **`<suburb> smart lock installation`** (that exact word order — the fixture
  filename is derived from it and the Python loader will not find a differently-ordered file)
- `country`: **`"AU"`** — MANDATORY. The parameter defaults to `US`; leaving it unset
  returns American results and silently poisons the whole bundle.
- `count`: `10`

Expect the response to open with a plan-unavailable notice line followed by a
web-search fallback stream — that is the normal, verified shape for this account
(the Python loader salvages it and marks the bundle `fallback_to_web`). It is not an
error and not a reason to retry.

Write the **full, verbatim** MCP response to:

```
research/raw/brave-local-<suburb-slug>-smart-lock-installation.json
```

relative to the client folder. `<suburb-slug>` = the suburb lowercased with any run of
non-alphanumeric characters replaced by a single hyphen (e.g. `Ascot Vale` → `ascot-vale`,
`St Albans` → `st-albans`).

Write it verbatim even if the response is a plan-unavailable notice or a web-search
fallback stream — the loader salvages those since v0.15.2. Do **not** hand-wrap,
reformat, pretty-print differently, or extract a subset. Do not create the folder;
it already exists.

### Step 2 — synthesis, grounded only in what Step 1 returned

Write a JSON object to:

```
research/raw/_synthesis/<suburb-slug>-smart-lock-installation.json
```

Create the `_synthesis` directory if it does not exist. The object must have **exactly
these five keys** (the physical contract for `mobile_service_area`):

- `climate_context` — one sentence on the suburb's climate relevance to smart lock
  installation. Be honest: climate is usually marginal for indoor door hardware. If the
  local signals say nothing about it, write `"Insufficient local data — recommend manual research"`
  rather than inventing a weather angle.
- `building_stock` — one sentence on dominant building types and how they affect
  **smart lock installation specifically** (door material and thickness, heritage
  timber doors, apartment/body-corporate common entrances, new-build estates with
  aluminium/composite doors, double-glazed sliders). Ground it in the returned records.
- `council_notes` — regulatory or planning considerations that actually bear on
  changing door hardware (heritage overlays on street-facing doors, body-corporate
  or owners-corporation rules on common-property entrances, rental-provider
  obligations). `"None identified"` if the signals show nothing.
- `demographic_skew` — one sentence on who lives here and how it shifts smart-lock
  demand (renters vs owner-occupiers, young professionals, families, short-stay/Airbnb
  turnover, downsizers).
- `common_concerns` — array of **2 to 4** specific concerns residents of this suburb
  commonly have about smart lock installation, each traceable to a returned record.

### Geo guard — check the records are about the RIGHT place first

Several of these suburb names exist elsewhere. Confirmed live in this project's keyword
research: Maidstone resolved to Kent UK, "Sunshine" resolved largely to Sunshine Coast
QLD, and Brighton/St Albans pulled `checkatrade.com` UK pricing in £. Brighton, Richmond,
Kew, Docklands, Kensington, Newport, Williamstown, Maidstone, St Albans, Flemington,
Ascot Vale, Hawthorn, St Kilda and Sunshine are all homonyms of non-Melbourne places.

So before you use any returned record, check it is about the **Melbourne/Victorian**
suburb. Discard records that are:

- UK or US (£ or $US pricing, `.co.uk`, Kent/Sussex/Hertfordshire/London, Checkatrade)
- interstate Australian (Sunshine Coast, Brisbane, QLD, Perth, Sydney, `(07)`, `(08)`,
  `(02)` numbers)

Grounding a claim in a discarded record is worse than having no claim, because it reads as
local research and is not. If discarding leaves you with too little, that is the honest
answer — say `"Insufficient local data — recommend manual research"`.

Report in your final line how many returned records you discarded as wrong-geo and why.

### The one rule that matters most

**Every claim must be traceable to a record Brave actually returned.** Before you write
any sentence, ask: which returned record is this from? If you cannot name one, you have
two options — write `"Insufficient local data — recommend manual research"`, or omit the
claim. You may **never** fill the gap from training-data knowledge about the suburb.

You know things about Melbourne suburbs from training. That knowledge is **not
admissible here.** Brighton being affluent, Richmond having Victorian terraces, Point
Cook being a new estate — if the Brave results do not evidence it, it does not go in the
file. This research becomes the ground truth a writer uses to differentiate 40 near-identical
pages for a real client whose live site already carries claims they cannot support.
Confident-sounding invention is the specific failure mode that ruins this deliverable.

Generic filler is equally useless: "residents value reliable service" differentiates
nothing. Either the sentence would change how a writer writes *this* suburb's page, or it
should be the insufficient-data string.

### Output

Report exactly: the two file paths you wrote, the byte size of each, how many local
records Brave returned, and which of the five keys you had to mark as insufficient data.
Nothing else.
