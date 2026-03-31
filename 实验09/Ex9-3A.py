import matplotlib.pyplot as plt
systolic = [159, 153, 147, 150, 151, 149, 155] # Systolic blood pressure data
diastolic = [107, 115, 87, 86, 110, 90, 112] # Diastolic blood pressure data
# Plot systolic blood pressure line
plt.subplot(2, 4, 3)
plt.plot(systolic, "b-o")
# Plot diastolic blood pressure line
plt.subplot(427)
plt.plot(diastolic, "r:p")
plt.show()