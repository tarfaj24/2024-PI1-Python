import tkinter,random

canvas = tkinter.Canvas(width=300,height=300)
canvas.pack()

x,y = 20,60

textt = input("zadaj text: ")


for pismeno in textt:
    farba = f"#{random.randrange(256**3):06x}"
    canvas.create_rectangle(x,y,x+30,y+30,fill=farba)
    farba1 = f"#{random.randrange(256**3):06x}"
    canvas.create_text(x+15,y+15,text=pismeno,fill=farba1,font="arial 26")
    x+=30



tkinter.mainloop()