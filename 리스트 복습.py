'''
from tkinter import *

win = Tk()
win.title("C3 coding")
win.geometry("300x200+100+100")
win.resizable(True, False)
win.mainloop()

from tkinter import *

win = Tk()
labl1 = Label(win, text = "one")
labl2 = Label(win, text = "two")
labl3 = Label(win, text = "three")
labl1.pack()
labl2.pack()
labl3.pack()
win.mainloop()

from tkinter import *

win = Tk()
lbl1 = Label(win, text = "orange" , width = 20 , height = 3 , relief = "solid")
lbl2 = Label(win, text = "banana" , font = ("Elephant" , 20) , bg = "yellow")
lbl3 = Label(win, text = "apple" , fg = "red")
lbl1.pack()
lbl2.pack()
lbl3.pack()
win.mainloop()

from tkinter import *

win = Tk()
List = ["info", "warning", "error", "question" , "questhead", "hourglass", "gray12", "gray25", "gray50", "gray75" ]

for i in range(10) :
    lbl = Label(win, bitmap = List[i])
    lbl.pack(side = "left")
win.mainloop()

from tkinter import *

win = Tk()
img = PhotoImage(file = "C3_img.gif")
lbl = Label(win, image = img)
lbl.pack()
win.mainloop()

from tkinter import *

win = Tk()
btn = Button(win, text = "button")
btn.pack()
win.mainloop()

from tkinter import *

win = Tk()


def click() :
    if btn["text"] == "red" :
        btn["text"] = "blue"
        btn["bg"] = "blue"
    else :
        btn["text"] = "red"
        btn["bg"] = "red"


btn = Button(win, text = "red", fg = "white", bg = "red", command = click)
btn.pack()
win.mainloop()
'''
from tkinter import *
win = Tk()

def click() :
    if lbl["text"] == "hello" :
        lbl["text"] = "python"
        lbl["bg"] = "green"
    else :
        lbl["text"] = "hello"
        lbl["bg"] = "yello"

lbl = Label(win, text = "hello" , bg = "yellow")
lbl.pack()
btn = Button(win, text = "red", command = click)
btn.pack()
win.mainloop()
