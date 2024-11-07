'''
from tkinter import *
win = Tk()
cavas = Canvas(win,bg = "white",width = 600,height = 600)
cavas.pack()
win.mainloop()

from tkinter import *
win = Tk()
cavas = Canvas(win,bg = "white",width = 600,height = 600)
canvas.create_line(0, 50, 500, 50, fill = "black",width = 10)
canvas.pack()
win.mainloop()

from tkinter import *
win = Tk()
cavas = Canvas(win,bg = "white",width = 400,height = 400)
x1,y1 = 200,50
x2,y2 = x1,y1 + 300
cavas.create_line(x1,y1,x2,y2, fill = "black",width = 5)
cavas.pack()
win.mainloop()

from tkinter import *
win = Tk()
canvas = Canvas(win,bg = "white",width = 500,height = 500)
canvas.pack()

x1,y1 = 0,0
x2,y2 = 500,0

for i in range(19) :
    y1 += 30
    y2 = y1
    canvas.create_line(x1,y1,x2,y2, fill = "black",width = 3)

win.mainloop()

from tkinter import *
win = Tk()
canvas = Canvas(win,bg = "white",width = 298,height = 298)
canvas.pack()

x1,y1 = 0,0
x2,y2 = 500,0

for i in range(10) :
    y1 += 30
    y2 = y1
    canvas.create_line(x1,y1,x2,y2, fill = "red",width = 3)

x1,y1 = 0,0
x2,y2 = 0,500

for j in range(10) :
    x1 += 30
    x2 = x1
    canvas.create_line(x1,y1,x2,y2, fill = "blue",width = 3)

win.mainloop()

from tkinter import *

pen_color = "black"

def paint(event):
    global pen_color
    x1,y1 = event.x,event.y
    x2,y2 = x1 + 5, y1 + 5
    canvas.create_line(x1,y1,x2,y2, width = 1,fill = pen_color)
def chang_color() :
    global pen_color
    pen_color = "red"
def rechang_color() :
    global pen_color
    pen_color = "black"
    
win = Tk()
canvas = Canvas(win,bg = "white",width = 500,height = 500)
btn1 = Button(win,text = "red",command = chang_color)
btn2 = Button(win,text = "Black",command = rechang_color)
canvas.pack()
btn2.pack()
btn1.pack()
'''
from tkinter import *

pen_width = 3
pen_color = "black"

win = Tk()
canvas = Canvas(win,bg = "white",width = 600,height = 600)
btn_black= Button(win,text = "black")
btn_red = Button(win,text = "red")
btn_green = Button(win,text = "green")
btn_blue = Button(win,text = "blue")
btn_yellow = Button(win,text = "yellow")
btn_white = Button(win,text = "white")
btn_clear = Button(win,text = "red")
btn_plus = Button(win,text = "+")
btn_mius = Button(win,text = "-")

canvas.grid(row = 0, column = 0, columnspan = 9)
btn_black.grid(row = 1, column = 0)
btn_red.grid(row = 1, column = 1)
btn_green.grid(row = 1, column = 2)
btn_blue.grid(row = 1, column = 3)
btn_yellow.grid(row = 1, column = 4)
btn_clear.grid(row = 1, column = 5)
btn_plus.grid(row = 1, column = 6)
btn_mius.grid(row = 1, column = 7)
btn_white.grid(row = 1, column = 8)
