import turtle, random
t = turtle.Turtle()
t.pu()
t.setpos(-400.00,300.00)
t.heading()
0.00
t.pd()

dlzkadomu = int(input("zadaj dlzku domov:"))
pocetdomovriadku = int(input("zadaj pocet domov v riadkui: "))
pocetriadkov = int(input("zadaj poce riadkov: "))

def stvorec():
    turtle.delay(0)
    t.fillcolor("red")
    t.begin_fill()
    t.pensize(1)
    for i in range(4):
        t.fd(dlzkadomu)
        t.right(90)
    t.end_fill()


def posun():
    t.pu()
    t.fd(2 * dlzkadomu)
    t.lt(90)
    t.fd(dlzkadomu/2)
    t.rt(90)
    t.pd()




def trojuholnik():
    t.fillcolor("black")
    t.begin_fill()
    for i in range(3):
        t.forward(dlzkadomu)
        t.rt(120)
    t.end_fill()

def okno():
    t.fillcolor("white")
    t.begin_fill()
    for i in range(4):

        t.fd(dlzkadomu/4)
        t.right(90)
    t.end_fill()
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

    



    


def domy():
    for i in range(pocetdomov):
            dom()
            posun()



posundolex = -400
posundoley = 300

def dedina(): 
    for i in range(pocetriadkov):
        domy()
        t.pu()
        t.rt(180)
        t.fd(2.25* (pocetdomov * dlzkadomu))
        t.lt(90)
        t.fd(2 *dlzkadomu)
        t.lt(90)
        t.pd()


        
        
    
        
        
        
        

        
         
    

        


dedina()


turtle.mainloop()