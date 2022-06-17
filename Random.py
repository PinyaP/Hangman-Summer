import random

category = ["animal.txt", "food.txt", "fruit.txt", "occupation.txt", "place.txt"]
fileW = open(random.choice(category),'r')


level = {"NORMAL|50":5, "HARD|150":4, "LEGENDAR|200":2}
randomLv = random.choice(list(level))

#print(randomLv, line)

#print(level["NORMAL"])

wordlist = fileW.readlines()
for word in wordlist:
    if word == randomLv:
        print(word)




#print(wordlist)




