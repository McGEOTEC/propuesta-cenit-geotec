# Script to completely update index.html with:
# 1. GEOTEC Intro Motion (Splash Screen) preloader
# 2. Client Marquee carousel with double track and full client chips
# 3. Dedicated visual showcase for campo_verificacion_humedal.jpg in "Capacidades en Operación"
# 4. Strategic placement of oficina_fachada_calle.jpg and oficina_fachada_contrapicado.jpg throughout the presentation

html_content = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GEOTEC InnoLab — Ecosistema Tecnológico para Gestión Socioambiental | Propuesta CENIT</title>
<meta name="description" content="GEOTEC InnoLab: Ingeniería que convierte complejidad en decisiones confiables. 91 herramientas en producción y +25 años de experiencia aplicados al sondeo de mercado CENIT VH-2026-369.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* ============================================================
   GEOTEC InnoLab — CENIT — Sondeo de Mercado VH-2026-369
   Sistema de Diseño: Paleta Oficial GEOTEC_2024 & Guía PPTX
   ============================================================ */
:root {
  /* Paleta Oficial GEOTEC_2024 */
  --verde-geotec:      #92A53D;
  --amarillo-geotec:   #FFD005;
  --amarillo-isotipo:  #FFD449;
  --oliva:             #C9B92E;
  --naranja:           #E37E4B;
  --carbon:            #53534D;
  --negro:             #0A0A0A;
  --verde-noche:       #1E2A24;
  --verde-bosque:      #17231D;
  
  /* Neutros y Superficies */
  --hueso:             #FAFAF8;
  --caja-beige:        #F0EFE5;
  --verde-tinte:       #F4F6EC;
  --blanco:            #FFFFFF;
  --gris-linea:        #D8D8D8;
  --gris-borde-suave:  #E5E5DE;
  --gris-fondo-card:   #FBFBFA;

  /* Textos */
  --texto-principal:   #0A0A0A;
  --texto-secundario:  #53534D;
  --texto-suave:       #76766E;
  --texto-inverso:     #FAFAF8;
  --texto-inverso-mut: #C7C4AE;

  /* Tipografías */
  --font-display: 'Outfit', 'Roboto', sans-serif;
  --font-body:    'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono:    'IBM Plex Mono', 'Consolas', monospace;

  /* Dimensiones y Sombras */
  --container-max: 1240px;
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --shadow-sm: 0 2px 8px rgba(10, 10, 10, 0.04);
  --shadow-md: 0 8px 24px rgba(10, 10, 10, 0.07);
  --shadow-lg: 0 16px 40px rgba(10, 10, 10, 0.12);
  --shadow-glow: 0 0 35px rgba(146, 165, 61, 0.25);

  --transition: all 0.28s cubic-bezier(0.2, 0.8, 0.2, 1);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
  background-color: var(--hueso);
  color: var(--texto-principal);
  font-family: var(--font-body);
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

body {
  overflow-x: hidden;
  position: relative;
  background: var(--hueso);
}

/* ============================================================
   GEOTEC INTRO MOTION (Splash Screen Preloader)
   ============================================================ */
body:not(.is-loaded) {
  overflow: hidden;
}

#geotec-preloader {
  position: fixed;
  inset: 0;
  background: #FAFAF8;
  background-image: url('assets/fondo_topografico_portada.png');
  background-position: center;
  background-size: cover;
  z-index: 999999;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 20px;
  transition: transform 0.85s cubic-bezier(0.77, 0, 0.175, 1), opacity 0.6s ease;
}

.preloader-logo-wrap {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.preloader-logo {
  width: clamp(240px, 30vw, 360px);
  height: auto;
  opacity: 0;
  transform: scale(0.9) translateY(24px);
  animation: geotecIntro 1.2s cubic-bezier(0.22, 0.61, 0.36, 1) forwards;
  animation-delay: 0.15s;
}

.preloader-tagline {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--verde-geotec);
  opacity: 0;
  transform: translateY(12px);
  animation: geotecIntroText 1s cubic-bezier(0.22, 0.61, 0.36, 1) forwards;
  animation-delay: 0.5s;
}

.preloader-spinner {
  width: 32px;
  height: 3px;
  background: var(--gris-linea);
  border-radius: 2px;
  overflow: hidden;
  position: relative;
}

.preloader-spinner::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 40%;
  background: var(--verde-geotec);
  border-radius: 2px;
  animation: preloaderLine 1.4s ease-in-out infinite;
}

@keyframes geotecIntro {
  100% { opacity: 1; transform: scale(1) translateY(0); }
}

@keyframes geotecIntroText {
  100% { opacity: 1; transform: translateY(0); }
}

@keyframes preloaderLine {
  0% { left: -40%; width: 30%; }
  50% { left: 30%; width: 60%; }
  100% { left: 100%; width: 30%; }
}

body.is-loaded #geotec-preloader {
  transform: translateY(-100%);
  opacity: 0;
  pointer-events: none;
}

@media (prefers-reduced-motion: reduce) {
  .preloader-logo, .preloader-tagline { animation: none; opacity: 1; transform: none; }
  #geotec-preloader { display: none; }
}

/* Barra de lectura superior */
#scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3.5px;
  width: 0%;
  background: linear-gradient(90deg, var(--amarillo-geotec), var(--verde-geotec));
  z-index: 1000;
  transition: width 0.1s ease-out;
}

/* ============================================================
   ELEMENTOS GRÁFICOS INSTITUCIONALES (Guía PPTX Slide 6)
   ============================================================ */
.barra-acento-inferior {
  display: block;
  width: 52px;
  height: 3px;
  background-color: var(--verde-geotec);
  border-radius: 2px;
  margin-top: 10px;
  margin-bottom: 14px;
}

.barra-acento-inferior.center {
  margin-left: auto;
  margin-right: auto;
}

.barra-acento-inferior.amarillo {
  background-color: var(--amarillo-geotec);
}

.barra-acento-lateral {
  border-left: 3.5px solid var(--verde-geotec);
  padding-left: 14px;
}

.tag-institucional {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  background: var(--verde-tinte);
  border: 1px solid rgba(146, 165, 61, 0.25);
  border-radius: 100px;
  font-family: var(--font-mono);
  font-size: 0.76rem;
  font-weight: 600;
  color: var(--carbon);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.tag-institucional.amarillo {
  background: #FFF9D6;
  border-color: rgba(255, 208, 5, 0.4);
  color: #7A6200;
}

.tag-institucional.dark {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.18);
  color: var(--amarillo-isotipo);
}

.folio-numero {
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--verde-geotec);
  font-size: 1rem;
  letter-spacing: 0.08em;
}

/* Layout container */
.container {
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 24px;
}

/* ============================================================
   NAVBAR INSTITUCIONAL
   ============================================================ */
.navbar {
  position: sticky;
  top: 0;
  background: rgba(250, 250, 248, 0.94);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--gris-linea);
  z-index: 900;
  transition: var(--transition);
}

.navbar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
}

.navbar-brand-group {
  display: flex;
  align-items: center;
  gap: 16px;
  text-decoration: none;
}

.nav-logo-geotec {
  height: 38px;
  width: auto;
  object-fit: contain;
}

.nav-divider {
  width: 1px;
  height: 28px;
  background-color: var(--gris-linea);
}

.nav-logo-innolab {
  height: 24px;
  width: auto;
  object-fit: contain;
}

.nav-logo-cenit {
  height: 28px;
  width: auto;
  object-fit: contain;
  opacity: 0.85;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 24px;
  list-style: none;
}

.nav-menu a {
  text-decoration: none;
  font-family: var(--font-display);
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--carbon);
  transition: var(--transition);
  position: relative;
  padding: 6px 0;
}

.nav-menu a:hover,
.nav-menu a.active {
  color: var(--verde-geotec);
}

.nav-menu a.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: var(--verde-geotec);
}

.nav-cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background-color: var(--verde-geotec);
  color: #FFFFFF !important;
  padding: 9px 18px !important;
  border-radius: var(--radius-sm);
  font-weight: 700 !important;
  font-size: 0.84rem !important;
  box-shadow: 0 2px 8px rgba(146, 165, 61, 0.3);
  transition: var(--transition);
}

.nav-cta:hover {
  background-color: #819332;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(146, 165, 61, 0.4);
}

/* Mobile Nav */
.nav-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
}

.nav-toggle span {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--carbon);
  margin: 5px 0;
  transition: var(--transition);
}

/* ============================================================
   HERO / PORTADA EDITORIAL (Corporate Book Cover & Concepts)
   ============================================================ */
.hero-section {
  position: relative;
  padding: 70px 0 80px 0;
  background-color: var(--hueso);
  background-image: url('assets/fondo_topografico_portada.png');
  background-position: center top;
  background-repeat: no-repeat;
  background-size: cover;
  border-bottom: 1px solid var(--gris-linea);
  overflow: hidden;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.95fr;
  gap: 48px;
  align-items: center;
}

.hero-content {
  position: relative;
  z-index: 2;
}

.hero-pretitle {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 18px;
  flex-wrap: wrap;
}

.hero-title-main {
  font-family: var(--font-display);
  font-size: 2.85rem;
  font-weight: 900;
  line-height: 1.12;
  color: var(--verde-noche);
  text-transform: uppercase;
  letter-spacing: -0.01em;
  margin-bottom: 8px;
}

.hero-title-sub {
  font-family: var(--font-display);
  font-size: 1.7rem;
  font-weight: 700;
  line-height: 1.25;
  color: var(--verde-geotec);
  text-transform: uppercase;
  margin-bottom: 14px;
}

.hero-description {
  font-size: 1.1rem;
  line-height: 1.6;
  color: var(--texto-secundario);
  margin-bottom: 28px;
  max-width: 580px;
}

