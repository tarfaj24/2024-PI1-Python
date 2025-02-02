import turtle
t = turtle.Turtle()
f = 30

def stvorce():
    for f in range(30,241,30):
        for n in range(4):
            t.fd(f)
            t.rt(90)
        t.pu()
        t.lt(135)
        t.fd(21.2130)
        t.rt(135)
        t.pd()

def polobluk():
    for i in range(10):
        t.fd(15)
        t.rt(12)

def celyobluk():
    for i in range(2):
        polobluk()
        t.rt(60)

def kvet():
    for i in range(30):
        celyobluk()
        t.rt(15)


def kruhy():
    for i in range(30,150,30):
        t.circle(i)
        t.rt(90)
        t.pu()
        t.fd(30)
        t.pd()
        t.lt(90)

turtle.delay(0)
t.setpos(0,0)
kvet()
t.pu()
t.setpos(-30,0)
t.pd()
kruhy()
t.pu()
t.setpos(15,15)
t.pd()
stvorce()

turtle.done()