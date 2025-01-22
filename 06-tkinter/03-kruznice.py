import tkinter, math

canvas = tkinter.Canvas()
canvas.pack()

x0, y0 = 180, 130  #suradnice stredu
r = 110   #polomer

for uhol in range(0, 360, 15):
    x = x0 + r * math.cos(math.radians(uhol))
    y = y0 + r * math.sin(math.radians(uhol))
    canvas.create_line(x0, y0, x, y)
    canvas.create_text(x, y, text=uhol)



tkinter.mainloop()
