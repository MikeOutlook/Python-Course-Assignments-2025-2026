#高血压判断
SBP = int(input("请输入收缩压"))
DBP = int(input("请输入舒张压"))
if (SBP >= 140) or (DBP >= 90):
    print("患者为高血压")
else:
    print("患者不是高血压")