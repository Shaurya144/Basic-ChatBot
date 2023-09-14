# This code takes five films and asks the user to rate them 1 through 5 and responds accordingly

import random
import time

movies = ["Marvel", "Harry Potter", "Doctor Strange", "SpiderMan", "Mice of Men"]
strings = ["Haha ", "OOOOKKK Then ", "That's Nice "]

RandString = random.choice(strings)
movieSelect = random.choice(movies)


userThought = input("What do you think of " + str(movieSelect) + ".         ")

Rating = int(input(str(RandString) + str(movieSelect) + " give it a rating from 1  to 5        "))

time.sleep(1)

if Rating == 1:
    print("Sorry to hear That")
elif Rating == 2:
    print("Sounds like it was OK then?")
elif Rating == 3:
    print("Great to hear! I might watch it myself then!")
elif Rating == 4:
    print("I thought so too! I bet you can't wait to see it again.")
elif Rating > 5:
    print("Must have been really good!")
else:
    print("Wow, you really didn't like it then.")
