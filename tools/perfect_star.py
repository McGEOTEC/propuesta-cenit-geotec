import cv2
import numpy as np
from PIL import Image

img_path = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\isotipo_geotec_estrella_transparente.png'
im_rgba = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

# Erase the area containing 'MÁS ALLÁ PROV'
# In coordinate space: y between 700 and 760, x between 660 and 810
im_rgba[700:780, 650:820, 3] = 0

# Also clean the tiny top-right straight edge border if any (x > 870, y < 100)
im_rgba[0:120, 850:, 3] = 0

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

print("Pristine star saved, size:", pil_im.size)
