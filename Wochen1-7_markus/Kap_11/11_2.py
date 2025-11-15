import turtle
import random

turtle.penup()
turtle.speed(1)

# random x und y generieren
def generate_coordinates():
    coordinates = []
    for _ in range (8):
        x = random.randint(-180,180)
        y = random.randint(-180,180)
        coordinates.append((x,y))
    return coordinates

def generate_y_coordinates():
    y_coordinates = []
    for _ in range (16):
        y_coordinates.append(random.randint(-180,180))
    return y_coordinates
             
def connecting_dots():
    coordinates = generate_coordinates()
    print(coordinates)
    for x, y in coordinates:
        turtle.pendown()
        turtle.goto(x, y)
    
connecting_dots()
turtle.done()