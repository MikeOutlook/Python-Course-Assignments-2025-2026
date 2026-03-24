import pandas as pd

DF_body=pd.read_csv("body_datas.csv",index_col='id')
DFQ=DF_body[(DF_body["age"]>45) & (DF_body["weight"]>70)].copy()
DFQ['BMI'] = DFQ['weight'] / (DFQ['height'] / 100) ** 2

new=DFQ[["age","weight","BMI","chest"]]
new.to_excel("result.xlsx",sheet_name="body",startcol=0,index=True)   #按题目要求输出excel文件，将本行代码补充完整