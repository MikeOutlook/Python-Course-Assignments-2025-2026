starlist=["One star","Two stars","Three stars"]
score=int(input("Enter employee rating: "))
star=score//10
level=starlist[star]
print("Employee score: {0}, Rating: {1}".format(score,level))
