import turtle

def main():
    print(turtle.window_width())
    print(turtle.window_height())
    turtle.speed(0)
    turtle.penup()
    
    middle_y = 0
    left_x = -376
    
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(356/2)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(180)
    turtle.pendown()
    turtle.circle(356/2)
    turtle.done()

main()
