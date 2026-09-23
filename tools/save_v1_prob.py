import re

with open('index_v1_original.html', 'r', encoding='utf-8') as f:
    v1_text = f.read()

m_prob = re.search(r'<section[^>]*id="problematica"[^>]*>[\s\S]*?</section>', v1_text)
m_lineas = re.search(r'<section[^>]*id="lineas"[^>]*>[\s\S]*?</section>', v1_text)

with open('v1_prob_and_lineas.html', 'w', encoding='utf-8') as out:
    out.write(m_prob.group(0) + '\n\n' + m_lineas.group(0))

print("Saved v1_prob_and_lineas.html")
