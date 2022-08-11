import getopt, sys

import numpy as np
import matplotlib.pyplot as plt
import header

help_msg = """Usage:
-h --Help   
-o: --Output=

The program requires the input file to be named dataset.csv and to be placed in the same directory.
"""

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "ho:"
 
# Long options
long_options = ["Help", "Output="]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print (help_msg)
            sys.exit("Program exiting")
             
        elif currentArgument in ("-o", "--Output"):
            print (("Enabling special output mode (% s)") % (currentValue))
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

user_input = input('Number:')

try:
    arr = header.retrieve()
except:
    print("Error while retrieving input: dataset.csv not found")
    sys.exit("Program exiting")

# header.visual(arr)

# bootstrap arr to second_arr
second_arr = header.bootstrap(arr)

# header.visual(second_arr)

header.export(second_arr)

sys.exit("Program exiting")