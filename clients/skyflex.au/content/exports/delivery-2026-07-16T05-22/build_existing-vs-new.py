import json, re, html
from pathlib import Path

CLIENT = Path("/home/invoi/fahad_projects/clients/skyflex.au/content")

ORDER = [
    ("homepage", "homepage", "add-blocks", "pergolas melbourne"),
    ("delta-pro-retractable-roof", "products", "rewrite-existing", "retractable roof system melbourne"),
    ("delta-commercial-folding-arm", "products", "rewrite-existing", "retractable awning melbourne"),
    ("skyflex-4k-android-smart-outdoor-tv", "products", "rewrite-existing", "waterproof tv australia"),
    ("skyflex-bbq-pods", "products", "rewrite-existing", "bbq pods melbourne"),
    ("smart-toilets", "product-categories", "new-page", "smart toilets melbourne"),
    ("louvred-pergolas-sydney", "service-location-pergolas", "add-blocks", "pergolas sydney"),
]
TITLES = {
    "homepage": "Homepage", "delta-pro-retractable-roof": "Delta Pro Retractable Roof",
    "delta-commercial-folding-arm": "Delta Commercial Folding Arm Awning",
    "skyflex-4k-android-smart-outdoor-tv": "Skyflex 4K Outdoor TV",
    "skyflex-bbq-pods": "Skyflex BBQ Pods", "smart-toilets": "Smart Toilets (category)",
    "louvred-pergolas-sydney": "Louvred Pergolas Sydney",
}

def esc(s): return html.escape(s)

def md_inline(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
    return s

def md_block_to_html(lines):
    """Convert a list of plain markdown lines (no markers) to HTML."""
    out, i = [], 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)', ln)
        if m:
            lvl = len(m.group(1)); out.append(f"<h{lvl+1}>{md_inline(m.group(2))}</h{lvl+1}>"); i += 1; continue
        if re.match(r'^[-*]\s+', ln):
            items = []
            while i < len(lines) and re.match(r'^[-*]\s+', lines[i].strip()):
                items.append(f"<li>{md_inline(re.sub(r'^[-*]\\s+','',lines[i].strip()))}</li>"); i += 1
            out.append("<ul>" + "".join(items) + "</ul>"); continue
        out.append(f"<p>{md_inline(ln)}</p>"); i += 1
    return "\n".join(out)

def render_generated(slug):
    """Render generated.md (new content). Strip the title:/meta_description: header lines into a meta box."""
    text = (CLIENT / f"content/{slug}/generated.md").read_text()
    lines = text.splitlines()
    title_tag = meta_desc = ""
    body_start = 0
    for i, ln in enumerate(lines[:6]):
        if ln.startswith("title:"): title_tag = ln.split(":",1)[1].strip()
        elif ln.lower().startswith("title_tag:"): title_tag = ln.split(":",1)[1].strip()
        elif ln.startswith("meta_description:") or ln.lower().startswith("meta description:"):
            meta_desc = ln.split(":",1)[1].strip()
        elif ln.startswith("# "):
            body_start = i; break
    body = md_block_to_html(lines[body_start:])
    metabox = ""
    if title_tag or meta_desc:
        metabox = f"<div class='metabox'><div><span class='lbl'>SEO title</span> {esc(title_tag)}</div><div><span class='lbl'>Meta description</span> {esc(meta_desc)}</div></div>"
    return metabox + "<div class='new'>" + body + "</div>"

MARKER_RE = re.compile(
    r'^(?:#{1,4}\s*|\*\*)\['
    r'(NEW|EXISTING(?:\s*[—-]\s*(?:KEEP|RECOMMEND CORRECTING))?)'
    r'\]\s*(.*?)(?:\*\*)?\s*$'
)
def _kind_to_cls(kind):
    k = kind.strip()
    if k == "NEW": return "new"
    if "RECOMMEND CORRECTING" in k: return "existfix"
    return "existing"   # [EXISTING] or [EXISTING — KEEP]

