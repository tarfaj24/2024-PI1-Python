import tkinter
import random

canvas_width = int(input("Sirka platna:  "))
canvas_height = int(input("Vyska platna: "))

canvas = tkinter.Canvas(width= canvas_width,height=canvas_height)
canvas.pack()

zadane = int(input("zadaj pocet stvorcov: "))

for i in range(zadane):
    dlzka = random.randrange(1,30)
    x = random.randint(3,canvas_width - 3 - dlzka)
    y = random.randint(3,canvas_height - 3 - dlzka)
    if dlzka <= 10:
        farba = "red"
    elif dlzka <= 20:
        farba = "green"
    else:
        farba = "blue"
    stvorec = canvas.create_rectangle(x,y,x+dlzka,y+dlzka,fill=farba, width = 0) #width zmeni velkost okrajov stvorca



tkinter.mainloop()