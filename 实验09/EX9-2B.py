#1.导入需要的库，补充完整后续两行代码
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#2.中文字体显示修正，在下面填写正确的代码
plt.rcParams['font.family'] = ['SimHei']
#3.产生横纵坐标数据
DF_hospital =pd.read_csv("hospital.csv")       #读取数据文件到DF_hospital数据框，将本行代码补充完整
data_ratio =DF_hospital["Tertiary"]/DF_hospital["Total"]  #计算比率，将本行代码补充完整
x= np.arange(0,data_ratio.size)          #产生0到4的横坐标数据，将本行代码补充完整
barLabel = ["广东", "江苏", "山东","浙江", "河南"]
#4.调用函数绘制柱形图，补充完整后续代码
plt.bar(x, data_ratio, tick_label=barLabel,color="orange",width=0.6,edgecolor="b")
#5.图形展示
plt.show()
