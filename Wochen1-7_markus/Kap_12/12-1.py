import turtle

turtle.colormode(255)

def up():
    turtle.setheading(90)
    turtle.color("red")
    turtle.forward(20)

def down():
    turtle.setheading(270)
    turtle.color("green")
    turtle.forward(20)

def left():
    turtle.setheading(180)
    turtle.color("blue")
    turtle.forward(20)

def right():
    turtle.setheading(0)
    turtle.color("orange ")
    turtle.forward(20)

################EVENT REGISTRATION################
turtle.listen()
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

turtle.mainloop()