'''
f = open("example.txt" , "w")
f.close()

f = open("example.txt" , "w")
for i in range(1,4) :
    f.write("Line %d\n" %i)

f.close()

f = open("example.txt" , "a")
alphabet = ["A","B","C","D","E"]
for c in alphabet :
    f.write(c)

f.close()

f = open("example.txt" , "r")
data = f.read()
print(data)
f.close()

f = open("example.txt" , "r")
while True :
    line = f.readline()
    if not line :
        break
    print(line, end = '')

f.close()

f = open("example.txt" , "r")
data = f.readlines()
for line in data :
    print(line, end = '')
f.close()

f = open("example.txt" , "r") 
while True :
    print(f.tell(), end = ' ')
    line = f.readline()
    print(line.strip())
    if not line :
        break
f.seek(26)
print("after setting a pointer : %d(%s)" %(f.tell(), f.read()[0]))
f.close()

f = open("porfile.txt" , "w")
name = input("Name : ")
age = input("age : ")
f.write("Name : %s\n" %name)
f.write("Age : %s\n" %age)
f.close()

f = open("porfile.txt" , "a")
School = input("School : ")
f.write("School : %s\n" %School)
f.close()
'''
from tkinter import *

def get_click() :
    lbl2["text"] = txt_box.get(1.0, END)

def ins_click() :
    txt_box.insert(1.0, lbl1["text"])

def del_click() :
    txt_box.delete(1.0, END)

win = Tk()
txt_box = Text(win, width = 40, height = 5)
lbl1 = Label(win, text = "Click the 'insert' button to insert this string.", width = 40 , height = 5, bg = "skyblue")
lbl2 = Label(win, text = "Click the 'get' button to import textbox strings\ninto this label.", width = 40, height = 5, bg = "pink")
btn_get = Button(win, text = "get", width = 10, command = get_click)
btn_ins = Button(win, text = "insert"
