# 智慧医学 Python 课程实验 (2025-2026)

本项目包含了“智慧医学” Python 课程的所有实验作业与练习代码。为了确保医学数据处理（如 Excel 读取和 Numpy 计算）的兼容性，本项目统一使用实验室标准的 **Python 3.6.8** 环境。

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
# 从配置文件创建环境
conda env create -f environment.yml

# 激活环境
conda activate MedPython