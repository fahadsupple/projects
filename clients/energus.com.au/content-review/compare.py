import asyncio, json, sys, re
from collections import Counter
from playwright.async_api import async_playwright

JS = """
() => {
  const root = document.querySelector('main#main') || document.querySelector('main') || document.body;
  const out = [];
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    const t = (n.textContent || '').replace(/\\s+/g, ' ').trim();
    if (!t) continue;
    const el = n.parentElement;
    if (!el) continue;
    const tag = el.tagName.toLowerCase();
    if (['script','style','noscript','template'].includes(tag)) continue;
    if (el.closest('nav, [role="navigation"], .elementor-nav-menu, .menu-main-menu-container, ul.menu, header, footer, .breadcrumb, .breadcrumbs')) continue;
    let vis = true;
    try { vis = el.checkVisibility({checkOpacity: true, checkVisibilityCSS: true}); } catch (e) {
      const r = el.getClientRects(); vis = r.length > 0;
    }
    if (!vis) continue;
    out.push(t);
  }
  return out;
}
"""

async def grab(ctx, url):
    page = await ctx.new_page()
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        # trigger lazy content
        await page.evaluate("async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60));}window.scrollTo(0,0);}")
        await page.wait_for_timeout(1200)
        return await page.evaluate(JS)
    finally:
        await page.close()

def norm(chunks):
    c = Counter()
    for t in chunks:
        t = re.sub(r'\s+', ' ', t).strip()
        t = t.strip('  ·|—–-')
        if len(t) < 3:
            continue
        c[t.lower()] += 1
    return c

async def main():
    urls = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        desk = await browser.new_context(viewport={"width": 1440, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
        mob = await browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True, device_scale_factor=3,
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")
        for i, u in enumerate(urls, 1):
            try:
                d, m = await asyncio.gather(grab(desk, u), grab(mob, u))
                dc, mc = norm(d), norm(m)
                only_d = dc - mc
                only_m = mc - dc
                results.append({"url": u, "desktop_chunks": sum(dc.values()), "mobile_chunks": sum(mc.values()),
                                "desktop_only": list(only_d.elements()), "mobile_only": list(only_m.elements())})
                status = "MATCH" if not only_d and not only_m else f"DIFF (D-only {sum(only_d.values())}, M-only {sum(only_m.values())})"
            except Exception as e:
                results.append({"url": u, "error": str(e)[:200]})
                status = "ERROR"
            print(f"[{i}/{len(urls)}] {status}  {u}", flush=True)
        await browser.close()
    json.dump(results, open(sys.argv[2], "w"), indent=1)

asyncio.run(main())
