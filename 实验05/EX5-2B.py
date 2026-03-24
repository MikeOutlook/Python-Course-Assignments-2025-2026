import numpy as np # 导入numpy，将本行代码补充完整

height_list = [1.68, 1.81, 1.76, 1.68, 1.73, 1.72, 1.74]
weight_list = [185.2, 169.4, 143.7, 191.8, 172.6, 124.1, 153.5]

height =np.array(height_list)  # 从身高列表创建为数组，将本行代码补充完整
weight =np.array(weight_list,dtype=int)  # 从体重列表创建为数组，数组数据类型为整数，将本行代码补充完整

print("患者身高数据如下：\n",height)
print("患者体重数据如下：\n",weight)


