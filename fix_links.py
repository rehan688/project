import os
import pathlib
import re

root = pathlib.Path(__file__).parent
html_files = list(root.rglob('*.html'))

# Map renamed targets where local file names differ from reference labels.
renames = {
    'products/products-chownow-app.html': 'products/products-marketplace.html',
    'products/products-order-better-network.html': 'products/products-discovery-network.html',
    'products/products-q2-feature-release.html': 'products/products-q2-feature-release.html',
    '/Aitisal/login.html': 'login.html',
    '/Aitisal/pricing.html': 'pricing.html',
    '/Aitisal/get-started.html': 'get-started.html',
}

for path in html_files:
    text = path.read_text(encoding='utf-8')
    original = text
    # Rewrite /Aitisal absolute references to local relative paths.
    text = text.replace('/Aitisal/', '')
    # Replace known renamed pages.
    text = text.replace('products/products-chownow-app.html', 'products/products-marketplace.html')
    text = text.replace('products/products-order-better-network.html', 'products/products-discovery-network.html')
    text = text.replace('/Aitisal/login.html', 'login.html')
    text = text.replace('/Aitisal/pricing.html', 'pricing.html')
    text = text.replace('/Aitisal/get-started.html', 'get-started.html')
    if text != original:
        path.write_text(text, encoding='utf-8')
        print(f'Updated {path}')
