from playwright.sync_api import sync_playwright

URL = "https://triplejfurniture.com.au/"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto(URL, wait_until="networkidle", timeout=60000)

    # Phone number in header
    phone_els = page.query_selector_all("a[href^='tel:']")
    print("=== PHONE LINKS ===")
    for el in phone_els:
        print(f"  href={el.get_attribute('href')}  text={el.inner_text().strip()}")

    # Address / NAP
    print("\n=== FOOTER TEXT (first 2000 chars) ===")
    footer = page.query_selector("footer")
    if footer:
        print(footer.inner_text()[:2000])
    else:
        print("No <footer> element found")

    # H1
    print("\n=== H1 TAGS ===")
    for h in page.query_selector_all("h1"):
        print(f"  {h.inner_text().strip()}")

    # H2 (first 10)
    print("\n=== H2 TAGS (first 10) ===")
    for i, h in enumerate(page.query_selector_all("h2")):
        if i >= 10:
            break
        print(f"  {h.inner_text().strip()}")

    # Navigation links
    print("\n=== MAIN NAV LINKS ===")
    nav = page.query_selector("nav, header nav, .nav, #nav")
    if nav:
        for a in nav.query_selector_all("a"):
            txt = a.inner_text().strip()
            if txt:
                print(f"  {txt}")

    # Trust / review badge text
    print("\n=== TRUST / REVIEW ELEMENTS ===")
    trust_selectors = [
        ".trustpilot", ".reviews", ".rating", ".badge",
        "[class*='trust']", "[class*='review']", "[class*='stars']",
        "[class*='guarantee']", "[class*='warranty']"
    ]
    for sel in trust_selectors:
        els = page.query_selector_all(sel)
        for el in els:
            txt = el.inner_text().strip()
            if txt:
                print(f"  [{sel}] {txt[:120]}")

    # CTA buttons above fold
    print("\n=== BUTTONS / CTA TEXT ===")
    for btn in page.query_selector_all("a.btn, button, .btn, [class*='button'], [class*='cta']"):
        txt = btn.inner_text().strip()
        if txt and len(txt) < 80:
            print(f"  {txt}")

    # Check for horizontal overflow at mobile
    page2 = browser.new_page(viewport={"width": 375, "height": 812})
    page2.goto(URL, wait_until="networkidle", timeout=60000)
    scroll_width = page2.evaluate("document.body.scrollWidth")
    client_width = page2.evaluate("document.body.clientWidth")
    print(f"\n=== MOBILE OVERFLOW CHECK (375px) ===")
    print(f"  body.scrollWidth={scroll_width}  body.clientWidth={client_width}")
    print(f"  Horizontal overflow: {'YES' if scroll_width > client_width else 'NO'}")

    browser.close()
