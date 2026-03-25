import os
import pandas as pd
# ==========================================
# 第一部分：项目路径自动定位 (Relative Path 1.0)
# ==========================================

# 1. 定位当前脚本所在文件夹 (e.g., 实验07)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 定位项目根目录 (向上跳一级)
project_root = os.path.dirname(current_dir)

# 3. 构建输入与输出的完整路径
input_file = os.path.join(project_root, "data_input", "body_datas.csv")
output_file = os.path.join(project_root, "data_output", "result.xlsx")

print(f"📂 正在从以下位置加载数据: {input_file}")

# ==========================================
# 第二部分：医学数据清洗与指标计算
# ==========================================

# [步骤1] 读取 CSV 数据，并将 'id' 列设为索引
df_body = pd.read_csv(input_file, index_col='id')

# [步骤2] 筛选目标人群：年龄 > 45 岁 且 体重 > 70 kg
# 使用 .copy() 确保后续计算在副本上进行，避免警告
df_filtered = df_body[(df_body["age"] > 45) & (df_body["weight"] > 70)].copy()

# [步骤3] 计算 BMI 指数 (公式: 体重 / 身高的平方，身高需从cm转为m)
df_filtered['BMI'] = df_filtered['weight'] / (df_filtered['height'] / 100) ** 2

# ==========================================
# 第三部分：筛选关键指标并导出结果
# ==========================================

# [步骤4] 提取需要展示的列：年龄、体重、BMI、胸围
result_table = df_filtered[["age", "weight", "BMI", "chest"]]

# [步骤5] 导出为 Excel 文件
# 设置工作表名称为 "body"，保留索引 (id)
result_table.to_excel(output_file, sheet_name="body", index=True)

print(f"✅ 处理完成！结果已保存至: {output_file}")


# import os
# import pandas as pd

# # 1. 获取当前脚本 (7-4-1.py) 所在的文件夹：实验07
# current_script_dir = os.path.dirname(__file__)

# # 2. 获取该文件夹的上一级目录：即项目根目录 Python-Course-Assignments-2025-2026
# project_root = os.path.abspath(os.path.join(current_script_dir, ".."))

# # 3. 拼接出 data_input 文件夹下 data.csv 的完整路径
# file_path = os.path.join(project_root, "data_input", "body_datas.csv")
# output_path = os.path.join(project_root, "data_output", "result.xlsx")

# # 4. 打印一下路径，方便你调试检查
# print(f"正在读取文件: {file_path}")

# DF_body=pd.read_csv(file_path,index_col='id')
# DFQ=DF_body[(DF_body["age"]>45) & (DF_body["weight"]>70)].copy()
# DFQ['BMI'] = DFQ['weight'] / (DFQ['height'] / 100) ** 2

# new=DFQ[["age","weight","BMI","chest"]]
# new.to_excel(output_path,sheet_name="body",startcol=0,index=True)   #按题目要求输出excel文件，将本行代码补充完整