from PIL import Image
im = Image.open('monalisa.jpg')
def negative_image(pixel):
 return tuple(map(lambda a : 255 - a, pixel))
negative_list = map( negative_image, im.getdata() )
"""
or with list comprehension,
neg_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
"""
im.putdata(list(negative_list))
im.save('negative.jpg')