import os, re

# Read original Kimi index_v1_original.html
with open('index_v1_original.html', 'r', encoding='utf-8') as f:
    orig_html = f.read()

print("Original length:", len(orig_html))

# Let's verify and build the clean MIX index.html strictly following the prompt scope
# 1. Colors & Typography: Use the pure GEOTEC palette + Roboto + IBM Plex Mono
# 2. Add Preloader
# 3. Add Top-Right Corner Logo with delicate Parallax in Hero
# 4. Add Humedal Field Image in Operación section
# 5. Add Client Marquee in Operación section
# 6. Soften security roadmap
# 7. Keep all 7 sections, exact 91 tools, 160 initiatives, 242 ANLA classes, 4.799 fields, 308 domains, 4 phases, Ecopetrol/Frontera/IDU

mix_html = orig_html

# 1. Inject Preloader HTML after <body>
preloader_html = '''
<!-- ================= PRELOADER / INTRO MOTION ================= -->
<div id="geotec-preloader" aria-hidden="true">
  <div class="preloader-inner">
    <img src="assets/logo_geotec_color.png" alt="GEOTEC InnoLab" class="preloader-logo" width="220" height="auto" onerror="this.src='assets/logo_geotec_horizontal_star.png'">
    <div class="preloader-sub">Ecosistema Tecnológico · Gestión Socioambiental</div>
    <div class="preloader-bar"><div class="preloader-progress"></div></div>
  </div>
</div>
'''

if 'id="geotec-preloader"' not in mix_html:
    mix_html = mix_html.replace('<body>', '<body>\n' + preloader_html)

# 2. Add Preloader CSS + Marquee CSS + Corner Brand CSS
extra_css = '''
/* --- PRELOADER --- */
#geotec-preloader {
  position: fixed;
  inset: 0;
  background: var(--paper, #FAFAF8);
  z-index: 99999;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.6s var(--ease), visibility 0.6s var(--ease);
}
#geotec-preloader.is-loaded {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}
.preloader-inner {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  animation: preloaderIn 0.8s var(--ease) forwards;
}
@keyframes preloaderIn {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}
.preloader-logo {
  max-width: 220px;
  height: auto;
  filter: drop-shadow(0 4px 12px rgba(10,10,10,0.06));
}
.preloader-sub {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  color: var(--ink-soft, #53534D);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.preloader-bar {
  width: 180px;
  height: 3px;
  background: var(--line, #D8D8D8);
  border-radius: 3px;
  overflow: hidden;
  position: relative;
}
.preloader-progress {
  width: 100%;
  height: 100%;
  background: var(--olive, #92A53D);
  transform: translateX(-100%);
  animation: preloaderFill 1.2s ease-in-out forwards;
}
@keyframes preloaderFill {
  0% { transform: translateX(-100%); }
  50% { transform: translateX(-30%); }
  100% { transform: translateX(0); }
}

/* --- HERO CORNER BRAND ELEMENT --- */
.hero-corner-brand {
  position: absolute;
  top: 30px;
  right: 40px;
  display: flex;
  align-items: center;
  gap: 14px;
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(8px);
  border: 1px solid var(--line, #D8D8D8);
  padding: 10px 18px;
  border-radius: 999px;
  box-shadow: 0 4px 16px rgba(10,10,10,0.04);
  transition: transform 0.3s var(--ease), box-shadow 0.3s var(--ease);
  z-index: 10;
}
.hero-corner-brand:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(146, 165, 61, 0.15);
  border-color: var(--olive, #92A53D);
}
.hero-corner-icon {
  width: 28px;
  height: 28px;
  object-fit: contain;
}
.hero-corner-text {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--olive-deep, #1E2A24);
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

/* --- CLIENT MARQUEE TRACK --- */
.clients-marquee-wrapper {
  margin-top: 48px;
  padding: 32px 0 20px;
  border-top: 1px solid var(--line, #D8D8D8);
  overflow: hidden;
  position: relative;
  mask-image: linear-gradient(to right, transparent, black 12%, black 88%, transparent);
  -webkit-mask-image: linear-gradient(to right, transparent, black 12%, black 88%, transparent);
}
.marquee-title {
  text-align: center;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--ink-soft, #53534D);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-bottom: 24px;
}
.marquee-track {
  display: flex;
  gap: 32px;
  width: max-content;
  animation: scrollMarquee 35s linear infinite;
}
.marquee-track:hover {
  animation-play-state: paused;
}
.marquee-card {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 12px 24px;
  background: var(--card, #FFFFFF);
  border: 1px solid var(--line, #D8D8D8);
  border-radius: 8px;
  min-width: 140px;
  height: 64px;
  transition: transform 0.25s var(--ease), border-color 0.25s var(--ease);
}
.marquee-card:hover {
  transform: translateY(-3px);
  border-color: var(--olive, #92A53D);
}
.marquee-card img {
  max-height: 38px;
  max-width: 110px;
  object-fit: contain;
  filter: grayscale(100%) opacity(0.8);
  transition: filter 0.25s var(--ease);
}
.marquee-card:hover img {
  filter: grayscale(0%) opacity(1);
}
@keyframes scrollMarquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* --- FIELD PHOTO HERO CARD --- */
.operacion-field-hero {
  margin-top: 36px;
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 28px;
  background: var(--paper-alt, #F0EFE5);
  border: 1px solid var(--line, #D8D8D8);
  border-radius: var(--radius, 10px);
  overflow: hidden;
  align-items: center;
}
.operacion-field-img {
  width: 100%;
  height: 100%;
  min-height: 260px;
  object-fit: cover;
}
.operacion-field-content {
  padding: 28px 32px 28px 12px;
}
.operacion-field-tag {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--olive, #92A53D);
  margin-bottom: 8px;
  letter-spacing: 0.08em;
}
.operacion-field-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--ink, #0A0A0A);
  margin-bottom: 12px;
  line-height: 1.3;
}
.operacion-field-desc {
  font-size: 0.92rem;
  color: var(--ink-soft, #53534D);
  line-height: 1.55;
  margin-bottom: 16px;
}
@media (max-width: 860px) {
  .operacion-field-hero {
    grid-template-columns: 1fr;
  }
  .operacion-field-content {
    padding: 24px;
  }
}
'''

