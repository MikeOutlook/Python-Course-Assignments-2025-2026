##、导入需要的库，将后续代码补充完整（不止一行）
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.family'] = ['SimHei']# 中文显示设置，将本行代码补充完整


# 1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

# 3. 构建输入与输出的完整路径
input_file = os.path.join(project_root, "data_input", "census.xlsx")

##、获取数据
DF1 =pd.read_excel(input_file,"book1",header=0,index_col=0,usecols=[0,1,2])   # 读取数据文件中的book工作表到DF1，将本行代码补充完整
DF2 =pd.read_excel(input_file,"education",header=0,index_col=0,usecols=[0,1,2,3,4,5])  # 读取数据文件中的education工作表到DF2，将本行代码补充完整
y1 =DF1["illiterate"]/DF1["Population"]*100   # 计算文盲率，将本行代码补充完整
y2 =DF2["college"]/1000   # 将各次普查大专人口折算为百分比，将本行代码补充完整
y3 =DF2["senior"]/1000   # 将各次普查高中人口折算为百分比，将本行代码补充完整
y4 =DF2["junior"]/1000   # 将各次普查初中人口折算为百分比，将本行代码补充完整
x = list(range(y1.size))
  #创建绘图对象，大小为10英寸*6英寸，将本行代码补充完整
plt.figure(figsize=(8,4))
## 绘制折线图
plt.plot(x,y1,c="r",linewidth=3,marker="o")  #绘制文盲率折线图，将本行代码补充完整
plt.plot(x,y2,c="g",linewidth=3,linestyle=":",marker="o")    # 绘制大专人口率折线图，将本行代码补充完整
plt.plot(x,y3,c="g",linewidth=3,linestyle=":",marker="o")  # 绘制高中人口率折线图，将本行代码补充完整
plt.plot(x,y4,c="m",linewidth=3,linestyle=":",marker="o")  # 绘制初中人口率折线图，将本行代码补充完整
plt.title("折线图")  # 设置标题，将本行代码补充完整
plt.show()
