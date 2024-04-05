import random
#1
for i in range(3):
    for j in range(3):
        print("*", end="")
    print("\n")

#2
mood=["happy","sad","calm","energetic"]
days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
times = ["morning", "afternoon", "evening"]
for day in days:
    for time in times:
        num=random.randrange(1,4)
        print("it's ",day," ",time," time and i feel ",mood[num],end="\n")

#3
for i in range(1,6):
    for o in range(1,11):
        print(i,"*",o,"=",i*o,end="   ")
    print("\n")