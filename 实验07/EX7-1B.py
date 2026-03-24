import pandas as pd
DF_bw = pd.read_csv("birthwt.csv",index_col=0)
#1 查看数据集
print(DF_bw.columns)  # 显示所有的列标签名称，将print括号内的代码补充完整
print(DF_bw.shape)  # 显示行列数，将print括号内的代码补充完整
#2 列查看
print(DF_bw["age"])   # 显示年龄数据，将print括号内的代码补充完整
print(DF_bw[["ptl","ftv"]])  # 显示流产次数和生产次数数据，将print括号内的代码补充完整
#3 特殊行查看
print(DF_bw.tail())  # 显示最后5行数据，将print括号内的代码补充完整
print(DF_bw.head(10))  # 显示前10行数据，将print括号内的代码补充完整
#4 iloc方法
print(DF_bw.iloc[3:10,7])  #显示第4到10行的第8列数据，将print括号内的代码补充完整
print(DF_bw.iloc[20:30,[4,7]])  #从第21行开始，取出10行第5列和第8列数据，将print括号内的代码补充完整
#5 loc方法
print(DF_bw.loc[47,["age","bwt"]])  # 显示行标签名称为47，列标签为年龄和新生儿体重的数据，将print括号内的代码补充完整
#6 按条件查看
print(DF_bw[["age"]<18 and ["smoke"]=="YES"]) # 显示年龄小于18并且有吸烟史的数据，将print括号内的代码补充完整

