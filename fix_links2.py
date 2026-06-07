import os
import pathlib
import re
from urllib.parse import urlsplit, urlunsplit

root = pathlib.Path(__file__).parent
existing = {p.relative_to(root).as_posix(): p for p in root.rglob('*.html')}

alias = {}

def add_alias(key, target):
    key = key.lstrip('/')
    if not key:
        return
    alias[key] = target
    if key.endswith('.html'):
        alias[key[:-5]] = target
    if key.endswith('/'):
        alias[key[:-1]] = target

root_aliases = {
    'login': 'login.html',
    'refer': 'refer.html',
    'pricing': 'pricing.html',
    'get-started': 'get-started.html',
    'legal-terms': 'legal-terms.html',
    'legal-privacy': 'legal-privacy.html',
    'legal-ca-privacy': 'legal-ca-privacy.html',
    'legal-refund': 'legal-refund.html',
}
for k, v in root_aliases.items():
    add_alias(k, v)
    add_alias(f'{k}.html', v)

company_pages = ['why-chownow', 'about', 'reviews', 'careers', 'contact']
for page in company_pages:
    add_alias(f'company/{page}.html', f'company/{page}.html')
    add_alias(f'company/{page}', f'company/{page}.html')
    add_alias(f'{page}.html', f'company/{page}.html')
    add_alias(page, f'company/{page}.html')

for key in ['company/refer-a-restaurant', 'company/refer', 'company/refer.html', 'refer.html', 'refer']:
    add_alias(key, 'refer.html')

for key in ['company/partners', 'company/partners.html', 'partners', 'partners.html']:
    add_alias(key, 'company/partners.html')

add_alias('affiliates/partner-signup', 'affiliates/partner-signup.html')
add_alias('affiliates/partner-signup.html', 'affiliates/partner-signup.html')

resource_pages = {
    'blog': 'resources/blog.html',
    'diner-support': 'resources/diner-support.html',
    'resources-case-studies': 'resources/resources-case-studies.html',
    'resources-guides': 'resources/resources-guides.html',
    'resources-marketing': 'resources/resources-marketing.html',
    'support': 'resources/support.html',
}
for key, target in resource_pages.items():
    add_alias(f'resources/{key}.html', target)
    add_alias(f'resources/{key}', target)
    add_alias(f'{key}.html', target)
    add_alias(key, target)

product_pages = {
    'online-ordering': 'products/products-online-ordering.html',
    'mobile-apps': 'products/products-mobile-apps.html',
    'website-builder': 'products/products-website-builder.html',
    'marketplace': 'products/products-marketplace.html',
    'discovery-network': 'products/products-discovery-network.html',
    'catering': 'products/products-catering.html',
    'qr-code': 'products/products-qr-code.html',
    'email-sms': 'products/products-email-sms.html',
    'rewards': 'products/products-rewards.html',
    'flex-delivery': 'products/products-flex-delivery.html',
    'order-aggregation': 'products/products-order-aggregation.html',
    'advanced-reporting': 'products/products-advanced-reporting.html',
    'products-q2-feature-release': 'products/products-q2-feature-release.html',
    'restaurant-websites': 'products/products-website-builder.html',
    'chownow-app': 'products/products-marketplace.html',
    'order-better-network': 'products/products-discovery-network.html',
}
for key, target in product_pages.items():
    add_alias(f'products/{key}.html', target)
    add_alias(f'products/{key}', target)
    add_alias(f'{key}.html', target)
    add_alias(key, target)
    add_alias(f'products-{key}.html', target)

integration_pages = {
    'all': 'integrations/all.html',
    'clover': 'integrations/clover.html',
    'doordash': 'integrations/doordash.html',
    'genius': 'integrations/genius.html',
    'google': 'integrations/google.html',
    'grubhub': 'integrations/integrations-grubhub.html',
    'revel': 'integrations/integrations-revel.html',
    'skytab': 'integrations/integrations-skytab.html',
    'square': 'integrations/integrations-square.html',
    'toast': 'integrations/integrations-toast.html',
    'uber-eats': 'integrations/integrations-ubereats.html',
    'ubereats': 'integrations/integrations-ubereats.html',
    'apple-maps': 'integrations/apple-maps.html',
    'yelp': 'integrations/yelp.html',
}
for key, target in integration_pages.items():
    add_alias(f'integrations/{key}.html', target)
    add_alias(f'integrations/{key}', target)
    add_alias(f'{key}.html', target)
    add_alias(key, target)
    add_alias(f'integrations-{key}.html', target)

legal_pages = {
    'terms': 'legal-terms.html',
    'privacy': 'legal-privacy.html',
    'ca-privacy': 'legal-ca-privacy.html',
    'refund': 'legal-refund.html',
}
for key, target in legal_pages.items():
    add_alias(f'legal/{key}.html', target)
    add_alias(f'legal/{key}', target)
    add_alias(f'{key}.html', target)
    add_alias(key, target)

add_alias('support/diner-support.html', 'resources/diner-support.html')
add_alias('support/restaurant-support.html', 'resources/support.html')
add_alias('support/restaurant-support', 'resources/support.html')

case_study_aliases = [
    'case-4top.html', 'case-emporium.html', 'case-ingrained.html', 'case-ollies.html',
    'case-renegade.html', 'case-sushi-zen.html',
    'case-studies/4top.html', 'case-studies/emporium.html', 'case-studies/ingrained.html',
    'case-studies/ollies.html', 'case-studies/renegade.html', 'case-studies/sushi-zen.html',
]
for key in case_study_aliases:
    add_alias(key, 'resources/resources-case-studies.html')

