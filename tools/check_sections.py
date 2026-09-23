import re

with open('index.html', encoding='utf-8') as f:
    text = f.read()

prob = re.search(r'<section id="problematica"[\s\S]*?</section>', text)
lineas = re.search(r'<section id="lineas"[\s\S]*?</section>', text)

print("Problematica length:", len(prob.group(0)) if prob else "NOT FOUND")
print("Lineas length:", len(lineas.group(0)) if lineas else "NOT FOUND")

# Check if IDU is present anywhere in index.html
idu_matches = re.findall(r'\bIDU\b', text, re.IGNORECASE)
print("IDU occurrences:", len(idu_matches))

# Check WhatsApp links
wa_matches = re.findall(r'https://wa\.me/\d+', text)
print("WhatsApp links count:", len(wa_matches))
print("WhatsApp link targets:", set(wa_matches))
