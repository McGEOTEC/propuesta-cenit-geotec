import os

# Complete master builder for index.html (Frankenstein / MIX version)
html_content = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GEOTEC InnoLab — Ecosistema Tecnológico para Gestión Socioambiental | Propuesta CENIT</title>
<meta name="description" content="GEOTEC InnoLab: Ingeniería que convierte complejidad en decisiones confiables. 91 herramientas en producción y +25 años de experiencia aplicados al sondeo de mercado CENIT VH-2026-369.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;0,900;1,300;1,400&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
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
  --font-display: 'Roboto', sans-serif;
  --font-body:    'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono:    'IBM Plex Mono', 'Consolas', monospace;

  /* Dimensiones y Sombras */
  --container-max: 1200px;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --shadow-sm: 0 2px 8px rgba(10, 10, 10, 0.04);
  --shadow-md: 0 8px 24px rgba(10, 10, 10, 0.07);
  --shadow-lg: 0 16px 40px rgba(10, 10, 10, 0.12);
  --ease: cubic-bezier(0.22, 0.61, 0.36, 1);
}

/* Reset y Base */
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
}

body {
  font-family: var(--font-body);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

/* --- PRELOADER (DE V2) --- */
#geotec-preloader {
  position: fixed;
  inset: 0;
  background: var(--hueso);
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
  max-width: 240px;
  height: auto;
  filter: drop-shadow(0 4px 12px rgba(10,10,10,0.06));
}
.preloader-sub {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  color: var(--carbon);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.preloader-bar {
  width: 180px;
  height: 3px;
  background: var(--gris-linea);
  border-radius: 3px;
  overflow: hidden;
}
.preloader-progress {
  width: 100%;
  height: 100%;
  background: var(--verde-geotec);
  transform: translateX(-100%);
  animation: preloaderFill 1.2s ease-in-out forwards;
}
@keyframes preloaderFill {
  0% { transform: translateX(-100%); }
  50% { transform: translateX(-30%); }
  100% { transform: translateX(0); }
}

/* Layout */
.container {
  width: 100%;
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 24px;
}

/* Tipografía de Encabezados con Subrayado PPTX */
h1, h2, h3, h4 {
  font-family: var(--font-display);
  font-weight: 700;
  line-height: 1.2;
  color: var(--negro);
}

.titulo-con-barra {
  position: relative;
  display: inline-block;
  margin-bottom: 20px;
}
.titulo-con-barra::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -6px;
  width: 44px;
  height: 3.5px;
  background: var(--verde-geotec);
  border-radius: 2px;
}
.titulo-con-barra.center::after {
  left: 50%;
  transform: translateX(-50%);
}

.tag-institucional {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--verde-geotec);
  background: var(--verde-tinte);
  padding: 4px 12px;
  border-radius: 999px;
  border: 1px solid rgba(146, 165, 61, 0.3);
  margin-bottom: 12px;
}
.tag-institucional.dark {
  background: rgba(255, 208, 5, 0.12);
  color: var(--amarillo-geotec);
  border-color: rgba(255, 208, 5, 0.3);
}

/* --- BARRA DE MENÚ (DE V1) --- */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(250, 250, 248, 0.94);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--gris-linea);
  padding: 12px 0;
  transition: all 0.3s var(--ease);
}
.nav-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.nav-left {
  display: flex;
  align-items: center;
  gap: 16px;
}
.logo-geotec-nav {
  height: 38px;
  width: auto;
  object-fit: contain;
}
.nav-divider-logo {
  width: 1px;
  height: 24px;
  background: var(--gris-linea);
}
.logo-cenit-nav {
  height: 28px;
  width: auto;
  object-fit: contain;
}
.nav-links {
  display: flex;
  align-items: center;
  gap: 20px;
  list-style: none;
}
.nav-links a {
  text-decoration: none;
  font-family: var(--font-body);
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--texto-secundario);
  transition: color 0.2s var(--ease);
  position: relative;
}
.nav-links a:hover,
.nav-links a.active {
  color: var(--negro);
}
.nav-links a.active::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--verde-geotec);
}
.nav-cta-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--blanco);
  background: var(--verde-noche);
  padding: 8px 16px;
  border-radius: var(--radius-sm);
  text-decoration: none;
  transition: background 0.2s var(--ease), transform 0.2s var(--ease);
}
.nav-cta-btn:hover {
  background: var(--verde-geotec);
  transform: translateY(-1px);
}

