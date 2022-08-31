# Copyright (C) 2022 Bálint Éliás
# You can find the copyright disclaimer in final/bootstrap.py
#
# This code was used in developing the full program,
# but this particular file is not used in it

# contact me at: ebalint896 [at] gmail [dot] com

"""
Python function for generating mock datasets
"""

import numpy as np
import matplotlib.pyplot as plt

def func_generate():
    outer_temp = []
    for x in range(5):
        temp = []
        newArr = np.random.randint(0, 100, size = 20)
        temp.extend(newArr)
        newArr = np.random.randint(40, 60, size = 10)
        temp.extend(newArr)
        newArr = np.random.randint(0, 100, size = 20)
        temp.extend(newArr)
        outer_temp.append(temp)
    return outer_temp