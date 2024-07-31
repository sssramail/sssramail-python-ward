from random import *

print("=====================가.바.보.게임====================")
a = int(input("가위 : 1 , 바위 : 2 , 보 : 3 중에 택1 :"))
com = choice([1,2,3])
c = com


if a == 1 :
    if a == 1 and c == 2 :
        print("com win")
    elif a == 1 and c == 3 :
        print("user win ")
    elif a == 1 and c == 1 :
        print("draw")
if a == 2 :
    if a == 2 and c == 2 :
        print("draw")
    elif a == 2 and c == 3 :
        print("com win")
    elif a == 2 and c == 1 :
        print("user win")
if a == 3 :
    if a == 3 and c == 3 :
        print("draw")
    elif a == 3 and c == 1 :
        print("com win")
    elif a == 3 and c == 2 :
        print("user win")