/* --- HERO (DIAGRAMACIÓN Y MENSAJE V2, SIN TARJETA PEQUEÑA) --- */
.hero-section {
  position: relative;
  background-color: var(--hueso);
  background-image: url('assets/fondo_topografico_portada.png');
  background-size: cover;
  background-position: center;
  padding: 70px 0 60px;
  border-bottom: 1px solid var(--gris-linea);
  overflow: hidden;
}
.hero-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 36px;
  max-width: 980px;
  margin: 0 auto;
  text-align: center;
}
.hero-header-area {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.hero-title {
  font-size: 2.7rem;
  font-weight: 900;
  letter-spacing: -0.02em;
  color: var(--negro);
  margin-bottom: 18px;
  line-height: 1.15;
}
.hero-title span {
  color: var(--verde-geotec);
  position: relative;
}
.hero-subtitle {
  font-size: 1.12rem;
  color: var(--texto-secundario);
  max-width: 820px;
  margin: 0 auto 30px;
  line-height: 1.6;
}
.hero-cta-group {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 40px;
}
.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-family: var(--font-body);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--negro);
  background: var(--amarillo-geotec);
  padding: 13px 26px;
  border-radius: var(--radius-sm);
  text-decoration: none;
  box-shadow: 0 4px 14px rgba(255, 208, 5, 0.28);
  transition: transform 0.2s var(--ease), box-shadow 0.2s var(--ease);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 208, 5, 0.4);
}
.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-family: var(--font-body);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--negro);
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  padding: 13px 24px;
  border-radius: var(--radius-sm);
  text-decoration: none;
  transition: background 0.2s var(--ease), border-color 0.2s var(--ease);
}
.btn-secondary:hover {
  background: var(--caja-beige);
  border-color: var(--carbon);
}

/* Métricas Hero en Chips (V2) */
.hero-stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  max-width: 900px;
  margin: 0 auto;
}
.stat-card {
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  padding: 20px 16px;
  text-align: center;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s var(--ease), border-color 0.2s var(--ease);
}
.stat-card:hover {
  transform: translateY(-3px);
  border-color: var(--verde-geotec);
  box-shadow: var(--shadow-md);
}
.stat-number {
  font-family: var(--font-mono);
  font-size: 2.1rem;
  font-weight: 700;
  color: var(--verde-geotec);
  line-height: 1;
  margin-bottom: 6px;
}
.stat-label {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--negro);
  margin-bottom: 2px;
}
.stat-subtext {
  font-size: 0.74rem;
  color: var(--texto-suave);
}

/* --- SECCIÓN PROBLEMÁTICA / EL RETO --- */
.section {
  padding: 70px 0;
  border-bottom: 1px solid var(--gris-linea);
}
.section-head {
  max-width: 780px;
  margin-bottom: 36px;
}
.section-desc {
  font-size: 1.05rem;
  color: var(--texto-secundario);
  margin-top: 8px;
}

.reto-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}
.reto-card {
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  padding: 28px;
  box-shadow: var(--shadow-sm);
}
.reto-card.tardio {
  border-left: 4px solid var(--naranja);
}
.reto-card.origen {
  border-left: 4px solid var(--verde-geotec);
  background: var(--verde-tinte);
}
.reto-badge {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 10px;
  display: inline-block;
}
.reto-card.tardio .reto-badge { color: var(--naranja); }
.reto-card.origen .reto-badge { color: var(--verde-geotec); }

.reto-title {
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 10px;
}
.reto-list {
  list-style: none;
  margin-top: 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.reto-list li {
  font-size: 0.88rem;
  color: var(--texto-secundario);
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

/* --- SECCIÓN 5 LÍNEAS FUNCIONALES (ESTILO PPTX REFINADO) --- */
.tabs-container {
  margin-top: 28px;
}
.tabs-nav {
  display: flex;
  gap: 8px;
  border-bottom: 2px solid var(--gris-linea);
  margin-bottom: 24px;
  overflow-x: auto;
}
.tab-btn {
  background: transparent;
  border: none;
  padding: 12px 18px;
  font-family: var(--font-mono);
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--texto-secundario);
  cursor: pointer;
  border-bottom: 3px solid transparent;
  margin-bottom: -2px;
  white-space: nowrap;
  transition: all 0.2s var(--ease);
}
.tab-btn:hover {
  color: var(--negro);
}
.tab-btn.active {
  color: var(--verde-geotec);
  border-bottom-color: var(--verde-geotec);
}
.tab-pane {
  display: none;
}
.tab-pane.active {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 28px;
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  padding: 32px;
  box-shadow: var(--shadow-md);
  animation: fadeIn 0.3s var(--ease) forwards;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.linea-tag {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--verde-geotec);
  text-transform: uppercase;
  margin-bottom: 6px;
}
.linea-title {
  font-size: 1.35rem;
  font-weight: 700;
  margin-bottom: 14px;
}
.linea-desc {
  font-size: 0.94rem;
  color: var(--texto-secundario);
  margin-bottom: 20px;
}
.linea-blocks {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-top: 18px;
}
.block-pill {
  background: var(--caja-beige);
  padding: 14px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--gris-borde-suave);
}
.block-pill-label {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  color: var(--verde-noche);
  text-transform: uppercase;
  margin-bottom: 4px;
}
.block-pill-desc {
  font-size: 0.82rem;
  color: var(--texto-secundario);
}

.linea-metrics-col {
  background: var(--caja-beige);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-sm);
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 18px;
}
.metric-row {
  display: flex;
  align-items: center;
  gap: 14px;
}
.metric-row-num {
  font-family: var(--font-mono);
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--verde-geotec);
  min-width: 65px;
}
.metric-row-text {
  font-size: 0.82rem;
  color: var(--texto-secundario);
}

