import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace if 1, 2, 3, 4
text = re.sub(r'<span class="tl-dot" aria-hidden="true">1</span>', '<span class="tl-dot" aria-hidden="true">01</span>', text)
text = re.sub(r'<span class="tl-dot" aria-hidden="true">2</span>', '<span class="tl-dot" aria-hidden="true">02</span>', text)
text = re.sub(r'<span class="tl-dot" aria-hidden="true">3</span>', '<span class="tl-dot" aria-hidden="true">03</span>', text)
text = re.sub(r'<span class="tl-dot" aria-hidden="true">4</span>', '<span class="tl-dot" aria-hidden="true">04</span>', text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

dots = re.findall(r'<span class="tl-dot"[^>]*>(.*?)</span>', text)
print("Timeline dots in index.html:", dots)
