""" Plan: create empty list, import json file and parse that into the list, return list
Execute
Learnings
"""
import json

usability_data: []
def load_usability_data(filepath):
    with open("usbility_data.json") as file:
        usability_data = json.load(file)
        print(file)
    return usability_data

load_usability_data(/Users/yeshetsultrim/Documents/dev/Woche_9/Programmierabgabe/usability_data.json)
# Ausgabe: [{'success': True, 'duration': 30, 'backtracks': 1}, ...]