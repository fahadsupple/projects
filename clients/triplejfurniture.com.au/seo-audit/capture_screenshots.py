from playwright.sync_api import sync_playwright
import time

URL = "https://triplejfurniture.com.au/"
SCREENSHOTS_DIR = "/home/invoi/fahad_projects/clients/triplejfurniture.com.au/seo-audit/screenshots"

viewports = [
    {"name": "desktop", "width": 1920, "height": 1080},
    {"name": "laptop", "width": 1366, "height": 768},
    {"name": "tablet", "width": 768, "height": 1024},
    {"name": "mobile", "width": 375, "height": 812},
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for vp in viewports:
        page = browser.new_page(viewport={"width": vp["width"], "height": vp["height"]})
        page.goto(URL, wait_until="networkidle", timeout=60000)
        time.sleep(2)  # allow lazy-loaded images to settle

        # Above-the-fold (viewport only)
        path_atf = f"{SCREENSHOTS_DIR}/{vp['name']}_atf.png"
        page.screenshot(path=path_atf, full_page=False)
        print(f"Saved: {path_atf}")

        # Full page
        path_full = f"{SCREENSHOTS_DIR}/{vp['name']}_full.png"
        page.screenshot(path=path_full, full_page=True)
        print(f"Saved: {path_full}")

        page.close()
    browser.close()

print("All screenshots captured.")
