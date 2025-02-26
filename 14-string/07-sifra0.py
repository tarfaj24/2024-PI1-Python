#cézarova sifra ahoj bgpk vzdy sa zvacsi o 1
 

ret= input("zadaj text: ")
podmienka = int(input("ak chces sifrovat stlac 1:  \nak desifrovat stlac 2:\n"))
cislo = 0
sifrslovo = ""

odsifcislo = 0
odsifrslovo = ""

if podmienka == 1:
    for pismeno in ret:
        sifcislo = (ord(pismeno)+1)
        sifpismeno = chr(sifcislo)
        sifrslovo += sifpismeno
    print(sifrslovo)

else:
    if podmienka == 2:
        for pismeno1 in ret:
            odsifcislo = (ord(pismeno1)-1)
            odsifpismeno = chr(odsifcislo)
            odsifrslovo += odsifpismeno
    print(odsifrslovo)
    

# pismeno = chr((ord(ret[cislo])+1))
#         cislo+=1
#         print(pismeno)