import os

assets_dir = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets'

# 1. Delete unused animal images
animal_files = [
    'animal_carpintero.png',
    'animal_carpintero_new.png',
    'animal_carpintero_old.png',
    'animal_garza.png',
    'animal_lorito_web.png',
    'animal_loro_verde.png',
    'animal_loro_verde_normal.png'
]

for af in animal_files:
    p = os.path.join(assets_dir, af)
    if os.path.exists(p):
        os.remove(p)
        print(f"Deleted unused animal file: {af}")

# 2. Integrate Screenshot_20260923110515-removebg-preview.png in index.html Hero
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's check how Hero is structured
# In Hero, let's create a 2-column layout or incorporate the star emblem elegantly
hero_old = '''<header id="inicio" class="hero-section">
  <div class="container hero-grid">
    <div class="hero-header-area">
      <span class="tag-institucional">Laboratorio de Innovación Ambiental · GEOTEC InnoLab</span>
      <h1 class="hero-title">
        La Calidad del Dato Socioambiental se Construye en el <span>Origen</span>, no en la Corrección Tardía
      </h1>
      <p class="hero-subtitle">
        <strong>91 herramientas en producción</strong> nacidas de la operación real de consultoría ambiental colombiana. Una respuesta tecnológica integral y comprobada para el sondeo de mercado <strong>CENIT VH-2026-369</strong>.
      </p>
      <div class="hero-cta-group">
        <a href="#lineas" class="btn-primary">Ver el Modelo Tecnológico</a>
        <a href="#contacto" class="btn-secondary">Agendar Demostración Técnica</a>
      </div>
    </div>

    <!-- Métricas en Chips (De V2) -->
    <div class="hero-stats-grid">
      <div class="stat-card">
        <div class="stat-number">91</div>
        <div class="stat-label">Herramientas en Producción</div>
        <div class="stat-subtext">Nacidas de la operación real</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">160</div>
        <div class="stat-label">Iniciativas en Portafolio</div>
        <div class="stat-subtext">Inventario trazable y activo</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">26 + 2</div>
        <div class="stat-label">Años de Trayectoria</div>
        <div class="stat-subtext">26 años GEOTEC + 2 años InnoLab</div>
      </div>
    </div>
  </div>
</header>'''

hero_new = '''<header id="inicio" class="hero-section">
  <div class="container hero-grid-2col">
    <div class="hero-header-area">
      <span class="tag-institucional">Laboratorio de Innovación Ambiental · GEOTEC InnoLab</span>
      <h1 class="hero-title">
        La Calidad del Dato Socioambiental se Construye en el <span>Origen</span>, no en la Corrección Tardía
      </h1>
      <p class="hero-subtitle">
        <strong>91 herramientas en producción</strong> nacidas de la operación real de consultoría ambiental colombiana. Una respuesta tecnológica integral y comprobada para el sondeo de mercado <strong>CENIT VH-2026-369</strong>.
      </p>
      <div class="hero-cta-group">
        <a href="#lineas" class="btn-primary">Ver el Modelo Tecnológico</a>
        <a href="#contacto" class="btn-secondary">Agendar Demostración Técnica</a>
      </div>
    </div>

    <!-- Isotipo Fotográfico Transparente Integrado -->
    <div class="hero-art-area">
      <div class="hero-art-card">
        <img src="assets/Screenshot_20260923110515-removebg-preview.png" alt="GEOTEC InnoLab — Ingeniería y Naturaleza" class="hero-art-star">
      </div>
    </div>
  </div>

  <!-- Métricas en Chips debajo -->
  <div class="container" style="margin-top: 36px;">
    <div class="hero-stats-grid">
      <div class="stat-card">
        <div class="stat-number">91</div>
        <div class="stat-label">Herramientas en Producción</div>
        <div class="stat-subtext">Nacidas de la operación real</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">160</div>
        <div class="stat-label">Iniciativas en Portafolio</div>
        <div class="stat-subtext">Inventario trazable y activo</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">26 + 2</div>
        <div class="stat-label">Años de Trayectoria</div>
        <div class="stat-subtext">26 años GEOTEC + 2 años InnoLab</div>
      </div>
    </div>
  </div>
</header>'''

html = html.replace(hero_old, hero_new)

# Add CSS for 2-column Hero and Star
hero_css_addon = '''
/* Hero 2-Column with Star Artwork */
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
'''

html = html.replace('</style>', hero_css_addon + '\n</style>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with integrated star artwork and cleaned unused animals!")
