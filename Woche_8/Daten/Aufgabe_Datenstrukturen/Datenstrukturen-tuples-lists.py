"""Ein Kühlraum soll zwischen 18.0°C und 24.0°C betrieben werden. Der zulässige Bereich ist als Tuple
definiert: """

"""Aufgabe
. Prüfe jeden Messwert.
. Gib eine Meldung aus, wenn ein Wert nicht im zulässigen Bereich liegt (also unter allowed[0] oder
über allowed[1]).
. Berechne wieviel Prozent der Messwerte im erlaubten Bereich liegen."""
def main():
    allowed = (18.0, 24.0) # tuple
    temps = [19.5, 25.0, 22.1, 17.9, 21.3] # list

    ok = 0
    for temp in temps:
        if temp > allowed[0] and temp < allowed[1]:
            ok += 1 # Werte, die in range sind, zu ok addieren
        else:
            print(f"Temperatur {temp} liegt nicht im zulässigen Bereich.")

    ratio = (ok / len(temps)) * 100
    print(ratio)
    print(f"{ratio:.1f}% der Messwerte liegen im zulässigen Bereich.")

main()

#for temp in temps:
 #   if temp < allowed[0]:
  #      print(temp, "low temp")
   # if temp > allowed[1]:
    #    print(temp, "high temp")