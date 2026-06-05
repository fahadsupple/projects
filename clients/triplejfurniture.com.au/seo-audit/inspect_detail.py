from playwright.sync_api import sync_playwright

URL = "https://triplejfurniture.com.au/"

with sync_playwright() as p:
    browser = p.chromium.launch()

    # ---- Desktop: hero/banner text, price beat, USP bars ----
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto(URL, wait_until="networkidle", timeout=60000)

    print("=== HERO / SLIDER TEXT ===")
    for sel in [".hero", ".slider", ".banner", "[class*='hero']", "[class*='slide']", "[class*='banner']"]:
        els = page.query_selector_all(sel)
        for el in els:
            txt = el.inner_text().strip()
            if txt and len(txt) < 400:
                print(f"  [{sel}]: {txt[:300]}")

    print("\n=== ANNOUNCEMENT BAR / TOP BAR ===")
    for sel in [".announcement", "[class*='announcement']", "[class*='topbar']", "[class*='top-bar']",
                "[class*='promo']", ".site-header__promo", "#shopify-section-announcement"]:
        els = page.query_selector_all(sel)
        for el in els:
            txt = el.inner_text().strip()
            if txt:
                print(f"  [{sel}]: {txt[:200]}")

    print("\n=== ADDRESS TEXT IN PAGE ===")
    body_text = page.inner_text("body")
    lines = [l.strip() for l in body_text.split('\n') if l.strip()]
    addr_keywords = ["yagoona", "hume", "590", "nsw 2199", "showroom", "address"]
    for line in lines:
        if any(kw in line.lower() for kw in addr_keywords):
            print(f"  {line}")

    print("\n=== PRICE BEAT / GUARANTEE TEXT ===")
    for line in lines:
        if any(kw in line.lower() for kw in ["price beat", "guarantee", "warranty", "free delivery", "free shipping"]):
            print(f"  {line}")

    print("\n=== REVIEW / STAR RATING VISIBLE TEXT ===")
    for line in lines:
        if any(kw in line.lower() for kw in ["review", "rating", "stars", "google", "trust", "customer"]):
            print(f"  {line[:150]}")

    print("\n=== STICKY / FIXED ELEMENTS (mobile) ===")
    page2 = browser.new_page(viewport={"width": 375, "height": 812})
    page2.goto(URL, wait_until="networkidle", timeout=60000)
    fixed_els = page2.evaluate("""
        () => {
            const results = [];
            document.querySelectorAll('*').forEach(el => {
                const style = window.getComputedStyle(el);
                if (style.position === 'fixed' || style.position === 'sticky') {
                    const rect = el.getBoundingClientRect();
                    if (rect.width > 0 && rect.height > 0) {
                        results.push({
                            tag: el.tagName,
                            class: el.className.toString().slice(0, 60),
                            top: rect.top,
                            height: rect.height,
                            width: rect.width,
                            position: style.position
                        });
                    }
                }
            });
            return results.slice(0, 20);
        }
    """)
    for el in fixed_els:
        print(f"  {el['tag']} .{el['class']} | pos={el['position']} top={el['top']:.0f} h={el['height']:.0f} w={el['width']:.0f}")

    print("\n=== MOBILE NAV HAMBURGER ===")
    for sel in ["[class*='hamburger']", "[class*='menu-toggle']", "[class*='mobile-nav']",
                "[class*='nav-toggle']", "[aria-label='menu']", ".mobile-menu"]:
        els = page2.query_selector_all(sel)
        for el in els:
            bb = el.bounding_box()
            if bb:
                print(f"  [{sel}] w={bb['width']:.0f} h={bb['height']:.0f} x={bb['x']:.0f} y={bb['y']:.0f}")

    print("\n=== HEADER HEIGHT MOBILE ===")
    header = page2.query_selector("header")
    if header:
        bb = header.bounding_box()
        print(f"  header: w={bb['width']:.0f} h={bb['height']:.0f}")

    print("\n=== HERO IMAGE ALT / SRC ===")
    page3 = browser.new_page(viewport={"width": 1920, "height": 1080})
    page3.goto(URL, wait_until="networkidle", timeout=60000)
    imgs = page3.query_selector_all("img")
    print(f"  Total images on page: {len(imgs)}")
    for i, img in enumerate(imgs[:15]):
        src = img.get_attribute("src") or ""
        alt = img.get_attribute("alt") or "(no alt)"
        loading = img.get_attribute("loading") or "eager"
        bb = img.bounding_box()
        size = f"w={bb['width']:.0f} h={bb['height']:.0f}" if bb else "not visible"
        print(f"  [{i}] {size} loading={loading} alt='{alt[:60]}' src={src[-60:]}")

    browser.close()
