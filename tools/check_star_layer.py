import cv2
import numpy as np
from PIL import Image

# Load official star layer
star_layer_path = r'F:\PROYECTOS\EMPRESARIAL\GEOTEC_IMG_CORP\01_IDENTIDAD_CORPORATIVA\FONDOS\capa_estrella_gigante_completa_blanco.png'
star_im = Image.open(star_layer_path).convert('RGBA')
star_arr = np.array(star_im)
print("Star layer shape:", star_arr.shape)

# Find alpha bounding box of the star
alpha = star_arr[:, :, 3]
y_indices, x_indices = np.where(alpha > 10)
print(f"Star bounds: x in [{x_indices.min()}, {x_indices.max()}], y in [{y_indices.min()}, {y_indices.max()}]")
