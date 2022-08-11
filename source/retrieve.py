"""
Python function for retrieving the dataset
"""
import numpy as np
import matplotlib.pyplot as plt


def func_retrieve():
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