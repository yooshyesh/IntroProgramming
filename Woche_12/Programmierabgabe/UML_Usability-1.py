"""Learning: Session brauchte eine Liste von tasks, muss also als Attribut 
festgelegt werden, wegen Testdaten"""

class Session(): 
    def __init__(self, identifier, success, tasks):
        self.identifier = identifier
        self.success = success
        self.tasks = tasks

    def get_total_duration(self):
        return sum(task.get_duration() for task in self.tasks)

class Task():
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def get_duration(self):
        return self.duration
    
class SmartphoneSession(Session):
    def __init__(self, identifier, success, tasks, device_type):
        super().__init__(identifier, success, tasks)
        self.device_type = device_type

class TabletSession(Session):
    def __init__(self, identifier, success, tasks, device_type):
        super().__init__(identifier, success, tasks)
        self.device_type = device_type
    
tasks = [Task("Bestelle Produkt X", 45), Task("Bestelle Produkt Y", 35)]
session = SmartphoneSession("Session 3", False, tasks, "iPhone")
print(session.identifier)
print(session.success)
print(session.device_type)
print(session.get_total_duration())
