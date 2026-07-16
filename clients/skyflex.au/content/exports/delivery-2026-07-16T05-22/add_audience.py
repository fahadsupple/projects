from pathlib import Path
CLIENT = Path("/home/invoi/fahad_projects/clients/skyflex.au/content")

# (audience_heading, audience_body, faq_heading_to_insert_before)
SECTIONS = {
"homepage": (
  "Who a Skyflex louvred pergola suits",
  "Skyflex louvred pergolas suit Melbourne homeowners and businesses who want an outdoor space they can use all year, not only on still, sunny days. They fit the DIY enthusiast happy to assemble a kit over a weekend just as well as the owner who would rather an approved installer handled it. At home the common settings are backyards, patios and gardens; cafes, restaurants and other commercial properties use them to make an outdoor area work in any weather. If you value durability and a fixed, upfront price over an open-ended bespoke build, this is the range built for that.",
  "## Louvred pergola questions Melbourne buyers ask"),
"louvred-pergolas-sydney": (
  "Who a Skyflex pergola in Sydney suits",
  "A Skyflex pergola suits Sydney homeowners and businesses who want a quality louvred pergola without commissioning a bespoke on-site build. Because it ships as a kit and is fitted through approved installers, it works for the hands-on owner who will assemble it and for the buyer who would rather an installer took it on. It is the right fit if you want a fixed, upfront price and a product engineered for the weather, rather than an open-ended custom quote.",
  "## Pergola questions from Sydney buyers"),
"delta-pro-retractable-roof": (
  "Who the Delta Pro is best for",
  "The Delta Pro is best for anyone with a patio, deck, poolside corner or open area that has nothing over it and who wants shade on a hot day and cover when it rains, from one structure. Because it is free-standing and carries a published price, it suits buyers who want a fixed cost and a product they can order today rather than a custom install quoted per site. It fits a capable DIY owner or someone who would rather bring in an installer, and anyone who uses an outdoor area often enough that losing it to the weather is a real cost. If your space already has a solid roof over it, a fixed awning or blind may suit better.",
  "## Common questions about retractable roofs"),
"delta-commercial-folding-arm": (
  "Who the Delta Commercial Folding Arm suits",
  "The Delta Commercial Folding Arm suits buyers who want a folding-arm awning built to last outdoors rather than the cheapest option on the shelf. The full cassette makes it a strong fit for a cafe or shopfront frontage, a deck exposed to Melbourne's swing from sun to sudden shower, or a home alfresco you want to keep for years. Because it is supplied for you or your contractor to fit, it works for owners comfortable arranging their own installation and keen to avoid a bundled measure-and-install cost. If you want a lightweight, occasional-use patio arm at the lowest price, an open folding arm will be cheaper.",
  "## Folding arm awning questions"),
"skyflex-4k-android-smart-outdoor-tv": (
  "Who the Skyflex outdoor TV is best for",
  "This TV is best for a covered or partly shaded outdoor spot: a roofed alfresco, a verandah, a pergola, or a corner that catches only glancing light. It suits homeowners who already have a shaded entertaining area and want a screen that can stay mounted outside through the seasons. It is not the right choice for a wall in open, direct sun through the middle of the day, where a brighter panel built for full sun performs better. If your spot has something overhead, this is the screen for it.",
  "## Questions buyers ask before going outdoors"),
"skyflex-bbq-pods": (
  "Who a Skyflex BBQ pod is for",
  "A Skyflex BBQ pod is for homeowners and venues planning a premium outdoor kitchen who want it configured to their space rather than bought off a shelf or built bespoke on site. It is a considered purchase settled through a consultation, so it suits buyers who want to tailor the size, finish and fit-out and are comfortable with a made-to-order timeline. If you want the look and function of a custom outdoor kitchen at a lower entry price than a fully bespoke build, this is the route. For a small, off-the-shelf grill on a budget, it is more than you need.",
  "## BBQ pod questions"),
"smart-toilets": (
  "Who a smart toilet is best for",
  "A smart toilet is best for buyers who value the daily comfort of a warm seat, a warm-water wash and a dryer, and who are renovating or building where the plumbing and a power point can be planned in. The U6 and U7 suit a household happy to add an electrical outlet near the pan if there is not one already. It is less suited to anyone unwilling to run power to the toilet, or who does not want the extra electronic parts to maintain over the years. If the wash and warm seat appeal and the bathroom can take a power point, the value follows.",
  "## What buyers want to know before choosing one"),
}

for slug, (h, body, before) in SECTIONS.items():
    p = CLIENT / f"content/{slug}/generated.md"
    text = p.read_text()
    block = f"## {h}\n\n{body}\n"
    if f"## {h}" in text:
        print(f"{slug}: already present, skipping"); continue
    if before in text:
        text = text.replace(before, block + "\n" + before, 1)
    else:
        text = text.rstrip() + "\n\n" + block
    p.write_text(text.rstrip() + "\n")
    print(f"{slug}: inserted 'Who ... is for' section before FAQ")
print("done")
