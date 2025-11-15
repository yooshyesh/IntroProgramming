import turtle

x_werte = []
y_werte = []

turtle.penup()
turtle.speed(0)
# Maus-Event: Klick speichern

def punkt_erfassen(x, y):
    x_werte.append(x)
    y_werte.append(y)
    turtle.goto(x, y)
    turtle.dot(6, "red")
    
# Tastendruck: Punkte abfahren
def punkte_abfahren():
    if len(x_werte) < 2:
        return
    turtle.color("blue")
    turtle.width(2)
    turtle.goto(x_werte[0], y_werte[0])
    turtle.pendown()
    for i in range(1, len(x_werte)):
        turtle.goto(x_werte[i], y_werte[i])
    turtle.penup()
    
# Events registrieren
turtle.onscreenclick(punkt_erfassen)
turtle.onkey(punkte_abfahren, "space")
turtle.listen()
turtle.mainloop()