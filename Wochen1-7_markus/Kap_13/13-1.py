import turtle

#x_values = [] #define list globally
#y_values = []
coordinates = []

turtle.penup()
turtle.speed(0)

def register_points(x, y):
    coordinates.append((x, y)) #double parentheses are necessary to append 2 arguments
    print(coordinates)
    turtle.goto(x, y)
    turtle.dot(6, "red")

def connect_dots():
    if len(coordinates) < 2:
        return
    turtle.color("blue")
    turtle.width(2)
    turtle.goto(coordinates[0])
    turtle.pendown()
    for i in range(1, len(coordinates)):
        turtle.goto(coordinates[i])
    turtle.penup()

#register events
turtle.listen()
turtle.onscreenclick(register_points)
turtle.onkey(connect_dots, "space")
turtle.mainloop()