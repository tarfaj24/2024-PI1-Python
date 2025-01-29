import turtle, random
t = turtle.Turtle()
dlzkadomu = int(input("zadaj dlzku domov:"))
def trojuholnik():
    t.fillcolor("black")
    t.begin_fill()
    for i in range(3):
        t.forward(dlzkadomu)
        t.rt(120)
    t.end_fill()

def stvorec():
    turtle.delay(0)
    t.fillcolor("red")
    t.begin_fill()
    t.pensize(3)
    for i in range(4):
        t.fd(dlzkadomu)
        t.right(90)
    t.end_fill()
def okno():
    for i in range(4):

        t.fd(dlzkadomu/4)
        t.right(90)

def dom():
    stvorec()
    t.lt(60)
    trojuholnik()
    t.rt(150)
    t.fd(dlzkadomu / 4)
    t.lt(90)
    t.pu()
    t.fd(dlzkadomu / 4)
    t.pd()
    okno()
    t.fd(dlzkadomu/4)
    okno()
    t.rt(90)
    t.fd(dlzkadomu/4)
    t.rt(90)
    t.fd(dlzkadomu/4)
    t.rt(180)
    okno()
    t.fd(dlzkadomu/4)
    okno()
    t.rt(180)
    t.fd(dlzkadomu/4)
    t.rt(180)

    

dom()

turtle.mainloop()