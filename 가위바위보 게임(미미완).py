
from tkinter import *
from random import *

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
def chage_img(user) :
    List = ["scissors.png" , "rock.png" , "paper.png"]


    
