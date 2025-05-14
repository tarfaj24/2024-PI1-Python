#objekt auto

class Auto:
    def __init__(self,znacka,farba,):
        self.znacka = znacka
        self.farba = farba
        self.rychlost = 0
    

    def zrychli(self):
        self.rychlost+=10
        print(f"auto zrychlilo na:{self.rychlost}km/h")
    
    def spomal(self):
        if self.rychlost >= 10:
            self.rychlost -= 10
            print(f"auto spomalilo na {self.rychlost}km/h")
        else:
            print("auto uz stoji.")
    def stav(self):
        print(f"aktualna rychlost auta je:{self.rychlost}km/h")


    

        
moje_auto2 = Auto("BMW","modrá")
moje_auto = Auto("audi","červená")

print(moje_auto.znacka)
print(moje_auto.farba)
    
moje_auto.zrychli()
moje_auto.stav()
moje_auto.zrychli()
moje_auto.spomal()
moje_auto.spomal()
moje_auto.stav()
moje_auto.spomal()

moje_auto2.zrychli()
moje_auto2.zrychli()
moje_auto2.spomal()