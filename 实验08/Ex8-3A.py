# Step 1: Import required libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
# Step 2: Data preparation

# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "GLU.csv")


datas = pd.read_csv(input_file)

x = datas["order"].values
y = datas["blood_glucose"].values
# Step 3: Chinese display correction
plt.rcParams["font.family"] = ["SimHei"]
# Step 4: Create plot object
plt.figure(figsize=(10, 4))
# Step 5: Call related plotting functions
plt.plot(x, y)
# Step 6: Appearance settings
plt.title('24 Hour Blood Glucose Change Chart')
plt.xlabel('Measurement Count')
plt.ylabel('Measurement Result (mmol/L)')
# Step 7: Output result
plt.show()