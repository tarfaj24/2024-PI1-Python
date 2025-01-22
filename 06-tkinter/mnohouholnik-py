import tkinter
import random
from math import sin, cos, radians

canvas = tkinter.Canvas()
canvas.pack()

x0, y0 = 150, 130
r = 110

n = int(input("zadaj aký chces mnohouholnik: "))

x,y=x0+r, y0

for i in range(1,n+1):
    x1 = x0+r * cos(radians(i * 360/n))
    y1 = y0 + r * sin(radians(i*360/n))
    farba= f"#{random.randrange(256**3):06x}"
    canvas.create_line(x,y,x1,y1,fill=farba,width=30)
    x,y=x1,y1




tkinter.mainloop()