import getopt, sys

import numpy as np
import matplotlib.pyplot as plt
import generate
import bootstrap
import visual
import retrieve
import export

help_msg = """Usage:
-h --Help   
-o: --Output=

The program requires the input file to be named dataset.txt and to be placed in the same directory.
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


try:
    arr = retrieve.func_retrieve()
except:
    print("Error while retrieving input: dataset.txt not found")
    sys.exit("Program exiting")

# visual.func_visual(arr)

# bootstrap arr to second_arr
second_arr = bootstrap.func_bootstrap(arr)

# visual.func_visual(second_arr)

export.func_export(second_arr)

sys.exit("Program exiting")