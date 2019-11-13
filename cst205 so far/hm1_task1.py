from collections import Counter

bins = [(0,63),(64,127),(128,191),(192,255)]


bin_data = [ 
     (54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167), 
     (204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93), 
     (71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122), 
     (168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)
]

def find_bin(value, bins):

	for i in range(0, len(bins)):
		if bins[i][0] <= value < bins[i][1]:
			return 1
		return 0
		if bins[i+1][0] <= value < bins[i+1][1]:
			return 1
		return 0
		
binned_data = []
for value in bin_data:
	bin_index = find_bin(value[0], bins)
	print(value, bin_index, bins[bin_index])
	binned_data.append(bin_index)

frequencies = Counter(binned_data)
print(frequencies)