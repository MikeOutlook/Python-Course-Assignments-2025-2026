# 步骤1：导入需要的库
import os
import pandas as pd  #导入pandas，将本行代码补充完整
import matplotlib.pyplot as plt   #导入绘图库，将本行代码补充完整
# 步骤2：全局设置

#中文显示设置，将本行代码补充完整
plt.rcParams["font.family"] = ["SimHei"]

# 步骤3：数据准备

# 1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

# 3. 构建输入与输出的完整路径
input_file = os.path.join(project_root, "data_input", "AIDS_data.csv")

datas = pd.read_csv(input_file,encoding="GBK") #读取数据文件到datas数据框
y1 =datas["发病数"].values #取出"发病数"列数据，将本行代码补充完整
y2 =datas["既往感染者转为病人"].values #取出"既往感染者转为病人"列数据，将本行代码补充完整
y3 =datas["死亡数"].values #取出"死亡数"列数据，将本行代码补充完整
x =list(range(6)) #产生横坐标数据，将本行代码补充完整
#5、调用函数绘图
plt.figure(figsize=(9,7))
plt.plot(x,y1,"r-s") #绘制第1条线，将本行代码补充完整
plt.plot(x,y2,"b-o") #绘制第2条线，将本行代码补充完整
plt.plot(x,y3,"m:D") #绘制第3条线，将本行代码补充完整
#7、图形展示

plt.show()
