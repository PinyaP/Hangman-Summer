import random

print("")

#____________________ Random catagory ____________________ 
category = ["animal", "food", "fruit", "occupation", "place"]
fileName = random.choice(category)
wordsFile = open(fileName+".txt", 'r') # Open file by follow the random index of category(ranInCat).
wordlist = wordsFile.readlines() # All possible word from wordsFile.

# Print to check.
print("Category: " + fileName)

#____________________ Random Level ____________________ 
level = ["NORMAL|50", "HARD|150", "LEGENDARY|200"]
randomLv = random.choice(level) # Random level by choice.

# Index Level
nIndex = [1,2,3,4,5] # Index of normal level words.
hIndex = [7,8,9,10] # Index of hard level words.
lIndex = [12,13] # Index of Legendary level words.


# Print to check.
print("Level: " + randomLv)

#____________________ Random word ____________________ 
for i in wordlist: # run all possible word.

    i = i.strip("\n").strip("\r") # Delete \n and \r (return).

    # Check word to find Level that user get from random.
    if i == randomLv:

        if i == "NORMAL|50":
            ran = random.choice(nIndex)  # Random index of those level.
            point = 50
            word = str(wordlist[ran]).strip("\n").strip("\r") # Random word from random category wordlist.
            print("indexline: "+str(ran+1)) # Print to check indexline (ran + 1 for people easy to find word on file).
            
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

