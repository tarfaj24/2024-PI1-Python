import tkinter
canvas = tkinter.Canvas(width=320, height=320)
canvas.pack()

def yko(x,y):
    canvas.create_rectangle(x, y, x+10, y+10)
    canvas.create_rectangle(x, y+20, x+10, y+10)
    canvas.create_rectangle(x+10,y+20,x+20,y+30)
    canvas.create_rectangle(x+20,y+30,x+30,y+40)
    canvas.create_rectangle(x+20,y+40,x+30,y+50)
    canvas.create_rectangle(x+20,y+50,x+30,y+60)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)
    canvas.create_rectangle(x+30,y+20,x+40,y+30)
    canvas.create_rectangle(x+40,y+20,x+50,y+10)
    canvas.create_rectangle(x+40,y+10,x+50,y)

def riadok_y(x,y, pocet):
    for i in range(pocet):
        yko(x,y)
        x=x+60

    
riadok_y(10,90,3)




tkinter.mainloop()

