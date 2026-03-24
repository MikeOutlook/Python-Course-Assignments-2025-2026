import numpy as np
arr1 = np.loadtxt("data.csv", delimiter=",", skiprows=1,
                  usecols=[0, 1], dtype=int,)
print(arr1)