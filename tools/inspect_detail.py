with open('index_v1_original.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the sections in order
import re
sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>', text)
print("Sections found:", sections)

# Inspect navbar
nav_match = re.search(r'<nav[\s\S]*?</nav>', text)
if nav_match:
    print("Nav length:", len(nav_match.group(0)))

# Inspect header
header_match = re.search(r'<header[\s\S]*?</header>', text)
if header_match:
    print("Header length:", len(header_match.group(0)))

# Inspect footer
footer_match = re.search(r'<footer[\s\S]*?</footer>', text)
if footer_match:
    print("Footer length:", len(footer_match.group(0)))

# Inspect script
script_match = re.search(r'<script[\s\S]*?</script>', text)
if script_match:
    print("Script length:", len(script_match.group(0)))
