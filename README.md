# PROPUESTA_CENIT — Presentación comercial GEOTEC InnoLab

Presentación HTML interactiva de GEOTEC InnoLab para evaluadores técnicos de CENIT, como respaldo del sondeo de mercado **VH-2026-369**, articulada con la identidad corporativa de la plantilla oficial de presentaciones (`GEOTEC_PLANTILLA_BASE_PRESENTACIONES.pptx`) y los conceptos estratégicos del **GEOTEC Corporate Book 2026**.

## Cómo abrir

Abrir `index.html` directamente en cualquier navegador moderno (doble clic). No requiere servidor ni dependencias locales complejas; utiliza tipografías Google Fonts (`Outfit`, `Roboto`, `IBM Plex Mono`) con respaldo de fuentes de sistema.

## Estructura

```
PROPUESTA_CENIT/
├── index.html                            # Versión MIX Maestra (Dinámica + Paleta GEOTEC + Animación + Marquee + Fotos)
├── index_v1_original.html                # Versión Original Base (Presentación Ecopetrol/InnoLab con styles y script)
├── index_v2_editorial.html               # Versión Editorial PPTX (Bloques estructurados tipo diapositiva)
├── styles.css                            # Estilos de soporte para index_v1_original.html
├── script.js                             # Scripts de soporte para index_v1_original.html
├── vendor/                               # Librerías cliente (Leaflet, D3, etc.)
├── assets/
│   ├── geotec_corporate_book_cover.png   # Arte de portada oficial Corporate Book 2026
│   ├── fondo_topografico_portada.png     # Fondo topográfico oficial GEOTEC
│   ├── logo_geotec_color.png             # Logo oficial horizontal a color
│   ├── logo_geotec_blanco.png            # Logo oficial blanco para fondos oscuros
│   ├── innolab_logo.png                  # Logo InnoLab
│   ├── cenit_logo.png                    # Logo CENIT
│   ├── sello_iso_llc.png                 # Certificación Trinorma ISO 9001 · 14001 · 45001 LL-C
│   ├── isotipo_geotec_blanco.png         # Isotipo monocromo blanco
│   ├── textura_patron_blanco.png         # Textura oficial de fondo
│   ├── oficina_fachada_calle.jpg         # Foto sede, vista de calle (carrusel)
│   ├── oficina_fachada_contrapicado.jpg  # Foto sede, contrapicado (carrusel)
│   └── campo_verificacion_humedal.jpg    # Verificación técnica en campo (carrusel)
├── tools/
│   ├── update_index.py                   # Generador / actualizador de la presentación
│   └── verify_presentation.py            # Verificación de integridad de assets y recursos
└── README.md
```

## Sistema de Diseño (Guía Oficial GEOTEC_2024)

- **Paleta de Color Oficial**: Verde GEOTEC `#92A53D`, Amarillo `#FFD005` / Isotipo `#FFD449`, Oliva `#C9B92E`, Naranja `#E37E4B`, Carbón `#53534D`, Negro `#0A0A0A`, Verde Noche `#1E2A24`, Neutros Hueso `#FAFAF8`, Caja Beige `#F0EFE5`, Tinte Verde `#F4F6EC`, Gris Línea `#D8D8D8`.
- **Diagramación en Dos Registros**:
  - **Registro A (Institucional / Técnico)**: Fondos limpios, tarjetas con bordes suaves, barras de subrayado de acento (`barra_titulo_inferior` verde `#92A53D`), folios numéricos (`01`, `02`...) en `IBM Plex Mono`.
  - **Registro B (Comercial / Impacto)**: Bloques en verde noche (`#1E2A24`), titulares de alto impacto en mayúsculas, chips amarillos y texturas translúcidas del isotipo.
- **Conceptos del Corporate Book 2026 Integrados**:
  - *"Ingeniería que convierte complejidad en decisiones confiables"*.
  - **Ciclo de Vida en 4 Ejes**: *01 Viabilizar*, *02 Articular*, *03 Acompañar*, *04 Cerrar & Sostener*.
  - **Las 5 Certezas GEOTEC**: *Técnica*, *Operativa*, *Preventiva*, *Documental*, *Regulatoria*.
  - **Casos de Éxito de Alto Impacto**: Ecopetrol Piedemonte (105 requerimientos cerrados), Offshore Bloques Fuerte Norte/Sur, La Esmeralda (470 puntos de agua), Guamal/Cubarral (2.424 encuentros territoriales), Playón 3D (+800 cargas saneadas) y Frontera Energy (7 años de portafolio continuo).

## Contacto Integrado

- **Email:** comercial@geotecingenieria.com
- **Teléfono:** +57 318 707 0358
- **Dirección:** Cra 15 No. 92-29, oficina 405, Bogotá D.C., Colombia
- **Certificaciones:** ISO 9001 · ISO 14001 · ISO 45001 | LL-C Certification
