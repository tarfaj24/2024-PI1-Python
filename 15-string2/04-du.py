#uzivatel zada celu vetu a program vetu rozdeli na slova, ktore vypise nahodnou farbou na nahonom mieste
#aj pismenka zo slov vypise nahodnymi farbami
#test zo stringov znakove retazce ako retazec.count, retazec.find ...
import tkinter,random

canvas = tkinter.Canvas(height=400,width = 400)
canvas.pack()



def program():
    slovo = ""
    
    for znak in retazec.get():
        slovo = slovo + znak
        farba = f"#{random.randrange(256**3):06x}"

        if znak == " ":
            x = random.randint(30,370)
            y = random.randint(30,370)
            canvas.create_text(x,y,text= slovo,font="arial 15",fill = farba)
            
            slovo = ""
        else:
            print("teraz nie")
        x = random.randint(30,370)
        y = random.randint(30,370)
    canvas.create_text(x,y,text= slovo,font="arial 15",fill = farba)
        
tkinter.Label(text="zadaj vetu").pack()
retazec = tkinter.Entry()
retazec.pack()
tkinter.Button(text = "spusti program",command = program).pack()




tkinter.mainloop()