.hero-description strong {
  color: var(--texto-principal);
  font-weight: 600;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 36px;
  flex-wrap: wrap;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background-color: var(--verde-geotec);
  color: #FFFFFF;
  padding: 13px 26px;
  border-radius: var(--radius-sm);
  font-family: var(--font-display);
  font-size: 0.96rem;
  font-weight: 700;
  text-decoration: none;
  transition: var(--transition);
  box-shadow: 0 4px 14px rgba(146, 165, 61, 0.35);
}

.btn-primary:hover {
  background-color: #7e8f2f;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(146, 165, 61, 0.45);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background-color: var(--blanco);
  color: var(--carbon);
  border: 1.5px solid var(--gris-linea);
  padding: 12px 22px;
  border-radius: var(--radius-sm);
  font-family: var(--font-display);
  font-size: 0.94rem;
  font-weight: 600;
  text-decoration: none;
  transition: var(--transition);
}

.btn-secondary:hover {
  border-color: var(--verde-geotec);
  color: var(--verde-geotec);
  background-color: var(--verde-tinte);
  transform: translateY(-2px);
}

/* Stats Ribbon */
.hero-stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  padding-top: 24px;
  border-top: 1px solid var(--gris-linea);
}

.hero-stat-item {
  display: flex;
  flex-direction: column;
}

.hero-stat-num {
  font-family: var(--font-mono);
  font-size: 1.65rem;
  font-weight: 700;
  color: var(--verde-noche);
  line-height: 1.1;
}

.hero-stat-num span {
  color: var(--verde-geotec);
}

.hero-stat-label {
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--texto-suave);
  line-height: 1.3;
  margin-top: 4px;
}

/* Hero Visual / Corporate Book Art */
.hero-visual-card {
  position: relative;
  background: var(--blanco);
  padding: 14px;
  border-radius: var(--radius-lg);
  border: 1px solid var(--gris-linea);
  box-shadow: var(--shadow-lg);
  transition: var(--transition);
  perspective: 1000px;
}

.hero-visual-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 50px rgba(30, 42, 36, 0.16);
  border-color: rgba(146, 165, 61, 0.4);
}

.hero-book-img-wrapper {
  position: relative;
  border-radius: var(--radius-md);
  overflow: hidden;
  background: #000;
}

.hero-book-cover-img {
  width: 100%;
  height: auto;
  display: block;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.hero-visual-card:hover .hero-book-cover-img {
  transform: scale(1.02);
}

/* Floating Concept Badges on Hero Cover */
.hero-concept-floating {
  position: absolute;
  z-index: 4;
  padding: 8px 14px;
  background: rgba(30, 42, 36, 0.88);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-sm);
  color: #FFFFFF;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
  transition: var(--transition);
}

.hero-concept-floating.pos-top-left {
  top: 18px;
  left: 18px;
}

.hero-concept-floating.pos-bottom-right {
  bottom: 18px;
  right: 18px;
}

.hero-concept-floating .concept-label {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  color: var(--amarillo-isotipo);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  display: block;
}

.hero-concept-floating .concept-val {
  font-family: var(--font-display);
  font-size: 0.86rem;
  font-weight: 600;
  color: #FFFFFF;
}

/* ============================================================
   SECCIÓN: EL CICLO GEOTEC Y LAS 5 CERTEZAS (Corporate Book)
   ============================================================ */
.section-certezas {
  padding: 90px 0;
  background-color: var(--blanco);
  border-bottom: 1px solid var(--gris-linea);
}

.section-header {
  text-align: center;
  max-width: 820px;
  margin: 0 auto 56px auto;
}

.section-title {
  font-family: var(--font-display);
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--verde-noche);
  text-transform: uppercase;
  line-height: 1.2;
}

.section-subtitle {
  font-size: 1.05rem;
  color: var(--texto-secundario);
  margin-top: 12px;
  line-height: 1.6;
}

/* 4 Ejes del Ciclo de Vida */
.ciclo-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 50px;
}

.ciclo-card {
  background: var(--caja-beige);
  border: 1px solid var(--gris-linea);
  border-top: 4px solid var(--verde-geotec);
  border-radius: var(--radius-md);
  padding: 24px 20px;
  transition: var(--transition);
  position: relative;
}

.ciclo-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  background: #FFFFFF;
  border-color: var(--verde-geotec);
}

.ciclo-card-num {
  font-family: var(--font-mono);
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--verde-geotec);
  margin-bottom: 8px;
}

.ciclo-card-title {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--verde-noche);
  text-transform: uppercase;
  margin-bottom: 10px;
}

.ciclo-card-desc {
  font-size: 0.9rem;
  color: var(--texto-secundario);
  line-height: 1.5;
  margin-bottom: 14px;
}

.ciclo-card-metrics {
  padding-top: 10px;
  border-top: 1px dashed var(--gris-linea);
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--verde-geotec);
}

/* 5 Dimensiones de Certeza */
.certezas-banner {
  background: linear-gradient(135deg, var(--verde-noche) 0%, #15201A 100%);
  border-radius: var(--radius-lg);
  padding: 44px 36px;
  color: #FFFFFF;
  position: relative;
  overflow: hidden;
  box-shadow: var(--shadow-lg);
}

.certezas-watermark {
  position: absolute;
  right: -40px;
  bottom: -40px;
  width: 320px;
  height: 320px;
  opacity: 0.08;
  pointer-events: none;
}

.certezas-header-inner {
  text-align: center;
  max-width: 720px;
  margin: 0 auto 36px auto;
  position: relative;
  z-index: 2;
}

.certezas-header-inner h3 {
  font-family: var(--font-display);
  font-size: 1.85rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.02em;
  color: #FFFFFF;
}

.certezas-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
  position: relative;
  z-index: 2;
}

.certeza-item {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-md);
  padding: 20px 16px;
  transition: var(--transition);
}

.certeza-item:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: var(--amarillo-isotipo);
  transform: translateY(-3px);
}

.certeza-item-title {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--amarillo-isotipo);
  margin-bottom: 8px;
  text-transform: uppercase;
}

.certeza-item-text {
  font-size: 0.85rem;
  color: var(--texto-inverso-mut);
  line-height: 1.45;
}

/* ============================================================
   SECCIÓN: PROBLEMÁTICA & ENFOQUE INTEGRADO
   ============================================================ */
.section-problematica {
  padding: 90px 0;
  background-color: var(--verde-tinte);
  border-bottom: 1px solid var(--gris-linea);
}

.problematica-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  margin-top: 40px;
}

.problema-col {
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-lg);
  padding: 36px 32px;
  box-shadow: var(--shadow-sm);
}

.problema-col.solucion {
  border-top: 5px solid var(--verde-geotec);
  background: linear-gradient(180deg, #FFFFFF 0%, #FAFAF7 100%);
}

.problema-col.desafio {
  border-top: 5px solid var(--naranja);
}

.problema-col-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}

.col-header-title {
  font-family: var(--font-display);
  font-size: 1.4rem;
  font-weight: 800;
  text-transform: uppercase;
  color: var(--verde-noche);
}

.problema-item-list {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.problema-item {
  display: flex;
  gap: 14px;
}

.problema-item-icon {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.85rem;
  flex-shrink: 0;
}

.desafio .problema-item-icon {
  background: #FEECEB;
  color: #D93829;
}

.solucion .problema-item-icon {
  background: #EAF3D1;
  color: var(--verde-geotec);
}

.problema-item-body strong {
  display: block;
  font-family: var(--font-display);
  font-size: 0.98rem;
  font-weight: 700;
  color: var(--texto-principal);
  margin-bottom: 2px;
}

.problema-item-body p {
  font-size: 0.88rem;
  color: var(--texto-secundario);
  line-height: 1.45;
}

/* ============================================================
   SECCIÓN: 5 LÍNEAS FUNCIONALES INNOLAB (Fichas Técnicas GEOTEC)
   ============================================================ */
.section-lineas {
  padding: 95px 0;
  background-color: var(--hueso);
  border-bottom: 1px solid var(--gris-linea);
}

.lineas-tabs {
  display: flex;
  gap: 8px;
  justify-content: center;
  margin-bottom: 40px;
  flex-wrap: wrap;
}

.tab-btn {
  padding: 10px 18px;
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: 100px;
  font-family: var(--font-display);
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--carbon);
  cursor: pointer;
  transition: var(--transition);
  display: flex;
  align-items: center;
  gap: 8px;
}

.tab-btn span.num {
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--verde-geotec);
}

.tab-btn:hover {
  border-color: var(--verde-geotec);
  color: var(--verde-geotec);
}

.tab-btn.active {
  background: var(--verde-noche);
  border-color: var(--verde-noche);
  color: #FFFFFF;
}

.tab-btn.active span.num {
  color: var(--amarillo-isotipo);
}

.linea-ficha-container {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.linea-ficha {
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-lg);
  padding: 38px;
  box-shadow: var(--shadow-sm);
  display: none;
  animation: fadeIn 0.4s ease-out forwards;
}

.linea-ficha.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

.ficha-header-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--gris-linea);
}

.ficha-title-block h3 {
  font-family: var(--font-display);
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--verde-noche);
  text-transform: uppercase;
  margin-top: 4px;
}

.ficha-meta-badge {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  background: var(--caja-beige);
  padding: 6px 14px;
  border-radius: var(--radius-sm);
  font-weight: 600;
  color: var(--carbon);
}

.ficha-body-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 36px;
}

.ficha-detail-block h4 {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--verde-noche);
  text-transform: uppercase;
  margin-bottom: 12px;
}

.ficha-features-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 24px;
}

.ficha-features-list li {
  position: relative;
  padding-left: 20px;
  font-size: 0.92rem;
  color: var(--texto-secundario);
  line-height: 1.5;
}

.ficha-features-list li::before {
  content: '▪';
  position: absolute;
  left: 0;
  top: -2px;
  color: var(--verde-geotec);
  font-size: 1.1rem;
}

