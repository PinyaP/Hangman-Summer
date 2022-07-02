from tkinter import *
import random

global user_name
global wordscore
global word
global file_name
global hangman_game
global the_word_withSpaces

count = 0
user_score = 0

def buttonExit(window):   
    window.destroy()                                    
    mainGUI.deiconify()                 #เปิดmainGUIอีกครั้ง                         
    button_newgame["state"] = "normal"  
    button_score["state"] = "normal"   

def login():                                  
    mainGUI.iconify()                        
    def start_game():
        global user_name
        user_name = enter_name.get()           
        print(user_name)
        login_window.destroy()
        hangman()
    
    login_window = Toplevel(mainGUI)
    login_window.title("L O G I N")
    login_window.geometry("550x260+350+200")
    login_window.resizable(0, 0)
    canvas_login = Canvas(login_window,bg="#191970")
    canvas_login.pack(fill="both", expand=True)

    canvas_login.create_image(0,0,image=bg_login,anchor="nw")
    canvas_login.create_text(270, 50, text="Enter Your Name",fill="white", font="Times 26 bold",justify="center")
    canvas_login.create_text(272, 50, text="Enter Your Name",fill="red", font="Times 26 bold",justify="center")
    enter_name = Entry(canvas_login, width=16, font="Times 26 bold", justify="center", bg="#FFE5B4") #ช่องที่ให้ผู้ใช้กรอกชื่อ
    canvas_login.create_window(270, 100, window=enter_name)
    
    start_button = Button(login_window, text="S T A R T", height=1, width=24, command=start_game, state=NORMAL,relief="raised", background='white')
    button_exit_login = Button(login_window, text="E X I T",fg = "red", height=1, width=24, command=lambda:buttonExit(login_window), state=NORMAL,relief="raised", background='white')
    
    start_button.place(x=270, y=160, anchor="center")
    button_exit_login.place(x=270, y=200, anchor="center")
 

    
def score_board():                           
    mainGUI.iconify()                          
    f = open("score.txt", "r")      #อ่านscore board จากไฟล์
    scoreList = f.read()
    f.close()
    
    score_window = Toplevel(mainGUI)
    score_window.title("L E A D E R   B O A R D")
    score_window.geometry("400x700+10+20")
    score_window.resizable(0, 0)
    canvas_score = Canvas(score_window)      
    
    canvas_score.pack(fill="both", expand=True)                          
    canvas_score.create_image(0, 0, image=bg_score, anchor="nw")     

    canvas_score.create_text(200, 80, text="L E A D E R   B O A R D", fill="white", font="Forte 30",justify="center")
    canvas_score.create_text(200, 120, text=scoreList,fill="white", font="Forte 18", justify="center", anchor="n")
    button_exit_score = Button(score_window, text="E X I T", fg='red', width=26,command=lambda:buttonExit(score_window), state=NORMAL, font="Forte 16")
    button_exit_score.place(x=200, y=580, anchor="center")

