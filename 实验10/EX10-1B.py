# 导入模块，将后续代码补充完整
import pandas as pd
import matplotlib.pylab as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 加载数据，文件类型为CSV
data =pd.read_csv("brain_weight_new.csv") #读取数据文件，讲本行代码补充完整
print(data)  #非必须代码，观察数据结构
#读取样本（自变量）和标签（因变量），将后续代码补充完整
x=data["Head_Size"].values.reshape(-1,1)
y=data["Brain_Weight"].values.reshape(-1,1)
# 随机划分训练集和测试集，其中测试集占30%，将后续代码补充完整
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
# 建立线性模型，将后续代码补充完整
regr=linear_model.LinearRegression()
# 利用训练集训练模型，将后续代码补充完整
regr.fit(x_train,y_train)
# 显示线性函数的回归系数与截距，按要求补充后续代码
a =regr.intercept_  # 获取截距，将本行代码补充完整
b =regr.coef_  # 获取回归系数，将本行代码补充完整
print("Coefficients: \n", b) #显示回归系数，将括号内代码补充完整
print("Intercept:\n", a)     #显示截距，将括号内代码补充完整
# 获取测试集自变量的预测数据，将后续代码补充完整
y_pred=regr.predict(x_test)
# 显示均方误差，将后续括号内代码补充完整
print("均方误差:",mean_squared_error(y_test,y_pred))
# 显示决定系数，将后续括号内代码补充完整
print("决定系数: ",r2_score(y_test,y_pred))
# 绘制训练好的线性回归拟合直线，将后续代码补充完整
# 包括绘制测试集数据散点图、最佳拟合线、标题、横轴标签、纵轴标签
plt.title("脑重量预测")
plt.xlabel("头脑尺寸")
plt.ylabel("大脑重量")
plt.scatter(x_test, y_test, color="black")
plt.plot(x_test, y_pred, color="blue", linewidth=3)
plt.show()
# 显示回归方程，将后续代码补充完整
print("Brain_Weight={}+{}*Head_Size".format(a,b))

