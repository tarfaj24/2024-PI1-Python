import tkinter

canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

a = 50,250
b=330,250
c=190,7.5189

canvas.create_polygon(a,b,c,fill="blue")

tkinter.mainloop()