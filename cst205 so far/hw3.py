"""
name: WON KYU JEONG
PARTNER: YE LIN JOH
DATE: 10/13/2019
COURSE: CST205
"""



import sys
from PIL import Image, ImageOps
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QComboBox, QVBoxLayout
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap


im1= Image.open('images/34694102243_3370955cf9_z.jpg','r')
im2= Image.open('images/37198655640_b64940bd52_z.jpg','r')
im3= Image.open('images/36909037971_884bd535b1_z.jpg','r')
im4= Image.open('images/36604481574_c9f5817172_z.jpg','r')
im5= Image.open('images/36885467710_124f3d1e5d_z.jpg','r')
im6= Image.open('images/37246779151_f26641d17f_z.jpg','r')
im7= Image.open('images/36523127054_763afc5ed0_z.jpg','r')
im8= Image.open('images/35889114281_85553fed76_z.jpg','r')
im9= Image.open('images/34944112220_de5c2684e7_z.jpg','r')
im10= Image.open('images/36140096743_df8ef41874_z.jpg','r')
#open image and assign them with variables.



image_info = [
     {
           "id" : "34694102243_3370955cf9_z",
           "title" : "Eastern",
           "flickr_user" : "Sean Davis",
           "tags" : ["Los Angeles", "California", "building"]
      },
      {
           "id" : "37198655640_b64940bd52_z",
           "title" : "Spreetunnel",
           "flickr_user" : "Jens-Olaf Walter",
           "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
      },
      {
           "id" : "36909037971_884bd535b1_z",
           "title" : "East Side Gallery",
           "flickr_user" : "Pieter van der Velden",
           "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
      },
      {
           "id" : "36604481574_c9f5817172_z",
           "title" : "Lombardia, september 2017",
           "flickr_user" : "Mónica Pinheiro",
           "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
      },
      {
           "id" : "36885467710_124f3d1e5d_z",
           "title" : "Palazzo Madama",
           "flickr_user" : "Kevin Kimtis",
           "tags" : [ "Rome", "Italy", "window", "road", "building"]
      },
      {
           "id" : "37246779151_f26641d17f_z",
           "title" : "Rijksmuseum library",
           "flickr_user" : "John Keogh",
           "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
      },
      {
           "id" : "36523127054_763afc5ed0_z",
           "title" : "Canoeing in Amsterdam",
           "flickr_user" : "bdodane",
           "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
      },
      {
           "id" : "35889114281_85553fed76_z",
           "title" : "Quiet at dawn, Cabo San Lucas",
           "flickr_user" : "Erin Johnson",
           "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
      },
      {
           "id" : "34944112220_de5c2684e7_z",
           "title" : "View from our rental",
           "flickr_user" : "Doug Finney",
           "tags" : ["Mexico", "ocean", "beach", "palm"]
      },
      {
           "id" : "36140096743_df8ef41874_z",
           "title" : "Someday",
           "flickr_user" : "Thomas Hawk",
           "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
      }
]


manipulation = ['select option', 'sepia', 'negative', 'grayscale', 'thumbnail', 'none']
# to make combobox i need to put filter keys in list


