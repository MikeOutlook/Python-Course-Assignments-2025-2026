import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = ['SimHei']
data = np.array([32, 187, 42, 29, 44, 38])
x = np.arange(0, data.size)
barLabels = ["外伤和中毒", "恶性肿瘤", "脑血管疾病",
             "内分泌疾病", "心血管疾病", "呼吸系统疾病"]
plt.bar(x, data, tick_label=barLabels)
plt.show()