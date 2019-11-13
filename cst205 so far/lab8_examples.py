from PIL import Image
im = Image.open("monalisa.jpg","r")

def effect_spread(self, distance):
    """
    Randomly spread pixels in an image.
    :param distance: Distance to spread pixels.
    """
    self.load()
    return self._new(self.im.effect_spread(distance))


im2 = im.effect_spread(100)

im2.show()
