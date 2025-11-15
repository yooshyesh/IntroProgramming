import turtle

def main():
    turtle.speed(0)
    turtle.penup()
    turtle.colormode(255)
    turtle.color(200, 0, 180)
    turtle.pendown()

    #for _ in range(36): # _ -> Platzhalter für ungenutzte Variable
    circle_size = 30
    circle_distance = 10
    for _ in range(30):
        for _ in range(4):
            turtle.circle(circle_size)
            circle_size += 15
    turtle.left(10)
    turtle.penup()
    turtle.forward(circle_distance)
    circle_distance += 10
        
        
    turtle.done()
main()