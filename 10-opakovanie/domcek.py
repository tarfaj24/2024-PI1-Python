import tkinter
import random

canvas_width = 600
canvas_height = 600
x = 50
y = 150
dlzka = 50
farba = "green"

canvas = tkinter.Canvas(height=canvas_height, width=canvas_width)
canvas.pack()

def dom(x, y, dlzka, farba):
    stvrtina = dlzka /4
    polovica = dlzka /2
    # canvas.create_polygon(x0, y0, x1, y1, x2, y2)   #vykreslí mnohouholník v tomto prípade trojúholník, lebo prejde cez tri body (x,y)
    canvas.create_polygon(x , y + polovica, x + polovica, y, x + dlzka, y + polovica)
    canvas.create_rectangle(x, y + polovica, x + dlzka, y + polovica + dlzka, fill=farba)
    canvas.create_rectangle(x + stvrtina, y + dlzka /2 + stvrtina, x + stvrtina+ polovica, y + dlzka + stvrtina, fill="light blue")
    canvas.create_line(x + stvrtina, y + dlzka, x + stvrtina + polovica, y + dlzka)
    canvas.create_line(x + polovica, y + polovica + stvrtina, x + polovica, y + dlzka + stvrtina)

def ulica(x, y, dlzka, pocet):
    farba1, farba2 = "red", "green"
    for i in range(pocet):
        dom(x, y, dlzka, farba1)
        x = x + dlzka + 2
        farba1, farba2 = farba2, farba1


ulica(x, y, dlzka, 5)

canvas.mainloop()