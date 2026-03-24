import random
a=random.randint(10,100)
b=random.randint(10,100)
print("计算{}+{}".format(a, b))
c=int(input("请输入计算结果："))
if c==a+b:
    print("结果正确，你真棒！")
else:
    print("结果错误，再想一想")