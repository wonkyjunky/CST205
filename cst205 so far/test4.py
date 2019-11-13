import pickle
import numpy as np
import matplotlib
matplotlib.use('SVG')
import matplotlib.pyplot as plt

import hw1_hist_plotter as hp

bins = [(0,63),(64,127),(128,191),(192,255)]


data = pickle.load (open('image_matrix','rb'))

red_values = []
for x in data:
	for y in x:
		red_values.append(y[0])

green_values = []
for x in data:
	for y in x:
		green_values.append(y[1])

blue_values = []
for x in data:
	for y in x:
		blue_values.append(y[2])

redlist = [(0,0,0,0)]
for x in red_values:
	if bins[0][0] <= x <= bins[0][1]:
		redlist.append(redlist[0][0]+1)
red1 = redlist.count(1)

redlist = [(0,0,0,0)]
for x in red_values:
	if bins[1][0] <= x <= bins[1][1]:
		redlist.append(redlist[0][1]+1)

red2 = redlist.count(1)

redlist = [(0,0,0,0)]
for x in red_values:
	if bins[2][0] <= x <= bins[2][1]:
		redlist.append(redlist[0][2]+1)

red3 = redlist.count(1)

redlist = [(0,0,0,0)]
for x in red_values:
	if bins[3][0] <= x <= bins[3][1]:
		redlist.append(redlist[0][3]+1)

red4 = redlist.count(1)


redfinal = [red1,red2,red3,red4]


bluelist = [(0,0,0,0)]
for x in blue_values:
	if bins[0][0] <= x <= bins[0][1]:
		bluelist.append(bluelist[0][0]+1)
blue1 = bluelist.count(1)

bluelist  = [(0,0,0,0)]
for x in blue_values:
	if bins[1][0] <= x <= bins[1][1]:
		bluelist.append(bluelist[0][1]+1)

blue2 = bluelist.count(1)

bluelist  = [(0,0,0,0)]
for x in blue_values:
	if bins[2][0] <= x <= bins[2][1]:
		bluelist.append(bluelist[0][2]+1)

blue3 = bluelist.count(1)

bluelist  = [(0,0,0,0)]
for x in blue_values:
	if bins[3][0] <= x <= bins[3][1]:
		bluelist.append(bluelist[0][3]+1)

blue4 = bluelist.count(1)

bluefinal = [blue1,blue2,blue3,blue4]

greenlist = [(0,0,0,0)]
for x in green_values:
	if bins[0][0] <= x <= bins[0][1]:
		greenlist.append(greenlist[0][0]+1)
green1 = greenlist.count(1)

greenlist = [(0,0,0,0)]
for x in green_values:
	if bins[1][0] <= x <= bins[1][1]:
		greenlist.append(greenlist[0][1]+1)

green2 = greenlist.count(1)

greenlist = [(0,0,0,0)]
for x in green_values:
	if bins[2][0] <= x <= bins[2][1]:
		greenlist.append(greenlist[0][2]+1)

green3 = greenlist.count(1)

greenlist = [(0,0,0,0)]
for x in green_values:
	if bins[3][0] <= x <= bins[3][1]:
		greenlist.append(greenlist[0][3]+1)

green4 = greenlist.count(1)

greenfinal = [green1,green2,green3,green4]

rgbvalue = [redfinal, greenfinal, bluefinal]

task2 = [red_values, green_values, blue_values]

final = ['Red','Green','Blue']

final = dict(zip(final, rgbvalue))

hp.hist_plotter(task2)