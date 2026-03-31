import random
a=random.randint(10,100)
b=random.randint(10,100)
print("Calculate {}+{}".format(a, b))
c=int(input("Enter the result: "))
if c==a+b:
    print("Correct, you are awesome!")
else:
    print("Incorrect, think again")