# Inject CSS before </style>
mix_html = mix_html.replace('</style>', extra_css + '\n</style>')

# 3. Inject Corner Brand in <header class="hero">
corner_brand_html = '''
  <div class="hero-corner-brand" title="GEOTEC InnoLab · 91 Herramientas en Producción">
    <img src="assets/isotipo_geotec_blanco.png" alt="Isotipo GEOTEC" class="hero-corner-icon" onerror="this.style.display='none'">
    <span class="hero-corner-text">91 Herramientas · 160 Iniciativas</span>
  </div>
'''

if 'class="hero-corner-brand"' not in mix_html:
    # Add inside header
    mix_html = re.sub(r'(<header[^>]*class="[^"]*hero[^"]*"[^>]*>)', r'\1\n' + corner_brand_html, mix_html)

# 4. Inject Field Photo and Client Marquee in <section id="operacion">
field_photo_html = '''
    <div class="operacion-field-hero">
      <img src="assets/campo_verificacion_humedal.jpg" alt="Verificación técnica de campo en humedales" class="operacion-field-img">
      <div class="operacion-field-content">
        <span class="operacion-field-tag">Operación en Terreno</span>
        <h3 class="operacion-field-title">Aseguramiento y captura con trazabilidad GNSS en campo</h3>
        <p class="operacion-field-desc">Especialistas socioambientales operando con formularios digitales desconectados, registro fotográfico con metadatos verificables y carga directa a geodatabase sin retrabajo manual.</p>
        <div style="display:flex; gap:16px; font-family:var(--font-mono); font-size:0.8rem; color:var(--olive-deep, #1E2A24);">
          <div><strong>✓ 242</strong> clases ANLA</div>
          <div><strong>✓ 4.799</strong> campos auditados</div>
        </div>
      </div>
    </div>
'''

