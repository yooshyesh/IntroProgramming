"""Plan: define func with parameter filepath, write txt-file with return statements from analyze data
Execute:
Learnings:
"""
import math


def analyze_data(data):
    
    success_count = 0
    for score in data:
        if score["success"]:
            success_count +=1

    durations = [entry["duration"] for entry in data] # create list durations from keys "duration" in data
    count = 0
    total = 0
    for entry in durations:
        total += entry
        count += 1
    avg_duration = total / count
    avg_duration = math.floor(avg_duration)

    filtered_users = []
    for entry in data:
        if entry["backtracks"] > 2 and entry["success"]:
            filtered_users.append(entry)

    if avg_duration.is_integer():
        avg_duration = int(avg_duration)

    return success_count, avg_duration, filtered_users

data = [
    {"success": True,  "duration": 30, "backtracks": 1},
    {"success": False, "duration": 75, "backtracks": 4},
    {"success": True,  "duration": 30, "backtracks": 0},
    {"success": True,  "duration": 60, "backtracks": 2},
    {"success": False, "duration": 90, "backtracks": 5}
]
analyze_data(data)

#def write_evaluation_to_file(filepath, success_count, avg_duration, filtered_users):
#    with open(filepath, "w", encoding="utf-8") as file:
#        file.write(f"Erfolgreiche Nutzer:innen: {success_count}\n") 
#        file.write(f"Durchschnittliche Dauer: {avg_duration} Sekunden\n")
#        file.write(f"Nutzer:innen mit >2 Backtracks und Erfolg:\n")
#        for user in filtered_users:
 #           file.write(f"- Dauer: {user['duration']}, Backtracks: {user['backtracks']}\n")
def write_evaluation_to_file(filepath, success_count, avg_duration, filtered_users):
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(f"Erfolgreiche Nutzer:innen: {success_count}\n") 
        file.write(f"Durchschnittliche Dauer: {int(avg_duration)} Sekunden\n")
        file.write(f"Nutzer:innen mit >2 Backtracks und Erfolg:\n")
        for user in filtered_users:
            file.write(f"- Dauer: {user['duration']}, Backtracks: {user['backtracks']}\n")

    # with open(filepath, "r", encoding="utf-8") as file:
    #    print(file.read())
    # return

results = analyze_data(data)
success_count, avg_duration, filtered_users = results
# write_evaluation_to_file("filepath", success_count, avg_duration, filtered_users)
print(write_evaluation_to_file("evalutation.txt", success_count, avg_duration, filtered_users))
