#导入需要的库，将本行代码补充完整
import pandas as pd
DF31 =pd.read_csv("checkup.csv",header=1) #按题目要求读取csv文件，将本行代码补充完整
DF32 =pd.read_excel("guangdong.xlsx",sheet_name="population",usecols=[0,2,3],engine="openpyxl") #按题目要求读取excel文件，将本行代码补充完整

DF31.to_excel("check.xlsx",sheet_name="answer",startcol=2,index=False)   #按题目要求输出excel文件，将本行代码补充完整
DF32.to_csv("gd.csv")   #按题目要求输出csv文件，将本行代码补充完整