/* --- SECCIÓN ESCALAMIENTO (DE V2 - TARJETAS CONECTADAS 01-04) --- */
.section-alt {
  background-color: var(--caja-beige);
}
.timeline-connected {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  position: relative;
  margin-top: 40px;
}
.timeline-connected::before {
  content: "";
  position: absolute;
  top: 26px;
  left: 6%;
  right: 6%;
  height: 2px;
  background: repeating-linear-gradient(90deg, var(--verde-geotec) 0 10px, transparent 10px 18px);
  z-index: 1;
}
.tl-card {
  position: relative;
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  padding: 24px 18px 20px;
  z-index: 2;
  box-shadow: var(--shadow-sm);
  transition: transform 0.25s var(--ease), box-shadow 0.25s var(--ease), border-color 0.25s var(--ease);
}
.tl-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
  border-color: var(--verde-geotec);
}
.tl-folio {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 2px solid var(--verde-geotec);
  background: var(--hueso);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--verde-noche);
  margin-bottom: 14px;
  transition: background 0.2s var(--ease), color 0.2s var(--ease);
}
.tl-card:hover .tl-folio {
  background: var(--verde-noche);
  color: var(--amarillo-geotec);
  border-color: var(--amarillo-geotec);
}
.tl-tag {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 999px;
  margin-bottom: 10px;
}
.tl-tag.ok { background: var(--verde-tinte); color: var(--verde-geotec); border: 1px solid rgba(146, 165, 61, 0.4); }
.tl-tag.next { background: var(--caja-beige); color: var(--carbon); border: 1px solid var(--gris-linea); }
.tl-tag.future { background: transparent; color: var(--texto-suave); border: 1px dashed var(--gris-linea); }

.tl-title {
  font-size: 1.05rem;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--negro);
}
.tl-text {
  font-size: 0.84rem;
  color: var(--texto-secundario);
  line-height: 1.45;
  margin-bottom: 12px;
}
.tl-scale {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--texto-suave);
  border-top: 1px solid var(--gris-linea);
  padding-top: 8px;
}

/* --- SECCIÓN CIBERSEGURIDAD Y SOBERANÍA DEL DATO --- */
.sec-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
}
.sec-card-box {
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  padding: 28px;
}
.sec-card-box h3 {
  font-size: 1.15rem;
  margin-bottom: 16px;
  color: var(--negro);
}
.sec-items-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.sec-item {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}
.sec-item-icon {
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--verde-geotec);
  font-size: 0.85rem;
  margin-top: 2px;
}
.sec-item-title {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--negro);
}
.sec-item-desc {
  font-size: 0.82rem;
  color: var(--texto-secundario);
}

/* --- SECCIÓN CAPACIDADES EN OPERACIÓN & FOTO + CARRUSEL --- */
.operacion-hero-card {
  margin-top: 24px;
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 28px;
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  align-items: center;
}
.operacion-img {
  width: 100%;
  height: 100%;
  min-height: 280px;
  object-fit: cover;
}
.operacion-content {
  padding: 28px 32px 28px 8px;
}
.operacion-tag {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--verde-geotec);
  margin-bottom: 8px;
}
.operacion-title {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 10px;
}
.operacion-desc {
  font-size: 0.9rem;
  color: var(--texto-secundario);
  margin-bottom: 16px;
  line-height: 1.5;
}

/* Carrusel Marquee Clientes (De V2) */
.clients-marquee-wrapper {
  margin-top: 40px;
  padding: 24px 0 10px;
  border-top: 1px solid var(--gris-linea);
  overflow: hidden;
  position: relative;
  mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
  -webkit-mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
}
.marquee-title {
  text-align: center;
  font-family: var(--font-mono);
  font-size: 0.76rem;
  font-weight: 700;
  color: var(--carbon);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-bottom: 20px;
}
.marquee-track {
  display: flex;
  gap: 28px;
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
  padding: 10px 20px;
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-sm);
  min-width: 130px;
  height: 58px;
  transition: transform 0.2s var(--ease), border-color 0.2s var(--ease);
}
.marquee-card:hover {
  transform: translateY(-2px);
  border-color: var(--verde-geotec);
}
.marquee-card img {
  max-height: 34px;
  max-width: 100px;
  object-fit: contain;
  filter: grayscale(100%) opacity(0.8);
  transition: filter 0.2s var(--ease);
}
.marquee-card:hover img {
  filter: grayscale(0%) opacity(1);
}
@keyframes scrollMarquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* --- SECCIÓN LÍMITES DECLARADOS (DE V1) --- */
.limit-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin-top: 24px;
}
.limit-card {
  background: var(--blanco);
  border: 1px solid var(--gris-linea);
  border-radius: var(--radius-md);
  padding: 24px;
}
.limit-card.no { border-top: 4px solid var(--naranja); }
.limit-card.si { border-top: 4px solid var(--verde-geotec); background: var(--verde-tinte); }
.limit-badge {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 8px;
}
.limit-card.no .limit-badge { color: var(--naranja); }
.limit-card.si .limit-badge { color: var(--verde-geotec); }
.limit-title { font-size: 1.1rem; font-weight: 700; margin-bottom: 8px; }
.limit-desc { font-size: 0.88rem; color: var(--texto-secundario); line-height: 1.5; }

