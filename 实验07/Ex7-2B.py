import os
import pandas as pd
#下行代码为东亚文字显示对齐设置
pd.set_option("display.unicode.east_asian_width", True) 

##1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

## 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

## 3. 构建输入与输出的完整路径
birthwt = os.path.join(project_root, "data_input", "score.csv")

DF_score = pd.read_csv(birthwt,index_col=0) # (1) 读取数据文件
print("原始数据：\n",DF_score)

DF_score.drop(index="赵云",inplace=True) #删除某行数据，将本行代码补充完整
DF_score.loc["吕布"]=[52,63,64,55,53] #追加一行数据，将本行代码补充完整
newScore = ["良","中","差","优","优","良","优","中","优"]
DF_score.insert(3,'体育',newScore)  #插入新列，新列数据为newScore列表，将本行代码补充完整
print("修改后数据：\n", DF_score)

DFnew =DF_score.query("数学>90 and 体育!='差'")  #筛选出需要的数据，将本行代码补充完整
print(DFnew)
