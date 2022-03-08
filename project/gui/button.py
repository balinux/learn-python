from tkinter import *
from PIL import ImageTk, Image
from numpy import pad

root = Tk()

root.geometry("300x300") #mengatur ukuran window
root.title(" main windows") # memberikan judul window

def showme():
    label = Label(root, text="hey look me")
    label.grid()
    btn2 = Button(root, text="new button")
    btn2.grid()

# membuat tombol
# menambah fungsi saat di klik
# menambah padding
buttonSubmit = Button(root, text="submit", command=showme, padx=10, pady=10)
buttonSubmit.grid()

root.mainloop()
