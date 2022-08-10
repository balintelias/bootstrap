"""
Python function for generating mock datasets
"""

import numpy as np
import matplotlib.pyplot as plt

def func_generate():
    temp = []
    newArr = np.random.randint(0, 100, size = 40)
    temp.extend(newArr)
    newArr = np.random.randint(40, 60, size = 20)
    temp.extend(newArr)
    newArr = np.random.randint(0, 100, size = 40)
    temp.extend(newArr)



    #print('-----Generated Random Array----')
    #print(temp)

    

    return temp