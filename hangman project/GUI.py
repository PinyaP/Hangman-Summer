from tkinter import *                                  
# from tkinter import ttk

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
    #     newgame()
    
    login_window = Toplevel(mainGUI)
    login_window.title("L O G I N")
    login_window.geometry("550x260+350+200")
    login_window.resizable(0, 0)
    canvas_login = Canvas(login_window,bg="#191970")
    canvas_login.pack(fill="both", expand=True)

    canvas_login.create_text(270, 50, text="Enter Your Name",fill="white", font="Times 26 bold",justify="center")
    canvas_login.create_text(272, 50, text="Enter Your Name",fill="red", font="Times 26 bold",justify="center")
    enter_name = Entry(canvas_login, width=16, font="Times 26 bold", justify="center", bg="#df91fa") #ช่องที่ให้ผู้ใช้กรอกชื่อ
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

    canvas_score.create_text(200, 80, text="L E A D E R   B O A R D", fill="white", font="Forte 30 bold",justify="center")
    canvas_score.create_text(200, 120, text=scoreList,fill="white", font="Forte 18", justify="center", anchor="n")
    button_exit_score = Button(score_window, text="E X I T", fg='red', height=2, width=26,command=lambda:buttonExit(score_window), state=NORMAL, font="Forte 16")
    button_exit_score.place(x=200, y=580, anchor="center")
   


mainGUI = Tk()                                                           
mainGUI.geometry("640x480+300+200")                                              
mainGUI.resizable(0, 0)                                           #ไม่่สามารถปรับหน้าจอเองได้

mainGUI.title("H  A  N  G  M  A  N")                           

user_name = ""                                                    #User name                           
bg_score = PhotoImage(file="score board.png")                                
bg_game = PhotoImage(file="game.png")                               
bg_logo = PhotoImage(file="hanged.png")

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
