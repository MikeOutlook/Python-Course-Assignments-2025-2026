import os
import pandas as pd

# 1. 获取当前脚本 (7-4-1.py) 所在的文件夹：实验07
current_script_dir = os.path.dirname(__file__)

# 2. 获取该文件夹的上一级目录：即项目根目录 Python-Course-Assignments-2025-2026
project_root = os.path.abspath(os.path.join(current_script_dir, ".."))

# 3. 拼接出 data_input 文件夹下 data.csv 的完整路径
file_path = os.path.join(project_root, "data_input", "body_datas.csv")
output_path = os.path.join(project_root, "data_output", "result.xlsx")

# 4. 打印一下路径，方便你调试检查
print(f"正在读取文件: {file_path}")

DF_body=pd.read_csv(file_path,index_col='id')
DFQ=DF_body[(DF_body["age"]>45) & (DF_body["weight"]>70)].copy()
DFQ['BMI'] = DFQ['weight'] / (DFQ['height'] / 100) ** 2

new=DFQ[["age","weight","BMI","chest"]]
new.to_excel(output_path,sheet_name="body",startcol=0,index=True)   #按题目要求输出excel文件，将本行代码补充完整