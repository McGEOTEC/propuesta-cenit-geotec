"""Optimizacion de fotos adicionales para PROPUESTA_CENIT (sin limpieza).

Redimensiona y exporta a JPEG las fotos que no requieren inpainting
(p. ej. la foto de verificacion en campo, que no tiene sello de fecha).

Uso:
    python tools/optimizar_foto.py

Dependencias: Pillow (PIL).
"""
import os
from PIL import Image, ImageOps

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE, "assets")

JOBS = [
    # (origen, destino, ancho_objetivo, calidad)
    (
        r"D:\OneDrive - GEOTEC INGENIERIA LTDA\IMAGEN_CORPORATIVA\01_IDENTIDAD_CORPORATIVA\SERVICIOS\Edwin\20260715_081559.jpg",
        "campo_verificacion_humedal.jpg",
        1200,
        76,
    ),
]


def optimizar(src_path, out_name, width, quality):
    img = Image.open(src_path)
    img = ImageOps.exif_transpose(img)  # respeta la orientacion EXIF (p. ej. fotos verticales)
    if img.mode != "RGB":
        img = img.convert("RGB")
    w, h = img.size
    escala = width / w
    img = img.resize((width, int(h * escala)), Image.LANCZOS)
    out_path = os.path.join(OUT_DIR, out_name)
    img.save(out_path, "JPEG", quality=quality, optimize=True, progressive=True)
    kb = os.path.getsize(out_path) / 1024
    print(f"{os.path.basename(src_path)} -> {out_path} ({img.size[0]}x{img.size[1]}, {kb:.0f} KB)")


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for src, out, width, quality in JOBS:
        optimizar(src, out, width, quality)
    print("Listo.")
