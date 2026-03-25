import os
import pandas as pd


# 1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

# 3. 构建输入与输出的完整路径
input_file = os.path.join(project_root, "data_input", "info.xlsx")
output_file = os.path.join(project_root, "data_output", "result.xlsx")


DF_check =pd.read_excel(input_file,"checkup",header=1,index_col=0,usecols=[0,2,4,5]) # 1.读取需要的数据，将本行代码补充完整

DF_check.eval('weight_kg=weight/2.204',inplace=True)  # 2.换算体重，将本行代码补充完整
DF_check["temp"]=((DF_check["temp"]-32)/1.8).round(1) # 3.换算体温，将本行代码补充完整
DF_check["country"].replace("EN","UK",inplace=True)  # 4.完成替换操作，将本行代码补充完整
DF_check.sort_values(["temp","weight"],ascending=[True,False],inplace=True)  # 5.完成排序操作，将本行代码补充完整

#DFout =DF_check[(DF_check["country"]=="US")|(DF_check["temp"]>37.3)]  # 6.筛选出需要的数据，将本行代码补充完整
DFout =DF_check.query("(country=='US') or (temp>37.3)")

DFout.to_excel(output_file,sheet_name="test",startcol=2)   # 7.将DFout写入到excel文件，将本行代码补充完整

