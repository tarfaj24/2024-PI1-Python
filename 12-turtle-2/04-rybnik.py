import turtle, random
t1 = turtle.Turtle()
t2= turtle.Turtle()
t3= turtle.Turtle()
t4= turtle.Turtle()
t5= turtle.Turtle()
t6= turtle.Turtle()
t7= turtle.Turtle()
t8= turtle.Turtle()
t9= turtle.Turtle()
t10= turtle.Turtle()
t11= turtle.Turtle()

tbg = turtle.Turtle()

t5.hideturtle()
t4.hideturtle()
t3.hideturtle()
t2.hideturtle()
t6.hideturtle()
t1.hideturtle()
t7.hideturtle()
t8.hideturtle()
t9.hideturtle()
t10.hideturtle()
t11.hideturtle()


def background(t):
    t.pd()
    t.setpos(-400,290)
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.fd(800)
        t.rt(90)
        t.fd(500)
        t.rt(90)
    t.end_fill()
    t.pencolor("black")
    t.pensize(10)
    for i in range(2):
        t.fd(800)
        t.rt(90)
        t.fd(500)
        t.rt(90)
    t.pensize(4)
    t.rt(90)
    t.fd(490)
    t.lt(90)
    t.pu()
    t.fd(30)
    t.lt(90)
    t.pd()
    t.pencolor("green")
    for i in range(55):
        t.lt(15)
        t.fd(80)
        t.rt(180)
        t.fd(80)
        t.lt(155)
        t.fd(80)
        t.pu()
        t.rt(170)
        t.fd(78.8)
        t.lt(90)
        t.lt(90)
        t.pd()
    t.pencolor("cornflowerblue")   
    for i in range(40):
        t.pu()
        t.setpos(random.randint(-360,390),random.randint(2,260))
        t.pd()
        t.fillcolor("deepskyblue")
        t.begin_fill()
        t.circle(15)
        t.end_fill()
    t.pencolor("slateblue")
    

    

def ryba(t):
    t.pencolor("black")
    t.lt(90)
    t.rt(70)
    t.pensize(5)
    t.fillcolor("red")
    t.begin_fill()
    t.lt(35)
    for i in range(10):
        t.fd(26)
        t.rt(10)
    t.rt(100)
    for i in range(10):
        t.fd(26)
        t.rt(10)
    t.lt(155)
    t.fd(80)
    t.end_fill()
    t.pu()
    t.lt(103)
    t.fd(180)
    t.pd()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(10) 
    t.end_fill()
    t.rt(180)  
    t.pu()
    t.fd(70)
    t.rt(90)
    t.fd(40)
    t.rt(190)
    t.pd()
    t.fd(40)
    t.lt(90)
    t.pu()
    t.fd(20)
    t.lt(90)
    t.pd()
    t.fd(40)
    t.rt(90)
    t.pu()
    t.fd(20)
    t.rt(90)
    t.pd()
    t.fd(40)



turtle.update()


def pohybryby():
    background(tbg)
    for i in range(10):
        t1.setpos(-370,160)
        ryba(t1)
        t1.clear()
        t2.setpos(-310,160)
        ryba(t2)
        t2.clear()
        t3.setpos(-260,160)
        ryba(t3)
        t3.clear()
        t4.setpos(-210,160)
        ryba(t4)
        t4.clear()
        t5.setpos(-160,160)
        ryba(t5)
        t5.clear()
        t6.setpos(-110,160)
        ryba(t6)
        t6.clear()
        t7.setpos(-60,160)
        ryba(t7)
        t7.clear()
        t8.setpos(-10,160)
        ryba(t8)
        t8.clear()
        t9.setpos(40,160)
        ryba(t9)
        t9.clear()
        t10.setpos(90,160)
        ryba(t10)
        t10.clear()
        t11.setpos(140,160)
        ryba(t11)
        t11.clear()
    
def pohybryby1():
    t1.pu()
    t1.setpos(-370,160)
    t1.pd()
    ryba(t1)
    
