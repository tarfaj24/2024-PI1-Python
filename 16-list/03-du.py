#du vypis najnizsiu teplotu v mesiaci a najvyssiu bez pouzitia min a max

import random
teploty = []
pocet_dni = 30




for i in range(pocet_dni):
    teploty.append(random.randint(10,30))
    
def vypisteplot():
    for i in range(pocet_dni):
        print(f"{i}.deň - {teploty[i]}°C")

def max():
    najvyssiateplota = 0
    for i in range(pocet_dni):
        if teploty[i] > najvyssiateplota:
            najvyssiateplota = teploty[i]
    print(f"najvyssia teplota je: {najvyssiateplota}")

def min():
    najnizsiateplota = 31
    for i in range(pocet_dni):
        if teploty[i] < najnizsiateplota:
            najnizsiateplota = teploty[i]
    print(f"najnizsia teplota je: {najnizsiateplota}")
    
vypisteplot()
max()
min()
