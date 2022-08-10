import numpy as np
import matplotlib.pyplot as plt
import generate

arr = generate.func_generate()

file1 = open("input.txt", "w")  # write mode


arr_size = len(arr)
count = 0

while (count < arr_size):
	content = np.array(arr)[count]
	file1.write(str(content))
	file1.write(" ")
	count = count + 1

file1.close()