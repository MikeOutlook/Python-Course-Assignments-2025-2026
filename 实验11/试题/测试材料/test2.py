#
#导入需要的库，将后续代码补充完整(共2行)
import os
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.unicode.east_asian_width", True) #本行代码为中文对齐修正
#matplotlib的中文字体显示修正，将本行代码补充完整
plt.rcParams["font.family"]=["SimHei"]
##1、数据获取

# 1. 定位当前脚本所在文件夹：测试材料
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 向上跳三级回到根目录 (测试材料 -> 试题 -> 实验11 -> 根目录)
# 修正：连续取三次 dirname
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))

# 3. 构建输入路径
input_file = os.path.join(project_root, "data_input", "guangdong.xlsx")

print(f"🔍 实际寻找的路径是: {input_file}")

DF2A =pd.read_excel(input_file,"population",usecols=[0,1]) #读取文件中数据到DF2A，将本行代码补充完整
DF2B =pd.read_excel(input_file,"health") #读取文件中数据到DF2B，将本行代码补充完整
##2、计算
DF2B["人均执业医师数"]=(DF2B["执业医师数"]/DF2A["常住人口"]*1000).round(2) #追加新列并计算，将本行代码补充完整
DF2B["人均注册护士数"]=(DF2B["注册护士数"]/DF2A["常住人口"]*1000).round(2)  #追加新列并计算，将本行代码补充完整
DF2C =DF2B[["年份","人均执业医师数","人均注册护士数"]]  #将需要的数据输出到DF2C，将本行代码补充完整
print(DF2C)
##3、针对DF2C的数据绘图
y1 =DF2B["人均执业医师数"]  #产生人均医师折线图纵坐标数据，将本行代码补充完整
y2 =DF2B["人均注册护士数"]  #产生人均注册护士条形图纵坐标数据，将本行代码补充完整
y3 =4.7-DF2B["人均注册护士数"]  #产生差额折线图纵坐标数据，将本行代码补充完整
x =list(range(y1.size))  #产生横坐标数据，将本行代码补充完整

plt.plot(x,y1,color="b",linewidth=3,marker="o",linestyle="--",label="人均执业医师数") #绘制人均医师折线图，将本行代码补充完整
plt.bar(x,y2,color="pink",edgecolor="purple",width=0.6,label="人均注册护士数") #绘制人均注册护士条形图，将本行代码补充完整
plt.plot(x,y3,color="r",linewidth=3,marker="*",linestyle=":",label="差额") #绘制差额折线图，将本行代码补充完整

plt.ylabel("人/千人") #设置纵轴标签，将本行代码补充完整
plt.ylim(1.0,3.5) #设置纵轴范围，将本行代码补充完整
xtick_list = ["2011年","2013年","2015年","2017年","2019年"]  #准备横轴刻度标签
plt.xticks([0,2,4,6,8],xtick_list) #设置横轴刻度，将本行代码补充完整
plt.legend() #设置图例，将本行代码补充完整
plt.show()
