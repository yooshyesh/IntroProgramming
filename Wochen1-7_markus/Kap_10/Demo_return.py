import turtle

def get_radius_and_color(index):
    match index % 3:
        case 0:
            return 20, "red"
        case 1:
            return 40, "green"
        case 2:
            return 60, "blue"
        
turtle.speed(0)

for i in range(24):
    radius, color = get_radius_and_color(i)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(i * 15) # 24 circles evenly spaced
    turtle.forward(100)
    turtle.pendown()
    
    turtle.color(color)
    turtle.circle(radius)

turtle.hideturtle()
turtle.done()