import turtle

def draw_square(size=100, color="blue"):
    turtle.color(color)
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
        
draw_square() # Blaues Rechteck mit Seitenlänge 100 wird gezeichnet 