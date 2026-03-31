def hypot(a, b, n=2):
    c = (a ** 2 + b ** 2) ** 0.5
    c = round(c, n)
    return c
x = hypot(7, 12)
y = hypot(6, 1442, n=4)
print("Right triangle x hypotenuse length: ",x)
print("Right triangle y hypotenuse length: ",y)