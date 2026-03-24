import pandas as pd
import matplotlib.pyplot as plt

data =pd.read_csv("metabolism.csv") #读取数据文件，将本行代码补充完整
x1 =data.iloc[0:12,1] #获取前12行横纵坐标数据，将本行代码补充完整
y1 =data.iloc[0:12,0] #获取前1行纵坐标数据，将本行代码补充完整
x2 =data.tail(8)["weight"] #获取后8行横坐标数据，将本行代码补充完整
y2 =data.tail(8)["BM"] #获取后8行纵坐标数据，将本行代码补充完整

plt.scatter(x1,y1,c="red",s=50,marker="D") #调用函数绘制前12行数据散点图，将本行代码补充完整
plt.scatter(x2,y2,c="blue",s=100,marker="p") #调用函数绘制前8行数据散点图，将本行代码补充完整

plt.savefig("j.png") #保存图形，将本行代码补充完整
plt.show() #显示图形，将本行代码补充完整