import re
from pathlib import Path

CLIENT = Path("/home/invoi/fahad_projects/clients/skyflex.au/content")

def faq_block(heading, items):
    out = [f"## {heading}", ""]
    for q, a in items:
        out.append(f"**{q}** {a}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"

PAGES = {
"homepage": dict(intro_h2=None, closing=None,
  faq_heading="Louvred pergola questions Melbourne buyers ask",
  items=[
    ("How do louvred pergolas handle Melbourne's weather?", "The adjustable aluminium slats tilt open to let sun and air through, or close flat to shed rain, so you control the space through heat, wind and a sudden downpour. The aluminium frame with stainless steel hardware is built to sit outside through every season."),
    ("Do I need council approval for a pergola in Melbourne?", "It depends on your property and where the structure sits, and the rules differ between councils. Check with your local council before you order, and we can supply the specifications and dimensions they may ask to see."),
    ("Can I install a louvred pergola myself?", "Yes. Every pergola is sold as a DIY kit with instructions, or you can have one of our approved installers fit it at an affordable rate. The product is the same either way, only the labour changes."),
    ("What warranty comes with a Skyflex pergola?", "Up to a 15-year product warranty, well beyond the 1 to 5 years common across the market."),
    ("How much maintenance does a louvred pergola need?", "Very little. Because the structure is aluminium rather than timber, it does not rot or rust, so it needs no regular servicing beyond an occasional clean."),
    ("What sizes and colours can I choose?", "The pergolas are fully customisable to the size, setting and colour of your space, from earthy tones through to black or white."),
    ("What is the difference between the Delta models?", "The Delta Light Motorised is the entry model. The Delta Motorised and Delta Open Sky sit in the mid-range, and the Open Sky is the one whose blades both rotate and fully retract, opening the roof right back to the sky."),
    ("How do I order, and can I see one first?", "Order online, or request a quote for a custom project and the team will match it to the right model and finish. You are also welcome to visit the Epping showroom by appointment to see the range before you buy."),
  ]),
"louvred-pergolas-sydney": dict(intro_h2=None, closing=None,
  faq_heading="Pergola questions from Sydney buyers",
  items=[
    ("How does ordering a pergola work if I am in Sydney?", "Skyflex is based in Melbourne and ships nationwide. You order the louvred pergola as a kit, we make and deliver it to your Sydney address, and you either assemble it with the instructions or have one of our approved installers fit it."),
    ("Is there a Skyflex installer in Sydney?", "Fitting in Sydney is handled through our approved-installer network, or by you with the supplied kit. There is no in-house Skyflex crew in Sydney, which is part of what keeps the finished pergola well under a custom-built one."),
    ("How do louvred pergolas handle the weather?", "The adjustable aluminium slats open for sun and air or close flat against rain. The aluminium frame with stainless steel hardware and double-walled, gasket-sealed louvre blades is built to stay outside through every season."),
    ("Do I need council approval in Sydney?", "It depends on the property and where the structure sits, and requirements vary by area. Check with your local council before you order, and we can supply the specifications and dimensions they may ask to see."),
    ("What warranty do I get?", "Up to a 15-year product warranty, well beyond the 1 to 5 years common across the market."),
    ("How much maintenance is involved?", "Little to none. The aluminium structure does not rot or rust, so it needs no regular servicing beyond an occasional clean."),
    ("Can I choose the size, colour and configuration?", "Yes. The pergolas are fully customisable to the size, setting and colour of your space, from earthy tones through to black or white."),
    ("How do I get a price for my space?", "Request a quote through the site with your size and configuration, and the Skyflex team will come back with the kit price, the colour and the approved-installer option in one go."),
  ]),
"delta-pro-retractable-roof": dict(intro_h2="A motorised roof for year-round outdoor living", closing="## Order your Delta Pro",
  faq_heading="Common questions about retractable roofs",
  items=[
    ("How much does a retractable roof cost in Australia?", "Prices swing widely because these roofs are usually sold as custom installs quoted per site. The Delta Pro takes the guesswork out: it is supplied from $5,200 for the 3x3 size up to $7,800 for the 6x4, with the figure set by the size, fabric and frame you pick. Fitting is separate."),
    ("Are retractable roofs worth it?", "If you have an outdoor area you only use in good weather, an opening roof turns it into a space that works across the year. You get sun when you want it and a sealed, waterproof cover when you do not, from one structure and one remote."),
    ("What is the disadvantage of a retractable roof?", "A fabric retractable roof runs on a motor and mains power, so it pays to choose one with a properly sealed drive. The Delta Pro answers that with its IP67-rated Dooya motor and mildew-resistant PVC fabric. The main thing to plan for is the footprint, since it is a free-standing unit."),
    ("Is the Delta Pro fully waterproof?", "Yes. Closed, the roof seals to 100% waterproof and blocks direct sun, which keeps the space beneath it noticeably cooler through summer."),
    ("Can I open and close it when it rains?", "Yes. One handheld remote runs the motorised roof, so you open it to the sun, close it over when the weather turns, or stop it anywhere in between for the shade you want."),
    ("Does it need power?", "Yes. The Dooya drive motor is a 40W, DC 24V unit on a standard AU plug-in, sealed to IP67 so it withstands dust and water where it sits out in the weather."),
    ("What sizes does it come in?", "The free-standing unit comes in 3x3, 3x4, 3x5, 4x4, 4x5 and 6x4 metres, with fabric in Beige, Black or White and frames in Black, Charcoal or White."),
    ("Do I install it myself?", "It is supplied on a buy basis with a 50% deposit to order, so fitting is yours to arrange, either as a capable weekend project or through an approved installer."),
  ]),
"delta-commercial-folding-arm": dict(intro_h2="The Delta Commercial Folding Arm awning", closing="## Talk to the Skyflex team",
  faq_heading="Folding arm awning questions",
  items=[
    ("Is the Delta Commercial Folding Arm weatherproof?", "When it retracts, the fabric and both folding arms seal inside a full aluminium cassette, so the parts that wear are shielded whenever the awning is not extended. The fabric is fade-resistant Dickson and the motor carries an IP67 seal against water and dust."),
    ("Is it motorised?", "Yes. A Dooya Silent 40W motor runs it by remote, with an integrated dimmable LED strip set into the cassette at no extra charge."),
    ("What sizes does it come in?", "Two sizes, 3000W x 2500P or 4000W x 3000P, in Black or White, with the projection angle adjustable up to 30 degrees to set your shade line."),
    ("What fabric is used?", "Fade-resistant Dickson, the long-run benchmark for outdoor awning fabric, on a box body and folding arms in 6063 aluminium alloy."),
    ("How is it mounted?", "Wall or ceiling brackets are included, so it suits most frontages. The full-cassette installation manual is included in the box."),
    ("Can it be customised?", "If the two standard sizes or colours do not fit your opening, customisation is available on request, with any additional charges quoted before you commit."),
    ("Do I install it myself?", "It is sold on a supply basis. You receive the awning and mount it yourself or hand it to your own contractor. Skyflex does not run an install crew for this product, and the pricing reflects that."),
    ("How much does it cost?", "Pricing runs from $2,000 to $2,300, supplied, depending on which of the two sizes you choose. It is a pre-order item with a 50% deposit per unit, and orders of five or more qualify for trade pricing."),
  ]),
"skyflex-4k-android-smart-outdoor-tv": dict(intro_h2="An outdoor TV built to stay outside", closing="## Pre-order your Skyflex outdoor TV",
  faq_heading="Questions buyers ask before going outdoors",
  items=[
    ("Is there a TV that is genuinely waterproof?", "This one is sealed to IP55, which means dust cannot get inside in a harmful amount and water jets from any direction will not reach the electronics. It is made to stay mounted outdoors through rain and the seasons, unlike an indoor set that needs bringing in."),
    ("Will it work in full, direct sun?", "Its 1000-nit screen is made for covered and partly shaded areas, a roofed alfresco, a verandah or under a pergola. In open sun with nothing overhead you want a brighter panel built for that. Match it to your spot and it performs well."),
    ("How bright is 1000 nits compared with a normal TV?", "About three times brighter. A typical indoor television sits near 300 nits, which washes out the moment you carry it outside. At 1000 nits this screen holds a clear picture in shaded daylight."),
    ("Can I not just put a regular TV outside instead?", "An indoor TV is not sealed against dust or water and is not bright enough for daylight, so it fails outdoors quickly. A purpose-built unit like this one is sealed, brighter and rated to stay put."),
    ("What sizes does it come in?", "Four sizes: 55, 65, 75 and 85 inch. All run 4K UHD at 3840 x 2160 on Google Android TV."),
    ("What operating system does it run?", "Google Android TV, with a 100 Hz refresh rate, built-in waterproof speakers, and three HDMI plus two USB inputs."),
    ("How does pre-order work?", "It ships as a pre-order item. A 50% deposit per unit places the order, and the balance follows before dispatch. Buying five or more for a venue or a fit-out opens trade pricing."),
    ("Do I mount it myself?", "It is supplied wall-mount compatible, so you or your installer mount it. With no bundled install cost, the same outdoor-TV specification lands well below many competing systems."),
  ]),
"skyflex-bbq-pods": dict(intro_h2="The Skyflex BBQ pod", closing="## Book a BBQ pod consultation",
  faq_heading="BBQ pod questions",
  items=[
    ("How much does a Skyflex BBQ pod cost?", "It is a custom order that starts from $13,500. Treat that as a starting point rather than a final quote, because the finished price follows the size you pick and the way you fit the pod out."),
    ("Can I buy a BBQ pod online?", "No. It is a custom-order product, not available for direct online purchase, so pricing, delivery and any customisation are settled by speaking with the team first. There is no add-to-cart button, and that is deliberate."),
    ("What sizes are available?", "Two footprints, both standing 2.3 metres tall: 2200w x 2300h x 770w for a courtyard or a tighter alfresco corner, and 2850w x 2300h x 770w for a larger space."),
    ("Is the pod built to stay outdoors?", "Yes. It lives outdoors permanently, and the finish and the way it is fitted out are confirmed with you during the consultation so the weather-facing build is matched to where the pod will stand."),
    ("How does the consultation work?", "You tell us the space and the brief, and we tailor the pod to where it will stand and how hard it will be worked, then come back with a real number rather than a guess."),
    ("How does a pod compare to a custom-built outdoor kitchen?", "Buying a configured pod direct, rather than a bundled design-and-install package, is a large part of what keeps the entry price where it is. Comparable pods on the market are commonly advertised from around $18,990 upward."),
    ("Can I choose the layout and finish?", "Yes. A made-to-configuration pod leaves the important details open until you have chosen them, so the finish and fit-out suit your space rather than a single spec sheet."),
    ("How do I get started?", "Call the Skyflex team on 03 9498 0505, email info@skyflex.au, or book a showroom visit in Epping to start the consultation."),
  ]),
"smart-toilets": dict(intro_h2=None, closing="## Enquire about a Skyflex Smartoilet",
  faq_heading="What buyers want to know before choosing one",
  items=[
    ("Is a smart toilet worth it?", "Opinions genuinely split. Some owners call it worth every cent for the daily comfort, while others decide the cost is not justified for their household. The wash, warm seat and dryer are what long-term owners rave about. If those matter to you, the value follows."),
    ("How much do smart toilets cost?", "Bidet-seat setups start near $1,500, integrated suites usually sit between about $2,000 and $4,500, and premium models run past $6,000. Skyflex confirms current U6 and U7 pricing on enquiry."),
    ("What are the disadvantages?", "The main ones are the upfront cost, the need for a power point and possibly an electrician, and the fact that the wash, dryer and heated seat depend on power. There are more electronic parts than a standard toilet, so servicing is a consideration over the years."),
    ("How is a smart toilet installed?", "It needs a plumber for the water connection and, in many bathrooms, an electrician to add a power point near the pan. If your bathroom has no outlet close by, factor that work into the budget from the start."),
    ("Do smart toilets work when the power goes out?", "The electronic functions stop, but most models retain a manual or mechanical flush so the toilet still works. Check the specific model's power-out behaviour before buying."),
    ("Do you still use toilet paper?", "You can, though many owners find the warm-water wash and air dryer reduce how much they reach for it. It is a preference, not a rule."),
    ("Can I fit a bidet seat to my existing toilet, or do I need a whole new suite?", "If your pan is compatible, a bidet seat is the lower-cost route and avoids replacing the whole suite. An integrated suite is the option when you want everything designed together or you are renovating anyway."),
    ("Which toilets do plumbers prefer?", "Plumbers tend to favour WELS-rated suites with standard connections and serviceable parts. The best guide is the person installing yours, so ask your plumber to sight the model and the bathroom before you order."),
  ]),
}

FAQ_SECTION_RE = re.compile(r'\n## [^\n]*(?:question|faq|ask|want to know|common questions)[^\n]*\n.*?(?=\n## |\Z)', re.I | re.S)

for slug, cfg in PAGES.items():
    p = CLIENT / f"content/{slug}/generated.md"
    text = p.read_text()

    # 1) product-page intro H2 after H1 (only if not already present)
    if cfg["intro_h2"]:
        h1m = re.search(r'^(# .+)$', text, re.M)
        h1_line = h1m.group(1)
        h2_line = f"## {cfg['intro_h2']}"
        if h2_line not in text:
            text = text.replace(h1_line + "\n\n", h1_line + "\n\n" + h2_line + "\n\n", 1)

    # 2) remove any existing FAQ section
    text = FAQ_SECTION_RE.sub('', text)

    # 3) build + insert new FAQ block
    fb = faq_block(cfg["faq_heading"], cfg["items"])
    text = text.rstrip() + "\n"
    if cfg["closing"] and cfg["closing"] in text:
        text = text.replace(cfg["closing"], fb + "\n" + cfg["closing"], 1)
    else:
        text = text.rstrip() + "\n\n" + fb

    p.write_text(text.rstrip() + "\n")
    nq = text.count("**") // 2  # rough
    print(f"{slug}: intro_h2={'yes' if cfg['intro_h2'] else 'no'}, FAQs={len(cfg['items'])}")

print("done")