def render_deliverable(slug):
    """Format-agnostic: a marker (heading OR bold) switches the active highlight
    class; all following content accumulates into it until the next marker.
    Handles both the heading-marker (homepage) and bold-marker (Sydney) styles."""
    text = (CLIENT / f"content/{slug}/deliverable.md").read_text()
    lines = text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].startswith("---"):
        i += 1
    i += 1
    out = []
    cur_cls = None; buf = []
    TAG = {"new":"NEW", "existing":"EXISTING — KEEP", "existfix":"EXISTING — FIX BEFORE SHIPPING"}
    def flush():
        nonlocal buf, cur_cls
        if buf and cur_cls:
            out.append(f"<div class='{cur_cls}'>{md_block_to_html(buf)}</div>")
        buf = []
    while i < len(lines):
        ln = lines[i]
        mk = MARKER_RE.match(ln.strip())
        if mk:
            flush()
            cur_cls = _kind_to_cls(mk.group(1))
            label = mk.group(2).lstrip("—- ").strip()
            lbl = f"{TAG[cur_cls]}: {esc(label)}" if label else TAG[cur_cls]
            out.append(f"<div class='blabel {cur_cls}-l'>{lbl}</div>")
            i += 1; continue
        if ln.strip() == "---":
            flush(); cur_cls = None; i += 1; continue
        # strip blockquote prefix; keep everything else as content of the active block
        if ln.startswith(">"):
            buf.append(ln[1:].lstrip()); i += 1; continue
        if cur_cls is None:
            # content before any marker (rare) — render plain
            if ln.strip(): out.append(f"<p>{md_inline(ln.strip())}</p>")
            i += 1; continue
        buf.append(ln); i += 1
    flush()
    return "\n".join(out)

def render_existing_replaced(slug):
    """For rewrite pages: show the current live-page body (being replaced) in yellow."""
    fixmap = {
        "delta-pro-retractable-roof":"research/raw/playwright-product-delta-pro-retractable-roof.json",
        "delta-commercial-folding-arm":"research/raw/playwright-product-delta-commercial-folding-arm.json",
        "skyflex-4k-android-smart-outdoor-tv":"research/raw/playwright-product-skyflex-4k-android-smart-outdoor-tv.json",
        "skyflex-bbq-pods":"research/raw/playwright-product-skyflex-bbq-pods.json",
    }
    p = CLIENT / fixmap[slug]
    if not p.exists(): return ""
    d = json.loads(p.read_text())
    bt = d.get("body_text","") or ""
    # trim leading nav chrome up to the H1 if we can find it
    h1 = (d.get("h1") or [""])[0]
    if h1 and h1 in bt:
        bt = bt[bt.find(h1):]
    # keep it readable: collapse blank runs, cap length
    bt = re.sub(r'\n{3,}', '\n\n', bt).strip()
    excerpt = esc(bt[:2600])
    if len(bt) > 2600: excerpt += "\n\n… (existing page continues)"
    return ("<details class='exwrap'><summary>Existing content currently on this page "
            "(being replaced by the new content above) — click to view</summary>"
            f"<div class='existing pre'>{excerpt}</div></details>")

