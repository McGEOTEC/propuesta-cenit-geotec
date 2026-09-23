import cv2
import numpy as np
from PIL import Image

img_path = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\isotipo_geotec_estrella_transparente.png'
im = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

# 1. Top left corner artifact: x in [0, 200], y in [0, 80]
im[0:80, 0:250, 3] = 0

# 2. Bottom right white box artifact: x in [700, 900], y in [760, 840]
im[760:850, 700:900, 3] = 0

# 3. Top border artifact (thin line across top)
im[0:15, 0:450, 3] = 0
im[0:15, 600:700, 3] = 0

pil_im = Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGRA2RGBA))
bbox = pil_im.getbbox()
if bbox:
    pil_im = pil_im.crop(bbox)

out1 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\isotipo_geotec_estrella_transparente.png'
out2 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\logo_geotec_naturaleza_sin_fondo.png'
out3 = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\isotipo_geotec_transparente.png'

pil_im.save(out1, format="PNG")
pil_im.save(out2, format="PNG")
pil_im.save(out3, format="PNG")

print("Pristine final star saved, size:", pil_im.size)
