s=0

for i in range (1,100):
    if i%2==0:
        s=s+0
    else:
        s=s+1/i
print("计算结果是{}".format(s))