grades: dict[str, float] = {"Anna": 5.0, "Bob": 4.0, "Clara": 5.5, "Diego": 3.5}
total = 0
for name in grades.keys():
    note = grades[name]
    if note >= 4.0:
        status = "bestanden"
    else:
        status = "nicht bestanden"
    print(f"{name}: {note:.1f} – {status}")
    total += note

avg = total / len(grades) if grades else 0
print(f"Klassendurchschnitt: {avg:.2f}")