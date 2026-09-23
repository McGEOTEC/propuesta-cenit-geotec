import re

with open('index_v1_original.html', 'r', encoding='utf-8') as f:
    v1 = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    target = f.read()

# 1. Extract #problematica and #lineas from v1
m_prob = re.search(r'<section[^>]*id="problematica"[^>]*>[\s\S]*?</section>', v1)
m_lineas = re.search(r'<section[^>]*id="lineas"[^>]*>[\s\S]*?</section>', v1)

v1_prob_html = m_prob.group(0)
v1_lineas_html = m_lineas.group(0)

# 2. Extract CSS for problematica, lineas, capsules, line-cards, accordions from v1
# Let's extract from v1 <style>
m_v1_style = re.search(r'<style>([\s\S]*?)</style>', v1)
v1_css = m_v1_style.group(1)

# Extract sections of CSS that belong to problem-grid, capsules, line-cards, etc.
# To be completely safe and rich, let's include the v1 styling rules for these sections
specific_css = '''
/* --- V1 PROBLEMÁTICA & LÍNEAS RICH STYLES --- */
.problem-grid{
  display: grid;
  grid-template-columns: 1.15fr 1fr;
  gap: 2.2rem;
  align-items: start;
}
.problem-copy p{
  margin-bottom: 1.1rem;
  color: var(--texto-secundario, #53534D);
  font-size: 0.96rem;
  line-height: 1.68;
}
.problem-copy .cierre{
  font-family: var(--font-mono);
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--verde-noche, #1E2A24);
  background: var(--caja-beige, #F0EFE5);
  border-left: 4px solid var(--verde-geotec, #92A53D);
  padding: 0.8rem 1.1rem;
  border-radius: 0 var(--radius-sm, 6px) var(--radius-sm, 6px) 0;
  margin-top: 1.4rem;
}
.problem-copy .cierre .kw{ color: var(--verde-geotec, #92A53D); font-weight: 700; }

.lines-hint{
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--texto-suave, #76766E);
  margin-bottom: 0.9rem;
  letter-spacing: 0.04em;
}
.capsules{
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-bottom: 2rem;
}
.capsule{
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  background: var(--blanco, #FFFFFF);
  border: 1px solid var(--gris-linea, #D8D8D8);
  border-radius: 999px;
  padding: 0.45rem 0.95rem;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--verde-noche, #1E2A24);
  text-decoration: none;
  cursor: pointer;
  transition: all 0.2s var(--ease);
}
.capsule b{
  color: var(--verde-geotec, #92A53D);
  font-size: 0.74rem;
}
.capsule:hover{
  border-color: var(--verde-geotec, #92A53D);
  background: var(--verde-tinte, #F4F6EC);
  transform: translateY(-2px);
}

.lines-stack{
  display: flex;
  flex-direction: column;
  gap: 1.4rem;
}
.line-card{
  background: var(--blanco, #FFFFFF);
  border: 1px solid var(--gris-linea, #D8D8D8);
  border-radius: var(--radius-md, 10px);
  overflow: hidden;
  transition: border-color 0.25s var(--ease), box-shadow 0.25s var(--ease);
}
.line-card:hover{
  border-color: var(--verde-geotec, #92A53D);
  box-shadow: var(--shadow-md);
}
.line-summary{
  padding: 1.4rem 1.6rem;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  list-style: none;
  user-select: none;
  gap: 1rem;
}
.line-summary::-webkit-details-marker{ display:none; }
.line-summary-left{
  display: flex;
  align-items: center;
  gap: 1.2rem;
  flex: 1;
}
.line-num{
  font-family: var(--font-mono);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--verde-geotec, #92A53D);
  min-width: 32px;
}
.line-titles h3{
  font-size: 1.18rem;
  font-weight: 700;
  color: var(--negro, #0A0A0A);
  margin-bottom: 0.2rem;
}
.line-titles p{
  font-size: 0.86rem;
  color: var(--texto-suave, #76766E);
}
.line-chevron{
  width: 24px;
  height: 24px;
  transition: transform 0.25s var(--ease);
  color: var(--texto-secundario, #53534D);
  flex-shrink: 0;
}
.line-card[open] .line-chevron{
  transform: rotate(180deg);
  color: var(--verde-geotec, #92A53D);
}
.line-body{
  padding: 0 1.6rem 1.6rem;
  border-top: 1px solid var(--gris-linea, #D8D8D8);
  margin-top: 0.2rem;
  padding-top: 1.2rem;
}
.line-grid{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.4rem;
}
.line-block-title{
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--verde-geotec, #92A53D);
  margin-bottom: 0.45rem;
}
.line-block-p{
  font-size: 0.9rem;
  color: var(--texto-secundario, #53534D);
  line-height: 1.55;
}
.line-evidence-box{
  margin-top: 1.2rem;
  background: var(--caja-beige, #F0EFE5);
  border-left: 3px solid var(--verde-geotec, #92A53D);
  padding: 0.8rem 1.1rem;
  border-radius: 0 var(--radius-sm, 6px) var(--radius-sm, 6px) 0;
  font-size: 0.86rem;
  color: var(--verde-noche, #1E2A24);
}
.line-evidence-box strong{
  font-family: var(--font-mono);
  font-size: 0.74rem;
  text-transform: uppercase;
  color: var(--verde-geotec, #92A53D);
  display: block;
  margin-bottom: 0.2rem;
}
.cap-num{
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--verde-geotec, #92A53D);
  letter-spacing: 0.1em;
  margin-bottom: 0.3rem;
  display: block;
}
@media (max-width: 900px){
  .problem-grid{ grid-template-columns: 1fr; }
  .line-grid{ grid-template-columns: 1fr; }
}
'''

# 3. Replace #problematica and #lineas in target
# Find from <section id="problematica" to </section> of #lineas
pattern = re.compile(r'<section[^>]*id="problematica"[^>]*>[\s\S]*?</section>\s*<section[^>]*id="lineas"[^>]*>[\s\S]*?</section>')
replacement = v1_prob_html + '\n\n' + v1_lineas_html

target = pattern.sub(replacement, target)

# Add CSS before </style>
target = target.replace('</style>', specific_css + '\n</style>')

# Add JS for capsule scroll interaction
js_capsule = '''
// Scroll suave para las cápsulas de líneas de InnoLab
document.querySelectorAll('.capsule').forEach(btn => {
  btn.addEventListener('click', () => {
    const targetId = btn.getAttribute('data-goto');
    const el = document.getElementById(targetId);
    if (el) {
      if (!el.open) el.open = true;
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  });
});
'''

target = target.replace('</script>', js_capsule + '\n</script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(target)

print("Updated index.html with v1 problematica and lineas successfully! Length:", len(target))
