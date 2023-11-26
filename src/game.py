import random
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

class game():
    def __init__(self,root):
        self.root = root
        
        self.root.title("Play")
        self.root.iconbitmap("src/icon.ico")
        self.root.geometry("1152x768")
        self.root.resizable(0,0)
        
        self.bat = True
        self.playerScore = int(0)
        self.compScore = int(0)
        self.choices = [1,2,3,4,5,6]
        
        c1=Canvas(self.root,bg="white",height=768,width=1152)
        c1.pack()
        
        batsman = ImageTk.PhotoImage(Image.open("./src/batsman6.jpg"))
        self.root.batsman=batsman
        batpic=c1.create_image(660,0,image=batsman,anchor=NW)

        bowler = ImageTk.PhotoImage(Image.open("./src/bowlerog3.jpg"))
        self.root.bowler=bowler
        bowlpic=c1.create_image(0,0,image=bowler,anchor=NW)
        
        tagp=Label(c1,text="Player",font=("Comic Sans MS", 20),bg="white",fg="#F97C07")
        tagp.place(x=380,y=100)
        tagd=Label(c1,text="VS",font=("Comic Sans MS", 20),bg="white",fg="black")
        tagd.place(x=330,y=100)
        tagc=Label(c1,text="Computer",font=("Comic Sans MS", 20),bg="white",fg="#0761F9")
        tagc.place(x=200,y=100)
        
        tag2=Label(c1,text=self.playerScore,justify=LEFT,font=("Comic Sans MS", 24),bg="white",fg="#F97C07")
        tag2.place(x=400,y=170)
        tag3=Label(c1,text=self.compScore,font=("Comic Sans MS", 24),bg="white",fg="#0761F9")
        tag3.place(x=250,y=170)
        
        compval = c1.create_text(300,400,fill="black",font=("Comic Sans MS", 24),text="The computer has chosen ")
        
        four=c1.create_text(800,150,fill="#F907B6",font="Times 26 italic bold",text="")
        six=c1.create_text(800,150,fill="#F907B6",font="Times 26 italic bold",text="")
        out=c1.create_text(800,150,fill="red",font="Times 26 italic bold",text="")
        
        def fsclear():
            c1.itemconfig(four,text="")
            c1.itemconfig(six,text="")
            
        def Run1():
            fsclear()
            if(self.bat):
                batting(1)
            else:
                bowling(1)
        def Run2():
            fsclear()
            if(self.bat):
                batting(2)
            else:
                bowling(2)
        def Run3():
            fsclear()
            if(self.bat):
                batting(3)
            else:
                bowling(3)
        def Run4():
            fsclear()
            if(self.bat):
                batting(4)
            else:
                bowling(4)
        def Run5():
            fsclear()
            if(self.bat):
                batting(5)
            else:
                bowling(5)
        def Run6():
            fsclear()
            if(self.bat):
                batting(6)
            else:
                bowling(6)
                
        def change():
            enable()
            b1.destroy()
            c1.itemconfig(out,text="")
            c1.itemconfig(compval,text="The computer has chosen")
             
        def disable():
            button1.config(state=DISABLED)
            button2.config(state=DISABLED)
            button3.config(state=DISABLED)
            button4.config(state=DISABLED)
            button5.config(state=DISABLED)
            button6.config(state=DISABLED)
            
        def enable():
            button1.config(state=NORMAL)
            button2.config(state=NORMAL)
            button3.config(state=NORMAL)
            button4.config(state=NORMAL)
            button5.config(state=NORMAL)
            button6.config(state=NORMAL)
        
        def batting(val):
            self.compchoice = int(random.choice(self.choices))
            val = int(val)
            if(val == self.compchoice):
                c1.itemconfig(compval,text=f"The computer chose : {self.compchoice}")
                c1.itemconfig(out,text="OUT!!")
                self.bat = False
                b1.place(x=200,y=500)
                disable()
            else:
                c1.itemconfig(compval,text=f"The computer chose : {self.compchoice}")
                self.playerScore += val
                tag2.config(text=self.playerScore)
                if(val == 4):
                   c1.itemconfig(four,text="Four")
                elif(val == 6):
                    c1.itemconfig(six,text="Six")
        
        def decide():
            if(self.playerScore < self.compScore):
                c1.itemconfig(out,text="The computer has WON")
            elif(self.playerScore > self.compScore):
                c1.itemconfig(out,text="You have WON")
            else:
                c1.itemconfig(out,text="Match Draw!!")
            disable()
        
        def  bowling(val):
            self.compchoice = int(random.choice(self.choices))
            val = int(val)
            if(val == self.compchoice):
                c1.itemconfig(compval,text=f"The computer chose : {self.compchoice}")
                decide()
            else:
                c1.itemconfig(compval,text=f"The computer chose : {self.compchoice}")
                self.compScore += self.compchoice
                tag3.config(text=self.compScore)
                if(self.playerScore < self.compScore):
                    c1.itemconfig(out,text="The computer has WON")

        exit_button = tk.Button(self.root,text="Back",font=('Roboto',15),fg="black",width=5,border=10,command=self.root.destroy)
        exit_button.config(activebackground="white",activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C")
        exit_button.place(x = 10,y = 10)

        button1 = Button(self.root,width =5,relief=RAISED,text="1",bd=1,command=Run1,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button1.place(x=700,y=250)
        button2 = Button(self.root,width =5,relief=RAISED,text="2",bd=1,command=Run2,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button2.place(x=800,y=250)
        button3 = Button(self.root,width =5,relief=RAISED,text="3",bd=1,command=Run3,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button3.place(x=700,y=300)
        button4 = Button(self.root,width =5,relief=RAISED,text="4",bd=1,command=Run4,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button4.place(x=800,y=300)
        button5 = Button(self.root,width =5,relief=RAISED,text="5",bd=1,command=Run5,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button5.place(x=700,y=350)
        button6 = Button(self.root,width =5,relief=RAISED,text="6",bd=1,command=Run6,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        button6.place(x=800,y=350)

        b1=Button(self.root,width =15,relief=RAISED,text="Start Bowling",bd=1,command=change,
                         highlightthickness=0,highlightcolor="#FB028D",activebackground="white",
                         activeforeground="#F22C2C",cursor="hand2", fg="black", bg="white",font=("Helvetica", 16, 'bold'))
        
        self.root.mainloop()
