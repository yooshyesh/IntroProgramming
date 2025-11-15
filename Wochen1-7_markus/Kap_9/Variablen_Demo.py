import turtle

color = "blue"
edges = 4
angle = 90
size = 100
turtle.color(color)

for _ in range(edges):
    turtle.forward(size)
    turtle.left(angle)