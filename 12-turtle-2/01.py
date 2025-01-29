import turtle
t = turtle.Turtle()

pocet = 3
dlzka = 30


def schody(pocet,dlzka):
    for i in range(pocet):
        t.fd(dlzka)
        t.rt(90)
        t.fd(dlzka)
        t.lt(90)


for i in range(3):
    schody(pocet,dlzka)
    t.lt(90)
    t.pu()
    t.fd(pocet * dlzka)
    t.rt(90)
    t.pd()









turtle.mainloop()