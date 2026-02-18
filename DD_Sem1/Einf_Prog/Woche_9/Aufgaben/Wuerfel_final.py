import random

num_rolls = 100
dice_throws = []
def generate_dicethrows():
    for i in range(num_rolls):
        dice_throws.append(random.randint(1, 6))

throws = generate_dicethrows()

with open("dice_rolls.txt", "w") as file:
    for single_throw in throws:
        file.write(str(single_throw) + "\n")

print("Dice throws were registered.")

with open("dice_rolls.txt", "r") as file:
    inhalt = file.read()
    print(inhalt)
