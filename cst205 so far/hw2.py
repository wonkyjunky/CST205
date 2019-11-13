"""
NAME: WON KYU JEONG
DATE: 10/5/2019
COURSE: CST 205
Coding Partner: YE LIN JOH
"""


from PIL import Image



def Mediansort(list):
  middle = len(list)//2
  return list[middle]  #define Mediansort function to find median pixel.


files = {1:"hw2_image/1.png",
     2:"hw2_image/2.png",
     3:"hw2_image/3.png",
     4:"hw2_image/4.png",
     5:"hw2_image/5.png",
     6:"hw2_image/6.png",
     7:"hw2_image/7.png",
     8:"hw2_image/8.png",
     9:"hw2_image/9.png",
     10:"hw2_image/10.png",
     11:"hw2_image/11.png"}
im1 = Image.open(files[1])
im2 = Image.open(files[2])
im3 = Image.open(files[3])
im4 = Image.open(files[4])
im5 = Image.open(files[5])
im6 = Image.open(files[6])
im7 = Image.open(files[7])
im8 = Image.open(files[8])
im9 = Image.open(files[9])
im10 = Image.open(files[10])
im11 = Image.open(files[11])
list1 = list(im1.getdata())
list2 = list(im2.getdata())
list3 = list(im3.getdata())
list4 = list(im4.getdata())
list5 = list(im5.getdata())
list6 = list(im6.getdata())
list7 = list(im7.getdata())
list8 = list(im8.getdata())
list9 = list(im9.getdata())
list10 = list(im10.getdata())
list11 = list(im11.getdata())  #put images into dictionary and load the images and get their data into list



count = 0 
nofoxlist = []
while(count < len(list1)):
  final = [list1[count],list2[count],list3[count],list4[count],list5[count],list6[count],list7[count],list8[count],list9[count],list10[count],list11[count]]
  final = sorted(final, reverse=True) # i did reverse one because it doesn't matter. it only need median number.
  pixel = Mediansort(final)
  count = count+1
  nofoxlist.append(pixel) #since i need to sort the data and find median number from 0th value to last value so i used while loop and finally i appended the pixel value to list. 
  
im1.putdata(nofoxlist)
im1.save('hw2_image/nofox.png') #i used first image and put the median sorted data into image. and saved it. 
