from tkinter import *
from tkinter import messagebox
try:
    from pygame import mixer
    mixer.init()
except:
    pass

root = Tk()
root.title("Tictactoe")
root.geometry("407x400")
root.resizable(False, False)
root.config(bg="#17161b")
try:
    root.iconbitmap(r"/Tictactoe/assets/Xoicon.ico")#specify Xoicon.ico path here
except:
    pass

clicked = True
winner = False
count = 0

#function to stop all changes to the board after winner is declared
def lock():
    tlb.config(state=DISABLED)
    tmb.config(state=DISABLED)
    trb.config(state=DISABLED)

    mlb.config(state=DISABLED)
    mmb.config(state=DISABLED)
    mrb.config(state=DISABLED)

    blb.config(state=DISABLED)
    bmb.config(state=DISABLED)
    brb.config(state=DISABLED)

#function to check winner
def winner_check():
    global winner
    winner = False
    #check for X
    if tlb["text"] == "X" and tmb["text"] == "X" and trb["text"] == "X":
        tlb.config(bg="#93C572")
        tmb.config(bg="#93C572")
        trb.config(bg="#93C572")
        winner = True
        messagebox.showinfo("Tictactoe", "X winner")
        lock()
        
    elif mlb["text"] == "X" and mmb["text"] == "X" and mrb["text"] == "X":
        mlb.config(bg="#93C572")
        mmb.config(bg="#93C572")
        mrb.config(bg="#93C572")
        winner = True
        messagebox.showinfo("Tictactoe", "X winner")
        lock()
        
    elif blb["text"] == "X" and bmb["text"] == "X" and brb["text"] == "X":
        blb.config(bg="#93C572")
        bmb.config(bg="#93C572")
        brb.config(bg="#93C572")
        winner = True
        messagebox.showinfo("Tictactoe", "X winner")
        lock()
        
    elif tlb["text"] == "X" and mlb["text"] == "X" and blb["text"] == "X":
        tlb.config(bg="#93C572")
        mlb.config(bg="#93C572")
        blb.config(bg="#93C572")
        winner = True
        messagebox.showinfo("Tictactoe", "X winner")
        lock()
        
    elif tmb["text"] == "X" and mmb["text"] == "X" and bmb["text"] == "X":
        tmb.config(bg="#93C572")
        mmb.config(bg="#93C572")
        bmb.config(bg="#93C572")
        winner = True
        messagebox.showinfo("Tictactoe", "X winner")
        lock()
        
    elif trb["text"] == "X" and mrb["text"] == "X" and brb["text"] == "X":
        trb.config(bg="#93C572")
        mrb.config(bg="#93C572")
        brb.config(bg="#93C572")
        winner = True
        messagebox.showinfo("Tictactoe", "X winner")
        lock()
        
    elif tlb["text"] == "X" and mmb["text"] == "X" and brb["text"] == "X":
        tlb.config(bg="#93C572")
        mmb.config(bg="#93C572")
        brb.config(bg="#93C572")
        winner = True
        messagebox.showinfo("Tictactoe", "X winner")
        lock()
        
    elif trb["text"] == "X" and mmb["text"] == "X" and blb["text"] == "X":
        trb.config(bg="#93C572")
        mmb.config(bg="#93C572")
        blb.config(bg="#93C572")
        winner = True
        messagebox.showinfo("Tictactoe", "X winner")
        lock()
    #check for O    
    elif tlb["text"] == "O" and tmb["text"] == "O" and trb["text"] == "O":
        tlb.config(bg="#6082B6")
        tmb.config(bg="#6082B6")
        trb.config(bg="#6082B6")
        winner = True
        messagebox.showinfo("Tictactoe", "O winner")
        lock()
        
    elif mlb["text"] == "O" and mmb["text"] == "O" and mrb["text"] == "O":
        mlb.config(bg="#6082B6")
        mmb.config(bg="#6082B6")
        mrb.config(bg="#6082B6")
        winner = True
        messagebox.showinfo("Tictactoe", "O winner")
        lock()
        
    elif blb["text"] == "O" and bmb["text"] == "O" and brb["text"] == "O":
        blb.config(bg="#6082B6")
        bmb.config(bg="#6082B6")
        brb.config(bg="#6082B6")
        winner = True
        messagebox.showinfo("Tictactoe", "O winner")
        lock()
        
    elif tlb["text"] == "O" and mlb["text"] == "O" and blb["text"] == "O":
        tlb.config(bg="#6082B6")
        mlb.config(bg="#6082B6")
        blb.config(bg="#6082B6")
        winner = True
        messagebox.showinfo("Tictactoe", "O winner")
        lock()
        
    elif tmb["text"] == "O" and mmb["text"] == "O" and bmb["text"] == "O":
        tmb.config(bg="#6082B6")
        mmb.config(bg="#6082B6")
        bmb.config(bg="#6082B6")
        winner = True
        messagebox.showinfo("Tictactoe", "O winner")
        lock()
        
    elif trb["text"] == "O" and mrb["text"] == "O" and brb["text"] == "O":
        trb.config(bg="#6082B6")
        mrb.config(bg="#6082B6")
        brb.config(bg="#6082B6")
        winner = True
        messagebox.showinfo("Tictactoe", "O winner")
        lock()
        
    elif tlb["text"] == "O" and mmb["text"] == "O" and brb["text"] == "O":
        tlb.config(bg="#6082B6")
        mmb.config(bg="#6082B6")
        brb.config(bg="#6082B6")
        winner = True
        messagebox.showinfo("Tictactoe", "O winner")
        lock()
        
    elif trb["text"] == "O" and mmb["text"] == "O" and blb["text"] == "O":
        trb.config(bg="#6082B6")
        mmb.config(bg="#6082B6")
        blb.config(bg="#6082B6")
        winner = True
        messagebox.showinfo("Tictactoe", "O winner")
        lock()
       
    elif count == 9:
        tlb.config(bg="#DE3163")
        tmb.config(bg="#DE3163")
        trb.config(bg="#DE3163")

        mlb.config(bg="#DE3163")
        mmb.config(bg="#DE3163")
        mrb.config(bg="#DE3163")

        blb.config(bg="#DE3163")
        bmb.config(bg="#DE3163")
        brb.config(bg="#DE3163")
        
        messagebox.showinfo("Tictactoe", "Draw!")
        
        lock()

