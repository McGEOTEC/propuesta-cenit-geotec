import cv2
import numpy as np
from PIL import Image

# 1. Load the original uploaded image media_1790178186312.png
img_path = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.user_uploaded\media_1790178186312.png'
im_orig = Image.open(img_path).convert('RGBA')
orig_arr = np.array(im_orig)
h, w, _ = orig_arr.shape

# Let's inspect the 3 circled areas from the user screenshot:
# Circle 1: Top-Left blade (Mountain/Sky) -> x around 130-330, y around 0-250
# Circle 2: Top-Middle blade (Mountain/Sky) -> x around 420-580, y around 0-260
# Circle 3: Top-Right yellow blade -> x around 700-940, y around 10-180

# In the uploaded image:
# The blade polygons in the uploaded image are clearly defined by their straight edges.
# Let's create the exact filled polygon for all blades:

# We can define the precise boundary polygon of each blade:
# Let's create a polygon mask with smooth antialiased edges:

mask = np.zeros((h, w), dtype=np.uint8)

# Blade 1 (Top-Left): Parallelogram with rounded corners extending to top
# Top edge: y=0, x from 295 to 425. Left edge down to (135, 260) then (250, 480)...
poly_blade1 = np.array([
    [290, 0], [428, 0], [480, 240], [455, 430], [360, 420], [135, 100], [290, 0]
], dtype=np.int32)

# Blade 2 (Top-Center): Parallelogram extending to top
# Top edge: y=0, x from 465 to 600.
poly_blade2 = np.array([
    [462, 0], [600, 0], [600, 240], [585, 360], [490, 455], [460, 220], [462, 0]
], dtype=np.int32)

# Blade 3 (Top-Right Upper - Pale Green):
poly_blade3 = np.array([
    [645, 16], [945, 0], [945, 120], [745, 172], [645, 16]
], dtype=np.int32)

# Blade 4 (Top-Right Lower - Yellow/Gold):
poly_blade4 = np.array([
    [550, 440], [715, 82], [945, 80], [945, 230], [575, 478], [550, 440]
], dtype=np.int32)

# Blade 5 (Middle-Right - Park/Road):
poly_blade5 = np.array([
    [665, 480], [755, 570], [705, 906], [605, 906], [580, 850], [630, 725], [665, 480]
], dtype=np.int32)

# Blade 6 (Bottom-Right Pale Green):
poly_blade6 = np.array([
    [760, 620], [860, 715], [820, 820], [745, 785], [760, 620]
], dtype=np.int32)

# Blade 7 (Bottom Vertical):
poly_blade7 = np.array([
    [320, 780], [590, 690], [580, 906], [320, 906], [320, 780]
], dtype=np.int32)

# Blade 8 (Middle-Left Upper):
poly_blade8 = np.array([
    [175, 420], [455, 450], [435, 575], [130, 495], [175, 420]
], dtype=np.int32)

# Blade 9 (Middle-Left Lower - Leaf):
poly_blade9 = np.array([
    [10, 545], [475, 500], [575, 545], [375, 725], [10, 615], [10, 545]
], dtype=np.int32)

all_polys = [poly_blade1, poly_blade2, poly_blade3, poly_blade4, poly_blade5, poly_blade6, poly_blade7, poly_blade8, poly_blade9]

# Draw all filled polygons on a clean canvas
poly_mask = np.zeros((h, w), dtype=np.uint8)
for p in all_polys:
    cv2.fillPoly(poly_mask, [p], 255)

# For any background outside the star that was white, ensure it's removed.
# But inside the polygons, we KEEP the image pixels completely (including pale sky and yellow gradients)!
gray = cv2.cvtColor(orig_arr[:, :, :3], cv2.COLOR_RGB2GRAY)
is_pure_bg = (gray > 248) & (poly_mask == 0)

final_alpha = np.where(poly_mask > 0, 255, 0).astype(np.uint8)

# Smooth edges with Gaussian blur for antialiasing
final_alpha_smooth = cv2.GaussianBlur(final_alpha, (3, 3), 0)

# Build result
result_arr = orig_arr.copy()
result_arr[:, :, 3] = final_alpha_smooth

result_img = Image.fromarray(result_arr)
bbox = result_img.getbbox()
if bbox:
    result_img = result_img.crop(bbox)

# Save
out_path_1 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\isotipo_geotec_estrella_transparente.png'
out_path_2 = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\logo_geotec_naturaleza_sin_fondo.png'
out_path_3 = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\isotipo_geotec_transparente.png'

result_img.save(out_path_1, format="PNG")
result_img.save(out_path_2, format="PNG")
result_img.save(out_path_3, format="PNG")

print("Generated corrected star, size:", result_img.size)
