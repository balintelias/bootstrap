import getopt, sys
import csv
import os
import numpy as np

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
	content = content.replace(';', ' ')

	fileobject = open("input-2.csv", "w")  # write mode
	#write output into file
	fileobject.write(content)
	fileobject.close()
	print(content)


	# opening the 'input.csv' file to read its contents
	with open('input-2.csv', newline = '') as file:
		reader = csv.reader(file, quoting = csv.QUOTE_NONE,
							delimiter = ' ')

		# storing all the rows in an output list
		output = []
		for row in reader:
			output.append(row[:])
	os.remove("input-2.csv")
	return output

def remove_ID(param):
	excess = []
	for row in param:
		currentID = row.pop(0)
		# print(currentID)
		excess.append(currentID)
	return excess


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
def export(id_param, param, filename):
	# combine id_param and param
	for row in param:
		currentID = id_param.pop(0)
		row.insert(0, currentID)

	# using the open method with 'w' mode
	# for creating a new csv file 'my_csv' with .csv extension
	with open(filename, 'w', newline = '') as file:
		writer = csv.writer(file, quoting = csv.QUOTE_NONE,
							delimiter = ' ')
		writer.writerows(param)
	
	file3 = open(filename, "r")
	#read input to file
	content = file3.read()
	file3.close()

	content = content.replace(' ', ';')

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
		while count < times:
			index = np.random.randint(0, arr_size, size = 1)
			count = count + 1
			new_element = np.array(row)[index]
			new_element = int(new_element)
			new_row.append(new_element)
		new_arr.append(new_row)
	return new_arr

help_msg = """Usage:
-h --Help
-d --Debug

The program needs the input file to be in the same directory.

"""
exit_msg = "Program exiting"

DBG = False

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hi:o:d"
 
# Long options
long_options = ["Help", "Debug"]

try:
	# Parsing argument
	arguments, values = getopt.getopt(argumentList, options, long_options)
	 
	# checking each argument
	for currentArgument, currentValue in arguments:
 
		if currentArgument in ("-h", "--Help"):
			print (help_msg)
			sys.exit(exit_msg)

		elif currentArgument in ("-d", "--Debug"):
			print("Enabling Debug mode")
			DBG = True


except getopt.error as err:
	# output error, and return with an error code
	print (str(err))
	sys.exit(exit_msg)

inputfilename = input("Name of the input file:")

# get input
try:
	arr = retrieve(inputfilename)
	if(DBG):
		print("DBG: Input file opened, data imported")
except:
	print("Error while retrieving input: input file not found")
	sys.exit(exit_msg)

# remove ID from the lists
id_list = remove_ID(arr)

user_input = input('Size of new dataset:')

try:
	user_input = int(user_input)
except:
	print(("Cannot cast input (% s) to integer.") % (user_input))
	sys.exit(exit_msg)

outputfilename = inputfilename
outputfilename = outputfilename[:-4]
outputfilename = outputfilename + "_rep_" + str(user_input) + ".csv"

# bootstrap arr to second_arr
second_arr = bootstrap(arr, user_input)
if(DBG):
	print("DBG: Bootstrapping finished")

export(id_list, second_arr, outputfilename)
if(DBG):
	print("DBG: New dataset exported")