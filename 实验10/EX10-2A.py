import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimHei"]

data = [187, 55, 546, 253, 81]
pieLabel = ["消化系统", "循环系统", "呼吸系统", "神经系统", "其他 "]
pieColor = ["r", "g", "pink", "y", "b"]
pieExplode = [0, 0.1, 0, 0, 0]


plt.pie(data,labels=pieLabel,colors=pieColor,explode=pieExplode,
        autopct="%.1f%%",shadow=True) #调用适当函数绘制饼图，将本行代码补充完整

plt.show()