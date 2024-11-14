'''
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

from tkinter import *
win = Tk()
canvas = Canvas(win,width = 200, height = 100, bg = "white")
canvas.pack()

canvas.create_oval(10,10,60,60, fill = "blue")

canvas.create_rectangle(100,10,60,60,fill = "yellow",outline = "red")

win.mainloop()

from tkinter import *
win = Tk()
canvas = Canvas(win,width = 200, height = 100, bg = "white")
canvas.pack()

canvas.create_polygon(100,10,50,50,100,50,fill = "red")

win.mainloop()

from tkinter import *
from random import *

def draw_shape(event) :
    color = ["black","white","blue","red","green","yellow"]
    x1,y1 =event.x,event.y
    x2,y2 = x1 + randint(10,70),y1 + randint(10,70)
    canvas.create_rectangle(x1,y1,x2,y2,fill = color[randint(0,5)])


win = Tk()
canvas = Canvas(win,width = 300,height = 300,bg = "white")
canvas.pack()

canvas.bind("<Double-Button-1>",draw_shape)

win.mainloop()
'''
from tkinter import *
win = Tk()
win.geometry("510x600+200+200")
canvas = Canvas(win,width = 510,height = 470,bg = "white")

pen_color = "black"
pen_size = 2
shape_size = 10
my_tool = "pen"
fill_color = "white"

def paint(event):
    global pen_size,pen_color
    x1,y1 = event.x,event.y
    x2,y2 = event.x + pen_size, event.y + pen_size
    canvas.create_line(x1,y1,x2,y2, width = pen_size,fill = pen_color)
def draw_shape(event) :
    global shape_size,my_tool
    x1,y1 = event.x,event.y
    x2,y2 = event.x + shape_size, event.y + shape_size
    if my_tool == "oval" :
        canvas.create_oval(x1 - (shape_size / 2),y1,x2 - (shape_size / 2),y2,fill = fill_color)
    elif my_tool == "rect" :
        canvas.create_rectangle(x1,y1,x2,y2,fill = fill_color)
    elif my_tool == "try" :
        canvas.create_polygon(x1,y1,x2,y2,(x1 -(shape_size)),y2,fill = fill_color,outline = "black")
    
btn_white = Button(win,width = 13,height = 2,text = "white",bg = "white")
btn_black= Button(win,width = 13,height = 2,text = "black",bg = "black",fg = "white")
btn_blue = Button(win,width = 13,height = 2,text = "blue",bg = "blue")
btn_green = Button(win,width = 13,height = 2,text = "green",bg = "green")
btn_red = Button(win,width = 13,height = 2,text = "red",bg = "red")
btn_yellow = Button(win,width = 13,height = 2,text = "yellow",bg = "yellow")
btn_plus = Button(win,width = 13,height = 2,text = "+",bg = "white")
btn_mius = Button(win,width = 13,height = 2,text = "-",bg = "white")
btn_fillcolor = Button(win,width = 13,height = 2,text = "fill color",bg = "white")
btn_c = Button(win,width = 13,height = 2,text = "○",bg = "white")
btn_r= Button(win,width = 13,height = 2,text = "■",bg = "white")
btn_o = Button(win,width = 13,height = 2,text = "▲",bg = "white")
btn_clear = Button(win,width = 13,height = 2,text = "clear",bg = "white")
btn_canvascolor = Button(win,width = 13,height = 2,text = "canvas color",bg = "white")
btn_pencolor = Button(win,width = 13,height = 2,text = "pencolor",bg = "black",fg = "white")

canvas.grid(row = 0, column = 0, columnspan = 5)

btn_canvascolor.grid(row = 1, column = 0)
btn_black.grid(row = 1, column = 1)
btn_blue.grid(row = 1, column = 2)
btn_green.grid(row = 1, column = 3)
btn_plus.grid(row = 1, column = 4)

btn_pencolor.grid(row = 2, column = 0)
btn_white.grid(row = 2, column = 1)
btn_red.grid(row = 2, column = 2)
btn_yellow.grid(row = 2, column = 3)
btn_mius.grid(row = 2, column = 4)

btn_fillcolor.grid(row = 3, column = 0)
btn_c.grid(row = 3, column = 1)
btn_r.grid(row = 3, column = 2)
btn_o.grid(row = 3, column = 3)
btn_clear.grid(row = 3, column = 4)

canvas.bind("<B1-Motion>",paint)

win.mainloop()
