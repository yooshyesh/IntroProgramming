import turtle

def main():
    print(turtle.window_width())
    print(turtle.window_height())
    turtle.speed(0)
    turtle.penup()
    turtle.colormode(255)
    turtle.color(0, 0, 255)
    
    turtle.goto(-376.0, -356.0)
    turtle.pendown()
    turtle.dot(10)
    turtle.penup()
    
    turtle.goto(366.0, -356.0)
    turtle.pendown()
    turtle.dot(10)
    turtle.penup()
    
    turtle.goto(366.0, 366.0)
    turtle.pendown()
    turtle.dot(10)
    turtle.penup()
    
    turtle.goto(-376.0, 366.0)
    turtle.pendown()
    turtle.dot(10)
    turtle.penup()

main()
