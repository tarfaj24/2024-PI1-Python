
import turtle, random
t = turtle.Turtle()


dlzka = 15

def stvorec():
    for i in range(4): 
        t.fd(dlzka)
        t.right(90)

def fillstvorec():
    t.pd
    t.pensize(5)
    t.fillcolor(farba)
    t.begin_fill()
    stvorec()
    t.end_fill()



def pismenoj():
    turtle.delay(0)
    for i in range(3):
        fillstvorec()
        t.fd(dlzka)
    t.pu
    t.backward(2 * dlzka)
    t.pd
    t.rt(90)
    t.fd(15)
    t.lt(90)
    for i in range(5):
        fillstvorec()
        t.rt(90)
        t.fd(dlzka)
        t.lt(90)
    t.pd
    t.rt(180)
    t.fd(dlzka)
    t.pu
    t.rt(180)
    for i in range(2):
        fillstvorec()
        t.rt(180)
        t.fd(dlzka)
        t.rt(180)
    t.lt(90)
    t.fd(dlzka)
    t.rt(90)
    fillstvorec()

def posun():
    t.pu()
    t.setpos(random.randint(-100,100), random.randint(-100,100))
    t.seth(random.randint(0,359))
    t.pd()

for i in range(10):
    posun()
    farba = f"#{random.randrange(256**3):06x}"
    pismenoj()




turtle.mainloop()
    