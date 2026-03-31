import math
angel = float(input("Enter angle: "))
A = math.radians(angel) # Convert angle to radians
result = (3*math.sin(A)-math.tan(A))/(4*math.sin(A)+2*math.tan(A))
print(result)