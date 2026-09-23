import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'/\* --- TIMELINE[\s\S]*?(?=\n/\*|\n\.|\n#|\n@media)', text)
if not m:
    m = re.search(r'\.timeline\s*\{[\s\S]*?(?=\n\n|\n/\*)', text)

if m:
    print(m.group(0))
else:
    # search for .tl-node
    m2 = re.search(r'\.tl-node[\s\S]*?(?=\n\n/\*|\n\.section)', text)
    if m2:
        print(m2.group(0))
