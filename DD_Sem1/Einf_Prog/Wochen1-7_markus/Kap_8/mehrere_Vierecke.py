import turtle
def main():
    turtle.speed(0)
    for i in range(36): # _ -> Platzhalter für ungenutzte Variable
        turtle.pendown()
        for _ in range(4):
            turtle.forward(20)
            turtle.left(90)
        turtle.penup()
        turtle.setheading(360 / i)
        turtle.forward(30)
        
        
    turtle.done()
    
main()