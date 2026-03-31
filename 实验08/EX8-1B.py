import os
import pandas as pd # Import pandas, complete this line

# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "Diabetes.csv")


DF1 =pd.read_csv(input_file,index_col=0)   # Read data file, complete this line
DF1.eval("Glucose=Glucose/18",inplace=True)  # Use eval function for calculation, complete this line
DF1["BSA"]=((DF1["Height"]*DF1["Weight"]/3600)**0.5).round(2)   # Add new column, use column index for simple calculation, complete this line

print(DF1)