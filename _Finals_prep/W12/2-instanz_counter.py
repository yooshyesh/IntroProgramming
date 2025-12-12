class Auto:
    # Klassenvariable
    # - gehört zur Klasse selbst, nicht zu einzelnen Objekten
    # - wird von allen Instanzen geteilt
    anzahl_autos = 0  

    def __init__(self, marke):
        self.marke = marke  # Instanzvariable
        Auto.anzahl_autos += 1

a1 = Auto("BMW")
a2 = Auto("Audi")

# Zugriff auf die Klassenvariable über den Klassennamen
print(Auto.anzahl_autos)  # Ausgabe: 2
