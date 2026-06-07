import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = 'assets/placeholder.svg'
STYLE_LINK = '<link rel="stylesheet" href="assets/styles.css">'

html_files = list(ROOT.rglob('*.html'))
exclude = [ROOT / 'assets']

for f in html_files:
    # skip files in assets
    if 'assets' + os.sep in str(f):
        continue
    text = f.read_text(encoding='utf-8')
    orig = text
    # add stylesheet link if missing
    if 'assets/styles.css' not in text:
        # insert before </head>
        if '</head>' in text:
            text = text.replace('</head>', STYLE_LINK + '\n</head>')
    # replace remote img src attributes with placeholder
    import re
    # pattern to match <img ... src="http[s]://..." ...>
    def repl_img(match):
        tag = match.group(0)
        # replace src value
        tag = re.sub(r'src\s*=\s*"[^"]+"', f'src="{PLACEHOLDER}"', tag)
        return tag
    text = re.sub(r'<img\s+[^>]*src\s*=\s*"https?://[^"]+"[^>]*>', repl_img, text, flags=re.IGNORECASE)

    if text != orig:
        bak = f.with_suffix(f.suffix + '.bak')
        bak.write_text(orig, encoding='utf-8')
        f.write_text(text, encoding='utf-8')
        print(f'Updated {f.relative_to(ROOT)}')
print('Done')
