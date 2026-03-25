#1.导入需要的库，补充完整后续两行代码
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#2.中文字体显示修正，在下面填写正确的代码
plt.rcParams['font.family'] = ['SimHei']

# 1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

# 3. 构建输入与输出的完整路径
input_file = os.path.join(project_root, "data_input", "hospital.csv")

#3.产生横纵坐标数据
DF_hospital =pd.read_csv(input_file)       #读取数据文件到DF_hospital数据框，将本行代码补充完整
data_ratio =DF_hospital["Tertiary"]/DF_hospital["Total"]  #计算比率，将本行代码补充完整
x= np.arange(0,data_ratio.size)          #产生0到4的横坐标数据，将本行代码补充完整
barLabel = ["广东", "江苏", "山东","浙江", "河南"]
#4.调用函数绘制柱形图，补充完整后续代码
plt.bar(x, data_ratio, tick_label=barLabel,color="orange",width=0.6,edgecolor="b")
#5.图形展示
plt.show()
