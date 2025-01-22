import tkinter

canvas=tkinter.Canvas()
canvas.pack()


polovica = 25
stvrtina = 50 / 4
tristvrte = (50/4) * 3
dlzka = 50


def dom(x,y,dlzka,farba):
    canvas.create_rectangle(x,y,x+dlzka,y+dlzka,fill=farba)
    canvas.create_rectangle(x+stvrtina,y+stvrtina,x+tristvrte,y+tristvrte,fill="light blue")
    canvas.create_line(x+stvrtina,y+polovica,x+tristvrte,y+polovica)
    canvas.create_line(x+polovica,y+stvrtina,x+polovica,y+tristvrte)
    canvas.create_polygon(x,y,x+dlzka,y,x+polovica,y-polovica,)

def ulica(x,y,dlzka,pocet):
    farba1, farba2 = "red", "green"
    for i in range(pocet):
        dom(x,y,dlzka,farba1)
        farba1,farba2=farba2,farba1
        x+=dlzka+2
    



ulica(50,60,50,4)

tkinter.mainloop()