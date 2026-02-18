registered: set[str] = {"Anna", "Bob", "Clara", "Diego"}
checkins: set[str] = ["Anna", "Edo", "Clara", "Anna"]
present = set()
unknown = set()

for person in checkins:
    if person in registered:
        present.add(person)
    else:
        unknown.add(person)

presence_quota = 100 / len(registered) * len(present)

print(f"Folgende Personen sind anwesend: {present}")
print(f"Folgende Personen sind unbekannt: {unknown}")
print(f"Prozent der Anwesenden: {presence_quota}")
