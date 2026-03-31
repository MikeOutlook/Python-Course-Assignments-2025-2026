import numpy as np # Import numpy, complete this line

height_list = [1.68, 1.81, 1.76, 1.68, 1.73, 1.72, 1.74]
weight_list = [185.2, 169.4, 143.7, 191.8, 172.6, 124.1, 153.5]

height =np.array(height_list)  # Create array from height list, complete this line
weight =np.array(weight_list,dtype=int)  # Create array from weight list, integer type, complete this line

print("Patient height data:\n",height)
print("Patient weight data:\n",weight)


