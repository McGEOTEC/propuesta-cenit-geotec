import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index_v1_original.html', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for idx, l in enumerate(lines):
    if any(k in l for k in ['GESTIÓN AMBIENTAL INTEGRAL', 'CINCO LÍNEAS FUNCIONALES', 'id="problematica"', 'id="lineas"']):
        print(f'{idx+1}: {l}')
