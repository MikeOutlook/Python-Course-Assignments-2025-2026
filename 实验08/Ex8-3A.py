# 步骤 1： 导入需要的库
import pandas as pd
import matplotlib.pyplot as plt
# 步骤 2： 数据准备
datas = pd.read_csv("GLU.csv")

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