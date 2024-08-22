'''
n = int(input())
sum = 0
while n>0 :
    sum = sum + n%10
    n = n // 10

print(sum)

n = int(input())
for i in range(1,n+1) :
    print(i*"*")

n = int(input())

for i in range(1,n+1) :
    for j in range(1, i+1) :
        print("*" , end = "")
    print()

print()

n = int(input())
sum = 0
for i in range(1,n+1) :
    for j in range(1, i+1) :
        sum = sum + 1
        print(sum , end = "")
    print()
    sum = 0

print()

n = int(input())

for i in range(1,n+1) :
    for j in range(n,i,-1) :
        print(" ", end = "")
        
    for k in range(1, i+1) :
        print(k, end = "")
    for o in range(i-1,0,-1) :
        print(o, end="")

    print()
    
print()

n = int(input())

for i in range(2,n+1) :
    cnt = 0
    for j in range(1,i+1) :
        if i%j == 0 :
            cnt = cnt + 1

    if cnt == 2 :
        print(i, end = " ")
'''
