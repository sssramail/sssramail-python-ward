import turtle

t = turtle.Turtle()
t.penup()
t.setx(200)
t.write("동", font = ("Arial", 30))
t.setx(-200)
t.write("서", font = ("Arial", 30))
t.setx(0)
t.sety(-200)
t.write("남", font = ("Arial", 30))
t.sety(200)
t.write("북", font = ("arial", 30))
t.goto(0,0)
t.pendown()
t.pencolor("blue")
a = turtle.textinput("거부부북", "방향을 입력하셈.  ($.$)")
t.speed(1)

if a == "동" :
    t.goto(200,0)
elif a == "서" :
    t.goto(-200,0)
elif a == "남" :
    t.goto(0,-200)
elif a == "북" :
    t.goto(0,200)
else :
    t.left(360)

turtle.done()
