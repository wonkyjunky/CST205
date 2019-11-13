"""
NAME: WON KYU JEONG
DATE: 10/5/2019
COURSE: CST 205
Coding Partner: YE LIN JOH
"""


import numpy as np
from PIL import Image

# Load images
im0 = np.array(Image.open('hw2_image/1.png'))
im1 = np.array(Image.open('hw2_image/2.png'))
im2 = np.array(Image.open('hw2_image/3.png'))
im3 = np.array(Image.open('hw2_image/4.png'))
im4 = np.array(Image.open('hw2_image/5.png'))
im5 = np.array(Image.open('hw2_image/6.png'))
im6 = np.array(Image.open('hw2_image/7.png'))
im7 = np.array(Image.open('hw2_image/8.png'))
im8 = np.array(Image.open('hw2_image/9.png'))
im9 = np.array(Image.open('hw2_image/10.png'))
im10 = np.array(Image.open('hw2_image/11.png')) #I opened the image and make it as numpy array and assigned it with im0~11

sequence = np.stack((im0, im1, im2, im3, im4, im5, im6, im7, im8, im9, im10), axis=3) 
#stack the 11 images

result = np.median(sequence, axis=3).astype(np.uint8)
#replace each pixel with meadian values of sequence.

Image.fromarray(result).save('hw2_image/result.png')
#save image