add_alias('resources-support.html', 'resources/support.html')
add_alias('seo-for-restaurants.html', 'resources/seo-for-restaurants.html')
add_alias('resources-seo-for-restaurants.html', 'resources/seo-for-restaurants.html')
add_alias('integrations-genius.html', 'integrations/genius.html')
add_alias('integrations-doordash.html', 'integrations/doordash.html')
add_alias('integrations-google.html', 'integrations/google.html')
add_alias('integrations-grubhub.html', 'integrations/integrations-grubhub.html')
add_alias('integrations-revel.html', 'integrations/integrations-revel.html')
add_alias('integrations-skytab.html', 'integrations/integrations-skytab.html')
add_alias('integrations-square.html', 'integrations/integrations-square.html')
add_alias('integrations-toast.html', 'integrations/integrations-toast.html')
add_alias('integrations-uber-eats.html', 'integrations/integrations-ubereats.html')
add_alias('integrations-apple-maps.html', 'integrations/apple-maps.html')
add_alias('integrations-yelp.html', 'integrations/yelp.html')
add_alias('resources-guides.html', 'resources/resources-guides.html')
add_alias('resources-marketing.html', 'resources/resources-marketing.html')
add_alias('resources-case-studies.html', 'resources/resources-case-studies.html')
add_alias('resources-blog.html', 'resources/blog.html')
add_alias('resources-diner-support.html', 'resources/diner-support.html')
add_alias('resources-support.html', 'resources/support.html')
add_alias('case-studies/atchanas.html', 'resources/resources-case-studies.html')
add_alias('case-atchanas.html', 'resources/resources-case-studies.html')

for path in existing:
    add_alias(path, path)
    if path.endswith('.html'):
        add_alias(path[:-5], path)

stub_pages = {
    'login.html': 'Login',
    'refer.html': 'Refer a Restaurant',
    'company/partners.html': 'Our Partners',
    'affiliates/partner-signup.html': 'Partner Signup',
    'resources/seo-for-restaurants.html': 'SEO for Restaurants',
    'integrations/google.html': 'Google Integration',
    'integrations/apple-maps.html': 'Apple Maps Integration',
    'integrations/yelp.html': 'Yelp Integration',
    'products/products-q2-feature-release.html': 'Q2 Feature Release',
    'legal-terms.html': 'Terms',
    'legal-privacy.html': 'Privacy Policy',
    'legal-ca-privacy.html': 'California Privacy Notice',
    'legal-refund.html': 'Refund Policy',
}

def stub_html(title):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | ChowNow</title>
  <meta name="description" content="{title} page placeholder for the ChowNow local copy.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Condensed:wght@400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600;700&family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {{ margin: 0; font-family: 'Roboto', sans-serif; background: #f8f8f8; color: #161616; }}
    a {{ color: #161616; text-decoration: none; }}
  </style>
</head>
<body class="min-h-screen bg-cn-bg">
  <main class="max-w-5xl mx-auto px-6 py-20">
    <h1 class="text-4xl font-bold mb-6">{title}</h1>
    <p class="text-lg text-cn-gray mb-8">This page was added so the local ChowNow copy resolves existing menu and footer links correctly.</p>
    <div class="flex items-center gap-4">
      <a href="/index.html" class="inline-flex items-center gap-2 rounded-full bg-cn-black px-6 py-3 text-white">Home</a>
      <a href="/pricing.html" class="inline-flex items-center gap-2 rounded-full border border-cn-black px-6 py-3 text-cn-black">Pricing</a>
    </div>
  </main>
</body>
</html>'''

for rel_path, title in stub_pages.items():
    stub_path = root / rel_path
    stub_path.parent.mkdir(parents=True, exist_ok=True)
    if not stub_path.exists():
        stub_path.write_text(stub_html(title), encoding='utf-8')
        print(f'Created stub {stub_path}')

link_re = re.compile(r'(<a[^>]+href=["\'])([^"\']+)(["\'])', re.IGNORECASE)

def compute_relative(from_path, to_path):
    return pathlib.Path(os.path.relpath(to_path, start=from_path.parent)).as_posix()

def resolve_target(page_path, href):
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        return href
    if not parsed.path or parsed.path.startswith('#'):
        return href
    clean_target = parsed.path.lstrip('/')
    actual = None
    candidate = (page_path.parent / clean_target).resolve()
    try:
        rel = candidate.relative_to(root).as_posix()
        if rel in existing:
            actual = rel
    except Exception:
        pass
    if actual is None and clean_target in alias:
        actual = alias[clean_target]
    if actual is None and clean_target in existing:
        actual = clean_target
    if actual is None and not clean_target.endswith('.html'):
        alt = f'{clean_target}.html'
        if alt in existing:
            actual = alt
        elif alt in alias:
            actual = alias[alt]
    if actual is None:
        return href
    to_path = root / actual
    relative_path = compute_relative(page_path, to_path)
    rebuilt = urlunsplit(('', '', relative_path, parsed.query, parsed.fragment))
    return rebuilt

for path in sorted(root.rglob('*.html')):
    text = path.read_text(encoding='utf-8', errors='ignore')
    new_text = link_re.sub(lambda m: m.group(1) + resolve_target(path, m.group(2)) + m.group(3), text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        print(f'Normalized links in {path}')
