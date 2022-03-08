from tkinter import *
from tkinter import messagebox

from matplotlib.pyplot import text, title

root = Tk()

root.geometry("300x300") #mengatur ukuran window
root.title(" main windows") # memberikan judul window

# menampilkan message box
def message():
    # normal message box
    # messagebox.showinfo(title="info", message="kamu ganteng")
    
    # ask question
    msg = messagebox.askquestion("info baru", "ini adalah sebuah info")
    if msg == "yes":
        Label(root, text="yes").grid()
    elif msg == "no":
        Label(root, text="no").grid()



btn = Button(root, text="show messagebox", command= message)
btn.grid()

root.mainloop()
