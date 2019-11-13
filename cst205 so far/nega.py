from PIL import Image
im = Image.open('negative.jpg')
def negative_image(pixel):
	return tuple(map(lambda a : 255 - a, pixel))
negative_list = map( negative_image, im.getdata() )

im.putdata(list(negative_list))
im.save('nagativeagain.jpg')