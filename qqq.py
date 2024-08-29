'''
x = int(input("숫자: "))
y = int(input("숫자: "))
print("x : %d, y : %d" %(x,y))
print("x와 y는 같다?", x == y)
print("x와 y는 다르다?", x!= y)
print("x는 y보다 크댜?", x > y)
print("x는 y보다 작다?",  x < y)
print("x는 y보다 크거나 같다", x >= y)
print("x는 y보다 작거나 같다?", x <= y)

x = True
y = False
print("x : %s, y : %s" %(x,y))
print("x and y =", x and y)
print("x or y =", x or y)
print("not x  =", not x)
print("not y =", not y)

score = 80
if score >= 60 and score <= 100 :
    print("Pass")
else :
    print("Fail")

score =50
if score >= 60 and score <= 100 :
    print("Pass")
else :
    print("Fail")

score = 90
if score >= 90 :
    print("A")
print("Pass")
    print("congratulation")

score = 72
if score >= 90 :
    print("A")
elif score >= 60:
    print("B")
else :
    print("C")

score = int(input("숫자 :"))
if score >= 90 :
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else :
    print("D")

score = int(input("숫자 :"))
if score >= 90 :
    print("A")
else :
    if score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else :
        print("D")

a = int(input())
b = int(input())
c = int(input())
print(a>= 140 and b>=140 and c >= 140)

a = int(input())
if a%2==0 :
    print("EVEN")
else :
    print("ODD")

y = int(input("year : "))

if ((y%4 ==0 and y%100 != 0) or (y%400 == 0 )):
    print("leap year")
else :
    print("common year")

a = 1 in [1,2,3]
print(a)

case = ["homework", "eating", "sleeping"]
a = input("case :")
if a in case :
    print("I have to do %s" %a)
else :
    print("I don't have %s" %a)

a = input()
if a == "m" :
    print("man")
elif a == "w" :
    print("woman")
else :
    print("what?")
'''
a = input()
if
