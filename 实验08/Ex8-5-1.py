# 步骤1：导入需要的库
import pandas as pd  #导入pandas，将本行代码补充完整
import matplotlib.pyplot as plt   #导入绘图库，将本行代码补充完整
DF3=pd.read_csv("boay_datas.csv",index_col=0)

age_mean=DF3["age"].mean().round(2)
print("年龄的均值是:",age_mean)
print("臀围的标准差是：",DF3["bip"].std().round(2))

DF3Q=DF3.query("age>45 and weight>70")
DF3Q.eval("BMI=weight/(height/100)**2",inplace=True)

r,p=