# Step 1: Import required libraries
import os
import pandas as pd # Import pandas, complete this line
import matplotlib.pyplot as plt   # Import plotting library, complete this line
# Step 2: Global settings

# Chinese display setting, complete this line
plt.rcParams["font.family"] = ["SimHei"]

# Step 3: Data preparation

# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "AIDS_data.csv")

datas = pd.read_csv(input_file,encoding="GBK") # Read data file to datas dataframe
y1 =datas["发病数"].values # Extract "发病数" column data, complete this line
y2 =datas["既往感染者转为病人"].values # Extract "既往感染者转为病人" column data, complete this line
y3 =datas["死亡数"].values # Extract "死亡数" column data, complete this line
x =list(range(6)) # Generate x-axis data, complete this line
# 5: Call function to plot
plt.figure(figsize=(9,7))
plt.plot(x,y1,"r-s") # Plot first line, complete this line
plt.plot(x,y2,"b-o") # Plot second line, complete this line
plt.plot(x,y3,"m:D") # Plot third line, complete this line
# 7: Display graph

plt.show()
