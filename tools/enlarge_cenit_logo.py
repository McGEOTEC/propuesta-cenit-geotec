import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_cenit_css = """.logo-cenit-nav {
  height: 28px;
  width: auto;
  object-fit: contain;
}"""

new_cenit_css = """.logo-cenit-nav {
  height: 38px;
  max-height: 42px;
  width: auto;
  object-fit: contain;
}"""

if old_cenit_css in content:
    content = content.replace(old_cenit_css, new_cenit_css)
    print("Replaced logo-cenit-nav CSS directly!")
else:
    content = re.sub(
        r'\.logo-cenit-nav\s*\{[^}]*\}',
        new_cenit_css,
        content
    )
    print("Replaced logo-cenit-nav CSS via regex!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated with larger CENIT logo!")
