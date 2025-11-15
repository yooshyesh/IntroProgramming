import turtle

def main():
    turtle.colormode(255)
    turtle.color((0, 255, 0))
    turtle.pensize(5)
    for i in range(3): # 4 Mal wiederholen mit range vor Zahl
        turtle.speed(1)
        turtle.forward(80)
        turtle.left(360/3)
        # Turn gibt es nicht, left oder right definieren
    turtle.done()

main()