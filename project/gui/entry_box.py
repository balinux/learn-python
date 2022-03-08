from tkinter import *

root = Tk()

root.geometry("300x300") #mengatur ukuran window
root.title(" main windows") # memberikan judul window

# membuat widget entry
entryName = Entry(root)
entryName.grid()

# menampilkan entry password
entryPassword = Entry(root, show="*")
entryPassword.grid()

def submit():
    label = Label(root, text=entryName.get()) # menampilkan data entry
    label.grid()
    entryName.delete(0,END) # menghapus entry saat submit

# mengambil nilai entry
btn = Button(root, text="submit", command=submit)
btn.grid()

root.mainloop()
