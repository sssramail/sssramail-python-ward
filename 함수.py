'''
def add(x,y) :
    s = x + y
    return s

result = add(10,20) + add(20,30)
print(result)
def minurs(x,y) :
    s = x - y
    return s
result = minurs(40,20) + add(10,20)
print(result)

def f(n) :
    n = 20
    return n


n = 10

f(n)
print(n)

n = f(n)
print(n)

def get_max(x,y) :
    if x > y :
        return x
    else :
        return y


x = int(input())
y = int(input())

n = get_max(x,y)
print(n)

def on_off(x) :
    if x > 0 :
        return "True"
    elif x == 0 :
        return "it's Zero"
    else :
        return "False"

x = int(input())

oner = on_off(x)
print(oner)

def go(n) :
    s = 0
    for i in range(1,n+1) :
        s = s + i
    return s

a = int(input())

one = go(a)

print("1부터 %d까지의 합은 %d입니다" %(a,one))

def go(a,b) :
    s = 0
    if a > b :
        for i in range(b,a+1) :
            s = s + i
        return s
    if b > a :
        for i in range(a,b+1) :
            s = s + i
        return s

a = int(input())
b = int(input())

one = go(a,b)

if a > b :
    n = a
    x = b
elif b > a :
    n = b
    x = a

print("%d부터 %d까지의 합은 %d입니다" %(n,x,one))

def sps(a,b,n) :
    s = 0
    if n == "x" :
        s = a * b
        return s
    if n == "y" :
        s = a * b * 0.5
        return s

a = int(input())
b = int(input())
c = input("x는 사각형,y는 삼각형. :")

o = sps(a,b,c)
print(o)

def even_odd(a) :
    if a%2 == 0 :
        return "even"
    else :
        return "odd"

a = int(input())

one = even_odd(a)
print(one)

def on(a) :
    s = 0
    n = 0
    while True :
        i = int(input())
        n = n + 1
        s = s + i
        if n == a :
            return s
            break

a = int(input())

one = on(a)
print(one)
'''
def on(a) :
    s = 0
    n = 0
    while True :
        i = int(input())
        n = n + 1
        s = s < i
        if n == a :
            break
            return s

a = int(input())

one = on(a)
print(one)
