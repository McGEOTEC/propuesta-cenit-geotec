with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Update hero corner badge image to use the newly extracted transparent star
text = text.replace('assets/isotipo_geotec_blanco.png', 'assets/isotipo_geotec_estrella_transparente.png')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated index.html to use the newly extracted transparent star!")
