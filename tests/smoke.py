"""Browser smoke checks for the built static site.

Prerequisites: Python 3.10+, `pip install playwright`, Chromium installed.
Run the site first: python -m http.server 4321 --directory dist
Run: python tests/smoke.py
Optional: SITE_URL, CHROMIUM_PATH, SCREENSHOT_DIR environment variables.
"""
import os
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
from playwright.sync_api import sync_playwright

BASE = os.environ.get('SITE_URL', 'http://127.0.0.1:4321').rstrip('/')
SHOTS = Path(os.environ.get('SCREENSHOT_DIR', '/tmp/site-qa'))
SHOTS.mkdir(parents=True, exist_ok=True)
PAGES = ['/', '/parcours/', '/programme/', '/lectures/', '/musiques/', '/regards/', '/contact/', '/informations/', '/404.html']
checks = 0
errors = []
links = set()

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        errors.append(message)

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH', '/usr/bin/chromium'), headless=True, args=['--no-sandbox'])
    for width in [1440, 390, 320]:
        context = browser.new_context(viewport={'width': width, 'height': 1000}, device_scale_factor=1)
        context.grant_permissions(['clipboard-read', 'clipboard-write'])
        page = context.new_page()
        console_errors = []
        failed_requests = []
        page.on('pageerror', lambda err: console_errors.append(str(err)))
        page.on('requestfailed', lambda req: failed_requests.append(f'{req.url}: {req.failure}'))
        for route in PAGES:
            response = page.goto(BASE + route, wait_until='networkidle')
            page.evaluate('document.fonts.ready')
            check(response.status == 200, f'{width} {route}: response {response.status}')
            check(page.locator('h1').count() == 1, f'{width} {route}: expected exactly one h1')
            check(page.locator('html').get_attribute('lang') == 'fr', f'{width} {route}: missing French lang')
            check(bool(page.locator('meta[name="description"]').get_attribute('content')), f'{width} {route}: missing description')
            check(page.locator('img:not([alt])').count() == 0, f'{width} {route}: image without alt')
            overflow = page.evaluate('document.documentElement.scrollWidth > innerWidth')
            check(not overflow, f'{width} {route}: horizontal overflow')
            check(page.locator('img').evaluate_all('(imgs) => imgs.every(i => i.complete && i.naturalWidth > 0)'), f'{width} {route}: image failed to load')
            nav = page.locator('#navigation')
            if width < 1101:
                toggle = page.locator('.menu-toggle')
                check(not nav.is_visible(), f'{width} {route}: nav should begin collapsed')
                toggle.click()
                check(toggle.get_attribute('aria-expanded') == 'true' and nav.is_visible(), f'{width} {route}: menu did not open accessibly')
                page.keyboard.press('Escape')
                check(toggle.get_attribute('aria-expanded') == 'false' and not nav.is_visible(), f'{width} {route}: Escape did not close menu')
                check(toggle.evaluate('(el) => el === document.activeElement'), f'{width} {route}: Escape did not return focus')
            else:
                check(nav.is_visible(), f'{width} {route}: desktop nav hidden')
            if route not in ['/404.html', '/informations/']:
                nav_href = route
                check(page.locator(f'#navigation a[href="{nav_href}"][aria-current="page"]').count() == 1, f'{width} {route}: active navigation missing')
            for href in page.locator('a[href]').evaluate_all('(els) => els.map(e => e.getAttribute("href"))'):
                if href.startswith('/') or href.startswith('#'):
                    links.add(urljoin(BASE + route, href))
            if route in ['/', '/contact/', '/programme/']:
                page.screenshot(path=str(SHOTS / f'{width}-{route.strip("/") or "home"}.png'), full_page=True)
            if route == '/contact/':
                page.locator('.copy-email').click()
                page.wait_for_function("document.querySelector('.copy-status').textContent.includes('Adresse copiée')")
                check('Adresse copiée' in page.locator('.copy-status').inner_text(), f'{width}: clipboard success feedback missing')
                check(page.evaluate('navigator.clipboard.readText()') == 'samuelcondesso@live.fr', f'{width}: clipboard value wrong')
                page.evaluate("() => { navigator.clipboard.writeText = async () => {throw new Error('test: unavailable')}; }")
                page.locator('.copy-email').click()
                page.wait_for_function("document.querySelector('.copy-status').textContent.includes('n’est pas disponible')")
                check('n’est pas disponible' in page.locator('.copy-status').inner_text(), f'{width}: clipboard failure feedback missing')
        check(not console_errors, f'{width}: JS errors {console_errors}')
        check(not failed_requests, f'{width}: failed requests {failed_requests}')
        context.close()
    context = browser.new_context()
    page = context.new_page()
    for url in sorted(links):
        parts = urlsplit(url)
        response = page.goto(url.split('#', 1)[0], wait_until='networkidle')
        check(response.status == 200, f'Broken internal link: {url} ({response.status})')
        if parts.fragment:
            check(page.locator(f'[id="{unquote(parts.fragment)}"]').count() == 1, f'Broken fragment: {url}')
    # Navigation should work with a real menu link click, not just direct requests.
    page.set_viewport_size({'width':390, 'height':844})
    page.goto(BASE)
    page.locator('.menu-toggle').click()
    page.locator('#navigation a[href="/parcours/"]').click()
    page.wait_for_url('**/parcours/')
    check(not page.locator('#navigation').is_visible(), 'Mobile navigation did not close after page change')
    page.goto(BASE)
    page.keyboard.press('Tab')
    check(page.locator('.skip-link').evaluate('(el) => el === document.activeElement'), 'Skip link not first in keyboard order')
    page.keyboard.press('Enter')
    check(page.evaluate('location.hash') == '#contenu', 'Skip link did not reach main content')
    browser.close()

print(f'{checks} checks; {len(errors)} failures. Screenshots: {SHOTS}')
for error in errors:
    print('FAIL:', error)
raise SystemExit(1 if errors else 0)
