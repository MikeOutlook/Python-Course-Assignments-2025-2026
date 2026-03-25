import os
import pandas as pd
import matplotlib.pyplot as plt


# 1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

# 3. 构建输入与输出的完整路径
input_file = os.path.join(project_root, "data_input", "metabolism.csv")

data =pd.read_csv(input_file) #读取数据文件，将本行代码补充完整
x1 =data.iloc[0:12,1] #获取前12行横纵坐标数据，将本行代码补充完整
y1 =data.iloc[0:12,0] #获取前1行纵坐标数据，将本行代码补充完整
x2 =data.tail(8)["weight"] #获取后8行横坐标数据，将本行代码补充完整
y2 =data.tail(8)["BM"] #获取后8行纵坐标数据，将本行代码补充完整

plt.scatter(x1,y1,c="red",s=50,marker="D") #调用函数绘制前12行数据散点图，将本行代码补充完整
plt.scatter(x2,y2,c="blue",s=100,marker="p") #调用函数绘制前8行数据散点图，将本行代码补充完整

plt.savefig("j.png") #保存图形，将本行代码补充完整
plt.show() #显示图形，将本行代码补充完整