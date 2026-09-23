import cv2
import numpy as np
from PIL import Image

# Load original uploaded image
img_path = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.user_uploaded\media_1790178186312.png'
im_bgr = cv2.imread(img_path)
h, w, _ = im_bgr.shape

# Let's define the exact geometric contours of the 7 official blades:
mask = np.zeros((h, w), dtype=np.uint8)

# Blade 1: Top-Left vertical blade (Mountains + sky)
# Top rounded tip at (295, 88) to (425, 88), left edge to (185, 415), bottom right at (455, 425), right edge up to (335, 120)
poly1 = np.array([
    [320, 88], [425, 88], [480, 240], [455, 425], [375, 425], [185, 120], [320, 88]
], dtype=np.int32)
# Create a smooth polygon with rounded corners
cv2.fillPoly(mask, [poly1], 255)

# Blade 2: Top-Center vertical blade (Mountain + river)
# Top rounded tip at (455, 2) to (600, 2), down right (595, 360), bottom point (490, 455), left edge up (460, 220)
poly2 = np.array([
    [480, 0], [600, 0], [590, 365], [490, 455], [460, 220], [480, 0]
], dtype=np.int32)
cv2.fillPoly(mask, [poly2], 255)

# Blade 3: Top-Right Upper Bar (Pale green)
poly3 = np.array([
    [705, 18], [945, 0], [945, 125], [745, 172], [705, 18]
], dtype=np.int32)
cv2.fillPoly(mask, [poly3], 255)

# Blade 4: Top-Right Lower Bar (Yellow/Orange gradient)
# Must extend all the way to right edge with clean rounded/angled cap
poly4 = np.array([
    [545, 450], [715, 82], [945, 82], [945, 245], [575, 480], [545, 450]
], dtype=np.int32)
cv2.fillPoly(mask, [poly4], 255)

# Blade 5: Middle-Right angled blade (Road, city, river)
poly5 = np.array([
    [670, 490], [755, 570], [705, 906], [610, 906], [580, 850], [630, 725], [670, 490]
], dtype=np.int32)
cv2.fillPoly(mask, [poly5], 255)

# Blade 6: Bottom-Right pale green badge
poly6 = np.array([
    [775, 625], [860, 715], [820, 820], [755, 785], [775, 625]
], dtype=np.int32)
cv2.fillPoly(mask, [poly6], 255)

# Blade 7: Bottom vertical blade (Green park/trees)
poly7 = np.array([
    [320, 780], [590, 690], [580, 906], [320, 906], [320, 780]
], dtype=np.int32)
cv2.fillPoly(mask, [poly7], 255)

# Blade 8: Middle-Left upper horizontal blade (Green texture)
poly8 = np.array([
    [175, 420], [455, 450], [435, 575], [130, 495], [175, 420]
], dtype=np.int32)
cv2.fillPoly(mask, [poly8], 255)

# Blade 9: Middle-Left lower horizontal blade (Leaf with vein)
poly9 = np.array([
    [10, 545], [475, 500], [575, 545], [375, 725], [10, 615], [10, 545]
], dtype=np.int32)
cv2.fillPoly(mask, [poly9], 255)

# Smooth edges with 3x3 gaussian blur for anti-aliasing
alpha_smooth = cv2.GaussianBlur(mask, (5, 5), 0)

# Build result image
rgba = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2BGRA)
rgba[:, :, 3] = alpha_smooth

result_img = Image.fromarray(cv2.cvtColor(rgba, cv2.COLOR_BGRA2RGBA))
bbox = result_img.getbbox()
if bbox:
    result_img = result_img.crop(bbox)

out1 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\isotipo_geotec_estrella_transparente.png'
out2 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\logo_geotec_naturaleza_sin_fondo.png'
out3 = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\isotipo_geotec_transparente.png'

result_img.save(out1, format="PNG")
result_img.save(out2, format="PNG")
result_img.save(out3, format="PNG")

print("Saved clean star with exact blade polygons, size:", result_img.size)
