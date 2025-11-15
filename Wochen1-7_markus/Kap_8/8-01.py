import turtle

def main():
    turtle.colormode(255)
    turtle.color((255, 0, 0))
    for _ in range(5):
        turtle.speed(1)
        turtle.forward(100)
        turtle.left(360/5)
    turtle.done()

main()