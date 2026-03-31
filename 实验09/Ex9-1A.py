import os
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "stats.csv")

data = pd.read_csv(input_file)
print(data)
weight = data["weight"]
area = data["BSA"]
plt.scatter(weight, area, c="red", s=5000, alpha=0.1)
plt.xlabel("Weight (kg)")
plt.ylabel("Body Surface Area (sq m)")
plt.show()