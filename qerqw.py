from random import *

a = 0
ad = 0
b = 0
bd = 0

print("====RUNIG GAME====")
while True :
    a = randint(1,5)
    ad = ad + a
    b = randint(1,5)
    bd = bd + b
    print("a(%d) : b(%d)" %(ad,bd))
    if ad > 30 or ad == 30 :
        print("a win!")
        break
    elif bd > 30 or bd == 30 :
        print("b win!")
        break
