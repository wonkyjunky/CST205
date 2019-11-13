import numpy as np
import cv2

img = cv2.imread('monalisa.jpg') 
img_remap = cv2.applyColorMap(img, cv2.COLORMAP_OCEAN)
cv2.imshow("Original", img_remap) 
cv2.waitKey(7000)