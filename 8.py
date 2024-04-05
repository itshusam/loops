import random
#1
number = random.randint(1,10)
guess = None
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("You guessed the correct number!")


#2
choise=["yes","no","maybe"]
question=input("what is your question?")
answer=random.choice(choise)

