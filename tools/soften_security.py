# Script to update index.html with the softened and polished security roadmap
import os

with open(r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's replace the section-seguridad content with the enriched and softened version
old_seguridad = '''<!-- ============================================================
     SECCIÓN 6: SEGURIDAD, GOBIERNO & SOBERANÍA DEL DATO
     ============================================================ -->
<section id="seguridad" class="section-seguridad">
  <div class="container">
    <div class="section-header">
      <span class="folio-numero">05 // CONFIANZA Y GOBIERNO</span>
      <h2 class="section-title">Soberanía Total y Rigor Institucional</h2>
      <div class="barra-acento-inferior center"></div>
      <p class="section-subtitle">
        Garantizamos que la información estratégica de CENIT permanezca bajo su absoluto control y dentro de sus estándares de ciberseguridad corporativa.
      </p>
    </div>

    <div class="seguridad-grid">
      <div class="seguridad-main-card">
        <div class="barra-acento-lateral">
          <h3 style="font-family: var(--font-display); font-size: 1.45rem; font-weight: 800; color: var(--verde-noche); text-transform: uppercase;">
            Principios de Arquitectura Segura
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
            <h5>Cifrado de Extremo a Extremo</h5>
            <p>Protocolos TLS 1.3 en tránsito y encriptación AES-256 en reposo para todas las bases de datos y repositorios de evidencias.</p>
          </div>
        </div>
      </div>

      <!-- Sello ISO LL-C Card -->
      <div class="iso-cert-card">
        <img src="assets/sello_iso_llc.png" alt="Sello ISO 9001 · 14001 · 45001 LL-C Certification" class="iso-stamp-img">
        <h4>Certificación Trinorma LL-C</h4>
        <p>
          GEOTEC cuenta con certificación internacional en <strong>ISO 9001</strong> (Calidad), <strong>ISO 14001</strong> (Gestión Ambiental) e <strong>ISO 45001</strong> (Seguridad y Salud en el Trabajo).
        </p>
      </div>
    </div>
  </div>
</section>'''

new_seguridad = '''<!-- ============================================================
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

        <!-- Hoja de Ruta y Madurez Progresiva (Suavizado y Propositivo) -->
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
  </div>
</section>'''

if old_seguridad in html:
    html = html.replace(old_seguridad, new_seguridad)
    with open(r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully replaced security section with softened version.")
else:
    print("Could not find exact string, applying regex or structured replacement.")
