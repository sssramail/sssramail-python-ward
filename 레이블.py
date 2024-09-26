'''
from tkinter import *
win = Tk()

lbl1 = Label(win, text = "orange" , width = 20 , height = 3 , relief = "solid")

lbl2 = Label(win, text = "banana" , font = ("Elephant" , 28) , bg = "yellow")

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
btn = Button(win, text = "Button")
btn.pack(side = "left")
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

lbl = Label(win, text = "hello" , bg = "yellow")

lbl.pack()

def click() :
    if lbl["text"] == "hello" :
        lbl["text"] = "python"
        lbl["bg"] = "green"
    else :
        lbl["text"] = "hello"
        lbl["bg"] = "yello"

btn = Button(win, text = "red", command = click)
btn.pack()
win.mainloop()
