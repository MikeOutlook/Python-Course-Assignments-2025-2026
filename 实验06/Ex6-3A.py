# import numpy as np

# arr1 = np.loadtxt("data.csv", delimiter=",", skiprows=1,
#                   usecols=[0, 1], dtype=int,)
# print(arr1)

import numpy as np
import os

# 1. Get the directory where current script (Ex6-3A.py) is located: Experiment 06
current_script_dir = os.path.dirname(__file__)

# 2. Get the parent directory of that folder: Project root Python-Course-Assignments-2025-2026
project_root = os.path.abspath(os.path.join(current_script_dir, ".."))

# 3. Construct the full path to data.csv in data_input folder
file_path = os.path.join(project_root, "data_input", "data.csv")

# 4. Print the path for debugging
print(f"Reading file: {file_path}")

# 5. Load data
try:
    arr1 = np.loadtxt(file_path, delimiter=",", skiprows=1,
                      usecols=[0, 1], dtype=int)
    print("Read successfully! Data as follows:")
    print(arr1)
except Exception as e:
    print(f"Read failed, please check if file exists. Error: {e}")