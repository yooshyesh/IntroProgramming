import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.penup()

# Zufällige Farbe generieren
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Ein einzelnes Quadrat zeichnen
def draw_square(x, y, size, color):
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()



# Schachbrett zeichnen
def draw_colored_board(rows=5, cols=5, size=50):
    start_x = -cols * size // 2
    start_y = rows * size // 2
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * size # bestimmt nur Startpunkt x
            y = start_y - row * size # bestimmt nur Startpunkt y
                
            if (col + row) % 2 == 1: # rechnet aus, ob square count durch 2 teilbar ist
                color = 255, 255, 255
                draw_square(x, y, size, color) # zeichnet das effektive square
            else:
                color = random_color()
            draw_square(x, y, size, color)
            
#################### Hauptprogramm ####################
def main():
    draw_colored_board()
    turtle.hideturtle()
    turtle.done()
    
main()