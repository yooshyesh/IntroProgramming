import turtle
def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(angle)
        
def main():
    turtle.speed(3)
# Beispiel: Vielecke zeichnen
    draw_polygon(3, 100) # Dreieck
    turtle.penup()
    turtle.goto(150, 0)
    turtle.pendown()
    draw_polygon(5, 80) # Fünfeck
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.pendown()
    draw_polygon(6, 70) # Sechseck
    turtle.done()

main()