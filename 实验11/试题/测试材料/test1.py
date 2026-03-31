#
# My Student ID: private
# My Name: 2023220986
import numpy as np
arr1 =np.arange(10,1200,7)   # 1. Create first array, complete this line
arr2 =arr1[arr1%3==0]   # 2. Use boolean index to generate second array, complete this line
arr3 =arr2.reshape(-1,8)   # 3. Convert to third array, complete this line
print("Number of elements in arr3:",arr3.size)  # 4. Display element count, complete code inside parentheses
arr3[:,0]=(arr3[:,-1]+arr3[:,-2])**0.5   # 5. Calculate, complete code inside left brackets and right side
result1 =arr3[2:6,0:3]   # 6. Slice, complete this line
print("result1 array is as follows:\n",result1)