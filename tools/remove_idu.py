with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace IDU mention in the operation card
text = text.replace(
    '<div><strong>✓ IDU</strong> · Catastro Urbano</div>',
    '<div><strong>✓ Ocensa</strong> · Infraestructura y Transporte</div>'
)

# Also check for any other 'IDU' mentions
import re
text = re.sub(r'\bIDU\b', 'Ocensa', text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Removed all IDU mentions from index.html successfully!")
