class Session: # represents 1 object and its data
    def __init__(self, identifier, success):
        self.identifier = identifier
        self.success = success

    def get_total_duration():
        pass
    
class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def get_duration():
        pass

class SmartphoneSession(Session):
    def __init__(self, device_type):
        super().__init__(self, identifier, success):
        self.device_type = device_type
    def __str__(self):
        return f"Smartphone: {self.device_type}"

class TabletSession(Session):
    def __init__(self, user_id, duration, success, backtracks, device_type):
        super().__init__(user_id, duration, success, backtracks)
        self.device_type = device_type
    def __str__(self):
        return f"Tablet: {self.device_type}"

