import random

num_rolls = 100

def generate_dicethrows():
    dice_throws = []  # create the list inside the function
    for i in range(num_rolls):
        dice_throws.append(random.randint(1, 6))
    return dice_throws  # <-- return AFTER the loop

# Generate the throws
throws = generate_dicethrows()

# Write results to file
with open("dice_rolls.txt", "w") as file:
    for single_throw in throws:
        file.write(str(single_throw) + "\n")

print("Dice throws were registered.")

# Read and print the file content
with open("dice_rolls.txt", "r") as file:
    inhalt = file.read()
    print(inhalt)
