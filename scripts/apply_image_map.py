import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
placeholder = 'assets/placeholder.svg'

rules = [
    (re.compile(r'hero|restaurant ordering|ChowNow customer review ratings', re.I), 'assets/hero.svg'),
    (re.compile(r'ordering features|Ordering features', re.I), 'assets/ordering.svg'),
    (re.compile(r'marketing features', re.I), 'assets/marketing.svg'),
    (re.compile(r'operations features', re.I), 'assets/operations.svg'),
    (re.compile(r'team member|author|team|office', re.I), 'assets/team-member.svg'),
    (re.compile(r'office|ChowNow office', re.I), 'assets/office.svg'),
    (re.compile(r'guide|guides|guide-card', re.I), 'assets/guide-card.svg'),
    (re.compile(r'blog|customer success story|marketing strategies|restaurant technology|online ordering setup|industry trends', re.I), 'assets/blog-card.svg'),
    (re.compile(r'case study|Ollie|Renegade Burrito|Sushi-Zen|ingrained|4Top|Emporium Thai', re.I), 'assets/case-study.svg'),
    (re.compile(r'Toast|Square|Revel|Clover|Lightspeed|Positouch|Skytab|Genius|ChowNow', re.I), 'assets/logo.svg'),
    (re.compile(r'discovery network|delivery app|POS|product|marketplace|mobile app|QR code|rewards|catering|reporting|analytics|dashboard', re.I), 'assets/product.svg'),
]

html_files = list(ROOT.rglob('*.html'))
for path in html_files:
    text = path.read_text(encoding='utf-8')
    if placeholder not in text:
        continue
    original = text
    def repl(match):
        tag = match.group(0)
        alt_match = re.search(r'alt="([^"]*)"', tag, re.I)
        alt = alt_match.group(1) if alt_match else ''
        target = 'assets/product.svg'
        for pattern, image in rules:
            if pattern.search(alt):
                target = image
                break
        return tag.replace(placeholder, target)
    text = re.sub(r'<img[^>]+src="assets/placeholder\.svg"[^>]*>', repl, text, flags=re.I)
    if text != original:
        backup = path.with_suffix(path.suffix + '.bak')
        backup.write_text(original, encoding='utf-8')
        path.write_text(text, encoding='utf-8')
        print(f'Updated {path.relative_to(ROOT)}')
print('Done mapping images.')
