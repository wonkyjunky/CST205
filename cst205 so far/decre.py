from PIL import Image
im = Image.open('bit.jpg')
def map_BlueandGreen(pixel):
	return (int(pixel[0]), int(pixel[1]*.7), int(pixel[2]*.7))
new_list = map(map_BlueandGreen, im.getdata())
im.putdata(list(new_list))
im.save('new5.jpg')