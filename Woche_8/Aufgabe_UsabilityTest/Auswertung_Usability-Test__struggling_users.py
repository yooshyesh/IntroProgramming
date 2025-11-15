# plan: Search dictionaries in list for max values and return those that surpass those with if entry["x"] > max(x) return
# execute: 
# learnings:
test_data = [ # list of dictionaries
    {"success": True,  "duration": 30, "backtracks": 1}, # dictionaries
    {"success": False, "duration": 75, "backtracks": 4},
    {"success": True,  "duration": 30, "backtracks": 0},
    {"success": True,  "duration": 60, "backtracks": 2},
    {"success": False, "duration": 90, "backtracks": 5}
]
max_duration = 74
max_backtracks = 3
def find_struggling_users(test_data, max_duration, max_backtracks):
    struggling = []
    for entry in test_data:
        if entry["duration"] > max_duration and entry["backtracks"] > max_backtracks:
            struggling.append(entry)
    return struggling

print(find_struggling_users(test_data, max_duration, max_backtracks))