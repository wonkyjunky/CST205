from PIL import Image
im = Image.open('picture.jpg')
width, height = im.size
big_pixel_list = []
for x in range(width):
 for y in range(height):
		big_pixel_list.append(im.getpixel((x,y)))

print(max(big_pixel_list))