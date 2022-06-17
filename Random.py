
import random

category = ["animal.txt", "food.txt", "fruit.txt", "occupation.txt", "place.txt"]
fileW = open(random.choice(category),'r')


level = {"NORMAL|50":1, "HARD|150":7, "LEGENDAR|200":12}
level_list = list(level)
randomLv = random.choice(list(level))



indexlevel = level_list.index(randomLv)
if indexlevel < len(level_list) - 1:
    indexlevel += 1
    index_stop = level[level_list[indexlevel]]
else:
    index_stop = 13

index = random.randint(level[randomLv] ,index_stop)
print(index)
if index in [0,6,11]:
    index +=1 

wordlist = fileW.readlines()
print(wordlist[index])
    
    
        




#print(wordlist)



