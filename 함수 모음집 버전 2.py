'''
a = 0
def f():
    global a
    global b
    print(a)
    a = 10
    b = 20

f()

print(a)
print(b)

def a():
    print(1)
    r = b()
    print(r)
def b():
    print(2)
    return 3

a()
print(4)

def f(n) :
    if n > 1 :
        f(n-1)
    print(n)

f(3)

def factorial(n) :
    f = 1
    for i in range(1,n+1) :
        print("%d X %d = %d" %(f,i,f*i))
        f = f * i
    return f  


n = int(input())

one = factorial(n)
print(one)

def factorial(n) :
    if n > 1 :
        return n * factorial(n-1)
    else :
        return 1


a = int(input())

b = factorial(a)

print(b)

def judge(n):
    if n > 0 :
        print("plus")
    elif n == 0 :
        print("zero")
    else :
        print("minus")

a = int(input())

judge(a)

def season(month) :
    global a
    if month > 3 and month < 6 :
        print("spring")
    elif month > 5 and month < 9 :
        print("summer")
    elif month > 8 and month < 12 :
        print("fail")
    elif month == 12 or month == 1 or month == 2 :
        print("winter")
    else :
        print("erre")


a = int(input())

season(a)

from random import *

def lotto():
    a = 0
    for i in range(1,7) :
        r = randint(1,45)
        print(r)

lotto()

from random import *

def lotto() :
    lot = []
    for i in range(6) :
        lot_append(randint(1,45))

    lot.sort()
    print(lot)

lotto()

from random import *

def lotto() :
    lot =set()
    while len(lot) < 6:
            lot.add(randint(1,45))
    
    lot = list(lot)
    lot.sort()
    print(lot)

lotto()
'''
def func_abs(a) :
    if a < 0 :
        a = a * -1
    print(a)

n = int(input())
func_abs(n)
