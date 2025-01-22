import tkinter

canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

pocetstvorcov = int(input("zadaj počet štvorcov: "))

x= 250
y=250

farba1 = "yellow"
farba2 = "red"
farba3= "blue"

for i in range(10*pocetstvorcov,1,-10):
    canvas.create_rectangle(x-i,y-i,x+i,y+i,fill = farba1)
    farba1,farba2,farba3=farba2,farba3,farba1
    

    
    
    

    
    


tkinter.mainloop()