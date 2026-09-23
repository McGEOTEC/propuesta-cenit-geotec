import cv2
import numpy as np
from PIL import Image

# Load original uploaded image
img_path = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.user_uploaded\media_1790178186312.png'
im_bgr = cv2.imread(img_path)
h, w, _ = im_bgr.shape

# Let's inspect each blade's exact boundaries:
# Each blade has a thin white border / gap in the original artwork, but outside the blade geometry it should be transparent.

# 1. Start with color difference from pure white background
gray = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2HSV)
sat = hsv[:, :, 1]
val = hsv[:, :, 2]

# Standard threshold for colored/textured areas:
# Pixels that have color OR texture OR are inside the sky regions of blade 1 & 2
is_foreground = (sat > 10) | (gray < 232)

# Specific region for Blade 1 top (Mountain & pale sky):
# x: [180, 430], y: [90, 300]
# In this region, include pale sky pixels that are within the blade parallelogram
poly_b1 = np.array([[295, 88], [428, 88], [475, 235], [445, 415], [375, 415], [185, 125]], dtype=np.int32)
mask_b1 = np.zeros((h, w), dtype=np.uint8)
cv2.fillPoly(mask_b1, [poly_b1], 255)

# Specific region for Blade 2 top (River mountain & pale sky):
# x: [460, 600], y: [0, 240]
poly_b2 = np.array([[465, 0], [600, 0], [595, 240], [580, 360], [490, 455], [460, 220]], dtype=np.int32)
mask_b2 = np.zeros((h, w), dtype=np.uint8)
cv2.fillPoly(mask_b2, [poly_b2], 255)

# Specific region for Blade 3 & 4 (Yellow/green gradient bars on top-right):
poly_b3_4 = np.array([[700, 18], [945, 0], [945, 230], [545, 450], [700, 18]], dtype=np.int32)
mask_b3_4 = np.zeros((h, w), dtype=np.uint8)
cv2.fillPoly(mask_b3_4, [poly_b3_4], 255)

# Combine: foreground is (standard colored foreground) OR (inside blade 1/2/3/4 polygons AND not pure white background > 252)
in_allowed_polys = (mask_b1 > 0) | (mask_b2 > 0) | (mask_b3_4 > 0)
is_sky_or_yellow = in_allowed_polys & (gray < 250)

combined_fg = is_foreground | is_sky_or_yellow

# Clean small noise / text using morphological operations and connected components
fg_uint = combined_fg.astype(np.uint8) * 255

# Remove text on the right (MÁS ALLÁ) and text on the left (CONOCIMIENTO SOLUCIONES)
fg_uint[700:800, 650:830] = 0 # MÁS ALLÁ
fg_uint[330:420, 100:280] = 0 # CONOCIMIENTO SOLUCIONES
fg_uint[400:500, 780:940] = 0 # PERSONAS NATURALEZA
fg_uint[870:906, 0:120] = 0   # nfiables

# Find connected components and keep only the large blades
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(fg_uint, connectivity=8)
clean_alpha = np.zeros((h, w), dtype=np.uint8)

for i in range(1, num_labels):
    area = stats[i, cv2.CC_STAT_AREA]
    if area > 1200: # large blade component
        clean_alpha[labels == i] = 255

# Fill internal holes inside the blades (e.g. pale clouds or bright river reflections)
contours, hierarchy = cv2.findContours(clean_alpha, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
filled_alpha = np.zeros((h, w), dtype=np.uint8)
for cnt in contours:
    cv2.drawContours(filled_alpha, [cnt], -1, 255, -1)

# Smooth edges with Gaussian blur for perfect anti-aliasing
smoothed_alpha = cv2.GaussianBlur(filled_alpha, (5, 5), 0)

# Build result
rgba = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2BGRA)
rgba[:, :, 3] = smoothed_alpha

result_img = Image.fromarray(cv2.cvtColor(rgba, cv2.COLOR_BGRA2RGBA))
bbox = result_img.getbbox()
if bbox:
    # 5px padding
    crop_box = (max(0, bbox[0]-5), max(0, bbox[1]-5), min(w, bbox[2]+5), min(h, bbox[3]+5))
    result_img = result_img.crop(crop_box)

out1 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\isotipo_geotec_estrella_transparente.png'
out2 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\logo_geotec_naturaleza_sin_fondo.png'
out3 = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\isotipo_geotec_transparente.png'

result_img.save(out1, format="PNG")
result_img.save(out2, format="PNG")
result_img.save(out3, format="PNG")

print("Saved perfectly refined star, size:", result_img.size)
