# Import required libraries, complete this line
import os
import pandas as pd

##1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

## 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

## 3. Construct full path for input and output
checkup = os.path.join(project_root, "data_input", "checkup.csv")
guangdong = os.path.join(project_root, "data_input", "guangdong.xlsx")
output_file = os.path.join(project_root, "data_output", "check.xlsx")
output_file2 = os.path.join(project_root, "data_output", "gd.csv")

DF31 =pd.read_csv(checkup,header=1) # Read csv file according to requirements, complete this line
DF32 =pd.read_excel(guangdong,sheet_name="population",usecols=[0,2,3]) # Read excel file according to requirements, complete this line

DF31.to_excel(output_file,sheet_name="answer",startcol=2,index=False)   # Output excel file according to requirements, complete this line
DF32.to_csv(output_file2,index=False)   # Output csv file according to requirements, complete this line
