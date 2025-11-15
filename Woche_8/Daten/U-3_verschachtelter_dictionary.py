tasks = ["t1", "t2", "t3", "t4"]

studie = [
    {
        "user_id": "505",
        "tasks": [
            {"task_id": "t1", "duration": 40, "success": False}
        ]
    }
]

print(studie[0]["user_id"])
print(studie[0]["tasks"][0])