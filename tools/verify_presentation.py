import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total img tags: {len(imgs)}")
all_ok = True
for src in sorted(set(imgs)):
    exists = os.path.exists(src)
    status = "OK" if exists else "MISSING"
    if not exists:
        all_ok = False
    size = os.path.getsize(src) if exists else 0
    print(f"  • {src}: {status} ({size} bytes)")

# Check background images in CSS
bg_imgs = re.findall(r'url\(["\']?([^"\'\)]+)["\']?\)', html)
print(f"\nTotal background images: {len(bg_imgs)}")
for src in sorted(set(bg_imgs)):
    if not src.startswith('data:'):
        exists = os.path.exists(src)
        status = "OK" if exists else "MISSING"
        if not exists:
            all_ok = False
        size = os.path.getsize(src) if exists else 0
        print(f"  • {src}: {status} ({size} bytes)")

print("\nAsset Verification Passed:", all_ok)
