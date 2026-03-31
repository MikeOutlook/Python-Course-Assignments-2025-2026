import numpy as np

temp_list = [37.7, 37.5, 37.3, 36.8, 38.4, 37.4, 37.7, 36.3, 39.0, 38.5,
             37.8, 37.3, 36.6, 36.2, 37.5, 37.6, 38.6, 36.9, 38.2, 37.9]

# Convert temp_list to numpy array
temp_array = np.array(temp_list)

# Use boolean index to filter values greater than 37.8
new = temp_array[temp_array > 37.8]

new_list = new.tolist()
print(new_list)

