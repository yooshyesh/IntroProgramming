import turtle
import random

def main():
    turtle.speed(0)
    turtle.pensize(50)
    radius = 100
    number_squares = 36
    square_size = None
    
    for i in range(number_squares): 
        radius = random.randint(50, 300)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(i * (360 / number_squares))
        turtle.forward(radius)
        turtle.pendown()
        
        square_size = (random.randint(10, 100))

        if square_size < 40:
            color = "red"
        elif square_size < 80:
            color = "blue"
        else:
            color = "orange"

        turtle.color(color) # match verifiziert ob es zutrifft und füllt ansonsten andere Anweisungen um

        match color: # color muss oben definiert werden (zB glbobal variable oder einzelne Variablen)
            case "red":
                turtle.pensize(5)
            case "blue":
                turtle.pensize(12)
            case "orange":
                turtle.pensize(25)
        
        for _ in range(4):
            turtle.forward(square_size)
            turtle.left(90)
       
    turtle.done()
    
main()