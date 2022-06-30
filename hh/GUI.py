from tkinter import *

global user_name
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
    button_exit_score = Button(score_window, text="E X I T", fg='red', height=2, width=26,command=lambda:buttonExit(score_window), state=NORMAL, font="Forte 16")
    button_exit_score.place(x=200, y=580, anchor="center")



def hangman():
    game_window = Toplevel(mainGUI)
    game_window.geometry('915x700')
    game_window.resizable(0,0)
    
    hangman_game = Canvas(game_window,width=905,height=700,bg="#E7FFFF") 
    hangman_game.pack(fill="both", expand=True)
    hangman_game.create_image(0, 0, image=bg_game, anchor="nw")      
    hangman_game.create_text(80, 50, text=("Player: "+user_name), fill="black", font=(None,25), anchor="nw")
    hangman_game.create_image(150 , 20, image= h1 , anchor="nw")
    
    #row1
    btnA = Button(game_window, text="A", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnA.place(x=60, y=470)
    btnB = Button(game_window, text="B", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnB.place(x=150, y=470)
    btnC = Button(game_window, text="C", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnC.place(x=240, y=470)
    btnD = Button(game_window, text="D", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnD.place(x=330, y=470)
    btnE = Button(game_window, text="E", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnE.place(x=420, y=470)
    btnF = Button(game_window, text="F", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnF.place(x=510, y=470)
    btnG = Button(game_window, text="G", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnG.place(x=600, y=470)
    btnH = Button(game_window, text="H", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnH.place(x=690, y=470)
    btnI = Button(game_window, text="F", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnI.place(x=780, y=470)
    
    #row2
    btnJ = Button(game_window, text="J", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnJ.place(x=15, y=535)
    btnK = Button(game_window, text="K", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnK.place(x=105, y=535)
    btnL = Button(game_window, text="L", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnL.place(x=195, y=535)
    btnM = Button(game_window, text="M", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnM.place(x=285, y=535)
    btnN = Button(game_window, text="N", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnN.place(x=375, y=535)
    btnO = Button(game_window, text="O", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnO.place(x=465, y=535)
    btnP = Button(game_window, text="P", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnP.place(x=555, y=535)
    btnQ = Button(game_window, text="Q", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnQ.place(x=645, y=535)
    btnR = Button(game_window, text="R", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnR.place(x=735, y=535)
    btnS = Button(game_window, text="S", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnS.place(x=825, y=535)
    
    #row3
    btnT = Button(game_window, text="T", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnT.place(x=150, y=600)
    btnU = Button(game_window, text="U", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnU.place(x=240, y=600)
    btnV = Button(game_window, text="V", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnV.place(x=330, y=600)
    btnW = Button(game_window, text="W", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnW.place(x=420, y=600)
    btnX = Button(game_window, text="X", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnX.place(x=510, y=600)
    btnY = Button(game_window, text="Y", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnY.place(x=600, y=600)
    btnZ = Button(game_window, text="Z", height=2, width=3, state=NORMAL, font=(None,20),bg = "blue") 
    btnZ.place(x=690, y=600)
    # btnl = Button(game_window,image=bg_light,anchor="center",width=60,height=65)
    # btnl.place(x=828, y=610)
    btnl = Button(game_window,image=bg_light,anchor="center",width=60,height=65)
    btnl.place(x=17, y=610)
    btnskip = Button(game_window,image=bg_skip,anchor="center",width=52,height=52)
    btnskip.place(x=840, y=610)
    # button = [['b1','a',0,595],['b2','b',70,595],['b3','c',140,595],['b4','d',210,595],['b5','e',280,595],['b6','f',350,595],['b7','g',420,595],['b8','h',490,595],['b9','i',560,595],['b10','j',630,595],['b11','k',700,595],['b12','l',770,595],['b13','m',840,595],['b14','n',0,645],['b15','o',70,645],['b16','p',140,645],['b17','q',210,645],['b18','r',280,645],['b19','s',350,645],['b20','t',420,645],['b21','u',490,645],['b22','v',560,645],['b23','w',630,645],['b24','x',700,645],['b25','y',770,645],['b26','z',840,645]]

    # for q1 in button:
    #     exec('{}=Button(hangman_game,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
    #     exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
    
    

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

button_newgame = Button(canvas_main, text="N E W   G A M E",font="Times 12", height=2, width=28, command=login, state=NORMAL ,foreground='green', background='white',activebackground = "#191970",activeforeground="yellow",relief="raised") #New Game Button
button_score = Button(canvas_main, text="L E A D E R   B O A R D",  font="Times 12",height=2, width=28, command=score_board, state=NORMAL,foreground='green', background='white',activebackground = "#191970",activeforeground="yellow",relief="raised")   #Score Button
button_exit = Button(canvas_main, text="E X I T", height=2, width=28, font="Times 12",command= mainGUI.destroy, state=NORMAL,fg="red",relief="raised",background='white')   #Exit Button

button_newgame.place(x=320, y=280, anchor="center")      
button_score.place(x=320, y=340, anchor="center")        
button_exit.place(x=320, y=400, anchor="center")  
      
mainGUI.mainloop()    