.ficha-card-sidebar {
  background: var(--verde-tinte);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.sidebar-kpi-box {
  background: var(--blanco);
  border-left: 3.5px solid var(--verde-geotec);
  padding: 14px;
  border-radius: var(--radius-sm);
}

.sidebar-kpi-num {
  font-family: var(--font-mono);
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--verde-noche);
}

.sidebar-kpi-label {
  font-size: 0.82rem;
  color: var(--texto-suave);
  margin-top: 2px;
}

.tech-pills-row {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.tech-pill {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  padding: 3px 8px;
  border-radius: 4px;
  color: var(--carbon);
}

/* ============================================================
   SECCIÓN: ESCALAMIENTO EN 4 FASES (Roadmap GEOTEC)
   ============================================================ */
.section-escalamiento {
  padding: 90px 0;
  background-color: var(--blanco);
  border-bottom: 1px solid var(--gris-linea);
}

.timeline-phases-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-top: 40px;
  position: relative;
}

.timeline-phases-grid::before {
  content: '';
  position: absolute;
  top: 40px;
  left: 5%;
  right: 5%;
  height: 2px;
  background: var(--gris-linea);
  z-index: 1;
}

.phase-card {
  background: var(--caja-beige);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  padding: 26px 20px;
  position: relative;
  z-index: 2;
  transition: var(--transition);
}

.phase-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: var(--verde-geotec);
  background: var(--verde-tinte);
}

.phase-node {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--blanco);
  border: 3px solid var(--verde-geotec);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: 1rem;
  color: var(--verde-geotec);
  margin-bottom: 18px;
  box-shadow: 0 0 0 6px var(--caja-beige);
}

.phase-card:hover .phase-node {
  background: var(--verde-geotec);
  color: #FFFFFF;
}

.phase-card h4 {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--verde-noche);
  text-transform: uppercase;
  margin-bottom: 8px;
}

.phase-tag {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 600;
  color: var(--verde-geotec);
  margin-bottom: 12px;
  display: block;
}

.phase-desc {
  font-size: 0.88rem;
  color: var(--texto-secundario);
  line-height: 1.5;
}

/* ============================================================
   SECCIÓN: SEGURIDAD, GOBIERNO & SOBERANÍA DEL DATO
   ============================================================ */
.section-seguridad {
  padding: 90px 0;
  background-color: var(--verde-tinte);
  border-bottom: 1px solid var(--gris-linea);
}

.seguridad-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 36px;
  align-items: stretch;
}

.seguridad-main-card {
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-lg);
  padding: 36px;
  box-shadow: var(--shadow-sm);
}

.garantias-list {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 24px;
}

.garantia-box {
  background: var(--hueso);
  border: 1px solid var(--gris-borde-suave);
  border-radius: var(--radius-sm);
  padding: 16px;
  border-left: 3px solid var(--verde-geotec);
}

.garantia-box h5 {
  font-family: var(--font-display);
  font-size: 0.96rem;
  font-weight: 700;
  color: var(--verde-noche);
  margin-bottom: 4px;
}

.garantia-box p {
  font-size: 0.84rem;
  color: var(--texto-secundario);
  line-height: 1.4;
}

.iso-cert-card {
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-lg);
  padding: 32px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  justify-content: center;
  box-shadow: var(--shadow-sm);
}

.iso-stamp-img {
  max-width: 170px;
  height: auto;
  margin-bottom: 18px;
}

.iso-cert-card h4 {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--verde-noche);
  margin-bottom: 6px;
}

.iso-cert-card p {
  font-size: 0.84rem;
  color: var(--texto-secundario);
  line-height: 1.45;
}

/* Sede Showcase Cards */
.sede-showcase-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 36px;
}

.sede-card {
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.sede-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
  border-color: var(--verde-geotec);
}

.sede-card img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  display: block;
}

.sede-card-body {
  padding: 18px 20px;
}

.sede-card-body h5 {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 700;
  color: var(--verde-noche);
  margin-bottom: 4px;
}

.sede-card-body p {
  font-size: 0.82rem;
  color: var(--texto-secundario);
  line-height: 1.4;
}

/* ============================================================
   SECCIÓN: CASOS REALES & PORTAFOLIO COMPROBADO
   ============================================================ */
.section-casos {
  padding: 95px 0 60px 0;
  background-color: var(--blanco);
  border-bottom: 1px solid var(--gris-linea);
}

/* Evidencia de Campo Destacada */
.campo-hero-card {
  background: var(--caja-beige);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-lg);
  overflow: hidden;
  margin-bottom: 48px;
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  box-shadow: var(--shadow-md);
  transition: var(--transition);
}

.campo-hero-card:hover {
  box-shadow: var(--shadow-lg);
  border-color: var(--verde-geotec);
}

.campo-hero-img-wrap {
  position: relative;
  min-height: 340px;
  overflow: hidden;
}

.campo-hero-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s ease;
}

.campo-hero-card:hover .campo-hero-img {
  transform: scale(1.03);
}

.campo-hero-badge {
  position: absolute;
  top: 18px;
  left: 18px;
  background: rgba(30, 42, 36, 0.9);
  backdrop-filter: blur(8px);
  color: var(--amarillo-isotipo);
  padding: 6px 14px;
  border-radius: 100px;
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 700;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.campo-hero-content {
  padding: 38px 32px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.campo-hero-content h3 {
  font-family: var(--font-display);
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--verde-noche);
  text-transform: uppercase;
  margin-bottom: 12px;
  line-height: 1.2;
}

.campo-hero-content p {
  font-size: 0.94rem;
  color: var(--texto-secundario);
  line-height: 1.6;
  margin-bottom: 20px;
}

.campo-hero-highlights {
  display: flex;
  gap: 24px;
  border-top: 1px solid var(--gris-linea);
  padding-top: 16px;
}

.campo-hl-num {
  font-family: var(--font-mono);
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--verde-geotec);
}

.campo-hl-label {
  font-size: 0.78rem;
  color: var(--texto-suave);
}

.casos-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.caso-card {
  background: var(--hueso);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  padding: 28px 24px;
  transition: var(--transition);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.caso-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: var(--verde-geotec);
  background: #FFFFFF;
}

.caso-badge {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--verde-geotec);
  text-transform: uppercase;
  margin-bottom: 10px;
  display: block;
}

.caso-card h4 {
  font-family: var(--font-display);
  font-size: 1.18rem;
  font-weight: 800;
  color: var(--verde-noche);
  margin-bottom: 8px;
  line-height: 1.3;
}

.caso-stat-highlight {
  font-family: var(--font-mono);
  font-size: 2rem;
  font-weight: 700;
  color: var(--verde-noche);
  margin: 12px 0 6px 0;
}

.caso-stat-highlight span {
  color: var(--verde-geotec);
}

.caso-desc {
  font-size: 0.88rem;
  color: var(--texto-secundario);
  line-height: 1.5;
  margin-bottom: 16px;
}

.caso-footer {
  padding-top: 12px;
  border-top: 1px solid var(--gris-linea);
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--carbon);
}

/* ============================================================
   SECCIÓN: CARRUSEL CONTINUO DE CLIENTES (Marquee Oficial)
   ============================================================ */
.clients-section {
  padding: 60px 0;
  background-color: var(--verde-tinte);
  border-bottom: 1px solid var(--gris-linea);
  position: relative;
  overflow: hidden;
}

.clients-head {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--carbon);
  text-align: center;
  margin-bottom: 24px;
}

.marquee-outer {
  overflow: hidden;
  margin-bottom: 14px;
  mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
  -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
}

.marquee-track {
  display: flex;
  gap: 0;
  white-space: nowrap;
  width: max-content;
  animation: marqueeA 30s linear infinite;
}

.marquee-track.rev {
  animation-direction: reverse;
  animation-duration: 34s;
}

.marquee-outer:hover .marquee-track {
  animation-play-state: paused;
}

