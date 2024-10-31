'''
from tkinter import *

win = Tk()
listbox = Listbox(win)
for i in range(10):
    listbox.insert(i,str(i))
print(listbox.curselection())
print(listbox.get(0,9))
listbox.pack()
win.mainloop()

from tkinter import *

def double_click(event) :
    index = listbox.curselection()
    print("Today :", listbox.get(index[0]))

def left_click(event):
    index = listbox.curselection()
    if index :
        if index[0] == 0 :
            print("yesterday : sun")
        else :
            print("yesterday : ", listbox.get(index[0]-1))

def right_click(event):
    index = listbox.curselection()
    if index :
        if index[0] == 6:
            print("tomorrw : mon")
        else :
            print("tomorrw :",listbox.get(index[0]+1))

day = ["mon","tue","wed","thu","fri","sat","sun"]

win = Tk()
listbox = Listbox(win)

for i in range(7):
    listbox.insert(i,day[i])

listbox.bind("<Double-Button-1>", double_click)
listbox.bind("<Button-1>",left_click)
listbox.bind("<Button-3>",right_click)
listbox.pack()
win.mainloop()

from tkinter import *

def double_click(event) :
    index = listbox.curselection()
    if index[0] == 0 :
        lbl["text"] = "sssramail"
    elif index[0] == 1 :
        lbl["text"] = "banana"
    else :
        lbl["text"] = "appel"

win = Tk()
lbl = Label(win, text = " ",bg = "red",fg = "navy")
listbox = Listbox(win)
clickbox = ["sssramail","banana","appel"]

for i in range(3):
    listbox.insert(i,clickbox[i])

lbl.pack()
listbox.bind("<Double-Button-1>", double_click)
listbox.pack()
win.mainloop()

from datetime import datetime
print(datetime.today())
print(datetime.now())
'''
from datetime import datetime
print(datetime.today().strftime("%Y년 %m월 %d일"))
print(datetime.today().strftime("%H시 %M분"))
print(datetime.today().strftime("%Y/%m월/%d일/%H시/%M분"))
