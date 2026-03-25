import random
import math
import datetime

# Liste von Karteikarten
karteikarten = [
    {"frage": "Was ist eine Liste in Python?", "antwort": "Eine geordnete, veränderbare Sammlung von Elementen."},
    {"frage": "Wie erstellt man ein Dictionary?", "antwort": "Mit geschweiften Klammern: z.B. {'key': 'value'}"},
    {"frage": "Was macht die 'len()'-Funktion?", "antwort": "Gibt die Anzahl der Elemente eines Objekts zurück."},
    {"frage": "Wie kommentiert man eine Zeile in Python?", "antwort": "Mit einem '#' am Anfang der Zeile."},
    {"frage": "Was ist eine Funktion?", "antwort": "Ein Block von Code, der eine Aufgabe erfüllt und wiederverwendbar ist."}
]

# TODO: Karten mischen
for entry in karteikarten:
    print(random.choice(entry))

#print("Python Karteikarten – starte das Quiz!\n")

# TODO: Abfrage-Schleife implementieren
#for # ...
#    input(f"Frage: {karte['frage']}\nDrücke Enter, um die Antwort zu sehen...")
#    # TODO: Antwort anzeigen
    
#    input("Drücke Enter für die nächste Karte...\n")

#print("Alle Karten abgefragt – gut gemacht!")