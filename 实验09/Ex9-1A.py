import os
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

# 1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

# 3. 构建输入与输出的完整路径
input_file = os.path.join(project_root, "data_input", "stats.csv")

data = pd.read_csv(input_file)
print(data)
weight = data["weight"]
area = data["BSA"]
plt.scatter(weight, area, c="red", s=5000, alpha=0.1)
plt.xlabel("体重(公斤)")
plt.ylabel("体表面积(平方米)")
plt.show()