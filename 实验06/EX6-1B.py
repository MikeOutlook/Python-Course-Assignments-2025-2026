import numpy as np

arr = np.arange(1,31)
arr2d = arr.reshape(5, 6)
print("原始数组:\n",arr2d)

slice_r =arr2d[0:5,0:2]  #使用切片索引取出红色部分数据，将本行代码补充完整
slice_g =arr2d[3:5,1:6]  #使用切片索引取出绿色部分数据，将本行代码补充完整
slice_b =arr2d[1:4,2:5]  #使用切片索引取出蓝色部分数据，将本行代码补充完整

print("切片索引")
print("红色部分:\n", slice_r)
print("绿色部分:\n", slice_g)
print("蓝色部分:\n", slice_b)