.client-chip {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 64px;
  padding: 0 28px;
  background: #FFFFFF;
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  margin: 0 8px;
  flex-shrink: 0;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.client-chip:hover {
  border-color: var(--verde-geotec);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.client-chip img {
  max-height: 38px;
  max-width: 140px;
  object-fit: contain;
  filter: grayscale(15%);
  transition: var(--transition);
}

.client-chip:hover img {
  filter: grayscale(0%);
}

@keyframes marqueeA {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* ============================================================
   SECCIÓN: CTA INSTITUCIONAL & CONTACTO (Registro B - Slide 25)
   ============================================================ */
.section-cta {
  padding: 100px 0;
  background: linear-gradient(135deg, var(--verde-noche) 0%, #111A15 100%);
  color: #FFFFFF;
  position: relative;
  overflow: hidden;
}

.cta-watermark {
  position: absolute;
  top: -50px;
  right: -50px;
  width: 480px;
  height: 480px;
  opacity: 0.05;
  pointer-events: none;
}

.cta-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 50px;
  align-items: center;
  position: relative;
  z-index: 2;
}

.cta-title {
  font-family: var(--font-display);
  font-size: 2.5rem;
  font-weight: 900;
  line-height: 1.18;
  text-transform: uppercase;
  margin-bottom: 14px;
  color: #FFFFFF;
}

.cta-title span {
  color: var(--amarillo-isotipo);
}

.cta-desc {
  font-size: 1.08rem;
  color: var(--texto-inverso-mut);
  line-height: 1.6;
  margin-bottom: 30px;
}

.cta-card-contact {
  background: rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: var(--radius-lg);
  padding: 36px;
}

.contact-info-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 28px;
}

.contact-info-item {
  display: flex;
  align-items: flex-start;
  gap: 14px;
}

.contact-info-item svg {
  width: 20px;
  height: 20px;
  fill: var(--amarillo-isotipo);
  flex-shrink: 0;
  margin-top: 2px;
}

.contact-info-item div strong {
  display: block;
  font-family: var(--font-display);
  font-size: 0.95rem;
  font-weight: 700;
  color: #FFFFFF;
}

.contact-info-item div a,
.contact-info-item div span {
  color: var(--texto-inverso-mut);
  text-decoration: none;
  font-size: 0.88rem;
}

.contact-info-item div a:hover {
  color: var(--amarillo-isotipo);
}

/* ============================================================
   FOOTER INSTITUCIONAL
   ============================================================ */
.footer {
  background: #0D1410;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding: 40px 0 30px 0;
  color: var(--texto-inverso-mut);
  font-size: 0.84rem;
}

.footer-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 24px;
  padding-bottom: 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 16px;
}

.footer-logo {
  height: 32px;
  width: auto;
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 20px;
  font-size: 0.78rem;
  color: #8C9078;
  flex-wrap: wrap;
  gap: 12px;
}

/* ============================================================
   RESPONSIVE DESIGN (Tablets y Smartphones)
   ============================================================ */
@media (max-width: 1024px) {
  .hero-grid,
  .problematica-grid,
  .seguridad-grid,
  .campo-hero-card,
  .cta-grid,
  .ficha-body-grid {
    grid-template-columns: 1fr;
  }
  
  .ciclo-grid,
  .certezas-grid,
  .timeline-phases-grid,
  .casos-grid,
  .sede-showcase-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .timeline-phases-grid::before {
    display: none;
  }

  .hero-title-main {
    font-size: 2.25rem;
  }

  .hero-stats-row {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .nav-menu {
    display: none;
  }
  
  .nav-toggle {
    display: block;
  }

  .hero-title-main {
    font-size: 1.9rem;
  }

  .hero-title-sub {
    font-size: 1.3rem;
  }

  .ciclo-grid,
  .certezas-grid,
  .timeline-phases-grid,
  .casos-grid,
  .garantias-list,
  .sede-showcase-grid {
    grid-template-columns: 1fr;
  }

  .hero-stats-row {
    grid-template-columns: 1fr 1fr;
  }

  .footer-inner,
  .footer-bottom {
    flex-direction: column;
    text-align: center;
  }
}
</style>
</head>
<body>

<!-- ============================================================
     GEOTEC INTRO MOTION (Splash Screen Preloader)
     ============================================================ -->
<div id="geotec-preloader" aria-hidden="true">
  <div class="preloader-logo-wrap">
    <img src="assets/logo_geotec_color.png" alt="GEOTEC Ingeniería Ltda." class="preloader-logo">
    <span class="preloader-tagline">Ingeniería que Convierte Complejidad en Decisiones Confiables</span>
  </div>
  <div class="preloader-spinner"></div>
</div>

<!-- Barra de lectura de progreso -->
<div id="scroll-progress"></div>

<!-- ============================================================
     NAVBAR
     ============================================================ -->
<nav class="navbar" id="navbar">
  <div class="container navbar-inner">
    <a href="#inicio" class="navbar-brand-group">
      <img src="assets/logo_geotec_color.png" alt="GEOTEC" class="nav-logo-geotec">
      <div class="nav-divider"></div>
      <img src="assets/innolab_logo.png" alt="InnoLab" class="nav-logo-innolab">
      <div class="nav-divider"></div>
      <img src="assets/cenit_logo.png" alt="CENIT" class="nav-logo-cenit">
    </a>

    <ul class="nav-menu" id="navMenu">
      <li><a href="#inicio" class="active">Inicio</a></li>
      <li><a href="#certezas">5 Certezas</a></li>
      <li><a href="#problematica">Problemática</a></li>
      <li><a href="#lineas">5 Líneas InnoLab</a></li>
      <li><a href="#escalamiento">Escalamiento</a></li>
      <li><a href="#seguridad">Seguridad</a></li>
      <li><a href="#casos">Casos Reales</a></li>
      <li><a href="#clientes">Clientes</a></li>
      <li><a href="#contacto" class="nav-cta">Agendar Sesión</a></li>
    </ul>

    <button class="nav-toggle" id="navToggle" aria-label="Abrir menú">
      <span></span>
      <span></span>
      <span></span>
    </button>
  </div>
</nav>

<!-- ============================================================
     SECCIÓN 1: INICIO / HERO EDITORIAL (Corporate Book & Tokens)
     ============================================================ -->
<section id="inicio" class="hero-section">
  <div class="container hero-grid">
    <div class="hero-content">
      <div class="hero-pretitle">
        <span class="tag-institucional amarillo">Sondeo de Mercado VH-2026-369</span>
        <span class="tag-institucional">GEOTEC InnoLab</span>
      </div>

      <h1 class="hero-title-main">Ingeniería que Convierte Complejidad</h1>
      <h2 class="hero-title-sub">En Decisiones Confiables para CENIT</h2>
      <div class="barra-acento-inferior"></div>

      <p class="hero-description">
        Transformamos los desafíos socioambientales, regulatorios y territoriales de la infraestructura en <strong>soluciones digitales en producción</strong>. Conectamos más de <strong>25 años de experiencia técnica</strong> en el sector energético colombiano con <strong>91 herramientas activas</strong> del ecosistema InnoLab.
      </p>

      <div class="hero-actions">
        <a href="#lineas" class="btn-primary">
          <span>Explorar 5 Líneas InnoLab</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
        <a href="#casos" class="btn-secondary">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg>
          <span>Ver Casos Reales</span>
        </a>
      </div>

      <!-- Respaldo Cuantitativo -->
      <div class="hero-stats-row">
        <div class="hero-stat-item">
          <span class="hero-stat-num">25<span>+</span></span>
          <span class="hero-stat-label">Años de Trayectoria Aplicada</span>
        </div>
        <div class="hero-stat-item">
          <span class="hero-stat-num">91</span>
          <span class="hero-stat-label">Herramientas en Producción</span>
        </div>
        <div class="hero-stat-item">
          <span class="hero-stat-num">300<span>+</span></span>
          <span class="hero-stat-label">Expedientes Gestionados</span>
        </div>
        <div class="hero-stat-item">
          <span class="hero-stat-num">5.000<span>+</span></span>
          <span class="hero-stat-label">Actos Administrativos Atendidos</span>
        </div>
      </div>
    </div>

    <!-- Visual Card: Corporate Book Cover -->
    <div class="hero-visual-card">
      <div class="hero-book-img-wrapper">
        <img src="assets/geotec_corporate_book_cover.png" alt="GEOTEC Corporate Book 2026 - Territorios que Perduran" class="hero-book-cover-img">
        
        <div class="hero-concept-floating pos-top-left">
          <span class="concept-label">Estrategia</span>
          <span class="concept-val">Conocimiento · Soluciones Sostenibles</span>
        </div>

        <div class="hero-concept-floating pos-bottom-right">
          <span class="concept-label">Propósito</span>
          <span class="concept-val">Territorios que Perduran</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     SECCIÓN 2: EL CICLO GEOTEC Y LAS 5 DIMENSIONES DE CERTEZA
     ============================================================ -->
<section id="certezas" class="section-certezas">
  <div class="container">
    <div class="section-header">
      <span class="folio-numero">01 // MODELO INSTITUCIONAL</span>
      <h2 class="section-title">Acompañamiento Integral en Todo el Ciclo</h2>
      <div class="barra-acento-inferior center"></div>
      <p class="section-subtitle">
        Más que gestionar obligaciones aisladas, aseguramos la continuidad operativa de CENIT mediante un modelo técnico, preventivo y alineado con los máximos estándares socioambientales.
      </p>
    </div>

    <!-- 4 Ejes del Ciclo de Vida -->
    <div class="ciclo-grid">
      <div class="ciclo-card">
        <div class="ciclo-card-num">01</div>
        <h3 class="ciclo-card-title">Viabilizar</h3>
        <p class="ciclo-card-desc">Evaluación de alternativas, estudios de impacto ambiental (EIA) y diseño de medidas de manejo (PMA) técnica y socialmente defendibles.</p>
        <div class="ciclo-card-metrics">+300 EIA, PMA y Estudios Especializados</div>
      </div>

      <div class="ciclo-card">
        <div class="ciclo-card-num">02</div>
        <h3 class="ciclo-card-title">Articular</h3>
        <p class="ciclo-card-desc">Diseño territorial, cumplimiento normativo (TdR, Escazú, ANLA) y relacionamiento transparente con comunidades y propietarios.</p>
        <div class="ciclo-card-metrics">76 Unidades Territoriales · 2.740 Participantes</div>
      </div>

      <div class="ciclo-card">
        <div class="ciclo-card-num">03</div>
        <h3 class="ciclo-card-title">Acompañar</h3>
        <p class="ciclo-card-desc">Sostenemos cumplimiento, trazabilidad documental y respuesta oportuna ante la autoridad para proteger la continuidad de la operación.</p>
        <div class="ciclo-card-metrics">+400 Informes de Cumplimiento (ICA)</div>
      </div>

      <div class="ciclo-card">
        <div class="ciclo-card-num">04</div>
        <h3 class="ciclo-card-title">Cerrar & Sostener</h3>
        <p class="ciclo-card-desc">Abandono y desmantelamiento responsable de activos, saneamiento de pasivos críticos e integración de estándares ESG, IFC y GRI.</p>
        <div class="ciclo-card-metrics">+800 Cargas Saneadas en Campo</div>
      </div>
    </div>

    <!-- 5 Dimensiones de Certeza Banner -->
    <div class="certezas-banner">
      <img src="assets/isotipo_geotec_blanco.png" alt="" class="certezas-watermark">
      <div class="certezas-header-inner">
        <span class="tag-institucional dark">Propuesta de Valor</span>
        <h3 style="margin-top: 10px;">Con GEOTEC, CENIT Elige Certeza</h3>
        <p style="color: var(--texto-inverso-mut); font-size: 0.95rem; margin-top: 6px;">
          Transformamos complejidad en decisiones trazables para decidir, operar y avanzar.
        </p>
      </div>

      <div class="certezas-grid">
        <div class="certeza-item">
          <div class="certeza-item-title">Certeza Técnica</div>
          <div class="certeza-item-text">Más de 25 años de experiencia aplicada y rigor científico en hidrocarburos y transporte.</div>
        </div>

        <div class="certeza-item">
          <div class="certeza-item-title">Certeza Operativa</div>
          <div class="certeza-item-text">Conocimiento real del terreno, ductos, estaciones y la dinámica de las comunidades.</div>
        </div>

        <div class="certeza-item">
          <div class="certeza-item-title">Certeza Preventiva</div>
          <div class="certeza-item-text">Modelaciones y monitoreo temprano para anticipar cuellos de botella y contingencias.</div>
        </div>

        <div class="certeza-item">
          <div class="certeza-item-title">Certeza Documental</div>
          <div class="certeza-item-text">InnoLab: 91 herramientas automatizadas para auditorías, ICAs y trazabilidad 100% verificable.</div>
        </div>

        <div class="certeza-item">
          <div class="certeza-item-title">Certeza Regulatoria</div>
          <div class="certeza-item-text">Sustentaciones técnica y jurídicamente blindadas ante ANLA, MinAmbiente y Corporaciones.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     SECCIÓN 3: PROBLEMÁTICA & ENFOQUE INTEGRADO
     ============================================================ -->
<section id="problematica" class="section-problematica">
  <div class="container">
    <div class="section-header">
      <span class="folio-numero">02 // DIAGNÓSTICO OPERATIVO</span>
      <h2 class="section-title">La Gestión de Infraestructura Exige Control</h2>
      <div class="barra-acento-inferior center"></div>
      <p class="section-subtitle">
        Comparación directa entre las limitaciones de los modelos dispersos tradicionales y el ecosistema integrado InnoLab desarrollado por GEOTEC.
      </p>
    </div>

    <div class="problematica-grid">
      <!-- Desafíos Tradicionales -->
      <div class="problema-col desafio">
        <div class="problema-col-header">
          <span class="tag-institucional" style="background:#FEECEB; color:#D93829; border-color:rgba(217,56,41,0.2);">Modelo Convencional</span>
          <h3 class="col-header-title">Fricciones y Riesgos</h3>
        </div>

        <div class="problema-item-list">
          <div class="problema-item">
            <div class="problema-item-icon">✕</div>
            <div class="problema-item-body">
              <strong>Silos de Información y Datos Dispersos</strong>
              <p>Geodatabases, informes PDF, actas prediales y reportes de campo fragmentados en múltiples carpetas y contratistas sin estándar unificado.</p>
            </div>
          </div>

          <div class="problema-item">
            <div class="problema-item-icon">✕</div>
            <div class="problema-item-body">
              <strong>Cuello de Botella en Validación Manual</strong>
              <p>Revisión tardía de capas geográficas y modelos ANLA al final de la consultoría, generando reprocesos y observaciones de la autoridad.</p>
            </div>
          </div>

          <div class="problema-item">
            <div class="problema-item-icon">✕</div>
            <div class="problema-item-body">
              <strong>Riesgo de Pérdida de Trazabilidad</strong>
              <p>Dificultad para sustentar históricamente el cumplimiento de obligaciones ambientales de vigencias anteriores ante requerimientos urgentes.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Solución GEOTEC InnoLab -->
      <div class="problema-col solucion">
        <div class="problema-col-header">
          <span class="tag-institucional">GEOTEC InnoLab</span>
          <h3 class="col-header-title">Ecosistema Integrado</h3>
        </div>

        <div class="problema-item-list">
          <div class="problema-item">
            <div class="problema-item-icon">✓</div>
            <div class="problema-item-body">
              <strong>Validación Automatizada en Tiempo Real</strong>
              <p>Control estricto de topología, dominios, catálogos de objetos y normativas ANLA desde la captura misma del dato en campo.</p>
            </div>
          </div>

          <div class="problema-item">
            <div class="problema-item-icon">✓</div>
            <div class="problema-item-body">
              <strong>Inteligencia Documental y Saneamiento</strong>
              <p>Procesamiento automatizado de expedientes, extracción de obligaciones y cruce directo con los Informes de Cumplimiento Ambiental (ICA).</p>
            </div>
          </div>

          <div class="problema-item">
            <div class="problema-item-icon">✓</div>
            <div class="problema-item-body">
              <strong>Decisiones Oportunas y Soberanía Total</strong>
              <p>Visores de consulta multicapa con buffers de derechos de vía y despliegue exclusivo en la infraestructura privada de CENIT.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     SECCIÓN 4: 5 LÍNEAS FUNCIONALES INNOLAB (Fichas Técnicas)
     ============================================================ -->
<section id="lineas" class="section-lineas">
  <div class="container">
    <div class="section-header">
      <span class="folio-numero">03 // CAPACIDADES EN PRODUCCIÓN</span>
      <h2 class="section-title">Cinco Líneas Funcionales, Un Mismo Ciclo del Dato</h2>
      <div class="barra-acento-inferior center"></div>
      <p class="section-subtitle">
        91 herramientas de software desarrolladas y probadas en operaciones reales de alta complejidad. Haz clic en cada línea para ver su ficha técnica detallada.
      </p>
    </div>

    <!-- Tabs de Selección -->
    <div class="lineas-tabs">
      <button class="tab-btn active" onclick="switchLinea(0)">
        <span class="num">01</span>
        <span>Aseguramiento Geoespacial</span>
      </button>
      <button class="tab-btn" onclick="switchLinea(1)">
        <span class="num">02</span>
        <span>Captura Digital de Campo</span>
      </button>
      <button class="tab-btn" onclick="switchLinea(2)">
        <span class="num">03</span>
        <span>Consulta Territorial</span>
      </button>
      <button class="tab-btn" onclick="switchLinea(3)">
        <span class="num">04</span>
        <span>Inteligencia Documental</span>
      </button>
      <button class="tab-btn" onclick="switchLinea(4)">
        <span class="num">05</span>
        <span>Gestión de Portafolios</span>
      </button>
    </div>

    <!-- Fichas Técnicas -->
    <div class="linea-ficha-container">
      <!-- Línea 1 -->
      <div class="linea-ficha active" id="linea-0">
        <div class="ficha-header-row">
          <div class="ficha-title-block">
            <span class="folio-numero">LÍNEA 01 // FICHA TÉCNICA</span>
            <h3>Aseguramiento y Certificación del Dato Geoespacial</h3>
            <div class="barra-acento-inferior"></div>
          </div>
          <span class="ficha-meta-badge">28 Herramientas Activas</span>
        </div>

        <div class="ficha-body-grid">
          <div class="ficha-detail-block">
            <h4>Alcance y Funcionalidad</h4>
            <p style="font-size: 0.94rem; color: var(--texto-secundario); margin-bottom: 16px; line-height: 1.55;">
              Automatiza la validación rigurosa de modelos de datos geográficos (GDB) bajo las especificaciones de la ANLA (Resoluciones 2182/2016, Metodología General 2026) y estándares corporativos de transporte de hidrocarburos.
            </p>
            <ul class="ficha-features-list">
              <li><strong>Validación Topológica Continua:</strong> Detección instantánea de auto-intersecciones, solapes, líneas desconectadas y gaps en coberturas y polilíneas de ductos.</li>
              <li><strong>Control de Dominios y Catálogos:</strong> Verificación de integridad referencial contra los diccionarios oficiales de datos sin intervención manual.</li>
              <li><strong>Generador de Reportes de Conformidad:</strong> Emisión automática de certificados de calidad técnica listos para auditorías regulatorias.</li>
            </ul>
          </div>

          <div class="ficha-card-sidebar">
            <div class="sidebar-kpi-box">
              <div class="sidebar-kpi-num">100%</div>
              <div class="sidebar-kpi-label">Conformidad con Modelo ANLA</div>
            </div>
            <div>
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--carbon); margin-bottom: 6px; text-transform: uppercase;">Tecnologías Aplicadas</div>
              <div class="tech-pills-row">
                <span class="tech-pill">Python</span>
                <span class="tech-pill">ArcPy / GDAL</span>
                <span class="tech-pill">PostGIS</span>
                <span class="tech-pill">GeoPandas</span>
                <span class="tech-pill">FME Engine</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Línea 2 -->
      <div class="linea-ficha" id="linea-1">
        <div class="ficha-header-row">
          <div class="ficha-title-block">
            <span class="folio-numero">LÍNEA 02 // FICHA TÉCNICA</span>
            <h3>Captura Digital de Campo y Trazabilidad de Evidencias</h3>
            <div class="barra-acento-inferior"></div>
          </div>
          <span class="ficha-meta-badge">14 Herramientas Activas</span>
        </div>

        <div class="ficha-body-grid">
          <div class="ficha-detail-block">
            <h4>Alcance y Funcionalidad</h4>
            <p style="font-size: 0.94rem; color: var(--texto-secundario); margin-bottom: 16px; line-height: 1.55;">
              Garantiza la captura estructurada de información biótica, física y social directamente en terreno, eliminando planillas físicas y vinculando evidencia fotográfica inalterable con coordenadas GNSS.
            </p>
            <ul class="ficha-features-list">
              <li><strong>Operación 100% Desconectada (Offline-First):</strong> Formularios dinámicos que operan en zonas remotas de derecho de vía sin cobertura celular.</li>
              <li><strong>Sello de Integridad y Metadatos EXIF:</strong> Registro automático de fecha, hora, azimut, precisión satelital y firma digital del especialista.</li>
              <li><strong>Sincronización Segura:</strong> Transmisión encriptada a la base central una vez restablecida la conexión.</li>
            </ul>
          </div>

          <div class="ficha-card-sidebar">
            <div class="sidebar-kpi-box">
              <div class="sidebar-kpi-num">0%</div>
              <div class="sidebar-kpi-label">Pérdida de Evidencia en Campo</div>
            </div>
            <div>
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--carbon); margin-bottom: 6px; text-transform: uppercase;">Tecnologías Aplicadas</div>
              <div class="tech-pills-row">
                <span class="tech-pill">ODK / Kobo</span>
                <span class="tech-pill">QField</span>
                <span class="tech-pill">SQLite / SpatiaLite</span>
                <span class="tech-pill">OpenCV EXIF</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Línea 3 -->
      <div class="linea-ficha" id="linea-2">
        <div class="ficha-header-row">
          <div class="ficha-title-block">
            <span class="folio-numero">LÍNEA 03 // FICHA TÉCNICA</span>
            <h3>Servicios de Datos y Consulta Territorial Multicapa</h3>
            <div class="barra-acento-inferior"></div>
          </div>
          <span class="ficha-meta-badge">21 Herramientas Activas</span>
        </div>

        <div class="ficha-body-grid">
          <div class="ficha-detail-block">
            <h4>Alcance y Funcionalidad</h4>
            <p style="font-size: 0.94rem; color: var(--texto-secundario); margin-bottom: 16px; line-height: 1.55;">
              Centraliza el inventario geoespacial de activos, ductos, estaciones y determinantes ambientales oficiales (RUNAP, POMCA, resguardos indígenas, títulos mineros y rondas hídricas).
            </p>
            <ul class="ficha-features-list">
              <li><strong>Geoprocesamiento Automatizado de Buffers:</strong> Análisis de impacto y áreas de influencia directa/indirecta en segundos.</li>
              <li><strong>Cruce de Restricciones Ambientales:</strong> Identificación temprana de traslapes con áreas protegidas o comunidades étnicas.</li>
              <li><strong>Servicios OGC Estándar:</strong> Conexión nativa mediante WMS, WFS y APIs REST seguras para los sistemas GIS corporativos de CENIT.</li>
            </ul>
          </div>

          <div class="ficha-card-sidebar">
            <div class="sidebar-kpi-box">
              <div class="sidebar-kpi-num">&lt; 3 s</div>
              <div class="sidebar-kpi-label">Tiempo de Respuesta en Consultas</div>
            </div>
            <div>
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--carbon); margin-bottom: 6px; text-transform: uppercase;">Tecnologías Aplicadas</div>
              <div class="tech-pills-row">
                <span class="tech-pill">GeoServer</span>
                <span class="tech-pill">Leaflet / MapLibre</span>
                <span class="tech-pill">PostGIS TileServer</span>
                <span class="tech-pill">FastAPI</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Línea 4 -->
      <div class="linea-ficha" id="linea-3">
        <div class="ficha-header-row">
          <div class="ficha-title-block">
            <span class="folio-numero">LÍNEA 04 // FICHA TÉCNICA</span>
            <h3>Inteligencia Documental y Saneamiento Regulatorio</h3>
            <div class="barra-acento-inferior"></div>
          </div>
          <span class="ficha-meta-badge">16 Herramientas Activas</span>
        </div>

        <div class="ficha-body-grid">
          <div class="ficha-detail-block">
            <h4>Alcance y Funcionalidad</h4>
            <p style="font-size: 0.94rem; color: var(--texto-secundario); margin-bottom: 16px; line-height: 1.55;">
              Convierte miles de páginas de expedientes administrativos, resoluciones, autos de seguimiento e ICAs en bases de conocimiento estructuradas, trazables y auditables.
            </p>
            <ul class="ficha-features-list">
              <li><strong>Extracción Semántica de Obligaciones:</strong> Tipificación automática de artículos resolutivos, plazos, responsables y condiciones de cumplimiento.</li>
              <li><strong>Matriz Dinámica de Cumplimiento:</strong> Semaforización de compromisos ante la ANLA y Corporaciones Autónomas Regionales.</li>
              <li><strong>Asistente Técnico de Búsqueda Regulatoria:</strong> Recuperación exacta de antecedentes y jurisprudencia técnica en segundos.</li>
            </ul>
          </div>

          <div class="ficha-card-sidebar">
            <div class="sidebar-kpi-box">
              <div class="sidebar-kpi-num">85%</div>
              <div class="sidebar-kpi-label">Ahorro en Tiempos de Auditoría</div>
            </div>
            <div>
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--carbon); margin-bottom: 6px; text-transform: uppercase;">Tecnologías Aplicadas</div>
              <div class="tech-pills-row">
                <span class="tech-pill">Python NLP</span>
                <span class="tech-pill">PyMuPDF / pdfplumber</span>
                <span class="tech-pill">LLM Seguro / Local RAG</span>
                <span class="tech-pill">Elasticsearch</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Línea 5 -->
      <div class="linea-ficha" id="linea-4">
        <div class="ficha-header-row">
          <div class="ficha-title-block">
            <span class="folio-numero">LÍNEA 05 // FICHA TÉCNICA</span>
            <h3>Gestión de Portafolios y Tableros Ejecutivos</h3>
            <div class="barra-acento-inferior"></div>
          </div>
          <span class="ficha-meta-badge">12 Herramientas Activas</span>
        </div>

        <div class="ficha-body-grid">
          <div class="ficha-detail-block">
            <h4>Alcance y Funcionalidad</h4>
            <p style="font-size: 0.94rem; color: var(--texto-secundario); margin-bottom: 16px; line-height: 1.55;">
              Consolida la visión gerencial del estado ambiental de toda la red de ductos e infraestructura de CENIT, integrando alertas tempranas y control presupuestal de compensaciones.
            </p>
            <ul class="ficha-features-list">
              <li><strong>Tableros de Mando en Tiempo Real:</strong> Indicadores de cumplimiento legal, estado de trámites de permisos menores y licencias.</li>
              <li><strong>Monitoreo de Compensaciones (1% e Inversión Forzosa):</strong> Seguimiento georreferenciado a predios y proyectos de restauración.</li>
              <li><strong>Alertas Preventivas de Vencimientos:</strong> Notificaciones programadas sobre vigencias de concesiones de agua, vertimientos y emisiones.</li>
            </ul>
          </div>

          <div class="ficha-card-sidebar">
            <div class="sidebar-kpi-box">
              <div class="sidebar-kpi-num">100%</div>
              <div class="sidebar-kpi-label">Visibilidad Ejecutiva Integral</div>
            </div>
            <div>
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--carbon); margin-bottom: 6px; text-transform: uppercase;">Tecnologías Aplicadas</div>
              <div class="tech-pills-row">
                <span class="tech-pill">PowerBI Embedded</span>
                <span class="tech-pill">ECharts / D3.js</span>
                <span class="tech-pill">PostgreSQL / Timescale</span>
                <span class="tech-pill">REST APIs</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     SECCIÓN 5: ESCALAMIENTO EN CUATRO FASES (Roadmap)
     ============================================================ -->
