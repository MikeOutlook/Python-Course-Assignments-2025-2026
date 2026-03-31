import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimHei"]

data = [187, 55, 546, 253, 81]
pieLabel = ["Digestive System", "Circulatory System", "Respiratory System", "Nervous System", "Others "]
pieColor = ["r", "g", "pink", "y", "b"]
pieExplode = [0, 0.1, 0, 0, 0]


plt.pie(data,labels=pieLabel,colors=pieColor,explode=pieExplode,
        autopct="%.1f%%",shadow=True) # Call appropriate function to draw pie chart, complete this line

plt.show()