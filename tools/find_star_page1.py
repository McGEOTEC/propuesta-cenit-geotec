import cv2
import numpy as np
from PIL import Image

# Load page1_highres.png
im = Image.open('page1_highres.png')
print("Page 1 size:", im.size)

# The star is located in the center-right of the cover page
# Let's inspect where it is located
arr = np.array(im)
print("Array shape:", arr.shape)
