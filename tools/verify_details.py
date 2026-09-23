import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

prob = re.search(r'<section id="problematica"[\s\S]*?</section>', text)
lineas = re.search(r'<section id="lineas"[\s\S]*?</section>', text)

print("Problematica found:", bool(prob), "length:", len(prob.group(0)) if prob else 0)
print("Lineas found:", bool(lineas), "length:", len(lineas.group(0)) if lineas else 0)

details = re.findall(r'<details class="linea', text)
print("Details linea count:", len(details))

capsules = re.findall(r'class="capsule"', text)
print("Capsules count:", len(capsules))

cap_nums = re.findall(r'class="cap-num"[^>]*>(\d+)', text)
print("Cap nums:", cap_nums)
