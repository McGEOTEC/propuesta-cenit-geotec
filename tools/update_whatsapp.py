with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

wa_url = "https://wa.me/573103430466?text=Hola%20GEOTEC%20InnoLab,%20quisiera%20agendar%20una%20sesi%C3%B3n%20t%C3%A9cnica%20sobre%20la%20propuesta%20para%20CENIT%20(Sondeo%20VH-2026-369)."

# 1. Update Navbar button
text = text.replace(
    '<a href="#contacto" class="nav-cta-btn">Agendar Sesión</a>',
    f'<a href="{wa_url}" target="_blank" rel="noopener noreferrer" class="nav-cta-btn" title="Contactar por WhatsApp (+57 310 343 0466)">Agendar por WhatsApp</a>'
)

# 2. Update Hero button
text = text.replace(
    '<a href="#contacto" class="btn-secondary">Agendar Demostración Técnica</a>',
    f'<a href="{wa_url}" target="_blank" rel="noopener noreferrer" class="btn-secondary" title="Contactar por WhatsApp (+57 310 343 0466)">📱 Agendar por WhatsApp (+57 310 343 0466)</a>'
)

# 3. Update Footer button and text
footer_old = '''<a href="mailto:contacto@geotec.com.co?subject=Demostracion%20Tecnica%20GEOTEC%20InnoLab%20-%20CENIT%20VH-2026-369" class="footer-btn-primary">
        Agendar Sesión Técnica
      </a>'''

footer_new = f'''<a href="{wa_url}" target="_blank" rel="noopener noreferrer" class="footer-btn-primary">
        📱 Agendar por WhatsApp (+57 310 343 0466)
      </a>'''

text = text.replace(footer_old, footer_new)

# 4. Update Footer contact info
text = text.replace(
    'Bogotá D.C., Colombia · contacto@geotec.com.co',
    'Bogotá D.C., Colombia · WhatsApp: +57 310 343 0466 · contacto@geotec.com.co'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated all Agendar links to WhatsApp (+57 310 343 0466)!")
