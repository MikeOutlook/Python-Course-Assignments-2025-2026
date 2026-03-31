import os
import pandas as pd
# ==========================================
# Part 1: Project Path Auto-Location (Relative Path 1.0)
# ==========================================

# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "body_datas.csv")
output_file = os.path.join(project_root, "data_output", "result.xlsx")

print(f"Loading data from: {input_file}")

# ==========================================
# Part 2: Medical Data Cleaning and Index Calculation
# ==========================================

# [Step 1] Read CSV data and set 'id' column as index
df_body = pd.read_csv(input_file, index_col='id')

# [Step 2] Filter target population: age > 45 and weight > 70 kg
# Use .copy() to ensure subsequent calculations are done on a copy to avoid warnings
df_filtered = df_body[(df_body["age"] > 45) & (df_body["weight"] > 70)].copy()

# [Step 3] Calculate BMI index (formula: weight / height squared, height needs to be converted from cm to m)
df_filtered['BMI'] = df_filtered['weight'] / (df_filtered['height'] / 100) ** 2

# ==========================================
# Part 3: Filter Key Indicators and Export Results
# ==========================================

# [Step 4] Extract columns to display: age, weight, BMI, chest
result_table = df_filtered[["age", "weight", "BMI", "chest"]]

# [Step 5] Export to Excel file
# Set worksheet name to "body", keep index (id)
result_table.to_excel(output_file, sheet_name="body", index=True)

print(f"Processing complete! Results saved to: {output_file}")


# import os
# import pandas as pd

# # 1. Get the directory where current script (7-4-1.py) is located: Experiment 07
# current_script_dir = os.path.dirname(__file__)

# # 2. Get the parent directory of that folder: Project root Python-Course-Assignments-2025-2026
# project_root = os.path.abspath(os.path.join(current_script_dir, ".."))

# # 3. Construct the full path to data.csv in data_input folder
# file_path = os.path.join(project_root, "data_input", "body_datas.csv")
# output_path = os.path.join(project_root, "data_output", "result.xlsx")

# # 4. Print the path for debugging
# print(f"Reading file: {file_path}")

# DF_body=pd.read_csv(file_path,index_col='id')
# DFQ=DF_body[(DF_body["age"]>45) & (DF_body["weight"]>70)].copy()
# DFQ['BMI'] = DFQ['weight'] / (DFQ['height'] / 100) ** 2

# new=DFQ[["age","weight","BMI","chest"]]
# new.to_excel(output_path,sheet_name="body",startcol=0,index=True)   # Output excel file according to requirements, complete this line
