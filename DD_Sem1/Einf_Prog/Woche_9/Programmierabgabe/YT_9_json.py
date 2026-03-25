""" Plan: create empty list, import json file and parse that into the list, return list
Execute: json import, define function with parameter filepath 
Learnings: Filepath needs to be defined as a string as well! Parameter can be used in open function, not file-specific
"""
import json

def load_usability_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        usability_data = json.load(file)
        #print(file)
    return usability_data

print(load_usability_data("Woche_9/Programmierabgabe/usability_data.json"))
# Ausgabe: [{'success': True, 'duration': 30, 'backtracks': 1}, ...]