/* --- CONTACTO / FOOTER FINAL (FUSIÓN FOTO V1 + MENSAJE V2) --- */
.footer-cta {
  position: relative;
  background-color: var(--verde-noche);
  color: var(--texto-inverso);
  padding: 80px 0 60px;
  overflow: hidden;
}
.footer-bg-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.16;
  filter: grayscale(80%);
  pointer-events: none;
}
.footer-texture {
  position: absolute;
  top: -50px;
  right: -50px;
  width: 380px;
  height: 380px;
  opacity: 0.08;
  pointer-events: none;
}
.footer-grid {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 40px;
  align-items: center;
}
.footer-title {
  font-size: 2.2rem;
  font-weight: 900;
  color: var(--blanco);
  margin-bottom: 14px;
  line-height: 1.2;
}
.footer-title span { color: var(--amarillo-geotec); }
.footer-desc {
  font-size: 1rem;
  color: var(--texto-inverso-mut);
  line-height: 1.6;
  margin-bottom: 24px;
}
.footer-card-action {
  background: rgba(38, 52, 44, 0.7);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-md);
  padding: 30px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.footer-btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: var(--amarillo-geotec);
  color: var(--negro);
  font-weight: 700;
  font-size: 0.95rem;
  padding: 14px 24px;
  border-radius: var(--radius-sm);
  text-decoration: none;
  box-shadow: 0 4px 16px rgba(255, 208, 5, 0.25);
  transition: transform 0.2s var(--ease);
}
.footer-btn-primary:hover {
  transform: translateY(-2px);
}
.footer-btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: transparent;
  color: var(--blanco);
  border: 1px solid rgba(255, 255, 255, 0.25);
  font-weight: 700;
  font-size: 0.95rem;
  padding: 13px 24px;
  border-radius: var(--radius-sm);
  text-decoration: none;
  transition: background 0.2s var(--ease);
}
.footer-btn-secondary:hover {
  background: rgba(255, 255, 255, 0.08);
}
.footer-iso-badge {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 10px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.footer-iso-badge img {
  height: 42px;
  width: auto;
  object-fit: contain;
}
.footer-iso-text {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--texto-inverso-mut);
}

.footer-bottom-bar {
  position: relative;
  z-index: 2;
  margin-top: 50px;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.78rem;
  color: var(--texto-inverso-mut);
}

/* Responsividad */
@media (max-width: 900px) {
  .hero-stats-grid, .reto-grid, .tab-pane.active, .timeline-connected, .sec-grid, .operacion-hero-card, .limit-grid, .footer-grid {
    grid-template-columns: 1fr;
  }
  .timeline-connected::before { display: none; }
  .nav-links { display: none; }
}
</style>
</head>
<body>

<!-- ================= 1. PRELOADER / INTRO MOTION (DE V2) ================= -->
<div id="geotec-preloader" aria-hidden="true">
  <div class="preloader-inner">
    <img src="assets/logo_geotec_color.png" alt="GEOTEC InnoLab" class="preloader-logo" width="240" height="auto" onerror="this.src='assets/logo_geotec_horizontal_star.png'">
    <div class="preloader-sub">Ecosistema Tecnológico · Gestión Socioambiental</div>
    <div class="preloader-bar"><div class="preloader-progress"></div></div>
  </div>
</div>

<!-- ================= 2. BARRA DE NAVEGACIÓN (DE V1) ================= -->
<nav class="navbar" id="navbar" aria-label="Navegación principal">
  <div class="container nav-content">
    <div class="nav-left">
      <img src="assets/logo_geotec_color.png" alt="GEOTEC Ingeniería Ltda." class="logo-geotec-nav" onerror="this.src='assets/logo_geotec_horizontal_star.png'">
      <div class="nav-divider-logo"></div>
      <img src="assets/cenit_logo.png" alt="CENIT Transporte y Logística" class="logo-cenit-nav">
    </div>
    <ul class="nav-links">
      <li><a href="#inicio" class="active">Inicio</a></li>
      <li><a href="#problematica">El Reto</a></li>
      <li><a href="#lineas">Líneas</a></li>
      <li><a href="#escalamiento">Escalamiento</a></li>
      <li><a href="#seguridad">Seguridad</a></li>
      <li><a href="#operacion">En Operación</a></li>
      <li><a href="#limitaciones">Límites</a></li>
    </ul>
    <a href="#contacto" class="nav-cta-btn">Agendar Sesión</a>
  </div>
</nav>

<!-- ================= 3. PRIMER ENCUADRE / HERO (DIAGRAMACIÓN Y MENSAJE V2, SIN TARJETA PEQUEÑA) ================= -->
<header id="inicio" class="hero-section">
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
</header>

