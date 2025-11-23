import math
import csv
import statistics


def analyze_data(data):
    
    success_count = 0
    for score in data:
        if score["success"]:
            success_count +=1

    durations = [entry["duration"] for entry in data]
    avg_duration = statistics.mean(durations)

    filtered_users = []
    for entry in data:
        if entry["backtracks"] > 2 and entry["success"]:
            filtered_users.append(entry)

    return success_count, avg_duration, filtered_users

def load_csv_data(filepath):
    data = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            entry = {
                "user_id": int(row["user_id"]),
                "success": row["success"].lower() == "true",  # string -> bool
                "duration": int(row["duration"]),
                "backtracks": int(row["backtracks"])
            }
            data.append(entry)
    return data

csv_data = load_csv_data("Woche_9/Programmierabgabe/usability_data.csv")
analyze_data(csv_data)