def hangman():
    
    global the_word_withSpaces
    global wordscore
    global word
    global file_name
    global user_score
    global hangman_game
                   
    game_window = Toplevel(mainGUI)
    game_window.geometry('915x700')
    game_window.resizable(0,0)
    
    hangman_game = Canvas(game_window,width=905,height=700,bg="#E7FFFF") 
    hangman_game.pack(fill="both", expand=True)
    
    hangman_game.create_image(0, 0, image=bg_game, anchor="nw")     
     
    hangman_game.create_text(119, 30, text=("Player: "+user_name), fill="black", font=(None,20))
    hangman_game.create_text(92,75,text=("Score " + str(user_score)),fill="black",font=(None,20))
    picture = hangman_game.create_image(90 , 10, image= h1 , anchor="nw")
    
    random_word()
    
    hangman_game.create_text(757,30,text=("Word Score:" + str(wordscore)),fill="black",font=(None,20))
    hangman_game.create_text(757,75,text=("Category: " + file_name),fill="black",font=(None,20))
    
    x=500
    if x+(len(word)*30) > 915:
        x = 300
    else:
        x = 500
    
    lblWord = StringVar()
    the_word_withSpaces=" ".join(word)
    lblWord.set((" ".join("_"*len(word))))
    hangman_game.create_text(550,250,text=lblWord.get(),font=("Consolas 24 bold"))
    
    
    photos = [PhotoImage(file="h1.png"), PhotoImage(file="h2.png"), PhotoImage(file="h3.png"), PhotoImage(file="h4.png"),
          PhotoImage(file="h5.png"), PhotoImage(file="h6.png"), PhotoImage(file="h7.png")]
    
    # for i in range(0,len(word)):
    #     x += 30
    #     if word[i] == " ":
    #         exec('guess{}=hangman_game.create_text({},250,text=" ",font=(None,25))'.format(i,x))
    #     else:
    #         exec('guess{}=hangman_game.create_text({},250,text="_",font=(None,25))'.format(i,x))

    
    #row1
    btnA = Button(game_window, text="A", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnA)) 
    btnA.place(x=60, y=470)
    btnB = Button(game_window, text="B", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnB)) 
    btnB.place(x=150, y=470)
    btnC = Button(game_window, text="C", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnC)) 
    btnC.place(x=240, y=470)
    btnD = Button(game_window, text="D", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnD)) 
    btnD.place(x=330, y=470)
    btnE = Button(game_window, text="E", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnE)) 
    btnE.place(x=420, y=470)
    btnF = Button(game_window, text="I", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnF)) 
    btnF.place(x=510, y=470)
    btnG = Button(game_window, text="G", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnG)) 
    btnG.place(x=600, y=470)
    btnH = Button(game_window, text="H", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnH)) 
    btnH.place(x=690, y=470)
    btnI = Button(game_window, text="F", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnI)) 
    btnI.place(x=780, y=470)
        
        #row2
    btnJ = Button(game_window, text="J", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnJ)) 
    btnJ.place(x=15, y=535)
    btnK = Button(game_window, text="K", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnK)) 
    btnK.place(x=105, y=535)
    btnL = Button(game_window, text="L", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnL)) 
    btnL.place(x=195, y=535)
    btnM = Button(game_window, text="M", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnM)) 
    btnM.place(x=285, y=535)
    btnN = Button(game_window, text="N", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnN)) 
    btnN.place(x=375, y=535)
    btnO = Button(game_window, text="O", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnO)) 
    btnO.place(x=465, y=535)
    btnP = Button(game_window, text="P", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnP)) 
    btnP.place(x=555, y=535)
    btnQ = Button(game_window, text="Q", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnQ)) 
    btnQ.place(x=645, y=535)
    btnR = Button(game_window, text="R", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnR)) 
    btnR.place(x=735, y=535)
    btnS = Button(game_window, text="S", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnS)) 
    btnS.place(x=825, y=535)
        
        #row3
    btnT = Button(game_window, text="T", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnT)) 
    btnT.place(x=150, y=600)
    btnU = Button(game_window, text="U", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnU)) 
    btnU.place(x=240, y=600)
    btnV = Button(game_window, text="V", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnV)) 
    btnV.place(x=330, y=600)
    btnW = Button(game_window, text="W", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnW)) 
    btnW.place(x=420, y=600)
    btnX = Button(game_window, text="X", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnX)) 
    btnX.place(x=510, y=600)
    btnY = Button(game_window, text="Y", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnY)) 
    btnY.place(x=600, y=600)
    btnZ = Button(game_window, text="Z", width = 4, state=NORMAL, font=(None,20),bg = "#FFE7BF",command=lambda:word_on(btnZ)) 
    btnZ.place(x=690, y=600)
    btnl = Button(game_window,image=bg_light,anchor="center",width=60,height=65)
    btnl.place(x=17, y=610)
    btnskip = Button(game_window,image=bg_skip,anchor="center",width=52,height=52)
    btnskip.place(x=840, y=610)
    
    
    def guess(letter):
        global count
        
        if count<6:
            txt=list(the_word_withSpaces)
            guessed=list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        lblWord.set(("".join(guessed)))
            else:
                count+=1
                hangman_game.itemconfig(picture,image=photos[count])
                
    
    def word_on(button):
        button.place_forget()
        my_text = button['text'].lower()
        guess(my_text) 
    
