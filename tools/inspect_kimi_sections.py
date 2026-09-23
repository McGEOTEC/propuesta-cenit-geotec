import re

with open('index_v1_original.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find sections
pattern = re.compile(r'<section[^>]*id="([^"]+)"[^>]*>([\s\S]*?)(?=</section>)')
matches = pattern.findall(text)
print(f"Total sections: {len(matches)}")
for sid, scontent in matches:
    titles = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', scontent)
    clean_titles = [re.sub(r'<[^>]+>', '', t).strip() for t in titles[:3]]
    eyebrows = re.findall(r'class="[^"]*eyebrow[^"]*"[^>]*>(.*?)</', scontent)
    clean_eye = [re.sub(r'<[^>]+>', '', e).strip() for e in eyebrows[:1]]
    print(f"[{sid}] Eyebrow: {clean_eye} | Titles: {clean_titles}")
