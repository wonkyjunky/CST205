from PIL import Image

my_list = []

with open('pixel2','r') as f:
	for x in range(len(f)):
		for y in range(len(f)-2):
			my_list.append = [(x,y), putpixel()]


mona = Image.new('L',(18,29),my_list)
mona.show()