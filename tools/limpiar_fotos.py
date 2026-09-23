"""Limpieza de fotos de oficina GEOTEC para PROPUESTA_CENIT.

Elimina el sello de fecha naranja ("06 08 2026") de la esquina inferior
derecha de las fotos DSC00007 y DSC00025 (5184x3888), redimensiona a
1920 px de ancho y exporta JPEG calidad 82 a assets/.

Uso:
    python tools/limpiar_fotos.py

Dependencias: opencv-python, numpy, Pillow (PIL).
"""
import os
import cv2
import numpy as np

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = r"D:\OneDrive - GEOTEC INGENIERIA LTDA\IMAGEN_CORPORATIVA\01_IDENTIDAD_CORPORATIVA\Oficina\fachadaOficina"
OUT_DIR = os.path.join(BASE, "assets")

JOBS = [
    ("DSC00007.JPG", "oficina_fachada_contrapicado.jpg"),
    ("DSC00025.JPG", "oficina_fachada_calle.jpg"),
]

# Region del sello en coordenadas de la imagen original 5184x3888.
# Se restringe la mascara a esta zona para evitar falsos positivos.
ROI_X0, ROI_Y0 = 3700, 3100


def limpiar(src_path, out_path):
    img = cv2.imread(src_path)
    if img is None:
        raise FileNotFoundError(src_path)
    h, w = img.shape[:2]

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Naranja del sello: hue 5-30, saturacion y valor altos
    mask = cv2.inRange(hsv, (5, 120, 120), (30, 255, 255))
    # Restringir a la esquina inferior derecha
    region = np.zeros_like(mask)
    region[ROI_Y0:h, ROI_X0:w] = 255
    mask = cv2.bitwise_and(mask, region)

    # Dilatar para cubrir bordes/alias de los digitos
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=3)

    px = int(cv2.countNonZero(mask))
    print(f"  pixeles de mascara: {px}")
    if px < 500:
        print("  AVISO: mascara casi vacia, revisar rangos HSV")

    limpio = cv2.inpaint(img, mask, 8, cv2.INPAINT_TELEA)

    # Redimensionar a 1920 de ancho manteniendo proporcion
    escala = 1920 / w
    nuevo = cv2.resize(limpio, (1920, int(h * escala)), interpolation=cv2.INTER_AREA)

    cv2.imwrite(out_path, nuevo, [cv2.IMWRITE_JPEG_QUALITY, 82])
    kb = os.path.getsize(out_path) / 1024
    print(f"  -> {out_path} ({kb:.0f} KB)")


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for src_name, out_name in JOBS:
        print(f"Procesando {src_name}...")
        limpiar(os.path.join(SRC_DIR, src_name), os.path.join(OUT_DIR, out_name))
    print("Listo.")
