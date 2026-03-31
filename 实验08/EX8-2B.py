import os
import pandas as pd


# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "info.xlsx")
output_file = os.path.join(project_root, "data_output", "result.xlsx")


DF_check =pd.read_excel(input_file,"checkup",header=1,index_col=0,usecols=[0,2,4,5]) # 1. Read required data, complete this line

DF_check.eval('weight_kg=weight/2.204',inplace=True)  # 2. Convert weight, complete this line
DF_check["temp"]=((DF_check["temp"]-32)/1.8).round(1) # 3. Convert temperature, complete this line
DF_check["country"].replace("EN","UK",inplace=True)  # 4. Complete replacement operation, complete this line
DF_check.sort_values(["temp","weight"],ascending=[True,False],inplace=True)  # 5. Complete sorting operation, complete this line

#DFout =DF_check[(DF_check["country"]=="US")|(DF_check["temp"]>37.3)]  # 6. Filter required data, complete this line
DFout =DF_check.query("(country=='US') or (temp>37.3)")

DFout.to_excel(output_file,sheet_name="test",startcol=2)   # 7. Write DFout to excel file, complete this line

