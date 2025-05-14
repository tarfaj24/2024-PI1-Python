import random 
import time
import os

while True:
    try:
        pocet_aut = int(input("zadaj počet áut: "))
        if pocet_aut < 1:
            print("auto musí byť aspoň jedno")
            continue
        if pocet_aut > 5:
            print("5 je maximalny pocet aut")
        break
    except ValueError:
        print("Zadaj platné číslo")


class Auto:
    def __init__(self,znacka,farba,):
        self.znacka = znacka
        self.farba = farba
        self.rychlost = 0
    

    def zrychli(self,kolko):
        self.rychlost+= kolko
        print(f"Auto {self.znacka} {farba} zrychlilo o {kolko}km/h na rýchlosť:{self.rychlost}km/h")
        if farba == "zelena":
            graficke_zobrazenie = ("=" * self.rychlost)+ "🚜"
        elif farba == "cervena":
            graficke_zobrazenie = ("=" * self.rychlost)+ "🚗"
        elif farba == "modra":
             graficke_zobrazenie = ("=" * self.rychlost)+ "🚙"
             
        print(graficke_zobrazenie)
        print(("-"*ciel)+"ciel🏁")

    def je_v_cieli(self,cielova_rychlost):
        return self.rychlost >= cielova_rychlost
auta = []
for i in range(pocet_aut):
    znacka = input("zadaj znacku auta: ")
    farba = input("zadaj farbu auta: ")
    auta.append(Auto(znacka,"farba"))
    
vitaz = None
kolo = 1
ciel = 100


while not vitaz:
    print(f"Kolo---{kolo}---")
    for auto in auta:
        nahodne_zrychlenie = random.randint(0,30)
        auto.zrychli(nahodne_zrychlenie)
        if auto.je_v_cieli(ciel):
            vitaz = auto
        print()
    time.sleep(3)
    kolo+=1
    os.system('cls' if os.name == 'nt' else 'clear')

print(f"Víťazom sa stáva {vitaz.znacka} s rychlostou {vitaz.rychlost}km/h🏆")

    
    


    

