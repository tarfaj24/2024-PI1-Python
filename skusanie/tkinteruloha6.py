import tkinter,random

canvas = tkinter.Canvas(height=320,width=320)
canvas.pack()

pocetdomcekov= int(input("kolko chces farebnych domcekov?: "))

def domcek(x,y):
    dlzka = random.randrange(10,50)
    farbastrechy= f"#{random.randrange(256**3):06x}"
    farbadomu = f"#{random.randrange(256**3):06x}"
    canvas.create_rectangle(x,y,x+dlzka,y+dlzka,fill=farbadomu,width=0)
    canvas.create_polygon(x, y, x + dlzka, y, x + dlzka / 2, y - ((dlzka**2-(dlzka/2)**2)**(1/2)), fill=farbastrechy)



for i in range(pocetdomcekov):
    x = random.randrange(3,320-53)
    y = random.randrange(33,320-53)
    domcek(x,y) 

tkinter.mainloop()