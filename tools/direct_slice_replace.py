import re

with open('index_v1_original.html', 'r', encoding='utf-8') as f:
    v1 = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    cur = f.read()

# Extract from v1: from <section id="problematica" to </section> of lineas
p_start = v1.find('<section id="problematica"')
# find </section> of lineas: search for <section id="escalamiento" and take everything before it
esc_pos = v1.find('<section id="escalamiento"')
v1_prob_lineas = v1[p_start:esc_pos].strip()

print("v1 section chunk length:", len(v1_prob_lineas))
print("Starts with:", v1_prob_lineas[:60])
print("Ends with:", v1_prob_lineas[-60:])

# Now in cur (index.html): find <section id="problematica" and the start of <section id="escalamiento"
cur_p_start = cur.find('<section id="problematica"')
cur_esc_pos = cur.find('<section id="escalamiento"')

if cur_p_start != -1 and cur_esc_pos != -1:
    new_cur = cur[:cur_p_start] + v1_prob_lineas + '\n\n' + cur[cur_esc_pos:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_cur)
    print("Replaced with exact v1 chunk in index.html successfully!")
else:
    print("Could not find start or end positions:", cur_p_start, cur_esc_pos)
