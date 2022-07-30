import numpy as np
import matplotlib.pyplot as plt
import generate
import bootstrap

arr = generate.func_generate()

# getting data of the histogram
count, bins_count = np.histogram(arr, bins=100)

# finding the PDF of the histogram using count values
pdf = count / sum(count)

standard_deviation = np.std(arr, ddof=1)
print("sd1")
print(standard_deviation)
  
# plotting
plt.plot(bins_count[1:], pdf)
plt.show()

#second_arr = bootstrap.func_bootstrap(array)
second_arr = bootstrap.func_bootstrap(arr)

# getting data of the histogram
new_count, new_bins_count = np.histogram(arr, bins=100)

# finding the PDF of the histogram using count values
new_pdf = new_count / sum(new_count)


new_standard_deviation = np.std(second_arr, ddof=1)
print("sd2")
print(new_standard_deviation)

# plotting
plt.plot(new_bins_count[1:], new_pdf)
plt.show()