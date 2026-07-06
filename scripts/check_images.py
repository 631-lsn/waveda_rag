"""Check if image paths in chunks resolve correctly"""
import json, os, re

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(base, 'data/index/chunks.json'), 'r', encoding='utf-8') as f:
    chunks = json.load(f)

found = 0
for c in chunks:
    content = c.get('content', '')
    if 'images/' not in content:
        continue
    # Extract image paths from chunk content
    for line in content.split('\n'):
        if 'images/' not in line or '.png' not in line:
            continue
        # Try simple extraction: find images/xxx.png
        m = re.search(r'images/[^\s\"\'\)\]]+\.png', line)
        if not m:
            continue
        img_name = m.group(0)
        help_base = os.path.join(base, 'wavEDA_docs', 'helpHtml', 'helpHtml')
        for root, dirs, files in os.walk(help_base):
            if 'images' in dirs:
                candidate = os.path.join(root, os.path.basename(img_name))
                if os.path.exists(candidate):
                    found += 1
                    if found <= 3:
                        print(f'OK: {c["title"]} -> {candidate}')
                    break
        break

print(f'\nTotal resolvable images: {found}')
print(f'HelpHtml base: {help_base}')
print(f'Images/ dirs found: {sum(1 for r,d,f in os.walk(help_base) if "images" in d)}')
