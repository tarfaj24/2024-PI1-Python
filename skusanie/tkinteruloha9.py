import tkinter
from math import sin, cos, radians

canvas = tkinter.Canvas()
canvas.pack()

n = int(input('zadaj n: '))
x, y, r = 180, 130, 125
uhol = 360 / n
for i in range(0, n):
    for j in range(i + 1, n):
        x1 = x + r * cos(radians(uhol * i))
        y1 = y + r * sin(radians(uhol * i))
        x2 = x + r * cos(radians(uhol * j))
        y2 = y + r * sin(radians(uhol * j))
        canvas.create_line(x1, y1, x2, y2)

tkinter.mainloop()