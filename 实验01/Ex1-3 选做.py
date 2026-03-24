import turtle
n=6
turtle.pensize(3)
turtle.speed(0)
turtle.bgcolor("black")
color_list=["red","green","blue","yellow","purple","pink"]
for i in range(200):
    c=i%n
    turtle.color(color_list[c])
    turtle.forward(2*i)
    turtle.left(61)