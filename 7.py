import random

# Initialize a dictionary to keep track of dice roll frequencies
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Let's roll the dice 10 times
for _ in range(10):
    dice_roll = random.randint(1, 6)
    # Update the roll_count dictionary
    roll_count[dice_roll] += 1
    print("You rolled a " + str(dice_roll) + "!")

# Print out the frequency of each number
for number, frequency in roll_count.items():
    print(f"Number {number} was rolled {frequency} times.")

#2
mylist=["iron","gold","silver","plastic"]

yourpick=input("please guess one (gold,iron,silver,plastic)")
pick=random.choice(mylist)
print(pick)
if yourpick==pick:
    print("you made the right choise")
else:
    print("your guess was wrong")

#3
deck = ['7 of Hearts', 'king of Diamonds', '10 of Clubs', 'queen of Spades']
print (deck)
random.shuffle(deck)
print (deck)