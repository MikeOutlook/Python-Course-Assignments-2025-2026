import numpy as np
import os

# Read CSV file (using relative path for github upload)

# 1. Get the directory where current script (Ex6-3B.py) is located
current_script_dir = os.path.dirname(__file__)

# 2. Get the parent directory of that folder: Project root Python-Course-Assignments-2025-2026
project_root = os.path.abspath(os.path.join(current_script_dir, ".."))

# 3. Construct the full path to patient_temperatures.csv in data_input folder
file_path = os.path.join(project_root, "data_input", "patient_temperatures.csv")

# 4. Print the path for debugging
print(f"Reading file: {file_path}")


data =np.loadtxt(file_path,
                 dtype=float,
                 delimiter=",",
                 skiprows=1)  # Complete this line

print(data)

print(data[0:10,0:2])

print(data[20:40,4:5])

print(data[50:75,1:4])

print(data[data>38.6])

print(data[data[:,6]>38.6])