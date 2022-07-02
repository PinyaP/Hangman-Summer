from tkinter import *
from tkinter import messagebox
# from string import ascii_uppercase
import random

window=Tk()
window.title("Hangman")

word_list = ["RAFAY", "LION", "PANNDA", "TIGER", "DOG", "CAT", "RABIT", "MOUSE"]

photos = [PhotoImage(file="h1.png"), PhotoImage(file="h2.png"), PhotoImage(file="h3.png"), PhotoImage(file="h4.png"),
          PhotoImage(file="h5.png"), PhotoImage(file="h6.png"), PhotoImage(file="h7.png")]
def newGame():
    messagebox.showinfo("Hangman", "Its The Animal Name")
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))



def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<6:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                    lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You Guessed it")
                    newGame()
        else:
            numberOfGuesses+=1
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses==6:
                messagebox.showwarning("Hangman", "Game Over")
    
imgLabel=Label(window)
imgLabel.pack()
imgLabel.config(image=photos[0])

user_name = ""                                            #User name                           
bg_score = PhotoImage(file="train.png")                                
bg_game = PhotoImage(file="sky.png")                               
bg_logo = PhotoImage(file="hanged.png")
h1 = PhotoImage(file="h1.png")
bg_light = PhotoImage(file="light2.png")
bg_login = PhotoImage(file="sunflower.png")
bg_skip = PhotoImage(file="skip btn1.png")    

lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).pack()

n=0
btnA = Button(window, text="A", height=2, width=3, state=NORMAL, font=(None,10), command=lambda:guess("A")) 
btnA.pack(side="left")
btnB = Button(window, text="B", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("B")) 
btnB.pack(side="left")
btnC = Button(window, text="C", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("C")) 
btnC.pack(side="left")
btnD = Button(window, text="D", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("D")) 
btnD.pack(side="left")
btnE = Button(window, text="E", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("E")) 
btnE.pack(side="left")
btnF = Button(window, text="F", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("F")) 
btnF.pack(side="left")
btnG = Button(window, text="G", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("G")) 
btnG.pack(side="left")
btnH = Button(window, text="H", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("H")) 
btnH.pack(side="left")
btnI = Button(window, text="F", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("I")) 
btnI.pack(side="left")

#row2
btnJ = Button(window, text="J", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("J")) 
btnJ.pack(side="left")
btnK = Button(window, text="K", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("K")) 
btnK.pack(side="left")
btnL = Button(window, text="L", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("L")) 
btnL.pack(side="left")
btnM = Button(window, text="M", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("M")) 
btnM.pack(side="left")
btnN = Button(window, text="N", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("N")) 
btnN.pack(side="left")
btnO = Button(window, text="O", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("O")) 
btnO.pack(side="left")
btnP = Button(window, text="P", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("P")) 
btnP.pack(side="left")
btnQ = Button(window, text="Q", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("Q")) 
btnQ.pack(side="left")
btnR = Button(window, text="R", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("R")) 
btnR.pack(side="left")
btnS = Button(window, text="S", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("S")) 
btnS.pack(side="left")

#row3
btnT = Button(window, text="T", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("T")) 
btnT.pack(side="left")
btnU = Button(window, text="U", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("U")) 
btnU.pack(side="left")
btnV = Button(window, text="V", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("V")) 
btnV.pack(side="left")
btnW = Button(window, text="W", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("W")) 
btnW.pack(side="left")
btnX = Button(window, text="X", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("X")) 
btnX.pack(side="left")
btnY = Button(window, text="Y", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("Y")) 
btnY.pack(side="left")
btnZ = Button(window, text="Z", height=2, width=3, state=NORMAL, font=(None,10),bg = "blue", command=lambda:guess("Z")) 
btnZ.pack(side="left")
btnl = Button(window,image=bg_light,anchor="center",width=60,height=65)
btnl.pack(side="left")
btnskip = Button(window,image=bg_skip,anchor="center",width=52,height=52)
btnskip.pack(side="left")
# n=0
# for c in ascii_uppercase:
#     Button(window, text=c, command=lambda c=c: guess(c), font=("Helvetica 18"), width=4).pack(row=1+n//9, column=n%9)
#     n+=1

Button(window, text="new\nGame", command=lambda:newGame(),font=("Helvetica 10 bold")).pack(side="left")

newGame()    
window.mainloop()