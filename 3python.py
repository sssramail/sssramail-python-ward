import random

print("== 주사위 게임 ==")
a = random.randint(1,6)
b = random.randint(1,6)
print("== 첫 번째 주사위 ==")
print("a(%d)  :  b(%d)" %(a,b))
c = random.randint(1,6)
v = random.randint(1,6)
print("== 두 번째 주사위 ==")
print("a(%d)  :  b(%d)" %(c,v))
print("== 결과 ==")
a = a + c
b = b + v 
print("a(%d)  :  b(%d)"  %(a,b))

if a<b :
    print("B님 승리!")
elif a>b :
    print("A님 승리!")
else :
    print("비겼다!")

print("== <주사위 게임이 종료되었습니다> ==")
