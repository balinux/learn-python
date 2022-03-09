from tkinter import *
from tkinter.ttk import Labelframe

root = Tk()

root.geometry("300x300") #mengatur ukuran window
root.title(" main windows") # memberikan judul window

def openNewWindow():
    # buat asset image menjadi global variabel
    global photo

    # top level main window
    newWindow = Toplevel(root)
    newWindow.title("window baru")
    newWindow.geometry("200x200")

    photo = PhotoImage(file="python.png")
    # membuat label yang di taruh di window baru
    labelNewWindow = Label(newWindow, image=photo)
    # labelNewWindow = Label(newWindow, text="text new window")
    labelNewWindow.grid()

# membuat button untuk menampilkan new window
btn = Button(root, text="open window", command=openNewWindow)
btn.grid()


root.mainloop()