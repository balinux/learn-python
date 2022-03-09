from tkinter import *

root = Tk()

root.geometry("300x300") #mengatur ukuran window
root.title(" main windows") # memberikan judul window

# penampung value dari radio
valueString = StringVar()

# memberikan nilai default pada valuestring
valueString.set("female")

# membuat fungsi cetak
def cetak(value):
    Label(root,text=value).grid()

radiob = Radiobutton(root, text="male", variable=valueString, value="male", command=lambda:cetak(valueString.get())).grid()

radiob2 = Radiobutton(root, text="female", variable=valueString, value="female", command=lambda:cetak(valueString.get())).grid()

root.mainloop()