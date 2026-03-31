weight_list=[70,60,78,85,77,54,65,80]
total=0
for i in weight_list:
    total=total+i
aver=total/(len(weight_list))
print("Average sample weight: {:.1f}".format(aver))
