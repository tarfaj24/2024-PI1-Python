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

     
    if (x > sirkaplatna / 4) and (y > sirkaplatna):
         farba = "black"
    elif (x < sirkaplatna -  sirkaplatna - (1/4) * sirkaplatna) and (y < vyskaplatna - (1/4) * vyskaplatna):
         farba = "black"
        
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