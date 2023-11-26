
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import random , sys
sys.path.append("./src")
import game as gme

class game():
    def __init__(self,root):
        self.root = root
        
        self.root.title("Hand Cricket Game")
        self.root.iconbitmap("src/icon.ico")
        self.root.geometry("1152x768")
        self.root.resizable(0,0)

        # import background image
        filename = ImageTk.PhotoImage(Image.open("./src/background.png"))
        
        # create canvas
        my_canvas = Canvas(self.root , width=1152, height=768)
        my_canvas.pack(fill="both",expand=True)

        # set image to canvas
        my_canvas.create_image(0,0,image=filename,anchor="nw")

        # set canvas label
        my_canvas.create_text(576,150 , text = "Welcome to hand Cricket",font=("Roboto",50))
        
        # functions
        def playGame():
            gm=Toplevel()
            frame2=gme.game(gm)
            gm.mainloop()

        # set buttons
        start_button = tk.Button(self.root,text="Start",font=('Roboto',25),width=10,border=10,command=playGame)
        start_button.config(activebackground="white",activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C")
        start_button.place(x = 480, y = 270)
        
        exit_button = tk.Button(self.root,text="Exit",font=('Roboto',25),fg="black",width=10,border=10,command=self.root.destroy)
        exit_button.config(activebackground="white",activeforeground="#F22C2C",cursor="hand2", fg="white", bg="#F22C2C")
        exit_button.place(x = 480,y = 370)
        
        self.root.mainloop()



if __name__ == "__main__":
   root = Tk()
   game(root)