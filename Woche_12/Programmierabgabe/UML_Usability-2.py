"""Learning: Session brauchte eine Liste von tasks, muss also als Attribut 
festgelegt werden, wegen Testdaten
Vererbung vs. Attributesharing, bei super.init werden alle Atrribute/Methoden an
einen speziellen Untertyp der Klasse weitergegeben
Beim Weitergeben von den User-Attributen muss also ein Attribut zu den sessions
hinzugefügt werden. Wenn mit Vererbung > super.init, würde man alle Methoden von session überschreiben
Vererbung (class Child(Parent)): Child > spezieller Typ v. Parent z.B. SmartphoneSession / Session)
Komposition (Attribut): Wenn Child ein Parent-Objekt besitzt (z.B. Session besitzt ein User-Objekt)"""

class User():
    def __init__(self, name):
        self.name = name

class Session():
    def __init__(self, identifier, success, tasks, user):
        self.identifier = identifier
        self.success = success
        self.tasks = tasks
        self.user = user

    def get_total_duration(self):
        return sum(task.get_duration() for task in self.tasks)

class Task():
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def get_duration(self):
        return self.duration
    
class SmartphoneSession(Session):
    def __init__(self, identifier, success, tasks, user, device_type):
        super().__init__(identifier, success, tasks, user)
        self.device_type = device_type

class TabletSession(Session):
    def __init__(self, identifier, success, tasks, user, device_type):
        super().__init__(identifier, success, user, tasks)
        self.device_type = device_type
    
tasks = [Task("Bestelle Produkt X", 45), Task("Bestelle Produkt Y", 35)]
session = SmartphoneSession("Session 3", False, tasks, "iPhone")
print(session.identifier)
print(session.success)
print(session.device_type)
print(session.get_total_duration())
