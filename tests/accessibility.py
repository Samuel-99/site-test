"""Audit axe-core WCAG A/AA des pages exportées (desktop et mobile).

Installer npm ci, Python playwright et Chromium ; démarrer npm run preview.
SITE_URL=http://127.0.0.1:4321 python tests/accessibility.py
Ne remplace pas une évaluation manuelle de l'accessibilité.
"""
import json
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

base = os.environ.get('SITE_URL', 'http://127.0.0.1:4321').rstrip('/')
routes = ['/', '/parcours/', '/programme/', '/lectures/', '/musiques/', '/regards/', '/contact/', '/informations/', '/404.html']
axe = Path(__file__).resolve().parents[1] / 'node_modules/axe-core/axe.min.js'
failures = {}
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH', '/usr/bin/chromium'), headless=True, args=['--no-sandbox'])
    for width in [1440, 390]:
        page = browser.new_page(viewport={'width': width, 'height': 1000})
        for route in routes:
            page.goto(base + route, wait_until='networkidle')
            page.add_script_tag(path=str(axe))
            violations = page.evaluate("""async () => (await axe.run(document, {
                runOnly: {type: 'tag', values: ['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}
            })).violations.map(v => ({id: v.id, nodes: v.nodes.map(n => ({target: n.target, reason: n.failureSummary}))}))""")
            if violations:
                failures[f'{width} {route}'] = violations
        page.close()
    browser.close()
print(f'{len(routes) * 2} audits axe-core ; {len(failures)} pages avec violations détectées.')
if failures:
    print(json.dumps(failures, ensure_ascii=False, indent=2))
raise SystemExit(bool(failures))