marquee_html = '''
    <div class="clients-marquee-wrapper">
      <div class="marquee-title">Experiencia Comprobada en el Sector Energético e Industrial</div>
      <div class="marquee-track">
        <div class="marquee-card"><img src="assets/clientes/cenit.png" alt="CENIT" onerror="this.parentElement.textContent='CENIT'"></div>
        <div class="marquee-card"><img src="assets/clientes/ecopetrol.png" alt="Ecopetrol" onerror="this.parentElement.textContent='Ecopetrol'"></div>
        <div class="marquee-card"><img src="assets/clientes/frontera_energy.png" alt="Frontera Energy" onerror="this.parentElement.textContent='Frontera Energy'"></div>
        <div class="marquee-card"><img src="assets/clientes/bp.png" alt="BP" onerror="this.parentElement.textContent='BP'"></div>
        <div class="marquee-card"><img src="assets/clientes/exxonmobil.png" alt="ExxonMobil" onerror="this.parentElement.textContent='ExxonMobil'"></div>
        <div class="marquee-card"><img src="assets/clientes/bhp_billiton.png" alt="BHP" onerror="this.parentElement.textContent='BHP'"></div>
        <div class="marquee-card"><img src="assets/clientes/petrobras.png" alt="Petrobras" onerror="this.parentElement.textContent='Petrobras'"></div>
        <div class="marquee-card"><img src="assets/clientes/gran_tierra.png" alt="Gran Tierra" onerror="this.parentElement.textContent='Gran Tierra'"></div>
        <div class="marquee-card"><img src="assets/clientes/equion.png" alt="Equión" onerror="this.parentElement.textContent='Equión'"></div>
        <div class="marquee-card"><img src="assets/clientes/anh.png" alt="ANH" onerror="this.parentElement.textContent='ANH'"></div>
        <div class="marquee-card"><img src="assets/clientes/mintransporte.png" alt="MinTransporte" onerror="this.parentElement.textContent='MinTransporte'"></div>
        <div class="marquee-card"><img src="assets/clientes/ocensa.webp" alt="Ocensa" onerror="this.parentElement.textContent='Ocensa'"></div>
        <!-- Duplicado para loop continuo -->
        <div class="marquee-card"><img src="assets/clientes/cenit.png" alt="CENIT" onerror="this.parentElement.textContent='CENIT'"></div>
        <div class="marquee-card"><img src="assets/clientes/ecopetrol.png" alt="Ecopetrol" onerror="this.parentElement.textContent='Ecopetrol'"></div>
        <div class="marquee-card"><img src="assets/clientes/frontera_energy.png" alt="Frontera Energy" onerror="this.parentElement.textContent='Frontera Energy'"></div>
        <div class="marquee-card"><img src="assets/clientes/bp.png" alt="BP" onerror="this.parentElement.textContent='BP'"></div>
        <div class="marquee-card"><img src="assets/clientes/exxonmobil.png" alt="ExxonMobil" onerror="this.parentElement.textContent='ExxonMobil'"></div>
        <div class="marquee-card"><img src="assets/clientes/bhp_billiton.png" alt="BHP" onerror="this.parentElement.textContent='BHP'"></div>
        <div class="marquee-card"><img src="assets/clientes/petrobras.png" alt="Petrobras" onerror="this.parentElement.textContent='Petrobras'"></div>
        <div class="marquee-card"><img src="assets/clientes/gran_tierra.png" alt="Gran Tierra" onerror="this.parentElement.textContent='Gran Tierra'"></div>
        <div class="marquee-card"><img src="assets/clientes/equion.png" alt="Equión" onerror="this.parentElement.textContent='Equión'"></div>
        <div class="marquee-card"><img src="assets/clientes/anh.png" alt="ANH" onerror="this.parentElement.textContent='ANH'"></div>
        <div class="marquee-card"><img src="assets/clientes/mintransporte.png" alt="MinTransporte" onerror="this.parentElement.textContent='MinTransporte'"></div>
        <div class="marquee-card"><img src="assets/clientes/ocensa.webp" alt="Ocensa" onerror="this.parentElement.textContent='Ocensa'"></div>
      </div>
    </div>
'''

if 'class="operacion-field-hero"' not in mix_html:
    # Inject before </section> in operacion
    mix_html = re.sub(r'(<section[^>]*id="operacion"[^>]*>[\s\S]*?)(</section>)', r'\1\n' + field_photo_html + '\n' + marquee_html + r'\n\2', mix_html)

# 5. Inject Preloader Dismiss JS
preloader_js = '''
// Preloader dismissal
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    const p = document.getElementById('geotec-preloader');
    if (p) p.classList.add('is-loaded');
  }, 900);
});
'''

if 'geotec-preloader' not in mix_html or 'classList.add(\'is-loaded\')' not in mix_html:
    mix_html = mix_html.replace('</script>', preloader_js + '\n</script>')

# Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(mix_html)

print("Updated index.html successfully! Total length:", len(mix_html), "lines:", len(mix_html.splitlines()))
