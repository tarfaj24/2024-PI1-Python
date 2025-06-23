import tkinter as tk
import random
from PIL import Image, ImageDraw, ImageFont, ImageTk


argument_uhol1 =random.randint(0,360)

argument_spustene = True

input = input("vypis mena: ")
inputsplitnuty = input.split()

print(inputsplitnuty)

dlzkainputu_premenna = len(inputsplitnuty)


argument_spomalovacia_premenna1 = 13.0
spomalovacia_premenna = 7.0

zvacsovanie_premenna = 360/dlzkainputu_premenna
pocet_vykresleni_premenna = 0

def _delete_():
    platno.delete("all")

def tick(sekunda):
    sekunda+=1

def koleso(uhol,zvacsovanie,dlzkainputu,spomalovacia_premenna1,spomalovacia_premenna,spustene,pocet_vykresleni):

    if spustene == True:
        _delete_()
        platno.after(16,lambda: koleso(uhol,zvacsovanie,dlzkainputu,spomalovacia_premenna1,spomalovacia_premenna,spustene,pocet_vykresleni))
        zvacsovanie=0
        for i in range(dlzkainputu):
            platno.create_arc(10,10,390,390,start = zvacsovanie + uhol,extent = 360/dlzkainputu)
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

        


    


okno = tk.Tk()
platno = tk.Canvas(okno,height = 400,width = 400)
platno.pack()



koleso(argument_uhol1,zvacsovanie_premenna,dlzkainputu_premenna,argument_spomalovacia_premenna1,spomalovacia_premenna,argument_spustene,pocet_vykresleni_premenna)




tk.mainloop()