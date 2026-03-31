import numpy as np # Import numpy library, complete this line

temp_list = [37.7, 37.5, 37.3, 36.8, 38.4, 37.4,
             37.7, 36.3, 39.0, 38.5, 37.8, 37.3,
             36.6, 36.2, 37.5, 37.6, 38.6, 36.9,
             38.2, 37.9]

temp = np.array(temp_list)  # Create array temp, complete this line
heat  =temp[temp>37.3]  # Find fever data and add to array heat, complete this line
F_heat =heat*1.8+32 # Convert to Fahrenheit temperature and store in array F_heat, complete this line
F_heat1 =np.round(F_heat,1) # Keep 1 decimal place, complete this line

print(F_heat1)
