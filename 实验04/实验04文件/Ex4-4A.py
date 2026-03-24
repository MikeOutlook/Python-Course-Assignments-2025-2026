import math
angel = float(input("请输入角度"))
A = math.radians(angel) #角度值转换为弧度值
result = (3*math.sin(A)-math.tan(A))/(4*math.sin(A)+2*math.tan(A))
print(result)