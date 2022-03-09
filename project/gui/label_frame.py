from tkinter import *
from tkinter.ttk import Labelframe

root = Tk()

root.geometry("300x300") #mengatur ukuran window
root.title(" main windows") # memberikan judul window

# membuat label fram
labelFramex = Labelframe(root, text="User profile")
labelFramex.grid()

# membuat sebuah label yang ditaruh di dalam labelframe
labeltext = Label(labelFramex, text="Halo, Nama saya balinux", padx=1, pady=10)
labeltext.grid()

root.mainloop()