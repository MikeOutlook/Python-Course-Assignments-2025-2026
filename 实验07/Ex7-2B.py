import os
import pandas as pd
# Below code is for East Asian text display alignment
pd.set_option("display.unicode.east_asian_width", True)

##1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

## 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

## 3. Construct full path for input and output
birthwt = os.path.join(project_root, "data_input", "score.csv")

DF_score = pd.read_csv(birthwt,index_col=0) # (1) Read data file
print("Original data:\n",DF_score)

DF_score.drop(index="Zhao Yun",inplace=True) # Delete a row, complete this line
DF_score.loc["Lu Bu"]=[52,63,64,55,53] # Add a row, complete this line
newScore = ["Good","Medium","Poor","Excellent","Excellent","Good","Excellent","Medium","Excellent"]
DF_score.insert(3,'PE',newScore)  # Insert new column, new column data is newScore list, complete this line
print("Modified data:\n", DF_score)

DFnew =DF_score.query("Math>90 and PE!='Poor'")  # Filter required data, complete this line
print(DFnew)
