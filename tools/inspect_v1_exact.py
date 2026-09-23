import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index_v1_original.html', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

# HTML of problematica and lineas
print("=== HTML OF PROBLEMATICA (1369 to 1426) ===")
for i in range(1368, 1427):
    print(lines[i])

print("\n=== HTML OF LINEAS (1427 to 1750) ===")
# Let's find end of lineas
end_lineas = 1428
for i in range(1428, len(lines)):
    if '<section id="escalamiento"' in lines[i]:
        end_lineas = i
        break

print(f"Lineas is from 1427 to {end_lineas}")
for i in range(1427, min(1470, end_lineas)):
    print(lines[i])
