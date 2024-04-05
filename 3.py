import random
#1
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#2
mood=["happy","sad","calm","energetic"]
lunch_time=7
for i in range(1,25):
    if i==lunch_time:
        continue
    num=random.randrange(0,4)
    print("it's ",i," O'clock and i feel ",mood[num])

#3
numbers=[1,5,7,99,44,32,11,4,29]
number=input("please enter a number between 1 and 40")
for i in numbers:
    if i==number:
        break
else: print("sorry number not found")
        