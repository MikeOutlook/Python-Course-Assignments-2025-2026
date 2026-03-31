import os
import pandas as pd
import matplotlib.pyplot as plt


# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "metabolism.csv")

data =pd.read_csv(input_file) # Read data file, complete this line
x1 =data.iloc[0:12,1] # Get first 12 rows x-y coordinate data, complete this line
y1 =data.iloc[0:12,0] # Get first 12 rows y coordinate data, complete this line
x2 =data.tail(8)["weight"] # Get last 8 rows x coordinate data, complete this line
y2 =data.tail(8)["BM"] # Get last 8 rows y coordinate data, complete this line

plt.scatter(x1,y1,c="red",s=50,marker="D") # Call function to plot scatter for first 12 rows, complete this line
plt.scatter(x2,y2,c="blue",s=100,marker="p") # Call function to plot scatter for first 8 rows, complete this line

plt.savefig("j.png") # Save figure, complete this line
plt.show() # Display figure, complete this line