# bootstrap.py, a Python program useful for bootstrapping complex datasets
# Copyright (C) 2022 Bálint Éliás

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# contact me at: ebalint896 [at] gmail [dot] com

import getopt, sys
import csv
import os
import numpy as np

# Python function for retrieving the dataset from file
def retrieve(filename):
	# opening the 'input.csv' file to read its contents
	with open('input.csv', newline = '') as file:
		reader = csv.reader(file, quoting = csv.QUOTE_NONE,
							delimiter = ';')

		# storing all the rows in an output list
		output = []
		for row in reader:
			output.append(row[:])
	return output

def remove_ID(param):
	excess = []
	for row in param:
		currentID = row.pop(0)
		# print(currentID)
		excess.append(currentID)
	return excess


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
							delimiter = ';')
		writer.writerows(param)

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

#init:
print("""bootstrap.py  Copyright (C) 2022  Bálint Éliás
This program comes with ABSOLUTELY NO WARRANTY; for details,
see the documentation, or the GNU GPLv3 License.
""")

# init values
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
options = "hd"
 
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