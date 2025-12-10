from abc import ABC, abstractmethod

class Tier(ABC):
    @abstractmethod
    def geräusch(self):
        pass

class Hund(Tier):
    def geräusch(self):
        return "Wau"

class Katze(Tier):
    def geräusch(self):
        return "Miau"

# Gibt eine Fehler, da Tier eine abstrakte Klasse ist und nicht instanziiert werden kann.
# t = Tier()
# print(t.geräusch())

def geräusche(tiere):
    for t in tiere:
        print(t.geräusch())

tiere = [Hund(), Katze(), Katze()]
geräusche(tiere)
