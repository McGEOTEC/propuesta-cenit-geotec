import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove watermark cap-num 02 and 03
content = re.sub(r'<span class="cap-num"[^>]*>02</span>\s*', '', content)
content = re.sub(r'<span class="cap-num"[^>]*>03</span>\s*', '', content)

# 2. Remove the figure from linea-2
figure_pattern = r'<figure class="oficina-figure"[\s\S]*?</figure>\s*'
content = re.sub(figure_pattern, '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html: cap-num 02/03 and linea-2 photo removed!")
