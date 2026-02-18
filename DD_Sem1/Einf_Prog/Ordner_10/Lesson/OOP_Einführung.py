# Basisklasse für alle Medien.
# Jedes Medium besitzt eine ID.
class Medium:
    def __init__(self, id):
        self.id = id # self ist eine Referenz auf das aktuelle Projekt, also hier das Objekt, das gerade initialisiert wird.

    def __str__(self):
        return f"Medium-ID: {self.id}"

# Jedes Buch ist ein Medium.
# Buch erbt von Medium und fügt Titel und Autor hinzu.
class Buch(Medium):
    def __init__(self, id, title, autor):
        super().__init__(id) # Initialisiert die ID aus der Basisklasse.
        self.title = title
        self.autor = autor

    def printInfo(self):
        print(f"Titel: {self.title}, Autor: {self.autor}")

    # __str__ wird aufgerufen, wenn das Objekt als STring dargestellt werden soll (z.B. in der print-Funktion).
    def __str__(self):
        return f"Buch: '{self.title}' von {self.autor} (ID: {self.id})" # In einer Subklasse (Buch) können auch Attribute einer Superklasse (Medium) verwendet werden.

# Jedes E-Book ist ein Buch.
# E-Book erbt von Buch und fügt Format hinzu.
class EBook(Buch):
    def __init__(self, id, title, autor, format):
        super().__init__(id, title, autor) # Initialisiert die Attribute der Basisklasse.
        self.format = format
    
    def printInfo(self):
        print(f"Titel: {self.title}, Autor: {self.autor}, Format: {self.format}")

    def __str__(self):
        return f"E-Book: '{self.title}' von {self.autor}, Format: {self.format} (ID: {self.id})"

# Um mit Klassen arbeiten zu können, müssen wir Instanzen erstellen.
derProzess = Buch(1, "Der Prozess", "Franz Kafka")
eurotrash = Buch(2, "Eurotrash", "Christian Kracht")
homoFaber = EBook(3, "Homo Faber", "Max Frisch", "Tolino")

# Ausgabe, es werden die __str__-Funktionen der Objekte verwendet.
print(derProzess)
print(eurotrash)
print(homoFaber)
