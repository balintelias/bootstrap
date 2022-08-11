import numpy as np
"""
bootstrap function is returning one array
which is bootstrapped from the original array
passed as a parameter
"""
def func_bootstrap(param):
    arr_size = len(param)
    count = 0
    new_arr = []
    while (count < arr_size):   
        index = np.random.randint(0, arr_size, size = 1)
        count = count + 1
        new_element = np.array(param)[index]
        new_arr.append(new_element)
    # print("new array size")
    # print(len(new_arr))
    return new_arr