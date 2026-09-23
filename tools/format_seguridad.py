import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

clean_seguridad_html = """<!-- ================= 7. CIBERSEGURIDAD Y SOBERANÍA DEL DATO (PRINCIPIOS REALES Y MADUREZ) ================= -->
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
        </div>
      </div>
    </div>
  </div>
</section>"""

content = re.sub(r'<!-- =+ 7\. CIBERSEGURIDAD[\s\S]*?</section>', clean_seguridad_html, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Formatted #seguridad cleanly!")
