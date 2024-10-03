'''
from tkinter import *
win = Tk()

def message(event) :
    lbl["text"] = entry.get()
    entry.delete(0,END)

entry = Entry(win)
entry.bind("<Return>", message)
entry.pack()
lbl = Label(win, text = "")
lbl.pack()
win.mainloop()

add = lambda x, y : x + y
print(add(10,100))

def qwer(x,y) :
    d = 0
    d = x + y
    return d

add = qwer(10,100)
print(add)

add = lambda a,b : a % b

print(add(10,4))

from tkinter import *

def Click(n) :
    if n == 1 :
        lbl["text"] = "First button clicked."
    elif n == 2 :
        lbl["text"] = "Second button clicked."
    else :
        lbl["text"] = "Third button clicked."

win = Tk()
lbl = Label(win, text = "이름")

btn1 = Button(win, text = "First", command = lambda : Click(1))
btn2= Button(win, text = "Second", command = lambda : Click(2))
btn3 = Button(win, text = "Third", command = lambda : Click(3))


lbl.grid(row = 0, column = 0, columnspan = 3)
btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, coumn = 1)
btn3.grid(row = 1, column = 2)

win.mainloop()

from tkinter import *

def Click(shape) :
    if shape == "circle" :
        img = PhotoImage(file = "circle.png")
    elif shape == "triangle" :
        img = PhotoImage(file = "triangle.png")
    else :
        img = PhotoImage(file = "star.png")

    lbl["image"] = img
    lbl.image = img

win = Tk()

img = PhotoImage(file = "circle.png")
lbl = Label(win, image = img)

btn1 = Button(win, text = "circle", command = lambda : Click("circle"))
btn2= Button(win, text = "triangle", command = lambda : Click("triangle"))
btn3 = Button(win, text = "star", command = lambda : Click("star"))


lbl.grid(row = 0, column = 0, columnspan = 3)
btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 1, column = 2)

win.mainloop()
'''
from tkinter import *

win = Tk()

win.title("<가위바위보 게임> (진사람이 라면사기)")

basic_img = PhotoImage(file = "ready.png")
#basic_img = PhotoImage(file = "rock.png")
#basic_img = PhotoImage(file = "scissors.png")
#basic_img = PhotoImage(file = "paper.png")

lbl_com = Label(win,image = basic_img)
lbl_user = Label(win,image = basic_img)

lbl_res = Label(win, text = "")


lbl_name1 = Label(win,text = "computer")
lbl_name2 = Label(win,text = "user")


btn_scissor = Button(win, text = "scissor")
btn_rock = Button(win, text = "rock")
btn_paper = Button(win, text = "paper")


lbl_com.grid(row = 0, column = 0)
lbl_res.grid(row = 0, column = 1)
lbl_user.grid(row = 0, column = 2)
lbl_name1.grid(row = 1, column = 0)
lbl_name2.grid(row = 1, column = 2)
btn_rock.grid(row = 2, column = 0)
btn_paper.grid(row = 2, column = 1)
btn_scissor.grid(row = 2, column = 2)
