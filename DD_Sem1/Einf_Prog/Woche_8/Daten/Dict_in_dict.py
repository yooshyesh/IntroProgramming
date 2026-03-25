adressbuch: dict[str, dict[str, str]] = {
 "Anton": {"Telefon": "044 123 45 67", "Adresse": "Musterweg 1, 8000 Zürich"},
 "Beate": {"Telefon": "031 987 65 43", "Adresse": "Beispielweg 2, 3000 Bern"}
}
# Lesen: Telefonnummer von Anton ausgeben
print(adressbuch["Anton"]["Telefon"]) # Ausgabe: 044 123 45 67

# Schreiben: Adresse von Beate ändern
adressbuch["Beate"]["Adresse"] = "Neue Strasse 5, 3000 Bern"
print(adressbuch["Beate"]["Adresse"]) # Ausgabe: Neue Strasse 5, 3000 Bern