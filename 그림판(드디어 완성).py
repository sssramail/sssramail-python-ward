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
def plus() :
    global pen_size
    pen_size += 3
def mins() :
    global pen_size
    pen_size = pen_size - 3
def pen_chang(color) :
    global pen_color,fill_color,my_tool
    if my_tool == "pencolor" :
        pen_color = color
        btn_pencolor["bg"] = color
        if color == "white" or color == "yellow" :
            btn_pencolor["fg"] = "black"
        if color == "black" :
            btn_pencolor["fg"] == "white"
    elif my_tool == "canvascolor" :
        canvas["bg"] = color
        btn_canvascolor["bg"] = color
        if color == "white" or color == "yellow" :
            btn_canvascolor["fg"] = "black"
        if color == "black" :
            btn_canvascolor["fg"] = "white"
    else :
        fill_color = color
        btn_fillcolor["bg"] = color
        if color == "white" or color == "yellow" :
            btn_fillcolor["fg"] = "black"
        if color == "black" :
            btn_fillcolor["fg"] = "white"
def tool_chang(n) :
    global my_tool
    my_tool = n
def clear() :
    canvas.delete("all")

btn_white = Button(win,width = 13,height = 2,text = "white",bg = "white",command = lambda : pen_chang("white"))
btn_black= Button(win,width = 13,height = 2,text = "black",bg = "black",fg = "white",command = lambda : pen_chang("black"))
btn_blue = Button(win,width = 13,height = 2,text = "blue",bg = "blue",command = lambda : pen_chang("blue"))
btn_green = Button(win,width = 13,height = 2,text = "green",bg = "green",command = lambda : pen_chang("green"))
btn_red = Button(win,width = 13,height = 2,text = "red",bg = "red",command = lambda : pen_chang("red"))
btn_yellow = Button(win,width = 13,height = 2,text = "yellow",bg = "yellow",command = lambda : pen_chang("yellow"))
btn_plus = Button(win,width = 13,height = 2,text = "+",bg = "white",command = plus)
btn_mius = Button(win,width = 13,height = 2,text = "-",bg = "white",command = mins)
btn_fillcolor = Button(win,width = 13,height = 2,text = "fill color",bg = "white",command = lambda : tool_chang("fillcolor"))
btn_c = Button(win,width = 13,height = 2,text = "○",bg = "white")
btn_r= Button(win,width = 13,height = 2,text = "■",bg = "white")
btn_o = Button(win,width = 13,height = 2,text = "▲",bg = "white")
btn_clear = Button(win,width = 13,height = 2,text = "clear",bg = "white",command = lambda : clear())
btn_canvascolor = Button(win,width = 13,height = 2,text = "canvas color",bg = "white",command = lambda : tool_chang("canvascolor"))
btn_pencolor = Button(win,width = 13,height = 2,text = "pencolor",bg = "black",fg = "white",command = lambda : tool_chang("pencolor"))

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
canvas.bind("<Double-Button-1>",draw_shape)

win.mainloop()
