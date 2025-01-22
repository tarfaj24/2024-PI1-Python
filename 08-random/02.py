import tkinter, random

canvas= tkinter.Canvas(height=400, width=500)

dlzka = int(input("zadaj dlzku stvorca: "))
pocet = int(input("zadaj pocet stvorcov: "))


canvas.pack()

for i in range(pocet):
    x = random.randint(3,500-dlzka-3)
    y = random.randint(3,400-dlzka-3)
    farba = f'#{random.randrange(256**3):06x}'
    canvas.create_rectangle(x,y,x+dlzka,y+dlzka,fill=farba)

tkinter.mainloop()