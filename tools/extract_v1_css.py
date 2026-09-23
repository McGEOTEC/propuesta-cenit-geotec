import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index_v1_original.html', encoding='utf-8') as f:
    v1_text = f.read()

# Let's extract the exact CSS for sections 2 and 3-7 from v1
import re
css_start = v1_text.find('/* ============================================================')
css_end = v1_text.find('</style>')
v1_css = v1_text[css_start:css_end]

# Let's see CSS related to section-head, cap-num, eyebrow, split-2, cierre, kw, capsules, linea, details
classes = ['cap-num', 'eyebrow', 'split-2', 'cierre', 'kw', 'capsules', 'capsule', 'lines-hint', 'linea', 'linea-num', 'linea-title', 'linea-sub', 'linea-chev', 'linea-body', 'linea-trio', 'dato', 'weave-divider']

for c in classes:
    matches = re.findall(rf'(\.{c}[^{{]*\{{[^}}]*\}})', v1_css)
    print(f'=== Matches for .{c} ===')
    for m in matches[:3]:
        print(m[:200])
