import tkinter

xx = yy = None

def klik(event):
    global xx, yy
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')
    if xx != None:
        canvas.create_line(xx, yy, x, y)
    xx, yy = x, y

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)

tkinter.mainloop()