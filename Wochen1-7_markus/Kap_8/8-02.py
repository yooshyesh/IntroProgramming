import turtle

def main():
    turtle.colormode(255)
    turtle.color((255, 0, 0))
    i = 0
    while i < 6:
        turtle.speed(1)
        turtle.forward(100)
        turtle.left(360/6)
        i += 1
    turtle.done()

main()