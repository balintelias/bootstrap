"""
Python function for exporting the dataset
"""
import numpy as np
import matplotlib.pyplot as plt


def func_export(param):
    file2 = open("output.txt", "w")  # write mode

    """
    for items in param:
        file2.writelines(str([items]))
    """
    for items in param:
        for values in items:
            file2.write(str([values]))

    file2.close()

    file3 = open("output.txt", "r")
    #read input to file
    content = file3.read()
    file3.close()

    content = content.replace(']', ' ')
    content = content.replace('[', '')

    file4 = open("output.txt", "w")  # write mode
    #write output into file
    file4.write(content)
    file4.close()