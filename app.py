import tkinter as tk
import random

class game():
    def __init__(self,root):
        self.root = root
        self.root.title("Hand Cricket Game")
        self.root.iconbitmap("src/icon.ico")
        
        
        


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='white')
    root.geometry("1024x768")
    root.resizable(False,False)
    
    bgimg = tk.PhotoImage(file="src/image1.png")
    new_label = tk.Label(root,image=bgimg)
    new_label.place(x=0,y=0,relheight=1,relwidth=1)
    
    hand_cricket = game(root)
    root.mainloop()