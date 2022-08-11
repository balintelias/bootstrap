import numpy as np
import matplotlib.pyplot as plt
import generate

arr = generate.func_generate()

print(str(arr))

file1 = open("input.csv", "w")  # write mode


arr_size = len(arr)
count = 0

while (count < arr_size):
	content = np.array(arr)[count]
	file1.write(str(content))
	file1.write(" ")
	count = count + 1

file1.close()

file5 = open("input.csv", "r")
#read input to file
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
#write output into file
file6.write(content)
file6.close()