# 智慧医学 Python 课程实验 (2025-2026)

本项目包含了”智慧医学” Python 课程的所有实验作业与练习代码。为了确保医学数据处理（如 Excel 读取和 Numpy 计算）的兼容性，本项目统一使用实验室标准的 **Python 3.6.8** 环境。

## 📚 实验目录

### 实验01 - Python 基础入门
- 基本输入输出、变量类型、算术表达式、字符串操作、Turtle绘图

### 实验02 - 序列数据类型
- 字符串切片、列表操作、格式化输出

### 实验03 - 条件与循环
- if-elif条件判断、for/while循环、BMI计算

### 实验04 - 函数与模块
- 自定义函数、math/random模块应用

### 实验05 - NumPy 基础
- NumPy数组创建、变形、元素筛选

### 实验06 - NumPy 进阶
- 切片索引、布尔索引、文件读写

### 实验07 - Pandas 基础
- DataFrame操作、数据筛选、Excel/CSV读写

### 实验08 - 数据处理与可视化
- Pandas数据清洗、Matplotlib基础绑图

### 实验09 - 高级可视化
- 柱状图、散点图、折线图、多子图

### 实验10 - 机器学习入门
- 线性回归模型建立与评估

## 🔬 实验环境配置 (Standard Lab Environment)

本项目依赖于特定的旧版科学计算库，建议使用 Anaconda 或 Miniconda 进行环境管理。

### 1. 环境参数
- **Python 版本**: `3.6.8`
- **核心依赖库**:
  - `numpy==1.17.4` (数值计算)
  - `pandas==0.22.0` (数据分析)
  - `matplotlib==3.0.1` (医学绘图)
  - `scikit-learn==0.24.1` (机器学习基础)
  - `xlrd==1.2.0` & `openpyxl==2.4.10` (Excel 兼容性支持)

### 2. 快速恢复环境
如果你克隆了本项目，可以通过以下命令一键还原开发环境：

```bash
# 安装依赖
pip install -r requirements.txt

# 或使用conda
conda env create -f environment.yml
conda activate MedPython
```

## 📊 数据文件

数据文件位于 `data_input` 目录，包括：
- Diabetes.csv - 糖尿病数据
- birthwt.csv - 婴儿出生体重数据
- body_datas.csv - 人体测量数据
- checkup.csv - 体检数据
- 以及其他医学相关数据集

## 🚀 快速开始

```bash
# 克隆项目
git clone https://github.com/yourusername/Python-Course-Assignments-2025-2026.git

# 安装依赖
pip install -r requirements.txt

# 运行示例
python 实验05/Ex5-1A.py
```