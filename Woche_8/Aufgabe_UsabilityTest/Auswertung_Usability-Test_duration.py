# plan: unpack durations into list, add all durations together / len(durations), return
# execute: variables total and count need to be defined in fuction, if global, python will not recognize count outside and within as the same variable
# instead of using avg = total / count, return does the same without defining an unused variable
# durations = [entry["duration"] for entry in test_data] > list comprehension > compact way to create a new list from an existing list, dictionary, or range
# entry(could be any keyword) stands for every line in test_data, entry["duration"] value that belongs to the key "duration",The square brackets mean: “put all those extracted values into a new list.”

def average_duration(test_data):
    durations = [entry["duration"] for entry in test_data]
    count = 0
    total = 0
    for entry in durations:
        total += entry
        count += 1
    return total / count

test_data = [ # list of dictionaries
    {"success": True,  "duration": 30, "backtracks": 1}, # dictionaries
    {"success": False, "duration": 75, "backtracks": 4},
    {"success": True,  "duration": 30, "backtracks": 0},
    {"success": True,  "duration": 60, "backtracks": 2},
    {"success": False, "duration": 90, "backtracks": 5}
]
print(average_duration(test_data))