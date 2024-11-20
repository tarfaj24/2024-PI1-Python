import tkinter, random

pocet = int(input("zadaj pocet jednotiek:"))

canvas= tkinter.Canvas(height=400, width=500)
canvas.pack()


def jednotka(x,y):
    canvas.create_rectangle(x+20,y,x+30,y+10,fill=farba)
    canvas.create_rectangle(x+20,y+10,x+30,y+20,fill=farba)
    canvas.create_rectangle(x+20,y+20,x+30,y+30,fill=farba)
    canvas.create_rectangle(x+20,y+30,x+30,y+40,fill=farba)
    canvas.create_rectangle(x+20,y+40,x+30,y+50,fill=farba)
    canvas.create_rectangle(x+20,y+50,x+30,y+60,fill=farba)
    canvas.create_rectangle(x+20,y+60,x+30,y+70,fill=farba)
    canvas.create_rectangle(x+30,y+60,x+40,y+70,fill=farba)
    canvas.create_rectangle(x+10,y+60,x+20,y+70,fill=farba)
    canvas.create_rectangle(x+10,y+10,x+20,y+20,fill=farba)


for i in range(pocet):
    x = random.randint(13,474)
    y = random.randint(13,310)
    jednotka(x,y)







tkinter.mainloop()