import numpy as np
import os

# 读取CSV文件(因为要上传github，所以使用相对路径)

# 1. 获取当前脚本 (Ex6-3B.py) 所在的文件夹
current_script_dir = os.path.dirname(__file__)

# 2. 获取该文件夹的上一级目录：即项目根目录 Python-Course-Assignments-2025-2026
project_root = os.path.abspath(os.path.join(current_script_dir, ".."))

# 3. 拼接出 data_input 文件夹下 data.csv 的完整路径
file_path = os.path.join(project_root, "data_input", "patient_temperatures.csv")

# 4. 打印一下路径，方便你调试检查
print(f"正在读取文件: {file_path}")


data =np.loadtxt(file_path,
                 dtype=float,
                 delimiter=",",
                 skiprows=1)  # 将本行代码补充完整

print(data)

print(data[0:10,0:2])

print(data[20:40,4:5])

print(data[50:75,1:4])

print(data[data>38.6])

print(data[data[:,6]>38.6])