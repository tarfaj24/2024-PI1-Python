import tkinter
canvas = tkinter.Canvas(height=320, width=320)
canvas.pack()
def sedem(x, y):
    canvas.create_rectangle(x,y,x+10,y+10, fill="black")
    canvas.create_rectangle(x+10,y,x+20,y+10, fill="black")
    canvas.create_rectangle(x+20,y,x+30,y+10, fill="black")
    canvas.create_rectangle(x+30,y,x+40,y+10, fill="black")
    canvas.create_rectangle(x+40,y,x+50,y+10, fill="black")
    canvas.create_rectangle(x+40,y+10,x+50,y+20, fill="black")
    canvas.create_rectangle(x+30,y+20,x+40,y+30, fill="black")
    canvas.create_rectangle(x+20,y+30,x+30,y+40, fill="black")
    canvas.create_rectangle(x+10,y+40,x+20,y+50, fill="black")
    canvas.create_rectangle(x+10,y+50,x+20,y+60, fill="black")
    canvas.create_rectangle(x+10,y+60,x+20,y+70, fill="black")

def tri(x,y):
    canvas.create_rectangle(x,y,x+10,y+10, fill="black")
    canvas.create_rectangle(x+10,y,x+20,y+10, fill="black")
    canvas.create_rectangle(x+20,y,x+30,y+10, fill="black")
    canvas.create_rectangle(x+30,y,x+40,y+10, fill="black")
    canvas.create_rectangle(x+40,y,x+50,y+10, fill="black")
    canvas.create_rectangle(x+30,y+10,x+40,y+20, fill="black")
    canvas.create_rectangle(x+20,y+20,x+30,y+30, fill="black")
    canvas.create_rectangle(x+30,y+30,x+40,y+40, fill="black")
    canvas.create_rectangle(x+40,y+40,x+50,y+50, fill="black")
    canvas.create_rectangle(x+40,y+50,x+50,y+60, fill="black")
    canvas.create_rectangle(x+30,y+60,x+40,y+70, fill="black")
    canvas.create_rectangle(x+20,y+60,x+30,y+70, fill="black")
    canvas.create_rectangle(x+10,y+60,x+20,y+70, fill="black")
    canvas.create_rectangle(x,y+50,x+10,y+60, fill="black")

def riadoksedem(x,y,pocet7):
    for i in range(pocet7):
        sedem(x,y)
        x = x+120


def riadoktri(x,y,pocet3):
    for i in range(pocet3):
        tri(x,y)
        x = x+120

def riadkytri(x,y,pocet3,pocetriadkov3):
    for i in range(pocetriadkov3):
        riadoktri(x,y,pocet3)
        y = y + 80

def riadky7(x,y,pocet7,pocetriadkov7):
    for i in range(pocetriadkov7):
        riadoksedem(x,y,pocet7)
        y = y+80
    

riadkytri(10,10,3,4)
riadky7(70,10,2,4)



tkinter.mainloop()