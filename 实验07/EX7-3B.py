#导入需要的库，将本行代码补充完整
import os
import pandas as pd

##1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

## 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

## 3. 构建输入与输出的完整路径
checkup = os.path.join(project_root, "data_input", "checkup.csv")
guangdong = os.path.join(project_root, "data_input", "guangdong.xlsx")
output_file = os.path.join(project_root, "data_output", "check.xlsx")
output_file2 = os.path.join(project_root, "data_output", "gd.csv")

DF31 =pd.read_csv(checkup,header=1) #按题目要求读取csv文件，将本行代码补充完整
DF32 =pd.read_excel(guangdong,sheet_name="population",usecols=[0,2,3]) #按题目要求读取excel文件，将本行代码补充完整

DF31.to_excel(output_file,sheet_name="answer",startcol=2,index=False)   #按题目要求输出excel文件，将本行代码补充完整
DF32.to_csv(output_file2,index=False)   #按题目要求输出csv文件，将本行代码补充完整