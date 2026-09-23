import re

with open('index_v1_original.html', 'r', encoding='utf-8') as f:
    v1 = f.read()

with open('index_v2_editorial.html', 'r', encoding='utf-8') as f:
    v2 = f.read()

print("=== V1 NAVBAR ===")
m_nav1 = re.search(r'<nav[\s\S]*?</nav>', v1)
if m_nav1:
    print(m_nav1.group(0)[:500])

print("\n=== V2 PRELOADER ===")
m_pre = re.search(r'<div id="geotec-preloader"[\s\S]*?</div>\s*</div>', v2)
if m_pre:
    print(m_pre.group(0))

print("\n=== V2 HERO ===")
m_hero2 = re.search(r'<header[\s\S]*?</header>', v2)
if m_hero2:
    print(m_hero2.group(0)[:800])

print("\n=== V1 LIMITACIONES ===")
m_lim1 = re.search(r'<section[^>]*id="limitaciones"[^>]*>[\s\S]*?</section>', v1)
if m_lim1:
    print(m_lim1.group(0)[:600])

print("\n=== V1 FOOTER / CONTACTO ===")
m_c1 = re.search(r'<section[^>]*id="contacto"[^>]*>[\s\S]*?</section>', v1)
if m_c1:
    print(m_c1.group(0)[:600])

print("\n=== V2 FOOTER / CONTACTO ===")
m_c2 = re.search(r'<section[^>]*id="contacto"[^>]*>[\s\S]*?</section>', v2)
if m_c2:
    print(m_c2.group(0)[:600])
