import pandas as pd  # Import pandas library, complete this line
import os

##1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

## 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

## 3. Construct full path for input and output
Diabetes = os.path.join(project_root, "data_input", "Diabetes.csv")

# 1 Read data file to DF1, note difference from numpy
DF1=pd.read_csv(Diabetes,index_col=0) # Complete the code on the right side of assignment
print("Display original data:\n",DF1)
# 2 Get single or multiple columns by column label
print("Display age data")
print(DF1["Age"])   # Complete the code inside print
print("Display gender and smoking data")
print(DF1[["Gender","Smoking"]])   # Complete the code inside print
# 3 Get single or multiple rows by row index slice
print("Display row 5 data")
print(DF1.iloc[4:5,:])   # Complete the code inside print
print("Display rows 11 to 15 data")
print(DF1[10:15])   # Complete the code inside print
# 4 Use head and tail methods
print("Display first 5 rows")
print(DF1.head())   # Complete the code inside print
print("Display first 7 rows")
print(DF1.head(7))   # Complete the code inside print
print("Display last 8 rows")
print(DF1.tail(8))   # Complete the code inside print
# 5 Use iloc method for row/column slicing by index position
print("Display rows 5-8, column 4 data")
print(DF1.iloc[4:8,3])   # Complete the code inside print
print("Display first 10 rows, columns 3 and 6 data")
print(DF1.iloc[:10,[2,5]])   # Complete the code inside print
# 6 Use loc method for row/column slicing by index name
print("Display height and weight data for VIP01 row")
print(DF1.loc["VIP01",["Height","Weight"]])   # Complete the code inside print
print("Display hypertension, type, age data for rows A01, B01, C01")
print(DF1.loc[["A01","B01","C01"],["HTN","Type","Age"]])   # Complete the code inside print
# 7 Get data satisfying conditions by boolean indexing
print("Display all data where gender is Male")
print(DF1[DF1["Gender"]=="Male"])   # Complete the code inside print