<!-- ================= 4. PROBLEMÁTICA / EL RETO (ESTILO PPTX REFINADO) ================= -->
<section id="problematica" class="section">
  <div class="container">
    <div class="section-head">
      <span class="tag-institucional">El Reto</span>
      <h2 class="titulo-con-barra">La Gestión Ambiental Integral Exige Control en Cada Fase</h2>
      <p class="section-desc">
        La dispersión de fuentes, la complejidad de las 242 clases ANLA y la intervención manual generan errores que se detectan meses después en radicación. InnoLab traslada el aseguramiento al momento exacto de la captura.
      </p>
    </div>

    <div class="reto-grid">
      <div class="reto-card tardio">
        <span class="reto-badge">Modelo Convencional</span>
        <h3 class="reto-title">Error Tardío y Sobrecostos</h3>
        <p style="font-size:0.88rem; color:var(--texto-secundario);">
          La corrección ocurre al final del ciclo frente a la autoridad ambiental, multiplicando tiempos de radicación y riesgo sancionatorio.
        </p>
        <ul class="reto-list">
          <li>❌ <strong>Retrabajos manuales</strong> en gabinete tras semanas de campo.</li>
          <li>❌ <strong>Inconsistencias topológicas</strong> detectadas en radicación oficial.</li>
          <li>❌ <strong>Riesgo de requerimientos</strong> y demoras en viabilidad operativa.</li>
        </ul>
      </div>

      <div class="reto-card origen">
        <span class="reto-badge">Modelo GEOTEC InnoLab</span>
        <h3 class="reto-title">Control Temprano en Origen</h3>
        <p style="font-size:0.88rem; color:var(--texto-secundario);">
          El dato nace estructurado y validado desde el formulario desconectado en campo y se certifica antes de ingresar a la base central.
        </p>
        <ul class="reto-list">
          <li>✅ <strong>242 clases y 4.799 campos</strong> auditados en tiempo real.</li>
          <li>✅ <strong>Certificado criptográfico SHA-256</strong> por cada entrega.</li>
          <li>✅ <strong>De campo a geodatabase</strong> sin manipulación intermedia.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ================= 5. QUÉ OFRECE INNOLAB / 5 LÍNEAS FUNCIONALES ================= -->
