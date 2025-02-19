import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack(side="left")

def vypis():
    x = random.randrange(50, 330)
    y = random.randrange(20, 240)
    canvas.create_text(x,y, text = vstup.get(),fill =f"{farba.get()}",font = f"arial {velkost.get()}",)
    canvas.create_image(x+80,y, image=obr)
obr = tkinter.PhotoImage(file='3.png')



def zmaz():
    canvas.delete('all')


tkinter.Button(text = "vypis", command=vypis).pack()
tkinter.Button(text = "zmaz", command =zmaz).pack()
tkinter.Label(text="zadaj text").pack()
vstup = tkinter.Entry(width = 13)
vstup.pack()
tkinter.Label(text="zadaj farbu").pack()
farba = tkinter.Entry(width = 13)
farba.pack()
tkinter.Label(text="zadaj velkost")
velkost = tkinter.Scale(length=70,from_=10,to=60,orient="horizontal")
velkost.pack()
x = random.randrange(50, 330)
y = random.randrange(20, 240)


tkinter.mainloop()