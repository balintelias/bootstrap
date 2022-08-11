import numpy as np
import matplotlib.pyplot as plt

# Python function for generating mock datasets
def generate():
    outer_temp = []
    for x in range(5):
        temp = []
        newArr = np.random.randint(0, 100, size = 4)
        temp.extend(newArr)
        newArr = np.random.randint(40, 60, size = 2)
        temp.extend(newArr)
        newArr = np.random.randint(0, 100, size = 4)
        temp.extend(newArr)
        outer_temp.append(temp)
    return outer_temp

# Python function for retrieving the dataset from file
def retrieve():
	temp = []
	file1 = open("input.csv", "r")  # read mode

	# init string
	content = file1.read()

	# using List comprehension + isdigit() +split()
	# getting numbers from string 
	res = [int(i) for i in content.split() if i.isdigit()]
  
	# print result
	# print("The numbers list is : " + str(res))
	file1.close()
	temp.extend(res)
	return temp

# Python script for visualizing a dataset
def visual(temp):
	# getting data of the histogram
	count, bins_count = np.histogram(temp, bins=100)

	# finding the PDF of the histogram using count values
	pdf = count / sum(count)

	standard_deviation = np.std(temp, ddof=1)
	print("sd1")
	print(standard_deviation)
  
	# plotting
	plt.plot(bins_count[1:], pdf)
	plt.show()

# Python function for exporting the dataset
def export(param):
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

"""
bootstrap function is returning one array
which is bootstrapped from the original array
passed as a parameter
"""
def bootstrap(param):
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