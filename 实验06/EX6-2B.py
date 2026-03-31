import numpy as np

arr = np.arange(1,31)
arr2d = arr.reshape(5, 6)
print("Original array:\n",arr2d)

bool_r =arr[arr%9==0]  # Use boolean index to extract red part data according to conditions, complete this line
bool_g =arr[(arr>20)&(arr%3!=0)]  # Use boolean index to extract green part data according to conditions, complete this line
bool_b =arr[(arr%11==1)|(arr%13==1)]  # Use boolean index to extract blue part data according to conditions, complete this line

print("Boolean index")
print("Red part:\n", bool_r)
print("Green part:\n", bool_g)
print("Blue part:\n", bool_b)
