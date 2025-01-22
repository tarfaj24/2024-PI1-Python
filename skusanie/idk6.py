import tkinter
import random

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

for y in range(3, 400, 30):
    for x in range (3, 400, 30):
        farba = random.choice(["blue", "cyan", "green", "red", "yellow", "pink", "chocolate", "darkorange"])
        canvas.create_rectangle(x,y,x+25,y+25, fill=farba)









tkinter.mainloop()