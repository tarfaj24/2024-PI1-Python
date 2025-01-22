import tkinter

canvas = tkinter.Canvas(width=370,height=250)
canvas.pack()

x = 3


for i in range(25):
    r=255-i*10
    b=255-r
    farba = f"#{r:02x}00{b:02x}"
    canvas.create_rectangle(x,5,x+25,255,fill=farba,width=0)
    x+=15


tkinter.mainloop()