<section id="escalamiento" class="section-escalamiento">
  <div class="container">
    <div class="section-header">
      <span class="folio-numero">04 // RUTA DE ADOPCIÓN</span>
      <h2 class="section-title">Escalamiento Modular sin Fricción</h2>
      <div class="barra-acento-inferior center"></div>
      <p class="section-subtitle">
        Diseñado para entregar valor inmediato desde el primer mes, integrándose de forma progresiva con los sistemas existentes de CENIT.
      </p>
    </div>

    <div class="timeline-phases-grid">
      <div class="phase-card">
        <div class="phase-node">01</div>
        <span class="phase-tag">Meses 1 – 2</span>
        <h4>Diagnóstico y Piloto</h4>
        <p class="phase-desc">Aprestamiento institucional, mapeo de expedientes piloto y validación inicial con herramientas de Línea 1 y 2 en un tramo de infraestructura seleccionado.</p>
      </div>

      <div class="phase-card">
        <div class="phase-node">02</div>
        <span class="phase-tag">Meses 3 – 5</span>
        <h4>Despliegue Distribuido</h4>
        <p class="phase-desc">Capacitación de equipos de campo, puesta en marcha de captura desconectada y automatización del procesamiento de ICAs con Inteligencia Documental.</p>
      </div>

      <div class="phase-card">
        <div class="phase-node">03</div>
        <span class="phase-tag">Meses 6 – 9</span>
        <h4>Operación Centralizada</h4>
        <p class="phase-desc">Integración total del Geovisor Multicapa corporativo, tableros de control gerencial de portafolio y conexión con los repositorios centrales de CENIT.</p>
      </div>

      <div class="phase-card">
        <div class="phase-node">04</div>
        <span class="phase-tag">Meses 10 – 12</span>
        <h4>Consolidación y Transferencia</h4>
        <p class="phase-desc">Optimización continua, entrega de manuales técnicos, soporte especializado permanente y autosuficiencia operativa para los administradores del cliente.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     SECCIÓN 6: SEGURIDAD, GOBIERNO & SOBERANÍA DEL DATO
     ============================================================ -->
