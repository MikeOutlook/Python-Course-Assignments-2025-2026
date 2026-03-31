import matplotlib.pyplot as plt
# Chinese font display correction, fill in correct code below
plt.rcParams["font.family"] = ["SimHei"]

data = [32, 187, 42, 29, 44, 38]
pieLabel = ["Trauma and Poisoning", "Malignant Tumors", "Cerebrovascular Disease", "Endocrine Disease", "Cardiovascular Disease", "Respiratory Disease"]
pieColor =["r","g","pink","y","m","b"] # Generate color data list, complete this line
pieExplode =[0,0,0.1,0,0,0.2] # Generate explode value data list, complete this line

plt.pie(data,labels=pieLabel,colors=pieColor,explode=pieExplode,
        autopct="%.1f%%",shadow=True) # Call function to draw pie chart, complete this line

plt.show()

