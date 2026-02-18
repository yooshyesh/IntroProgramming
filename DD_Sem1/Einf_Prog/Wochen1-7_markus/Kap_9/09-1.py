import turtle
import random

colors = ["red", "green", "blue", "orange"]

def main():
    turtle.speed(0)
    radius = 100
    number_squares = 36
    square_size = None
    
    for i in range(number_squares): 
        turtle.color(random.choice(colors))
        radius = random.randint(50, 300)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(i * (360 / number_squares))
        turtle.forward(radius)
        turtle.pendown()
        
        square_size = (random.randint(10, 100))
        
        for _ in range(4):
            turtle.forward(square_size)
            turtle.left(90)
       
    turtle.done()
    
main()