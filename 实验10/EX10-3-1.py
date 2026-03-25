##、导入需要的库，将后续代码补充完整（不止一行）
import os
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.family"] = ["SimHei"] # 中文显示设置，将本行代码补充完整
##、获取数据


# 1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

# 3. 构建输入与输出的完整路径
input_file = os.path.join(project_root, "data_input", "Census.xlsx")


DF1 =pd.read_excel(input_file,"book1",index_col=0)   # 读取数据文件中的book工作表到DF1，将本行代码补充完整
DF2 =pd.read_excel(input_file,"education",index_col=0)   # 读取数据文件中的education工作表到DF2，将本行代码补充完整

y1 =DF1["illiterate"]/DF1["Population"]*100   # 计算文盲率，将本行代码补充完整
y2 =DF2["college"]/100000*100   # 取出各次普查大专人口数，折算为百分比，将本行代码补充完整
y3 =DF2["senior"]/100000*100   # 计算各次普查高中人口数，折算为百分比，将本行代码补充完整
y4 =DF2["junior"]/100000*100   # 计算各次普查初中人口数，折算为百分比，将本行代码补充完整
x = list(range(y1.size))
  #创建绘图对象，大小为10英寸*6英寸，将本行代码补充完整
## 绘图
plt.bar(x,y1,color="y",width=0.5,edgecolor="r",label="illiterate")  # 绘制文盲率条形图，将本行代码补充完整
plt.plot(x,y2,color="g",linestyle=":",linewidth=3,marker="o",label="college")  # 绘制大专人口率折线图，将本行代码补充完整
plt.plot(x,y3,color="b",linestyle=":",linewidth=2,marker="o",label="senior")  # 绘制高中人口率折线图，将本行代码补充完整
plt.plot(x,y4,color="m",linestyle=":",linewidth=2,marker="o",label="junior")  # 绘制初中人口率折线图，将本行代码补充完整
##外观设置
plt.title("历次普查受教育情况折线图")  # 设置标题，将本行代码补充完整
plt.xlabel("普查年份")  # 设置横轴标签，将本行代码补充完整
plt.ylabel("百分比")  # 设置纵轴标签，将本行代码补充完整
plt.ylim(0,55)  # 设置纵轴范围，将本行代码补充完整
plt.xticks(x,y1.index)  # 设置横轴刻度文字，将本行代码补充完整
plt.yticks(range(0,60,5))  # 设置纵轴刻度，将本行代码补充完整
plt.legend()  # 设置图例，将本行代码补充完整
plt.savefig("census.png")  # 保存文件，将本行代码补充完整
plt.show()