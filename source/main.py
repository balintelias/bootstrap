import getopt, sys

import numpy as np
import matplotlib.pyplot as plt
import header

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
	arr = header.retrieve(inputfilename)
except:
	print("Error while retrieving input: input file not found")
	sys.exit("Program exiting")

user_input = input('Number:')

# header.visual(arr)

# bootstrap arr to second_arr
second_arr = header.bootstrap(arr, user_input)

# header.visual(second_arr)

header.export(second_arr, outputfilename)

sys.exit("Program exiting")