#1. Import required libraries, complete the next two lines
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#2. Chinese font display correction, fill in the correct code below
plt.rcParams['font.family'] = ['SimHei']

# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "hospital.csv")

#3. Generate x and y coordinate data
DF_hospital =pd.read_csv(input_file)       # Read data file to DF_hospital dataframe, complete this line
data_ratio =DF_hospital["Tertiary"]/DF_hospital["Total"]  # Calculate ratio, complete this line
x= np.arange(0,data_ratio.size)          # Generate x-axis data from 0 to 4, complete this line
barLabel = ["Guangdong", "Jiangsu", "Shandong","Zhejiang", "Henan"]
#4. Call function to draw bar chart, complete subsequent code
plt.bar(x, data_ratio, tick_label=barLabel,color="orange",width=0.6,edgecolor="b")
#5. Display graph
plt.show()
