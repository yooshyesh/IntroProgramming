# Berechne den Durchschnitt aller Werte. Ignoriere 0.

# scores = [58, 72, 0, 91, 65]
scores: list[int] = [58, 72, 0, 91, 65] # dictionary mit integers erstellen

total = 0 # what variables are useful for the operations?
count = 0 # define globally

for score in scores:
    print(score)
    if score != 0: # 0 wird ignoriert
        total += score # adding scores
        count += 1 # adding 1 to count for each score

avg = total / count if count else 0
if avg >= 60:
    print("Kursziel erreicht:", round(avg, 1))
else:
    print("Kursziel nicht erreicht:", round(avg, 1))

scores.append(77)
print(scores)

#def sort_list():
 #   scores.sort()
 #   return
  #  print(scores)

# coded for single use = BAD
#def average(scores):
    #total = scores[1] + scores[2] + scores[3] + scores[4] + scores[5]
   # new_total = total/4
   # return
   # if new_total >= 60:
   #     print("Kursziel nicht erreicht.")
   # else:
   #     print("Kursziel erreicht.")

#sort_list()
#average(scores)