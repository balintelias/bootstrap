import numpy as np
import matplotlib.pyplot as plt
import generate

# generate two dimensional input array
arr = generate.func_generate()

# write to file
file1 = open("input.csv", "w")  # write mode
arr_size = len(arr)
count = 0
while (count < arr_size):
	content = np.array(arr)[count]
	file1.write(str(content))
	file1.write(" ")
	count = count + 1
file1.close()

# separate values by commas
file5 = open("input.csv", "r")  #read mode
content = file5.read()
file5.close()

content = content.replace(']', '\n')
content = content.replace('[', '')
content = content.replace('  ', ' ')
content = content.replace('\n ', '\n')
content = content[1:]
content = content[:-1]
content = content.replace(' ',',')

file6 = open("input.csv", "w")  # write mode
file6.write(content)
file6.close()