<section id="lineas" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="tag-institucional">Qué Ofrece InnoLab</span>
      <h2 class="titulo-con-barra">Cinco Líneas Funcionales, un Mismo Ciclo del Dato</h2>
      <p class="section-desc">
        Un ecosistema modular donde cada herramienta resuelve un punto crítico de la gestión socioambiental sin fisuras entre etapas.
      </p>
    </div>

    <div class="tabs-container">
      <div class="tabs-nav" role="tablist">
        <button class="tab-btn active" onclick="switchTab(event, 'tab-linea1')">01. Aseguramiento GDB</button>
        <button class="tab-btn" onclick="switchTab(event, 'tab-linea2')">02. Captura Digital Campo</button>
        <button class="tab-btn" onclick="switchTab(event, 'tab-linea3')">03. Servicios de Datos</button>
        <button class="tab-btn" onclick="switchTab(event, 'tab-linea4')">04. Inteligencia Documental</button>
        <button class="tab-btn" onclick="switchTab(event, 'tab-linea5')">05. Gestión de Portafolios</button>
      </div>

      <!-- Tab 1 -->
      <div id="tab-linea1" class="tab-pane active">
        <div>
          <div class="linea-tag">Línea 01 · Aseguramiento y Validación</div>
          <h3 class="linea-title">Certificación Estructural y Topológica de Geodatabases ANLA</h3>
          <p class="linea-desc">Motor automatizado que audita 242 clases de entidad, 4.799 campos y 308 dominios reglamentarios, emitiendo un reporte exhaustivo y certificado de conformidad por entrega.</p>
          <div class="linea-blocks">
            <div class="block-pill">
              <div class="block-pill-label">Qué Hace</div>
              <div class="block-pill-desc">Evalúa estructura, tipos de datos, dominios oficiales, relaciones y consistencia espacial.</div>
            </div>
            <div class="block-pill">
              <div class="block-pill-label">Evidencia</div>
              <div class="block-pill-desc">Certificado digital de conformidad descargable previo a cualquier radicación.</div>
            </div>
          </div>
        </div>
        <div class="linea-metrics-col">
          <div class="metric-row">
            <div class="metric-row-num">242</div>
            <div class="metric-row-text">Clases de entidad ANLA validadas automáticamente</div>
          </div>
          <div class="metric-row">
            <div class="metric-row-num">4.799</div>
            <div class="metric-row-text">Campos verificados en estructura y completitud</div>
          </div>
          <div class="metric-row">
            <div class="metric-row-num">308</div>
            <div class="metric-row-text">Dominios oficiales homologados sin inconsistencias</div>
          </div>
        </div>
      </div>

      <!-- Tab 2 -->
      <div id="tab-linea2" class="tab-pane">
        <div>
          <div class="linea-tag">Línea 02 · Campo Digital</div>
          <h3 class="linea-title">Captura Digital Desconectada con Trazabilidad GNSS</h3>
          <p class="linea-desc">Formularios digitales configurados con validaciones en origen, control de rangos y registro fotográfico con estampa de metadatos espaciales y temporales inalterables.</p>
          <div class="linea-blocks">
            <div class="block-pill">
              <div class="block-pill-label">Qué Hace</div>
              <div class="block-pill-desc">Captura sin conectividad en campo con validación obligatoria de atributos requeridos.</div>
            </div>
            <div class="block-pill">
              <div class="block-pill-label">Evidencia</div>
              <div class="block-pill-desc">Sincronización directa a GDB corporativa sin digitación manual en oficina.</div>
            </div>
          </div>
        </div>
        <div class="linea-metrics-col">
          <div class="metric-row">
            <div class="metric-row-num">100%</div>
            <div class="metric-row-text">Operatividad sin internet en áreas remotas</div>
          </div>
          <div class="metric-row">
            <div class="metric-row-num">0</div>
            <div class="metric-row-text">Retrabajos de redigitación de libretas de campo</div>
          </div>
        </div>
      </div>

      <!-- Tab 3 -->
      <div id="tab-linea3" class="tab-pane">
        <div>
          <div class="linea-tag">Línea 03 · Servicios de Información</div>
          <h3 class="linea-title">Integración Automatizada de Fuentes Oficiales y Geovisores</h3>
          <p class="linea-desc">Conectores automáticos con repositorios públicos y visores interactivos por proyecto para reunir el contexto territorial previo a la salida de brigadas.</p>
          <div class="linea-blocks">
            <div class="block-pill">
              <div class="block-pill-label">Qué Hace</div>
              <div class="block-pill-desc">Descarga y procesa cartografía base, determinantes ambientales y restricciones.</div>
            </div>
            <div class="block-pill">
              <div class="block-pill-label">Evidencia</div>
              <div class="block-pill-desc">Formatos abiertos interoperables con plataformas GIS corporativas de CENIT.</div>
            </div>
          </div>
        </div>
        <div class="linea-metrics-col">
          <div class="metric-row">
            <div class="metric-row-num">1 Click</div>
            <div class="metric-row-text">Carga de capas de determinantes ambientales</div>
          </div>
          <div class="metric-row">
            <div class="metric-row-num">OGC</div>
            <div class="metric-row-text">Estándares abiertos listos para federación institucional</div>
          </div>
        </div>
      </div>

      <!-- Tab 4 -->
      <div id="tab-linea4" class="tab-pane">
        <div>
          <div class="linea-tag">Línea 04 · Inteligencia Artificial</div>
          <h3 class="linea-title">Inteligencia Documental y RAG sobre Infraestructura Local</h3>
          <p class="linea-desc">Consulta en lenguaje natural sobre volúmenes masivos de expedientes, ICAs y obligaciones ambientales, ejecutada en servidores locales dedicados sin transferir información a nubes públicas.</p>
          <div class="linea-blocks">
            <div class="block-pill">
              <div class="block-pill-label">Qué Hace</div>
              <div class="block-pill-desc">Indexa actos administrativos, planes de manejo y reportes de cumplimiento.</div>
            </div>
            <div class="block-pill">
              <div class="block-pill-label">Evidencia</div>
              <div class="block-pill-desc">Cada respuesta incluye cita exacta del párrafo y documento de origen.</div>
            </div>
          </div>
        </div>
        <div class="linea-metrics-col">
          <div class="metric-row">
            <div class="metric-row-num">100%</div>
            <div class="metric-row-text">Privacidad local sin fuga de datos confidenciales</div>
          </div>
          <div class="metric-row">
            <div class="metric-row-num">Citas</div>
            <div class="metric-row-text">Trazabilidad verificable por cada afirmación técnica</div>
          </div>
        </div>
      </div>

      <!-- Tab 5 -->
      <div id="tab-linea5" class="tab-pane">
        <div>
          <div class="linea-tag">Línea 05 · Gobernanza</div>
          <h3 class="linea-title">Gestión y Trazabilidad de Portafolios de Innovación</h3>
          <p class="linea-desc">Tableros de control en vivo para priorización, semaforización y seguimiento de iniciativas tecnológicas y obligaciones en infraestructura lineal.</p>
          <div class="linea-blocks">
            <div class="block-pill">
              <div class="block-pill-label">Qué Hace</div>
              <div class="block-pill-desc">Parametriza criterios de impacto, madurez operativa y estado de avance.</div>
            </div>
            <div class="block-pill">
              <div class="block-pill-label">Evidencia</div>
              <div class="block-pill-desc">160 iniciativas activas gestionadas bajo un mismo panel ejecutivo.</div>
            </div>
          </div>
        </div>
        <div class="linea-metrics-col">
          <div class="metric-row">
            <div class="metric-row-num">160</div>
            <div class="metric-row-text">Iniciativas mapeadas y controladas en portafolio</div>
          </div>
          <div class="metric-row">
            <div class="metric-row-num">KPIs</div>
            <div class="metric-row-text">Semaforización en tiempo real para toma de decisiones</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ================= 6. ESCALAMIENTO MODULAR EN 4 FASES (DE V2 - TARJETAS CONECTADAS 01-04) ================= -->
