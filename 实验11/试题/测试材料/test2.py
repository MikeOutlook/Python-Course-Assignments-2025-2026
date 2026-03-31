#
# Import required libraries, complete subsequent code (2 lines in total)
import os
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.unicode.east_asian_width", True) # This line is for Chinese alignment correction
# matplotlib Chinese font display correction, complete this line
plt.rcParams["font.family"]=["SimHei"]
##1. Data acquisition

# 1. Locate current script directory: Test Materials
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go up three levels to return to root directory (Test Materials -> Questions -> Experiment 11 -> Root)
# Correction: Get dirname three times in a row
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))

# 3. Construct input path
input_file = os.path.join(project_root, "data_input", "guangdong.xlsx")

print(f"Actual path being looked for: {input_file}")

DF2A =pd.read_excel(input_file,"population",usecols=[0,1]) # Read data from file to DF2A, complete this line
DF2B =pd.read_excel(input_file,"health") # Read data from file to DF2B, complete this line
##2. Calculation
DF2B["人均执业医师数"]=(DF2B["执业医师数"]/DF2A["常住人口"]*1000).round(2) # Add new column and calculate, complete this line
DF2B["人均注册护士数"]=(DF2B["注册护士数"]/DF2A["常住人口"]*1000).round(2)  # Add new column and calculate, complete this line
DF2C =DF2B[["年份","人均执业医师数","人均注册护士数"]]  # Output required data to DF2C, complete this line
print(DF2C)
##3. Draw chart for DF2C data
y1 =DF2B["人均执业医师数"]  # Generate y-axis data for per capita physicians line chart, complete this line
y2 =DF2B["人均注册护士数"]  # Generate y-axis data for per capita registered nurses bar chart, complete this line
y3 =4.7-DF2B["人均注册护士数"]  # Generate y-axis data for difference line chart, complete this line
x =list(range(y1.size))  # Generate x-axis data, complete this line

plt.plot(x,y1,color="b",linewidth=3,marker="o",linestyle="--",label="Per Capita Physicians") # Draw per capita physicians line chart, complete this line
plt.bar(x,y2,color="pink",edgecolor="purple",width=0.6,label="Per Capita Registered Nurses") # Draw per capita registered nurses bar chart, complete this line
plt.plot(x,y3,color="r",linewidth=3,marker="*",linestyle=":",label="Difference") # Draw difference line chart, complete this line

plt.ylabel("Per 1000 people") # Set y-axis label, complete this line
plt.ylim(1.0,3.5) # Set y-axis range, complete this line
xtick_list = ["2011","2013","2015","2017","2019"]  # Prepare x-axis tick labels
plt.xticks([0,2,4,6,8],xtick_list) # Set x-axis ticks, complete this line
plt.legend() # Set legend, complete this line
plt.show()
