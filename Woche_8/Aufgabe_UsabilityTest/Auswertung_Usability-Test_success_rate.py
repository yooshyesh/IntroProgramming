# plan: A list of data, where only "success" is relevant for this part, unpack test_data dictionary "success" into variable, 100/len(test_data)*sucess_variable, return 
# execute: in a for loop, score/i/_ takes the position of the current dictionary it's looping through, test_data is defined outside the function, but before calling it, 
# IF defined within the function, no parameter is needed!
# learning: defining lists outside the function, but after makes the code more flexible
# when looping through dictionary, if score["success"]: is sufficient, because True is automatically true, == True is never needed

def calculate_success_rate(test_data):
    
    successes = 0
    for score in test_data:
        if score["success"]:
            successes += 1
    return 100/len(test_data) * successes

test_data = [ # list of dictionaries
    {"success": True,  "duration": 30, "backtracks": 1}, # dictionaries
    {"success": False, "duration": 75, "backtracks": 4},
    {"success": True,  "duration": 30, "backtracks": 0},
    {"success": True,  "duration": 60, "backtracks": 2},
    {"success": False, "duration": 90, "backtracks": 5}
]
print(calculate_success_rate(test_data))