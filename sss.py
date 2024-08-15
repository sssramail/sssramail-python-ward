'''
List = ["a","b","c"]
for s in List :
    print(s)

num_list = [1,2,3,4,5]
sum = 0
for num in num_list :
    sum += num
print("asg : %d " %(sum//5))

aList = [1,2,3]
bList = [10,100,1000]
for a in aList :
    for b in bList :
        print(a * b, end = ' ')
    print()

a = [1,2,3]
b = ["a","b","c"]
for n in a :
    for m in b :
        print("%d %c" %(n,m), end = " ")
    print()

for i in range(10) :
    print(i, end = " ")

for i in range(10,21) :
    print(i, end = " ")

for i in range(1,10,2) :
    print(i, end = " ")

List = ["Noah","Minsu","Keily","Yuri"]

for name in List :
    print("%s, Congratulation" % name)

n = int(input("몇단임?"))
for i in range(1,10) :
    print("%d X %d = %d" %(n,i,n*i))

a = int(input("정수입력"))
for i in range(1,a + 1) :
    print(i, end = " ")
print()

sum = 0
n = 0
while True :
   a = int(input())
   n += 1
   sum = sum + a
   if a == -1 :
       sum += 1
       n = n - 1
       print("sum : %d" %sum)
       sum = sum/n
       print("avg : %d" %sum)
       break

for i in range(2,10) :
    print("< %d 단 >" %i)
    for j in range(1,10) :
        print("%d X %d = %d" %(i,j,i*j))
    print()

a = int(input())
sum = 0
for i in range(1,a+1) :
    if i%3 == 0 :
        sum = sum + i

print(sum)
'''
