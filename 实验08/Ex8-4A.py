import matplotlib.pyplot as plt
systolic = [159, 153, 147, 150, 151, 149, 155]
diastolic = [107, 115, 87, 86, 110, 90, 112]
plt.plot(systolic, color="b",linestyle="-", marker="o")
#plt.plot(systolic, "b-o")
plt.plot(diastolic, "r:p")
plt.show()

