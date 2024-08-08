'''
i = 1
while i <= 10 :
    print(i, end = " ")
    i += 1

sum = 0
i = 1
sss = int(input())
while i <= sss :
    sum += i
    i += 1
print(sum)

i = 0
while i < 10 :
    i += 1
    if i % 2 == 0 :
        continue
    print(i, end = " ")

while True :
    ans = input("shall we close? (y/n)")
    if ans == "y" :
        print("the end")
        break

ans = " "
while ans != "yes" :
    ans = input("Are you ready?")
print("going out")

stamp = 0
while stamp < 10 :
    stamp += 1
    print("stamp %d." % stamp)
    if stamp == 10 :
        print("good job! free food 1 give you!")
        break

i = 0
while i<5 :
    i = i + 1
    n = int(input("input:"))
    if n %5 != 0 :
        continue
    print("output: %d" % n)

i = 0
while True :
    n = int(input())
    i = i + n 
    if n == 0 :
        print(i)
        break

a = 0
b = int(input("정수 입력 : "))
while True :
    a += 1
    c = b % 10
    print("%d" %c, end = " ")
    b //= 10
    if b == 0 :
        break
print("output : %d" % a)

a = 0
c = 0
b = int(input("정수 입력 : "))
while True :
    a += 1
    c = c*10 + b%10
    b //= 10
    if b == 0 :
        break
print("output : %d" % a)
print(c)
'''
