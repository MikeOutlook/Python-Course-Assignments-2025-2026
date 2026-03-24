import numpy as np #导入numpy库，将本行代码补充完整

temp_list = [37.7, 37.5, 37.3, 36.8, 38.4, 37.4,
             37.7, 36.3, 39.0, 38.5, 37.8, 37.3,
             36.6, 36.2, 37.5, 37.6, 38.6, 36.9,
             38.2, 37.9]

temp = np.array(temp_list)  #创建数组temp，将本行代码补充完整
heat  =temp[temp>37.3]  #找出发热数据加入数组heat，将本行代码补充完整
F_heat =heat*1.8+32 #转换为华氏温度值存入数组F_heat，将本行代码补充完整
F_heat1 =np.round(F_heat,1) #保留小数点后1位，将本行代码补充完整

print(F_heat1)
