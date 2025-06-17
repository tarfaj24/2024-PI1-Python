import tkinter as tk
import random

spustene = True

input = input("vypis mena")
inputsplitnuty = input.split()

dlzkainputu = len(inputsplitnuty)

uhol =random.randint(0,360)
rychlost_kolesa = 16

spomalovacia_premenna1 = 13.0
spomalovacia_premenna = 7.0

zvacsovanie = 360/dlzkainputu
tisicka = 1000
pocet_vykresleni= 0

def _delete_():
    platno.delete("all")

def tick(sekunda):
    sekunda+=1

# def spomal():
#     global uhol
#     global rychlost_kolesa
#     rychlost_kolesa = 30
#     platno.after(5000,spomal)
#     uhol -=30
#     print(uhol)

def koleso():
    global uhol
    global zvacsovanie
    global dlzkainputu
    global rychlost_kolesa
    global tisicka
    global pocet_vykresleni
    global spustene
    global spomalovacia_premenna
    global spomalovacia_premenna1

    if spustene == True:
        _delete_()
        platno.after(rychlost_kolesa,koleso)
        zvacsovanie=0
        for i in range(dlzkainputu):
            platno.create_arc(100,100,300,300,start = 20 + zvacsovanie + uhol,extent = 360/dlzkainputu)
            zvacsovanie+=360/dlzkainputu
        pocet_vykresleni+=1
        #print(pocet_vykresleni)
        
        #print(rychlost_kolesa)
        # if pocet_vykresleni>100:
        #     uhol-=50
        
        if pocet_vykresleni>100:
            spomalovacia_premenna-=0.025
            uhol+=spomalovacia_premenna

            
            if spomalovacia_premenna < 1:
                 spustene = False
            if uhol < 1:
                spustene = False
        else:
            spomalovacia_premenna1-=0.02
            uhol+=spomalovacia_premenna1

        print(uhol)


    


okno = tk.Tk()
platno = tk.Canvas(okno,height = 400,width = 400)
platno.pack()


koleso()




tk.mainloop()