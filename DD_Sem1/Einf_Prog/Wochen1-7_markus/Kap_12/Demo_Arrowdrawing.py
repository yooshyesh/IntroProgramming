import turtle

def up():
    turtle.setheading(90)
    turtle.forward(20)
    
def down():
    turtle.setheading(270)
    turtle.forward(20)
    
def left():
    turtle.setheading(180)
    turtle.forward(20)
    
def right():
    turtle.setheading(0)
    turtle.forward(20)

# Events registrieren
turtle.listen()
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.mainloop()