from cProfile import label
from tkinter import *

root = Tk()

root.geometry("300x300") #mengatur ukuran window
root.title(" main windows") # memberikan judul window

# memebuat slider dengan nilai 0 - 100
slider1 = Scale(root, from_=0,to=100, orient=HORIZONTAL)
slider1.grid()

# fungsi f=prin label
def print():
    label1 = Label(root, text=slider1.get())
    label1.grid()

def changeResolution(var):
    root.geometry(str(var)+"x300")

# menganti resolusi dengan window menggunakan scale
sliderResolutionSetter = Scale(root, from_=100,to=600, orient=HORIZONTAL, label="mengubah resolusi", command=changeResolution)
sliderResolutionSetter.grid()
sliderResolutionSetter.set(300)


# mengambil nilai slider dengan button
btn =  Button(root, text="cetak", command=print)
btn.grid()


# ===============
# mengubah banckgroud dengan slider

def changebackgroundColor(var):
    root["bg"] = "#"+str(var)+"062FF"
    sliderChangeColorBg["bg"] = "#"+str(var)+"062FF"

sliderChangeColorBg = Scale(root, from_=4,to=9, orient=HORIZONTAL, label="mengubah background", command=changebackgroundColor)
sliderChangeColorBg.grid()
sliderChangeColorBg.set(4)

root.mainloop()