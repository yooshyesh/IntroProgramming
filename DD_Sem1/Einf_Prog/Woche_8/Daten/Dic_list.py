sehenswürdigkeiten: Dict[str, List[str]] = {
 "Appenzell": ["Landsgemeindeplatz", "Museum Appenzell", "Kirche St.
Mauritius"],
 "Rapperswil": ["Schloss Rapperswil", "Holzbrücke", "Kinderzoo"],
 "St. Gallen": ["Stiftsbibliothek", "Kathedrale", "Roter Platz"],
 "Wil": ["Altstadt Wil", "Stadtweier", "Baronenhaus"],
 "Zürich": ["Grossmünster", "Fraumünster", "Uetliberg"]
}
# Lesen: z.B. die zweite Sehenswürdigkeit von Zürich ausgeben
print(sehenswürdigkeiten["Zürich"][1]) # Ausgabe: Fraumünster
# Schreiben: eine neue Sehenswürdigkeit zu Zürich hinzufügen
sehenswürdigkeiten["Zürich"].append("Opernhaus")
