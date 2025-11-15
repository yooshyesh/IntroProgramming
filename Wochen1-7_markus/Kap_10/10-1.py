import turtle

def draw_polygon(color, sides, length): # Wieso color als Parameter, wenn nachher durch if-else aufgehoben?
    angle = 360 / sides

    if sides % 2 == 0:
        turtle.color("red")
    else:
        turtle.color("cyan")

    turtle.speed(1)
    turtle.pendown()
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(angle)
    turtle.penup() 

def main():
    draw_polygon("blue", 6, 40) # color parameter wird in dieser Verwendung überschrieben
    turtle.goto(-120, 0)
    draw_polygon("magenta", 3, 70)
    turtle.goto(-200, 0)
    draw_polygon("orange", 11, 30)

main()
turtle.done() # Braucht es immer am Schluss, sonst schliesst das Fenster nach dem Zeichnen