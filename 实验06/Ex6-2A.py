import numpy as np
arr = np.arange(1, 10)
print(arr)
# 选出数组中大于 5 的数
print(arr[arr > 5])
# 选出数组中大于 5 的偶数
print(arr[(arr > 5) & (arr % 2 == 0)])
# 选出数组中大于 5 的数或者偶数
print(arr[(arr > 5) | (arr % 2 == 0)])
arr2d = arr.reshape(3, 3)
print(arr2d)
# 找出第 2 列元素能够被 2 整除的所有行
print(arr2d[arr2d[:, 1] % 2 == 0])