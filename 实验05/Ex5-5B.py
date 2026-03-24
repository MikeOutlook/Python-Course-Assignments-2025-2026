original=[100,36,44,27,65,77,56,95,84]
new=[]
for i in original:
    i=(i**0.5)*10
    i=round(i,0)
    new.append(i)
print(new)