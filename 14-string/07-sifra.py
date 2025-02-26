#cézarova sifra ahoj bgpk vzdy sa zvacsi o 1
ret= input("zadaj text: ")
podmienka = int(input("ak chces sifrovat stlac 1 \n ak desifrovat stlac 2"))
cislo = 0
if podmienka == 1:
    for i in range(len(ret)):
        pismeno = chr((ord(ret[cislo])+1))
        cislo+=1
        print(pismeno)

   
        
else:
    print("zatial nic")
