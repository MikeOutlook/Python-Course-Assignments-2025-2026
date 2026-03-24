import pandas as pd
DF1 = pd.read_csv("Diabetes.csv",index_col=0)
DF2 = DF1.iloc[:6, :5]
print(DF2)
# 使用索引进行简单计算
DF2["Glucose"] = (DF2["Glucose"] / 18).round(1)
# 使用 eval 函数进行计算
DF2.eval("BMI=Weight/(Height/100)**2", inplace=True)
print(DF2)