EXISTING_JSON = {
    "homepage": "content/homepage-existing.json",
    "louvred-pergolas-sydney": "content/louvred-pergolas-sydney-existing.json",
}
DEFECTS = {
    "homepage": [
        'Existing H1 "Louvred Pergolas Melbourne" and its "designs and supplies" intro are superseded by the new "Pergolas Melbourne" lead section. Demote the old H1 to H2 or fold it into the new structure; do not keep two competing intros.',
        '"Why Choose SkyFlex for Louvred Pergolas in Melbourne?" heading is a self-praise recital pattern. Rename to a plain-language heading or fold its real points into the new About section.',
        "U6 Smartoilet and U7 Smartoilet product tiles in the grid are empty (no body/price). Populate or remove until the SKUs are ready.",
    ],
    "louvred-pergolas-sydney": [
        '"SkyFlex designs and installs these versatile structures... across the city" intro implies an in-house Sydney build crew Skyflex does not have. Superseded by the new "Pergolas Sydney" lead section; replace it.',
        'Wrong domain: the "Buy" block links to skyflex.com.au. The live site is skyflex.au. Fix the link.',
        "A Melbourne phone number is shown on this Sydney page. Use a Sydney-appropriate contact path or the general enquiry form.",
        '"WHY CHOOSE SKYFLEX FOR LOUVRED PERGOLAS IN SYDNEY" heading is a self-praise recital pattern. Rename or fold into the new About section.',
    ],
}
def render_existing_json(slug):
    d = json.loads((CLIENT / EXISTING_JSON[slug]).read_text())
    parts = ["<div class='blabel existing-l'>EXISTING — KEEP (current live page, shown below the new sections; highlight yellow)</div>"]
    # existing title/meta
    tt = d.get("title",""); mt = d.get("meta","")
    if tt or mt:
        parts.append(f"<div class='existing'><p><strong>Current SEO title:</strong> {esc(tt)}</p>" +
                     (f"<p><strong>Current meta:</strong> {esc(mt)}</p>" if mt else "") +
                     "<p class='note'>Replace with the new title/description shown at the top of this entry.</p></div>")
    # existing section headings (the page structure that stays)
    heads = [h for h in d.get("headings",[]) if h.get("tag") in ("H2","H3") and "cart" not in h.get("text","").lower()]
    seen=set(); uniq=[]
    for h in heads:
        t=h["text"].strip()
        if t and t.lower() not in seen: seen.add(t.lower()); uniq.append(h)
    if uniq:
        parts.append("<div class='existing'><p><strong>Existing page sections kept, in order:</strong></p><ul>" +
                     "".join(f"<li>{esc(h['text'])}</li>" for h in uniq[:22]) + "</ul></div>")
    # a few representative existing paragraphs
    paras=[p for p in d.get("paragraphs",[]) if len(p)>50 and "reCAPTCHA" not in p and "$0.00" not in p][:4]
    if paras:
        parts.append("<div class='existing'><p><strong>Sample of existing body copy (kept verbatim):</strong></p>" +
                     "".join(f"<p>{esc(p)}</p>" for p in paras) + "</div>")
    if d.get("existing_faq_questions"):
        parts.append("<div class='existing'><p><strong>Existing FAQs (kept):</strong></p><ul>" +
                     "".join(f"<li>{esc(q)}</li>" for q in d['existing_faq_questions']) + "</ul></div>")
    # defects
    parts.append("<div class='blabel existfix-l'>EXISTING — FIX BEFORE SHIPPING</div>")
    parts.append("<div class='existfix'><ul>" + "".join(f"<li>{esc(x)}</li>" for x in DEFECTS[slug]) + "</ul></div>")
    return "\n".join(parts)

# ---- assemble ----
sections = []
for slug, cluster, mode, kw in ORDER:
    ent = json.loads((CLIENT / f"entries/{slug}.json").read_text())
    url = ent.get("url","")
    if slug in EXISTING_JSON:
        body = ("<div class='blabel new-l'>NEW — the three new sections that lead the page (Pergolas → Louvred Pergolas → About)</div>"
                + render_generated(slug) + render_existing_json(slug))
        modenote = "Add-blocks: the new sections above lead the page; existing content (yellow) is kept below in its current order. Yellow FIX items must be corrected before shipping."
    elif mode == "new-page":
        body = render_generated(slug) + "<div class='allnew'>Brand-new page. No existing content to keep — everything here is new.</div>"
        modenote = "New page: all content is new."
    else:
        body = render_generated(slug) + render_existing_replaced(slug)
        modenote = "Rewrite: the new content above replaces the current page body. Expand the panel to see the existing content being replaced (yellow)."
    sections.append((slug, cluster, mode, kw, url, modenote, body))

# TOC grouped by cluster
clusters = {}
for s in sections: clusters.setdefault(s[1], []).append(s)
toc = []
for cl, items in clusters.items():
    toc.append(f"<li class='toc-cl'>{esc(cl)}<ul>" + "".join(
        f"<li><a href='#{s[0]}'>{esc(TITLES[s[0]])} <span class='kw'>{esc(s[3])}</span></a></li>" for s in items
    ) + "</ul></li>")

body_html = []
for slug, cluster, mode, kw, url, modenote, body in sections:
    body_html.append(f"""
<section id="{slug}" class="entry">
  <div class="ehead">
    <h2>{esc(TITLES[slug])}</h2>
    <div class="emeta"><span class="pill">{esc(cluster)}</span><span class="pill mode">{esc(mode)}</span>
      <span class="kwt">target: <b>{esc(kw)}</b></span>
      <a class="url" href="{esc(url)}">{esc(url)}</a></div>
    <div class="modenote">{esc(modenote)}</div>
  </div>
  {body}
</section>""")

