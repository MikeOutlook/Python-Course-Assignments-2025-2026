## Import required libraries, complete subsequent code (more than one line)
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.family'] = ['SimHei']# Chinese display setting, complete this line


# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "census.xlsx")

## Get data
DF1 =pd.read_excel(input_file,"book1",header=0,index_col=0,usecols=[0,1,2])   # Read book worksheet from data file to DF1, complete this line
DF2 =pd.read_excel(input_file,"education",header=0,index_col=0,usecols=[0,1,2,3,4,5])  # Read education worksheet from data file to DF2, complete this line
y1 =DF1["illiterate"]/DF1["Population"]*100   # Calculate illiteracy rate, complete this line
y2 =DF2["college"]/1000   # Convert college population from each census to percentage, complete this line
y3 =DF2["senior"]/1000   # Convert senior high school population from each census to percentage, complete this line
y4 =DF2["junior"]/1000   # Convert junior high school population from each census to percentage, complete this line
x = list(range(y1.size))
  # Create plot object, size 10 inches * 6 inches, complete this line
plt.figure(figsize=(8,4))
## Draw line chart
plt.plot(x,y1,c="r",linewidth=3,marker="o")  # Draw illiteracy rate line chart, complete this line
plt.plot(x,y2,c="g",linewidth=3,linestyle=":",marker="o")    # Draw college population rate line chart, complete this line
plt.plot(x,y3,c="g",linewidth=3,linestyle=":",marker="o")  # Draw senior high school population rate line chart, complete this line
plt.plot(x,y4,c="m",linewidth=3,linestyle=":",marker="o")  # Draw junior high school population rate line chart, complete this line
plt.title("Line Chart")  # Set title, complete this line
plt.show()
