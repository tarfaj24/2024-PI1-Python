subor = open("subor.txt","r") #subor.txt je relatívna cesta k súboru (musí byť v tom istom priečinku ako samotný kód)
# open otvorí súbor subor.txt na čítanie, pre zápis sa používa "w" -write , "r" -read. Ak s=ubor neexistuje vypíše chybu
# subor = open("c:/dokumenty/subor.txt","r") -absolútna cesta 
# subor = open("../subor.txt","r").. je o priečinok vyššie

# for i in range(4):
#     riadok = subor.readline() # readline prečíta celý riadok (od miesta kde sa aktuálne nachádza) zo súboru a uloží do premennej riadok
#     print(riadok)

# riadok = subor.readline()
# while riadok != "":
#     print(riadok)
#     riadok = subor.readline()

while True:
    riadok = subor.readline()
    if riadok == "":
        break #break prerusi cyklus a vyskoci z neho
    print(riadok.strip()) #strip odstráni nečitateľné znaky napr. \n, \t

subor.close() #zatvorí súbor