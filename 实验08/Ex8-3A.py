# 步骤 1： 导入需要的库
import os
import pandas as pd
import matplotlib.pyplot as plt
# 步骤 2： 数据准备

# 1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

# 3. 构建输入与输出的完整路径
input_file = os.path.join(project_root, "data_input", "GLU.csv")


datas = pd.read_csv(input_file)

x = datas["order"].values
y = datas["blood_glucose"].values
# 步骤 3： 中文显示修正
plt.rcParams["font.family"] = ["SimHei"]
# 步骤 4： 创建绘图对象
plt.figure(figsize=(10, 4))
# 步骤 5： 调用相关绘图函数
plt.plot(x, y)
# 步骤 6： 外观设置
plt.title('24 小时血糖变化图')
plt.xlabel('测量次数')
plt.ylabel('测量结果（mmol/L） ')
# 步骤 7： 结果输出
plt.show()