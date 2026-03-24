import #导入numpy库，将本行代码补充完整

arr_A =    #产生数组，将本行代码补充完整
print("数组arr_A：\n",arr_A)

arr_B =    #找出被7整除的数存入数组，将本行代码补充完整
print("数组arr_B：\n",arr_B)

n =    #求arr_B数组元素个数，将本行代码补充完整
arr_C =    #切片arr_A数组需要的数据并除以arr_B数组，将本行代码补充完整
print("数组arr_C：\n",arr_C)

import numpy as np  #导入numpy库，将本行代码补充完整

arr_A = np.arange(3, 1000, 4)    #产生数组，将本行代码补充完整
print("数组arr_A：\n",arr_A)

arr_B = arr_A[arr_A % 7 == 0]    #找出被7整除的数存入数组，将本行代码补充完整
print("数组arr_B：\n",arr_B)

n = len(arr_B)    #求arr_B数组元素个数，将本行代码补充完整
arr_C = arr_A[50:50+n] / arr_B    #切片arr_A数组需要的数据并除以arr_B数组，将本行代码补充完整
print("数组arr_C：\n",arr_C)