<section id="escalamiento" class="section">
  <div class="container">
    <div class="section-head">
      <span class="tag-institucional">Cómo Crece</span>
      <h2 class="titulo-con-barra">Escalamiento Modular en Cuatro Fases</h2>
      <p class="section-desc">
        Un esquema de crecimiento sin rediseño: el paso de una fase a la siguiente amplía la capacidad operativa sin invalidar lo procesado previamente.
      </p>
    </div>

    <div class="timeline-connected">
      <!-- 01 -->
      <div class="tl-card">
        <div class="tl-folio">01</div>
        <span class="tl-tag ok">Disponible Hoy</span>
        <h3 class="tl-title">Operación Distribuida</h3>
        <p class="tl-text">Herramientas locales portables, Python Toolboxes, captura desconectada y aseguramiento en origen por brigada.</p>
        <div class="tl-scale">Escala en: Instancias de ejecución y brigadas de campo</div>
      </div>

      <!-- 02 -->
      <div class="tl-card">
        <div class="tl-folio">02</div>
        <span class="tl-tag next">3 – 4 Meses</span>
        <h3 class="tl-title">Operación Centralizada</h3>
        <p class="tl-text">Servidor de sincronización autoalojado, repositorio central de proyectos, respaldo automatizado y control de versiones.</p>
        <div class="tl-scale">Escala en: Usuarios concurrentes y proyectos simultáneos</div>
      </div>

      <!-- 03 -->
      <div class="tl-card">
        <div class="tl-folio">03</div>
        <span class="tl-tag next">4 – 6 Meses</span>
        <h3 class="tl-title">Servicios Consumibles</h3>
        <p class="tl-text">Validación y certificación expuestas como APIs REST internas, integradas a los sistemas corporativos que CENIT designe.</p>
        <div class="tl-scale">Escala en: Conectividad con plataformas corporativas del cliente</div>
      </div>

      <!-- 04 -->
      <div class="tl-card">
        <div class="tl-folio">04</div>
        <span class="tl-tag future">2027</span>
        <h3 class="tl-title">Gobierno y Terceros</h3>
        <p class="tl-text">Portal de entrega para contratistas, habilitación certificada, federación institucional y estándares abiertos.</p>
        <div class="tl-scale">Escala en: Ecosistema integral de proveedores y aliados</div>
      </div>
    </div>
  </div>
</section>

<!-- ================= 7. CIBERSEGURIDAD Y SOBERANÍA DEL DATO (PRINCIPIOS REALES Y MADUREZ) ================= -->
<section id="seguridad" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="tag-institucional">Confianza y Gobernanza</span>
      <h2 class="titulo-con-barra">Minimización de Exposición y Soberanía del Dato</h2>
      <p class="section-desc">
        Principios técnicos reales implementados hoy para garantizar la estricta confidencialidad de la información corporativa de CENIT.
      </p>
    </div>

    <div class="sec-grid">
      <div class="sec-card-box">
        <h3>Controles y Principios en Operación Actual</h3>
        <div class="sec-items-list">
          <div class="sec-item">
            <span class="sec-item-icon">✓</span>
            <div>
              <div class="sec-item-title">Procesamiento en Infraestructura Local</div>
              <div class="sec-item-desc">Servidores dedicados en Bogotá D.C. sin depender de microservicios externos.</div>
            </div>
          </div>
          <div class="sec-item">
            <span class="sec-item-icon">✓</span>
            <div>
              <div class="sec-item-title">Sin Transferencia a IA en Nube Pública</div>
              <div class="sec-item-desc">Los modelos de lenguaje operan dentro del perímetro seguro sin enviar tokens a terceros.</div>
            </div>
          </div>
          <div class="sec-item">
            <span class="sec-item-icon">✓</span>
            <div>
              <div class="sec-item-title">Integridad Criptográfica SHA-256</div>
              <div class="sec-item-desc">Huella digital por cada archivo de entrega para garantizar no repudio y trazabilidad.</div>
            </div>
          </div>
          <div class="sec-item">
            <span class="sec-item-icon">✓</span>
            <div>
              <div class="sec-item-title">Cumplimiento Ley 1581 de 2012</div>
              <div class="sec-item-desc">Políticas estrictas de protección de datos personales en consultas y cartografía predial.</div>
            </div>
          </div>
        </div>
      </div>

      <div class="sec-card-box">
        <h3>Hoja de Ruta y Madurez Progresiva</h3>
        <div class="sec-items-list">
          <div class="sec-item">
            <span class="sec-item-icon">→</span>
            <div>
              <div class="sec-item-title">Delegación de Autenticación al Active Directory / SSO de CENIT</div>
              <div class="sec-item-desc">La gestión de identidades y accesos se apoya en los mecanismos y políticas corporativas del cliente.</div>
            </div>
          </div>
          <div class="sec-item">
            <span class="sec-item-icon">→</span>
            <div>
              <div class="sec-item-title">Cifrado de Capas en Reposo y Tránsito</div>
              <div class="sec-item-desc">Cifrado AES-256 en almacenamiento local y protocolos TLS 1.3 en sincronización.</div>
            </div>
          </div>
          <div class="sec-item">
            <span class="sec-item-icon">→</span>
            <div>
              <div class="sec-item-title">Proyección de Certificación ISO 27001 / SOC 2</div>
              <div class="sec-item-desc">Horizonte de maduración formal de 12 a 18 meses para auditoría de seguridad de la información.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ================= 8. EN OPERACIÓN & FOTO + CARRUSEL CLIENTES (DE V2) ================= -->
<section id="operacion" class="section">
  <div class="container">
    <div class="section-head">
      <span class="tag-institucional">Demostrado</span>
      <h2 class="titulo-con-barra">Capacidades que ya Operan en Proyectos Reales</h2>
      <p class="section-desc">
        Herramientas probadas en contratos exigentes con los principales operadores del sector energético e institucional.
      </p>
    </div>

    <!-- Tarjeta con Foto Real de Campo -->
    <div class="operacion-hero-card">
      <img src="assets/campo_verificacion_humedal.jpg" alt="Especialistas de GEOTEC en verificación de campo en humedales" class="operacion-img">
      <div class="operacion-content">
        <span class="operacion-tag">Operación en Terreno</span>
        <h3 class="operacion-title">Captura Digital de Campo y Validación GNSS</h3>
        <p class="operacion-desc">
          Especialistas de GEOTEC ejecutando levantamiento socioambiental con formularios desconectados, control de variables bióticas y georreferenciación estricta en ecosistemas estratégicos.
        </p>
        <div style="display:flex; gap:16px; font-family:var(--font-mono); font-size:0.82rem; color:var(--verde-noche);">
          <div><strong>✓ Ecopetrol</strong> · Estudios Ambientales</div>
          <div><strong>✓ Frontera Energy</strong> · Gestión Predial</div>
          <div><strong>✓ IDU</strong> · Catastro Urbano</div>
        </div>
      </div>
    </div>

    <!-- Carrusel Continuo de Clientes (Marquee) -->
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
        <!-- Loop duplicate -->
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
  </div>
