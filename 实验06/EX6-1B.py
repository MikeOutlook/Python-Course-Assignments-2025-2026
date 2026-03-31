import numpy as np

arr = np.arange(1,31)
arr2d = arr.reshape(5, 6)
print("Original array:\n",arr2d)

slice_r =arr2d[0:5,0:2]  # Use slice index to extract red part data, complete this line
slice_g =arr2d[3:5,1:6]  # Use slice index to extract green part data, complete this line
slice_b =arr2d[1:4,2:5]  # Use slice index to extract blue part data, complete this line

print("Slice index")
print("Red part:\n", slice_r)
print("Green part:\n", slice_g)
print("Blue part:\n", slice_b)
