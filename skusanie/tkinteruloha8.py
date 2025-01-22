import tkinter,random
from math import sin,cos,radians

canvas = tkinter.Canvas()
canvas.pack()

n = int(input("zadaj kolkopocetný chces mnohouholník: "))
a = int(input("zadaj dĺžku strany mnohouholníka: "))

x0,y0 = 180,130 
r = a / sin(radians(180 / n)) / 2
x, y=x0+r,y0

for i in range(1,n+1):
    x1 = x0+r * cos(radians(i*360/n))
    y1 = y0+ r* sin(radians(i*360/n))
    canvas.create_line(x,y,x1,y1,width=3)
    x,y=x1,y1








tkinter.mainloop()