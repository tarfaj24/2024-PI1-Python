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
    

    def zrychli(self,kolko,farba_auta):
        self.rychlost+= kolko
        print(f"Auto {self.znacka} {self.farba} zrychlilo o {kolko}km/h na rýchlosť:{self.rychlost}km/h")
    
        graficke_zobrazenie = ("=" * self.rychlost)+ farba_auta
        print(graficke_zobrazenie)
        print(" " * ciel + "🏁 cieľ")


    def je_v_cieli(self,cielova_rychlost):
        return self.rychlost >= cielova_rychlost
auta = []
for i in range(pocet_aut):
    znacka = input("zadaj znacku auta: ")
    while True:
        try:
            farba = input("zadaj farbu auta (oranzova,cervena,modra,zelena,zlta): ")
            platne_farby = ["oranzova", "cervena", "modra", "zelena", "zlta"]

            if farba not in platne_farby:
                print("neplatna farba!")
                continue
            break
        except ValueError:
            print("zadaj spravnu farbu")
            
            
    auta.append(Auto(znacka,farba))
    
vitaz = None
kolo = 1
ciel = 100


while not vitaz:
    print(f"Kolo---{kolo}---")
    for auto in auta:
        nahodne_zrychlenie = random.randint(0,30)
        if auto.farba == "zelena":
            farba_auta = "🚜"
        elif auto.farba == "modra":
            farba_auta = "🚙"
        elif auto.farba == "cervena":
            farba_auta = "🚗"
        elif auto.farba == "oranzova":
            farba_auta = "🚚"
        elif auto.farba == "zlta":
            farba_auta = "🚕"

        auto.zrychli(nahodne_zrychlenie,farba_auta)
        if auto.je_v_cieli(ciel):
            vitaz = auto
        print()
    time.sleep(3)
    kolo+=1
    os.system('cls')

print(f"Víťazom sa stáva {vitaz.znacka} s rychlostou {vitaz.rychlost}km/h🏆")

    
    


    

