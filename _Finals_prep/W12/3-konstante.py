
class Kreis:
    pi = 3.14159  # Klassenvariable: Konstante

    def __init__(self, radius):
        self.radius = radius

    def flaeche(self):
        return Kreis.pi * (self.radius ** 2)

# Anwendung
k = Kreis(5)
print(k.flaeche())  # Ausgabe: 78.53975
