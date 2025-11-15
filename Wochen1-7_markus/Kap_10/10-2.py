import turtle
import random

colors = "red", "green", "blue"    

def draw_polygon(color, sides, length): 
    angle = 360 / sides

    turtle.speed(0)
    turtle.pendown()
    for i in range(sides):
        turtle.forward(length)
        turtle.left(angle)
    turtle.penup() 

def get_next_position(offset_x, offset_y):
    x, y = turtle.pos()
    new_x = x + offset_x
    new_y = y - offset_y
    return (new_x, new_y)

def zigzag(color, x):
    match color:
        case "red":
            zig_x = x + 20
        case "green":
            zig_x = x - 40
        case "blue":
            zig_x = x + 60
    return (zig_x) # Eine einzige Variable wird ausgegeben

def main():
    turtle.penup()
    turtle.goto(-340, 340)
    for i in range(16):
        color = (random.choice(colors)) 
        x, y = get_next_position(20, 40) # return values empfangen und x, y innerhalb Funktion definieren
        zig_x = zigzag(color, x) # Auch zig definieren und durch zigzag-Dunktion bestimmen
        turtle.goto(zig_x, y) # Zu neuer x Koordinate gehen
        draw_polygon(turtle.color(color), random.randint(3, 16), 20)

main()
turtle.done()