import tkinter
canvas = tkinter.Canvas(height=320, width=320)
canvas.pack()
def yko(x, y):
    canvas.create_rectangle(x,y, x+10, y+10,fill="black")
    canvas.create_rectangle(x, y+10, x+10, y+20,fill="black")
    canvas.create_rectangle(x+10, y+20, x+20, y+30,fill="black")
    canvas.create_rectangle(x+20, y+30, x+30, y+40,fill="black")
    canvas.create_rectangle(x+20, y+40, x+30, y+50,fill="black")
    canvas.create_rectangle(x+20, y+50, x+30, y+60,fill="black")
    canvas.create_rectangle(x+20, y+60, x+30, y+70,fill="black")
    canvas.create_rectangle(x+30, y+20, x+40, y+30,fill="black")
    canvas.create_rectangle(x+40, y+10, x+50, y,fill="black")
    canvas.create_rectangle(x+40, y+20, x+50, y+10,fill="black")
    canvas.create_rectangle(x+40, y+10, x+50, y,fill="black")

def riadok_y(x,y,pocet):
    for i in range(pocet):
        yko(x,y)
        x = x+60

def riadky_y(x,y,pocetriadkov,pocet):
    for i in range(pocetriadkov):
        riadok_y(x,y,pocet)
        y=y+90

riadky_y(10,10,4,5)
tkinter.mainloop()



    