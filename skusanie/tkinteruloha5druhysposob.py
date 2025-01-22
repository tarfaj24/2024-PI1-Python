import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x, y = 50, 250
a = 280
canvas.create_polygon(x, y, x + a, y, x + a / 2, y - ((280**2-140**2)**(1/2)), fill='blue')

tkinter.mainloop()