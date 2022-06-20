
import random
score = 0 
def random_word():
    global score
    
    played = []
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
    word = wordlist[index].strip("\n").strip("\r")
    if(word in played):
        random_word()
    played.append(word)
    

    wordscore = 0
    if ("50" in randomLv):
        wordscore = 50 
    elif ("150" in randomLv):
        wordscore = 150 
    elif ("200" in randomLv):
        wordscore = 200 
    
    print(randomLv)
    print(wordscore)
    print(f"category {file_name}")
    print("index:" , index)
    print(word)
    
    
    score += play(word,wordscore)
    print(score)


    
    

def play(word,wordscore):
    quantity_cha = len(word)
    correct_word = []
    incorrect_word = []
    chance = 7
    if(" " in word):
        quantity_cha -= 1
    while(chance > 0):
        input_character = input("input character: ")
        
        if(input_character in word):
            if(word.count(input_character) > 1):
                for i in range(0,word.count(input_character)):
                    correct_word.append(input_character)
            else:
                correct_word.append(input_character)
            print("TRUE")
            
            if(len(correct_word) == quantity_cha):
                print("your word correct")
                return wordscore
        
        elif(input_character in incorrect_word):
            print("you have chosen")

        else:
            incorrect_word.append(input_character)
            print("FALSE")
            chance -= 1
        
    print("GAME OVER")

random_word()


    
    
        








