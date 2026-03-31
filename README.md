# Smart Medical Python Course Lab (2025-2026)

This project contains all lab assignments and practice code for the "Smart Medical" Python course. To ensure compatibility with medical data processing (e.g., Excel reading and NumPy calculations), this project uses the lab's standard **Python 3.6.8** environment.

## 📚 Experiment Directory

### Lab 01 - Python Basics
- Basic I/O, variable types, arithmetic expressions, string operations, Turtle graphics

### Lab 02 - Sequence Data Types
- String slicing, list operations, formatted output

### Lab 03 - Conditionals and Loops
- if-elif statements, for/while loops, BMI calculation

### Lab 04 - Functions and Modules
- Custom functions, math/random module applications

### Lab 05 - NumPy Basics
- NumPy array creation, reshaping, element filtering

### Lab 06 - NumPy Advanced
- Array slicing, boolean indexing, file I/O

### Lab 07 - Pandas Basics
- DataFrame operations, data filtering, Excel/CSV I/O

### Lab 08 - Data Processing and Visualization
- Pandas data cleaning, Matplotlib basic plotting

### Lab 09 - Advanced Visualization
- Bar charts, scatter plots, line charts, subplots

### Lab 10 - Machine Learning Introduction
- Linear regression model building and evaluation

## 🔬 Environment Setup (Standard Lab Environment)

This project depends on specific older versions of scientific computing libraries. It is recommended to use Anaconda or Miniconda for environment management.

### 1. Environment Parameters
- **Python Version**: `3.6.8`
- **Core Dependencies**:
  - `numpy==1.17.4` (numerical computing)
  - `pandas==0.22.0` (data analysis)
  - `matplotlib==3.0.1` (medical plotting)
  - `scikit-learn==0.24.1` (machine learning basics)
  - `xlrd==1.2.0` & `openpyxl==2.4.10` (Excel compatibility)

### 2. Quick Environment Setup
If you clone this project, you can restore the environment with:

```bash
# Install dependencies
pip install -r requirements.txt

# Or use conda
conda env create -f environment.yml
conda activate MedPython
```

## 📊 Data Files

Data files are located in the `data_input` directory, including:
- Diabetes.csv - Diabetes patient data
- birthwt.csv - Birth weight data
- body_datas.csv - Body measurement data
- checkup.csv - Health checkup data
- And other medical-related datasets

## 🚀 Quick Start

```bash
# Clone project
git clone https://github.com/yourusername/Python-Course-Assignments-2025-2026.git

# Install dependencies
pip install -r requirements.txt

# Run example
python Lab05/Ex5-1A.py
```

## Project Structure

```
Python-Course-Assignments-2025-2026/
├── Lab01-Lab11/       # Lab code files
├── data_input/        # Input data
├── data_output/       # Output results
├── README.md
├── requirements.txt
└── .gitignore
```
