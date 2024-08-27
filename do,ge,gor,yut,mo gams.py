import random
o = 0
t = 0
s = 0
f = 0
n = 0
s = 1
while True :
    o = random.randint(0,1)
    o = o * 1000
    n = n + o
    t = random.randint(0,1)
    t = t * 100
    n = n + t
    s = random.randint(0,1)
    s = s * 10
    n = n + s
    f = random.randint(0,1)
    n = n + f
    if n == 1111 :
        print(n)
        print("모")
        s = 0
    if n == 1110 :
        print(n)
        print("도")
        s = 0
    if n == 1101 :
            print("1101")
            print("도")
            s = 0
    if n == 1011 :
            print("1011")
            print("도")
            s = 0
    if n == 111 :
            print("1110")
            print("도")
            s = 0
    if n == 1100 :
        print("1100")
        print("개")
        s = 0
    if n == 1001 :
            print("1001")
            print("개")
            s = 0
    if n == 101 :
            print("0101")
            print("개")
            s = 0
    if n == 11 :
            print("0011")
            print("개")
            s = 0
    if n == 1000 :
        print(n)
        print("걸")
        s = 0
    if n == 1 :
            print("0001")
            print("걸")
            s = 0
    if n == 100 :
            print("0100")
            print("걸")
            s = 0
    if n == 10 :
            print("0010")
            print("걸")
            s = 0
    if n == 0000 :
        print(n)
        print("윷")
        s = 0
    if s == 0 :
        print("끄으으으으읕")
        break
