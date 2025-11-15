import turtle

def draw_square(x, y):
    turtle.penup()
    turtle.goto(x, y)
    for i in range(4):
        turtle.pendown()
        turtle.forward(30)
        turtle.left(90)

turtle.onscreenclick(draw_square)
turtle.mainloop()