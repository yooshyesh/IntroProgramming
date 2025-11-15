kommentare = [
    {"text": "Die Navigation war klar.", "bewertung": "positiv"},
    {"text": "Ich habe den Warenkorb nicht gefunden.", "bewertung": "negativ"},
    {"text": "Zu viele Klicks nötig.", "bewertung": "negativ"},
    {"text": "Sehr gute Suchfunktion!", "bewertung": "positiv"},
]

for k in kommentare: # k steht fuer Kategorie in kommentare
    if (k["bewertung"] == "positiv"):
        positiv = positiv + 1
    elif (k["bewertung"] == "negativ"):
        negativ = negativ + 1
    elif (k["bewertung"] == "neutral"):
        neutral = neutral + 1

print(f"Positive Kommentrare: {positiv}.")
print(f"Negative Kommentrare: {negativ}.")