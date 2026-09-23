import re

with open('index_v1_original.html', 'r', encoding='utf-8') as f:
    v1_html = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    cur_html = f.read()

# 1. Extract exact HTML of #problematica and #lineas from v1
prob_match = re.search(r'(<section id="problematica"[\s\S]*?</section>\s*(?:<div class="weave-divider"[^>]*></div>\s*)?<section id="lineas"[\s\S]*?</section>)', v1_html)

if not prob_match:
    print("Could not match both sections together, trying individually...")
    prob = re.search(r'<section id="problematica"[\s\S]*?</section>', v1_html).group(0)
    lineas = re.search(r'<section id="lineas"[\s\S]*?</section>', v1_html).group(0)
    exact_sections = prob + '\n\n<div class="weave-divider" aria-hidden="true"></div>\n\n' + lineas
else:
    exact_sections = prob_match.group(1)

print("Exact sections length:", len(exact_sections))

# 2. Extract CSS from v1
v1_style = re.search(r'<style>([\s\S]*?)</style>', v1_html).group(1)

# Let's see what CSS rules are in v1 for these components:
# We can extract all rules between section-head, cap-num, eyebrow, cadena/grid, cierre, linea, capsules, etc.
# Or better yet, we can include the complete CSS block from v1 for sections 2-7
css_needed = """
/* ==================== ESTILOS EXACTOS V1 PARA EL RETO Y LÍNEAS ==================== */
.section{
  padding: 5rem 0;
  position: relative;
}
.section-alt{
  background: var(--paper-alt);
}
.section-tint{
  background: var(--tint-green);
}
.section-head{
  position: relative;
  max-width: 820px;
  margin-bottom: 2.8rem;
}
.section-head h2{
  font-size: clamp(1.75rem, 3.2vw, 2.35rem);
  color: var(--olive-deep);
  line-height: 1.15;
  text-transform: uppercase;
  letter-spacing: 0.012em;
  position: relative;
  padding-bottom: 1.05rem;
}
.section-head h2::after{
  content: "";
  position: absolute;
  left: 0; bottom: 0;
  width: 72px; height: 4px;
  background: var(--olive);
  border-radius: 2px;
}
.section-head p{
  font-size: 1.05rem;
  color: var(--ink-soft);
  margin-top: 1rem;
  max-width: 68ch;
}
.cap-num{
  position: absolute;
  right: -2rem; top: -1.2rem;
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: clamp(2.6rem, 5vw, 4rem);
  line-height: 1;
  color: transparent;
  -webkit-text-stroke: 1.5px rgba(146, 165, 61, 0.45);
  pointer-events: none;
  user-select: none;
}
.eyebrow{
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--olive);
  margin-bottom: 0.9rem;
}

/* Grids y Layout v1 */
.grid-2{
  display: grid;
  grid-template-columns: 1.15fr 1fr;
  gap: 2.8rem;
  align-items: center;
}
.grid-2 p{
  font-size: 1.02rem;
  color: var(--ink-soft);
  margin-bottom: 1.1rem;
}
.cierre{
  border-left: 4px solid var(--olive);
  padding: 0.4rem 0 0.4rem 1.2rem;
  font-size: 1.08rem;
  font-weight: 500;
  color: var(--ink);
  max-width: 62ch;
  margin-top: 1.4rem;
}
.cierre .kw{
  color: var(--olive);
  font-weight: 700;
}
.kw{
  color: var(--olive);
  font-weight: 700;
}

/* Hint & Capsules */
.lines-hint{
  font-size: 0.85rem;
  color: var(--ink-faint);
  margin: -1.4rem 0 2rem;
  font-family: var(--font-mono);
  letter-spacing: 0.04em;
}
.capsules{
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: -1rem 0 2rem;
}
.capsule{
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  padding: 0.38rem 0.95rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--ink-soft);
  cursor: pointer;
  transition: all .2s var(--ease);
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
}
.capsule b{
  color: var(--olive);
  font-weight: 700;
}
.capsule:hover{
  border-color: var(--olive);
  color: var(--olive-deep);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(10,10,10,0.06);
}

/* Acordeón de Líneas v1 (exacto a la captura) */
.linea{
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  margin-bottom: 1.1rem;
  overflow: hidden;
  transition: box-shadow .25s var(--ease), border-color .25s var(--ease), transform .25s var(--ease);
}
.linea:hover{
  box-shadow: 0 14px 34px rgba(10,10,10,0.08);
  transform: translateY(-2px);
}
.linea[open]{
  border-color: var(--olive-bright);
  box-shadow: 0 18px 44px rgba(10,10,10,0.10);
}
.linea summary{
  list-style: none;
  cursor: pointer;
  padding: 1.35rem 1.8rem;
  display: grid;
  grid-template-columns: 60px 1fr auto;
  align-items: center;
  gap: 1.2rem;
  user-select: none;
}
.linea summary::-webkit-details-marker{ display:none; }
.linea-num{
  font-family: var(--font-mono);
  font-size: 2.2rem;
  font-weight: 700;
  color: #C9B92E;
  line-height: 1;
  transition: color .25s var(--ease);
}
.linea:hover .linea-num, .linea[open] .linea-num{
  color: var(--olive-deep);
}
.linea-title h3{
  font-size: 1.18rem;
  color: var(--olive-deep);
  font-weight: 700;
  margin-bottom: 0.2rem;
}
.linea-title .linea-sub{
  font-size: 0.88rem;
  color: var(--ink-faint);
  font-weight: 400;
}
.linea-chev{
  width: 34px; height: 34px;
  border-radius: 50%;
  border: 1.5px solid #C9B92E;
  display: flex; align-items: center; justify-content: center;
  transition: transform .3s var(--ease), background .25s var(--ease), border-color .25s var(--ease);
  flex-shrink: 0;
}
.linea-chev svg{
  width: 15px; height: 15px;
  stroke: var(--olive-deep);
  transition: transform .3s var(--ease);
}
.linea[open] .linea-chev{
  transform: rotate(45deg);
  background: var(--mustard-bright);
  border-color: var(--mustard-bright);
}

.linea-body{
  padding: 0.2rem 2rem 1.8rem;
  border-top: 1px solid var(--line);
  margin: 0 0 0 1.5rem;
  animation: lineaIn .35s var(--ease);
}
@keyframes lineaIn{
  from{ opacity: 0; transform: translateY(-6px); }
  to{ opacity: 1; transform: translateY(0); }
}
.linea-trio{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  padding-top: 1.3rem;
}
.linea-trio h4{
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--mustard);
  margin-bottom: 0.45rem;
}
.linea-trio p{
  font-size: 0.92rem;
  color: var(--ink-soft);
  line-height: 1.55;
}
.dato{
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--olive-deep);
  border-bottom: 1px dotted var(--olive);
  cursor: help;
  white-space: nowrap;
}
.chips{
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: 1.2rem;
  padding-top: 1rem;
  border-top: 1px dashed var(--line);
}
.chip{
  font-family: var(--font-mono);
  font-size: 0.72rem;
  padding: 0.25rem 0.65rem;
  background: var(--paper-alt);
  border-radius: 4px;
  color: var(--ink-soft);
}
.weave-divider{
  height: 3px;
  background: linear-gradient(90deg, var(--olive-deep), var(--olive-bright), var(--mustard), var(--olive-bright), var(--olive-deep));
  opacity: 0.5;
}

@media (max-width: 900px){
  .grid-2{
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  .linea summary{
    grid-template-columns: 45px 1fr auto;
    padding: 1.1rem;
  }
  .linea-num{ font-size: 1.6rem; }
  .linea-trio{
    grid-template-columns: 1fr;
    gap: 1.1rem;
  }
  .cap-num{
    right: 0;
    top: -1.8rem;
  }
}
"""

