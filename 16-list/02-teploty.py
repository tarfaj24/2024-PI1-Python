import random
teploty = []
pocet_dni = 30
#naplní list teploty náhodnými teplotami z rozsahu od 10 do 30
for i in range(pocet_dni):
    #teploty[i] = random.randint(10,30)  # vráti chybu, lebo prvky ešte neexistuju
    teploty.append(random.randint(10,30))

#vypíše list teploty
for i in range(pocet_dni):
    print(f"{i}.deň - {teploty[i]}°C")

# vypočíta a vypíše priemernú teplotu


sucet = 0
for i in range(pocet_dni):
    sucet+= teploty[i]
priemhodnota = sucet / pocet_dni
    
print(f"Priemerná teplota v mesiaci je {priemhodnota}°C")

for i in range(pocet_dni):
    if teploty[i] < priemhodnota:
        print(f"Deň s podriemernou teplotou: {i}.deň - {teploty[i]}°C")


