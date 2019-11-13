import math
from PIL import Image

# constant
target_green = (0, 255, 11)
color_distance = 100

def distance(color_1, color_2):
 red_diff = math.pow((color_1[0] - color_2[0]), 2)
 green_diff = math.pow((color_1[1] - color_2[1]), 2)
 blue_diff = math.pow((color_1[2] - color_2[2]), 2)
 return math.sqrt(red_diff + green_diff + blue_diff)

def chromakey(background, greenscreen):
    new_image = Image.new("RGB", (background.width,background.height), "black")
    for x in range(background.width):
            for y in range(background.height):
                background_pixel = background.getpixel((x,y))
                new_pixel = background_pixel
                if (y < greenscreen.height and x < greenscreen.width):
                    greenscreen_pixel = greenscreen.getpixel((x,y)) 
                    if distance(greenscreen_pixel, target_green) > color_distance:
                        new_pixel = greenscreen_pixel;
                new_image.putpixel((x,y), new_pixel)
    return new_image

greenscreen = Image.open("markz.jpg")
background = Image.open("facebook.png")


our_new_image = chromakey(background, greenscreen)
our_new_image.save('wonkyu1 .jpg')