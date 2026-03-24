import matplotlib.pyplot as plt
systolic = [159, 153, 147, 150, 151, 149, 155] # 收缩压数据
diastolic = [107, 115, 87, 86, 110, 90, 112] # 舒张压数据
# 绘制收缩压折线
plt.subplot(2, 4, 3)
plt.plot(systolic, "b-o")
# 绘制舒张压折线
plt.subplot(427)
plt.plot(diastolic, "r:p")
plt.show()