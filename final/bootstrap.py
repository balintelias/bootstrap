import getopt, sys
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

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
def retrieve(filename):
	fileobject = open(filename, "r")
	#read input to file
	content = fileobject.read()
	fileobject.close()
	content = content.replace(',', ' ')
	fileobject = open("input-2.csv", "w")  # write mode
	#write output into file
	fileobject.write(content)
	fileobject.close()


	# opening the 'input.csv' file to read its contents
	with open('input-2.csv', newline = '') as file:
		reader = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC,
							delimiter = ' ')
	 
		# storing all the rows in an output list
		output = []
		for row in reader:
			output.append(row[:])

	os.remove("input-2.csv")
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
def export(param, filename):
	# using the open method with 'w' mode
	# for creating a new csv file 'my_csv' with .csv extension
	with open(filename, 'w', newline = '') as file:
		writer = csv.writer(file, quoting = csv.QUOTE_NONNUMERIC,
							delimiter = ' ')
		writer.writerows(param)
	
	file3 = open(filename, "r")
	#read input to file
	content = file3.read()
	file3.close()

	content = content.replace(' ', ',')

	file4 = open(filename, "w")  # write mode
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

help_msg = """Usage:
-h --Help
-i: --Input=
-o: --Output=

The program needs the input file to be in the same directory.
The -i:/--Input= flag may be used to specify the input file, but by default it's input.csv.
The -o:/--Output= flag may be used to specify the output file, but by default it's output.csv.
"""

inputfilename = "input.csv"
outputfilename = "output.csv"

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hi:o:"
 
# Long options
long_options = ["Help", "Input=", "Output="]

try:
	# Parsing argument
	arguments, values = getopt.getopt(argumentList, options, long_options)
	 
	# checking each argument
	for currentArgument, currentValue in arguments:
 
		if currentArgument in ("-h", "--Help"):
			print (help_msg)
			sys.exit("Program exiting")

		elif currentArgument in ("-i", "--Input"):
			print (("Enabling special input mode (% s)") % (currentValue[1:]))
			inputfilename = currentValue[1:]

		elif currentArgument in ("-o", "--Output"):
			print (("Enabling special output mode (% s)") % (currentValue[1:]))
			outputfilename = currentValue[1:]

except getopt.error as err:
	# output error, and return with an error code
	print (str(err))

try:
	print(inputfilename)
	arr = retrieve(inputfilename)
except:
	print("Error while retrieving input: input file not found")
	sys.exit("Program exiting")

user_input = input('Number:')

# bootstrap arr to second_arr
second_arr = bootstrap(arr, user_input)

export(second_arr, outputfilename)

sys.exit("Program exiting")