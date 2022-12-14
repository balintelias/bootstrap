# Copyright (C) 2022 Bálint Éliás
# You can find the copyright disclaimer in final/bootstrap.py
#
# This code was used in developing the full program,
# but this particular file is not used in it

# contact me at: ebalint896 [at] gmail [dot] com


"""
Python script for visualizing a dataset
"""
import numpy as np
import matplotlib.pyplot as plt

def func_visual(temp):
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