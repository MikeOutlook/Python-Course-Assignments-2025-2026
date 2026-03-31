import numpy as np
arr = np.arange(1, 10)
print(arr)
# Select numbers greater than 5 from array
print(arr[arr > 5])
# Select even numbers greater than 5 from array
print(arr[(arr > 5) & (arr % 2 == 0)])
# Select numbers greater than 5 or even numbers from array
print(arr[(arr > 5) | (arr % 2 == 0)])
arr2d = arr.reshape(3, 3)
print(arr2d)
# Find all rows where column 2 elements are divisible by 2
print(arr2d[arr2d[:, 1] % 2 == 0])