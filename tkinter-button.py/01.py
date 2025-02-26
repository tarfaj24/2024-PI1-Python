import tkinter
import random

def vypis():
    text = 'PYTHON'
    x = random.randrange(50, 330)
    y = random.randrange(20, 240)
    canvas.create_text(x, y, text=text, font='arial 20')

def zmaz():
    canvas.delete('all')
canvas = tkinter.Canvas()
canvas.pack()

tlacidlo = tkinter.Button(text = "vypis", command = vypis).pack()
tlacidlo = tkinter.Button(text = "zmaz", command = zmaz).pack()

vstup = tkinter.Entry(width=10)
vstup.pack()

tkinter.mainloop()