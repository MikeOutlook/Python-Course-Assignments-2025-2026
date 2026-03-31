import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = ['SimHei']
data = np.array([32, 187, 42, 29, 44, 38])
x = np.arange(0, data.size)
barLabels = ["Trauma and Poisoning", "Malignant Tumors", "Cerebrovascular Disease",
             "Endocrine Disease", "Cardiovascular Disease", "Respiratory Disease"]
plt.bar(x, data, tick_label=barLabels)
plt.show()