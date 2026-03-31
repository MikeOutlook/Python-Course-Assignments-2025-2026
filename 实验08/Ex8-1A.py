import os
import pandas as pd

# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "Diabetes.csv")

DF1 = pd.read_csv(input_file,index_col=0)
DF2 = DF1.iloc[:6, :5]
print(DF2)
# Use index for simple calculation
DF2["Glucose"] = (DF2["Glucose"] / 18).round(1)
# Use eval function for calculation
DF2.eval("BMI=Weight/(Height/100)**2", inplace=True)
print(DF2)