# def show_word(alphabet):
#     global word
#     global count
    
#     for i in range(len(word)):
#         if alphabet == word[i]:
#             exec('hangman_game.itemconfig(guess{},text=str(alphabet))'.format(i))
#         else:
#             count+=1
                       
    
def random_word():
    global wordscore
    global word
    global file_name
    
    played = []
    category = ["animal", "food", "fruit", "occupation", "place"]
    file_name = random.choice(category)
    fileW = open(file_name+".txt",'r')

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
    if ("200" in randomLv):
        wordscore = 200 
    elif ("150" in randomLv):
        wordscore = 150 
    elif ("50" in randomLv):
        wordscore = 50 
    
    
    print(randomLv)
    print(wordscore)
    print(f"category {file_name}")
    print("index:" , index)
    print(word)
    
########################################################
# def word_on(alphabet):
#     global word
#     exec('btn{}.place_forget()'.format(alphabet))
#     if alphabet in word:
#         exec('hangman_game.create_text(500+(len(word)*30),250,text="{}",font=(None,25))'.format(alphabet))
        



mainGUI = Tk()                                                           
mainGUI.geometry("640x480+300+200")                                              
mainGUI.resizable(0, 0)                                           #ไม่่สามารถปรับหน้าจอเองได้

mainGUI.title("H  A  N  G  M  A  N")                           

user_name = ""                                            #User name                           
bg_score = PhotoImage(file="train.png")                                
bg_game = PhotoImage(file="sky.png")                               
bg_logo = PhotoImage(file="hanged.png")
h1 = PhotoImage(file="h1.png")
bg_light = PhotoImage(file="light2.png")
bg_login = PhotoImage(file="sunflower.png")
bg_skip = PhotoImage(file="skip btn1.png")


# al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# for let in al:
#     exec('{}=PhotoImage(file="{}.png")'.format(let,let))


canvas_main = Canvas(mainGUI,width=640, height=480,bg= '#E7FFFF')                                #เป็นการวาดรูปสร้างออปเจ็กขึ้นมาทับที่mainGUI            
canvas_main.pack(fill="both", expand=True)                                            

canvas_main.create_text(320, 35, text="HANGMAN GAME", fill="yellow", font="Forte 34 bold", justify="center", anchor="n")
canvas_main.create_text(323, 35, text="HANGMAN GAME", fill="red", font="Forte 34 bold", justify="center", anchor="n")
canvas_main.create_image(190, 75, image=bg_logo, anchor="nw")   

button_newgame = Button(canvas_main, text="N E W   G A M E",font="Times 12", width=28, command=login, state=NORMAL ,foreground='green', background='white',activebackground = "#191970",activeforeground="yellow",relief="raised") #New Game Button
button_score = Button(canvas_main, text="L E A D E R   B O A R D",  font="Times 12",height=2, width=28, command=score_board, state=NORMAL,foreground='green', background='white',activebackground = "#191970",activeforeground="yellow",relief="raised")   #Score Button
button_exit = Button(canvas_main, text="E X I T", width=28, font="Times 12",command= mainGUI.destroy, state=NORMAL,fg="red",relief="raised",background='white')   #Exit Button

button_newgame.place(x=320, y=280, anchor="center")      
button_score.place(x=320, y=340, anchor="center")        
button_exit.place(x=320, y=400, anchor="center")  
      
mainGUI.mainloop()    