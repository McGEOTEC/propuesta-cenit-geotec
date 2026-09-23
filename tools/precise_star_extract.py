import cv2
import numpy as np
from PIL import Image

img_path = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.user_uploaded\media_1790178186312.png'
im_bgr = cv2.imread(img_path)
im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)
h, w, _ = im_bgr.shape

# Convert to grayscale and HSV / Lab
gray = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2LAB)

# Background is essentially near-white/light gray with lightness > 235 and low saturation
# Blades have rich color or distinct structure
sat = hsv[:, :, 1]
val = hsv[:, :, 2]
lightness = lab[:, :, 0]

# Threshold where pixels differ from the off-white background
# Background: L > 238 and sat < 15
is_bg = (lightness > 238) & (sat < 18)

# Foreground is NOT is_bg
fg_mask = (~is_bg).astype(np.uint8) * 255

# Apply morphological operations to smooth edges of the blades
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)
fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

# Find all contours
contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Keep only contours that belong to the blades (area > 800) and ignore tiny text
clean_mask = np.zeros((h, w), dtype=np.uint8)
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 800:
        # Check if it's not a text block: text blocks have high aspect ratio or low fill density
        x, y, cw, ch = cv2.boundingRect(cnt)
        # Avoid text on edges
        if cw < w * 0.95 and ch < h * 0.95:
            cv2.drawContours(clean_mask, [cnt], -1, 255, -1)

# Smooth edges with Gaussian blur on the mask for antialiasing
smoothed_alpha = cv2.GaussianBlur(clean_mask, (5, 5), 0)

# Build RGBA image
rgba = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2BGRA)
rgba[:, :, 3] = smoothed_alpha

# Convert to PIL
result = Image.fromarray(cv2.cvtColor(rgba, cv2.COLOR_BGRA2RGBA))

# Autocrop
bbox = result.getbbox()
if bbox:
    # Add a 10px margin
    crop_box = (max(0, bbox[0]-10), max(0, bbox[1]-10), min(w, bbox[2]+10), min(h, bbox[3]+10))
    result = result.crop(crop_box)

out_path = r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\isotipo_geotec_estrella_transparente.png'
result.save(out_path, format="PNG")
result.save(r'f:\PROYECTOS\EMPRESARIAL\PROPUESTA_CENIT\assets\logo_geotec_naturaleza_sin_fondo.png', format="PNG")

print("Saved mask-based extraction, size:", result.size)
