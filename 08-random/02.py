import tkinter, random

canvas= tkinter.Canvas(height=400, width=500)

dlzka = int(input("zadaj dlzku stvorca: "))
pocet = int(input("zadaj pocet stvorcov: "))


canvas.pack()

for i in range(pocet):
    x = random.randint(3,487-dlzka-3)
    y = random.randint(3,387-dlzka-3)
    canvas.create_rectangle(x,y,x+dlzka,y+dlzka,fill=random.choice(["red","green","blue","yellow"]))

tkinter.mainloop()