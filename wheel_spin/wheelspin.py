import tkinter as tk

input = input("vypis mena")
inputsplitnuty = input.split()

dlzkainputu = len(inputsplitnuty)

uhol =20
rychlost_kolesa = 1


zvacsovanie = 360/dlzkainputu
#for i in range(input):
    # platno.create_arc(100,100,300,300,start = 20 + zvacsovanie + uhol)


def _delete_():
    platno.delete("all")
def zvacsovanie_rychlosti():
    rychlost_kolesa+=1
    return rychlost_kolesa

def koleso():
    global uhol
    global zvacsovanie
    global dlzkainputu
    global rychlost_kolesa
    _delete_()
    platno.after(rychlost_kolesa,koleso)
    platno.after(15,zvacsovanie_rychlosti)
    print(rychlost_kolesa)
    for i in range(dlzkainputu):
        platno.create_arc(100,100,300,300,start = 20 + zvacsovanie + uhol,extent = 360/dlzkainputu)
        zvacsovanie+=360/dlzkainputu
    
    uhol+=1

    

    
    

okno = tk.Tk()
platno = tk.Canvas(okno,height = 400,width = 400)
platno.pack()


koleso()
    




tk.mainloop()