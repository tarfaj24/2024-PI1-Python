import tkinter, random

canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()

def program():
    canvas.delete("all")
    x = random.randint(30,370)
    y = random.randint(30,370)

    for znak in retazec.get():
        farba = f"#{random.randrange(256**3):06x}"
        canvas.create_text(x, y, text=znak, font="arial 15", fill=farba)
        x += 12
        
        if znak == " ":

            x = random.randint(30,370)
            y = random.randint(30,370)

tkinter.Label(text="zadaj vetu:").pack()
retazec = tkinter.Entry()
retazec.pack()
tkinter.Button(text="spusti program", command=program).pack()

tkinter.mainloop()