<section id="seguridad" class="section-seguridad">
  <div class="container">
    <div class="section-header">
      <span class="folio-numero">05 // CONFIANZA Y GOBIERNO</span>
      <h2 class="section-title">Soberanía Total y Rigor Institucional</h2>
      <div class="barra-acento-inferior center"></div>
      <p class="section-subtitle">
        Garantizamos que la información estratégica de CENIT permanezca bajo su absoluto control, con arquitectura segura y un plan activo de madurez tecnológica continua.
      </p>
    </div>

    <div class="seguridad-grid">
      <div class="seguridad-main-card">
        <div class="barra-acento-lateral">
          <h3 style="font-family: var(--font-display); font-size: 1.45rem; font-weight: 800; color: var(--verde-noche); text-transform: uppercase;">
            Principios de Arquitectura y Soberanía
          </h3>
        </div>

        <div class="garantias-list">
          <div class="garantia-box">
            <h5>Aislamiento y Soberanía</h5>
            <p>Todo el procesamiento se despliega en la infraestructura privada (on-premise o nube corporativa) designada por CENIT, sin compartir datos con terceros.</p>
          </div>

          <div class="garantia-box">
            <h5>Control de Acceso RBAC</h5>
            <p>Autenticación robusta basada en roles para garantizar que cada usuario acceda exclusivamente a la información y expedientes autorizados.</p>
          </div>

          <div class="garantia-box">
            <h5>Trazabilidad Inmutable</h5>
            <p>Registro de auditoría (logs) de todas las consultas, modificaciones y exportaciones de cartografía o documentos oficiales.</p>
          </div>

          <div class="garantia-box">
            <h5>Cifrado Integral</h5>
            <p>Protocolos TLS 1.3 en tránsito y encriptación robusta de volúmenes en reposo para todas las bases de datos y repositorios de evidencias.</p>
          </div>
        </div>

        <!-- Hoja de Ruta y Madurez Progresiva -->
        <div style="margin-top: 32px; padding: 24px; background: var(--hueso); border: 1px solid var(--gris-linea); border-radius: var(--radius-md); border-left: 4px solid var(--amarillo-isotipo);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
            <h4 style="font-family: var(--font-display); font-size: 1.15rem; font-weight: 800; color: var(--verde-noche); text-transform: uppercase;">
              Hoja de Ruta y Madurez Progresiva
            </h4>
            <span class="tag-institucional amarillo">Evolución Continua</span>
          </div>
          <p style="font-size: 0.88rem; color: var(--texto-secundario); margin-bottom: 16px; line-height: 1.5;">
            Con el respaldo de nuestra experiencia y certificaciones vigentes, trabajamos de forma permanente en la evolución de nuestras capacidades de ciberseguridad y gobierno tecnológico:
          </p>

          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div style="display: flex; gap: 12px; align-items: flex-start;">
              <span style="font-family: var(--font-mono); font-weight: 700; color: var(--verde-geotec); font-size: 0.95rem; line-height: 1.4;">01.</span>
              <div style="font-size: 0.86rem; color: var(--texto-secundario); line-height: 1.45;">
                <strong style="color: var(--texto-principal);">Proyección de Certificaciones Especializadas:</strong> Avanzamos en el plan de alineación técnica hacia las certificaciones <strong>ISO/IEC 27001 y SOC 2</strong> en un horizonte proyectado de 12 a 18 meses, con plena disposición para formalizar hitos de avance dentro de los compromisos del servicio.
              </div>
            </div>

            <div style="display: flex; gap: 12px; align-items: flex-start;">
              <span style="font-family: var(--font-mono); font-weight: 700; color: var(--verde-geotec); font-size: 0.95rem; line-height: 1.4;">02.</span>
              <div style="font-size: 0.86rem; color: var(--texto-secundario); line-height: 1.45;">
                <strong style="color: var(--texto-principal);">Integración Nativa con el Directorio de CENIT:</strong> El ecosistema está diseñado para integrarse y delegar la gestión de identidades en el <em>Active Directory / SSO corporativo</em> de CENIT, asegurando que las políticas de seguridad y control multiusuario sean gobernadas directamente por los sistemas centrales del cliente.
              </div>
            </div>

            <div style="display: flex; gap: 12px; align-items: flex-start;">
              <span style="font-family: var(--font-mono); font-weight: 700; color: var(--verde-geotec); font-size: 0.95rem; line-height: 1.4;">03.</span>
              <div style="font-size: 0.86rem; color: var(--texto-secundario); line-height: 1.45;">
                <strong style="color: var(--texto-principal);">Seguridad y Cifrado en Capas:</strong> La protección de datos se apoya en el cifrado nativo de volúmenes e infraestructura empresarial, complementándose progresivamente con mecanismos de cifrado granular a nivel de aplicación según las necesidades operativas.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Sello ISO LL-C Card -->
      <div class="iso-cert-card">
        <img src="assets/sello_iso_llc.png" alt="Sello ISO 9001 · 14001 · 45001 LL-C Certification" class="iso-stamp-img">
        <h4>Certificación Trinorma LL-C</h4>
        <p style="margin-bottom: 16px;">
          GEOTEC cuenta con certificación internacional en <strong>ISO 9001</strong> (Calidad), <strong>ISO 14001</strong> (Gestión Ambiental) e <strong>ISO 45001</strong> (Seguridad y Salud en el Trabajo).
        </p>
        <div style="padding: 12px; background: var(--verde-tinte); border-radius: var(--radius-sm); font-size: 0.8rem; color: var(--carbon); border: 1px solid var(--gris-linea);">
          Base sólida de gestión integral para soportar procesos de auditoría y mejora continua.
        </div>
      </div>
    </div>

    <!-- Sede Corporativa & Centro de Ingeniería (Fotos de Empresa) -->
    <div class="sede-showcase-grid">
      <div class="sede-card">
        <img src="assets/oficina_fachada_calle.jpg" alt="Sede Corporativa GEOTEC Bogotá">
        <div class="sede-card-body">
          <h5>Sede Principal y Centro de Operaciones</h5>
          <p>Bogotá D.C. — Instalaciones con conectividad redundante y estaciones de trabajo de alto rendimiento para geoprocesamiento.</p>
        </div>
      </div>

      <div class="sede-card">
        <img src="assets/oficina_fachada_contrapicado.jpg" alt="Centro de Ingeniería GEOTEC">
        <div class="sede-card-body">
          <h5>Infraestructura Tecnológica Dedicada</h5>
          <p>Servidores propios, almacenamiento seguro y equipo interdisciplinario de ingeniería SIG, ambiental y de software.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     SECCIÓN 7: CASOS REALES & CAPACIDADES EN OPERACIÓN
     ============================================================ -->
