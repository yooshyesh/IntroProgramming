kommentare = [
    ("Die Navigation war klar.", "positiv",
    "Ich habe den Warenkorb nicht gefunden.", "negativ",
    "Zu viele Klicks nötig.", "negativ",
    "Sehr gute Suchfunktion!", "positiv",
     )
]

positiv:int = 0
negativ:int = 0
neutral:int = 0

for k in kommentare: # k steht fuer Kategorie in kommentare
    if (k[1] == "positiv"):
        positiv = positiv + 1
    elif (k[1] == "negativ"):
        negativ = negativ + 1
    elif (k[1] == "neutral"):
        neutral = neutral + 1

print(f"Positive Kommentrare: {positiv}.")
print(f"Negative Kommentrare: {negativ}.")



