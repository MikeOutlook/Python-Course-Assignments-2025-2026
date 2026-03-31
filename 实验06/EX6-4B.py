import numpy as np

height_list = [1.68, 1.81, 1.76, 1.68, 1.73, 1.72, 1.74]
weight_list = [185.2, 169.4, 143.7, 191.8, 172.6, 124.1, 153.5]

height =np.array(height_list)  # Create array from height list, complete this line
weight =np.array(weight_list,dtype=int)  # Create array from weight list, integer type, complete this line

weight_kg =weight*0.454   # Convert weight from pounds to kilograms, complete this line


BMI =weight_kg/(height**2)  # Calculate BMI according to formula, complete this line

BMI2 =np.round(BMI,2)   # Keep BMI value to 2 decimal places, complete this line

BMI3 =BMI2[(BMI2>18.5) & (BMI2<24)]   # Find BMI values in normal range, complete this line

print("Patient BMI data:\n",BMI2)
print("Normal BMI values:\n",BMI3)


