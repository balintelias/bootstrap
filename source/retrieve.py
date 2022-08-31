# Copyright (C) 2022 Bálint Éliás
# You can find the copyright disclaimer in final/bootstrap.py
#
# This code was used in developing the full program,
# but this particular file is not used in it

# contact me at: ebalint [at] gmail [dot] com


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