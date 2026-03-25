import turtle

def zeichne_kreis(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(30)
    
turtle.onscreenclick(zeichne_kreis)

turtle.mainloop()