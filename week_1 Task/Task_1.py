import numpy as np


numbers = [5, 20, 65, 12, 25]

num_array = np.array(numbers)

mean_value = np.mean(num_array)

max_value = np.max(num_array)

sum_value = np.sum(num_array)

print("The results of the operations:")
print("Mean:", mean_value)
print("Max value:", max_value)
print("Sum:", sum_value)
