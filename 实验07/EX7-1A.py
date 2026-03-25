import pandas as pd  #导入pandas库，将本行代码补充完整
import os

##1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

## 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

## 3. 构建输入与输出的完整路径
Diabetes = os.path.join(project_root, "data_input", "Diabetes.csv")

# 1 读取数据文件到DF1，注意和numpy的区别
DF1=pd.read_csv(Diabetes,index_col=0) # 将赋值号右侧的代码补充完整
print("显示原始数据：\n",DF1)
# 2 通过列标签获取单列或多列
print("显示年龄数据")
print(DF1["Age"])   # 将print括号内的代码补充完整
print("显示性别和抽烟数据")
print(DF1[["Gender","Smoking"]])   # 将print括号内的代码补充完整
# 3 通过行索引位置的切片形式获取单行或多行
print("显示第5行数据")
print(DF1.iloc[4:5,:])   # 将print括号内的代码补充完整
print("显示第11行到第15行的数据")
print(DF1[10:15])   # 将print括号内的代码补充完整
# 4 使用head和tail方法
print("显示前5行")
print(DF1.head())   # 将print括号内的代码补充完整
print("显示前7行")
print(DF1.head(7))   # 将print括号内的代码补充完整
print("显示最后8行")
print(DF1.tail(8))   # 将print括号内的代码补充完整
# 5 使用iloc方法通过索引位置序号做行列切片
print("显示第5到8行的第4列数据")
print(DF1.iloc[4:8,3])   # 将print括号内的代码补充完整
print("显示前10行的第3列和第6列数据")
print(DF1.iloc[:10,[2,5]])   # 将print括号内的代码补充完整
# 6使用loc方法通过索引名称序号做行列切片
print("显示VIP01行的身高和体重数据")
print(DF1.loc["VIP01",["Height","Weight"]])   # 将print括号内的代码补充完整
print("显示A01,B01,C01三行的高血压、类型、年龄数据")
print(DF1.loc[["A01","B01","C01"],["HTN","Type","Age"]])   # 将print括号内的代码补充完整
# 7 通过布尔索引方式获取满足条件的数据
print("显示性别为男性的所有数据")
print(DF1[DF1["Gender"]=="Male"])   # 将print括号内的代码补充完整