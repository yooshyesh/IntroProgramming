# plan: create class UsabilityStudy with objects from UsabilitySession
# method 1: load json filepath, keys are saved as objects ^ name set user_id = 1, 2, 3, 4,… for each entry
# Learning: SINGLE RESPONSABILITY PRINCIPLE > a class is only responsible for one thing
# enumerate auto-assigns numbers to tuples (start needs to be defined)
import json
import statistics

class UsabilitySession: # represents 1 object and its data
    def __init__(self, user_id, duration, success, backtracks):
        self.user_id = user_id
        self.duration = duration
        self.success = success
        self.backtracks = backtracks

    def is_successful(self):
        return self.success

    def has_many_backtracks(self, threshold=2):
        return self.backtracks > threshold

    def __str__(self):
        return f"- {self.user_id}, Dauer: {self.duration}s, Backtracks: {self.backtracks}"
    
class SmartphoneSession(UsabilitySession):
    def __init__(self, user_id, duration, success, backtracks, device_type):
        super().__init__(user_id, duration, success, backtracks)
        self.device_type = device_type
    def __str__(self):
        return f"- {self.user_id}, Dauer: {self.duration}s, Backtracks: {self.backtracks}, Geräteart: {self.device_type}"

class TabletSession(UsabilitySession):
    def __init__(self, user_id, duration, success, backtracks, device_type):
        super().__init__(user_id, duration, success, backtracks)
        self.device_type = device_type
    def __str__(self):
        return f"- {self.user_id}, Dauer: {self.duration}s, Backtracks: {self.backtracks}, Geräteart: {self.device_type}"
    
    
class UsabilityStudy(): # represents a collection of many objects and the logic behind managing them
    def __init__(self):
        self.sessions = []

    def load_from_json(self, filepath):
        with open(filepath, "r") as file:
            data = json.load(file)
        for user_id, entry in enumerate(data, start=1): # go through each line and entry in json file and number it
            session = UsabilitySession( # define Class with its content as one session
                user_id,
                entry["duration"],
                entry["success"],
                entry["backtracks"],
                if entry["device_type"] :
            )
            self.sessions.append(session)
    
    def average_duration(self):
        # durations = [] | for single_session in self.sessions: | durations.append(single_session.duration) | return statistics.mean(durations)
        return statistics.mean(int(session.duration for session in self.sessions))

    def count_successful_sessions(self):
        return sum(1 for s in self.sessions if s.is_successful())
    #successes = 0
        #for session in self.sessions:
           # if session.success:
            #    successes += 1
        #return successes
        
    def filter_sessions_with_many_backtracks_and_success(self):
        return [
            s for s in self.sessions
            if s.is_successful() and s.has_many_backtracks()
        ]
        #filtered_sessions = []
        #for session in self.sessions:
        #    if session.backtracks > 2 and session.success:
        #        filtered_sessions.append(session)
        #return filtered_sessions
    
    def save_evaluation(self, filepath):
        #successful = self.count_successful_sessions() # self. in front of other methods
        #avg_duration = round(self.average_duration())
        #filtered_u = self.filter_sessions_with_many_backtracks_and_success()

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(f"Erfolgreiche Nutzer:innen: {self.count_successful_sessions()}")
            file.write(f"Durchschnittliche Dauer: {int(self.average_duration())} Sekunden\n")
            file.write(f"Nutzer:innen mit >2 Backtracks und Erfolg:\n")
            for session in self.filter_sessions_with_many_backtracks_and_success():
                file.write(str(session) + "\n")

filepath = "Ordner_10/Programmierabgabe/usability_data.json"
study = UsabilityStudy()
study.load_from_json(filepath)
print(len(study.sessions)) 

