temps = [19.5, 25.0, 22.1, 17.9, 21.3]
allowed = (18.0, 24.0) # zulässiger Bereich

ok = 0 # zählt Menge der Werte innerhalb des zulässigen Bereich
for t in temps:
    if t > allowed[0] and t < allowed[1]: # innerhalb zulässigen Bereich
        ok += 1 # fügt Anzahl Werte welche innerhalb des zulässigen Bereich liegen hinzu
    else:
        print(f"Temperatur {t} liegt nicht im zulässigen Bereich.")

ratio = (ok / len(temps)) * 100
print(ratio)

print(f"{ratio:.1f}% der Messwerte liegen im zulässigen Bereich.")