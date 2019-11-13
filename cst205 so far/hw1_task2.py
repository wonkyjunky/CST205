"""
My name: WONKYU JEONG
DATE: 2019.09.22
Partner : YE LIN JOH
COURSE NAME: CST205 
"""



import pickle
import numpy as np
import matplotlib
matplotlib.use('SVG')
import matplotlib.pyplot as plt
import hw1_hist_plotter as hp

def task2(file_name): # I defined task2() function.
	data = pickle.load (open('image_matrix','rb')) # to open data file, i used pickle.load.

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

	"""In order to get red, green and blue values seperated. i made seperated list of R,G,B Values.
	and i put those value lists to final list"""

	final = [red_values, green_values, blue_values]

	return final

	hp.hist_plotter(final) #To use helper module i used hp.hist_plotter.


hp.hist_plotter(task2("image_matrix")) 
# To execute the task2. and i got the results of histograms.


