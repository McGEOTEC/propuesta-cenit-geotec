import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

wa_svg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="#25D366" style="vertical-align: middle; margin-right: 7px; display: inline-block; flex-shrink: 0;"><path d="M12.004 2c-5.523 0-10 4.477-10 10 0 1.767.458 3.428 1.258 4.873L2 22l5.247-1.224A9.957 9.957 0 0012.004 22c5.522 0 10-4.477 10-10s-4.478-10-10-10zm5.823 14.205c-.244.686-1.218 1.309-1.697 1.378-.479.07-1.077.098-3.417-.866-2.736-1.127-4.498-3.901-4.634-4.083-.137-.182-1.108-1.474-1.108-2.812 0-1.338.701-1.996.95-2.26.248-.264.542-.33.722-.33.18 0 .361.002.518.01.168.008.393-.064.615.468.228.547.777 1.895.845 2.034.068.138.114.3.023.48-.091.18-.137.293-.274.453-.137.16-.289.357-.412.48-.137.136-.28.283-.12.557.16.274.712 1.173 1.528 1.9 1.05.936 1.936 1.226 2.211 1.363.275.137.435.114.595-.069.16-.183.687-.799.87-1.073.183-.274.366-.229.617-.137.252.091 1.597.753 1.871.89.274.137.457.206.525.32.069.114.069.663-.175 1.349z"/></svg>'

c = re.sub(
    r'<a href="https://wa\.me/573103430466[^"]*"[^>]*class="footer-btn-primary"[^>]*>[\s\S]*?</a>',
    f'<a href="https://wa.me/573103430466?text=Hola%20GEOTEC%20InnoLab,%20quisiera%20agendar%20una%20sesi%C3%B3n%20t%C3%A9cnica%20sobre%20la%20propuesta%20para%20CENIT%20(Sondeo%20VH-2026-369)." target="_blank" rel="noopener noreferrer" class="footer-btn-primary" style="display:inline-flex;align-items:center;justify-content:center;">{wa_svg}Agendar</a>',
    c
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Footer CTA updated successfully!')
