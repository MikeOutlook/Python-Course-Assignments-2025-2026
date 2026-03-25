import os
import pandas as pd

# 1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

# 3. 构建输入与输出的完整路径
input_file = os.path.join(project_root, "data_input", "Diabetes.csv")

DF1 = pd.read_csv(input_file,index_col=0)
DF2 = DF1.iloc[:6, :5]
print(DF2)
# 使用索引进行简单计算
DF2["Glucose"] = (DF2["Glucose"] / 18).round(1)
# 使用 eval 函数进行计算
DF2.eval("BMI=Weight/(Height/100)**2", inplace=True)
print(DF2)



