import cv2
import numpy as np
from PIL import Image

# Load the mask extracted image
img_path = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\isotipo_geotec_estrella_transparente.png'
im_rgba = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
h, w, _ = im_rgba.shape

alpha = im_rgba[:, :, 3]

# The text is at x > 650, y > 600, area < 5000 or disconnected
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats((alpha > 20).astype(np.uint8), connectivity=8)

cleaned_alpha = np.zeros_like(alpha)
for i in range(1, num_labels):
    area = stats[i, cv2.CC_STAT_AREA]
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    cw = stats[i, cv2.CC_STAT_WIDTH]
    ch = stats[i, cv2.CC_STAT_HEIGHT]
    
    # Filter out text elements: text is small or located in the text regions
    if area < 2500 and (x > 680 or y > 700 or x < 150):
        continue
    # Keep the blade
    cleaned_alpha[labels == i] = alpha[labels == i]

im_rgba[:, :, 3] = cleaned_alpha

# Also smooth edges slightly
pil_im = Image.fromarray(cv2.cvtColor(im_rgba, cv2.COLOR_BGRA2RGBA))
bbox = pil_im.getbbox()
if bbox:
    pil_im = pil_im.crop(bbox)

out1 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\isotipo_geotec_estrella_transparente.png'
out2 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\logo_geotec_naturaleza_sin_fondo.png'
out3 = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\isotipo_geotec_transparente.png'

pil_im.save(out1, format="PNG")
pil_im.save(out2, format="PNG")
pil_im.save(out3, format="PNG")

print("Cleaned text, new size:", pil_im.size)
