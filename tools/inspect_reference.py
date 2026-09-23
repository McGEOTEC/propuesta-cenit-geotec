import os
import re

path = r'F:\PROYECTOS\EMPRESARIAL\PROPUESTA_ECOPETROL\PROPUESTA\COPIA_PRESENTACIONTAMI\COPIA_PRESENTACIONTAMI'

with open(os.path.join(path, 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

sections = re.findall(r'<section[^>]+id=["\']([^"\']+)["\']', text)
print("Sections in reference:", sections)

# Print headers
for s in sections[:10]:
    m = re.search(rf'<section[^>]+id=["\']{s}["\'][\s\S]*?(?=<section|\Z)', text)
    if m:
        titles = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', m.group(0))
        clean_t = [re.sub(r'<[^>]+>', '', t).strip() for t in titles]
        print(f"\nSection #{s}:", clean_t[:3])
