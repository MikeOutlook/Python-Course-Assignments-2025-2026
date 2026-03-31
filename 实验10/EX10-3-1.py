## Import required libraries, complete subsequent code (more than one line)
import os
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.family"] = ["SimHei"] # Chinese display setting, complete this line
## Get data


# 1. Locate current script directory (e.g., Experiment 07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Locate project root directory (go up one level)
project_root = os.path.dirname(current_dir)

# 3. Construct full path for input and output
input_file = os.path.join(project_root, "data_input", "Census.xlsx")


DF1 =pd.read_excel(input_file,"book1",index_col=0)   # Read book worksheet from data file to DF1, complete this line
DF2 =pd.read_excel(input_file,"education",index_col=0)   # Read education worksheet from data file to DF2, complete this line

y1 =DF1["illiterate"]/DF1["Population"]*100   # Calculate illiteracy rate, complete this line
y2 =DF2["college"]/100000*100   # Extract college population from each census, convert to percentage, complete this line
y3 =DF2["senior"]/100000*100   # Calculate senior high school population from each census, convert to percentage, complete this line
y4 =DF2["junior"]/100000*100   # Calculate junior high school population from each census, convert to percentage, complete this line
x = list(range(y1.size))
  # Create plot object, size 10 inches * 6 inches, complete this line
## Draw chart
plt.bar(x,y1,color="y",width=0.5,edgecolor="r",label="illiterate")  # Draw illiteracy rate bar chart, complete this line
plt.plot(x,y2,color="g",linestyle=":",linewidth=3,marker="o",label="college")  # Draw college population rate line chart, complete this line
plt.plot(x,y3,color="b",linestyle=":",linewidth=2,marker="o",label="senior")  # Draw senior high school population rate line chart, complete this line
plt.plot(x,y4,color="m",linestyle=":",linewidth=2,marker="o",label="junior")  # Draw junior high school population rate line chart, complete this line
## Appearance settings
plt.title("Census Education Line Chart")  # Set title, complete this line
plt.xlabel("Census Year")  # Set x-axis label, complete this line
plt.ylabel("Percentage")  # Set y-axis label, complete this line
plt.ylim(0,55)  # Set y-axis range, complete this line
plt.xticks(x,y1.index)  # Set x-axis tick labels, complete this line
plt.yticks(range(0,60,5))  # Set y-axis ticks, complete this line
plt.legend()  # Set legend, complete this line
plt.savefig("census.png")  # Save file, complete this line
plt.show()