#function to decide to put X or O or if the spot is already taken
def logic(b):
    global count, clicked
    #for X
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        try:
            mixer.music.load(r"/Tictactoe/assets/Sounds/Xpress.mp3")#specify Xsound.mp3 path here
            mixer.music.play(loops=0)
        except:
            pass
        winner_check()
    #for O    
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        b["fg"] = "#0096FF"
        clicked = True
        count += 1
        try:
            mixer.music.load(r"/Tictactoe/assets/Sounds/Opress.mp3")#specify Osound.mp3 path here
            mixer.music.play(loops=0)
        except:
            pass
        winner_check()
    else:
        messagebox.showerror("Tictactoe", "position already taken")
        
#top buttons     
tlb = Button(root, text=" ", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#4169E1", bg="#FFAA33", command=lambda: logic(tlb))
tlb.place(x=10 , y=10)
tmb = Button(root, text=" ", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#4169E1", bg="#F8DE7E", command=lambda: logic(tmb))
tmb.place(x=140 , y=10)
trb = Button(root, text=" ", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#4169E1", bg="#FFAA33", command=lambda: logic(trb))
trb.place(x=270 , y=10)
#middle buttons
mlb = Button(root, text=" ", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#4169E1", bg="#F8DE7E", command=lambda: logic(mlb))
mlb.place(x=10 , y=138)
mmb = Button(root, text=" ", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#4169E1", bg="#FFAA33", command=lambda: logic(mmb))
mmb.place(x=140 , y=138)
mrb = Button(root, text=" ", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#4169E1", bg="#F8DE7E", command=lambda: logic(mrb))
mrb.place(x=270 , y=138)
#bottom buttons
blb = Button(root, text=" ", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#4169E1", bg="#FFAA33", command=lambda: logic(blb))
blb.place(x=10 , y=266)
bmb = Button(root, text=" ", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#4169E1", bg="#F8DE7E", command=lambda: logic(bmb))
bmb.place(x=140 , y=266)
brb = Button(root, text=" ", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#4169E1", bg="#FFAA33", command=lambda: logic(brb))
brb.place(x=270 , y=266)

root.mainloop()
