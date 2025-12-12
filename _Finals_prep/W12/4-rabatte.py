
class Produkt:
    rabatt = 0.1  # Klassenvariable: Standardrabatt für alle Produkte (10%)

    def __init__(self, preis):
        self.preis = preis

    def endpreis(self):
        return self.preis * (1 - Produkt.rabatt)

# Anwendung
p1 = Produkt(100)
p2 = Produkt(200)
print(p1.endpreis())  # 90.0
print(p2.endpreis())  # 180.0
