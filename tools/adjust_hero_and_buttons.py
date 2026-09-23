import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for Hero Star sizing and framing
old_hero_css = """
.hero-grid-2col {
  display: grid;
  grid-template-columns: 1.25fr 0.85fr;
  gap: 36px;
  align-items: center;
}
.hero-header-area {
  text-align: left;
  align-items: flex-start;
}
.hero-header-area .hero-subtitle {
  margin: 0 0 24px;
}
.hero-header-area .hero-cta-group {
  justify-content: flex-start;
  margin-bottom: 0;
}
.hero-art-area {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
.hero-art-card {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
  transition: transform 0.4s var(--ease);
}
.hero-art-card:hover {
  transform: scale(1.03) rotate(1deg);
}
.hero-art-star {
  width: 100%;
  max-width: 360px;
  height: auto;
  object-fit: contain;
  filter: drop-shadow(0 14px 32px rgba(10, 10, 10, 0.12));
}

@media (max-width: 900px) {
  .hero-grid-2col {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .hero-header-area {
    text-align: center;
    align-items: center;
  }
  .hero-header-area .hero-cta-group {
    justify-content: center;
  }
  .hero-art-star {
    max-width: 260px;
  }
}
""".strip()

new_hero_css = """
.hero-grid-2col {
  display: grid;
  grid-template-columns: 1.08fr 1fr;
  gap: 32px;
  align-items: center;
}
.hero-header-area {
  text-align: left;
  align-items: flex-start;
}
.hero-header-area .hero-subtitle {
  margin: 0 0 24px;
}
.hero-header-area .hero-cta-group {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  justify-content: flex-start;
  margin-bottom: 0;
}
.hero-art-area {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  width: 100%;
}
.hero-art-card {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 0;
  transition: transform 0.4s var(--ease);
}
.hero-art-card:hover {
  transform: scale(1.02);
}
.hero-art-star {
  width: 100%;
  max-width: 520px;
  height: auto;
  object-fit: contain;
  filter: drop-shadow(0 18px 40px rgba(10, 10, 10, 0.14));
}

@media (max-width: 900px) {
  .hero-grid-2col {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .hero-header-area {
    text-align: center;
    align-items: center;
  }
  .hero-header-area .hero-cta-group {
    justify-content: center;
  }
  .hero-art-star {
    max-width: 340px;
  }
}
""".strip()

if old_hero_css in content:
    content = content.replace(old_hero_css, new_hero_css)
    print("Replaced hero CSS directly!")
else:
    # regex replace hero-grid-2col block
    content = re.sub(
        r'\.hero-grid-2col\s*\{[\s\S]*?@media \(max-width: 900px\)\s*\{[\s\S]*?\.hero-art-star\s*\{\s*max-width:\s*260px;\s*\}\s*\}',
        new_hero_css,
        content
    )
    print("Replaced hero CSS via regex!")

# 2. SVG WhatsApp Icon snippet
wa_svg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="#25D366" style="vertical-align: middle; margin-right: 7px; display: inline-block; flex-shrink: 0;"><path d="M12.004 2c-5.523 0-10 4.477-10 10 0 1.767.458 3.428 1.258 4.873L2 22l5.247-1.224A9.957 9.957 0 0012.004 22c5.522 0 10-4.477 10-10s-4.478-10-10-10zm5.823 14.205c-.244.686-1.218 1.309-1.697 1.378-.479.07-1.077.098-3.417-.866-2.736-1.127-4.498-3.901-4.634-4.083-.137-.182-1.108-1.474-1.108-2.812 0-1.338.701-1.996.95-2.26.248-.264.542-.33.722-.33.18 0 .361.002.518.01.168.008.393-.064.615.468.228.547.777 1.895.845 2.034.068.138.114.3.023.48-.091.18-.137.293-.274.453-.137.16-.289.357-.412.48-.137.136-.28.283-.12.557.16.274.712 1.173 1.528 1.9 1.05.936 1.936 1.226 2.211 1.363.275.137.435.114.595-.069.16-.183.687-.799.87-1.073.183-.274.366-.229.617-.137.252.091 1.597.753 1.871.89.274.137.457.206.525.32.069.114.069.663-.175 1.349z"/></svg>'

# 3. Update Navbar CTA Button
content = re.sub(
    r'<a href="https://wa\.me/573103430466[^"]*"[^>]*class="nav-cta-btn"[^>]*>.*?</a>',
    f'<a href="https://wa.me/573103430466?text=Hola%20GEOTEC%20InnoLab,%20quisiera%20agendar%20una%20sesi%C3%B3n%20t%C3%A9cnica%20sobre%20la%20propuesta%20para%20CENIT%20(Sondeo%20VH-2026-369)." target="_blank" rel="noopener noreferrer" class="nav-cta-btn" style="display:inline-flex;align-items:center;">{wa_svg}Agendar</a>',
    content
)

# 4. Update Hero CTA Button
content = re.sub(
    r'<a href="https://wa\.me/573103430466[^"]*"[^>]*class="btn-secondary"[^>]*>.*?</a>',
    f'<a href="https://wa.me/573103430466?text=Hola%20GEOTEC%20InnoLab,%20quisiera%20agendar%20una%20sesi%C3%B3n%20t%C3%A9cnica%20sobre%20la%20propuesta%20para%20CENIT%20(Sondeo%20VH-2026-369)." target="_blank" rel="noopener noreferrer" class="btn-secondary" style="display:inline-flex;align-items:center;">{wa_svg}Agendar</a>',
    content
)

# 5. Update Footer CTA Button
content = re.sub(
    r'<a href="https://wa\.me/573103430466[^"]*"[^>]*class="footer-btn-primary"[^>]*>.*?</a>',
    f'<a href="https://wa.me/573103430466?text=Hola%20GEOTEC%20InnoLab,%20quisiera%20agendar%20una%20sesi%C3%B3n%20t%C3%A9cnica%20sobre%20la%20propuesta%20para%20CENIT%20(Sondeo%20VH-2026-369)." target="_blank" rel="noopener noreferrer" class="footer-btn-primary" style="display:inline-flex;align-items:center;justify-content:center;">{wa_svg}Agendar</a>',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully!")
