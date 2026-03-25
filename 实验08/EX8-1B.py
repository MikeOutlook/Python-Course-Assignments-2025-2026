import os
import pandas as pd# 导入pandas，将本行代码补充完整

# 1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

# 3. 构建输入与输出的完整路径
input_file = os.path.join(project_root, "data_input", "Diabetes.csv")


DF1 =pd.read_csv(input_file,index_col=0)   # 读取数据文件，将本行代码补充完整
DF1.eval("Glucose=Glucose/18",inplace=True)  # 使用eval函数进行计算，将本行代码补充完整
DF1["BSA"]=((DF1["Height"]*DF1["Weight"]/3600)**0.5).round(2)   # 添加新列，使用列索引进行简单计算，将本行代码补充完整

print(DF1)