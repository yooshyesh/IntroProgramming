import turtle

def main():
    turtle.colormode(255)
    turtle.color((255, 0, 0))
    for i in range(4): # 4 Mal wiederholen mit range vor Zahl
        turtle.speed(1)
        turtle.forward(100)
        turtle.left(90)
        # Turn gibt es nicht, left oder right definieren
    print(turtle.window_width())
    print(turtle.window_height())
    turtle.done()

main()