HTML = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Skyflex — Content Deliverable (existing vs new)</title>
<style>
:root{--yellow:#fff3b0;--yellowb:#e8d268;--fix:#ffd9d0;--fixb:#e39a86;}
*{box-sizing:border-box}
body{font:16px/1.6 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#1a1a1a;margin:0;background:#f4f5f7}
.wrap{max-width:900px;margin:0 auto;padding:32px 20px 120px}
h1{font-size:26px;margin:0 0 4px}
.sub{color:#555;margin:0 0 24px}
.legend{background:#fff;border:1px solid #e2e4e8;border-radius:10px;padding:14px 16px;margin:0 0 24px;font-size:14px}
.legend span{display:inline-block;padding:2px 8px;border-radius:4px;margin-right:6px;font-weight:600}
.sw-new{background:#eef1f4;border:1px solid #d3d8de}
.sw-ex{background:var(--yellow);border:1px solid var(--yellowb)}
.sw-fix{background:var(--fix);border:1px solid var(--fixb)}
nav{background:#fff;border:1px solid #e2e4e8;border-radius:10px;padding:14px 18px;margin:0 0 28px}
nav ul{margin:6px 0;padding-left:18px}
.toc-cl{font-weight:700;text-transform:capitalize;margin-top:6px}
nav a{color:#1758c4;text-decoration:none}
nav a:hover{text-decoration:underline}
.kw{color:#888;font-weight:400;font-size:13px}
.entry{background:#fff;border:1px solid #e2e4e8;border-radius:12px;padding:26px 30px;margin:0 0 26px;page-break-before:always}
.ehead{border-bottom:2px solid #eef0f3;padding-bottom:14px;margin-bottom:18px}
.ehead h2{margin:0 0 8px;font-size:22px}
.emeta{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center;font-size:13px}
.pill{background:#eef1f4;border-radius:20px;padding:2px 10px;text-transform:capitalize;color:#333}
.pill.mode{background:#e3edff;color:#1758c4}
.kwt{color:#555}
.url{color:#1758c4;text-decoration:none;font-size:12px}
.modenote{font-size:13px;color:#666;margin-top:8px;font-style:italic}
.new{}
.existing{background:var(--yellow);border-left:4px solid var(--yellowb);padding:10px 16px;border-radius:0 6px 6px 0;margin:6px 0 14px}
.existfix{background:var(--fix);border-left:4px solid var(--fixb);padding:10px 16px;border-radius:0 6px 6px 0;margin:6px 0 14px}
.blabel{font-size:11px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;margin:16px 0 4px}
.new-l{color:#3a7a3a}
.existing-l{color:#8a6d00}
.existfix-l{color:#b2402a}
.cnote{font-size:13px;color:#7a2a18;background:#fff;border-radius:6px;padding:8px 12px;margin-top:8px;border:1px dashed var(--fixb)}
.secdiv{margin:26px 0 6px;color:#444;font-size:15px;border-top:1px solid #eee;padding-top:16px}
.entry h3{font-size:17px;margin:16px 0 6px}
.entry h4{font-size:15px;margin:14px 0 6px}
.entry ul{margin:6px 0 12px}
.exwrap{margin-top:18px;border-top:1px dashed #ccc;padding-top:10px}
.exwrap summary{cursor:pointer;font-size:13px;color:#8a6d00;font-weight:600}
.pre{white-space:pre-wrap;font-size:13px}
.allnew{font-size:13px;color:#3a7a3a;margin-top:10px;font-style:italic}
@media print{body{background:#fff}.entry{border:none;box-shadow:none}nav,.legend{break-inside:avoid}}
</style></head><body><div class="wrap">
<h1>Skyflex — Content Deliverable</h1>
<p class="sub">7 pages · existing content shown on <span style="background:var(--yellow);padding:1px 5px;border-radius:3px">yellow</span> in position, new content plain. Generated 2026-07-16.</p>
<div class="legend">
<span class="sw-new">NEW</span> newly written content &nbsp;
<span class="sw-ex">EXISTING — KEEP</span> copied verbatim from the live page, keep as-is &nbsp;
<span class="sw-fix">EXISTING — FIX</span> on the live page now but should be corrected before shipping
</div>
<nav><b>Contents</b><ul>""" + "".join(toc) + """</ul></nav>
""" + "".join(body_html) + """
</div></body></html>"""

# write into the latest export dir
import glob, os
exdirs = sorted(glob.glob(str(CLIENT/"exports/delivery-*")))
outdir = Path(exdirs[-1]) if exdirs else (CLIENT/"exports")
outpath = outdir / "existing-vs-new-deliverable.html"
outpath.write_text(HTML, encoding="utf-8")
print("WROTE", outpath, f"({len(HTML)} bytes)")
