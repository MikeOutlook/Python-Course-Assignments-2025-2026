import pandas as pd
import os

##1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

## 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

## 3. Construct full path for input and output
birthwt = os.path.join(project_root, "data_input", "birthwt.csv")

DF_bw = pd.read_csv(birthwt,index_col=0)
#1 View dataset
print(DF_bw.columns)  # Display all column labels, complete code inside print
print(DF_bw.shape)  # Display row and column count, complete code inside print
#2 Column view
print(DF_bw["age"])   # Display age data, complete code inside print
print(DF_bw[["ptl","ftv"]])  # Display miscarriage times and birth times data, complete code inside print
#3 Special row view
print(DF_bw.tail())  # Display last 5 rows, complete code inside print
print(DF_bw.head(10))  # Display first 10 rows, complete code inside print
#4 iloc method
print(DF_bw.iloc[3:10,7])  # Display rows 4-10, column 8 data, complete code inside print
print(DF_bw.iloc[20:30,[4,7]])  # From row 21, get 10 rows of columns 5 and 8, complete code inside print
#5 loc method
print(DF_bw.loc[47,["age","bwt"]])  # Display row label 47, columns age and newborn weight data, complete code inside print
#6 Conditional view
print(DF_bw[(DF_bw["age"] < 18) & (DF_bw["smoke"] == "YES")]) # Display data where age < 18 and has smoking history, complete code inside print
