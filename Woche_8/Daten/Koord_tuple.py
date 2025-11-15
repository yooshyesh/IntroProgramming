ort_beschreibung: dict[tuple[float, float], dict[str, str]] = {
 (46.9481, 7.4474): {"Name": "Bundeshaus Bern", "Beschreibung": "Sitz der Schweizer Regierung"},
 (47.2266, 8.8167): {"Name": "OST Campus Rapperswil", "Beschreibung": "Campus der OST in Rapperswil"},
 (47.4239, 9.3748): {"Name": "Stiftsbibliothek St. Gallen","Beschreibung": "UNESCO-Weltkulturerbe und historische Bibliothek"},
 (47.0502, 8.3093): {"Name": "Kapellbrücke Luzern", "Beschreibung": "Historische Holzbrücke in Luzern"}
}
# Lesen: Beschreibung für eine gegebene Koordinate ausgeben
print(ort_beschreibung[(46.9481, 7.4474)]["Beschreibung"])
# Ausgabe: Sitz der Schweizer Regierung
# Schreiben (1): Beschreibung eines bestehenden Eintrags ändern
ort_beschreibung[(47.0502, 8.3093)]["Beschreibung"] = "Historische gedeckte Holzbrücke in Luzern"
print(ort_beschreibung[(47.0502, 8.3093)]["Beschreibung"])
# Ausgabe: Historische gedeckte Holzbrücke in Luzern