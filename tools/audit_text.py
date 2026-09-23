import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

unwanted = ['sísmica', 'sismica', 'voladuras', 'perforación', 'perforacion', '2.424', 'offshore', 'off-shore', 'Playón', 'Playon', 'Guamal', 'Cubarral']
for w in unwanted:
    matches = list(re.finditer(re.escape(w), text, re.IGNORECASE))
    if matches:
        print(f'Found "{w}" at {len(matches)} positions')
    else:
        print(f'Clean: "{w}" not found')

print("\n--- Sections in index.html ---")
secs = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>', text)
for s in secs:
    print("Section:", s)