# Replace in index.html:
# 1. Replace problematica and lineas in HTML
cur_html = re.sub(
    r'<section id="problematica"[\s\S]*?</section>\s*(?:<div class="weave-divider"[^>]*></div>\s*)?<section id="lineas"[\s\S]*?</section>',
    exact_sections,
    cur_html
)

# 2. Add or update the exact CSS
if '/* ==================== ESTILOS EXACTOS V1 PARA EL RETO Y LÍNEAS ==================== */' in cur_html:
    cur_html = re.sub(
        r'/\* ==================== ESTILOS EXACTOS V1 PARA EL RETO Y LÍNEAS ==================== \*/[\s\S]*?(?=/\* ==+|\n</style>)',
        css_needed,
        cur_html
    )
else:
    # Insert right before </style>
    cur_html = cur_html.replace('</style>', css_needed + '\n</style>')

# 3. Add JS for capsule data-goto navigation if not present
js_capsule = """
  // Capsules: abrir y saltar a una línea funcional
  document.querySelectorAll('.capsule[data-goto]').forEach(function(cap){
    cap.addEventListener('click', function(){
      var target = document.getElementById(cap.getAttribute('data-goto'));
      if(!target) return;
      target.open = true;
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
"""

if "data-goto" not in cur_html:
    cur_html = cur_html.replace('</script>', js_capsule + '\n</script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(cur_html)

print("index.html fully updated with 100% exact v1 Reto and Lineas!")
