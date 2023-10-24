import tkinter as tk
import random

class game():
    def __init__(self,root,img):
        self.root = root
        self.root.title("Hand Cricket Game")
        self.root.iconbitmap("src/icon.ico")

        ## Create canvas
        my_canvas = tk.Canvas(self.root,width=1024,height=768)
        my_canvas.pack(fill="both",expand=True)

        # Add image to canvas
        my_canvas.create_image(0,0,image=bgimg,anchor="nw")

        ## Add elements to canvvas
        my_canvas.create_text(500,150,text="Hand Cricket",font=("Roboto",50),fill="#014707")

        start_button = tk.Button(self.root,text="Start",font=('Roboto',25),fg="black",width=10,border=10)
        exit_button = tk.Button(self.root,text="Exit",font=('Roboto',25),fg="black",width=10,border=10)

        start_window = my_canvas.create_window(430,270,anchor="nw",window=start_button)
        exit_window = my_canvas.create_window(430,370,anchor="nw",window=exit_button)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='white')
    root.geometry("1024x768")
    root.resizable(False,False)
    
    bgimg = tk.PhotoImage(file="src/background.png")

    hand_cricket = game(root,bgimg)
    root.mainloop()