</section>

<!-- ================= 9. LÍMITES DECLARADOS (DE V1) ================= -->
<section id="limitaciones" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="tag-institucional">Lo que está en desarrollo</span>
      <h2 class="titulo-con-barra">Límites Declarados, con Horizonte de Resolución</h2>
      <p class="section-desc">
        Una evaluación técnica seria requiere transparencia sobre el alcance actual y las rutas de integración corporativa.
      </p>
    </div>

    <div class="limit-grid">
      <div class="limit-card no">
        <span class="limit-badge">Alcance Actual</span>
        <h3 class="limit-title">Hoy no opera como plataforma web multiusuario de alta concurrencia</h3>
        <p class="limit-desc">
          Opera como conjunto de aplicaciones portables, módulos de automatización e infraestructura local. El acceso web centralizado corresponde a la Fase 2–3 del plan de escalamiento.
        </p>
      </div>

      <div class="limit-card si">
        <span class="limit-badge">Capacidad de Integración</span>
        <h3 class="limit-title">Sí se integra con la plataforma corporativa del cliente</h3>
        <p class="limit-desc">
          Las herramientas pueden exponerse como servicios consumibles desde la infraestructura GIS y los repositorios documentales que CENIT tenga en operación.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- ================= 10. CONTACTO / FOOTER FINAL (FUSIÓN FOTO V1 + MENSAJE V2) ================= -->
<footer id="contacto" class="footer-cta">
  <!-- Foto de fondo de GEOTEC (De V1) -->
  <img src="assets/oficina_fachada_contrapicado.jpg" alt="" class="footer-bg-img" aria-hidden="true">
  <img src="assets/texture_isotipo.png" alt="" class="footer-texture" aria-hidden="true">

  <div class="container footer-grid">
    <!-- Mensaje y contenido (De V2) -->
    <div>
      <span class="tag-institucional dark">Siguiente Paso</span>
      <h2 class="footer-title">
        Listos para Acompañar a <span>CENIT</span> desde el Primer Día
      </h2>
      <p class="footer-desc">
        Ponemos a disposición de los evaluadores técnicos de CENIT nuestro equipo directivo y especialistas en GIS para realizar una sesión técnica de demostración en vivo de las 91 herramientas de InnoLab.
      </p>
      
      <!-- Sello ISO Trinorma (De V2) -->
      <div class="footer-iso-badge">
        <img src="assets/sello_iso_llc.png" alt="Certificación ISO 9001 · 14001 · 45001 LL-C">
        <div class="footer-iso-text">
          Sistema Integrado de Gestión Certificado<br>
          ISO 9001:2015 · ISO 14001:2015 · ISO 45001:2018
        </div>
      </div>
    </div>

    <!-- Botones de Acción -->
    <div class="footer-card-action">
      <a href="mailto:contacto@geotec.com.co?subject=Demostracion%20Tecnica%20GEOTEC%20InnoLab%20-%20CENIT%20VH-2026-369" class="footer-btn-primary">
        Agendar Sesión Técnica
      </a>
      <a href="#" class="footer-btn-secondary" title="[PLACEHOLDER_PDF_CAPACIDADES] Fichas técnicas descargables">
        Descargar Fichas de Capacidades
      </a>
      <div style="font-size: 0.8rem; color: var(--texto-inverso-mut); text-align: center; margin-top: 4px;">
        Bogotá D.C., Colombia · contacto@geotec.com.co
      </div>
    </div>
  </div>

  <div class="container footer-bottom-bar">
    <div>GEOTEC Ingeniería Ltda. · Laboratorio de Innovación InnoLab © 2026</div>
    <div>Sondeo de Mercado CENIT VH-2026-369</div>
  </div>
</footer>

<script>
// Descarte de Preloader al cargar
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    const preloader = document.getElementById('geotec-preloader');
    if (preloader) {
      preloader.classList.add('is-loaded');
    }
  }, 800);
});

// Interactividad de Tabs en 5 Líneas
function switchTab(e, tabId) {
  const navButtons = document.querySelectorAll('.tab-btn');
  const panes = document.querySelectorAll('.tab-pane');

  navButtons.forEach(btn => btn.classList.remove('active'));
  panes.forEach(pane => pane.classList.remove('active'));

  e.currentTarget.classList.add('active');
  const target = document.getElementById(tabId);
  if (target) {
    target.classList.add('active');
  }
}
</script>

</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Master Frankenstein/MIX index.html built successfully! Size:", len(html_content), "lines:", len(html_content.splitlines()))