<section id="casos" class="section-casos">
  <div class="container">
    <div class="section-header">
      <span class="folio-numero">06 // EXPERIENCIA DEMOSTRADA</span>
      <h2 class="section-title">Capacidades que Operan en Proyectos Reales</h2>
      <div class="barra-acento-inferior center"></div>
      <p class="section-subtitle">
        Casos de éxito documentados en operaciones de máxima exigencia técnica y regulatoria en Colombia.
      </p>
    </div>

    <!-- Tarjeta Destacada: Verificación en Campo y Línea Base -->
    <div class="campo-hero-card">
      <div class="campo-hero-img-wrap">
        <img src="assets/campo_verificacion_humedal.jpg" alt="Verificación Técnica en Campo y Línea Base" class="campo-hero-img">
        <span class="campo-hero-badge">Operación Real en Terreno</span>
      </div>
      <div class="campo-hero-content">
        <span class="tag-institucional" style="margin-bottom: 12px; width: fit-content;">Líneas 1, 2 y 3 en Campo</span>
        <h3>Verificación Técnica y Línea Base Geoespacial</h3>
        <p>
          Especialistas bióticos y geoespaciales validando en terreno cruces de infraestructura con determinantes ambientales, rondas hídricas y ecosistemas sensibles, capturando evidencia georreferenciada e inalterable.
        </p>
        <div class="campo-hero-highlights">
          <div>
            <div class="campo-hl-num">0%</div>
            <div class="campo-hl-label">Pérdida de Evidencia</div>
          </div>
          <div>
            <div class="campo-hl-num">100%</div>
            <div class="campo-hl-label">Trazabilidad GNSS</div>
          </div>
          <div>
            <div class="campo-hl-num">Offline</div>
            <div class="campo-hl-label">Operación en Zonas Remotas</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Grid de Casos de Éxito -->
    <div class="casos-grid">
      <!-- Caso 1 -->
      <div class="caso-card">
        <div>
          <span class="caso-badge">Ecopetrol · Piedemonte</span>
          <h4>Cierre Integral de Requerimientos ANLA</h4>
          <div class="caso-stat-highlight">105<span> Requerimientos</span></div>
          <p class="caso-desc">
            Saneamiento y unificación de 67 expedientes ambientales complejos (Cusiana, Cupiagua y Floreña), cerrando el 100% de observaciones sin requerimientos posteriores.
          </p>
        </div>
        <div class="caso-footer">Líneas 4 y 5 en Producción</div>
      </div>

      <!-- Caso 2 -->
      <div class="caso-card">
        <div>
          <span class="caso-badge">Ecopetrol · La Esmeralda</span>
          <h4>Modelación Hidrogeológica y Gestión Social</h4>
          <div class="caso-stat-highlight">470<span> Puntos de Agua</span></div>
          <p class="caso-desc">
            Caracterización predial y modelación hidrogeológica de alto detalle que desvirtuó quejas socioambientales con evidencia técnica verificable e inobjetable.
          </p>
        </div>
        <div class="caso-footer">Líneas 2 y 3 en Producción</div>
      </div>

      <!-- Caso 3 -->
      <div class="caso-card">
        <div>
          <span class="caso-badge">Ecopetrol · Sísmica Playón 3D</span>
          <h4>Intervención Segura de Pasivos Críticos</h4>
          <div class="caso-stat-highlight">800+<span> Cargas Saneadas</span></div>
          <p class="caso-desc">
            Saneamiento integral de pozo y cargas remanentes suspendidas en zona de alta sensibilidad social, logrando cero PQR y ejecución dentro de cronograma.
          </p>
        </div>
        <div class="caso-footer">Líneas 1, 2 y 4 en Producción</div>
      </div>

      <!-- Caso 4 -->
      <div class="caso-card">
        <div>
          <span class="caso-badge">Ecopetrol · Guamal & Cubarral</span>
          <h4>Participación Social que Construye Viabilidad</h4>
          <div class="caso-stat-highlight">2.424<span> Encuentros</span></div>
          <p class="caso-desc">
            Ferias interactivas y diálogo territorial predio a predio en 40 unidades territoriales para 2 EIA estratégicos con trazabilidad absoluta.
          </p>
        </div>
        <div class="caso-footer">Líneas 2 y 3 en Producción</div>
      </div>

      <!-- Caso 5 -->
      <div class="caso-card">
        <div>
          <span class="caso-badge">Ecopetrol · Offshore Fuerte Norte/Sur</span>
          <h4>Licenciamiento Marino de Alta Complejidad</h4>
          <div class="caso-stat-highlight">2<span> Licencias ANLA</span></div>
          <p class="caso-desc">
            Elaboración de EIA marinos con modelación hidrodinámica de contingencias y socialización costera, obteniendo las resoluciones 0723 y 1016 de 2012.
          </p>
        </div>
        <div class="caso-footer">Líneas 1 y 3 en Producción</div>
      </div>

      <!-- Caso 6 -->
      <div class="caso-card">
        <div>
          <span class="caso-badge">Frontera Energy Corp.</span>
          <h4>Gestión Integral de Portafolio Continuo</h4>
          <div class="caso-stat-highlight">7<span> Años Continuos</span></div>
          <p class="caso-desc">
            Acompañamiento integral y trazabilidad regulatoria de todo el portafolio ambiental de la operadora, con cero hallazgos críticos de la autoridad.
          </p>
        </div>
        <div class="caso-footer">Línea 5 en Producción</div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     SECCIÓN: CARRUSEL CONTINUO DE CLIENTES (Marquee Oficial)
     ============================================================ -->
