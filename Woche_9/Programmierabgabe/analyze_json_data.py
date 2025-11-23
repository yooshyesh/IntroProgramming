"""Plan: define func that counts amounts of true/false in success, avg bearbdauer, more than 2 backtracks
Execute:
Learnings: count variable can be skipped with len() function
+= to variable can be skipped with list.append()
"""
import statistics

def analyze_data(data):
    
    # success_count = 0
    successful = []
    for score in data:
        if score["success"]:
            # success_count +=1
            successful.append(score)

    #durations = [entry["duration"] for entry in data] # create list durations from keys "duration" in data
    # ^ungültiges Python
    # count = 0
    durations = []
    total = 0
    for entry in durations:
        durations.append(entry["durations"])# total += entry
        # count += 1
    # avg_duration = total / len(total)
    avg_duration = statistics.mean(durations)

    filtered_users = []
    for entry in data:
        if entry["backtracks"] > 2 and entry["success"]:
            filtered_users.append(entry)

    return len(successful), avg_duration, filtered_users # len() da Anzahl bestanden gefragt ist
    # return success_count

data = [
    {"success": True,  "duration": 30, "backtracks": 1},
    {"success": False, "duration": 75, "backtracks": 4},
    {"success": True,  "duration": 30, "backtracks": 0},
    {"success": True,  "duration": 60, "backtracks": 2},
    {"success": False, "duration": 90, "backtracks": 5}
]
print(analyze_data(data))