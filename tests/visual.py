"""Compare les 9 pages d'un export de référence et d'un export réorganisé.

python tests/visual.py --reference http://127.0.0.1:4340 --candidate http://127.0.0.1:4341
Même navigateur et mêmes dimensions : les captures doivent être identiques.
Les différences sont enregistrées dans /tmp/site-visual-comparison.
"""
import argparse
from pathlib import Path
from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--reference', required=True)
parser.add_argument('--candidate', required=True)
args = parser.parse_args()
routes = ['/', '/parcours/', '/programme/', '/lectures/', '/musiques/', '/regards/', '/contact/', '/informations/', '/404.html']
output = Path('/tmp/site-visual-comparison')
output.mkdir(exist_ok=True)
failures = []
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True, args=['--no-sandbox'])
    for width in [1440, 1024, 390, 320]:
        for route in routes:
            captures = []
            for origin in [args.reference, args.candidate]:
                page = browser.new_page(viewport={'width': width, 'height': 1000}, reduced_motion='reduce')
                response = page.goto(origin.rstrip('/') + route, wait_until='networkidle')
                assert response.status == 200, (origin, route, response.status)
                page.evaluate('document.fonts.ready')
                captures.append(page.screenshot(full_page=True, animations='disabled'))
                page.close()
            if captures[0] != captures[1]:
                label = f'{width}-{route.strip("/") or "accueil"}'
                failures.append(label)
                for name, capture in zip(['avant', 'apres'], captures):
                    (output / f'{label}-{name}.png').write_bytes(capture)
    browser.close()
print(f'36 comparaisons visuelles ; {len(failures)} différences.')
for failure in failures:
    print(f'DIFF : {failure}')
raise SystemExit(bool(failures))
