with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="seguridad"' in line or 'seguridad-main-card' in line:
        print(f"Found on line {i+1}")
        for j in range(max(0, i-5), min(len(lines), i+60)):
            print(f"{j+1}: {lines[j]}", end="")
        break
