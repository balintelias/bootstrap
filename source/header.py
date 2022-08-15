import numpy as np
import matplotlib.pyplot as plt
import csv

# Python function for generating mock datasets
def generate():
	outer_temp = []
	for x in range(5):
		temp = []
		newArr = np.random.randint(0, 100, size = 4)
		temp.extend(newArr)
		newArr = np.random.randint(40, 60, size = 2)
		temp.extend(newArr)
		newArr = np.random.randint(0, 100, size = 4)
		temp.extend(newArr)
		outer_temp.append(temp)
	return outer_temp

# Python function for retrieving the dataset from file
def retrieve():
	fileobject = open("input.csv", "r")
	#read input to file
	content = fileobject.read()
	fileobject.close()
	content = content.replace(',', ' ')
	fileobject = open("input-2.csv", "w")  # write mode
	#write output into file
	fileobject.write(content)
	fileobject.close()
	# TODO: delete input-2.csv

	# opening the 'input.csv' file to read its contents
	with open('input-2.csv', newline = '') as file:
		reader = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC,
							delimiter = ' ')
	 
		# storing all the rows in an output list
		output = []
		for row in reader:
			output.append(row[:])
	return output


# Python script for visualizing a dataset
def visual(temp):
	# getting data of the histogram
	count, bins_count = np.histogram(temp, bins=100)

	# finding the PDF of the histogram using count values
	pdf = count / sum(count)

	standard_deviation = np.std(temp, ddof=1)
	print("sd1")
	print(standard_deviation)

	# plotting
	plt.plot(bins_count[1:], pdf)
	plt.show()


# Python function for exporting the dataset
def export(param):
	# using the open method with 'w' mode
	# for creating a new csv file 'my_csv' with .csv extension
	with open('output.csv', 'w', newline = '') as file:
		writer = csv.writer(file, quoting = csv.QUOTE_NONNUMERIC,
							delimiter = ' ')
		writer.writerows(param)
	
	file3 = open("output.csv", "r")
	#read input to file
	content = file3.read()
	file3.close()

	content = content.replace(' ', ',')

	file4 = open("output.csv", "w")  # write mode
	#write output into file
	file4.write(content)
	file4.close()


"""
bootstrap function is returning a new dataset with
arbitrary size. the new datasert is bootstrapped from
the original array passed as a parameter.
"""
def bootstrap(param, times):
	new_arr = []
	for row in param:
		count = 0
		arr_size = len(row)
		new_row = []
		while count < int(times):
			index = np.random.randint(0, arr_size, size = 1)
			count = count + 1
			new_element = np.array(row)[index]
			new_element = int(new_element)
			new_row.append(new_element)
		new_arr.append(new_row)
	return new_arr