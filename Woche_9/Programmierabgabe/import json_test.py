""" Learning: with open() as abc: 
json.load(abc)
encoding="utf-8" optional, nur wenn file komisch ausieht
"""import json

def load_usability_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)  # Dateiinhalt als Python-Objekt einlesen
    return data

# Pfad zur Datei (relativ oder absolut)
filepath = "Woche_9/Programmierabgabe/usability_data.json"

# Daten einlesen
data = load_usability_data(filepath)

# Direkt im Terminal ausgeben
print(data)