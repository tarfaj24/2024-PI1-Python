import tkinter
import random
sirkaplatna = int(input("Zadaj sirku platna: "))
vyskaplatna = int(input("Zadaj vysku platna: "))



canvas = tkinter.Canvas(width=sirkaplatna, height=vyskaplatna)
canvas.pack()

for i in range(100):
    dlzka = 10
    x = random.randint(3, sirkaplatna -3)
    y = random.randint(3,vyskaplatna - 3)

#     if (x < sirkaplatna / 2) and (y < vyskaplatna /2): # zlozena podmienka, tzn testujeme viac vlastnosti
#         # medzi zlozene podmienky vkladame logicke operatory (and = a zaroven, or = alebo)
#         farba = "blue"
#     elif (x > sirkaplatna / 2) and (y > vyskaplatna / 2):
#         farba = "yellow"
#     elif (x > sirkaplatna / 2) and (y < vyskaplatna /2):
#         farba = "red"
#     elif (x < sirkaplatna / 2) and (y > vyskaplatna /2):
#         farba = "green"

            
    if x > sirkaplatna / 2:
            if y < vyskaplatna / 2:
                farba = "blue"
            else:
                farba = "green"
    else:
        if y < vyskaplatna / 2:
              farba = "red"
        else:
             farba = "yellow"

        
    
             
    
    
    
    canvas.create_oval(x,y,x+dlzka,y+dlzka, fill = farba, width = 0)

tkinter.mainloop()



