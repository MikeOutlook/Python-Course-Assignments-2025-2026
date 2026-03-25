# import numpy as np

# arr1 = np.loadtxt("data.csv", delimiter=",", skiprows=1,
#                   usecols=[0, 1], dtype=int,)
# print(arr1)

import numpy as np
import os

# 1. 获取当前脚本 (Ex6-3A.py) 所在的文件夹：实验06
current_script_dir = os.path.dirname(__file__)

# 2. 获取该文件夹的上一级目录：即项目根目录 Python-Course-Assignments-2025-2026
project_root = os.path.abspath(os.path.join(current_script_dir, ".."))

# 3. 拼接出 data_input 文件夹下 data.csv 的完整路径
file_path = os.path.join(project_root, "data_input", "data.csv")

# 4. 打印一下路径，方便你调试检查
print(f"正在读取文件: {file_path}")

# 5. 加载数据
try:
    arr1 = np.loadtxt(file_path, delimiter=",", skiprows=1,
                      usecols=[0, 1], dtype=int)
    print("读取成功！数据如下：")
    print(arr1)
except Exception as e:
    print(f"读取失败，请检查文件是否存在。错误信息: {e}")