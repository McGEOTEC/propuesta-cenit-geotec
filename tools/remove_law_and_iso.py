import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove Ley 1581 item
ley_pattern = r'<div class="sec-item">\s*<span class="sec-item-icon">✓</span>\s*<div>\s*<div class="sec-item-title">Cumplimiento Ley 1581 de 2012</div>[\s\S]*?</div>\s*</div>'
content = re.sub(ley_pattern, '', content)

# Remove ISO 27001 projection item
iso_pattern = r'<div class="sec-item">\s*<span class="sec-item-icon">→</span>\s*<div>\s*<div class="sec-item-title">Proyección de Certificación ISO 27001 / SOC 2</div>[\s\S]*?</div>\s*</div>'
content = re.sub(iso_pattern, '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed Ley 1581 and ISO 27001 projection successfully!")
