'''
def anj(a,b,c,e) :
    s = a + b + c + e
    return s
def ai(a,b,c,e) :
    s = a + b + c + e
    n = s/4
    return n

a = int(input("수학:"))
b = int(input("국어:"))
c = int(input("사회:"))
e = int(input("과학:"))

one = anj(a,b,c,e)
print(one)
one = ai(a,b,c,e)
print(one)

def wornl(n) :
    a = 0
    for i in range(1,n+1) :
        a = a + i
    print(a)

n = int(input())
wornl(n)
'''
def func_abs(a,b,c,d,e) :
    if a < 0 :
        a = a * -1
    print(a)
    if b < 0 :
        b = b * -1
    print(b)
    if c < 0 :
        c = c * -1
    print(c)
    if d < 0 :
        d = d * -1
    print(d)
    if e < 0 :
        e = e * -1
    print(e)




a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

func_abs(a,b,c,d,e)