def pohybryby2():
    t2.pu()
    t2.setpos(-310,160)
    t2.pd()
    ryba(t2)

def pohybryby3():
    t3.pu()
    t3.setpos(-260,160)
    t3.pd()
    ryba(t3)
    
def pohybryby4():
    t4.pu()
    t4.setpos(-210,160)
    t4.pd()
    ryba(t4)


def pohybryby5():
    t5.pu()
    t5.setpos(-160,160)
    t5.pd()
    ryba(t5)


def pohybryby6():
    t6.pu()
    t6.setpos(-110,160)
    t6.pd()
    ryba(t6)


def pohybryby7():
    t7.pu()
    t7.setpos(-60,160)
    t7.pd()
    ryba(t7)


def pohybryby8():
    t8.pu()
    t8.setpos(-10,160)
    t8.pd()
    ryba(t8)


def pohybryby9():
    t9.pu()
    t9.setpos(40,160)
    t9.pd()
    ryba(t9)


def pohybryby10():
    t10.pu()
    t10.setpos(90,160)
    t10.pd()
    ryba(t10)


def pohybryby11():
    t11.pu()
    t11.setpos(140,160)
    t11.pd()
    ryba(t11)





 


turtle.tracer(0,0)
background(tbg)

for i in range(15):
    turtle.delay(0)
    t1.seth(360)
    t2.seth(360)
    t3.seth(360)
    t4.seth(360)
    t5.seth(360)
    t6.seth(360)
    t7.seth(360)
    t8.seth(360)
    t9.seth(360)
    t10.seth(360)
    t11.seth(360)


    turtle.tracer(0,0)
    pohybryby1()
    turtle.update()
    turtle.tracer(1,10)
    turtle.delay(5)
    t1.pu()
    t1.fd(100)
    t1.pd()
    t1.clear()

    turtle.tracer(0,0)
    pohybryby2()
    turtle.update()
    turtle.tracer(1,10)
    turtle.delay(5)
    t2.pu()
    t2.fd(100)
    t2.pd()
    t2.clear()

    turtle.tracer(0,0)
    pohybryby3()
    turtle.update()
    turtle.tracer(1,10)
    turtle.delay(5)
    t3.pu()
    t3.fd(100)
    t3.pd()
    t3.clear()

    turtle.tracer(0,0)
    pohybryby4()
    turtle.update()
    turtle.tracer(1,10)
    turtle.delay(5)
    t4.pu()
    t4.fd(100)
    t4.pd()
    t4.clear()

    turtle.tracer(0,0)
    pohybryby5()
    turtle.update()
    turtle.tracer(1,10)
    turtle.delay(5)
    t5.pu()
    t5.fd(100)
    t5.pd()
    t5.clear()

    turtle.tracer(0,0)
    pohybryby6()
    turtle.update()
    turtle.tracer(1,10)
    turtle.delay(5)
    t6.pu()
    t6.fd(100)
    t6.pd()
    t6.clear()

    turtle.tracer(0,0)
    pohybryby7()
    turtle.update()
    turtle.tracer(1,10)
    turtle.delay(5)
    t7.pu()
    t7.fd(100)
    t7.pd()
    t7.clear()

    turtle.tracer(0,0)
    pohybryby8()
    turtle.update()
    turtle.tracer(1,10)
    turtle.delay(5)
    t8.pu()
    t8.fd(100)
    t8.pd()
    t8.clear()

    turtle.tracer(0,0)
    pohybryby9()
    turtle.update()
    turtle.tracer(1,10)
    turtle.delay(5)
    t9.pu()
    t9.fd(100)
    t9.pd()
    t9.clear()

    turtle.tracer(0,0)
    pohybryby10()
    turtle.update()
    turtle.tracer(1,10)
    turtle.delay(5)
    t10.pu()
    t10.fd(100)
    t10.pd()
    t10.clear()

    turtle.tracer(0,0)
    pohybryby11()
    turtle.update()
    turtle.tracer(1,10)
    turtle.delay(5)
    t11.pu()
    t11.fd(100)
    t11.pd()
    t11.clear()
    
    








turtle.done()