scores = [58, 72, 0, 91, 65]

scores.remove(0)
average = sum(scores) / len(scores)
if average >= 60:
    print("Kursziel erreicht")
else:
    print("Kursziel nicht erreicht")

scores.append(77)
print(sum(scores))