# To open new windows
class Window2(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Image")

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget) 

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Image Search Engine")  # set window titile 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Image: ')
        self.line = QLineEdit(self) # QLineEdit to user to input text.

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20) #set size and location of QLineEdit

        self.pycombobox = QComboBox(centralWidget)
        self.pycombobox.addItems(manipulation)
        self.pycombobox.setGeometry(QRect(40, 40, 120, 31))
        self.pycombobox.setObjectName(("comboBox"))
        self.pycombobox.move(120,100)
        self.pycombobox.currentIndexChanged.connect(self.update_ui1) #put combobox and set size and location with item


       #	pycombobox.currentIndexChanged.connect(self.update_ui)

        pybutton = QPushButton('search', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)       # set button and connect with function. set size and location
        
        self.a = '' # To determine filter i used variable a.

        #to count how many words matches.
        self.a_none1 = 0
        self.a_none2 = 0
        self.a_none3 = 0
        self.a_none4 = 0
        self.a_none5 = 0
        self.a_none6 = 0
        self.a_none7 = 0
        self.a_none8 = 0
        self.a_none9 = 0
        self.a_none10 = 0
    #def sepia(image):

    def update_ui1(self):
    	my_text = self.pycombobox.currentText()
    	my_index = self.pycombobox.currentIndex()
    	if my_text == 'none':
    		self.a = 'none'
    	if my_text == 'sepia':
    		self.a = 'sepia'
    	if my_text == 'negative':
    		self.a = 'negative'
    	if my_text == 'grayscale':
    		self.a = 'grayscale'	
    	if my_text == 'thumbnail':
    		self.a = 'thumbnail'          #to make difference between color filters. make change of a values.


    def clickMethod(self):
      def thumbnail(img):
        (width, height) = (img.width // 2, img.height // 2)
        img_resized = img.resize((width, height))

        img_resized.save('thumbnail.jpg')
      def grayscale(img):
        width, height = img.size
        grayscale_image = img.copy()

        grayscale_image = ImageOps.grayscale(img) 

        grayscale_image.save('grayscale.jpg')
      def negative(img):
        width, height = img.size
        inverted_image = img.copy()

        inverted_image = ImageOps.invert(img)

        inverted_image.save('negative.jpg')
      def sepia(img):
        width, height = img.size
        new_img = img.copy()

        for x in range(width):
          for y in range(height):
            red, green, blue = img.getpixel((x,y))
            new_val = (0.3 * red + 0.59 * green + 0.11 * blue)

            new_red = int(new_val * 2)
            if new_red > 255:
                new_red = 255
            new_green = int(new_val * 1.5)
            if new_green > 255:
                new_green = 255
            new_blue = int(new_val)
            if new_blue > 255:
                new_blue = 255

            new_img.putpixel((x,y), (new_red, new_green, new_blue))
        new_img.save('sepia.jpg')
        
      def clear(self):
        self.a_none1 = 0
        self.a_none2 = 0
        self.a_none3 = 0
        self.a_none4 = 0
        self.a_none5 = 0
        self.a_none6 = 0
        self.a_none7 = 0
        self.a_none8 = 0
        self.a_none9 = 0
        self.a_none10 = 0

      count = []

      tag_1 = self.line.text().split()
      for x in tag_1:
        if (self.a == 'none' and (x== "Eastern" or x == "California" or x== "building")):
          self.a_none1= self.a_none1 + 1
        if (self.a == 'none' and (x== "Spreetunnel" or x == "Berlin" or x == "Germany" or x== "tunnel" or x == "ceiling")):
          self.a_none2 = self.a_none2 + 1
        if (self.a == 'none' and (x== "Eastern" or x == "Berlin" or x== "Eastern" or x== "wall" or x == "mosaic" or x == "sky" or x == "clouds")):
          self.a_none3= self.a_none3 + 1
        if (self.a == 'none' and (x == "Italy" or x == "Lombardia" or x == "alley" or x == "building" or x == "wall")):
          self.a_none4= self.a_none4 + 1
        if (self.a == 'none' and (x == "Rome" or x == "Italy" or x == "window" or x == "road" or x == "building")):
          self.a_none5= self.a_none5 + 1
        if (self.a == 'none' and (x == "Amsterdam" or x == "Netherlands" or x == "book" or x == "library" or x == "museum")):
          self.a_none6= self.a_none6 + 1
        if (self.a == 'none' and (x == "Amsterdam" or x == "Netherlands" or x == "canal" or x == "boat")):
          self.a_none7= self.a_none7 + 1
        if (self.a == 'none' and (x == "Mexico" or x == "Cabo" or x == "beach" or x == "cactus" or x == "sunrise")):
          self.a_none8= self.a_none8 + 1
        if (self.a == 'none' and (x == "Mexico" or x == "ocean" or x == "beach" or x == "palm")):
          self.a_none9= self.a_none9 + 1
        if (self.a == 'none' and (x == "Hollywood" or x == "California" or x == "Volkswagen" or x == "Beatle" or x == "car")):
          self.a_none10= self.a_none10 + 1
        if (self.a == 'none' and (x =="Los" or x== "Angeles")):
          self.a_none1= self.a_none1 + 0.5
          self.a_none10= self.a_none10 +0.5

        count = [self.a_none1,self.a_none2,self.a_none3,self.a_none4,self.a_none5,self.a_none6,self.a_none7,self.a_none8,self.a_none9,self.a_none10]
      if self.a == 'none':
        if self.a_none7 == max(count):
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('images/36523127054_763afc5ed0_z.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none1 == max(count):
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('images/34694102243_3370955cf9_z.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none3 == max(count):
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('images/36909037971_884bd535b1_z.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none4 == max(count):
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('images/36604481574_c9f5817172_z.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none5 == max(count):
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('images/36885467710_124f3d1e5d_z.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none8 == max(count):
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('images/35889114281_85553fed76_z.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none6 == max(count):
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('images/37246779151_f26641d17f_z.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none10 == max(count):
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('images/36140096743_df8ef41874_z.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none2 == max(count):
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('images/37198655640_b64940bd52_z.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none9 == max(count):
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('images/34944112220_de5c2684e7_z.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)

        count = []

      for x in tag_1:
        if (self.a == 'negative' and (x== "Eastern" or x == "California" or x== "building")):
          self.a_none1= self.a_none1 + 1
        if (self.a == 'negative' and (x== "Spreetunnel" or x == "Berlin" or x == "Germany" or x== "tunnel" or x == "ceiling")):
          self.a_none2 = self.a_none2 + 1
        if (self.a == 'negative' and (x== "Eastern" or x == "Berlin" or x== "Eastern" or x== "wall" or x == "mosaic" or x == "sky" or x == "clouds")):
          self.a_none3= self.a_none3 + 1
        if (self.a == 'negative' and (x == "Italy" or x == "Lombardia" or x == "alley" or x == "building" or x == "wall")):
          self.a_none4= self.a_none4 + 1
        if (self.a == 'negative' and (x == "Rome" or x == "Italy" or x == "window" or x == "road" or x == "building")):
          self.a_none5= self.a_none5 + 1
        if (self.a == 'negative' and (x == "Amsterdam" or x == "Netherlands" or x == "book" or x == "library" or x == "museum")):
          self.a_none6= self.a_none6 + 1
        if (self.a == 'negative' and (x == "Amsterdam" or x == "Netherlands" or x == "canal" or x == "boat")):
          self.a_none7= self.a_none7 + 1
        if (self.a == 'negative' and (x == "Mexico" or x == "Cabo" or x == "beach" or x == "cactus" or x == "sunrise")):
          self.a_none8= self.a_none8 + 1
        if (self.a == 'negative' and (x == "Mexico" or x == "ocean" or x == "beach" or x == "palm")):
          self.a_none9= self.a_none9 + 1
        if (self.a == 'negative' and (x == "Hollywood" or x == "California" or x == "Volkswagen" or x == "Beatle" or x == "car")):
          self.a_none10= self.a_none10 + 1
        if (self.a == 'negative' and (x =="Los" or x== "Angeles")):
          self.a_none1= self.a_none1 + 0.5
          self.a_none10= self.a_none10 +0.5

        count = [self.a_none1,self.a_none2,self.a_none3,self.a_none4,self.a_none5,self.a_none6,self.a_none7,self.a_none8,self.a_none9,self.a_none10]

      if self.a == 'negative':  
        if self.a_none7 == max(count):
          negative(im7)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('negative.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none1 == max(count):
          negative(im1)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('negative.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none3 == max(count):
          negative(im3)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('negative.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none4 == max(count):
          negative(im4)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('negative.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none5 == max(count):
          negative(im5)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('negative.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none8 == max(count):
          negative(im8)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('negative.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none6 == max(count):
          negative(im6)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('negative.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none10 == max(count):
          negative(im10)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('negative.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none2 == max(count):
          negative(im2)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('negative.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none9 == max(count):
          negative(im9)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('negative.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)

        count = []

      for x in tag_1:
        if (self.a == 'sepia' and (x== "Eastern" or x == "California" or x== "building")):
          self.a_none1= self.a_none1 + 1
        if (self.a == 'sepia' and (x== "Spreetunnel" or x == "Berlin" or x == "Germany" or x== "tunnel" or x == "ceiling")):
          self.a_none2 = self.a_none2 + 1
        if (self.a == 'sepia' and (x== "Eastern" or x == "Berlin" or x== "Eastern" or x== "wall" or x == "mosaic" or x == "sky" or x == "clouds")):
          self.a_none3= self.a_none3 + 1
        if (self.a == 'sepia' and (x == "Italy" or x == "Lombardia" or x == "alley" or x == "building" or x == "wall")):
          self.a_none4= self.a_none4 + 1
        if (self.a == 'sepia' and (x == "Rome" or x == "Italy" or x == "window" or x == "road" or x == "building")):
          self.a_none5= self.a_none5 + 1
        if (self.a == 'sepia' and (x == "Amsterdam" or x == "Netherlands" or x == "book" or x == "library" or x == "museum")):
          self.a_none6= self.a_none6 + 1
        if (self.a == 'sepia' and (x == "Amsterdam" or x == "Netherlands" or x == "canal" or x == "boat")):
          self.a_none7= self.a_none7 + 1
        if (self.a == 'sepia' and (x == "Mexico" or x == "Cabo" or x == "beach" or x == "cactus" or x == "sunrise")):
          self.a_none8= self.a_none8 + 1
        if (self.a == 'sepia' and (x == "Mexico" or x == "ocean" or x == "beach" or x == "palm")):
          self.a_none9= self.a_none9 + 1
        if (self.a == 'sepia' and (x == "Hollywood" or x == "California" or x == "Volkswagen" or x == "Beatle" or x == "car")):
          self.a_none10= self.a_none10 + 1
        if (self.a == 'sepia' and (x =="Los" or x== "Angeles")):
          self.a_none1= self.a_none1 + 0.5
          self.a_none10= self.a_none10 +0.5

        count = [self.a_none1,self.a_none2,self.a_none3,self.a_none4,self.a_none5,self.a_none6,self.a_none7,self.a_none8,self.a_none9,self.a_none10]

      if self.a == 'sepia':
        if self.a_none7 == max(count):
          sepia(im7)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('sepia.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none1 == max(count):
          sepia(im1)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('sepia.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none3 == max(count):
          sepia(im3)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('sepia.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none4 == max(count):
          sepia(im4)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('sepia.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none5 == max(count):
          sepia(im5)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('sepia.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none8 == max(count):
          sepia(im8)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('sepia.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none6 == max(count):
          sepia(im6)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('sepia.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none10 == max(count):
          sepia(im10)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('sepia.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none2 == max(count):
          sepia(im2)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('sepia.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none9 == max(count):
          sepia(im9)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('sepia.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)

        count = []

      for x in tag_1:
        if (self.a == 'grayscale' and (x== "Eastern" or x == (x =="Los" or x== "Angeles") or x == "California" or x== "building")):
          self.a_none1= self.a_none1 + 1
        if (self.a == 'grayscale' and (x== "Spreetunnel" or x == "Berlin" or x == "Germany" or x== "tunnel" or x == "ceiling")):
          self.a_none2 = self.a_none2 + 1
        if (self.a == 'grayscale' and (x== "Eastern" or x == "Berlin" or x== "Eastern" or x== "wall" or x == "mosaic" or x == "sky" or x == "clouds")):
          self.a_none3= self.a_none3 + 1
        if (self.a == 'grayscale' and (x == "Italy" or x == "Lombardia" or x == "alley" or x == "building" or x == "wall")):
          self.a_none4= self.a_none4 + 1
        if (self.a == 'grayscale' and (x == "Rome" or x == "Italy" or x == "window" or x == "road" or x == "building")):
          self.a_none5= self.a_none5 + 1
        if (self.a == 'grayscale' and (x == "Amsterdam" or x == "Netherlands" or x == "book" or x == "library" or x == "museum")):
          self.a_none6= self.a_none6 + 1
        if (self.a == 'grayscale' and (x == "Amsterdam" or x == "Netherlands" or x == "canal" or x == "boat")):
          self.a_none7= self.a_none7 + 1
        if (self.a == 'grayscale' and (x == "Mexico" or x == "Cabo" or x == "beach" or x == "cactus" or x == "sunrise")):
          self.a_none8= self.a_none8 + 1
        if (self.a == 'grayscale' and (x == "Mexico" or x == "ocean" or x == "beach" or x == "palm")):
          self.a_none9= self.a_none9 + 1
        if (self.a == 'grayscale' and (x == "Hollywood" or x == "California" or x == "Volkswagen" or x == "Beatle" or x == "car")):
          self.a_none10= self.a_none10 + 1
        if (self.a == 'grayscale' and (x =="Los" or x== "Angeles")):
          self.a_none1= self.a_none1 + 0.5
          self.a_none10= self.a_none10 +0.5
        count = [self.a_none1,self.a_none2,self.a_none3,self.a_none4,self.a_none5,self.a_none6,self.a_none7,self.a_none8,self.a_none9,self.a_none10]


      if self.a == 'grayscale':
        if self.a_none7 == max(count):
          grayscale(im7)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('grayscale.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none1 == max(count):
          grayscale(im1)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('grayscale.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none3 == max(count):
          grayscale(im3)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('grayscale.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none4 == max(count):
          grayscale(im4)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('grayscale.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none5 == max(count):
          grayscale(im5)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('grayscale.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none8 == max(count):
          grayscale(im8)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('grayscale.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none6 == max(count):
          grayscale(im6)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('grayscale.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none10 == max(count):
          grayscale(im10)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('grayscale.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none2 == max(count):
          grayscale(im2)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('grayscale.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none9 == max(count):
          grayscale(im9)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('grayscale.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)

        count = []  

      for x in tag_1:
        if (self.a == 'thumbnail' and (x== "Eastern" or x == (x =="Los" or x== "Angeles") or x == "California" or x== "building")):
          self.a_none1= self.a_none1 + 1
        if (self.a == 'thumbnail' and (x== "Spreetunnel" or x == "Berlin" or x == "Germany" or x== "tunnel" or x == "ceiling")):
          self.a_none2 = self.a_none2 + 1
        if (self.a == 'thumbnail' and (x== "Eastern" or x == "Berlin" or x== "Eastern" or x== "wall" or x == "mosaic" or x == "sky" or x == "clouds")):
          self.a_none3= self.a_none3 + 1
        if (self.a == 'thumbnail' and (x == "Italy" or x == "Lombardia" or x == "alley" or x == "building" or x == "wall")):
          self.a_none4= self.a_none4 + 1
        if (self.a == 'thumbnail' and (x == "Rome" or x == "Italy" or x == "window" or x == "road" or x == "building")):
          self.a_none5= self.a_none5 + 1
        if (self.a == 'thumbnail' and (x == "Amsterdam" or x == "Netherlands" or x == "book" or x == "library" or x == "museum")):
          self.a_none6= self.a_none6 + 1
        if (self.a == 'thumbnail' and (x == "Amsterdam" or x == "Netherlands" or x == "canal" or x == "boat")):
          self.a_none7= self.a_none7 + 1
        if (self.a == 'thumbnail' and (x == "Mexico" or x == "Cabo" or x == "beach" or x == "cactus" or x == "sunrise")):
          self.a_none8= self.a_none8 + 1
        if (self.a == 'thumbnail' and (x == "Mexico" or x == "ocean" or x == "beach" or x == "palm")):
          self.a_none9= self.a_none9 + 1
        if (self.a == 'thumbnail' and (x == "Hollywood" or x == "California" or x == "Volkswagen" or x == "Beatle" or x == "car")):
          self.a_none10= self.a_none10 + 1
        if (self.a == 'thumbnail' and (x =="Los" or x== "Angeles")):
          self.a_none1= self.a_none1 + 0.5
          self.a_none10= self.a_none10 +0.5
      count = [self.a_none1,self.a_none2,self.a_none3,self.a_none4,self.a_none5,self.a_none6,self.a_none7,self.a_none8,self.a_none9,self.a_none10]

      if self.a == 'thumbnail':
        if self.a_none7 == max(count):
          thumbnail(im7)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('thumbnail.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none1 == max(count):
          thumbnail(im1)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('thumbnail.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none3 == max(count):
          thumbnail(im3)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('thumbnail.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none4 == max(count):
          thumbnail(im4)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('thumbnail.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none5 == max(count):
          thumbnail(im5)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('thumbnail.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none8 == max(count):
          thumbnail(im8)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('thumbnail.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none6 == max(count):
          thumbnail(im6)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('thumbnail.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none10 == max(count):
          thumbnail(im10)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('thumbnail.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none2 == max(count):
          thumbnail(im2)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('thumbnail.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)
        if self.a_none9 == max(count):
          thumbnail(im9)
          w = self.w = Window2()
          my_label = QLabel(w)
          pixmap = QPixmap('thumbnail.jpg')
          my_label.setPixmap(pixmap)
          my_label.resize(pixmap.width(),pixmap.height())
          w.show()
          clear(self)

#i made function and inside the function there are filter functions to save the images with filter. and if words matches count goes up by 1. 
# and if count has highest match. then it shows images and clear the count. and if the count is same for multiple picture it show first picture in alphabet order

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
