import turtle, random
t = turtle.Turtle()
t.pos()
(0.00,0.00)
t.heading()
0.00

def stvorec(dlzka):
    turtle.delay(10)
    t.pencolor(farbastvorca)
    t.pensize(10)
    for i in range(4):
        t.fd(dlzka)
        t.right(90)


def posun():
    t.pu()
    t.setpos(random.randint(-100,100), random.randint(-100,100))
    t.seth(random.randint(0,359))
    t.pd()


def trojuholnik(dlzkat):
    for i in range(3):
        t.pencolor(farbatrojuholnika)
        t.forward(dlzkat)
        t.rt(120)
def dom():
    stvorec(30)
    t.lt(60)
    trojuholnik(30)


def stvorecfill():
    t.pd
    t.pensize(5)
    t.fillcolor("red")
    t.begin_fill()
    stvorec(100)
    t.end_fill()

def pohybdomu():
    for i in range(10):
        posun()
        farba = f"#"




turtle.mainloop()