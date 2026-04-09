#!/usr/bin/env python3
"""
Crawl a website and count internal links pointing to a target URL.
Uses curl for fetching (bypasses Cloudflare) + Python stdlib for parsing.
Usage: python3 crawl_internal_links.py <target_url>
"""

import sys
import subprocess
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
import time

def fetch(url, timeout=15):
    """Fetch URL content using curl (handles Cloudflare better than urllib)."""
    try:
        result = subprocess.run(
            ['curl', '-s', '-L', '-A',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
             '--max-time', str(timeout), url],
            capture_output=True, text=True, timeout=timeout + 5
        )
        if result.returncode == 0:
            return result.stdout
    except:
        pass
    return None

def normalize_url(url):
    parsed = urlparse(url)
    path = parsed.path.rstrip('/')
    return f"{parsed.scheme}://{parsed.netloc}{path}".lower()


class LinkFinder(HTMLParser):
    def __init__(self, base_url, target_normalized):
        super().__init__()
        self.base_url = base_url
        self.target_normalized = target_normalized
        self.nav_depth = 0
        self.in_link = False
        self.current_anchor = ''
        self.current_is_nav = False
        self.links = []
        self.nav_tags = {'nav', 'header', 'footer'}
        self.nav_words = ['nav', 'menu', 'header', 'footer', 'sidebar', 'widget', 'breadcrumb', 'navigation']

    def _check_nav(self, tag, attrs):
        if tag in self.nav_tags:
            return True
        attrs_dict = dict(attrs)
        for attr in ['class', 'id', 'role']:
            val = attrs_dict.get(attr, '').lower()
            if any(w in val for w in self.nav_words):
                return True
        return False

    def handle_starttag(self, tag, attrs):
        if self._check_nav(tag, attrs):
            self.nav_depth += 1
        if tag == 'a':
            href = dict(attrs).get('href', '')
            if href:
                full_url = urljoin(self.base_url, href)
                if normalize_url(full_url) == self.target_normalized:
                    self.in_link = True
                    self.current_anchor = ''
                    self.current_is_nav = self.nav_depth > 0

    def handle_data(self, data):
        if self.in_link:
            self.current_anchor += data

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_link:
            self.links.append({
                'anchor_text': self.current_anchor.strip(),
                'is_nav': self.current_is_nav
            })
            self.in_link = False
        if tag in self.nav_tags:
            self.nav_depth = max(0, self.nav_depth - 1)


class SitemapParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_loc = False
        self.urls = []
        self.current_text = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'loc':
            self.in_loc = True
            self.current_text = ''

    def handle_data(self, data):
        if self.in_loc:
            self.current_text += data

    def handle_endtag(self, tag):
        if tag == 'loc' and self.in_loc:
            self.urls.append(self.current_text.strip())
            self.in_loc = False


def get_sitemap_urls(domain):
    urls = set()
    content = fetch(f"https://{domain}/sitemap.xml")
    if not content:
        return urls

    parser = SitemapParser()
    try:
        parser.feed(content)
    except:
        return urls

    for url in parser.urls:
        if url.endswith('.xml'):
            sub = fetch(url)
            if sub:
                sp = SitemapParser()
                try:
                    sp.feed(sub)
                    for u in sp.urls:
                        if domain in u:
                            urls.add(u)
                except:
                    pass
        else:
            if domain in url:
                urls.add(url)
    return urls


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 crawl_internal_links.py <target_url>")
        sys.exit(1)

    target_url = sys.argv[1]
    target_normalized = normalize_url(target_url)
    domain = urlparse(target_url).netloc

    print(f"\nCrawling to find internal links pointing to: {target_url}")
    print(f"{'='*70}\n")

    urls = get_sitemap_urls(domain)
    print(f"Found {len(urls)} URLs from sitemap")

    if not urls:
        urls.add(f"https://{domain}/")

    nav_links = []
    contextual_links = []
    pages_crawled = 0
    errors = 0

    sorted_urls = sorted(urls)
    total = len(sorted_urls)

    for i, url in enumerate(sorted_urls):
        if normalize_url(url) == target_normalized:
            continue

        html = fetch(url)
        if not html:
            errors += 1
            continue

        pages_crawled += 1

        try:
            parser = LinkFinder(url, target_normalized)
            parser.feed(html)

            for link in parser.links:
                entry = {
                    'source_url': url,
                    'anchor_text': link['anchor_text'],
                    'is_nav': link['is_nav']
                }
                if link['is_nav']:
                    nav_links.append(entry)
                else:
                    contextual_links.append(entry)
        except:
            errors += 1

        if (i + 1) % 20 == 0:
            print(f"  Crawled {i + 1}/{total} pages...")

        if (i + 1) % 5 == 0:
            time.sleep(0.2)

    # Deduplicate
    nav_sources = set(l['source_url'] for l in nav_links)
    nav_anchors = set(l['anchor_text'] for l in nav_links if l['anchor_text'])

    unique_contextual = {}
    for link in contextual_links:
        key = f"{link['source_url']}|{link['anchor_text']}"
        if key not in unique_contextual:
            unique_contextual[key] = link

    # Output
    print(f"\n{'='*70}")
    print(f"RESULTS FOR: {target_url}")
    print(f"{'='*70}")
    print(f"\nPages crawled: {pages_crawled}")
    print(f"Errors/skipped: {errors}")

    print(f"\n--- NAVIGATIONAL LINKS (nav/header/footer/menu) ---")
    if nav_anchors:
        print(f"Present on ~{len(nav_sources)} pages (sitewide)")
        print(f"Anchor texts: {', '.join(sorted(nav_anchors))}")
    else:
        print("None found")

    print(f"\n--- CONTEXTUAL LINKS (in-content/body) ---")
    print(f"Total unique contextual links: {len(unique_contextual)}")

    if unique_contextual:
        print(f"\n{'Source Page':<70} | {'Anchor Text'}")
        print(f"{'-'*70}-+-{'-'*40}")
        for link in unique_contextual.values():
            source_short = link['source_url'].replace(f"https://{domain}", '')
            anchor = link['anchor_text'][:40] if link['anchor_text'] else '(empty)'
            print(f"{source_short:<70} | {anchor}")
    else:
        print("NO contextual links found!")

    total_ctx = len(unique_contextual)
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"Navigational (sitewide) links: {'Yes (' + str(len(nav_sources)) + ' pages)' if nav_anchors else 'No'}")
    print(f"Contextual (in-content) links: {total_ctx}")

    if total_ctx == 0:
        print(f"\nRECOMMENDATION: ZERO contextual links. Needs 5-9 new contextual links from relevant pages.")
    elif total_ctx < 3:
        needed = 5 - total_ctx
        print(f"\nRECOMMENDATION: UNDER-LINKED ({total_ctx}). Needs {needed}-{needed+3} more contextual links.")
    elif total_ctx <= 9:
        remaining = 9 - total_ctx
        if remaining > 0:
            print(f"\nRECOMMENDATION: Healthy count ({total_ctx}). Can add up to {remaining} more if relevant.")
        else:
            print(f"\nRECOMMENDATION: Healthy count ({total_ctx}). No urgent need for more links.")
    elif total_ctx <= 15:
        print(f"\nRECOMMENDATION: Sufficient links ({total_ctx}). Only add more for new highly relevant content.")
    else:
        print(f"\nRECOMMENDATION: MANY links ({total_ctx}). No additional links needed — over-optimization risk.")


if __name__ == '__main__':
    main()
