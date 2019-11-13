"""
My name: WONKYU JEONG
DATE: 2019.09.22
Partner : YE LIN JOH
COURSE NAME: CST205 
"""



import pickle
def task1(): #definated task1
	bins = [(0,63),(64,127),(128,191),(192,255)] #make bins to sort values into bins


	data= pickle.load (open('image_matrix','rb')) # to open data, i used pickle.load.

	red_values = []
	for x in data:
		for y in x:
			red_values.append(y[0]) # I put red data into list

		green_values = []
	for x in data:
		for y in x:
			green_values.append(y[1]) # I put green data into list

	blue_values = []
	for x in data:
		for y in x:
			blue_values.append(y[2]) # I put blue data into list

	redlist = [(0,0,0,0)]
	for x in red_values:
		if bins[0][0] <= x <= bins[0][1]:
			redlist.append(redlist[0][0]+1)
	red1 = redlist.count(1) # i counted how many numbers in first bin for red values

	redlist = [(0,0,0,0)]
	for x in red_values:
		if bins[1][0] <= x <= bins[1][1]:
			redlist.append(redlist[0][1]+1)

	red2 = redlist.count(1) # i counted how many numbers in second bin for red values


	redlist = [(0,0,0,0)]
	for x in red_values:
		if bins[2][0] <= x <= bins[2][1]:
			redlist.append(redlist[0][2]+1)

	red3 = redlist.count(1) # i counted how many numbers in third bin for red values

	redlist = [(0,0,0,0)]
	for x in red_values:
		if bins[3][0] <= x <= bins[3][1]:
			redlist.append(redlist[0][3]+1)

	red4 = redlist.count(1) # i counted how many numbers in fourth bin for red values


	redfinal = [red1,red2,red3,red4] #and i put counted number into a list called redfinal.

	""" i did same method for blue and green values."""	
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


#after making counted numbers lists i put those to a emptylist. 
	rgbvalue = [redfinal, greenfinal, bluefinal]

	final = ['Red','Green','Blue']

# and i made list of value's name. and i used zip to make counted numbers to connect to the names. 
	final = dict(zip(final, rgbvalue))


	print(final)

task1()