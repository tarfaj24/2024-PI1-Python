import tkinter

canvas = tkinter.Canvas(width = 400, height = 400)
canvas.pack()

#Nemecko
def nemecko(x,y):
    canvas.create_rectangle(x,y,x+135,y+30,fill="black",width=0)
    canvas.create_rectangle(x,y+30,x+135,y+60,fill="red",width=0)
    canvas.create_rectangle(x,y+60,x+135,y+90,fill="yellow",width=0)
    canvas.create_rectangle(x,y,x+135,y+90)

def taliansko(x,y):
    canvas.create_rectangle(x,y,x+45,y+90,fill="green",width=0)
    canvas.create_rectangle(x+45,y,x+90,y+90,fill="white",width=0)
    canvas.create_rectangle(x+90,y,x+135,y+90,fill="red",width=0)
    canvas.create_rectangle(x,y,x+135,y+90)

def francúzko(x,y):
    canvas.create_rectangle(x,y,x+45,y+90,fill="blue",width=0)
    canvas.create_rectangle(x+45,y,x+90,y+90,fill="white",width=0)
    canvas.create_rectangle(x+90,y,x+135,y+90,fill="red",width=0)
    canvas.create_rectangle(x,y,x+135,y+90)
    
def ukrajina(x,y):
    canvas.create_rectangle(x,y,x+135,y+45,fill="blue", width=0)
    canvas.create_rectangle(x,y+45,x+135,y+90,fill="yellow", width=0)
    canvas.create_rectangle(x,y,x+135,y+90)


nemecko(20,20)
taliansko(200,20)
francúzko(20,200)
ukrajina(200,200)

tkinter.mainloop()