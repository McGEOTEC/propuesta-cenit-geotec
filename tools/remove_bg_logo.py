import os
from PIL import Image
import rembg
import numpy as np
import cv2

input_path = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.user_uploaded\media_1790178186312.png'
out_path_1 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\isotipo_geotec_estrella_transparente.png'
out_path_2 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\logo_geotec_naturaleza_sin_fondo.png'
out_path_brain = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\isotipo_geotec_transparente.png'

print("Opening image:", input_path)
inp = Image.open(input_path).convert("RGBA")

# Remove background using rembg
print("Running rembg removal...")
output_im = rembg.remove(inp)

# Convert to numpy array to filter out small text noise if any
arr = np.array(output_im)
alpha = arr[:, :, 3]

# Find connected components in alpha to remove stray text elements
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats((alpha > 30).astype(np.uint8), connectivity=8)

# Keep components with significant area (the star blades are large, text is small)
min_size = 400  # text letters are < 300 px
cleaned_alpha = np.zeros_like(alpha)

for i in range(1, num_labels):
    area = stats[i, cv2.CC_STAT_AREA]
    if area >= min_size:
        cleaned_alpha[labels == i] = alpha[labels == i]

arr[:, :, 3] = cleaned_alpha

# Convert back to image
final_im = Image.fromarray(arr)

# Autocrop transparent borders
bbox = final_im.getbbox()
if bbox:
    final_im = final_im.crop(bbox)

# Save output files
os.makedirs(os.path.dirname(out_path_1), exist_ok=True)
final_im.save(out_path_1, format="PNG")
final_im.save(out_path_2, format="PNG")
final_im.save(out_path_brain, format="PNG")

print(f"Saved successfully!")
print(f"Dimensions: {final_im.size}")
print(f"Output 1: {out_path_1} ({os.path.getsize(out_path_1)} bytes)")
print(f"Output 2: {out_path_2} ({os.path.getsize(out_path_2)} bytes)")
