# 导入模块
import pandas as pd
import matplotlib.pylab as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
# 加载数据， 文件类型为 xls；
data = pd.read_excel("time_cholesterol.xls")
print(data) #非必须代码， 观察数据结构
#读取样本（自变量） 和标签（因变量）
x=data["time"].values.reshape(-1,1)
y=data["cholesterol"].values.reshape(-1,1)
# 随机划分训练集和测试集， 其中测试集占 30%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
# 建立线性模型；
regr = linear_model.LinearRegression()
# 利用训练集训练模型；
regr.fit(x_train, y_train)
# 显示线性函数的回归系数与截距
a = regr.intercept_
b = regr.coef_
print("Coefficients: \n", b)
print("Intercept:\n", a)
# 获取测试集自变量的预测数据
y_pred = regr.predict(x_test)
# 显示均方误差
print("均方误差:", mean_squared_error(y_test, y_pred))
# 显示决定系数
print("决定系数: ", r2_score(y_test, y_pred))
# 绘制训练好的线性回归拟合直线；
plt.title("LinearRegression time-choles")
plt.xlabel("time")
plt.ylabel("choles")
plt.scatter(x_test, y_test, color="black")
plt.plot(x_test, y_pred, color="red", linewidth=3)
plt.show()
# 显示回归方程
print("choles= {}+ {}* time".format(a, b))