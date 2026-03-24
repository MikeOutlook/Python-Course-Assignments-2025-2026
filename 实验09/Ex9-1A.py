import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
data = pd.read_csv("stats.csv")
print(data)
weight = data["weight"]
area = data["BSA"]
plt.scatter(weight, area, c="red", s=5000, alpha=0.1)
plt.xlabel("体重(公斤)")
plt.ylabel("体表面积(平方米)")
plt.show()