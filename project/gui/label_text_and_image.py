from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.geometry("300x300") #mengatur ukuran window
root.title(" main windows") # memberikan judul window

# membuat label pada window
# memberi warna pada background
# memberi warna pada font
# menambahkan padding
lbl = Label(root,text="hello word", bg="red", fg="white", padx=10, pady=10,)

# menampilkan gambar dengan widget PhotoImage
# imagepython = ImageTk.PhotoImage(file="python.png")
imagepython = PhotoImage(file='./python.png')
lbl2 = Label(root, image=imagepython)

# menempatkan label
# lbl.grid()

# memberikan lokasi lebih spesifik
lbl.place(x=100, y=100)

root.mainloop()
