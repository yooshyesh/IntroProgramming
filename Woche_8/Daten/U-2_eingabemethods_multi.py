# Jede Testperson kann mehrere Geräte (z.B. "Smartphone", "Notebook") verwenden. Du möchtest
# speichern, welche Geräte ein Nutzer verwendet. Jedes Gerät wird nur einmal verwendet.


# Liste macht keinen Sinn, da Werte nicht verändert werden müssen
# user: list[tuple[str, str]] = [(user1)]

# dictionary verwenden, da devices nur 1 Mal verwendet werden

devices = {
    "user_1": {"Smartphone"}
    "user_2": {"Tablet"}
    "user_3": {"Smartphone", "Tablet"}
}