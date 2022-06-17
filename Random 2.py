
import random

category = ["animal.txt", "food.txt", "fruit.txt", "occupation.txt", "place.txt"]
file_name = random.choice(category)
fileW = open(file_name,'r')


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
#กรณีindexไปทับกับบรรทัด level
if index in [0,6,11]:
    index +=1 

wordlist = fileW.readlines()
print(randomLv)
print(f"category {file_name}")
print("index:" , index)
print(wordlist[index])
    
    
        




#print(wordlist)



