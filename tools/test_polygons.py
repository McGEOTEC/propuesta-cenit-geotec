import cv2
import numpy as np
from PIL import Image

img_path = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.user_uploaded\media_1790178186312.png'
im_bgr = cv2.imread(img_path)
h, w, _ = im_bgr.shape

# Let's inspect each blade's coordinates and bounding box
# We can define the precise polygon for each blade of the GEOTEC star:

# Blade 1: Top left vertical blade (Mountains + sky + foliage)
# Coordinates in the 945x906 image:
# Extends from top y=0 down to center y~420
# Left side x~180-280, right side x~330-450

# Let's use grabcut or precise geometric bounding polygons:
# Let's define the 9 main blade polygons:

polygons = [
    # 1. Top-Left vertical blade (Mountains, sky at top, foliage below)
    np.array([[298, 0], [425, 0], [510, 260], [455, 425], [360, 425], [185, 105], [298, 0]], dtype=np.int32),
    
    # 2. Top-Center vertical blade (Sky at top, river & mountain)
    np.array([[465, 0], [600, 0], [600, 240], [580, 365], [490, 455], [465, 230], [465, 0]], dtype=np.int32),
    
    # 3. Top-Right upper bar (Pale green gradient)
    np.array([[700, 15], [945, 15], [945, 80], [705, 160], [700, 15]], dtype=np.int32),
    
    # 4. Top-Right lower bar (Yellow/orange gradient)
    np.array([[715, 85], [945, 85], [945, 195], [680, 265], [670, 320], [525, 470], [525, 435], [715, 85]], dtype=np.int32),
    
    # 5. Middle-Right angled blade (Road, amphitheater, river, park)
    np.array([[675, 490], [755, 570], [700, 906], [610, 906], [585, 850], [630, 725], [675, 490]], dtype=np.int32),
    
    # 6. Bottom-Right pale green badge
    np.array([[750, 615], [860, 715], [830, 815], [745, 785], [750, 615]], dtype=np.int32),
    
    # 7. Bottom vertical blade (Green park/fields)
    np.array([[325, 770], [590, 700], [580, 906], [325, 906], [325, 770]], dtype=np.int32),
    
    # 8. Middle-Left upper horizontal blade (Green texture)
    np.array([[180, 425], [445, 455], [425, 570], [140, 500], [180, 425]], dtype=np.int32),
    
    # 9. Middle-Left lower horizontal blade (Leaf with prominent vein)
    np.array([[12, 545], [475, 505], [575, 545], [375, 715], [12, 610], [12, 545]], dtype=np.int32),
]

mask = np.zeros((h, w), dtype=np.uint8)
for poly in polygons:
    cv2.fillPoly(mask, [poly], 255)

# Now, within each polygon, let's refine the edges:
# Outside the polygons: 100% transparent.
# Inside the polygons: Keep the image pixels, only remove background if near the outer edge and pure white (>250)
cv2.imwrite('debug_polygons.png', mask)
print("Debug mask written")
