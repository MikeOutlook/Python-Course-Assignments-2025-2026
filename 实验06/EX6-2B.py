import numpy as np

arr = np.arange(1,31)
arr2d = arr.reshape(5, 6)
print("原始数组:\n",arr2d)

bool_r =arr[arr%9==0]  #使用布尔索引按题目要求的条件取出红色部分数据，将本行代码补充完整
bool_g =arr[(arr>20)&(arr%3!=0)]  #使用布尔索引按题目要求的条件取出绿色部分数据，将本行代码补充完整
bool_b =arr[(arr%11==1)|(arr%13==1)]  #使用布尔索引按题目要求的条件取出蓝色部分数据，将本行代码补充完整

print("布尔索引")
print("红色部分:\n", bool_r)
print("绿色部分:\n", bool_g)
print("蓝色部分:\n", bool_b)
