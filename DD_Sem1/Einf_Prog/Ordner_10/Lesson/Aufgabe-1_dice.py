""" Learning: attribute sides is defined in the init function and when defining the objects d1, d2
"""
import random

class Dice:
    def __init__(self, sides=6): # =6 gibt Standardwert noch an
        self.sides = sides
    
    def roll(self): 
            return random.randint(1, self.sides) # sides ist nicht definiert

dice1 = Dice(6)
dice2 = Dice(10)

results6 = [dice1.roll() for _ in range(10)]
# Dice](dice1.roll()) erzeugt wieder ein Dice Objekt, wird oben mit dice1 = bereits gemacht
results10 = [dice2.roll() for _ in range(10)]

print(f"Ergebnisse des 6-seitigen Würfels: {results6}\n"), print(f"Ergebnisse des 10-seitigen Würfels: {results10}\n")
