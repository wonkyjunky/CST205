from PIL import Image
def copy_smallthings():
 # source image

	small1 = Image.open("small1.jpg")
 # destination image
	canvas = Image.new("RGB", (1920,1080), "white")
	target_x = 500
	for source_x in range(0,small1.width,2):
 		target_y = 500
 	
 		for source_y in range(0,small1.height,2):
 			color = small1.getpixel((source_x, source_y)) # get pixels from the source
 			canvas.putpixel((target_x, target_y), color) # put pixels onto target
 			target_y += 1
 		target_x +=1

	small2 = Image.open("small2.jpg")
	target_x = 0
	for source_x in range(small2.width):
 		target_y = 0
 	
 		for source_y in range(small2.height):
 			color = small2.getpixel((source_x, source_y)) # get pixels from the source
 			canvas.putpixel((target_x, target_y), color) # put pixels onto target
 			target_y += 1
 		target_x +=1

	small3 = Image.open("small3.jpeg")
	target_x = 1000
	for source_x in range(0,small3.width,3):
 		target_y = 900

 		for source_y in range(0,small3.height,2):
 			color = small3.getpixel((source_x, source_y)) # get pixels from the source
 			canvas.putpixel((target_x, target_y), color) # put pixels onto target
 			target_y += 1
 		target_x +=1

 		canvas.save("small1-1.jpg")



copy_smallthings()
