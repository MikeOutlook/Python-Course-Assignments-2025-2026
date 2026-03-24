import numpy as np

# 读取CSV文件
data =np.loadtxt("patient_temperatures.csv",
                 dtype=float,
                 delimiter=",",
                 skiprows=1)  # 将本行代码补充完整

print(data)

print(data[0:10,0:2])

print(data[20:40,4:5])

print(data[50:75,1:4])

print(data[data>38.6])

print(data[data[:,6]>38.6])