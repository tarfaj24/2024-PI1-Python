import random
import tkinter

pocet = int(input("Zadaj počet jednotiek: "))

canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()


def jednotka(x, y):
    x = random.randint(3, 500-33)
    y = random.randint(3, 400-73)
    canvas.create_rectangle(x, y+10, x+10, y+20, fill=random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"]))
    canvas.create_rectangle(x+10, y, x+20, y+10, fill=random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"]))
    canvas.create_rectangle(x+10, y+10, x+20, y+20, fill=random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"]))
    canvas.create_rectangle(x+10, y+20, x+20, y+30, fill=random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"]))
    canvas.create_rectangle(x+10, y+30, x+20, y+40, fill=random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"]))
    canvas.create_rectangle(x+10, y+40, x+20, y+50, fill=random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"]))
    canvas.create_rectangle(x+10, y+50, x+20, y+60, fill=random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"]))
    canvas.create_rectangle(x, y+60, x+10, y+70, fill=random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"]))
    canvas.create_rectangle(x+10, y+60, x+20, y+70, fill=random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"]))
    canvas.create_rectangle(x+20, y+60, x+30, y+70, fill=random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"]))

for _ in range(pocet):
    jednotka(10, 10)


tkinter.mainloop()