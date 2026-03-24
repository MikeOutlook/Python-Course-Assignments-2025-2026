import pandas as pd
#下行代码为东亚文字显示对齐设置
pd.set_option("display.unicode.east_asian_width", True) 

DF_score = pd.read_csv("score.csv",index_col=0) # (1) 读取数据文件
print("原始数据：\n",DF_score)

DF_score.drop(index="赵云",inplace=True) #删除某行数据，将本行代码补充完整
DF_score.loc["吕布"]=[52,63,64,55,53] #追加一行数据，将本行代码补充完整
newScore = ["良","中","差","优","优","良","优","中","优"]
DF_score.insert(3,'体育',newScore)  #插入新列，新列数据为newScore列表，将本行代码补充完整
print("修改后数据：\n", DF_score)

DFnew =DF_score.query("数学>90 and 体育!='差'")  #筛选出需要的数据，将本行代码补充完整
print(DFnew)
