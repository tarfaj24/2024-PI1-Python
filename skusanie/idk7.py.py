import tkinter
import random

canvas = tkinter.Canvas(background="navy")
canvas.pack()

n = int(input("zadaj pocet hviezd: "))

canvas.create_rectangle(1,500,500,1,fill="navy")
for i in range(n):
    x = random.randint(5,370)
    y = random.randint(5,260)
    velkost = random.randint(10,20)
    canvas.create_text(x,y,text="*",fill="yellow",font=f"arial {velkost}")

tkinter.mainloop()