#1
marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
#we have 0 marshmallows and the loop adds 1 everytime till we get 5 then the loop ends

#2
marshmallows = 0
while marshmallows < 5:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1
#when we place the + on the end of the loop it excutes all the commands before adding 1 to the marshmallows


#3
marshmallows = 0
while marshmallows < 10:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    
#we can fix that by putting the increment before the print statement
