import turtle
Ugol =  8

turtle.color('red')
turtle.begin_fill()
for i in range(Ugol):
    turtle.forward(80)
    turtle.right(360 * 3/ Ugol)
turtle.end_fill()