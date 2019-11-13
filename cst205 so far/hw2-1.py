"""
NAME: WON KYU JEONG
DATE: 10/5/2019
COURSE: CST 205
Coding Partner: YE LIN JOH
"""

""" i used hw2 code with image from internet and it worked"""


from PIL import Image



def Mediansort(list):
  middle = len(list)//2
  return list[middle]
files = {1:"hw2_image/01.jpg",
     2:"hw2_image/02.jpg",
     3:"hw2_image/03.jpg"}
im1 = Image.open(files[1])
im2 = Image.open(files[2])
im3 = Image.open(files[3])
list1 = list(im1.getdata())
list2 = list(im2.getdata())
list3 = list(im3.getdata())
count = 0
nofoxlist = []
while(count < len(list1)):
  final = [list1[count],list2[count],list3[count]]

  final = sorted(final, reverse=True)

  
  pixel = Mediansort(final)
  count = count+1
  nofoxlist.append(pixel)
  
im1.putdata(nofoxlist)
im1.save('hw2_image/nohand.jpg')