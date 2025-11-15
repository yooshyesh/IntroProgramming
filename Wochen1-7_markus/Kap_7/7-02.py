import turtle

def main():
    print(turtle.window_width())
    print(turtle.window_height())
    turtle.colormode(255)
    turtle.color((0, 0, 255))
    turtle.speed(0)
    turtle.penup()
    
    bottom_y = -356
    middle_x = 0
    
    turtle.goto(middle_x, bottom_y)
    turtle.pendown()
    turtle.circle(356)
    turtle.done()

main()
