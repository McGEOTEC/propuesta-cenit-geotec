import re

with open('index_v1_original.html', 'r', encoding='utf-8') as f:
    v1_text = f.read()

# Extract #problematica and #lineas
m_prob = re.search(r'<section[^>]*id="problematica"[^>]*>[\s\S]*?</section>', v1_text)
m_lineas = re.search(r'<section[^>]*id="lineas"[^>]*>[\s\S]*?</section>', v1_text)

print("Found #problematica in v1:", bool(m_prob), len(m_prob.group(0)) if m_prob else 0)
print("Found #lineas in v1:", bool(m_lineas), len(m_lineas.group(0)) if m_lineas else 0)

# Check CSS related to problematica and lineas in v1
# Let's search CSS selectors in v1
css_match = re.search(r'<style>([\s\S]*?)</style>', v1_text)
if css_match:
    css = css_match.group(1)
    print("CSS length in v1:", len(css))
