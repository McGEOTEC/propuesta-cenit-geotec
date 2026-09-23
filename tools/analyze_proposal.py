import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("HTML size:", len(html))

# Find sections
sections = re.findall(r'<section\s+id="([^"]+)"[^>]*>([\s\S]*?)(?=</section>)', html)
for sec_id, content in sections:
    # Find h2, h3
    titles = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', content)
    clean_titles = [re.sub(r'<[^>]+>', '', t).strip() for t in titles]
    print(f"\n--- Section #{sec_id} ---")
    for t in clean_titles[:4]:
        print(f"  • {t}")
