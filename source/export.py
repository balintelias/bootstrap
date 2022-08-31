# Copyright (C) 2022 Bálint Éliás
# You can find the copyright disclaimer in final/bootstrap.py
#
# This code was used in developing the full program,
# but this particular file is not used in it

# contact me at: ebalint896 [at] gmail [dot] com

"""
Python function for exporting the dataset
"""
import numpy as np
import matplotlib.pyplot as plt


def func_export(param):
    file2 = open("output.csv", "w")  # write mode

    """
    for items in param:
        file2.writelines(str([items]))
    """
    for items in param:
        for values in items:
            file2.write(str([values]))

    file2.close()

    file3 = open("output.csv", "r")
    #read input to file
    content = file3.read()
    file3.close()

    content = content.replace(']', ' ')
    content = content.replace('[', '')

    file4 = open("output.csv", "w")  # write mode
    #write output into file
    file4.write(content)
    file4.close()