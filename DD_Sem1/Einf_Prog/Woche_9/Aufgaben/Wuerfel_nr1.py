import random

def generate_dicethrows():
    dice_throws = []

    for i in range(100):
        dice_throws.append(random.randint(1,6))
    return dice_throws

#Variable muss noch definiert werden

throws = generate_dicethrows()

with open("dice_rolls.txt", "w") as file:
    for single_throw in throws:
        file.write(str(single_throw) + "\n") # new line muss in str ausgegeben werden

print("Dice throws were registered.")