<section id="clientes" class="clients-section" aria-label="Algunos de nuestros clientes">
  <div class="container">
    <p class="clients-head">Algunos de Nuestros Clientes en el Sector Energético e Industrial</p>
    
    <div class="marquee-outer">
      <div class="marquee-track" id="mq1"></div>
    </div>
    
    <div class="marquee-outer">
      <div class="marquee-track rev" id="mq2"></div>
    </div>
  </div>
</section>

<!-- ============================================================
     SECCIÓN 8: CTA INSTITUCIONAL & CONTACTO (Registro B)
     ============================================================ -->
<section id="contacto" class="section-cta">
  <img src="assets/textura_patron_blanco.png" alt="" class="cta-watermark">
  
  <div class="container cta-grid">
    <div>
      <span class="tag-institucional dark" style="margin-bottom: 16px;">Siguiente Paso</span>
      <h2 class="cta-title">
        Listos para Acompañar a <span>CENIT</span> desde el Primer Día
      </h2>
      <p class="cta-desc">
        Ponemos a disposición de los evaluadores técnicos de CENIT nuestro equipo directivo y especialistas en GIS para realizar una sesión técnica de demostración en vivo de las 91 herramientas de InnoLab.
      </p>

      <div style="display: flex; gap: 14px; flex-wrap: wrap;">
        <a href="mailto:comercial@geotecingenieria.com?subject=Sondeo%20CENIT%20VH-2026-369%20-%20Sesi%C3%B3n%20T%C3%A9cnica%20GEOTEC" class="btn-primary" style="background: var(--verde-geotec);">
          <span>Agendar Sesión Técnica</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </div>

    <!-- Contact Box -->
    <div class="cta-card-contact">
      <h3 style="font-family: var(--font-display); font-size: 1.35rem; font-weight: 800; color: #FFFFFF; text-transform: uppercase; margin-bottom: 20px;">
        Contacto Institucional
      </h3>

      <div class="contact-info-list">
        <div class="contact-info-item">
          <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          <div>
            <strong>Correo Electrónico Directo</strong>
            <a href="mailto:comercial@geotecingenieria.com">comercial@geotecingenieria.com</a>
          </div>
        </div>

        <div class="contact-info-item">
          <svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          <div>
            <strong>Línea de Atención Comercial</strong>
            <a href="tel:+573187070358">+57 318 707 0358</a>
          </div>
        </div>

        <div class="contact-info-item">
          <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
          <div>
            <strong>Sede Principal</strong>
            <span>Cra 15 No. 92-29, Oficina 405<br>Bogotá D.C., Colombia</span>
          </div>
        </div>
      </div>

      <div style="padding-top: 14px; border-top: 1px solid rgba(255, 255, 255, 0.12); display: flex; align-items: center; justify-content: space-between;">
        <span style="font-size: 0.78rem; color: var(--texto-inverso-mut); font-family: var(--font-mono);">RUT / NIT: 800.229.873-1</span>
        <span class="tag-institucional dark" style="font-size: 0.7rem;">GEOTEC LTDA</span>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     FOOTER
     ============================================================ -->
<footer class="footer">
  <div class="container">
    <div class="footer-inner">
      <div class="footer-brand">
        <img src="assets/logo_geotec_blanco.png" alt="GEOTEC" class="footer-logo">
      </div>

      <div style="display: flex; gap: 24px; align-items: center; flex-wrap: wrap;">
        <span style="font-size: 0.82rem; color: #C7C4AE;">Sondeo de Mercado CENIT VH-2026-369</span>
        <span style="color: #4F5927;">•</span>
        <span style="font-size: 0.82rem; color: #C7C4AE;">Ecosistema Tecnológico InnoLab</span>
        <span style="color: #4F5927;">•</span>
        <a href="https://www.geotecingenieria.com" target="_blank" rel="noopener" style="color: var(--amarillo-isotipo); text-decoration: none; font-size: 0.82rem;">www.geotecingenieria.com</a>
      </div>
    </div>

    <div class="footer-bottom">
      <div>
        © 2026 GEOTEC Ingeniería Ltda. Todos los derechos reservados. Información técnica confidencial para evaluación de CENIT.
      </div>
      <div>
        ISO 9001 · ISO 14001 · ISO 45001 | LL-C Certification
      </div>
    </div>
  </div>
</footer>

<!-- ============================================================
     JAVASCRIPT INTERACTIVO
     ============================================================ -->
<script>
// Clientes array para Marquee
const clients = [
  { src: 'assets/clientes/ecopetrol.png', alt: 'Ecopetrol' },
  { src: 'assets/clientes/frontera_energy.png', alt: 'Frontera Energy' },
  { src: 'assets/clientes/exxonmobil.png', alt: 'ExxonMobil' },
  { src: 'assets/clientes/bp.png', alt: 'BP' },
  { src: 'assets/clientes/bhp_billiton.png', alt: 'BHP Billiton' },
  { src: 'assets/clientes/petrobras.png', alt: 'Petrobras' },
  { src: 'assets/clientes/gran_tierra.png', alt: 'Gran Tierra' },
  { src: 'assets/clientes/equion.png', alt: 'Equion' },
  { src: 'assets/clientes/anh.png', alt: 'ANH' },
  { src: 'assets/clientes/cenit.png', alt: 'CENIT' },
  { src: 'assets/clientes/mintransporte.png', alt: 'Mintransporte' },
  { src: 'assets/clientes/tw_solar.png', alt: 'TW Solar' },
  { src: 'assets/clientes/acorn.png', alt: 'Acorn International' },
  { src: 'assets/clientes/fonade.png', alt: 'Fonade' },
  { src: 'assets/clientes/kof.png', alt: 'Coca-Cola FEMSA' },
  { src: 'assets/clientes/ocensa.webp', alt: 'Ocensa' },
  { src: 'assets/clientes/petrosantander.webp', alt: 'PetroSantander' },
  { src: 'assets/clientes/uaesp.png', alt: 'UAESP' },
  { src: 'assets/clientes/secop.png', alt: 'SECOP' }
];

function initClientMarquee() {
  const mq1 = document.getElementById('mq1');
  const mq2 = document.getElementById('mq2');
  if (!mq1 || !mq2) return;

  function makeChip(c) {
    const chip = document.createElement('div');
    chip.className = 'client-chip';
    const img = document.createElement('img');
    img.src = c.src;
    img.alt = c.alt;
    img.loading = 'lazy';
    chip.appendChild(img);
    return chip;
  }

  const rowA = clients.slice(0, 10);
  const rowB = clients.slice(10);

  // Duplicar para scroll infinito continuo
  [...rowA, ...rowA, ...rowA].forEach(c => mq1.appendChild(makeChip(c)));
  [...rowB, ...rowB, ...rowB, ...rowB].forEach(c => mq2.appendChild(makeChip(c)));
}

// Preloader Intro Motion Event
window.addEventListener('load', () => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const introDelay = reduceMotion ? 0 : 1400;
  setTimeout(() => {
    document.body.classList.add('is-loaded');
  }, introDelay);
});

// Inicialización general DOM
document.addEventListener('DOMContentLoaded', () => {
  initClientMarquee();
});

// Barra de progreso de lectura
window.addEventListener('scroll', () => {
  const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
  const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const scrolled = (winScroll / height) * 100;
  document.getElementById('scroll-progress').style.width = scrolled + '%';
});

// Selector de Líneas Funcionales (Tabs)
function switchLinea(index) {
  const tabs = document.querySelectorAll('.tab-btn');
  const fichas = document.querySelectorAll('.linea-ficha');

  tabs.forEach((t, i) => {
    if (i === index) {
      t.classList.add('active');
    } else {
      t.classList.remove('active');
    }
  });

  fichas.forEach((f, i) => {
    if (i === index) {
      f.classList.add('active');
    } else {
      f.classList.remove('active');
    }
  });
}

// Mobile Nav Toggle
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
if (navToggle) {
  navToggle.addEventListener('click', () => {
    if (navMenu.style.display === 'flex') {
      navMenu.style.display = 'none';
    } else {
      navMenu.style.display = 'flex';
      navMenu.style.flexDirection = 'column';
      navMenu.style.position = 'absolute';
      navMenu.style.top = '72px';
      navMenu.style.left = '0';
      navMenu.style.right = '0';
      navMenu.style.background = '#FAFAF8';
      navMenu.style.padding = '20px';
      navMenu.style.borderBottom = '1px solid #D8D8D8';
    }
  });
}

// Scrollspy para menú
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('section');
  const navLinks = document.querySelectorAll('.nav-menu a');
  let current = '';

  sections.forEach(sec => {
    const top = sec.offsetTop - 100;
    if (pageYOffset >= top) {
      current = sec.getAttribute('id');
    }
  });

  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${current}`) {
      link.classList.add('active');
    }
  });
});
</script>
</body>
</html>
'''

with open(r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated index.html successfully with Preloader, Client Marquee, and Field/Office showcases. Size:", len(html_content))
