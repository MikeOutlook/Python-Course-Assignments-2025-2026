import numpy as np

height_list = [1.68, 1.81, 1.76, 1.68, 1.73, 1.72, 1.74]
weight_list = [185.2, 169.4, 143.7, 191.8, 172.6, 124.1, 153.5]

height =np.array(height_list)  # 从身高列表创建为数组，将本行代码补充完整
weight =np.array(weight_list,dtype=int)  # 从体重列表创建为数组，数组数据类型为整数，将本行代码补充完整

weight_kg =weight*0.454   # 将体重数据由磅值改为公斤为单位的值，将本行代码补充完整


BMI =weight_kg/(height**2)  # 根据题目公式计算BMI，将本行代码补充完整

BMI2 =np.round(BMI,2)   # 将BMI值保留2位小数，将本行代码补充完整

BMI3 =BMI2[(BMI2>18.5) & (BMI2<24)]   # 找出正常范围内的BMI值，将本行代码补充完整

print("患者BMI数据如下：\n",BMI2)
print("患者BMI的正常BMI值如下：\n",BMI3)


