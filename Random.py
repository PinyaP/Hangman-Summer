import random

print("")

#____________________ Random catagory ____________________ 
category = ["animal.txt", "food.txt", "fruit.txt", "occupation.txt", "place.txt"]
ranInCat = random.randint(0, 4) # Random index of category.
wordsFile = open(category[ranInCat]) # Open file by follow random index of category(ranInCat).
wordlist = wordsFile.readlines() # All posible word from wordsFile.

# Print to check.
print("File name: " + category[ranInCat])

#____________________ Random Level ____________________ 
level = ["NORMAL|50", "HARD|150", "LEGENDARY|200"]
randomLv = random.choice(level) # Random level by choice

# Index Level
nIndex = [1,2,3,4,5] # Index of normal level words.
hIndex = [7,8,9,10] # Index of hard level words.
lIndex = [12,13] # Index of Legendary level words.


# Print to check.
print("Level: " + randomLv)

#____________________ Random word ____________________ 
for i in wordlist: # run all posible word.

    i = i.strip("\n").strip("\r") # Delete \n and \r (return).

    # Check word to find Level that user get from random.
    if i == randomLv:

        if i == "NORMAL|50":
            ran = random.choice(nIndex) 
            point = 50
            word = str(wordlist[ran]).strip("\n").strip("\r")
            print("indexline: "+str(ran+1))
            
        elif i == "HARD|150":
            ran = random.choice(hIndex)
            point = 150
            word = str(wordlist[ran]).strip("\n").strip("\r")
            print("indexline: "+str(ran+1))

        elif i == "LEGENDARY|200":
            ran = random.choice(lIndex)
            point = 200
            word = str(wordlist[ran]).strip("\n").strip("\r")
            print("indexline: "+str(ran+1))
    
        print(word)

print("")

